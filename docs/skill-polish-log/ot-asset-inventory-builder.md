# Polish log: ot-asset-inventory-builder (+ paired reviewer)

## 2026-07-30

**Picked because:** W30/W31 carryover target (issue #41, cybersecurity domain), next in W31 list order after #40 landed on Wednesday (c6f1cf6). No open `skill-bug` or `reviewer-finding` issues and no orphan builders; both files still sat at the 2026-05-03 import baseline. Polished **pair-complete** per the W30 lockstep convention.

**What's good**
- Builder's 10-tab structure is genuinely well chosen for an IACS inventory — separating safety/specialized modules and edge/gateway devices from generic network gear is the right cut, and the firmware/patch and end-of-support tabs make it usable as a real risk-assessment input rather than a flat device list.
- Builder generator is **fully implemented** (all 10 tabs actually created) — unlike several other import-baseline pairs in this suite, this one produces a real workbook.
- Reviewer's 24 checks (IC1–IC8 / DQ1–DQ8 / RL1–RL8) are well balanced and each carries a sensible confidence rating; IC8 ("device count matches physical walkdown") correctly sits at Low confidence since no tool can verify it.
- Both descriptions comfortably under the 1024-char limit (560/700 before edit; 690/781 after).

**What to fix**
1. **No IEC 62443 part anchoring (safety-critical domain check).** Both descriptions said only "IEC 62443 compliance" with no part number, and neither used the standard's own vocabulary. FIXED — both now anchor on **IEC 62443-2-1** and **IEC 62443-3-2** and use **System under Consideration (SuC)**, matching the `iec62443-risk-assessment` and `zone-conduit-plan` pairs per the W31 standards table.
2. **Zone assignment was missing entirely.** The builder captured criticality and VLAN but never the IEC 62443-3-2 zone an asset belongs to — which is precisely the field `zone-conduit-plan-builder` needs downstream. FIXED — added zone/conduit to the Step 2 collection list, to the Network & IO tab purpose, and to the reviewer's Data Quality walkthrough. Added a new "Downstream hand-off" section to the builder naming the two consuming skills and the stable-asset-ID convention.
3. **Reviewer documented 7 tabs; the generator creates 5.** Workflow Step 3 walked the user through "Network Topology Validation" and "Support Status" tabs that do not exist, and the output table also listed non-existent "General Info" and "Guide" tabs. This is user-facing — a reviewer following the doc would look for tabs that were never written. FIXED — both the walkthrough and the output table now describe the 5 real tabs (Title, Summary, Inventory Completeness, Data Quality & Accuracy, Risk & Lifecycle) with the check-ID ranges.
4. **Builder tab names mismatched the generator.** SKILL.md said "HMI & Operator Station Inventory" and "Safety & Specialized Modules"; `generate_ot_inventory.py` creates "HMI & Operator Stations" and "Safety & Specialized". FIXED — same class of bug as 7f24c5d.
5. **File trees inaccurate in both.** Builder listed a `references/methodology.md` and `examples/sample_input_amr_fleet.json` that do not exist in the archive; reviewer listed `inventory_probe.py` (actual filename is `ot-asset-inventory-checklist_probe.py`), omitted `dashboard.py`, and listed four `references/*.md` files that do not exist. Both omitted `scripts/office/__init__.py`. FIXED — trees now match archive contents exactly.
6. **Reviewer description overclaimed "Probes the source workbook".** `generate_checklist.py` calls `load_workbook` inside a bare `try/except` and then never reads it; no check is auto-filled. FIXED (wording) — description now says "Reads the source asset inventory workbook", and the file tree section carries an explicit note that auto-fill is not yet implemented and that the probe/dashboard/check-definition scripts are placeholders.

**Deferred (too large for a polish pass) — SEVERITY MEDIUM**
- **Reviewer auto-fill is not implemented.** `ot-asset-inventory-checklist_probe.py` (62 B), `check_definitions.py` (62 B) and `dashboard.py` (32 B) are one-line placeholders; all 24 checks emit PENDING. Several are cheaply machine-verifiable against the builder's own output — IC1–IC7 (tab presence and row counts), DQ2/DQ7/DQ8 (empty-cell scan), RL1/RL3/RL4/RL7 (column population). Worth a dedicated implementation target, not a POLISH slot. Note this is **less severe than the `machinery-safety-lifecycle` case** — there the builder itself was a stub; here the builder works and only reviewer auto-fill is missing.
- **`check_definitions.py` is dead weight** — the `CHECKS` list lives inline in `generate_checklist.py`. Either move it or delete the file during that implementation pass.
- **No dashboard tab** despite `dashboard.py` existing as a placeholder; other reviewers in the suite ship a visual dashboard. Out of scope today.
- **"Engineering workstations" has no home tab.** Named in the builder description and checked by reviewer IC7, but none of the 10 tabs owns it — it falls between "Edge & Gateway Devices" and nothing. Either add a tab or fold it explicitly into an existing one; needs a generator change, so deferred.

**Severity:** medium — all description, edition-anchoring, tab-name, tab-count and file-tree defects fixed in both files; the pair is functional today, with reviewer auto-fill as the remaining known gap.
