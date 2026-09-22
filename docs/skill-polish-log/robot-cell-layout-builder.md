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

## 2026-09-22 (POLISH, severity: high)

**Selection rationale:** Rule (1) — open issue [#60](https://github.com/jherrodthomas/robotics-skills-suite/issues/60),
labelled `weekly-target`/`cell-design`, designated Tuesday in `WEEK-2026-W39.md`. Ranked first by
`rank_reviewer_thinness.py`: a **6-body-line reviewer against a 33-line builder**, the thinnest artifact
in all 76 files, 81 days stale on the reviewer half (2026-05-03), and carrying every edition asymmetry
in the pair. This is the first run of the successor selector standing up in production.

**What's good (unchanged from the 2026-07-01 pass, and it held up):**
- The builder's 11-tab structure still maps cleanly onto integrator deliverables and needed no re-cut.
- Edition anchoring done on 07-01 was correct on all three counts — re-verified today, no drift.
- The 07-01 entry's own "suggested future edits" predicted exactly this work: *"cross-link the paired
  reviewer to check that light-curtain safety distances were computed with the 2024 formula (not the
  legacy S = (K×T) + C)."* That suggestion is now implemented. **The log worked as a queue.**

**What was fixed — reviewer half (the real work):**
- Body went from 6 lines (one purpose sentence + a 3-item undated Standards list, **zero stated checks**)
  to four rated check groups. The description promised "structured pass-fail criteria"; it now has them.
- **Space terminology made explicit and put first.** Maximum / restricted / operating / safeguarded
  space are now tabulated with the note that a layout fencing to "the robot envelope" has not
  distinguished restricted from safeguarded space and its separation distance is therefore unverifiable.
  This is the defect the pair exists to catch and neither half named it before.
- **Group 2 requires the distance to be derived, not asserted** — T decomposed into detection +
  controller + robot stop + final actuator (overall system stop performance, not sensor response time),
  approach direction stated rather than assumed, and a legacy `S = (K×T) + C` result called out as a
  finding rather than a rounding difference.
- Group 3 pairs aperture/gap sizing with guard setback and reconciles *every* perimeter opening — gate,
  conveyor port, chute, cable pass — to an interlock, a tunnel, or a guarded distance.
- Group 4 adds trapped-person escape and restart prevention from inside, whole-body access risk, and
  muting/blanking justification with an invalidating condition — none of which existed anywhere in the pair.
- Three editions pinned to match the builder. Boundaries drawn against `safety-io-matrix`,
  `interlock-estop-architecture`, `ssm-plan`/`pfl-plan`, and the acceptance pair.
- Description rewritten, **982 chars** (was 358). Held ~40 chars under the 1024 limit deliberately after
  a first draft landed at 1015 — that is too little headroom for the next edit to be safe.

**What was fixed — builder half (lockstep):**
- Added the matching four-space table and a Scope boundaries section.
- Tabs 3/4/5/7/8 reworded so the workbook *asks for* what the reviewer now checks: derivation shown,
  coverage mapped against the restricted space, muting justified, trapped-person escape recorded.
- Standards block states the 13855 edition delta in words, not just a year.
- `generate_cell_layout.py`: four tab-description strings updated so produced workbooks match. **No
  logic change**; compiles clean.

**Edition verification (web-confirmed 2026-09-22 — mandatory step, cell-design is safety-critical):**
- **ISO 10218-2:2025** — current, 2nd edition, published 2025-01-31, revision of ISO 10218-2:2011. ✅
- **ISO 13855:2024** — current, 3rd edition; 2024 revision added dynamic separation distance
  calculation, revised the two-hand formula, and set new vertical ESPE limits. ✅
- **ISO 13857:2019** — current; revises the 2008 edition and **was reviewed and confirmed in 2025**. ✅
- No drift from the 07-01 verification. Three consecutive weeks of "do not assume the builder is right"
  have now produced one week where the builder *was* right, which is also a useful result.

**Two audit-script findings — the plan was wrong about this pair, in a way worth recording:**

1. **The `['2011','2025']` flag on ISO 10218-2 is a false positive.** `WEEK-2026-W39.md` records it as
   "the builder still carries superseded 2011" and instructed the edition step to fire on it. It is not
   a stale pin — it is the phrase *"supersedes ISO 10218-2:2011"* inside a correctly dated reference.
   `audit_pair_editions.py` regex-harvests every 4-digit year near a standard token and cannot tell a
   supersession note from a citation. **`robot-cell-scope` is now the top MISMATCH entry for exactly the
   same reason** (builder `['2011','2025']` vs reviewer `['2025']`) and is equally likely to be clean.
   Not fixed today — changing the audit heuristic is a script change, not a polish, and the safer fix is
   an explicit ignore-phrase list rather than a looser regex. **Filed to #64.**
2. **The plan's asymmetry arithmetic double-counts.** It says this pair carries "3 of the 9 open
   asymmetries" and that Tue+Wed would close 7 of 9. The audit counts **pairs**, not lines: this pair was
   *one* of nine and the count went 9 → 8, not 9 → 6. Wednesday's `interlock-estop-architecture` will
   take it to 7. **W40's plan should not promise a 9 → 2 drop.**

**Scope discipline:** prose and four generator strings only. No refactor of `recalc.py` or the office
helper. The three reviewer placeholders were left as placeholders and are now *declared* as such in a
new "Implementation status" section — this reviewer is tier C (no `generate_checklist.py` at all), and
stating that in the file is the cheapest partial answer available to #63's complaint that "38/38 paired
(100%)" reads as 100% working. Archives re-zipped from the original trees; no `__pycache__` leakage;
`yaml.safe_load` passes on both halves.

**Suggested future edits (NOT done today):**
- Add a worked numeric `S = (K×T) + DDS + Z` example to the builder's Light Curtains tab — carried over
  untouched from the 07-01 entry, still the single most useful addition to this pair and still out of
  scope for a polish pass.
- Give the audit script an ignore-phrase list so "supersedes X:YYYY" stops generating false MISMATCHes.
- When #63 is answered, this reviewer's four groups are now specified tightly enough to be implemented
  as a `CHECKS` table more or less directly.
