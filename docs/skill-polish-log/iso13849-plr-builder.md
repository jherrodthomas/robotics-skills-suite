# Polish log — iso13849-plr-builder

## 2026-06-23 (autonomous POLISH, issue #24)

**Domain:** compliance (safety-critical → edition verification performed)
**Severity of findings:** med

### What's good
- Description names the right technical surface: PLr derivation via the S/F/P risk graph, and PL verification through Category, MTTFD, DC, and CCF — the four pillars of an ISO 13849-1 assessment.
- Trigger vocabulary is solid: ISO 13849, PLr, performance level, SRP/CS, MTTFD, category B/1/2/3/4.
- Description is 426 chars, well under the 1024 limit. Frontmatter has both required fields (name, description).
- Generator + recalc scripts present and structured (`scripts/generate_iso13849.py`, `scripts/recalc.py`, `scripts/office/soffice.py`).

### What was fixed this run
- **Edition anchor (the issue #24 definition-of-done).** The description previously referenced "ISO 13849-1" with no edition. ISO 13849-1:**2023** is the current edition (it superseded the 2015 edition). Anchored the description on `ISO 13849-1:2023` in both the opening clause and the trigger list, and added the explicit `SRP/CS` expansion. SKILL.md 1187 → 1219 bytes; `.skill` re-zipped preserving structure. Small surgical change, no refactor.

### What to fix next (flagged, NOT changed this run)
- **Doc/file mismatch (med).** SKILL.md's "Files in this skill" section lists `references/methodology.md` and `references/iso13849_conventions.md`, but the archive contains **no `references/` directory** (5 payload files: SKILL.md + 4 scripts). Either the reference docs were dropped from the package or the file list is aspirational. Recommend: restore the two reference files OR trim the file list to match reality. Left for a follow-up because adding/removing reference content is beyond a small typo-class fix.
- **Generic body (low).** The "# Iso13849 Builder" body is boilerplate ("Use this skill when the user mentions iso13849, or related requirements") and does not mention the 2023 edition, the risk-graph inputs, or MTTFD/DC/CCF. The description carries the real signal; the body could be enriched in a future DOCS pass. Low severity — body text does not affect triggering.
- **Casing (low).** Heading reads "Iso13849 Builder"; preferred form is "ISO 13849-1 PLr Builder". Cosmetic.

### Edition check summary
- ISO 13849-1: **2023** — anchored ✅
- No other standard editions referenced in this skill's description.
