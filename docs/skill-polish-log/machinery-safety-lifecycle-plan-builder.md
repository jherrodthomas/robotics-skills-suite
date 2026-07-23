# Polish log: machinery-safety-lifecycle-plan-builder (+ paired reviewer)

## 2026-07-23

**Picked because:** W30 planning target (issue #38, foundation domain), sitting at the 2026-05-03 initial-import baseline. No open skill-bug / reviewer-finding issues and no orphan builders today. Next in W30 list order after #37 (Tue) and #39 (Wed).

**What's good**
- Reviewer's 7-tab checklist output structure is well documented and matches the suite-wide reviewer convention.
- Builder workflow section is clear and the pair naming/packaging follows the repo standard.
- Both descriptions comfortably under the 1024-char limit (472/477 before edit; 613/652 after).

**What to fix**
1. **Reviewer description was a copy-paste of the builder's.** It said "Generate an audit-ready … workbook" (wrong verb for a reviewer) and had broken grammar ("Use this skill to review the user mentions safety lifecycle plan"). FIXED — rewritten as a review-oriented description consistent with the suite's other reviewers.
2. **Standard editions missing (safety-critical domain check).** Bare "ISO 13849-1 and IEC 62061" with no editions, and no ISO 12100 / EU Machinery Regulation anchor despite this being the foundation-domain lifecycle skill. FIXED — both descriptions now anchor on ISO 12100:2010, ISO 13849-1:2023, IEC 62061:2021, and EU Machinery Regulation 2023/1230, matching the W30 plan's standards table and the iso12100-risk-assessment pair.
3. **File trees inaccurate in both SKILL.md files.** Both listed a `references/` directory (methodology.md, conventions/checks md) that does not exist in either archive; both omitted `scripts/office/__init__.py`; the reviewer tree omitted 3 of its actual scripts. FIXED — trees now match archive contents exactly.
4. **Leaked local session path.** `generate_safety-lifecycle.py` contained a comment referencing `/sessions/vigilant-ecstatic-maxwell/mnt/CL work/automotive-skills-suite/...` — a path from the original authoring machine. FIXED — replaced with a neutral reference note.

**Deferred (too large for a polish pass) — SEVERITY HIGH**
- **Both generator scripts are placeholders.** `generate_safety-lifecycle.py` prints "Placeholder: implement builder" and `generate_checklist.py` likewise; all reviewer probe/dashboard/check-definition scripts are 1-8 line stubs. This pair cannot produce a workbook or checklist at all. It is scaffold-only from the initial import. Needs a full implementation pass modeled on the working pairs (e.g. loto-procedure, pfl-plan).
- Reviewer carries three overlapping probe stubs (`safety-lifecycle_probe.py`, `machinery-safety-lifecycle-plan-checklist_probe.py`, `probe_workbook.py`); consolidate to one when implementing.
- SKILL.md "Output structure" for the builder says only "multiple tabs" — define the actual tab list when the generator is implemented.

**Severity:** high — description/tree/edition issues fixed, but the pair is non-functional until generators are implemented. Recommend a dedicated implementation target in a future weekly plan (larger than one POLISH slot).
