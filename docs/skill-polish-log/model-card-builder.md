## 2026-07-02 — POLISH (autonomous)

**Domain:** ai-ml (not on the mandatory standard-edition list; governance frameworks verified via web anyway)
**Linked issue:** #32 (W27 target: refresh model-card builder governance terminology)
**Severity:** med

**What's good**
- Cleanly structured SKILL.md: clear trigger description, 4-step workflow, 11-tab output map.
- Anchored on the canonical model cards framework (Mitchell et al. 2019) — still the correct primary reference.
- Deterministic generate + recalc script pipeline; frontmatter has required name + description; description well under 1024 chars.

**What was fixed this run**
1. **File-tree accuracy (bug).** The "Files in this skill" tree listed `references/methodology.md` and `examples/sample_input_perception_model.json`, neither of which exists in the packaged skill. Corrected the tree to reflect the actual contents (SKILL.md + scripts/{generate_model_card.py, recalc.py, office/{__init__.py, soffice.py}}).
2. **Governance terminology refresh (issue #32).** Added a "When to use" bullet and expanded the Step 2 Fairness & Ethical item to map documentation onto the current AI-governance triad: ISO/IEC 42001:2023 (AI management systems), NIST AI RMF (Govern/Map/Measure/Manage, incl. the July 2024 Generative AI Profile), and EU AI Act transparency obligations. Editions verified against current sources on 2026-07-02.

**Suggested (future, not applied — would exceed a small POLISH edit)**
- Add the missing `references/methodology.md` and an `examples/*.json` so the tree can advertise them again, and so generate_model_card.py has a shipped sample input (med).
- Consider a dedicated tab 12 "Governance Mapping" cross-referencing each framework's clauses rather than folding it into Fairness & Ethical (low).
- The generator emits Mitchell-style sections only; an optional EU AI Act Annex IV technical-documentation cross-map would raise audit value (low).

**Notes:** No large refactor performed. Scripts left byte-identical. Issue #32 addressed in substance; leaving the issue open for human confirmation (autonomous runs do not close issues).
