# Polish log — loto-procedure-builder

## 2026-07-15

**Picked because:** Top W28 carryover target (issue #31, W27+W28), operational domain, untouched since 2026-05-03 baseline. No open skill-bug/reviewer-finding issues and no orphan builders existed today.

**What's good**
- Clear, focused description that triggers on the right phrases (LOTO, lockout tagout, energy isolation).
- Output tab list covers the core OSHA 1910.147 elements: energy inventory, verification of zero energy, group lockout, re-energization.
- Paired reviewer's checklist mirrors the builder's output structure well.

**What was fixed (small, applied this run)**
- Standards anchoring: "OSHA 1910 147" → **OSHA 29 CFR 1910.147** (full citation) in both frontmatter descriptions and bodies.
- Added **ISO 14118:2017** (prevention of unexpected start-up) to Standards in builder and reviewer, per W28 definition of done.
- OSHA terminology: added "energy-isolating devices" and "authorized **and affected** employee" language (previously only "isolation points" / "authorized employees").
- Added "Files in this skill" tree sections matching actual archive contents (house style per polished skills, e.g. iec62061-sil-builder).
- Reviewer touched in lockstep — first reviewer polish in the suite (all 38 reviewers had sat at the 2026-05-03 baseline).

**What still needs fixing (not applied — beyond small-fix scope)**
- **No generator script.** The builder archive contains only `scripts/recalc.py` and `scripts/office/soffice.py` — there is no `generate_loto.py` (or equivalent) producing the promised 10-tab XLSX. Other builders (e.g. iec62061-sil-builder) ship a generator. The skill currently relies entirely on the model improvising the workbook.
- SKILL.md body is thin vs. house style: no "When to use this skill" / "Workflow" / "Output structure" sections.
- Consistency check vs. robot-sop pair: robot-sop-builder still cites bare "OSHA 1910" — same citation-style fix should be applied when robot-sop is polished.

**Severity:** medium (missing generator script is the substantive gap; standards anchoring now resolved)

**Standard-edition verification (safety-relevant skill):** OSHA 29 CFR 1910.147 is a regulation (no edition year); ISO 14118:2017 is the current edition. No mismatches after fix.
