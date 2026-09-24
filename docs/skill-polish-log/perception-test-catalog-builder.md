# Polish log — perception-test-catalog-builder (+ paired checklist-reviewer)

## 2026-09-24 (autonomous POLISH, W39 Thursday, issue #62)

**Severity:** high. The contract was polished, but the "tier A" premise the plan relied on turned out to be false (see below).

**Selection:** rule (1), open `weekly-target` issue #62. This is the oldest untouched builder (140 days, part of the 2026-05-03 import cohort) and had no polish log before today.

**What was good**
- Tab structure is sensible: taxonomy, nominal / edge / adversarial, FP and FN catalogs, per-scenario metrics, and re-test triggers.
- The reviewer's 28 checks cover the right territory and are stable, so they are worth keeping.

**What was wrong**
1. **Automotive leftovers in a robotics suite.** The builder's example baselines were "daylight urban" and "highway", and its FP example was "road markings". Snow/ice rows were hard-coded whatever the ODD.
2. **Bare-percentage thresholds** such as "≥99 %", "≥85 %" and "accuracy", with no sample size or confidence bound. A threshold like that is not a pass/fail criterion. "Accuracy" also hides the FN/FP split.
3. **No ODD, no row contract, and no condition-class split.** FN and FP were catalogued, but their asymmetric consequences in a robot cell were never stated.
4. **No boundary against `model-card` / `dataset-documentation`,** and no statement that passing the catalog is not a PL/SIL claim.
5. **Reviewer description was false.** It said the generator "auto-fills FC, LC, PC, NO, or NA and drafts findings". In fact `generate_checklist.py` opens the source workbook, never reads it, and writes "—" into every Assessment cell. The body promised 7 tabs, but the generator writes 5. The walkthrough named two tabs that do not exist. The probe filename was wrong, and a phantom `references/` directory was listed.
6. The builder listed phantom `references/` and `examples/` directories.

**Edits applied (SKILL.md only, both halves; no generator code changed)**
- Builder: new requirements table **R1–R10**. It covers the ODD as dimensions with ranges, a one-row-per-test-case contract, and the nominal / degraded / adversarial definitions (including soiling, reflective and low-texture surfaces). Thresholds must be rates with a one-sided 95 % Clopper-Pearson bound and a stated *n*, and the rule of three applies at zero failures. FN and FP get separate thresholds, and FN rows on people link to hazard IDs. It also covers re-test triggers, reproducibility, and the boundaries.
- Builder: added an honest **Implementation status** section saying the generator still writes illustrative automotive / bare-percentage rows. The output-tab table is now keyed to R-IDs, and the file tree is corrected.
- Reviewer: rewrote the description and body to match the code. The generator lays out 28 checks and the reviewer rates them. Every check is **re-keyed to the builder requirement it verifies** (this closes the zone-conduit follow-up for this pair). SC3/SC4/SC10 are NA only with a cited ODD exclusion. SC5 is widened to indoor obscurants (dust, oil mist, steam). Five **manual checks M1–M5** were added for the requirements the generator does not cover (ODD per row, CI + *n*, FN/FP separation, soiling/texture, boundary). The tab count is corrected to 5 and the file tree is corrected.
- Worked numbers were checked by computation. Recall ≥ 0.99 (one-sided 95 % CP lower bound) is met by 0/300 or ≤1/474 failures, and **not** by 1/460 (bound 0.9897). The rule of three gives 3/0.01 = 300.

**Standards:** ai-ml domain, so the mandatory edition step does not fire. One new citation was added: **ISO/IEC TR 5469:2024**, 1st ed., Jan 2024, *Artificial intelligence — Functional safety and AI systems* (source: iso.org/standard/81283). It is cited as informative background only.

**Finding that matters beyond this pair: "tier A" is not what `audit_reviewer_impl.py` says it is.** All 6 tier-A reviewers (dataset-documentation, iec62443-risk-assessment, model-card, ot-asset-inventory, perception-test-catalog, zone-conduit-plan) share one template. Each loads `src_wb`, never uses it, writes "—" for every assessment, and creates 5 sheets. The script measures "has a check table ≥ 3 kB", not "rates anything". So **0 of 38 reviewers auto-rate**, even though most descriptions promise auto-filled FC/LC/PC/NO/NA. The W39 plan's rationale ("a promise the code actually keeps") does not hold. This belongs in #63.

**Suggested future edits**
- Builder generator: drive the Nominal / Edge / Adversarial / Acceptance tabs from input rows with the R2 columns, and drop the hard-coded automotive rows. This is a build, not a polish.
- Reviewer generator: add M1–M5 to `CHECKS` with their R-IDs, and write an `Req` column.
- `audit_reviewer_impl.py`: split tier A into "A-template (check table, no source inspection)" and "A-rating (reads the source and emits ratings)". Today that split would be 6 → 0.
- Descriptions of the other five tier-A reviewers also claim auto-fill. Correct them the same way when each comes up.
- `examples/perception-test-catalog-builder/README.md`: add a sample input with R2 rows once the generator supports them.
