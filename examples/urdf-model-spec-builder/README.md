# urdf-model-spec-builder — example

- **What this skill produces:** a 10-tab URDF/xacro robot model specification workbook — kinematic chain, link inertials, joint limits and safety-controller margins, collision and visual geometry, mesh asset catalog, `ros2_control` hardware interfaces and transmissions, actuator specs, Gazebo simulation parameters, validation checklist, and xacro macro index.
- **Typical input shape:** the target ROS 2 distro, a CAD-derived kinematic description (link names, joint types and axes, masses and inertia tensors), the actuator datasheets behind the joint limits, mesh asset paths with their export units, and whether the model is destined for simulation, real hardware, or both.
- **Expected output:** xlsx spec with a named distro baseline (Jazzy Jalisco or Lyrical Luth), an explicit URDF/xacro-versus-SDFormat boundary including any closed-loop limitation, collision geometry specified separately from visual, REP-103 units and REP-105 frame conventions applied throughout, and the Gazebo release matched to the distro (Jazzy→Harmonic, Kilted→Ionic, Lyrical→Jetty).
- **Sample input:** _TODO — add sample kinematic chain + actuator datasheet input._
- **Sample output:** _TODO — add generated URDF model spec xlsx._
