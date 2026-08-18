# Polish log — robot-hil-test-catalog-builder

## 2026-08-18 (autonomous POLISH, severity: med)

**Domain:** v&v · **Paired reviewer:** robot-hil-test-catalog-checklist-reviewer.skill (present) · **Issue:** #48 (W34 target)

**Selection rationale:** W34 plan named this as the Tuesday pick — open target issue #48 (`description-quality`, v&v), at the 2026-05-03 import baseline (107 days untouched), and immediately upstream of `robot-acceptance-protocol` which was polished 2026-08-12 while that pass is still fresh.

**What's good**
- The 10-tab structure is genuinely well chosen: the five fault families (sensor / comm / power / E-stop / timing) plus state-machine and pass-fail tabs cover what a safety-controller HIL bench is actually for, and the order runs setup → cases → criteria → execution tracking.
- Description names concrete trigger phrasings ("robot HIL", "fault injection test", "safety controller HIL") rather than gesturing at the topic.
- Frontmatter has both required fields; `name` matches file and internal directory in both halves.
- Reviewer's verification-area list mirrors the builder's tabs one-for-one — the pair was at least structurally in lockstep before this pass.

**What to fix**
1. **PLr/SIL cited with no edition (primary).** `## Standards` read only `ISO 13849-1 Performance Level definitions` / `IEC 62061 Safety Integrity Level requirements`. This is the same defect class corrected in `safety-io-matrix` on 2026-08-13 (d909fc2), which anchored the identical two standards at ISO 13849-1:**2023** and IEC 62061:**2021**. This file contradicted a sibling in its own domain cluster.
2. **ISO 13849-2 absent entirely — the actual governing standard.** A HIL catalog *is* validation evidence, and ISO 13849-2 is the validation part: fault lists, the analysis-vs-test split, and the required record. Citing -1 without -2 anchors the targets but not the method by which the catalog claims to have met them.
3. **No HIL/FAT scope boundary.** The single largest real-world defect in these catalogs, and the DoD item from the W34 plan. Nothing stated which plant is simulated and which is real, so nothing prevented duplicate-or-gap between this catalog and `robot-acceptance-protocol`.
4. **No test-case ID convention**, so a safety function could not be walked from PL claim → bench evidence → cell acceptance without a hand-built mapping table.
5. **No traceability rules.** Fault-injection cases were not tied to the DC assumptions they exist to defend, and channel/OSSD cases were not tied to `safety-io-matrix` rows. An injection catalog that does not defend its own DC figures is decorative.
6. **Plant-model validity unaddressed.** A HIL result is bounded by the fidelity of the simulated plant, and the plant model is software in the verification toolchain. Nothing in either half asked for that argument.
7. **Reviewer had no standards section**, so it could not flag a catalog citing superseded editions — chain break against its own builder, same shape as the one fixed in the `robot-acceptance-protocol` pass.

**Edits applied (small, obvious)**
- Builder description: appended `anchored on ISO 13849-1:2023 for PLr claims, IEC 62061:2021 for SIL claims, and ISO 10218-2:2025 for the cell-level functions under test` (557 chars, under 1024).
- Builder: new `## Scope boundary — HIL vs FAT` — real controller + simulated plant here, real cell at FAT; destructive/out-of-envelope cases belong on the bench; shared test-case ID where a case must exist in both, with the FAT instance marked as re-verification.
- Builder: new `## Test-case ID convention` — `HIL-<function-id>-<class>-<nn>`, class ∈ {FI, COMM, PWR, ESTOP, TIM, SM}, `<function-id>` carried from `safety-io-matrix-builder`.
- Builder: new `## Traceability requirements` — DC assumptions each defended by an injection case; dual-channel/OSSD cases referencing matrix row IDs; timing budgets decomposed into input detection + logic execution + output de-energisation.
- Builder `## Standards`: replaced two bare lines with six edition-anchored entries (ISO 13849-1:2023, ISO 13849-2:2012, IEC 62061:2021, IEC 61508-3:2010, ISO 10218-1/-2:2025, IEC 60204-1:2016), each with a stated reason for being there.
- Builder: new `## Related skills` (safety-io-matrix, interlock-estop, iso13849-plr, iec62061-sil, robot-acceptance-protocol, robot-field-acceptance, paired reviewer).
- Reviewer description: appended `against ISO 13849-1:2023, ISO 13849-2:2012, IEC 62061:2021, and ISO 10218-2:2025`.
- Reviewer: added `## Scope-boundary checks`, `## Traceability checks`, and `## Standards baseline`, each mirroring the builder rule it audits; added the "does not modify the source workbook" line the other polished reviewers carry.
- `examples/robot-hil-test-catalog-builder/README.md` stub created.

**Edition verification** (v&v is outside the mandatory safety-critical set, but every reference here is version-dated, so the check was run anyway)
- **IEC 61508-3:2010** confirmed as Edition 2.0 on the IEC webstore (publication 5517) and ANSI webstore — cancels and replaces the 1998 first edition. New citation to this suite; recorded so later passes have the provenance.
- **ISO 13849-2:2012** confirmed Edition 2 on iso.org (std 53640), last reviewed and confirmed 2018, still the published edition. **ISO/DIS 13849-2 (std 87709) is in the enquiry phase** and will supersede it — retitled *Application of principles for the design and validation*. Explicit "do not bump until published" notes written into both halves so a future pass does not cite a draft.
- ISO 13849-1:2023 (Ed 5), IEC 62061:2021 (Ed 2), ISO 10218-1/-2:2025 carried from prior verified passes (d909fc2, 6244fd2, aadcd83) — unchanged, not re-litigated.

**Not done (deliberately descoped)**
- Same structural gap as the rest of the suite: the builder has no generator script (only `recalc.py` and shared `office/` helpers), and the reviewer's `check_definitions.py`, `dashboard.py`, and `robot-hil-test-catalog-checklist_probe.py` are placeholder stubs. Writing them is a refactor, not a polish edit.
- Did **not** retro-fit the new `HIL-*` ID convention into `robot-acceptance-protocol`'s FAT protocol. The convention is declared from this side and the FAT side references it, but making the two workbooks share an ID namespace properly is a two-file change that deserves its own target.

**Follow-ups**
- `robot-field-acceptance` is the last v&v builder at import baseline and will carry the same bare-`ISO 13849-1` / missing-`-2` defect. Natural W35 pick to close the v&v cluster.
- Repo-wide grep for bare `ISO 13849-1` and `IEC 62061` with no edition — the safety-io-matrix pass predicted more instances and this was one; there are likely others across cobot and cell-design.
- **Watch item for whoever runs POLISH after ISO/DIS 13849-2 publishes:** two files now carry an explicit do-not-bump note. When it publishes, both need updating together plus a sweep of any other -2 citation.
- Reciprocal edit on `robot-acceptance-protocol-builder` to reference the `HIL-*` ID namespace from the FAT side, closing the loop this pass opened one-directionally.
