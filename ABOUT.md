# About — Robotics Skills Suite

## GitHub repo "About" sidebar (paste into the repo settings)

**Description (340 chars max):**

> 76 audit-ready Claude skills automating the industrial robot, cobot, AMR, ROS2, V&V, AI/ML, and IEC 62443 lifecycle. 38 builder + reviewer pairs anchored to ISO 10218, 13849, 62061, 12100, 9283, 15066, 3691-4 and IEC 62443. Same chain-compounding pattern as the automotive-skills-suite.

**Website:** `https://github.com/jherrodthomas/robotics-skills-suite`

**Topics (comma-separated, paste into "Add topics"):**

```
claude, claude-skills, anthropic, robotics, industrial-robotics, cobot, amr, ros2, ros, functional-safety, machinery-safety, iso10218, iso13849, iec62061, iso12100, iso15066, iso3691-4, iec62443, ot-cybersecurity, machine-vision, model-cards, datasheets-for-datasets, behaviortree, nav2, urdf, fat-sat, ce-marking
```

---

## Long-form About (already embedded in README.md)

The Robotics Skills Suite is a curated set of 38 builder + 38 matching reviewer skills that automate every structured xlsx deliverable in the modern industrial-robotics lifecycle — from ISO 12100 risk assessment through ISO 13849-1 PLr / IEC 62061 SIL determination, ISO 10218-2:2025 / ANSI R15.06 compliance matrices, ISO/TS 15066 cobot biomechanics, ISO 3691-4 AMR risk, OSHA 1910.147 LOTO, ROS2 architecture artifacts, ISO 9283 performance verification, FAT/SAT acceptance protocols, AI/ML governance (datasheets, model cards), and IEC 62443 industrial cybersecurity.

Every builder produces a multi-tab audit-ready xlsx workbook. Every reviewer produces a confirmation-measures checklist over that workbook with a visual dashboard (KPI tiles, pie chart, compliance bar, stacked rating breakdown by section, findings table). Skills hand off via stable xlsx contracts — change a number in the upstream Risk Assessment and every downstream skill in the chain (PLr → Compliance Matrix → Declaration of Conformity) consumes the new value automatically.

The suite is the natural counterpart to the [automotive-skills-suite](https://github.com/jherrodthomas/automotive-skills-suite) (152 skills, ISO 26262 / ISO/SAE 21434 / IATF 16949 / ASPICE / AUTOSAR / V&V). Together they cover the two largest standards-driven engineering verticals.

## Who this is for

- **Robot integrators** producing ISO 10218-2 / ANSI R15.06 compliance documentation for every cell delivery
- **OEM machine builders** generating CE marking / ANSI safety files at scale
- **Cobot deployers** running ISO/TS 15066 biomechanical validation, SSM, and PFL plans
- **AMR / AGV operators** executing ISO 3691-4 risk assessments and fleet manager architectures
- **ROS2 development teams** producing system architecture, URDF, behavior tree, Nav2, and TF spec documents
- **OT cybersecurity teams** running IEC 62443-3-2 risk assessments and zone & conduit segmentation
- **AI/ML in robotics teams** producing datasheets for datasets, model cards, and perception test catalogs

## How it differs from generic LLM prompts

Most LLM "robot safety prompts" produce free text. Every skill in this suite produces a **structured deliverable** — a multi-tab xlsx with named tabs, formulas where appropriate, color coding, and audit-ready reviewer artifacts. The output looks like what an integrator's quality-management system actually requires.

## License

MIT.
