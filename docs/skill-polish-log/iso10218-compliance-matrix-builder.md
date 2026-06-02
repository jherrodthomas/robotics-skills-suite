# Polish log — iso10218-compliance-matrix-builder

## 2026-06-02 (POLISH, Tuesday)

**Selection rationale:** No open issues labeled `skill-bug` or `reviewer-finding`. No
orphan builders. All 38 builders tied at last-touched 2026-05-03. Aligned pick with
weekly target #5 (POLISH W23: iso10218-compliance-matrix — verify ISO 10218-1/-2:2025
edition); safety-critical compliance domain.

**Edition verification (mandatory for compliance domain):**
- Description anchors on **ISO 10218-1:2025 and ISO 10218-2:2025** — CORRECT current edition (the 2025 revision superseded the 2011 edition and folded in the bulk of ISO/TS 15066:2016 collaborative-robot content).
- Description explicitly notes the ISO/TS 15066 fold-in — CORRECT.
- No edition mismatch found.

**What's good:**
- Frontmatter `name` and `description` present; description is well-scoped (~480 chars, well under 1024).
- Description triggers on the right phrases: "ISO 10218", "robot compliance matrix", "robot integration compliance", "industrial robot safety compliance".
- Covers both ISO 10218-1 (manufacturer) and ISO 10218-2 (integrator) scope plus 15066 fold-in.
- Generator + recalc scripts present (`generate_iso10218.py`, `recalc.py`).

**What to fix:**
1. (low, applied) Title was "# Iso10218 Builder" — improper casing of the standard number and missing the "Compliance Matrix" qualifier from the skill name. Fixed to "# ISO 10218 Compliance Matrix Builder".
2. (low, applied) Body sentence "Generates a complete, audit-ready workbook for iso10218 compliance assessment." — corrected "iso10218" → "ISO 10218".
3. (low, applied) "Use this skill when the user mentions iso10218" — corrected casing.
4. (med, NOT applied — descope) `## Files in this skill` section claims a `references/` directory containing `methodology.md` and `iso10218_conventions.md`, but the skill archive contains only `SKILL.md` and `scripts/`. Either the references should be added or the claim removed from SKILL.md. Logging as follow-up for human review since adding content is a refactor, not a typo fix.
5. (med, NOT applied) `## When to use this skill` is one sentence: "Use this skill when the user mentions ISO 10218, or related requirements." Should enumerate the canonical triggers also listed in the frontmatter description (compliance matrix, integrator file, gap analysis, conformance status) for stronger in-skill self-documentation. Refactor-scale.
6. (med, NOT applied) `## Output structure` section is generic ("multiple tabs organized by assessment category") — should name the actual tabs the generator emits (Title Page, ISO 10218-1 Clause Matrix, ISO 10218-2 Clause Matrix, Cobot Annex, Evidence Index, Gap Tracker, Signoff). Requires reading `generate_iso10218.py` and is a refactor.

**Suggested edits (for next POLISH or human pass):**
- Either ship the two `references/*.md` files or strike the references/ block from `## Files in this skill`.
- Expand `## When to use this skill` with 3-5 bullet triggers.
- Replace `## Output structure` placeholder with the actual generated tab list.
- Consider adding a `## Methodology` short note linking to AIAG-style compliance-matrix patterns plus the 10218 Annex structure.

**Severity:** low (applied fixes are typo-class; remaining items are content gaps, not correctness bugs).
