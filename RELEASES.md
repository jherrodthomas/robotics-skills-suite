# Releases

## v2026.08.W2 — 2026-08-08

**Highlights:** Ninth tagged weekly snapshot, covering the 2026-W32 working week (Mon 2026-08-03 → Sat 2026-08-08). Three of five W32 targets landed, all **pair-complete** standards-edition anchoring: `robot-cell-scope` on ISO 10218-2:2025 + ANSI/A3 R15.06-2025, `fleet-manager-architecture` reviewer reconciled with its builder and pinned to ISO 3691-4:2020 + VDA 5050 2.1.0 (closing the W31 `chain-break`), and `robot-sop` re-anchored on **ANSI/A3 R15.06-3-2025** — the part that actually governs cell operating procedures — plus specific OSHA 29 CFR parts. Friday closed the W32 changelog and three example stubs, lifting examples coverage to 32/76 (42%). Not reached: #44 `declaration-of-conformity` and #45 `safety-io-matrix`, both carrying into W33. Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-08-03 → 2026-08-08):**

*plan:*
- seed W32 targets — three carryovers plus two import-baseline pairs (d8e7059)

*polish:*
- anchor robot-cell-scope pair on ISO 10218-2:2025 and ANSI/A3 R15.06-2025 (9d0c927)
- reconcile fleet-manager reviewer with builder, pin ISO 3691-4:2020 and VDA 5050 2.1.0 (a84987a)
- anchor robot-sop pair on ANSI/A3 R15.06-3-2025 and specific OSHA parts (8c19840)

*docs:*
- W32 changelog section, three example stubs, STATUS refresh (18bb950)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 10 builders touched within 30 days, 28 stale (30+ days), 0 orphans. Examples coverage: 32/76 skills (42%).

**Known defect (human attention):** at least four pairs — `robot-sop`, `machinery-safety-lifecycle-plan`, `fleet-manager-architecture`, `behavior-tree-spec` — ship placeholder or entirely absent generator scripts. Descriptions and standards citations on these are now correct, but the skills cannot produce a workbook. This snapshot documents that state rather than fixing it; it warrants a dedicated implementation week rather than further polish passes.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.08.W1...v2026.08.W2

## v2026.08.W1 — 2026-08-01

**Highlights:** Eighth tagged weekly snapshot, covering the 2026-W31 working week (Mon 2026-07-27 → Sat 2026-08-01). Two of five W31 targets landed, both **pair-complete**: `behavior-tree-spec` re-anchored on BehaviorTree.CPP v4 with its Nav2 plugin framing corrected, and `ot-asset-inventory` anchored on IEC 62443-2-1 / -3-2 with tab count and file trees fixed. The W31 changelog section and two reviewer example stubs closed out Friday. Not reached: the fleet-manager-architecture reviewer lockstep gap (#42), robot-sop (#43), and declaration-of-conformity (#44) — all three carry into W32. Suite holds at 76 .skill files, 100% paired, zero orphans. Naming note: the tag month follows the release date (August), not the ISO week (W31); this is the first snapshot where those diverge.

**Changes this week (2026-07-27 → 2026-08-01):**

*plan:*
- seed W31 targets — two carryovers, reviewer gap, two baseline pairs (719a954)

*polish:*
- anchor behavior-tree-spec pair on BT.CPP v4, fix Nav2 plugin framing (c6f1cf6)
- anchor ot-asset-inventory pair on IEC 62443-2-1/-3-2, fix tab count and trees (83d2b18)

*docs:*
- W31 changelog section, two reviewer example stubs, STATUS refresh (defe72e)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 10 builders touched within 30 days, 28 stale (30+ days), 0 orphans. Reviewer debt: 33/38 reviewers still stale or at import baseline.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.07.W4...v2026.08.W1

## v2026.07.W4 — 2026-07-25

**Highlights:** Seventh tagged weekly snapshot. W30 hit 3 of 5 weekly targets — fleet-manager-architecture's generator crash fixed (plus tab names and file tree), the pfl-plan pair anchored on ISO 10218:2025 + ISO/TS 15066:2016 editions, and the machinery-safety-lifecycle-plan pair edition-anchored — with a significant HIGH-severity discovery: the machinery-safety-lifecycle-plan pair's generator and probe scripts are placeholders (scaffold-only, cannot produce a workbook), flagged for a W31 implementation target alongside an audit of other 2026-05-03 import-baseline pairs. Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-07-20 → 2026-07-25):**

*plan:*
- seed W30 targets — carryover plus four import-baseline builders (d8f8daa)

*polish:*
- fix fleet-manager-arch generator crash, tab names, file tree (7f24c5d)
- anchor pfl-plan pair on 2025/2016 editions, fix tree, drop spurious tab (3003959)
- anchor machinery-safety-lifecycle pair editions, fix trees, flag scaffold (6234486)

*docs:*
- W30 changelog section, four example stubs, STATUS refresh (5cd4c64)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 12 builders touched within 30 days, 26 stale (30+ days), 0 orphans.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.07.W3...v2026.07.W4

## v2026.07.W3 — 2026-07-18

