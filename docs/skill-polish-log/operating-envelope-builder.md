# Polish log — operating-envelope-builder

## 2026-06-03 (POLISH, Wednesday)

**Selection rationale:** No open issues labeled `skill-bug` or `reviewer-finding`. No
orphan builders. Aligned pick with weekly target #7 (POLISH W23: operating-envelope —
verify ISO 3691-4:2020 zone semantics). Issue #7 was the least-recently-updated open
target (2026-06-01) versus the other four W23 targets (2026-06-03). Safety-critical
AMR domain, so edition-anchor verification is mandatory.

**Edition verification (mandatory for AMR domain):**
- Description before edit did **not** name a standard at all — just referenced "AMR
  fleets" and "mobile robot fleet zoning". Major gap for a safety-critical skill.
- Standard for driverless industrial trucks is **ISO 3691-4:2020** (current edition;
  Amendment A1 exists but the base remains 2020). This is what the weekly plan asks
  for and what was applied.
- Reviewer pair had the same gap. Updated in lockstep.
- No edition **mismatch** found (because no edition was named); applied edits add the
  anchor rather than correcting one.

**What's good:**
- Frontmatter `name` and `description` present and well-formed.
- Description, after edit, sits at 518 chars (builder) / 416 chars (reviewer) — well
  below the 1024 limit.
- Scope is coherent (zone catalog, coordinates, sensor coverage, E-stops, pedestrian
  crossings, speed limits, lighting/marking) and matches what an ISO 3691-4 operating-
  area definition would cover.
- Builder + reviewer pair is symmetric (both anchor on the same standard, same
  terminology).
- Both skills ship working generator/recalc scripts under `scripts/`.

**What to fix:**
1. (low, applied) Builder description did not name ISO 3691-4:2020. Added the
   anchor phrase "per ISO 3691-4:2020 (driverless industrial trucks) operating-area
   requirements" and extended trigger keywords to include "ISO 3691-4 operating
   areas".
2. (low, applied) Reviewer description did not name ISO 3691-4:2020. Added "against
   an ISO 3691-4:2020-aligned expert checklist" and a verification-clause trigger.
3. (low, applied) Builder body section `## When to use this skill` was a single
   sentence with no standard reference. Appended "Anchored on ISO 3691-4:2020
   (driverless industrial trucks)."
4. (low, applied) Builder body header "Generates a complete, audit-ready workbook
   for AMR fleet operating area definition and hazard zoning." now reads "…hazard
   zoning, aligned with ISO 3691-4:2020."
5. (low, applied) Reviewer body section likewise gained an ISO 3691-4:2020 mention
   in both the lead sentence and the "When to use this skill" bullet list.
6. (med, NOT applied — descope) Neither SKILL.md uses the standard's own terminology
   for **warning zone vs. hazard zone** or **protective stop / restart-after-reset**
   (ISO 3691-4 §§4.4 and 5.1). Adding these as named columns in the generated
   workbook is a generator-script change, not a SKILL.md typo, so it's out of scope
   for a POLISH pass. Logging for a future targeted update or a human pass.
7. (med, NOT applied) Builder `## Files in this skill` block claims an
   `examples/sample_input.json` and `references/iso-3691-4-operating-areas.md` +
   `references/envelope_methodology.md`, but the archive ships only `SKILL.md` and
   `scripts/`. Same pattern flagged on iso10218-compliance-matrix-builder on
   2026-06-02. The two skills should either ship the referenced files or the block
   should be struck. Refactor-scale across the suite — recommend a single repo-wide
   sweep rather than per-skill fixes.
8. (med, NOT applied) Reviewer `## Files in this skill` block lists
   `scripts/envelope_probe.py` but the actual file is
   `scripts/operating-envelope-checklist_probe.py`. Same root cause as #7 — defer.
9. (low, NOT applied) Reviewer `## Output structure` table is generic ("Technical
   Assessment: Zone definitions, coordinates, sensor placement, E-stop coverage").
   ISO 3691-4 would expect explicit checks on warning-zone deceleration profiles
   and on safety-related parts of control systems (SRP/CS). Refactor-scale.

**Suggested edits (for next POLISH or human pass):**
- Add `warning_zone` and `hazard_zone` as distinct enumerable zone types in
  `generate_envelope.py` (and reflect in Zone Catalog tab) — direct ISO 3691-4
  alignment.
- Add a "Protective Stop & Restart-after-Reset" tab with cells for stop-category
  (0/1/2), reset means, and operator-acknowledgement requirement.
- Repo-wide sweep on `## Files in this skill` blocks: either ship the referenced
  `examples/` + `references/` content for all 76 skills or strike the missing
  entries from each SKILL.md.

**Severity:** low (applied fixes are anchor-class; remaining items are content gaps
in the generated workbook, not correctness bugs in today's edited surface).
