## 2026-07-21

**Picked because:** least-recently-touched builder (2026-05-03) AND open weekly-target issue #37 (W28 carryover, amr domain).

**What's good**
- Frontmatter clean; description 407 chars (<1024) with solid trigger phrases (fleet manager, AMR coordination, VDA 5050, multi-robot orchestration).
- Clear 7-step workflow; reviewer pair (fleet-manager-architecture-checklist-reviewer) exists and its 7-tab checklist structure aligns with the builder's documented output.

**What was fixed this pass (small, applied)**
- BUG (high): generator crashed on run — tab name "VDA 5050 / MQTT / REST Interfaces" contains "/", which is illegal in Excel sheet titles (openpyxl ValueError). Renamed to "VDA 5050 MQTT REST Interfaces" in generator and SKILL.md. Verified generator now runs and produces a valid workbook.
- Placeholder tab "Worksheet" renamed to "References" to match the documented output structure.
- Tab count corrected from "11-tab" to "12-tab" in SKILL.md body and generator docstring (12 tabs incl. Title).
- File tree in SKILL.md claimed examples/sample_input.json and references/*.md that do not exist in the package; tree corrected to actual contents.

**Still to fix (not applied — beyond small-fix scope)**
- HIGH: generate_fleet_arch.py is a placeholder — it ignores the input JSON entirely and writes "Placeholder" in each tab. Needs a real implementation before this builder produces audit-ready output.
- MED (standards, amr = safety-critical): SKILL.md cites no standard editions. Should reference ISO 3691-4:2020 (AMR safety) and pin a VDA 5050 version (currently unversioned in description and tabs). Verify current VDA 5050 release before pinning.
- LOW: generator tab "Traffic Management" vs SKILL.md "Traffic Management Algorithm" — harmonize when the real generator is written.
- LOW: examples/sample_input.json and references/ docs promised by the old file tree never existed; consider actually adding them.

**Severity:** high (crash bug fixed; placeholder generator remains)

---

## 2026-08-05 (reviewer-side lockstep pass)

**Picked because:** open issue #42 — the only `chain-break`-labelled issue in the repo, W31→W32 carryover, and explicitly named target 1 in `docs/weekly/WEEK-2026-W32.md`. Task priority order lists `skill-bug` / `reviewer-finding` first; no issue carries either label, so the weekly plan's escalation of #42 governed. Judgement call, noted here.

**Scope:** `fleet-manager-architecture-checklist-reviewer.skill` (primary), plus a one-line standards anchor on the builder to keep the pair in lockstep.

**What's good (reviewer)**
- Frontmatter clean, single `name` + `description`, description well under 1024 chars.
- Documented tab purposes are coherent and map onto the builder's 12-tab output.
- Package layout matches the repo convention (`SKILL.md` + `scripts/` + `scripts/office/`).

**What was fixed this pass (small, applied)**
- MED (chain-break, the reason #42 exists): reviewer file tree claimed `scripts/fleet_arch_probe.py`, but the shipped file was `fleet-manager-architecture-checklist_probe.py`. Hyphens also make that filename un-importable as a Python module. Renamed the file to `fleet_arch_probe.py` — resolves the doc mismatch and the latent import problem in one move.
- MED: reviewer file tree claimed `examples/sample_workbook.xlsx`, `references/reviewer_methodology.md`, and `references/fleet_architecture_checks.md`, none of which exist in the package. Tree corrected to actual contents (same defect class fixed on the builder 2026-07-21).
- MED: tab-count mismatch. SKILL.md documented "7 tabs" and named tab 5 "Documentation"; the generator emits 8 sheets (Title + 7) and names it "Documentation Review", plus a stray placeholder "Worksheet". Renamed "Worksheet" → "References" in the generator (matching the builder precedent) and rewrote the SKILL.md table as 8 rows using the generator's actual sheet names. Smoke-tested: generator runs and emits exactly `['Title','General Info','Guide','Summary','Documentation Review','Technical Assessment','Verification Assessment','References']`.
- MED (standards — amr is safety-critical, edition verification required): neither skill in the pair cited a standard edition. Added a **Governing standards** table and edition strings to both descriptions:
  - **ISO 3691-4:2020** — driverless industrial trucks / AMR safety.
  - **VDA 5050 2.1.0** — verified this run against VDA/VDMA: 2.1.0 was published January 2025, is English-only, adds corridors for obstacle avoidance, and is backward compatible with 2.0.0. This clears the "verify current VDA 5050 release before pinning" follow-up left open on 2026-07-21.
- Removed a stale `scripts/__pycache__/` directory that had been committed inside the builder archive.

**Still to fix (not applied — beyond small-fix scope)**
- HIGH: both generators are placeholders. `generate_fleet_arch.py` ignores its input JSON; `generate_checklist.py` ignores the source workbook and writes `"<tab> - Placeholder"` into A1 of every sheet. Neither produces audit-ready output. This is the real work and needs a dedicated implementation session, not a polish pass.
- HIGH: `fleet_arch_probe.py`, `check_definitions.py`, and `dashboard.py` are all one-line stubs. The reviewer has no checks, no dashboard, and no probe.
- LOW: builder generator sheet "Traffic Management" vs SKILL.md "Traffic Management Algorithm" — still unharmonized (carried from 2026-07-21).
- LOW: `examples/` and `references/` content promised by the original trees still does not exist; a stub was seeded at `examples/fleet-manager-architecture-builder/README.md` this run.

**Severity:** medium (documentation and standards accuracy restored across the pair; placeholder generators remain the blocking defect)
