# Polish Log — robot-cell-layout-builder

## 2026-07-01 (POLISH, severity: medium)

**Selection rationale:** No orphan builders exist (38/38 paired), so POLISH fell to the
least-recently-touched builder tier (many tied at 2026-05-03). Picked
`robot-cell-layout-builder` because it is (a) least-recently-touched, (b) the open W27
target #30, and (c) a safety-critical **cell-design** domain skill requiring standard-edition
verification — while giving good domain spread vs. recent polishes (amr/cobot/cybersecurity/compliance).

**What's good:**
- Clear 11-tab structure that maps cleanly onto integrator layout deliverables.
- Scripts (`generate_cell_layout.py`, `recalc.py`, office helper) compile cleanly and are self-contained.
- Trigger phrasing ("robot cell layout", "cell footprint", "fence design", "robot work zone") is concrete.

**What was fixed (edition anchoring, per DoD #30):**
- Description anchored bare "ISO 10218-2" → **ISO 10218-2:2025** (verified current; supersedes 2011,
  retitled "Industrial robot applications and robot cells").
- Added the missing minimum-distance standards that a layout with light curtains / perimeter sensors /
  fencing structurally depends on: **ISO 13855:2024** (safeguard positioning; new separation-distance
  formula S = (K×T) + DDS + Z incl. dynamic separation) and **ISO 13857:2019** (reaching-over/through
  safety distances). These were entirely absent before.
- Updated Standards & References block with full current titles + edition years; expanded OSHA to
  "29 CFR 1910.147 — Control of Hazardous Energy".
- Cross-referenced the editions into the Fence Design (tab 3), Perimeter Sensors (tab 4), Light Curtains
  (tab 5), and Regulatory Checklist (tab 10) descriptions.
- Kept the generator (`generate_cell_layout.py`) `standards` list and Regulatory Checklist tab consistent
  with the same editions so produced workbooks match the documented references.

**Edition verification (web-confirmed 2026-07-01):**
- ISO 10218-2:2025 — current. (iso.org/standard/73934)
- ISO 13855:2024 — current; EN ISO 13855:2024 in force Nov 2024, supersedes 2010. (iso.org/standard/80590)
- ISO 13857:2019 — current. (iso.org/standard/, referenced via machinebuilding/pilz)

**Scope discipline:** description remains 530 chars (< 1024). No structural/logic refactor of scripts;
only string/reference edits. Archive re-zipped preserving original tree (no `__pycache__` leakage).

**Suggested future edits (NOT done today — out of single-skill scope):**
- Consider adding a numeric worked example of the ISO 13855:2024 S = (K×T) + DDS + Z calculation to the
  Light Curtains tab so integrators see the dynamic-separation term applied.
- Cross-link the paired `robot-cell-layout-checklist-reviewer` to check that light-curtain safety
  distances were computed with the 2024 formula (not the legacy S = (K×T) + C).
