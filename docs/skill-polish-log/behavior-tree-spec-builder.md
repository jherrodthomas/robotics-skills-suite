# Polish log: behavior-tree-spec-builder (+ paired reviewer)

## 2026-07-28

**Reviewed:** `behavior-tree-spec-builder.skill` and `behavior-tree-spec-checklist-reviewer.skill`
(W31 target #1, issue [#40](https://github.com/jherrodthomas/robotics-skills-suite/issues/40) — W30 carryover; also tied for least-recently-touched at the 2026-05-03 import baseline, 86 days.)

**What's good**
- Trigger phrases were already reasonable (behavior tree, BT.CPP, BehaviorTree.CPP, Nav2 BT, robot mission tree).
- The 10-tab output outline is the right decomposition for a BT spec: methodology → control/action/condition nodes → decorators → blackboard → ports → recovery → XML validation → visualization.
- Builder and reviewer scopes were already mirror images of each other — the pair concept was sound, only the content was thin.

**What was fixed this pass (small, applied)**
- **Version anchored on BehaviorTree.CPP v4.x** in both descriptions and bodies (was unversioned "BehaviorTree.CPP library"). v4 is the current major line; v3 trees and Groot-1-only palettes are now explicitly a reviewer finding rather than an accepted input.
- **Groot2 named as the v4 tool.** The original Groot targets v3.x only — confirmed against the Nav2 docs, which state Groot is for BT.CPP v3.x and Groot2 for v4.x.
- **Nav2 nodes correctly framed as project plugins, not BT.CPP built-ins** (`ComputePathToPose`, `FollowPath`, `RecoveryNode`, `PipelineSequence`, `RoundRobin`, `RateController`, Spin/BackUp/Wait/ClearCostmap). Nav2 docs are explicit that Groot2 must be pointed at a Nav2 node palette because it knows only BT.CPP defaults. This was the single most misleading gap in the old text.
- **Concrete v4 node vocabulary added:** control nodes (Sequence, SequenceWithMemory, ReactiveSequence, Fallback, ReactiveFallback, Parallel) and decorators (Inverter, Retry, Repeat, Timeout, Delay, Precondition); `SKIPPED` noted alongside SUCCESS/FAILURE/RUNNING/IDLE.
- **ROS 2 LTS baseline cross-referenced** to `ros2-system-architecture-builder` (Humble / Jazzy / Lyrical) so the two ros2-domain skills stop drifting apart.
- **Reviewer given a real audit-scope table** (9 areas with what-is-checked per area) replacing an eight-bullet list, and an explicit reactivity/port-direction/subtree-remapping check — the three things most often wrong in real BT designs.
- **File trees added and made accurate** in both SKILL.md files, per the repo convention. Neither file previously had one.
- Both skills now follow the repo's polished layout: When to use / Workflow / Output structure / baseline / Files in this skill.

**What still needs fixing (not applied — too large for a polish pass)**
- **HIGH — reviewer is a hollow shell.** `behavior-tree-spec-checklist_probe.py`, `check_definitions.py`, and `dashboard.py` are each a **single comment line**. There is no `generate_checklist.py` at all. The reviewer cannot currently run against a workbook; the SKILL.md now says so explicitly rather than implying a working tool. Needs a real probe + check definitions + dashboard, same shape as `pfl-plan-checklist-reviewer`.
- **HIGH — builder has no generator.** Only `recalc.py` and `office/` ship. There is no `generate_behavior_tree_spec.py`, so the promised 10-tab XLSX is not actually produced by the skill. Same class of defect logged for `pfl-plan-builder` on 2026-07-22 and `machinery-safety-lifecycle-plan-builder` on 2026-07-23 — this is looking structural across the import baseline, not incidental.
- **MED — v4 node-name specifics warrant a human check.** `SKIPPED` and the v4 rename of `SequenceStar` → `SequenceWithMemory` are stated from working knowledge; the Nav2/Groot2 relationship was verified against docs but the per-node list was not read off the BT.CPP v4 API reference this pass. Worth one confirming pass by someone with the library open.
- **LOW — no `examples/` worked example.** Stub created this run; real sample I/O still missing.

**Severity:** high (both halves of the pair are non-functional scaffolds), med (v4 node-name verification), low (examples)

**Lockstep:** yes — builder and reviewer edited in the same pass, per the W30 convention.
