# Changelog

All notable changes to the Robotics Skills Suite are documented in this file.

The format groups commits by week of the year. Within each week, entries are bucketed by conventional-commit type (`feat:` / `fix:` / `polish:` / `docs:` / `chore:`). Releases are tagged separately in [RELEASES.md](RELEASES.md).

## [Unreleased]

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
