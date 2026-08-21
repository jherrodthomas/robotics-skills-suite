#!/usr/bin/env python3
"""Regenerate STATUS.md for robotics-skills-suite.

Run from the repo root:

    python3 scripts/gen_status.py            # uses today's date
    python3 scripts/gen_status.py 2026-08-21 # pin the date (for reproducible runs)

Committed deliberately. The daily standup task used to rebuild this generator
from scratch in /tmp on every run, and the same two defects were re-introduced
three times (see docs/AUTONOMOUS_LOG.md, 2026-08-17 / 2026-08-19 / 2026-08-21):

  1. Domain inference matched builder *stems* against dash-terminated prefixes,
     so any stem ending exactly at the prefix boundary -- `pfl-plan`,
     `ssm-plan`, `robot-sop`, `eoat-spec` and six others -- fell through to
     "unclassified". Fixed by matching the full filename.
  2. A skill edited in the working tree but not yet committed showed its
     previous commit date, so the skill polished by a run appeared stale in the
     STATUS committed by that same run. Fixed by treating dirty files as
     touched today.

Edit this file rather than re-deriving the logic.
"""

import collections
import datetime
import os
import subprocess
import sys

SKILLS_DIR = "skills"
OUT = "STATUS.md"
STALE_DAYS = 30

# Prefix -> domain. Matched against the full builder filename.
DOMAIN_RULES = [
    (("iso12100-", "machinery-safety-lifecycle-plan-", "robot-cell-scope-"), "foundation"),
    (("iso13849-", "iec62061-", "iso10218-", "ansi-r1506-", "declaration-of-conformity-"), "compliance"),
    (("iso15066-", "ssm-plan-", "pfl-plan-", "cobot-"), "cobot"),
    (("iso3691-", "operating-envelope-", "fleet-manager-", "wireless-coexistence-"), "amr"),
    (("robot-cell-layout-", "eoat-", "safety-io-", "interlock-estop-"), "cell-design"),
    (("robot-sop-", "loto-procedure-", "operator-training-"), "operational"),
    (("ros2-", "urdf-", "behavior-tree-", "nav2-", "tf-tree-"), "ros2"),
    (("iso9283-", "robot-acceptance-", "robot-hil-", "robot-field-"), "v&v"),
    (("dataset-documentation-", "model-card-", "perception-test-"), "ai-ml"),
    (("iec62443-", "ot-asset-", "zone-conduit-"), "cybersecurity"),
]


def domain(filename):
    for prefixes, name in DOMAIN_RULES:
        if any(filename.startswith(p) for p in prefixes):
            return name
    return "unclassified"


def dirty_paths():
    out = subprocess.run(["git", "status", "--porcelain", "--", SKILLS_DIR],
                         capture_output=True, text=True).stdout
    return {line[3:].strip() for line in out.splitlines() if line.strip()}


def last_touched(filename, dirty, today):
    """Commit date of the last change, or today if the file is modified in-tree."""
    path = f"{SKILLS_DIR}/{filename}"
    if path in dirty:
        return today.isoformat()
    return subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short", "--", path],
                          capture_output=True, text=True).stdout.strip() or "unknown"


def main():
    today = (datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1
             else datetime.date.today())
    dirty = dirty_paths()

    files = sorted(os.listdir(SKILLS_DIR))
    builders = [f for f in files if f.endswith("-builder.skill")]
    reviewers = {f for f in files if f.endswith("-reviewer.skill")}

    rows = []
    for b in builders:
        stem = b[: -len("-builder.skill")]
        rev = next((c for c in (f"{stem}-checklist-reviewer.skill", f"{stem}-reviewer.skill")
                    if c in reviewers), None)
        touched = last_touched(b, dirty, today)
        if rev is None:
            flag = "🔴 missing paired reviewer"
        elif touched == "unknown":
            flag = "🟡 stale — never committed"
        else:
            age = (today - datetime.date.fromisoformat(touched)).days
            flag = (f"🟢 paired, {age}d" if age <= STALE_DAYS
                    else f"🟡 stale — {age}d since touch")
        rows.append((b, domain(b), rev, touched, flag))

    rows.sort(key=lambda r: (r[1], r[0]))

    unclassified = [r[0] for r in rows if r[1] == "unclassified"]
    if unclassified:
        sys.stderr.write("WARNING: unclassified builders (add a DOMAIN_RULES prefix): "
                         + ", ".join(unclassified) + "\n")

    green = sum(r[4].startswith("🟢") for r in rows)
    yellow = sum(r[4].startswith("🟡") for r in rows)
    red = sum(r[4].startswith("🔴") for r in rows)
    paired = sum(r[2] is not None for r in rows)
    spread = collections.Counter(r[1] for r in rows)

    lines = [
        "# STATUS — robotics-skills-suite\n",
        f"_Auto-generated {today.isoformat()} by the daily standup task via "
        "`scripts/gen_status.py`. Do not edit by hand — regenerated every run._\n",
        "| Builder | Domain | Paired Reviewer | Last Touched | Flag |",
        "| --- | --- | --- | --- | --- |",
    ]
    for b, dom, rev, touched, flag in rows:
        lines.append(f"| `{b}` | {dom} | " + (f"`{rev}`" if rev else "—")
                     + f" | {touched} | {flag} |")
    lines += [
        "",
        "## Summary\n",
        f"- **Inventory:** {len(builders)} builders · {len(reviewers)} reviewers · "
        f"{len(files)} .skill files total",
        f"- **Pairing:** {paired}/{len(builders)} builders paired "
        f"({round(100 * paired / len(builders))}%) · {red} orphan builders 🔴 · "
        f"{len(reviewers) - paired} unpaired reviewers",
        f"- **Freshness:** {green} builders 🟢 touched ≤{STALE_DAYS}d · "
        f"{yellow} builders 🟡 stale at {STALE_DAYS}+d",
        "- **Domain spread:** " + " · ".join(f"{k} {spread[k]}" for k in sorted(spread)),
        f"- **Health:** {'no orphans' if red == 0 else f'{red} orphan builders'}; "
        f"staleness is the open debt — {yellow} builders await a POLISH pass.",
        "",
    ]
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"{OUT}: {len(rows)} builders · {green} green · {yellow} yellow · {red} red")


if __name__ == "__main__":
    main()
