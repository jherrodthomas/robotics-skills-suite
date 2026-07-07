# Polish log: ssm-plan-builder

## 2026-07-07

**Picked because:** least-recently-touched builder (2026-05-03) and W28 planning target (issue #35, cobot domain). No open skill-bug / reviewer-finding issues and no orphan builders today.

**What's good**
- Clear workflow and output-structure sections; the 11-tab workbook layout is well described.
- The protective separation distance formula (Sp = Sh + Sr + Ss + C + Zd + Zr) is stated explicitly in the output structure — good anchor for auditors.
- Description length well under the 1024-char limit; trigger phrases (SSM, protective separation distance, cobot SSM mode) are specific and useful.

**What to fix**
1. **Standard editions missing (safety-critical domain check).** Description cited bare "ISO 10218-1 and ISO TS 15066" with no editions. Current editions: ISO 10218-1:**2025** and ISO/TS 15066:**2016**. FIXED — editions anchored in frontmatter description and "When to use" section.
2. **ISO 13855 absent.** The Sp formula and operator approach-speed assumptions derive from ISO 13855 (current edition **2024**); the skill never referenced it. FIXED — added "protective separation distance per ISO 13855:2024" to the description.
3. **File tree inaccurate.** SKILL.md listed `examples/sample_input.json` and `references/iso-10218-1-ssm.md` / `ssm_methodology.md` that do not exist in the archive, and omitted `scripts/office/__init__.py`. FIXED — tree now matches actual archive contents.

**Suggested edits (deferred — too large for a polish pass)**
- Note that ISO 10218-2:2025 now integrates collaborative-application requirements formerly carried by ISO/TS 15066; the workbook References tab and generator text should reflect that relationship. Needs a look inside generate_ssm_plan.py's references output.
- Consider actually adding the missing `examples/sample_input.json` and reference notes rather than just deleting them from the tree.

**Severity:** medium (edition anchoring on a safety-critical skill), now resolved for the description-level issues.
