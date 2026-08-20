# Polish log — dataset-documentation (builder + checklist-reviewer)

## 2026-08-20 (autonomous POLISH run) — severity: **high**

**Target selection.** W34 target 3 of 3, issue [#50](https://github.com/jherrodthomas/robotics-skills-suite/issues/50), scheduled for Thursday by the W34 plan. Also satisfies priority rule (3) independently — both halves sat at the 2026-05-03 import baseline. Rules (1) and (2) selected nothing again: no open issue carries `skill-bug` or `reviewer-finding`, and the suite has been 38/38 paired since W29.

**What's good**
- The 11-tab decomposition is faithful to Gebru et al. and needed no reordering: motivation → composition → collection → preprocessing → recommended uses → out-of-scope → distribution → maintenance → known biases.
- Both halves had complete, well-formed frontmatter, with `name` matching file and internal directory in each.
- The builder already separated **Recommended Uses** from **Out-of-Scope Uses** as distinct tabs. That split is the single most useful thing a datasheet does and it was already right.
- The reviewer's 26 checks are genuinely well-chosen — CA1–CA10 in particular cover class balance, splits, geographic and temporal coverage, sensor specs, and annotation protocol without padding. The check *content* needed no change; only its documentation did.

**What to fix**
1. **No dataset identity or version convention (primary, and the DoD's first item).** Neither half named a dataset ID, a version, or a citation string. `model-card-builder` records a training dataset and an evaluation dataset by name on two of its tabs — but with no stable identifier defined anywhere, those entries resolve to nothing. This is the exact ai-ml chain break the W34 plan picked this target to close: the model card was polished 2026-07-02 against an upstream datasheet that could not be cited.
2. **In-place version mutation was unguarded.** Following from (1): re-annotating a dataset without bumping a version silently changes what every existing model card describes. Nothing in either half prohibited it, and the reviewer had no way to raise it.
3. **Split membership treated as equivalent to split ratios.** The builder asked for train/val/test ratios only. Two datasets with identical counts and different membership produce different models; the ratios do not distinguish them.
4. **Governance references absent entirely** — the DoD's second item. Neither half named ISO/IEC 42001, ISO/IEC 23894, ISO/IEC 5259, the EU AI Act, or NIST AI RMF. Notably, the *paired* `model-card-builder` already cites 42001:2023, NIST AI RMF, and the AI Act. The downstream artifact was governance-aware and its upstream was not, which is backwards — Article 10 obligations attach to the training data.
5. **Robotics provenance fields missing** — the DoD's third item. "Sensor hardware" and "annotation protocols" appeared as bare phrases. Absent: shutter type, capture-rig geometry relative to `base_link`, calibration state and residual, inter-stream time-sync skew, and coverage stated against a *named* operating envelope. These are the fields that decide whether a robotics dataset transfers, and a generic datasheet framework does not ask for them.
6. **Reviewer claimed 7 tabs; the generator emits 5.** `generate_checklist.py` creates Title, Summary, Document Quality, Composition Assessment, Use Case Verification. The SKILL.md advertised a General Info tab and a Guide tab that are never created, and then Step 3 walked the user through two further tabs — "Collection & Preprocessing" and "Known Limitations" — that exist in neither the generator nor its own output table. A user following the documented walkthrough would look for four tabs that are not there.
7. **Reviewer file tree wrong in three ways.** It listed `dataset_doc_probe.py` (the file is `dataset-documentation-checklist_probe.py`), omitted `dashboard.py` entirely, and listed four `references/*.md` files that do not exist.
8. **Builder file tree listed two nonexistent paths** — `references/methodology.md` and `examples/sample_input_robot_dataset.json`.
9. **Tab 6 name mismatch.** Builder SKILL.md said "Preprocessing & Labeling"; the generated sheet is `Preprocessing`. Trivial, but it is the kind of drift that makes a reviewer's tab-name probe fail once one is written.
10. **Three reviewer scripts are one-line placeholders** — `check_definitions.py` ("# Check definitions for..."), `dashboard.py` ("# Dashboard builder placeholder"), and the probe. All 26 checks actually live inline in `generate_checklist.py`. The emitted checklist is therefore flat: no KPI tiles, no charts, no roll-up dashboard, unlike the mature reviewers in this suite. **Not fixed in this pass — implementing a probe and dashboard is a build job, not a polish job.** Captured as a follow-up and now stated honestly in the reviewer's own SKILL.md rather than being papered over by a fictional file tree.

**Edits applied**
- Builder description: rewritten to name the dataset identity/version handshake, the robotics provenance fields, and the dated governance baseline including the Article 10 application date. 968 chars, under 1024. All original trigger phrasings kept; added `training-data governance`.
- Builder: new `## Dataset identity and version — the model-card handshake` — dataset ID, semantic version, `<dataset-id>@<version>` citation string, split fingerprint, and an explicit prohibition on in-place version mutation.
- Builder: new `## Governance baseline — name it and date it` with a six-row edition table and the Article-10-is-live statement, plus the instruction to state the high-risk classification or the basis for excluding it.
- Builder: new `## Robotics provenance — the fields generic datasheets omit` — sensor part and shutter type, capture-rig geometry in REP-103 terms, calibration state and residual, time-sync skew, envelope coverage with named gaps, annotation provenance including the automated-pre-label trap.
- Builder: Step 1 and Step 2 extended for dataset ID/version and governance posture; Step 4 now checks the citation string and asks whether gaps are named rather than gestured at.
- Builder: tab table corrected (tab 6 → `Preprocessing`) and enriched per the new fields.
- Builder: new `## Downstream consumers` (model-card, perception-test-catalog) and `## Standards and references`.
- Builder: file tree corrected to the four files that actually exist.
- Reviewer description: rewritten in lockstep, enumerating the same check families. 997 chars.
- Reviewer: tab count corrected 7 → 5; the two phantom walkthrough tabs removed and the walkthrough rewritten against the five real tabs.
- Reviewer: new `### Step 4 — Apply the review judgement the automated checks cannot` (citation-string stability, falsifiable coverage claims, calibration recorded in the right place) and `### Step 5 — Governance baseline check` with the edition table.
- Reviewer: file tree corrected, with the three placeholder scripts labelled as placeholders, and a `**Known gap:**` block stating plainly that the checklist is flat.
- `examples/dataset-documentation-builder/README.md` and `examples/dataset-documentation-checklist-reviewer/README.md` stubs created.

**Version verification** (ai-ml is outside the mandatory safety-critical set, but every governance reference here is version-dated, so the check was run — and it moved one item from "future" to "in force")
- **EU AI Act, Regulation (EU) 2024/1689, Article 10** — high-risk data-governance obligations **applied from 2 August 2026**, i.e. **eighteen days ago**, and they reach systems already placed on the market before that date. The W34 plan listed Art. 10 as a reference to cite; it is now a live obligation, and both halves are written accordingly. This is the most consequential finding of the pass.
- **ISO/IEC 42001:2023** — current, no revision. Matches what `model-card-builder` already cites.
- **ISO/IEC 23894:2023** — current, no revision.
- **ISO/IEC 5259 series** — not referenced by either half before this pass, and directly on point for a dataset datasheet. Parts 1–4 published **2024**, Part 5 **2025**, Part 6 **2026** as a Technical Report. **Part 3 is the only part carrying requirements** — recorded explicitly, because citing "ISO/IEC 5259" as a conformity claim without naming Part 3 is meaningless.
- **NIST AI RMF 1.0** — cited as an alternative or parallel mapping, matching the model card's framing.

**Chain-consistency note.** With this pass the ai-ml cluster is internally consistent for the first time: `dataset-documentation` defines the citation string, `model-card` consumes it, and `perception-test-catalog` is named as the consumer of envelope-coverage gaps. `perception-test-catalog` itself remains at the import baseline and is the last ai-ml builder untouched — it should be picked before the vocabulary set here drifts.

**Severity rationale: high.** Two independent reasons. First, the identity gap was a real chain break between two shipped skills, not a stylistic one. Second, the reviewer's documented tab list and file tree described a skill that does not exist — a user following Step 3 would have hunted for four absent tabs. Documentation that is confidently wrong is worse than documentation that is thin.
