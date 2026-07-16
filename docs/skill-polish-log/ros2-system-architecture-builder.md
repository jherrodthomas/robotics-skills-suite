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
