# Releases

## v2026.09.W3 — 2026-09-19

**Highlights:** Weekly snapshot for ISO week **2026-W38** (Mon 2026-09-14 → Sat 2026-09-19). Three POLISH passes landed and all three closed pair-complete — `ros2-system-architecture`, `robot-field-acceptance`, `zone-conduit-plan` — but **the week ran without a plan**: the Monday PLAN slot did not execute, so no `docs/weekly/WEEK-2026-W38.md` exists and no definition-of-done was recorded before the work. The more consequential news is that **two target selectors died this week**. Builder body-thinness is exhausted — `robot-field-acceptance` was the last inverted pair (reviewer more substantive than its builder) — and the open-issue backlog is now *empty*: this run queried the API and got **0 open issues** after the 2026-09-11 bulk close of #37–#59, which also closed #59 (the edition-asymmetry sweep) without the work being done. From W39 the PLAN run has neither priority rule (a) nor thinness to select on; staleness and domain rotation are all that remain. Suite holds at 76 .skill files, 38/38 paired, zero orphans, examples coverage 76/76.

**Tag-count correction:** this is the **twelfth tag** in the series. `v2026.09.W1` described itself as the twelfth snapshot; it was the eleventh tag. The drift comes from counting skipped Saturdays as snapshots.

**Note on the gap:** no `v2026.09.W2` tag exists. W37 (2026-09-07 → 09-12) produced two commits — the PLAN seed (`0b66a11`) and one polish pass (`4db26d8`) — but its Friday, Saturday and Sunday runs did not fire, so the week was never tagged and never got a DOCS pass; W37's work is covered by this tag's compare range. This is the **second missed Saturday in four weeks** (W35, W37).

**Changes this week (2026-09-14 → 2026-09-19):**

*polish:*
- **ros2-system-architecture** pair (ros2) — W37 carryover, second-thinnest builder in the suite and named three weeks running without being taken. Builder rewritten from a nine-line glossary of tab names into a method: decomposition by failure domain and rate domain with consequence-of-absence required per node; a QoS data-class table carrying compatibility, `transient_local` late-joiner and history-depth rules; executors and callback groups including the synchronous-service reentrancy deadlock; lifecycle justification and bringup-as-dependency-graph; faults and degraded modes with named detectors. Distro table brought into lockstep with `nav2-config` and declared **inherited from `urdf-model-spec`, URDF wins on conflict**, rather than inventing a second precedence rule. **Safety boundary added to both halves** — the reviewer now rates any ROS 2 mechanism presented as a risk reduction measure as its highest-severity NO, the defect the old pair was silent on (`2048716`)
- **robot-field-acceptance** pair (v&v) — the **last inverted pair**, selected by both available measures at once (joint-oldest builder at 136 days, thinnest remaining at 9 body lines against 14). The builder named metrics without defining any; it now carries an OEE table giving each factor its definition and required denominator, with **ideal cycle time required to come from demonstrated rather than quoted performance**, and starved/blocked time captured as its own state from the first interval since it is the largest source of disputed availability at handover and cannot be reconstructed afterwards. **Boundary added to both halves:** no safety conformity is granted here — that is the integrator's declaration under ISO 10218-2:2025 (`dcf516f`)
- **zone-conduit-plan** pair (cybersecurity) — least-recently-touched builder in a safety-critical domain, so the mandatory edition step fired and found both halves saying a bare "IEC 62443" for a family spanning a dozen parts. Now dated per part: partitioning **IEC 62443-3-2:2020** (ZCR 1–7), SL1–SL4 and FR1–FR7 **IEC 62443-3-3:2013**, component capability **IEC 62443-4-2:2019**. **SL-T split from SL-C and SL-A** — collapsing the three invites the failure where a target/achieved gap is closed by quietly lowering the target. ZCR 3.1–3.5 stated as five checkable conditions (`7ac735d`)

