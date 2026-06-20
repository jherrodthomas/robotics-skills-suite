# Releases

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
