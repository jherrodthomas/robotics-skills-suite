# Polish log — five compliance/foundation reviewer descriptions

Themed target, issue [#51](https://github.com/jherrodthomas/robotics-skills-suite/issues/51).
Scope: frontmatter `description:` only, five files, no body changes.

---

## 2026-08-25 (POLISH, W35 target 1) — severity: **high** (safety-claim), resolved

### Files

| Skill | Domain |
| --- | --- |
| `ansi-r1506-compliance-matrix-checklist-reviewer` | compliance |
| `iec62061-sil-checklist-reviewer` | compliance |
| `iso13849-plr-checklist-reviewer` | compliance |
| `iso12100-risk-assessment-checklist-reviewer` | foundation |
| `iso10218-compliance-matrix-checklist-reviewer` | compliance |

### What was wrong

Reproduced all three defects before editing, and confirmed the set is exactly five — no sixth case in the 76.

1. **Generator framing.** All five opened `Generate an audit-ready … workbook`, describing what the *paired builder* produces. A reviewer that advertises itself as a generator will be selected to generate, which is the one thing it must not do.
2. **Broken trigger clause.** All five carried `Use this skill to review the user mentions …` — ungrammatical, and it destroys the trigger. `iso12100` was worse: `Use this skill to reviewever the user mentions`.
3. **Edition drift against the paired builder.** Four of five. Each file was internally consistent, which is why reading either half alone would not catch it.

### Edition verification

Mandatory for this target (safety-critical domains). Checked against the standards bodies, not against the builders.

| Reviewer said | Verified position | Action |
| --- | --- | --- |
| ANSI/RIA R15.06 **2012 (R2017)** | **Superseded.** ANSI/A3 R15.06-2025 Parts 1+2 approved 2025-08-21, published 2025-10-29 as a total revision; the 2012 edition is being withdrawn. Its own builder, one file away, cited 2025 correctly. | Rewritten to ANSI/A3 R15.06-2025, naming 2012 (R2017) as superseded |
| IEC 62061, *"safety-related **electrical** control systems"*, SRECS | **Wrong for the current edition.** IEC 62061:2021 (Ed. 2.0) dropped SRECS for **SCS**, because scope now covers pneumatic and hydraulic as well as electrical. Not merely a rename — a scope change. | Rewritten to IEC 62061:2021 / SCS; SRECS kept in the trigger list only, as a legacy search term |
| ISO 13849-1, undated | Current edition **ISO 13849-1:2023** | Dated |
| ISO 12100, undated | **ISO 12100:2010** still current | Dated |
| ISO 10218-1/-2 **2025** | Correct | No edition change; framing and trigger fixed |

### What was done

Each description rewritten to (a) open `Review and audit any …`, (b) carry `Use this skill when the user wants to review, audit, or confirm …`, (c) cite the same dated edition as its paired builder. Descriptions now name what the review actually interrogates — per-clause evidence mapping, CCF ≥65, HFT/SFF constraints, the 3-step iteration, Part 1 vs Part 2 duty separation — rather than restating the builder's feature list.

Verified after re-zip: all 76 archives pass `unzip -t`; repo-wide, **0** generator-framed reviewers and **0** broken trigger clauses remain. All five under the 1024-char limit (681–789).

**Deliberately not claimed:** no check counts, no dashboard, no auto-fill of FC/LC/PC/NO/NA. See below for why.

---

### Finding that outgrew the target — reviewer implementation tiers

While reading these five to write accurate descriptions, their `generate_checklist.py` turned out to be a stub that prints `Placeholder: generate checklist from …`, and `check_definitions.py` a single comment line. Scanning all 38 reviewers with the newly committed `scripts/audit_reviewer_impl.py`:

| Tier | Count | What it means |
| --- | --- | --- |
| **A — implemented** | 6 | Real generator (~7 KB) with a populated check table |
| **B — stub generator** | 16 | Generator present but writes placeholder tabs or only prints |
| **C — no generator** | 16 | No `generate_checklist.py` at all |

- **Tier B is the misleading tier.** Its SKILL.md walks the reader through `python scripts/generate_checklist.py`, tabulates a 7-tab output with a visual dashboard, and lists a `references/` tree — none of which the stub produces. All five of today's targets are tier B.
- **Tier C is not the same defect.** These ship a leaner prose body that documents the checks narratively and never claims a runnable script. Less bad than it first looked.
- **17 archives cite a `references/` directory that is not in the zip.** Concentrated in tiers A and B (13 of 16 tier B, 4 of 6 tier A).

**Why this changes the polish programme.** The recorded "placeholder-generator defect" has been carried in the weekly plans as affecting four skills. It affects 16, and the previously named four are split across two different tiers. More pointedly: `safety-io-matrix` (W32), `robot-hil-test-catalog` (W34) and `urdf-model-spec` (W34) are all **tier C**. Those passes rewrote descriptions to promise detailed verification against dated standards for packages with no code to run. The descriptions are good; they are writing cheques the archives cannot cash.

That is why today's five were written to describe *what a reviewer interrogates* rather than to promise counts, dashboards or auto-filled ratings. Tightening a description is safe; inflating one on a tier B or C package widens the gap.

### Follow-ups

- **Human decision, blocking further POLISH value:** decide whether the reviewer suite is meant to be runnable. If yes, tiers B and C need 32 generators and this is an implementation programme, not a weekly description slot. If no, the tier B bodies should drop the Workflow section and the `references/` tree so they stop advertising a generator that does not exist. Either way the answer changes what POLISH is for.
- Run `python3 scripts/audit_reviewer_impl.py` before picking any future POLISH target; record the tier in the weekly plan next to the domain.
- The five bodies polished today remain generic boilerplate (`Runs a confirmation review on any ansi-r1506 workbook`, "a ansi-r1506"). Out of scope for #51 and left untouched.
- `references/methodology.md` and `references/<name>_checks.md` are cited by 17 archives and shipped by none.
