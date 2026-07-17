# Changelog

All notable changes to the Robotics Skills Suite are documented in this file.

The format groups commits by week of the year. Within each week, entries are bucketed by conventional-commit type (`feat:` / `fix:` / `polish:` / `docs:` / `chore:`). Releases are tagged separately in [RELEASES.md](RELEASES.md).

## [Unreleased]

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
