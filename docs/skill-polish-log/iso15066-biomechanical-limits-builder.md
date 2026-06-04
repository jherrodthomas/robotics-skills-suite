# Polish log — `iso15066-biomechanical-limits-builder` (+ paired reviewer)

## 2026-06-04 (autonomous POLISH, addresses issue #6)

**Severity:** medium — edition strings ambiguous, one wrong filename in reviewer file tree.

### What's good
- Builder description already names body-region force/pressure, quasi-static AND transient contact, safety margin, and verification method — the full ISO/TS 15066:2016 Annex A modelling surface.
- Output structure correctly lists the 11 tabs in roughly the order an analyst would walk them (Title → Doc Control → Cobot ID → Body Region Catalog → Contact Scenarios → Quasi-Static → Transient → Safety Margin → Verification → References).
- Body Region Catalog correctly anchored on ISO/TS 15066 Annex A.2 (the canonical 29-region human-body table).
- Reviewer 7-tab output layout (Title, General Info, Guide, Summary, Documentation, Technical Assessment, Verification Assessment) matches the same shape used by other reviewers in this suite — consistent UX across the family.

### What to fix
1. **(applied)** Edition strings — both files said "ISO TS 15066" (no slash, no year) and "ISO 10218-1 2025" (no colon). Canonical forms are `ISO/TS 15066:2016` and `ISO 10218-1:2025`. Updated description, H1, "When to use" prose, and the Annex A.2 reference.
2. **(applied)** Builder description now adds `ISO/TS 15066:2016` as a trigger keyword alongside the bare `ISO 15066` — analysts cite the full edition; the fully qualified form should fire the skill too.
3. **(applied)** Reviewer "Files in this skill" tree listed `biomechanical_probe.py` but the archive actually ships `iso15066-biomechanical-limits-checklist_probe.py`. Fixed the tree to match reality.
4. **(applied)** Builder "When to use" now clarifies that ISO/TS 15066:2016 has been consolidated into ISO 10218-1:2025 Clause 5.11 — both editions remain valid evidence, the new one supersedes for new builds but legacy projects citing only TS 15066 are still in scope.

### Descoped (follow-ups)
- Annex A.3 (quasi-static limits, 29 body regions) and Annex A.4 (transient limits, transient amplification factors) are referenced obliquely via the "Quasi-Static Limits Table" and "Transient Limits Table" tab names but the SKILL.md does not call out the source clause. Worth a future micro-edit but not a typo-class fix.
- Same `## Files in this skill` examples/ + references/ gap previously flagged on iso10218-compliance-matrix-builder and operating-envelope: the tree advertises `examples/sample_input.json` and `references/iso-ts-15066-annex-a2.md` + `references/biomechanical_methodology.md` that the archive does not ship. Same gap on reviewer (examples/sample_workbook.xlsx, references/reviewer_methodology.md, references/biomechanical_checks.md). Holding for the planned repo-wide sweep.
- Builder description does not yet mention pressure-pain-detection-threshold (PPT) vs maximum-permissible-force (MPF) — the two distinct families of limits inside Annex A. Minor copy improvement, future polish day.
- Generator script `generate_iso15066.py` was not opened — script-level edits are out of scope for a polish pass.

### Edition verification (mandatory for safety-critical domain)
- ISO/TS 15066:**2016** — confirmed correct edition. No 2024 or 2025 revision of TS 15066 has been issued; the document was instead folded into ISO 10218-1:2025 Clause 5.11.
- ISO 10218-1:**2025** — confirmed correct edition (replaced 2011 version).
- Anchor language now appears in both builder and reviewer descriptions.

### Files touched
- `skills/iso15066-biomechanical-limits-builder.skill` (SKILL.md inside zip)
- `skills/iso15066-biomechanical-limits-checklist-reviewer.skill` (SKILL.md inside zip)

