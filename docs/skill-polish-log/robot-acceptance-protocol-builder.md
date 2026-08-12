# Polish log — robot-acceptance-protocol-builder

## 2026-08-12 (autonomous POLISH, severity: med)

**Domain:** v&v · **Paired reviewer:** robot-acceptance-protocol-checklist-reviewer.skill (present) · **Issue:** #47 (W33 target)

**Selection rationale:** open W33 target issue #47 (`description-quality`, v&v) coincides with the least-recently-touched builder in the repo (last touched 2026-05-03, 101 days).

**What's good**
- Description is compact and names the two real phases (FAT / SAT) plus the concrete test families, so triggering on "robot FAT", "robot SAT", "cell commissioning" is unambiguous.
- Frontmatter has both required fields; `name` matches file and internal directory.
- The 11-tab output structure is well sequenced — FAT gates before SAT planning, and customer sign-off is terminal rather than sprinkled through.

**What to fix**
1. **Edition anchor missing (primary).** `## Standards` read only `ISO 10218-2 Robots and robotic devices — Safety` — no edition, and the title was the *2011* wording. ISO 10218-2 was revised in 2025 and retitled *Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells* (Edition 2, superseding 2011). This is the exact mismatch class the repo has been correcting since the iso12100/iso15066/robot-cell-scope passes, and the 2026-08-11 declaration-of-conformity commit already anchored ISO 10218-1/-2:2025 elsewhere in the suite — this file was inconsistent with it.
2. **Standards list too thin for what the tabs actually assert.** The workbook has a performance-acceptance tab, a safety-function-validation tab, and an electrical commissioning checklist, but cited no source for any of them. Acceptance metrics invented per-project are the most common FAT dispute.
3. **Reviewer had no standards section at all**, so it could not flag a protocol citing superseded editions — a chain break against its own builder.
4. **No related-skills pointer**, unlike other polished builders; `iso9283-performance-test-builder` and `robot-field-acceptance-builder` are the obvious neighbours and were undiscoverable from here.

**Edits applied (small, obvious)**
- Builder description: appended `anchored on ISO 10218-2:2025 for cell integration and ISO 9283:1998 for performance criteria` (515 chars, well under 1024).
- Builder `## Standards`: replaced the single loose line with edition-anchored entries — ISO 10218-2:2025 (Ed 2, supersedes 2011, retitled), ISO 10218-1:2025 (Ed 3), ISO 9283:1998 (Ed 2, confirmed 2021), ISO 13849-1:2023 / -2:2012 (validation part), IEC 60204-1:2016. Kept "customer-specific acceptance requirements" but demoted it to *on top of, never in place of*.
- Builder: added a `## Related skills` section (iso9283, robot-cell-layout, interlock-estop, robot-field-acceptance, paired reviewer).
- Reviewer description: appended `against ISO 10218-2:2025 and ISO 9283:1998`.
- Reviewer: added a `## Standards baseline` section mirroring the builder, with an explicit instruction to flag protocols citing superseded editions; noted it does not modify the source workbook.

**Edition verification**
- ISO 10218-2:2025 confirmed on iso.org (std 73934) and ANSI webstore: *Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells*, revision replacing the 2011 version. ISO 10218-1:2025 (std 73933) confirmed as the Part 1 companion.
- ISO 9283:1998 remains current (Ed 2, reviewed and confirmed 2021) — carried over from the 2026-06-18 iso9283 pass, no change.
- ISO 13849-2 has **not** been revised alongside -1:2023; 2012 is still the validation edition. Recorded so a future pass does not "helpfully" bump it.

**Not done (deliberately descoped)**
- The reviewer's `check_definitions.py`, `dashboard.py`, and `*_probe.py` are all one-line placeholder stubs (69 b / 32 b / 69 b). The builder has no generator script at all — only `recalc.py` and the shared `office/` helpers. Wiring real check definitions and a generator is a refactor, not a polish edit.

**Follow-ups**
- Write a real `generate_acceptance_protocol.py` for the builder; today the workbook exists only as prose structure.
- Implement the reviewer's three stub scripts (check definitions, probe, dashboard) so the pair can actually run an audit.
- Sweep the remaining v&v skills (`robot-field-acceptance`, `robot-hil-test-catalog`) for the same ISO 10218-2:2011→:2025 mismatch — both untouched since 2026-05-03 and likely carry it.
- Repo-wide: grep every skill for bare `ISO 10218-2` with no edition; the fix is mechanical and this is unlikely to be the last instance.
