# Polish log — iso9283-performance-test-builder

## 2026-09-02 (autonomous POLISH, severity: high)

**Domain:** v&v · **Paired reviewer:** iso9283-performance-test-checklist-reviewer.skill (present) · **Issue:** #55 (W36 target)

**Selection rationale:** Rule (1) returned nothing — no open issue carries `skill-bug` or `reviewer-finding`; all 20 open issues are `weekly-target`. Rule (2) returned nothing — 38/38 paired. Rule (3): five builders remain at the 2026-05-03 import baseline, but W36 (#55) named this pair for Wednesday on a sharper measure than date — it was the **thinnest builder in the repo at 6 body lines** against a 13-line reviewer, i.e. inverted. Followed the plan.

**What's good**
- Frontmatter valid in both halves; `name` matches filename and internal zip directory.
- The builder already pinned **ISO 9283:1998 (Edition 2; reviewed and confirmed 2021)** and the reviewer named the 1998 methodology — the pair was *not* an edition asymmetry, and `robot-acceptance-protocol-builder` (polished W33) cites the same edition and already hands its performance-acceptance tab to this skill. The boundary existed from the FAT/SAT side; it did not exist from this side.
- The 11-tab spine was right and was kept; the tabs were made specific rather than renamed.

**What to fix**
1. **Six body lines on the skill that every performance claim in the repo routes through.** The body was: one sentence, a tab list, and one edition line. A reviewer 2× its size will pass workbooks the builder never asked for.
2. **"Pose accuracy and pose repeatability" listed as one phrase, with no definition of either.** AP is systematic deviation from the *commanded* pose; RP is scatter about the *barycentre* (l̄ + 3·Sl). Datasheets quote RP because it is always the smaller number, and users read it as AP. This is the single most common ISO 9283 misreading and neither half could name it.
3. **Multi-directional pose accuracy variation (vAP) named but not distinguished from unidirectional RP.** Unidirectional RP hides backlash and compliance; vAP exposes them. Users don't know it exists; the builder didn't say why it matters.
4. **Test conditions "referred to" rather than stated.** No cube, no measurement plane, no five poses, no rated-load / velocity percentages, no cycle counts, no warm-up rule, no ambient. A user cannot fill the workbook from the standard they haven't bought.
5. **Measurement uncertainty named as a tab with no rule.** Nothing required the uncertainty to be stated *relative to the value claimed*, so a 0.05 mm RP measured with a 0.1 mm instrument would have passed both halves.
6. **Acceptance criteria with no source.** ISO 9283 defines method, not limits. Neither half said where limits come from or flagged datasheet-condition vs ISO-condition mismatch.
7. **No scope boundary against `robot-acceptance-protocol`.** ISO 9283 measures manipulator performance, not application capability, and it is a performance standard, not a safety standard. Neither half prevented either conflation — on a v&v skill, that is the defect that lets a cell get "accepted" on a cube test.
8. **Reviewer: ten bullet nouns, no findings, no ratings, no silent-failure class.** Nothing distinguished "RP reported as AP" (looks complete, proves nothing) from a missing signature.

**Verification performed (v&v is not a mandatory-check domain; run anyway per the standing rule from 2026-09-01 — the builder carries a version claim)**
- **ISO 9283:1998 confirmed current at iso.org (cat. 22244):** Edition 2, 1998-04, 60 pp., ISO/TC 299, last reviewed and confirmed 2021, status Published, stage **90.60 close of review**. Supersedes ISO 9283:1990 (withdrawn) and its Amd 1:1991. No revision listed under development. The builder's existing pin was correct and stays.
- **ISO/TR 13309:1995** confirmed at iso.org (cat. 21679) as the equipment/metrology guide for ISO 9283 — added as the reference for the uncertainty rule rather than inventing one.
- Boundary references pinned to **ISO 10218-1:2025 / ISO 10218-2:2025**, matching `robot-acceptance-protocol` (W33) and the repo-wide edition audit; written out in full because the shorthand `10218-1:2025 / 10218-2:2025` does not match `audit_pair_editions.py` and produced a transient asymmetry until fixed.
- Stage 90.60 means the standard has passed its systematic review with no revision; **no edition action is needed, but a 90.60 close-of-review status is worth re-checking at the next PLAN that touches v&v** in case TC 299 opens a revision.
- One thing deliberately *not* asserted as a standard requirement: the "instrument uncertainty ≤ 1/4 of the claimed value" rule. ISO 9283 requires uncertainty to be *stated*; the 25 % ratio is common practice and ISO/TR 13309 territory. The builder phrases it as "a commonly applied acceptance rule" and makes the workbook record the ratio actually achieved; the reviewer flags > 25 % rather than failing it outright.

**Edits applied**
- Builder description rewritten: characteristics by symbol, the numeric test conditions, the uncertainty-ratio rule, the FAT/SAT boundary, and added triggers `path accuracy` and `robot calibration verification`. 930 chars.
- Builder body 6 → 55 non-blank lines: new `## Characteristics — name each one, never "accuracy" alone` (table of AP, RP, vAP, AD/RD, stabilization, overshoot, drift, AT/RT, CR/CO, AV/RV/FV, optional characteristics, with the confusion each prevents); `## Test conditions — stated as numbers` (cube, diagonal plane, P1–P5 at 10 % of the diagonal, 100 % rated load mandatory, 100/50/10 % velocity, 30/10/3 cycles and 8 h drift, warm-up rule, 20 °C ± 2 °C with soak); `## Data reduction — formulas in cells` (barycentre, APp, lj, Sl with n−1, RP = l̄ + 3·Sl); `## Measurement uncertainty — declared relative to the claim`; `## Acceptance — criteria come from outside this standard`; `## Scope boundary — performance, not application capability` including the explicit no-safety-claim rule; `## Standards and references` (ISO 9283:1998 with review status, ISO/TR 13309, ISO 9787, ISO 9946, ISO 10218 as boundary only); `## Related skills`.
- Reviewer description rewritten to mirror the builder rules as checks. 980 chars.
- Reviewer body 13 → 35 lines: `## Characteristic checks`, `## Test-condition checks`, `## Data-reduction checks`, `## Measurement-uncertainty checks`, `## Acceptance checks`, `## Scope and boundary checks` (including the 1990-edition finding), `## Findings format` reserving top severity for **RP reported as AP** and **uncertainty ratio unstated**, `## Related skills`. Added the "does not modify the source workbook" and FC/LC/PC/NO/NA rating line the other polished reviewers carry.
- `examples/iso9283-performance-test-builder/README.md` and `.../checklist-reviewer/README.md`: "what this skill produces" and "expected output" blurbs refreshed from the new descriptions (they quoted the old ones). Sample I/O remains TODO.
- Both archives re-zipped preserving every other payload entry (4 entries builder, 7 reviewer; `recalc.py`, `office/`, and the reviewer's placeholder `check_definitions.py` / probe untouched). `unzip -t` clean; frontmatter `name` re-read from inside each archive.
- `scripts/audit_pair_editions.py` re-run: **1 mismatch / 10 asymmetries — unchanged.** The pair no longer holds the thinnest-builder title; the next thinnest are `operator-training-matrix` (7, Thursday's #56), `ros2-system-architecture` (9), `robot-field-acceptance` (9).

**Not done (descoped):** the reviewer's `check_definitions.py` and `_probe.py` are still one-line placeholders. Turning the new check list into executable probes is real work, not a small fix, and is a candidate for a themed W37+ slot across all reviewers rather than one-off here.

**Severity: high** — the v&v keystone the FAT/SAT protocol defers to had no definition of the two numbers it exists to produce, and no rule stopping a performance test being read as a safety or acceptance result.
