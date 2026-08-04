# robot-cell-scope-builder / robot-cell-scope-checklist-reviewer — polish log

## 2026-08-04 (autonomous POLISH, issue #46)

**Domain:** foundation (safety-critical — standard editions verified)
**Severity:** **high**

### What's good

- The builder's frontmatter description was already substantive and specific: it named the actual content of the artifact (physical boundaries, robot inventory, peripherals, operational modes, intended use, foreseeable misuse, stakeholder roles) rather than restating the skill name.
- The pair is intact — builder and checklist reviewer both present, consistent naming.
- The reviewer's 7-tab output table was accurate and matches the house reviewer layout used across the suite.
- `recalc.py` and the `office/` helpers are the shared real implementations, not stubs.

### What was wrong

1. **Reviewer description was a copy-paste of the builder description (HIGH).** It read "Generate an audit-ready Robot Cell Scope and Boundary document workbook … Use this skill to review the user mentions robot cell scope …" — describing *generation*, with a broken trigger clause. A user asking to *build* a cell scope document could plausibly have fired the reviewer, and a user asking to *review* one had no matching trigger language. This is the single highest-value fix in this pass.
2. **Stale standard editions (HIGH, safety-critical domain).** Both skills cited bare "ISO 10218-2" and "ANSI R15.06" with no edition year. Verified current editions:
   - **ISO 10218-2:2025** (Edition 2) supersedes ISO 10218-2:2011; **ISO 10218-1:2025** is Edition 3.
   - **ANSI/A3 R15.06-2025** — US national adoption of both parts, approved 21 Aug 2025, published Sept 2025. Supersedes **ANSI/RIA R15.06-2012**. Note the *designation change from RIA to A3* — the suite has been writing "ANSI R15.06" / "ANSI/RIA R15.06" throughout.
   - The 2025 editions consolidate collaborative-application content formerly in **ISO/TS 15066:2016**, and replace the term *safety-rated monitored stop* with **monitored standstill**.
3. **Placeholder boilerplate in the builder body (MED).** "Use this skill when the user mentions robot-cell, or related requirements" and "The generated workbook contains multiple tabs organized by assessment category" — both contentless import artifacts. H1 was "Robot Cell Builder", dropping "Scope".
4. **Files tree did not match archive contents (MED).** Both SKILL.md files documented a `references/` directory with `methodology.md` and a conventions/checks file. Neither archive contains a `references/` directory at all.
5. **Leaked absolute path from an unrelated project (MED, hygiene).** `generate_robot-cell.py` carried the comment `See /sessions/vigilant-ecstatic-maxwell/mnt/CL work/automotive-skills-suite/source/hara-builder/scripts/generate_hara.py for reference pattern` — a session path from the automotive suite. Worth grepping the other 74 archives for the same leak.
6. **Three redundant probe scripts in the reviewer (LOW).** `probe_workbook.py`, `robot-cell_probe.py`, and `robot-cell-scope-checklist_probe.py` all exist; all three are empty stubs, and SKILL.md documented only the middle one.
7. **Generator filename is not importable (LOW).** `generate_robot-cell.py` — a hyphen makes the module un-importable. Convention elsewhere in the suite uses underscores.

### Applied this pass

- Rewrote the **reviewer description** to describe reviewing, with correct trigger language and a "does not modify the source workbook" clause, matching the house reviewer pattern.
- Anchored both skills on **ISO 10218-2:2025 / ISO 10218-1:2025 / ANSI/A3 R15.06-2025**, in frontmatter and in a new "Standards baseline" section.
- Added an explicit reviewer check instruction: flag source workbooks still citing ISO 10218-2:2011, ANSI/RIA R15.06-2012, or "safety-rated monitored stop".
- Replaced the builder's placeholder "When to use" and "Output structure" sections with real content; corrected both H1 titles.
- Corrected both files trees to match actual archive contents; added stub-status notes in the house `> **Note:**` style.
- Removed the leaked `/sessions/vigilant-ecstatic-maxwell/...` path from the generator stub.

### Not applied — deliberately descoped

- Implementing the actual generator and checklist logic (both are stubs). Out of scope for a polish pass.
- Renaming `generate_robot-cell.py` → `generate_robot_cell_scope.py`.
- Deleting the two redundant probe stubs.

### Follow-ups

- **Suite-wide:** grep all 76 archives for `/sessions/` absolute paths and for bare `ANSI R15.06` / `ANSI/RIA R15.06` / `ISO 10218-*:2011`. The RIA→A3 designation change likely affects `ansi-r1506-compliance-matrix-*` and `iso10218-compliance-matrix-*` directly.
- **Cobot domain:** ISO/TS 15066:2016 content is now folded into the 2025 editions. `iso15066-biomechanical-limits-*`, `pfl-plan-*`, and `ssm-plan-*` still treat TS 15066 as the governing source and should be re-framed as informative background. Worth a dedicated weekly target.
- **Terminology:** "safety-rated monitored stop" → "monitored standstill" across the cobot and cell-design domains.
- Audit how many other builders still carry the "Use this skill when the user mentions <slug>, or related requirements" placeholder line.
