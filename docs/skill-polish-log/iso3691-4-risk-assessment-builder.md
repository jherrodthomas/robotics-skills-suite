# Polish log — iso3691-4-risk-assessment-builder

## 2026-06-30 (POLISH run, domain: amr)

**Severity:** med

**What's good**
- Clear, well-scoped description that names concrete AMR hazard sources (autonomous navigation, payload handling, charging, blind corners, mixed pedestrian environments, autonomous↔manual mode transitions) — strong trigger surface.
- Sensible 7-step workflow and an 11-tab output structure that maps to a real ISO 3691-4 risk-assessment deliverable (hazard catalog → risk estimation → safeguard selection → pedestrian interaction → validation).
- Builder is paired with iso3691-4-risk-assessment-checklist-reviewer (no orphan).

**What to fix**
1. **Standard edition mismatch (safety-critical).** The skill referenced bare "ISO 3691-4" with no edition anchor, and weekly-target issue #29 names **ISO 3691-4:2020**. Verified against ISO: the current published edition is **ISO 3691-4:2023** (published June 2023), which supersedes the 2020 edition. The 2023 revision notably adds the "restricted zones" higher-speed framework requiring detailed hazard analysis. Anchoring on 2020 would document an out-of-date basis. **Applied:** anchored the description on `ISO 3691-4:2023`. Follow-up: issue #29 wording should be corrected from :2020 to :2023, and the hazard catalog/restricted-zone content should be reviewed against the 2023 text in a future builder pass.
2. **Inaccurate "Files in this skill" tree (doc-quality).** SKILL.md listed `examples/sample_input.json`, `references/iso-3691-4-hazards.md`, and `references/amr_risk_methodology.md`, but the packaged `.skill` archive contains only `SKILL.md` and `scripts/` (generate_iso3691_4.py, recalc.py, office/soffice.py). The documented tree referenced files that do not ship. **Applied:** corrected the tree to match the actual package contents.

**Suggested edits (not applied — larger than a polish pass)**
- Restore genuine `examples/sample_input.json` and `references/` content, or keep the workflow's "examples" references consistent with what actually ships. If sample input + reference notes are intended to exist, they should be authored and re-bundled (builder-level work, not polish).
- Review hazard catalog and risk-estimation tabs against the ISO 3691-4:2023 restricted-zone provisions.

**Edition verification**
- ISO 3691-4:2023 confirmed as current edition (supersedes ISO 3691-4:2020). Source: iso.org standard 83545 (2023) vs 70660 (2020).
