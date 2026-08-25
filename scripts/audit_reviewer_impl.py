#!/usr/bin/env python3
"""Audit the *implementation* tier of every reviewer skill in skills/.

Run from the repo root:

    python3 scripts/audit_reviewer_impl.py           # table + summary
    python3 scripts/audit_reviewer_impl.py --tier C  # list one tier only

Committed deliberately, for the same reason as gen_status.py.

Background (docs/AUTONOMOUS_LOG.md, 2026-08-25): the "placeholder-generator
defect" had been recorded in the weekly plans as affecting four skills. It does
not. Scanning all 38 reviewers showed that only 6 carry a real checklist
generator; the other 32 either ship a stub or ship no generator at all, while
every one of the 38 SKILL.md bodies instructs the reader to run
`python scripts/generate_checklist.py` and advertises a `references/` directory
that exists in none of the archives.

That matters because the weekly POLISH programme rewrites reviewer
*descriptions*. A description promising detailed verification against dated
standards is a promise the package may have no code to keep. Run this before
picking a POLISH target so the choice is made with the tier visible.

Tiers
-----
A  implemented   generate_checklist.py present and carries a real check table
B  stub          generate_checklist.py present but writes placeholder output.
                 These are the misleading ones: their SKILL.md documents a
                 Workflow, a 7-tab output table and a references/ directory
                 that the stub does not produce and the archive does not hold.
C  absent        no generate_checklist.py at all. Not the same defect: these
                 ship a leaner prose body that documents the checks narratively
                 and never claims a runnable script.

.skill files are zip archives; this reads them in place without unpacking.
"""

import argparse
import glob
import os
import re
import sys
import zipfile

# A real generator carries a check table; stubs announce themselves in the
# docstring or in what they print. Do not match the bare word "placeholder":
# two genuine generators use it inside a legitimate check string ("Author and
# approver names filled (not placeholders)") and were misclassified as stubs.
REAL_GENERATOR_MIN_BYTES = 3000
STUB_MARKERS = (
    "Placeholder: implement",
    "Placeholder: generate",
    '- Placeholder"',
)


def _read(zf, suffix):
    """Return (name, text) for the single member ending in suffix, or (None, '')."""
    hits = [n for n in zf.namelist() if n.endswith(suffix) and not n.endswith("/")]
    if len(hits) != 1:
        return None, ""
    return hits[0], zf.read(hits[0]).decode("utf-8", "replace")


def classify(path):
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        gen_name, gen = _read(zf, "scripts/generate_checklist.py")
        _, chk = _read(zf, "scripts/check_definitions.py")
        _, skill_md = _read(zf, "SKILL.md")

        has_refs = any("/references/" in n for n in names)
        cites_gen = "generate_checklist.py" in skill_md
        cites_refs = "references/" in skill_md

        if gen_name is None:
            tier = "C"
        elif len(gen) >= REAL_GENERATOR_MIN_BYTES and not any(
            m in gen for m in STUB_MARKERS
        ):
            tier = "A"
        else:
            tier = "B"

        # A populated check table is what makes findings reproducible.
        n_checks = len(re.findall(r'"id"\s*:\s*"', gen)) if gen else 0

        return {
            "name": os.path.basename(path)[: -len(".skill")],
            "tier": tier,
            "gen_bytes": len(gen),
            "checkdef_bytes": len(chk.strip()),
            "n_checks": n_checks,
            "has_refs": has_refs,
            "cites_gen": cites_gen,
            "cites_refs": cites_refs,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["A", "B", "C"], help="list only this tier")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    args = ap.parse_args()

    paths = sorted(
        set(glob.glob("skills/*-checklist-reviewer.skill"))
        | set(glob.glob("skills/*-reviewer.skill"))
    )
    if not paths:
        sys.exit("no reviewer skills found - run from the repo root")

    rows = [classify(p) for p in paths]

    if args.tier:
        for r in rows:
            if r["tier"] == args.tier:
                print(r["name"])
        return 0

    if not args.quiet:
        print(f"{'reviewer':<52} {'tier':<5} {'gen B':>7} {'checks':>7} {'refs/':>6}")
        print("-" * 82)
        for r in rows:
            print(
                f"{r['name']:<52} {r['tier']:<5} {r['gen_bytes']:>7} "
                f"{r['n_checks']:>7} {'yes' if r['has_refs'] else 'NO':>6}"
            )
        print()

    tally = {t: sum(1 for r in rows if r["tier"] == t) for t in "ABC"}
    broken_gen = sum(1 for r in rows if r["cites_gen"] and r["tier"] == "C")
    broken_refs = sum(1 for r in rows if r["cites_refs"] and not r["has_refs"])

    print(f"reviewers scanned          : {len(rows)}")
    print(f"tier A (implemented)       : {tally['A']}")
    print(f"tier B (stub generator)    : {tally['B']}")
    print(f"tier C (no generator)      : {tally['C']}")
    print(f"SKILL.md cites a generator that is not in the archive : {broken_gen}")
    print(f"SKILL.md cites references/ that is not in the archive  : {broken_refs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
