# Polish log: pfl-plan-builder (+ paired reviewer)

## 2026-07-22

**Reviewed:** pfl-plan-builder.skill and pfl-plan-checklist-reviewer.skill (W30 target, issue #39; also tied for least-recently-touched at 80 days)

**What's good**
- Clear, well-scoped description and workflow; trigger phrases cover PFL, cobot inherent safety, biofidelic measurement.
- 11-tab output structure is sensible and matches PFL practice (function definition → contact scenarios → force/pressure measurement → results vs limits → re-test triggers).
- Generator script is syntactically clean; tab short-names correctly stay under Excel's 31-char sheet-name limit.

**What was fixed this pass (small, applied)**
- Standard editions anchored in both descriptions: ISO 10218-1:2025/-2:2025 and ISO/TS 15066:2016 (was unversioned "ISO 10218-1 and ISO TS 15066").
- File tree in builder SKILL.md claimed `examples/sample_input.json` and `references/` files that do not exist in the archive — tree corrected to actual contents.
- Generator produced 12 tabs (spurious trailing "Worksheet") vs the promised 11 — removed.

**What still needs fixing (not applied — too large for a polish pass)**
- **HIGH:** `generate_pfl_plan.py` is a placeholder stub — it accepts `<input.json>` but never reads it, and every tab is `"<name> - Placeholder"`. The skill does not actually produce the audit-ready workbook its description promises. Needs a real generator (input schema, per-body-region ISO/TS 15066 limit table, pass/fail formulas).
- **MED (edition nuance for human review):** in the 2025 revision, collaborative application requirements (incl. PFL) largely moved from ISO 10218-1/TS 15066 into ISO 10218-2:2025; TS 15066:2016 remains the biomechanical limits data source. SKILL.md body text still frames PFL as "ISO 10218-1" — a human with the standards should decide the correct clause references before deeper rewording.
- **LOW:** SKILL.md tab list says "Contact Scenario Catalog" / "Pre-Test Risk Reduction Measures"; script uses shortened sheet names (required by the 31-char limit). Consider noting the mapping in SKILL.md.

**Severity:** high (placeholder generator), med (edition framing), low (naming drift)
