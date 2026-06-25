# Polish log — cobot-hand-guiding-builder

## 2026-06-25 (autonomous POLISH, issue #25)

**Domain:** cobot (safety-critical → edition verification performed)
**Severity of findings:** med

### What's good
- Description names the right technical surface: hand guiding device design, enabling switch wiring, reduced speed limits, supervisor approval workflow, and a validation protocol — the core controls of a collaborative hand-guiding operation.
- Trigger vocabulary is good and covers the synonyms operators actually use: hand guiding, cobot teach, manual lead through, collaborative robot direct manipulation.
- Frontmatter has both required fields (name, description). Description is 450 chars after this run's edit — well under the 1024 limit.
- Generator + recalc scripts present and structured (`scripts/generate_hand_guide.py`, `scripts/recalc.py`, `scripts/office/soffice.py`).

### What was fixed this run
- **Edition anchor (the issue #25 definition-of-done).** The description previously referenced "ISO 10218-1" (no edition) and "ISO TS 15066" (no edition, non-standard notation). Anchored on the current editions and corrected the notation: `ISO 10218-1:2025`, `ISO 10218-2:2025`, and `ISO/TS 15066:2016`. ISO 10218 Parts 1 and 2 were both revised to the **2025** editions (superseding 2011); collaborative-operation/integration requirements (including hand guiding applied at the cell level) now sit primarily in **Part 2:2025**, while the robot-level capabilities (enabling device, reduced speed) are in **Part 1:2025**. ISO/TS 15066:**2016** remains current and supplies the biomechanical/speed-and-separation detail. Updated both the description opening clause and the "When to use" line. SKILL.md 1822 → 1876 bytes; `.skill` re-zipped preserving the other 4 payload files (integrity verified, `unzip -t` clean).

### What to fix next (flagged, NOT changed this run)
- **Doc/file mismatch (med).** SKILL.md's "Files in this skill" section lists `examples/sample_input.json`, `references/iso-10218-1-hand-guide.md`, and `references/hand_guiding_methodology.md`, but the archive contains **no `examples/` or `references/` directories** (5 payload files only: SKILL.md + 4 scripts). Either those files were dropped from the package or the listing is aspirational. Recommend restoring the reference/example files OR trimming the file list to match reality. Left for follow-up — adding/removing packaged content is beyond a small typo-class fix.
- **Reference doc should cite Part 2 (low/med).** The listed (missing) reference `iso-10218-1-hand-guide.md` is named for Part 1 only; once restored it should also reflect the Part 2:2025 home of integration-level hand-guiding requirements.
- **Body is thin (low).** The body does not mention the 2025 editions, the enabling-switch 3-position logic, or the reduced-speed limit basis. The description carries the triggering signal; body enrichment is a future DOCS-pass item. Low severity.

### Edition check summary
- ISO 10218-1: **2025** — anchored ✅ (superseded 2011)
- ISO 10218-2: **2025** — anchored ✅ (superseded 2011; integration-level home of hand guiding)
- ISO/TS 15066: **2016** — anchored ✅ (current; notation corrected from "ISO TS 15066")
