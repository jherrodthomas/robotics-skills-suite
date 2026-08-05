# Example — fleet-manager-architecture-builder

**What this skill produces:** a 12-tab AMR Fleet Manager architecture workbook (`.xlsx`) covering fleet scope, robot inventory, traffic management, charging coordination, mission dispatch, health monitoring, VDA 5050 2.1.0 interfaces, and deadlock resolution.

**Typical input shape:** a JSON fleet specification — site/fleet identification, per-robot inventory rows (model, payload, footprint, charge profile), traffic zones and intersection rules, charging policy thresholds, and the master-control endpoint config.

**Expected output:** one workbook at the path you pass to `scripts/generate_fleet_arch.py`, with a Title tab, Doc Control, and the ten content tabs; References cites ISO 3691-4:2020 and VDA 5050 2.1.0.

**Sample I/O:** `python scripts/generate_fleet_arch.py fleet_spec.json fleet_architecture.xlsx`

> ⚠️ **Status:** the generator is currently a placeholder — it emits the tab skeleton but does not yet read the input JSON. Tracked in `docs/skill-polish-log/fleet-manager-architecture-builder.md` (severity HIGH).
