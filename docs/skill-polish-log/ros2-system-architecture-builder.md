# Polish log — ros2-system-architecture-builder

## 2026-07-16 (POLISH pass, W28 carryover target #33)

**What's good**
- Clear 11-tab output contract (node inventory, topic/service/action catalog, lifecycle, QoS, composition, executor topology, deployment).
- Frontmatter complete; description 405 chars, well under the 1024 limit, with concrete trigger phrases.
- Scope areas (lifecycle/managed nodes, DDS QoS, composition, executors) match current ROS 2 LTS practice and align with the nav2-config, tf-tree-spec, and behavior-tree-spec pairs.

**What to fix**
- Version claims were stale and factually wrong: listed "ROS 2 Iron LTS" — Iron Irwini was a **non-LTS** release and reached **EOL 2024-12-04**. Description also said "Humble or Iron LTS".

**Applied (small fix)**
- Replaced Iron with the current supported LTS set, verified 2026-07-16 against docs.ros.org and endoflife.date: Humble (EOL May 2027), Jazzy (EOL May 2029), Lyrical (EOL May 2031). Added explicit do-not-target note for Iron. Updated in both the description and the ROS 2 Versions section.

**Suggested edits (not applied — larger than a polish pass)**
- Body is thin (17 lines) relative to the safety-domain builders: add input-shape guidance, a tab-by-tab column spec, and a default DDS QoS profile catalog (sensor data, reliable command, transient-local config).
- Consider stating executor guidance (single vs multi-threaded, callback groups) as build rules rather than only a tab name.

**Paired reviewer (ros2-system-architecture-checklist-reviewer)**
- No version/edition claims present, so no lockstep fix was required. Suggest adding a "target distro is a currently supported LTS" check to the probe script — captured as follow-up for a future POLISH/PLAN pass.

**Severity:** medium — an EOL, non-LTS distro presented as LTS could steer production system designs onto unsupported infrastructure.

## 2026-09-15 (POLISH pass, W37 carryover target #58)

**What's good**
- The 11-tab output contract was sound and needed no restructuring — node inventory, catalog, lifecycle, QoS, composition, executor topology and deployment are the right decomposition of the problem.
- The 2026-07-16 fix held: no EOL distro claims, Iron correctly excluded as non-LTS.
- Description was well-formed and under limit on both halves.

**What was wrong**
- **The body was a glossary, not a method.** Nine lines listing tab names. Every one of the 2026-07-16 "suggested edits (not applied)" was still outstanding, and the skill had been selected three consecutive weeks as the second-thinnest builder in the suite.
- The reviewer was worse in kind: eight bullets restating the builder's tab names as "review scope", with no check, no rating vocabulary, and no statement of what failure looks like. A reviewer that lists topics cannot produce findings.
- **No safety boundary on either half.** This is the serious one. A ROS 2 architecture workbook that does not say a QoS profile is not a protective stop invites exactly that mistake, and this suite contains the rated-hardware skills that should own it.
- No frame/link vocabulary reconciliation, despite `tf-tree-spec` (#52), `urdf-model-spec` (#49) and `nav2-config` (#54) all landing in the last four weeks and all inheriting spelling from here.
- The distro table omitted Kilted Kaiju entirely, where the downstream `nav2-config` pair lists it with an explicit do-not-baseline verdict. Silence upstream, warning downstream.

**Applied**
- Builder rewritten from 9 body lines to a method: decomposition by failure domain and rate domain with consequence-of-absence required per node; a QoS data-class table with the compatibility, `transient_local` late-joiner and history-depth rules stated; executors and callback groups including the synchronous-service reentrancy deadlock; lifecycle justification and bringup-as-dependency-graph; namespace and remapping conventions; faults and degraded modes with named detectors.
- Distro table brought into lockstep with `nav2-config` (Lyrical / Kilted / Jazzy / Humble, Iron EOL), including Kilted's do-not-ship verdict. Baseline declared **inherited from `urdf-model-spec`, URDF wins on conflict** — matching the rule `nav2-config` already applies, rather than inventing a second precedence.
- **Safety boundary section added to both halves**, with the reviewer rating any ROS 2 mechanism presented as a risk reduction measure as its highest-severity NO.
- Reviewer rewritten as nine numbered check groups with FC/LC/PC/NO/NA ratings and explicit NO conditions.
- `## Implementation status` added to both halves (see below).

**Verification**
- Distro table verified 2026-09-15 by web search against the ROS 2 distribution list and endoflife.date: Lyrical Luth May 2026 → EOL May 2031; Kilted Kaiju May 2025 → EOL Nov 2026. Consistent with the baseline b52ef25 set in `nav2-config`. Not a safety-critical domain, so the mandatory edition step did not fire — the distro check was run anyway because the plan asked for it.
- `audit_pair_editions.py` re-run: pair not listed before or after; the 16-claim asymmetry backlog is unchanged and still outstanding (see follow-ups).
- Both archives repacked and `unzip -t` clean. Descriptions 850 / 784 chars, both under the 1024 ceiling.

**Implementation status**
The builder ships **no generator script at all** — only the shared `recalc.py` and `office/` helpers. The reviewer's probe is a one-line placeholder. This is the same condition `audit_reviewer_impl.py` found in 32 of 38 reviewers and that the iso10218 pass flagged on 2026-09-08; both halves now carry an explicit `## Implementation status` section so the documented contract is not mistaken for working code.

**Severity:** high — not for factual error, but for absence. A production ROS 2 architecture document with no QoS compatibility rule, no reentrancy warning and no safety boundary is a document whose most expensive failure modes are the ones it does not mention.
