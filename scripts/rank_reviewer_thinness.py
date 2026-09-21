#!/usr/bin/env python3
"""Rank pairs by reviewer thinness -- the successor selector to builder thinness.

Run from the repo root:

    python3 scripts/rank_reviewer_thinness.py

Why this exists
---------------
Builder-thinness (the "inverted pair" measure: reviewer body longer than builder
body) drove target selection from W33 to W38 and was **exhausted** on 2026-09-16
when `robot-field-acceptance`, the last inverted pair, was polished. Three
consecutive journal entries (2026-09-08, 09-15, 09-16) asked for a successor
ranking to be stood up. This is it, committed rather than re-derived weekly, for
the same reason `gen_status.py` is committed: a measure re-invented in scratch
space every run re-introduces its own defects.

The measure, and the trap it avoids
-----------------------------------
The obvious formulation -- sort by ``reviewer_body - builder_body`` -- is wrong,
and the first run of this ranking (2026-09-21) proved it. That delta is
dominated by *recently polished* pairs: `dataset-documentation` tops the delta
sort at -42 only because its builder was grown to 109 lines, while its reviewer
at 67 lines is one of the most substantial in the repo. Delta measures
imbalance; it does not measure thinness.

**Absolute reviewer body size is the signal.** A reviewer under ~15 body lines
cannot be stating rated checks -- it is stating a topic list. The 2026-09-21 run
found `robot-cell-layout-checklist-reviewer` at **6 body lines** (one sentence
of purpose plus a 3-item Standards list, zero checks) against a 33-line builder;
delta ranked it 4th, absolute size ranked it 1st, and reading the file confirmed
absolute size was right.

Both columns are printed. Sort on ABSOLUTE. Use DELTA only as a tie-breaker.

Line counts are a proxy and the last step is always to read the file: a short
reviewer that names real checks and dates its standards (`safety-io-matrix`, 13
lines) is healthier than a longer one that lists topics.
"""

import glob
import os
import sys
import zipfile

SKILLS_DIR = "skills"
THIN_THRESHOLD = 15  # body lines below which a reviewer cannot be stating checks


def body_lines(path):
    """Non-blank body lines of the archive's SKILL.md, frontmatter stripped."""
    try:
        z = zipfile.ZipFile(path)
    except (OSError, zipfile.BadZipFile):
        return None
    names = [n for n in z.namelist() if n.endswith("SKILL.md")]
    if not names:
        return None
    text = z.read(sorted(names, key=len)[0]).decode("utf-8", "replace")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) > 2:
            text = parts[2]
    return sum(1 for line in text.splitlines() if line.strip())


def reviewer_for(stem):
    for suffix in ("-checklist-reviewer.skill", "-reviewer.skill"):
        path = os.path.join(SKILLS_DIR, stem + suffix)
        if os.path.exists(path):
            return path
    return None


def main():
    rows = []
    unreadable = []
    for builder in sorted(glob.glob(os.path.join(SKILLS_DIR, "*-builder.skill"))):
        stem = os.path.basename(builder)[: -len("-builder.skill")]
        reviewer = reviewer_for(stem)
        if reviewer is None:
            unreadable.append((stem, "no paired reviewer"))
            continue
        b, r = body_lines(builder), body_lines(reviewer)
        if b is None or r is None:
            unreadable.append((stem, "unreadable archive or missing SKILL.md"))
            continue
        rows.append((stem, b, r, r - b))

    rows.sort(key=lambda x: (x[2], x[3]))  # ABSOLUTE reviewer size, then delta

    print(f"{'pair':<48} {'bldr':>5} {'revw':>5} {'delta':>6}  flag")
    print("-" * 76)
    for stem, b, r, d in rows:
        flag = "THIN -- cannot be stating checks" if r < THIN_THRESHOLD else ""
        print(f"{stem:<48} {b:5} {r:5} {d:+6}  {flag}")

    thin = [x for x in rows if x[2] < THIN_THRESHOLD]
    print()
    print(f"pairs ranked            : {len(rows)}")
    print(f"reviewers under {THIN_THRESHOLD} lines : {len(thin)}")
    if thin:
        print("next targets (thinnest first): " + ", ".join(x[0] for x in thin[:5]))
    for stem, why in unreadable:
        print(f"SKIPPED {stem}: {why}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
