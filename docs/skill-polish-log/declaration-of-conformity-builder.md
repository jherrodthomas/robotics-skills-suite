# Polish log — declaration-of-conformity (builder + checklist-reviewer)

## 2026-08-11 — first POLISH pass (severity: **high**)

Target from `docs/weekly/WEEK-2026-W33.md` #1, issue [#44](https://github.com/jherrodthomas/robotics-skills-suite/issues/44). Opened W31, carried through W32, third week open. Both files sat at the 2026-05-03 import baseline.

### What was good

- The builder's *description* frontmatter was the only part of either file that had real content: it already named both instruments and listed the DoC's constituent blocks (manufacturer, machine ID, harmonised standards, notified body, technical file, signatory). That list survived the rewrite largely intact.
- The pair was structurally complete — builder and reviewer both present, 7-tab reviewer skeleton matching house convention.

### What was wrong

| # | Finding | Severity |
|---|---|---|
| 1 | **Reviewer description was a copy of the builder description**, verbatim except for "Use this skill to review the user mentions…" — an ungrammatical patch over a paste. The reviewer therefore advertised itself as a *generator*. | high |
| 2 | Both bodies were placeholder text about a skill called "Doc" — *"Use this skill when the user mentions doc, or related requirements"*, *"doc substantive checks"*. `declaration-of-conformity` had been tokenised to `doc` at import and never restored. | high |
| 3 | **Legal instruments were named but never distinguished.** "Machinery Directive 2006 42 EC and the new Machinery Regulation 2023 1230" — no applicable date, no rule for which one governs, no statement that Directive 2006/42/EC is repealed. A DoC citing the wrong instrument is void, not untidy. | high |
| 4 | Instrument numbers were written **without slashes** (`2006 42 EC`, `2023 1230`), so they would not match any search or citation check. | med |
| 5 | No standards-baseline section on either file, in a *compliance*-domain pair whose entire job is listing standards. No ISO 10218-1/-2:2025, no ISO 13849-1:2023, no IEC 62061:2021. | high |
| 6 | **No mention that presumption of conformity is edition-specific and OJEU-citation-specific.** This is the single most common real DoC error: listing the newest edition of a standard as harmonised when the *Official Journal* still cites an older one. | high |
| 7 | Declaration of **Incorporation** (partly completed machinery, Annex II 1.B) not covered at all, despite being the more common output for integrators shipping cells. | med |
| 8 | Both file trees listed a `references/` directory containing `methodology.md` and `doc_conventions.md` / `doc_checks.md`. **No such directory exists in either archive.** Documented files that aren't there. | med |
| 9 | Reviewer archive carries two redundant near-empty probe stubs (`doc_probe.py` 184 B, `declaration-of-conformity-checklist_probe.py` 69 B) alongside `probe_workbook.py` (185 B). Same import artifact seen on `robot-cell-scope`. | low |
| 10 | Reviewer workflow step 4 said only "Iterate" — no named counterpart, and no statement that the source workbook is never modified. | low |

### Edition verification (safety-critical domain — required step)

| Reference | Status before | Status after |
|---|---|---|
| Machinery Regulation | "2023 1230", no date | **Regulation (EU) 2023/1230**, applies **20 Jan 2027**, repeals 2006/42/EC |
| Machinery Directive | "2006 42 EC", presented as co-current | **Directive 2006/42/EC**, governs placing on market up to **19 Jan 2027** |
| ISO 10218-1 / -2 | absent | **:2025** (Ed. 3 / Ed. 2) |
| ISO 13849-1 | absent | **:2023** (Ed. 5) |
| IEC 62061 | absent | **:2021** |
| ISO 12100 | absent | **:2010** |

### What was applied this run

- Builder rewritten: real title and purpose, 11-step workflow that **forks on legal instrument first**, output structure with an OJEU-citation-status column, full standards-and-legal baseline, Declaration of Incorporation coverage, GB/UKCA separation note, corrected file tree, generator-is-a-stub note.
- Reviewer rewritten: description now describes *reviewing*, not generating; added an explicit **"Edition and legal findings to raise"** list of 11 flaggable conditions; named `declaration-of-conformity-builder` as the iteration counterpart; added the never-modifies-source statement; corrected file tree.
- Both descriptions kept under the 1024-char frontmatter limit (builder 729, reviewer 808).
- `examples/` stubs created for both halves.

### Deliberately not done

- **No generator implementation.** `generate_doc.py` is 545 bytes of stub; writing a real DoC generator is a feature, not a polish pass. Same for the reviewer's four stub scripts.
- **No probe-file consolidation.** Deleting files from inside a `.skill` archive is a refactor; deferred, consistent with how the same finding was handled on `robot-cell-scope`.
- **No claim about current OJEU citation status of any specific standard edition.** This run could not verify the *Official Journal* list, so the skills instruct the user to verify it and record the result, rather than asserting that ISO 13849-1:2023 or ISO 10218-1:2025 are cited. Asserting harmonisation without checking is exactly the error the reviewer now flags — the skill should not commit it in its own text.

### Follow-ups

- Implement `generate_doc.py`, rename to `generate_declaration_of_conformity.py`.
- Consolidate reviewer probe stubs onto `probe_workbook.py` (repo-wide pattern — worth one dedicated pass across all 38 reviewers rather than one at a time).
- Consider a `ukca-declaration-builder` if GB scope comes up; deliberately kept out of the EU DoC.
- Human: issue #44 can be closed.