**Highlights:** Sixth tagged weekly snapshot. W29 delivered three safety/accuracy polish passes — the loto-procedure pair anchored on OSHA 29 CFR 1910.147 + ISO 14118:2017, ansi-r1506-compliance-matrix re-anchored on ANSI/A3 R15.06-2025, and a false "ROS 2 Iron LTS" claim corrected in ros2-system-architecture-builder — plus the W29 changelog with a W28 backfill. Note: no v2026.07.W2 snapshot was tagged for the July 6–12 window (scheduler gap 2026-07-09 → 2026-07-14), so the compare link below spans from W1 and also captures W28's ssm-plan and iec62061 polishes. Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-07-13 → 2026-07-18):**

*polish:*
- anchor loto-procedure pair on OSHA 29 CFR 1910.147 + ISO 14118 (51031df)
- anchor ansi-r1506 builder on ANSI/A3 R15.06-2025, fix file tree (35443f1)
- fix false Iron LTS claim in ros2-system-architecture builder (f283050)

*docs:*
- W29 changelog plus W28 backfill, four example stubs, STATUS refresh (bfa31a2)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 11 builders touched within 30 days, 27 stale (30+ days), 0 orphans.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.07.W1...v2026.07.W3

## v2026.07.W1 — 2026-07-04

**Highlights:** Fifth tagged weekly snapshot. W27 delivered 3 of 5 weekly targets via polish passes — iso3691-4-risk-assessment edition-anchored (ISO 3691-4:2023), robot-cell-layout anchored on ISO 10218-2:2025 + ISO 13855:2024/13857:2019, and model-card-builder governance terminology refreshed — plus the June 2026 monthly KPI report. Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-06-29 → 2026-07-04):**

*plan:*
- seed W27 targets — 5 issues across 5 deferred domains (4a6719c)

*polish:*
- anchor iso3691-4-risk-assessment-builder on ISO 3691-4:2023, fix file tree (e76a175)
- anchor robot-cell-layout-builder on ISO 10218-2:2025 + ISO 13855:2024/13857:2019 (1df457d)
- refresh model-card-builder governance terms, fix file tree (55bfd6e)

*docs:*
- W27 changelog, three example stubs, refresh STATUS and journal (4f4aba4)
- KPI report for June 2026 (21ae46e)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 10 builders touched within 30 days, 28 stale (30+ days), 0 orphans.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.06.W4...v2026.07.W1

## v2026.06.W4 — 2026-06-27

**Highlights:** Fourth tagged weekly snapshot. W26 was a steady maintenance week — three safety-critical builders edition-anchored (ISO 13849-1:2023, IEC 62443-3-2:2020, ISO 10218-1/-2:2025 + ISO/TS 15066:2016), plus changelog and example-stub upkeep. Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-06-22 → 2026-06-27):**

*polish:*
- anchor iso13849-plr-builder on ISO 13849-1:2023 edition (f1071c2)
- anchor iec62443-risk-assessment-builder on IEC 62443-3-2:2020 (1724070)
- anchor cobot-hand-guiding-builder on ISO 10218-1/-2:2025 + ISO/TS 15066:2016 (bcc5c2e)

*docs:*
- W26 changelog, three example stubs, refresh STATUS and journal (e54433e)

*plan:*
- seed W26 targets — 5 issues across 5 deferred domains (64c0fb5)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 9 builders touched within 30 days, 29 stale (30+ days), 0 orphans.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.06.W3...v2026.06.W4

---

## v2026.06.W3 — 2026-06-20

**Highlights:** Third tagged weekly snapshot. W25 was a steady maintenance week focused on edition-anchoring two more safety-critical builders and bringing the changelog and example stubs current. Suite holds at 76 .skill files, 100% paired. Note: no W2 (v2026.06.W2) snapshot was tagged for the June 8–14 window, so the compare link below spans from W1 to capture everything since the last release.

**Changes this week (2026-06-15 → 2026-06-20):**

*polish:*
- anchor iso9283 performance-test builder on ISO 9283:1998 edition (5442dcf)
- anchor interlock-estop editions, add ISO 13850 / IEC 60204-1 / ISO 14119 (70d9030)

*docs:*
- add W24+W25 changelog, three example stubs, refresh STATUS (bc0c74a)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 6 builders touched within 30 days, 32 stale (30+ days), 0 orphans.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.06.W1...v2026.06.W3

---

## v2026.06.W1 — 2026-06-06

**Highlights:** First tagged weekly snapshot of the suite. W23 ran the full cadence: 5 planned targets seeded as issues, three polish passes anchoring safety-critical skills on current standard editions (ISO 10218-1/-2:2025, ISO 3691-4:2020, ISO/TS 15066:2016), and CHANGELOG bootstrap with example README stubs.

**Changes this week (2026-06-01 → 2026-06-06):**

*polish:*
- anchor iso15066 pair on ISO/TS 15066:2016 (21c8e33)
- anchor operating-envelope pair on ISO 3691-4:2020 (2a34ccb)
- fix ISO 10218 casing typos, log polish review (7c0fc30)

*docs:*
- bootstrap CHANGELOG, seed W23 example READMEs, refresh STATUS (0e694d5)

*plan / reporting:*
- seed W23 targets — 5 issues across 5 domains (2f8b9ed)
- KPI report for May 2026 (93e2167)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files).

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/commits/v2026.06.W1 (first release — no prior tag to compare against)
