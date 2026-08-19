# Polish log — urdf-model-spec (builder + checklist-reviewer)

## 2026-08-19 (autonomous POLISH run) — severity: **high**

**Target selection.** W34 target 2 of 3, issue [#49](https://github.com/jherrodthomas/robotics-skills-suite/issues/49), scheduled for Wednesday by the W34 plan. Also satisfies priority rule (3) independently — both halves sat at the 2026-05-03 import baseline, tied least-recently-touched. Rules (1) and (2) selected nothing: no issue carries `skill-bug` or `reviewer-finding`, and the suite has been 38/38 paired since W29.

**What's good**
- The 10-tab structure is the right decomposition for a robot description: chain → link properties → joint limits → collision → visual → transmissions → actuators → simulation → validation → macro index. Nothing needed reordering.
- Both halves have complete frontmatter, and `name` matches file and internal directory in each.
- The reviewer's verification list already mirrored the builder's tabs one-for-one, so the pair was structurally in lockstep before this pass even though both halves were thin.
- The builder already separated collision from visual as distinct tabs — the concept was present, only the rule was missing.

**What to fix**
1. **No ROS 2 distro baseline (primary, and the DoD's first item).** `## ROS Standards` read `ROS URDF specification` with no distro named anywhere in either half. A robot description is only valid against a distro: `ros2_control` interface names, Gazebo plugin names, and the `gz`/`ign` prefix split all move between releases. Un-baselined, the reviewer has nothing to check currency *against*, which is why the reviewer also had no currency check.
2. **"Gazebo or Ignition" — stale on two counts.** Ignition Gazebo was renamed **Gazebo** in 2022, so "Ignition" names a project that no longer exists under that name. Separately, **Gazebo Classic 11 reached end-of-life 2025-01-31**, so the other reading of the phrase points at a dead simulator. The file offered both wrong options and no right one.
3. **URDF/SDF boundary absent** — the DoD's second item, and the defect that actually breaks models. Closed kinematic loops (parallel linkages, four-bars, differentials) *cannot* be expressed in URDF, and nothing in either half said so or asked for the limitation to be declared. A spec that silently omits a four-bar produces a model that is wrong in a way no syntax check catches.
4. **Collision-vs-visual stated as two tabs but with no rule.** Reusing the detailed visual mesh as collision geometry is the highest-frequency real defect in URDF work, and neither half prohibited it or asked why they were identical.
5. **Inertial plausibility unaddressed.** The reviewer said "inertial property values and reasonableness" without defining reasonable. Mass > 0 and the triangle inequality on principal moments are mechanical checks; without them, identity tensors ship.
6. **`ros2_control` not covered — only ROS 1 `<transmission>`.** The builder's "transmission types" tab is the ROS 1 `ros_control` mechanism. Under ROS 2 the `<ros2_control>` block carries hardware components and command/state interfaces, and legacy `<transmission>` tags carried over from ROS 1 are inert. The workbook was specifying the wrong element.
7. **REP-103 / REP-105 never cited** — the DoD's frame-naming item. Units, axis orientation, and the `map`/`odom`/`base_link` boundary were all left implicit, which is precisely the vocabulary `tf-tree-spec` and `nav2-config` inherit.
8. **No downstream-consumer section.** The W34 plan picked URDF *first in the ros2 cluster* on the reasoning that `tf-tree-spec` and `nav2-config` consume what it defines. Neither half recorded that dependency, so the ordering rationale existed only in the plan file.
9. **Reviewer had no standards baseline section** — same chain break corrected in `robot-acceptance-protocol` (6244fd2) and `robot-hil-test-catalog` (8ba1789): a reviewer that cannot name what it checks against cannot flag a stale spec.

**Edits applied**
- Builder description: rewritten to name `ros2_control` explicitly, drop "Ignition", and state the three load-bearing additions (distro baseline, URDF/SDFormat boundary, REP-103/105). 583 chars, under 1024. Kept all original trigger phrasings and added `robot description`.
- Builder: new `## ROS 2 distro baseline` with a four-row support table and an explicit default (**Jazzy**, on driver availability; **Lyrical** where the 26.04 target or the five-year window governs; **not Kilted** for anything shipping).
- Builder: new `## Scope boundary — URDF/xacro vs SDFormat`, with closed loops called out as the hard boundary and a required declared mitigation.
- Builder: new `## Link, joint, and geometry conventions` — collision-vs-visual rule, inertial plausibility and provenance, the three `<limit>` numbers plus `<safety_controller>`, fixed-joint collapse, and `package://` mesh paths with per-mesh unit and scale.
- Builder: new `## Units and frame conventions — REP-103 and REP-105` (plus REP-120 where humanoid), with the `base_link` ownership boundary stated.
- Builder: `## ros2_control transmissions and hardware interfaces` replacing the bare transmission mention, including the legacy-`<transmission>`-tag trap and the controller-manager update rate.
- Builder: `## Simulation parameters — Gazebo naming` with the rename, the Classic EOL date, and the distro↔Gazebo pairing table (Lyrical→Jetty, Kilted→Ionic, Jazzy→Harmonic, bridge `ros_gz`).
- Builder: new `## Downstream consumers` and `## Related skills`, including the caveat that URDF collision geometry is **not** a safety-rated envelope — separation distances come from `ssm-plan-builder` / `operating-envelope-builder`.
- Reviewer description: rewritten in lockstep to enumerate the same check families. 628 chars.
- Reviewer: added `## Distro baseline checks`, `## Scope-boundary checks`, `## Geometry, inertial, and joint checks`, `## Units and frame conformance`, `## ros2_control checks`, `## Simulation currency checks`, `## Downstream-consumer checks`, and `## Standards baseline`; each mirrors a builder rule one-for-one. Added the "does not modify the source workbook" line the other polished reviewers carry.
- `examples/urdf-model-spec-builder/README.md` stub created.

**Version verification** (ros2 is outside the mandatory safety-critical set, but every reference here is version-dated, so the check was run — and it produced the two largest findings)
- **Lyrical Luth** — confirmed released **2026-05-22**, LTS, Ubuntu 26.04 "Resolute" as Tier 1, supported to **May 2031**. This is the current LTS and did not exist when the file was imported.
- **Kilted Kaiju** — GA 2025-05-23, standard release, support ends **November 2026**. Recorded as an explicit do-not-baseline for shipping work; this is three months away and will become a live finding on any spec picked up on Kilted.
- **Jazzy Jalisco** — LTS, to May 2029. Chosen as the default baseline on driver and `ros2_control` support breadth rather than on recency.
- **Humble Hawksbill** — LTS, to May 2027. Legacy-fleet only.
- **Gazebo Classic 11 EOL confirmed 2025-01-31**; Ignition→Gazebo rename confirmed 2022. Both written into the builder and made explicit findings in the reviewer.
- Distro↔Gazebo pairing confirmed: Jazzy↔Harmonic, Kilted↔Ionic, Lyrical↔Jetty, bridge `ros_gz` throughout.
- REP-103 (units/axis), REP-105 (mobile-platform frames), REP-120 (humanoid frames) — numbers confirmed against ros.org REP index; these are stable and unversioned.

**Not done (deliberately descoped)**
- Same structural gap as the rest of the suite: the builder ships no generator script (only `recalc.py` and the shared `office/` helpers), and the reviewer's `check_definitions.py`, `dashboard.py`, and `urdf-model-spec-checklist_probe.py` remain 32–59 byte placeholder stubs. Writing them is a refactor, not a polish edit.
- Did **not** touch `tf-tree-spec` or `nav2-config` to reference the conventions this pass declares. The dependency is now recorded from the URDF side one-directionally; the reciprocal edits belong to those skills' own targets (W35 per the plan, tf before nav2).
- Did **not** attempt to pick a single suite-wide distro baseline. `ros2-system-architecture` (polished 2026-07-16) may state a different one; reconciling them is a cross-file decision, captured below.

**Follow-ups**
- **Check `ros2-system-architecture-builder` for a conflicting or absent distro baseline.** It was polished 2026-07-16, before Lyrical's support window was a consideration in this repo. If it names a distro, the two must agree; if it names none, it has the same primary defect this pass just fixed.
- `tf-tree-spec` and `nav2-config` are both still at import baseline and will carry the same missing-REP-105 and missing-distro defects. W35, tf first.
- **Repo-wide grep for `Ignition` and `Gazebo Classic`.** This file had both; `nav2-config` and `ros2-system-architecture` are the likely other carriers, and the reviewer halves will not catch it because most of them have no standards baseline.
- **Time-boxed watch item: Kilted Kaiju leaves support November 2026.** Any spec baselined on it becomes non-current in roughly three months. Worth a sweep in W44–W46.
