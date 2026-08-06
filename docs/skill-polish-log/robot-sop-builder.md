# Polish log — `robot-sop-builder` / `robot-sop-checklist-reviewer`

## 2026-08-06 (pair pass)

**Picked because:** open issue [#43](https://github.com/jherrodthomas/robotics-skills-suite/issues/43) — W31→W32 carryover, target 2 in `docs/weekly/WEEK-2026-W32.md`, and the plan says work strictly in order. Target 1 (#42, fleet-manager reviewer) landed 2026-08-05, so #43 is next. No issue in the repo carries `skill-bug` or `reviewer-finding`, and there are no orphan builders (38/38 paired), so the weekly plan governed the pick. Both files were also still at the 2026-05-03 import baseline.

**Scope:** `robot-sop-builder.skill` and `robot-sop-checklist-reviewer.skill`, edited in lockstep.

**What's good**
- Frontmatter clean on both: single `name` + `description`, both well under 1024 chars.
- The 10-tab SOP structure is genuinely well chosen — it separates planned stop from emergency response, which is the distinction most real cell SOPs blur.
- Package layout matches the repo convention (`SKILL.md` + `scripts/` + `scripts/office/`).

**What was fixed this pass (small, applied)**
- MED (standards): neither skill cited a standard edition. The description said only "OSHA 1910" and "ISO 10218-2". Added a **Governing standards** table to both and edition strings to both descriptions:
  - **ANSI/A3 R15.06-3-2025** — verified this run: A3 published the revised R15.06 as a three-part standard, a US national adoption of ISO 10218-1:2025 / -2:2025. Parts 1 and 2 approved 2025-08-21; **Part 3 approved 2025-10-07**. Part 3 covers *use of industrial robot cells* — operating procedures, operator tasks, manual load/unload. That is precisely this skill's subject matter, so Part 3 is now the primary anchor rather than the generic ISO 10218-2 reference. First major R15.06 revision in ~15 years; supersedes ANSI/RIA R15.06-2012.
  - **ISO 10218-2:2025**, **OSHA 29 CFR 1910.147** (LOTO), **1910.132** (PPE), **1910.212** (guarding) — "OSHA 1910" alone was too coarse to be auditable; the specific parts are now named against the tabs that rely on them.
- MED: added a boundary note that energy-isolation detail belongs in `loto-procedure-builder` output and should be *referenced*, not duplicated, by the SOP. Duplicated LOTO text drifting out of sync between two documents is a real failure mode in this domain.
- MED (chain-break, same defect class as #42): the reviewer shipped `scripts/robot-sop-checklist_probe.py`. Hyphens make that un-importable as a Python module. Renamed to `robot_sop_probe.py` and corrected the documented file tree — same fix applied to the fleet-manager reviewer on 2026-08-05.
- LOW: both SKILL.md bodies were four-line placeholders with no "When to use", no workflow, and no file tree. Rewrote both to the house structure established by `fleet-manager-architecture-builder`. Reviewer review-scope section now maps its checks 1:1 onto the builder's 10 tabs, so the pair is documented in lockstep.
- LOW: added `examples/robot-sop-builder/README.md` and `examples/robot-sop-checklist-reviewer/README.md` stubs (neither existed).
- Added an explicit "Known gap" line to both SKILL.md files so the missing implementation is visible to a user of the skill, not just to this log.

**Still to fix (not applied — beyond small-fix scope)**
- HIGH: **the builder ships no generator script at all.** `scripts/` contains only `recalc.py` and `office/`. Every other builder in the suite has a `generate_*.py`. This is worse than the placeholder-generator problem tracked on fleet-manager and behavior-tree — there is nothing to run. Needs a dedicated implementation session.
- HIGH: reviewer `robot_sop_probe.py`, `check_definitions.py`, and `dashboard.py` are all one-line stubs. Zero checks implemented.
- MED: once the generator exists, verify the SOP's emergency-response tab against R15.06-3-2025's operator-task clauses rather than the generic framing used here — the 2025 revision added content on end-effectors and manual load/unload that a run book should reflect.
- LOW: `sample_input.json` / `sample_output.xlsx` promised by the new example stubs do not exist yet.

**Severity:** medium (documentation and standards accuracy restored across the pair; the absent generator remains the blocking defect and is the reason #43 should stay open)

**Sources for the standards verification**
- https://www.automate.org/robotics/news/new-ansi-a3-r15-06-2025-american-national-standard-for-industrial-robot-safety-now-available-for-purchase
- https://www.therobotreport.com/now-available-full-403-page-ansi-a3-r15-06-2025-robot-safety-standard/
- https://blog.ansi.org/ansi/ansi-a3-r15-06-2025-robot-safety/