*fix:*
- **ISO 13855 retitled at the 2024 edition** — "Positioning of safeguards with respect to the approach of the human body". The 2010/2002 title is what most secondary sources still repeat and what the first draft of the `robot-field-acceptance` rewrite carried. Caught by verifying rather than assuming (`dcf516f`)
- **ISO 13849-2 supersession watch** — :2012 is current (confirmed 2018) but ISO/DIS 13849-2 is at enquiry stage. Both halves of the `robot-field-acceptance` pair now say so; other 13849-2 citations in the repo do not (`dcf516f`)

*docs:*
- **README.md** — IEC 62443 family dated per part to match what `zone-conduit-plan` now pins; ISO 13849-2:2012 (DIS noted), ISO 13855:2024 and IEC 60204-1:2016 added. Skill table unchanged at 38 pairs (`e8e512c`)
- **CHANGELOG.md** — W38 section (`e8e512c`)
- **STATUS.md** — regenerated every run via `scripts/gen_status.py`
- **docs/skill-polish-log/** — three logs appended (not overwritten — the W37 failure mode)

**Skills inventory:** 38 builders · 38 reviewers · **100% paired** (76 .skill files). Freshness: **10 builders 🟢** touched ≤30d, **28 🟡** stale at 30+d, **0 orphans 🔴**. Examples coverage: **76/76 (100%)**. Domain spread: ai-ml 3 · amr 4 · cell-design 4 · cobot 4 · compliance 5 · cybersecurity 3 · foundation 3 · operational 3 · ros2 5 · v&v 4.

**Audits re-run at snapshot time** (all three committed scripts, measured this run rather than quoted from last week):

| Audit | Result | Δ since v2026.09.W1 |
| --- | --- | --- |
| `audit_reviewer_impl.py` | 6 tier A · 16 tier B · 16 tier C | `zone-conduit-plan` C → A (only tier change in three weeks) |
| `audit_pair_editions.py` | 38 pairs · 2 mismatch · 9 asymmetry | mismatches 1 → 2 (both documented supersessions, not defects); asymmetries 10 → 9 |
| phantom `references/` in SKILL.md | 15 reviewers | 16 → 15 (`zone-conduit-plan` manifest corrected) |

**Resolved this week — removed from the carried list:**
- **ISO 13855 title sweep is clean.** W38's DOCS pass flagged "any skill citing 13855:2024 under the old title has a right year on a wrong name — suite-wide check outstanding". Run this snapshot: **4 skills cite ISO 13855; 3 state a title and all 3 use the 2024 title; 1 cites the year only. Zero carry the pre-2024 title.** The flag was precautionary and the sweep closes it. No action needed.

**Carried defects (human attention):**
- **Placeholder-generator defect — sixth consecutive snapshot.** 6 reviewers implemented, 16 stub, 16 with no generator at all. One tier moved in three weeks, and only because a polish pass happened to land on it. At that rate the 32 non-A reviewers clear in 2028. This cannot be fixed by POLISH passes; it needs a dedicated implementation week that only a human can authorize. Reviewer descriptions remain deliberately silent on check counts and dashboards as a consequence.
- **Rule (a) is not broken any more — it is dead.** Open issues: **0**. For four weeks this list said "one human bulk-close restores the signal"; the bulk-close happened on 2026-09-11 and the result is that priority rule (a) now returns nothing because there is nothing to return. The PLAN run needs either a standing practice of filing issues for known debt (the placeholder tiers, the 9 edition asymmetries, the 15 phantom manifests are ~24 filable items) or rule (a) should be retired from the task file.
- **Selector exhaustion.** Thinness is spent — no inverted pairs remain. W39 PLAN has only staleness and domain rotation, and staleness alone rotates the same 28 🟡 builders indefinitely without ever asking whether a pass is *warranted*. A `scripts/audit_pair_balance.py` (proposed at v2026.09.W1, not built) or issue-backed debt would restore a second axis.
- **Scheduled-run reliability, now affecting weekdays.** W35 lost Fri/Sat/Sun, W37 lost Fri/Sat/Sun, W38 lost **Monday**. Three missed slots in four weeks and the first weekday miss. Worth checking whether the 7:30 task is actually firing, rather than continuing to reconstruct weeks from git after the fact.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.09.W1...v2026.09.W3

## v2026.09.W1 — 2026-09-05

**Highlights:** Twelfth tagged weekly snapshot and the first September tag, covering the 2026-W36 working week (Mon 2026-08-31 → Sat 2026-09-05). **Fourth consecutive 3-of-3 week, zero carryover.** W36 selected its targets by *body thinness* rather than staleness, and the selection surfaced a structural pattern: every builder under ten body lines was an **inverted pair** — a reviewer more substantive than the builder it reviews. All three were taken (`nav2-config`, `iso9283-performance-test`, `operator-training-matrix`) and all three landed pair-complete. `nav2-config` produced the repo's first **wrong-edition** (rather than missing-edition) defect: the builder pinned Iron Irwini, end-of-life since November 2024, so the pair would have passed a configuration built on an unsupported distro. The `urdf → tf → nav2` sequence opened in W34 closed on Tuesday. Suite holds at 76 .skill files, 38/38 paired, zero orphans, examples coverage 76/76.

**Note on the gap:** no `v2026.08.W5` tag exists. The 2026-08-28 → 08-30 DOCS/RELEASE/TRIAGE runs did not execute; W35's three landed polish commits were backfilled into CHANGELOG.md on 2026-09-04 and are covered by this tag's compare range.

**Changes this week (2026-08-31 → 2026-09-05):**

*plan:*
- seed W36 with three inverted-pair targets across ros2, v&v and operational; issues #54–#56. Ships `scripts/audit_pair_editions.py`, extending the builder↔reviewer edition-agreement check from 5 compliance pairs to all 38 (result: 1 benign supersession note, 10 asymmetries, no false claims) (`3ea30de`)

*polish:*
- rebaseline `nav2-config` pair off EOL Iron onto Jazzy / Kilted / Lyrical, inherited from `urdf-model-spec` (#49) rather than re-derived; add the cross-distro deltas that silently break bringup (`enable_stamped_cmd_vel` Twist→TwistStamped at Kilted, `nav2_ros_common` / `nav2::LifecycleNode` at Lyrical), a byte-identical frame contract with `tf-tree-spec`, footprint-derived inflation, lifecycle ordering, and an explicit non-safety-rated boundary; closes the urdf→tf→nav2 chain (#54) (`b52ef25`)
- rewrite `iso9283-performance-test` pair — thinnest builder in the repo, 6 body lines → 55. Defines AP vs RP vs path accuracy, states test cube / five poses / load / velocity / cycle conditions as numbers, requires measurement uncertainty stated relative to claimed tolerance (≤ 25 % as common practice referenced to ISO/TR 13309, *not* as a 9283 requirement), and draws boundaries against `robot-acceptance-protocol` and against any safety claim. ISO 9283:1998 confirmed current at iso.org (stage 90.60) (#55) (`e9cdbaa`, log fix-up `159b5c5`)
- rewrite `operator-training-matrix` pair — last operational builder at import baseline, 7 body lines → 66. OSHA 1910.147(c)(7) authorized/affected/other status carried as an attribute separate from role; every row splits training *delivered* from competency *demonstrated* with an evidence type; retraining driven by the five (c)(7)(iii) conditions rather than a bare interval — the original builder had the interval and none of the conditions, the regulation is the reverse. **ANSI/ASSP Z490.1-2024** new to the suite (#56) (`d88845e`)

*docs:*
- August KPI report (`docs/monthly/2026-08.md`) — 29 commits, 27 skills touched, 4 releases; first month the 60+-day staleness curve bent (48 → 33). Records that the June/July `iso3691-4` "defect" was a false positive caused by a stale row in the task file — current edition is **ISO 3691-4:2023**, not :2020 (`0fbfb0d`)
- W36 changelog, W35 backfill, and three stale README corrections (R15.06-2012 R2017 → ANSI/A3 R15.06-2025; ISO 3691-4:2020 → :2023; ROS 2 Humble/Iron → Jazzy/Lyrical) (`0f366be`)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Freshness: 12 builders 🟢 touched ≤30d, 26 🟡 stale at 30+d, 0 orphans 🔴. Examples coverage: **76/76 (100%)**. Domain spread: ai-ml 3 · amr 4 · cell-design 4 · cobot 4 · compliance 5 · cybersecurity 3 · foundation 3 · operational 3 · ros2 5 · v&v 4.

**Carried defects (human attention):**
- **Placeholder-generator defect — fifth consecutive snapshot, and it is worse than recorded.** `scripts/audit_reviewer_impl.py` (shipped W35) measured the real scope: **6 reviewers implemented, 16 stub, 16 with no generator at all** — not the 4 pairs carried on this list since v2026.08.W2. Reviewer descriptions have been deliberately written to claim no check counts or dashboards as a consequence. Polish passes cannot resolve this; it needs a dedicated implementation week that only a human can authorize.
- **Open-issue count is now fully broken as a signal.** Twenty issues open (#37–#56); all twenty describe work that has shipped. This task never closes issues by design, so PLAN priority rule (a) — "skills referenced by open issues" — has selected nothing for four consecutive planning runs. One human bulk-close of #37–#56 restores it.
- **The weekend runs are unreliable.** W35 lost its Friday, Saturday and Sunday runs entirely and no one noticed until the following Friday's DOCS pass reconstructed the week from git. Worth checking whether the 7:30 scheduled task actually fires on weekends.
- **Inverted pairs are a measurable defect class.** Three of three W36 targets were reviewers more substantive than their builders. Nothing currently audits for this; a `scripts/audit_pair_balance.py` would make the remaining cases selectable instead of discovered by accident.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.08.W4...v2026.09.W1

## v2026.08.W4 — 2026-08-22

**Highlights:** Eleventh tagged weekly snapshot, covering the 2026-W34 working week (Mon 2026-08-17 → Sat 2026-08-22). **Second consecutive 3-of-3 week, zero carryover** — and the first week where all three targets were *import-baseline* pairs, skills untouched since the 2026-05-03 import. Three clusters that had never had a POLISH pass — v&v (`robot-hil-test-catalog`), ros2 (`urdf-model-spec`), ai-ml (`dataset-documentation`) — each now carry an edition-anchored, lockstep-reviewed pair. Friday's DOCS run cleared two long-standing structural debts in one pass: **examples coverage closed 42/76 → 76/76 (100%)**, retiring a follow-up that at the prior 2-per-week rate would not have cleared until 2027, and the STATUS generator became a committed script (`scripts/gen_status.py`) instead of being rebuilt in `/tmp` every run — the same two defects had been re-introduced and lost three separate times. Suite holds at 76 .skill files, 38/38 paired, zero orphans.

**Changes this week (2026-08-17 → 2026-08-22):**

*plan:*
- seed W34 with three import-baseline targets across v&v, ros2, ai-ml; issues #48–#50 (4dc22b1)

*polish:*
- anchor robot-hil-test-catalog pair on ISO 13849-1:2023 / -2:2012, add HIL-vs-FAT scope boundary and `HIL-<function-id>-<class>-<nn>` case-ID convention; ISO/DIS 13849-2 flagged do-not-bump (#48) (8ba1789)
- baseline urdf-model-spec pair on a dated ROS 2 distro table (Jazzy default, Kilted do-not-ship on Nov 2026 EOL), fix stale Ignition / Gazebo Classic naming, pin REP-103 / REP-105, replace ROS 1 transmissions with `ros2_control` (#49) (df811d4)
- give dataset-documentation a citable `<dataset-id>@<version>` ID consumed by model-card, date the governance baseline (ISO/IEC 42001:2023, 23894:2023, 5259, EU AI Act 2024/1689 Art. 10), correct reviewer tab count 7 → 5 (#50) (662de6b)

*docs:*
- close examples coverage to 76/76, commit STATUS generator, W34 changelog (46166a8)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Freshness: 12 builders 🟢 touched ≤30d, 26 🟡 stale at 30+d, 0 orphans 🔴. Examples coverage: **76/76 (100%)**. Domain spread: ai-ml 3 · amr 4 · cell-design 4 · cobot 4 · compliance 5 · cybersecurity 3 · foundation 3 · operational 3 · ros2 5 · v&v 4.

**Carried defects (human attention):**
- **NEW — five reviewers carry their builder's `description:` verbatim.** `ansi-r1506-compliance-matrix`, `iec62061-sil`, `iso10218-compliance-matrix`, `iso12100-risk-assessment` and `iso13849-plr` checklist reviewers all describe *generating* a workbook rather than reviewing one, so triggering will be unreliable for all five. All five sit in the safety-critical compliance/foundation clusters. Surfaced by Friday's DOCS batch pass; each affected `examples/*/README.md` carries a warning banner. **No issue exists for this** — RELEASE runs do not create issues, so it needs either a human issue or a W35 PLAN slot. Strong candidate for a single themed polish week, since the fix is the same edit five times.
- **Placeholder-generator defect — fourth consecutive snapshot, still unfixed.** `robot-sop`, `machinery-safety-lifecycle-plan`, `fleet-manager-architecture` and `behavior-tree-spec` ship placeholder or absent generator scripts. Polish passes cannot resolve it; it needs a dedicated implementation week. Escalating: four snapshots of documentation without action means the standing process is not going to fix this.
- **Open-issue count remains a broken signal.** Fourteen issues open; all fourteen (#37–#50) describe work that has shipped. This task never closes issues by design, so priority rule (a) — "skills referenced by open issues" — has now selected nothing for two consecutive PLAN runs and will keep selecting nothing. One human bulk-close before W35 planning restores the signal.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.08.W3...v2026.08.W4

## v2026.08.W3 — 2026-08-15

**Highlights:** Tenth tagged weekly snapshot, covering the 2026-W33 working week (Mon 2026-08-10 → Sat 2026-08-15). **All three planned targets landed, pair-complete — the first clean sweep in the repo's history.** W33 was also the first week the plan set capacity to observed throughput (3) rather than aspiration (5), and the carryover queue did not grow. `declaration-of-conformity` (#44, open four weeks) finally cleared and now forks correctly on **EU Machinery Regulation 2023/1230** vs the superseding Directive 2006/42/EC; `safety-io-matrix` (#45) was reconciled with the `interlock-estop-architecture` pair and pinned to **ISO 13849-1:2023** + **IEC 62061:2021** with a SIL-CL cross-reference; `robot-acceptance-protocol` (#47) opened the v&v cluster — previously untouched since the 2026-05-03 import baseline — on **ISO 9283:1998** and **ISO 10218-2:2025**. Examples coverage crossed the halfway line at 38/76 (50%). Suite holds at 76 .skill files, 100% paired, zero orphans.

**Changes this week (2026-08-10 → 2026-08-15):**

*plan:*
- seed W33 with three targets — two carryovers plus v&v beachhead (e246935)

*polish:*
- rewrite declaration-of-conformity pair, fork on Directive vs Regulation 2023/1230 (aadcd83)
- anchor robot-acceptance-protocol pair on ISO 10218-2:2025, add reviewer standards baseline (6244fd2)
- pin safety-io-matrix pair to ISO 13849-1:2023, IEC 62061:2021, add SIL CL cross-reference (d909fc2)

*docs:*
- W33 changelog, two v&v example stubs, STATUS refresh (a8ca532)

**Skills inventory:** 38 builders · 38 reviewers · 100% paired (76 .skill files). Domain health: 10 builders touched within 30 days, 28 stale (30+ days), 0 orphans. Examples coverage: 38/76 skills (50%).

**Carried defects (human attention):**
- The **placeholder-generator defect** first recorded in v2026.08.W2 is unchanged. At least four pairs — `robot-sop`, `machinery-safety-lifecycle-plan`, `fleet-manager-architecture`, `behavior-tree-spec` — ship placeholder or absent generator scripts. Three consecutive snapshots have now documented this without fixing it. Polish passes cannot resolve it; it needs a dedicated implementation week.
- **Open-issue count is a broken signal.** Eleven issues are open; at least six of them (#42, #43, #44, #45, #46, #47) describe work that has already shipped. This task never closes issues by design, so the backlog only shrinks when a human closes it. Recommended before W34 planning.

**Compare:** https://github.com/jherrodthomas/robotics-skills-suite/compare/v2026.08.W2...v2026.08.W3

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
