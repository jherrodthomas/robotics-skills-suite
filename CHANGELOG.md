# Changelog

All notable changes to the Robotics Skills Suite are documented in this file.

The format groups commits by week of the year. Within each week, entries are bucketed by conventional-commit type (`feat:` / `fix:` / `polish:` / `docs:` / `chore:`). Releases are tagged separately in [RELEASES.md](RELEASES.md).

## [Unreleased]

### Week 2026-W34 (2026-08-17 → 2026-08-21)

**Second consecutive 3-of-3 week.** All three W34 targets (#48, #49, #50) landed on their scheduled days, and every one was an *import-baseline* pair — a skill that had never had a POLISH pass since the 2026-05-03 import. Three clusters (v&v, ros2, ai-ml) that were untouched a week ago now each have an anchored pair.

#### polish

- **robot-hil-test-catalog-builder** + **robot-hil-test-catalog-checklist-reviewer** (v&v) — edition-anchored six standards, adding `ISO 13849-2:2012` as the validation part the catalog actually rests on and `IEC 61508-3:2010` as the basis for arguing simulated-plant model validity; `ISO/DIS 13849-2` flagged do-not-bump until published. Introduced an explicit **HIL-versus-FAT scope boundary** (what is simulated, what is real, which evidence transfers), the `HIL-<function-id>-<class>-<nn>` case-ID convention resolving against the `safety-io-matrix` safety-function inventory, and traceability rules requiring every claimed DC figure to be defended by at least one injection case. Reviewer rewritten in lockstep and given the standards baseline it previously lacked entirely (#48) (`8ba1789`)
- **urdf-model-spec-builder** + **urdf-model-spec-checklist-reviewer** (ros2) — replaced the generic "ROS 2" reference with a dated distro baseline table (Jazzy default, Lyrical for 24.04→26.04, **Kilted flagged do-not-ship** on an EOL of November 2026). Corrected stale simulator naming — Ignition was renamed to Gazebo in 2022, Gazebo Classic 11 reached EOL 2025-01-31. Added the URDF/xacro-versus-SDFormat boundary including the closed-kinematic-loop limitation URDF cannot express, and pinned units and frames to REP-103 / REP-105. ROS 1 transmission coverage replaced with `ros2_control` interfaces (#49) (`df811d4`)
- **dataset-documentation-builder** + **dataset-documentation-checklist-reviewer** (ai-ml) — closed the known chain gap with the `model-card` pair: the builder now owns a dataset ID, semantic version, `<dataset-id>@<version>` citation string, and split fingerprint that `model-card-builder` consumes, with in-place version mutation prohibited. Governance baseline named and dated (ISO/IEC 42001:2023, 23894:2023, 5259 series, EU AI Act Regulation 2024/1689 Art. 10). Added robotics provenance fields — sensor part and shutter type, capture-rig geometry, calibration state and residual, time-sync skew, envelope coverage with named gaps. Reviewer's tab count corrected 7 → 5 and two phantom walkthrough tabs removed (#50) (`662de6b`)

#### docs

- **examples/** — **batch pass: examples coverage closed from 42/76 to 76/76 (100%).** Every one of the 34 remaining skills — 32 reviewer halves plus the `eoat-spec`, `iec62061-sil`, `nav2-config`, `operator-training-matrix`, `perception-test-catalog`, `robot-field-acceptance`, `ssm-plan`, `tf-tree-spec`, `wireless-coexistence-plan` and `zone-conduit-plan` builders — now has a `README.md`. Stub content is derived from each skill's own frontmatter and body, not invented, and each file says so. This retires the standing follow-up that the 2-per-week rate would not clear the gap until 2027. The two stubs for skills polished this week (`robot-hil-test-catalog-checklist-reviewer`, `urdf-model-spec-checklist-reviewer`) were written by hand against the full skill bodies and name the specific headline findings each reviewer raises
- **scripts/gen_status.py** — the STATUS generator is now a committed script instead of being rebuilt in `/tmp` on every run. Two defects had been fixed in it three separate times and lost each time (domain prefixes matched against stems rather than filenames; working-tree-modified skills reported as stale in the STATUS committed by the run that touched them). Both fixes are now in the file, with a warning emitted if any builder falls through to `unclassified`. Retires a follow-up that had been carried since W33
- **CHANGELOG.md** — add W34 weekly section
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 orphans, 13 fresh 🟢 / 25 stale 🟡
- **docs/AUTONOMOUS_LOG.md** — daily journal entries for the W34 run

#### chore

- **plan** — W34 seeded Monday with three least-recently-touched targets spread across v&v, ros2 and ai-ml, capacity held at 3 after W33's zero-carryover week; new issues #48–#50 (`4dc22b1`); see [docs/weekly/WEEK-2026-W34.md](docs/weekly/WEEK-2026-W34.md)

#### known issues

- **Five reviewers carry their builder's `description:` verbatim** — `ansi-r1506-compliance-matrix`, `iec62061-sil`, `iso10218-compliance-matrix`, `iso12100-risk-assessment`, and `iso13849-plr` checklist reviewers all describe *generating* a workbook rather than reviewing one. Triggering will be unreliable for all five, and all five sit in the safety-critical compliance/foundation clusters. Surfaced by the W34 DOCS batch pass, which reads every skill's frontmatter; each affected `examples/*/README.md` carries a warning banner. Not fixed here — this is POLISH work and needs an issue

### Week 2026-W33 (2026-08-10 → 2026-08-14)

**All three W33 targets landed — first fully cleared week in the repo's history.** Capacity was deliberately set to 3 on Monday to match observed throughput rather than exceed it; the plan held.

#### polish

- **declaration-of-conformity-builder** + **declaration-of-conformity-checklist-reviewer** (compliance) — full rewrite of both halves. Both bodies were import placeholder text about a skill called "Doc" (`declaration-of-conformity` had been tokenised to `doc` and never restored). Workflow now **forks on legal instrument first**: `Directive 2006/42/EC` governs placing on market through 19 Jan 2027, `Regulation (EU) 2023/1230` applies from 20 Jan 2027 and repeals it. Instrument numbers corrected to slashed form. Added standards-and-legal baseline (ISO 10218-1/-2:2025, ISO 13849-1:2023, IEC 62061:2021, ISO 12100:2010), an OJEU-citation-status column, Declaration of Incorporation (Annex II 1.B) coverage for integrators shipping partly completed machinery, and a GB/UKCA separation note. Reviewer gained an explicit list of 11 flaggable edition/legal conditions. Closes the oldest open target in the repo (#44, open since W31) (`aadcd83`)
- **robot-acceptance-protocol-builder** + **robot-acceptance-protocol-checklist-reviewer** (v&v) — anchored on `ISO 10218-2:2025` (Edition 2, supersedes 2011, retitled *Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells*); the file still carried the 2011 title with no edition. Standards section expanded to cover what the tabs actually assert (ISO 10218-1:2025, ISO 9283:1998, ISO 13849-1:2023 / -2:2012, IEC 60204-1:2016), with customer-specific criteria demoted to *on top of, never in place of*. Reviewer gained a standards baseline it previously lacked entirely — it could not flag superseded editions, a chain break against its own builder. Added a `## Related skills` pointer. **First POLISH pass on the v&v cluster** (#47) (`6244fd2`)
- **safety-io-matrix-builder** + **safety-io-matrix-checklist-reviewer** (cell-design) — pinned unversioned `ISO 13849-1` / `IEC 62061` references to `ISO 13849-1:2023` and `IEC 62061:2021`, added `ISO 10218-2:2025` and `IEC 60204-1:2016`. Reconciled OSSD / dual-channel wiring language (including cross-circuit fault detection) with the `interlock-estop-architecture` pair polished 2026-06-17, and added a per-row PL/Category ↔ SIL CL cross-reference convention. Reviewer updated in lockstep with EDM/feedback-monitoring and SIL CL consistency checks (#45) (`d909fc2`)

#### docs

- **CHANGELOG.md** — add W33 weekly section
- **examples/** — stub READMEs for skills touched in W33 lacking one: `robot-acceptance-protocol-builder`, `robot-acceptance-protocol-checklist-reviewer` (examples coverage now 38 dirs, 50% of the 76 skill files)
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 11 fresh / 27 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entries for the W33 run

#### chore

- **plan** — W33 seeded Monday with three targets: two carryovers (#44, #45) reusing their existing issues plus one new v&v beachhead (#47) (`e246935`); see [docs/weekly/WEEK-2026-W33.md](docs/weekly/WEEK-2026-W33.md)

### Week 2026-W32 (2026-08-03 → 2026-08-07)

#### polish

- **robot-cell-scope-builder** + **robot-cell-scope-checklist-reviewer** (foundation) — anchor the pair on `ISO 10218-2:2025` (Edition 2) and `ANSI/A3 R15.06-2025` (approved 21 Aug 2025, supersedes ANSI/RIA R15.06-2012), adopt *monitored standstill* in place of *safety-rated monitored stop*, reframe ISO/TS 15066:2016 as informative background now that collaborative content is consolidated into the 2025 editions; stub generator and two redundant empty probe files logged as follow-ups (`9d0c927`)
- **fleet-manager-architecture-builder** + **fleet-manager-architecture-checklist-reviewer** (amr) — reconcile the reviewer with the builder (closes the lockstep gap tracked in #42), pin `ISO 3691-4:2020` and `VDA 5050 2.1.0` (Jan 2025, backward compatible with 2.0.0) (`a84987a`)
- **robot-sop-builder** + **robot-sop-checklist-reviewer** (operational) — anchor the pair on `ANSI/A3 R15.06-3-2025` (use of industrial robot cells) and cite specific OSHA parts — 29 CFR 1910.147 (LOTO) and 1910.132 (PPE) — rather than a bare "OSHA" reference (`8c19840`)

#### docs

- **CHANGELOG.md** — add W32 weekly section
- **examples/** — stub READMEs for skills touched in W32 lacking one: `robot-cell-scope-builder`, `robot-cell-scope-checklist-reviewer`, `fleet-manager-architecture-checklist-reviewer` (examples coverage now 32 dirs)
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 11 fresh / 27 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entries for the W32 run

#### chore

- **plan** — W32 targets seeded Monday: three W30/W31 carryovers plus two import-baseline pairs, new issues #45–#46 (`d8e7059`); see [docs/weekly/WEEK-2026-W32.md](docs/weekly/WEEK-2026-W32.md)

### Week 2026-W31 (2026-07-27 → 2026-08-02)

#### polish

- **behavior-tree-spec-builder** + **behavior-tree-spec-checklist-reviewer** (ros2) — anchor the pair on `BehaviorTree.CPP v4.x` (`SKIPPED` status, precondition scripting, Groot2), reframe Nav2 node names as project plugins requiring registration rather than built-ins, fix file trees; placeholder checklist-generator scripts flagged in the polish log (`c6f1cf6`)
- **ot-asset-inventory-builder** + **ot-asset-inventory-checklist-reviewer** (cybersecurity) — anchor the pair on `IEC 62443-2-1` / `IEC 62443-3-2` terminology (System under Consideration, zones and conduits, asset criticality), correct tab count and file trees (`83d2b18`)

#### docs

- **CHANGELOG.md** — add W31 weekly section
- **examples/** — stub READMEs for skills touched in W31 lacking one: `behavior-tree-spec-checklist-reviewer`, `ot-asset-inventory-checklist-reviewer` (examples coverage now 27 dirs)
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 11 fresh / 27 stale (30+ days), reviewer debt 33/38
- **docs/AUTONOMOUS_LOG.md** — daily journal entries for the W31 run

#### chore

- **plan** — W31 targets seeded Monday: carryovers #40 and #41 reused (not duplicated) plus three new targets #42–#44 (`719a954`); see [docs/weekly/WEEK-2026-W31.md](docs/weekly/WEEK-2026-W31.md)

### Week 2026-W30 (2026-07-20 → 2026-07-26)

#### polish

- **fleet-manager-architecture-builder** (amr) — fix generator crash (illegal `/` in Excel tab name "VDA 5050 / MQTT / REST Interfaces"), rename placeholder "Worksheet" tab to "References", correct tab count to 12, fix file tree; placeholder-generator gap logged HIGH (`7f24c5d`)
- **pfl-plan-builder** + **pfl-plan-checklist-reviewer** (cobot) — anchor the pair on `ISO 10218-1:2025/-2:2025` and `ISO/TS 15066:2016`, fix file tree, drop spurious 12th tab; placeholder-generator gap logged HIGH (`3003959`)
- **machinery-safety-lifecycle-plan-builder** + **machinery-safety-lifecycle-plan-checklist-reviewer** (foundation) — anchor `ISO 12100:2010` / `ISO 13849-1:2023` / `IEC 62061:2021` / `EU Machinery Regulation 2023/1230` editions, rewrite reviewer description (was verbatim copy of builder's), fix file trees, remove leaked authoring-machine path from generator; scaffold-only pair flagged HIGH (`6234486`)

#### docs

- **CHANGELOG.md** — add W30 weekly section
- **examples/** — stub READMEs for skills touched in W30 lacking one: `fleet-manager-architecture-builder`, `pfl-plan-builder`, `pfl-plan-checklist-reviewer`, `machinery-safety-lifecycle-plan-checklist-reviewer`
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 13 fresh / 25 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entry for 2026-07-24 DOCS

#### chore

- **plan** — W30 targets seeded Monday: fleet-manager carryover (#37) plus four import-baseline polish targets #38–#41 (`d8f8daa`); see [docs/weekly/WEEK-2026-W30.md](docs/weekly/WEEK-2026-W30.md)

### Week 2026-W29 (2026-07-13 → 2026-07-19)

#### polish

- **loto-procedure-builder** + **loto-procedure-checklist-reviewer** (operational) — anchor the pair on `OSHA 29 CFR 1910.147` and `ISO 14118:2017` (energy isolation); log polish review (`51031df`)
- **ansi-r1506-compliance-matrix-builder** (compliance) — re-anchor on `ANSI/A3 R15.06-2025` (U.S. adoption of `ISO 10218-1/-2:2025`, superseding R15.06-2012 (R2017)); fix file tree; log polish review (`35443f1`)
- **ros2-system-architecture-builder** (ros2) — fix false "Iron LTS" claim; target current LTS set (Humble / Jazzy / Lyrical) with explicit do-not-target-Iron note; log polish review (`f283050`)

#### docs

- **CHANGELOG.md** — add W29 weekly section; backfill the missed W28 section (see below)
- **examples/** — stub READMEs for skills touched in W29 lacking one: `ansi-r1506-compliance-matrix-builder`, `loto-procedure-builder`, `loto-procedure-checklist-reviewer`, `ros2-system-architecture-builder`
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers
- **docs/AUTONOMOUS_LOG.md** — daily journal entry for 2026-07-17 DOCS

### Week 2026-W28 (2026-07-06 → 2026-07-12) — backfilled 2026-07-17

_The W28 Friday DOCS run did not execute (no commits 2026-07-09 → 2026-07-14); this section was reconstructed from the git log._

#### polish

- **ssm-plan-builder** (cobot) — anchor builder on `ISO 10218-1:2025` and `ISO/TS 15066:2016` (speed and separation monitoring); fix file tree; log polish review (`7bb3b4e`)
- **iec62061-sil-builder** (compliance) — anchor builder on `IEC 62061:2021` edition; fix file tree; log polish review (`44c4fc6`)

#### chore

- **plan** — W28 targets seeded Monday: 2 carryovers plus 3 new across 5 domains (`df2670b`); see [docs/weekly/WEEK-2026-W28.md](docs/weekly/WEEK-2026-W28.md)

### Week 2026-W27 (2026-06-29 → 2026-07-05)

#### polish

- **model-card-builder** (ai-ml) — refresh AI-governance terminology; align on `ISO/IEC 42001:2023`, NIST AI RMF, and EU AI Act references; verify fairness / slice-analysis / ethical-considerations coverage; fix file tree; log polish review (`55bfd6e`)
- **robot-cell-layout-builder** (cell-design) — anchor builder on `ISO 10218-2:2025` with safeguard positioning per `ISO 13855:2024` and minimum safety distances per `ISO 13857:2019`; log polish review (`1df457d`)
- **iso3691-4-risk-assessment-builder** (amr) — anchor builder on `ISO 3691-4:2023` (driverless industrial trucks / AMR); verify S/F/P risk-estimation and pedestrian-interaction coverage; fix file tree; log polish review (`e76a175`)

#### docs

- **CHANGELOG.md** — add W27 weekly section
- **examples/** — stub READMEs for skills touched in W27 lacking one: `model-card-builder`, `robot-cell-layout-builder`, `iso3691-4-risk-assessment-builder`
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 11 fresh / 27 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entry for 2026-07-03 DOCS

#### chore

- **monthly** — June 2026 KPI report generated (`21ae46e`)
- **plan** — W27 targets seeded Monday: 5 issues across 5 deferred domains (`4a6719c`); see [docs/weekly/WEEK-2026-W27.md](docs/weekly/WEEK-2026-W27.md)

### Week 2026-W26 (2026-06-22 → 2026-06-28)

#### polish

- **iso13849-plr-builder** (compliance) — anchor builder on `ISO 13849-1:2023` edition; verify PLr / Category / MTTFD / DC / CCF terminology and S/F/P risk-graph references; log polish review (`f1071c2`)
- **iec62443-risk-assessment-builder** (cybersecurity) — anchor builder on `IEC 62443-3-2:2020` edition; verify SL-T per FR1–FR7 and IEC 62443-3-3 cross-reference; log polish review (`1724070`)
- **cobot-hand-guiding-builder** (cobot) — anchor builder on `ISO 10218-1:2025`, `ISO 10218-2:2025`, and `ISO/TS 15066:2016`; verify enabling-switch / reduced-speed / supervisor-approval coverage; log polish review (`bcc5c2e`)

#### docs

- **CHANGELOG.md** — add W26 weekly section
- **examples/** — stub READMEs for skills touched in W26 lacking one: `cobot-hand-guiding-builder`, `iec62443-risk-assessment-builder`, `iso13849-plr-builder`
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 9 fresh / 29 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entry for 2026-06-26 DOCS

#### chore

- **plan** — W26 targets seeded Monday: 5 issues across 5 deferred domains (`64c0fb5`); see [docs/weekly/WEEK-2026-W26.md](docs/weekly/WEEK-2026-W26.md)

### Week 2026-W25 (2026-06-15 → 2026-06-21)

#### polish

- **interlock-estop-architecture-builder** (cell-design) — anchor descriptions on `ISO 14119:2013`, `ISO 13850:2015`, and `IEC 60204-1:2016`; add interlocking-device / E-stop / electrical-equipment edition references; log polish review (`70d9030`)
- **iso9283-performance-test-builder** (v&v) — anchor builder on `ISO 9283:1998` (manipulating industrial robots — performance criteria and related test methods) edition string; log polish review (`5442dcf`)

#### docs

- **CHANGELOG.md** — add W24 + W25 weekly sections (W24 was never recorded; closing the gap)
- **examples/** — stub READMEs for skills touched in W24/W25 lacking one: `interlock-estop-architecture-builder`, `iso9283-performance-test-builder`, `iso12100-risk-assessment-builder`
- **STATUS.md** — daily regeneration; 38/38 builders paired (100%), 0 missing reviewers, 6 fresh / 32 stale (30+ days)
- **docs/AUTONOMOUS_LOG.md** — daily journal entry for 2026-06-19 DOCS

### Week 2026-W24 (2026-06-08 → 2026-06-14)

#### polish

- **iso12100-risk-assessment-builder** (foundation) — anchor builder on `ISO 12100:2010` (safety of machinery — general principles for design, risk assessment and risk reduction) edition string; log polish review (`93b51a1`)

#### chore

- **plan** — seeded W24 targets: 5 issues across 5 deferred domains (`032175f`)

### Week 2026-W23 (2026-06-01 → 2026-06-07)

#### polish

- **iso15066-biomechanical-limits** pair — anchor descriptions on `ISO/TS 15066:2016` and `ISO 10218-1:2025`; add `ISO/TS 15066:2016` trigger keyword; note consolidation into ISO 10218-1:2025 Clause 5.11; fix wrong probe filename in reviewer file tree (`21c8e33`, closes W23 target #6)
- **operating-envelope** pair — anchor builder and reviewer on `ISO 3691-4:2020` (driverless industrial trucks); add standard anchor to lead paragraphs; refine STATUS.md domain-prefix matcher so all 10 domains resolve (`2a34ccb`, closes W23 target #7)
- **iso10218-compliance-matrix-builder** — fix 3 casing typos ("Iso10218" → "ISO 10218") inside SKILL.md; verify `ISO 10218-1:2025` and `ISO 10218-2:2025` edition strings in description (`7c0fc30`, closes W23 target #5)

#### docs

- **CHANGELOG.md** — first-time bootstrap of grouped weekly changelog (this entry)
- **examples/** — stub READMEs for every skill touched in W23 (iso10218-compliance-matrix-builder, iso15066-biomechanical-limits builder + reviewer, operating-envelope builder + reviewer)
- **STATUS.md** — daily regeneration; fresh-count now 3 builders (iso10218-compliance-matrix-builder, operating-envelope-builder, iso15066-biomechanical-limits-builder)
- **docs/AUTONOMOUS_LOG.md** — daily journal entries for 2026-06-01 PLAN, 2026-06-02 / 03 / 04 POLISH, and 2026-06-05 DOCS
- **docs/weekly/WEEK-2026-W23.md** — Monday plan: 5 polish targets across compliance / cobot / amr / ros2 / cybersecurity
- **docs/skill-polish-log/** — per-skill polish notes for iso10218-compliance-matrix-builder, operating-envelope-builder, iso15066-biomechanical-limits-builder
- **docs/monthly/2026-05.md** — May 2026 KPI rollup (`93e2167`)

#### chore

- **issues #5–#9** — weekly tracking issues filed for W23 polish targets (one per touched domain), each labeled `weekly-target` + domain label (`2f8b9ed`)
- **labels** — created `weekly-target`, `compliance`, `cobot`, `amr`, `ros2`, `cybersecurity`

#### outstanding (open W23 issues, deferred to next week)

- **#8 nav2-config-builder** (ros2) — no edit applied this week
- **#9 iec62443-risk-assessment-builder** (cybersecurity) — no edit applied this week

---

_This changelog starts at week 2026-W23 (first week with a `docs:`-mode autonomous run). Earlier history is summarized in the journal at [docs/AUTONOMOUS_LOG.md](docs/AUTONOMOUS_LOG.md) and the founding commits `27fa0da` / `94e3368` (76 skills seeded 2026-05-03)._
