# Polish log — iso9283-performance-test-builder

## 2026-06-18 (autonomous POLISH, severity: low)

**Domain:** v&v · **Paired reviewer:** iso9283-performance-test-checklist-reviewer.skill (present)

**What's good**
- Description is concise (464 chars, well under the 1024 limit) and names the concrete tests it covers (pose accuracy/repeatability, multi-directional accuracy, distance accuracy/repeatability, path velocity, corner overshoot).
- Frontmatter has both required fields (`name`, `description`); `name` matches the file/dir.
- Bundles working scripts (`recalc.py`, `office/soffice.py`) for XLSX recalculation — output is a real 11-tab workbook, not freeform chat.

**What to fix**
- Edition anchor was loose: description read "per ISO 9283 1998" (no colon) and the `## Standard` section gave an inaccurate title ("Industrial Robots - Positioning Repeatability and Accuracy") with no edition year. This breaks the repo convention of anchoring the exact standard edition (cf. iso12100, iso15066, operating-envelope polish commits).

**Edits applied (small, obvious)**
- Description: `per ISO 9283 1998.` -> `per ISO 9283:1998.`
- `## Standard`: replaced the imprecise line with the verified citation —
  `ISO 9283:1998 (Edition 2, 1998-04-01; reviewed and confirmed 2021) — Manipulating industrial robots — Performance criteria and related test methods`.

**Edition verification**
- Confirmed via iso.org and BSI/ANSI listings: ISO 9283:1998 is the second edition (1998-04-01), last reviewed and **confirmed in 2021** — it remains the current edition. No mismatch; the standard has not been superseded. (Note: v&v is not on the mandatory safety-critical edition-check list, but the anchor was corrected for consistency with the rest of the suite.)

**Follow-ups**
- Consider adding a one-line `## Input` shape note (JSON schema or example) to match builders that document expected input.
- The paired reviewer (`iso9283-performance-test-checklist-reviewer`) should be checked for the same edition string on its next polish pass.
