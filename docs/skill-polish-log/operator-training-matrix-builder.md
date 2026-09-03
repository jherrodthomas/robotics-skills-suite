# Polish log — operator-training-matrix-builder

## 2026-09-03 (autonomous POLISH, severity: high)

**Domain:** operational · **Paired reviewer:** operator-training-matrix-checklist-reviewer.skill (present) · **Issue:** #56 (W36 target)

**Selection rationale:** Rule (1) returned nothing — no open issue carries `skill-bug` or `reviewer-finding`; all 20 open issues are `weekly-target`. Rule (2) returned nothing — 38/38 paired. Rule (3): W36 (#56) named this pair for Thursday — 7 body lines against a 10-line reviewer, inverted, and the last operational builder at the 2026-05-03 import baseline. Followed the plan. **Operational is a safety-critical domain: the mandatory edition check fired.**

**What's good**
- Frontmatter valid in both halves; `name` matches filename and internal zip directory.
- The 9-tab spine (roles, catalog, prerequisites, evaluation, recertification, records, roster, competency template, sign-off) was the right spine and was kept; tabs were made specific, not renamed.
- The builder already named four roles (operators, integrators, programmers, maintenance) in the description — the vocabulary was there, the duty boundaries were not.

**What to fix**
1. **Seven body lines on the skill that `loto-procedure` and `robot-sop` both point at for "trained personnel".** The body was one sentence, a tab list, and two unpinned standards.
2. **Roles named, never distinguished.** Nothing said what an operator may not do without the programmer role, or that manual-mode entry needs an enabling device. A matrix that merges roles is exactly what ISO 10218-2:2025 / R15.06-3-2025 mode-by-role duties make unusable.
3. **No OSHA 1910.147(c)(7) authorized / affected / other distinction at all** — on the skill that receives the LOTO training obligation. Neither half could catch a roster that infers authorized status from "is maintenance".
4. **Training delivered conflated with competency demonstrated.** One "training records" tab, no evidence-type column, nothing requiring practical observation for entry/teach/LOTO competencies.
5. **"Recertification interval" as the only retraining trigger.** 1910.147(c)(7)(iii) lists conditions (job change, new hazard, procedure change, inspection deviation, reason to believe) and sets no interval; the builder had the interval and none of the conditions — the inverse of the regulation.
6. **No certification content (name + dates per (c)(7)(iv)), no retention, no re-qualification path.**
7. **Both halves cited "ISO 10218-2" and "ANSI R15.06" with no edition.** In a safety-critical domain that is the class of defect the mandatory check exists for. Not *wrong* — absent.
8. **Reviewer: seven bullet nouns, no findings, no ratings, no silent-failure class.**

**Edition verification (mandatory — operational domain)**
- **ISO 10218-2:2025** — Edition 2, published February 2025, supersedes 2011; most ISO/TS 15066 content incorporated (Annex M carries the former TS 15066 Annex A body-region limits). Pinned in both halves.
- **ANSI/A3 R15.06-2025** — Parts 1 and 2 approved **2025-08-21** as a revision of ANSI/RIA R15.06-2012 (US adoption of ISO 10218-1/-2:2025); Part 3 (use of industrial robot cells) approved **2025-10-07**. Consistent with what `robot-sop-builder` (W31) already carries. Pinned; 2012 named only in the reviewer's negative check.
- **OSHA 29 CFR 1910.147(c)(7)** — verified the (c)(7)(i)(A)/(B)/(C) status definitions, the (c)(7)(iii) retraining conditions, and the (c)(7)(iv) certification content (name + dates) against osha.gov. The regulation sets **no fixed retraining interval** — written into the builder explicitly, since the original body implied the interval was the requirement.
- **ANSI/ASSP Z490.1** — the 2016 edition is **superseded by Z490.1-2024**. Neither half cited Z490.1 before; added at 2024 as the evaluation/records reference rather than inventing evidence-type rules. Worth noting for the rest of the suite: any skill that later cites Z490.1-2016 is stale on arrival.
- **ISO/TS 15066:2016 — near-miss worth recording.** A search-engine summary asserted the TS was "withdrawn, stage 95.99". **iso.org (cat. 62996) says otherwise:** Published, Edition 1, last confirmed 2022-12, stage **90.92 "to be revised"**, to be replaced by ISO/AWI 15066-1 (cat. 91522) under development. The 95.99 line in the lifecycle is the *template* row every ISO page shows, not the current state. Had the summary been trusted, this run would have written "withdrawn" into a safety-critical pair and the task file's `ISO/TS 15066:2016` row would have been reported as a second stale entry. It is not stale. Same lesson as `iso3691-4` (W35) inverted: check the primary source before "correcting" anything — including the check itself.
- ISO 13849-1:2023 named once in the integrator role's training content (both halves) — matches the repo-wide pin.

**Edits applied**
- Builder description rewritten: roles, the (c)(7) status attribute, delivered-vs-demonstrated, conditional retraining, certification, three pinned editions, added triggers `LOTO training records` and `who is authorized to enter the cell`. 1013 chars (first draft was 1039 — over the limit — trimmed).
- Builder body 7 → 66 non-blank lines: `## Roles — keep them distinct` (five-role table with may / may-not / training content); `## LOTO employee status — an attribute, not a role` (the (c)(7)(i)(A)/(B)/(C) definitions and the by-name rule); `## Every row: delivered vs demonstrated, with evidence type`; `## Retraining — conditions first, interval second` (the five (c)(7)(iii) conditions with robot-cell instances, then the employer-set interval with rationale); `## Certification and records` ((c)(7)(iv), retention, re-qualification path, revision block); `## Scope boundary` (no procedure content, no safety claim); `## Standards and references` table with editions and "do not cite 2012/2011"; `## Related skills`; `## Files in this skill`.
- Reviewer description rewritten to mirror the builder as checks. 992 chars.
- Reviewer body 10 → 46 lines: `## Role checks`, `## LOTO status checks` (including the roster-agreement check against `loto-procedure` — a chain-break finding), `## Delivered-vs-demonstrated checks`, `## Retraining checks`, `## Certification and records checks`, `## Edition and boundary checks`, `## Findings format` reserving top severity for **attendance recorded as competency**, **LOTO status inferred from role**, **interval as the only trigger**; the standard "does not modify the source" and FC/LC/PC/NO/NA line.
- `examples/operator-training-matrix-builder/README.md` and `.../checklist-reviewer/README.md`: blurbs refreshed from the new descriptions. Sample I/O remains TODO.
- Both archives re-zipped preserving every other payload entry (4 entries builder, 7 reviewer; `recalc.py`, `office/`, and the reviewer's placeholder scripts untouched). `unzip -t` clean; `name` re-read from inside each archive.
- **Process trap caught:** the first repack used `zip -r` without `-D`, which added three directory entries per archive (4 → 7, 7 → 10). Harmless to readers but it changes the entry count the log uses as a preservation check. Re-packed with `-X -D`. Second trap: the standards *table* wrote `| ISO/TS 15066 | 2016 ...|`, which `audit_pair_editions.py` cannot see (the year must follow the number), producing a transient asymmetry until written as `ISO/TS 15066:2016`. Same class as yesterday's `10218-1/-2` shorthand: always write the full `STANDARD:YEAR` token at least once.
- `scripts/audit_pair_editions.py` re-run: **1 mismatch / 10 asymmetries — unchanged.**

**Not done (descoped):** reviewer `check_definitions.py` / `_probe.py` / `dashboard.py` remain one-line placeholders — themed W37+ slot, not a polish side-effect. No generator script ships in the builder (same known gap as `robot-sop-builder`). The 1910.332 / NFPA 70E electrical-safety row for maintenance is named as conditional only; scoping it properly needs the cell's hazard assessment.

**Severity: high** — the skill the LOTO and SOP workbooks hand their training obligation to had no authorized/affected distinction, treated attendance as qualification, and inverted the regulation's retraining logic (interval only, no conditions).
