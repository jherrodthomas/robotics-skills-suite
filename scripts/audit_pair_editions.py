#!/usr/bin/env python3
"""Audit builder<->reviewer standard-edition agreement across all pairs.

Run from the repo root:

    python3 scripts/audit_pair_editions.py            # full report
    python3 scripts/audit_pair_editions.py --mismatch # hard mismatches only

Committed deliberately, for the same reason as scripts/gen_status.py.

The 2026-08-23 TRIAGE run found that four of five compliance pairs had a
builder anchored to a current standard edition and a reviewer left behind on a
superseded one. Each file was internally consistent, so neither half read alone
looks wrong -- the defect only exists in the gap between them. That audit was
run by hand against five pairs and W35 flagged extending it to all 38 as the
highest-value unclaimed job in the repo. This script is that extension.

Two classes are reported, and they are NOT the same severity:

  MISMATCH   both halves cite the standard, with different years. Usually real,
             but read the context before filing: a builder that says
             "ISO 10218-2:2025 supersedes ISO 10218-2:2011" legitimately
             contains both years. The 2026-08-31 run's only mismatch
             (robot-cell-scope) was exactly this benign shape.

  ASYMMETRY  one half pins an edition and the other names the standard with no
             year. Lower severity, higher volume. It is not a wrong claim, it
             is a missing one -- and it is the state a pair passes through on
             its way to drifting, because the unpinned half is free to be read
             against whatever edition the reader assumes.

Skills are zip archives (`<name>/SKILL.md` plus scripts), not plain files, so
every read goes through zipfile. A previous ad-hoc version of this check read
the .skill files as text, matched nothing at all, and reported a clean repo.
That false negative is why this file exists rather than being retyped each run.
"""

import glob
import os
import re
import sys
import zipfile
from collections import defaultdict

SKILLS_DIR = "skills"

# (label, regex capturing the 4-digit edition year)
PATTERNS = [
    ("ISO 10218-1",     r"ISO\s*10218-1[\s:\u2013-]*(\d{4})"),
    ("ISO 10218-2",     r"ISO\s*10218-2[\s:\u2013-]*(\d{4})"),
    ("ISO 10218",       r"ISO\s*10218(?!-)[\s:\u2013-]*(\d{4})"),
    ("ISO 13849-1",     r"ISO\s*13849-1[\s:\u2013-]*(\d{4})"),
    ("ISO 13849-2",     r"ISO\s*13849-2[\s:\u2013-]*(\d{4})"),
    ("IEC 62061",       r"IEC\s*62061[\s:\u2013-]*(\d{4})"),
    ("ISO 12100",       r"ISO\s*12100[\s:\u2013-]*(\d{4})"),
    ("ISO/TS 15066",    r"ISO/?TS\s*15066[\s:\u2013-]*(\d{4})"),
    ("ISO 3691-4",      r"ISO\s*3691-4[\s:\u2013-]*(\d{4})"),
    ("ISO 9283",        r"ISO\s*9283[\s:\u2013-]*(\d{4})"),
    ("ANSI R15.06",     r"R15\.06[\s:\u2013-]*(\d{4})"),
    ("IEC 62443",       r"IEC\s*62443(?:-\d(?:-\d)?)?[\s:\u2013-]*(\d{4})"),
    ("EU MR 2023/1230", r"(?:Machinery Regulation|Regulation)\s*\(?EU\)?\s*(20\d\d)/1230"),
    ("IEC 61508",       r"IEC\s*61508(?:-\d)?[\s:\u2013-]*(\d{4})"),
    ("ISO 13855",       r"ISO\s*13855[\s:\u2013-]*(\d{4})"),
    ("ISO 13857",       r"ISO\s*13857[\s:\u2013-]*(\d{4})"),
    ("ISO 14119",       r"ISO\s*14119[\s:\u2013-]*(\d{4})"),
    ("ISO 13850",       r"ISO\s*13850[\s:\u2013-]*(\d{4})"),
    ("ISO 11161",       r"ISO\s*11161[\s:\u2013-]*(\d{4})"),
    ("IEC 61496",       r"IEC\s*61496(?:-\d)?[\s:\u2013-]*(\d{4})"),
]


def read_skill(path):
    """Concatenate every text member of a .skill zip."""
    chunks = []
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if name.endswith("/"):
                continue
            try:
                chunks.append(z.read(name).decode("utf-8", "replace"))
            except Exception:
                pass
    return "\n".join(chunks)


def editions(text):
    found = defaultdict(set)
    for label, pattern in PATTERNS:
        for m in re.finditer(pattern, text, re.I):
            found[label].add(m.group(1))
    return found


def find_reviewer(stem):
    for suffix in ("checklist-reviewer", "reviewer"):
        path = os.path.join(SKILLS_DIR, f"{stem}-{suffix}.skill")
        if os.path.exists(path):
            return path
    return None


def audit():
    results = []
    for builder in sorted(glob.glob(os.path.join(SKILLS_DIR, "*-builder.skill"))):
        stem = os.path.basename(builder)[: -len("-builder.skill")]
        reviewer = find_reviewer(stem)
        if reviewer is None:
            results.append((stem, [("ORPHAN", "no paired reviewer")]))
            continue
        be = editions(read_skill(builder))
        re_ = editions(read_skill(reviewer))
        issues = []
        for std in sorted(set(be) | set(re_)):
            bv, rv = be.get(std, set()), re_.get(std, set())
            if bv and rv and bv != rv:
                issues.append(("MISMATCH",
                               f"{std}: builder {sorted(bv)} vs reviewer {sorted(rv)}"))
            elif bv and not rv:
                issues.append(("ASYMMETRY",
                               f"{std}: builder pins {sorted(bv)}, reviewer unpinned"))
            elif rv and not bv:
                issues.append(("ASYMMETRY",
                               f"{std}: reviewer pins {sorted(rv)}, builder unpinned"))
        results.append((stem, issues))
    return results


def main():
    only_mismatch = "--mismatch" in sys.argv
    results = audit()
    mismatch = [r for r in results if any(k == "MISMATCH" for k, _ in r[1])]
    asym = [r for r in results if any(k == "ASYMMETRY" for k, _ in r[1])]

    print(f"pairs scanned: {len(results)} | "
          f"MISMATCH: {len(mismatch)} | ASYMMETRY: {len(asym)}")

    print("\n===== MISMATCH (both halves pin, years differ) =====")
    if not mismatch:
        print("  none")
    for stem, issues in mismatch:
        print(f"\n### {stem}")
        for kind, text in issues:
            if kind == "MISMATCH":
                print("   *", text)

    if only_mismatch:
        return 0

    print("\n===== ASYMMETRY (one half unpinned) =====")
    if not asym:
        print("  none")
    for stem, issues in asym:
        lines = [t for k, t in issues if k == "ASYMMETRY"]
        if lines:
            print(f"\n### {stem}")
            for text in lines:
                print("   -", text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
