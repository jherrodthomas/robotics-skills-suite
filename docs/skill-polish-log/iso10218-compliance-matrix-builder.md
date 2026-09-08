# Polish log — iso10218-compliance-matrix-builder

## 2026-06-02 (POLISH, Tuesday)

**Selection rationale:** No open issues labeled `skill-bug` or `reviewer-finding`. No
orphan builders. All 38 builders tied at last-touched 2026-05-03. Aligned pick with
weekly target #5 (POLISH W23: iso10218-compliance-matrix — verify ISO 10218-1/-2:2025
edition); safety-critical compliance domain.

**Edition verification (mandatory for compliance domain):**
- Description anchors on **ISO 10218-1:2025 and ISO 10218-2:2025** — CORRECT current edition (the 2025 revision superseded the 2011 edition and folded in the bulk of ISO/TS 15066:2016 collaborative-robot content).
- Description explicitly notes the ISO/TS 15066 fold-in — CORRECT.
- No edition mismatch found.

**What's good:**
- Frontmatter `name` and `description` present; description is well-scoped (~480 chars, well under 1024).
- Description triggers on the right phrases: "ISO 10218", "robot compliance matrix", "robot integration compliance", "industrial robot safety compliance".
- Covers both ISO 10218-1 (manufacturer) and ISO 10218-2 (integrator) scope plus 15066 fold-in.
- Generator + recalc scripts present (`generate_iso10218.py`, `recalc.py`).

**What to fix:**
1. (low, applied) Title was "# Iso10218 Builder" — improper casing of the standard number and missing the "Compliance Matrix" qualifier from the skill name. Fixed to "# ISO 10218 Compliance Matrix Builder".
2. (low, applied) Body sentence "Generates a complete, audit-ready workbook for iso10218 compliance assessment." — corrected "iso10218" → "ISO 10218".
3. (low, applied) "Use this skill when the user mentions iso10218" — corrected casing.
4. (med, NOT applied — descope) `## Files in this skill` section claims a `references/` directory containing `methodology.md` and `iso10218_conventions.md`, but the skill archive contains only `SKILL.md` and `scripts/`. Either the references should be added or the claim removed from SKILL.md. Logging as follow-up for human review since adding content is a refactor, not a typo fix.
5. (med, NOT applied) `## When to use this skill` is one sentence: "Use this skill when the user mentions ISO 10218, or related requirements." Should enumerate the canonical triggers also listed in the frontmatter description (compliance matrix, integrator file, gap analysis, conformance status) for stronger in-skill self-documentation. Refactor-scale.
6. (med, NOT applied) `## Output structure` section is generic ("multiple tabs organized by assessment category") — should name the actual tabs the generator emits (Title Page, ISO 10218-1 Clause Matrix, ISO 10218-2 Clause Matrix, Cobot Annex, Evidence Index, Gap Tracker, Signoff). Requires reading `generate_iso10218.py` and is a refactor.

**Suggested edits (for next POLISH or human pass):**
- Either ship the two `references/*.md` files or strike the references/ block from `## Files in this skill`.
- Expand `## When to use this skill` with 3-5 bullet triggers.
- Replace `## Output structure` placeholder with the actual generated tab list.
- Consider adding a `## Methodology` short note linking to AIAG-style compliance-matrix patterns plus the 10218 Annex structure.

**Severity:** low (applied fixes are typo-class; remaining items are content gaps, not correctness bugs).

## 2026-09-08 (POLISH, Tuesday)

**Selection rationale:** W37 target #57, the Tuesday slot. Selected by the
builder/reviewer substance ratio (23-line builder body against a 36-line
reviewer, worst in the suite) and independently by `audit_pair_editions.py`,
which flagged the pair because the reviewer pinned ISO 10218-1:2025 and
ISO/TS 15066:2016 while the builder pinned neither. The thin half was the
unpinned half — two selectors agreeing from different directions.

**Edition verification (mandatory, compliance domain) — one correction to the plan:**

- **ISO 10218-1:2025 / ISO 10218-2:2025** — CONFIRMED current. Published and in
  force 1 April 2025, superseding the 2011 editions.
- **ANSI/A3 R15.06-2025** — CONFIRMED current, published 29 October 2025
  (Parts 1-2 approved 21 Aug 2025, Part 3 approved 7 Oct 2025). It is the US
  national adoption of ISO 10218-1/-2 and replaces ANSI/RIA R15.06-2012, which
  is withdrawn. **Note for `ansi-r1506-compliance-matrix`:** R15.06-2025 carries
  a **Part 3 with no ISO counterpart**, so the ANSI matrix is not a two-part
  mirror of the ISO one.
- **ISO/TS 15066:2016 — the W37 plan's reference table is wrong.** It states
  "still a TS and still current". The TS is flagged *to be revised* (26 June
  2025), its collaborative-application content has been folded into the 2025
  editions of ISO 10218-1/-2, and **ISO/AWI 15066-1 is under development to
  replace it**. The year 2016 is still the right pin — there is no newer
  published edition — but "still current" is not a safe description, and a
  matrix that defers a collaborative clause to the TS is deferring to a
  document being superseded. Both halves now say so explicitly.

  The pre-existing reviewer description already had this right ("folded into
  the 2025 edition ... rather than deferred to the technical specification").
  The builder is what was wrong. Recorded here because the plan asserted the
  builder-side framing and the plan's own standing instruction — *do not assume
  the builder is right* — is what caught it.

**What's good:**

- Reviewer description was already substantive, correctly scoped and correctly
  pinned; it needed sharpening, not rewriting. The lockstep edit was small.
- Both descriptions remain under the 1024-char limit (builder 943, reviewer
  1002). **Reviewer is within 22 chars of the ceiling — do not extend it
  further without cutting something.**

**What was fixed (applied):**

1. (high, applied) Builder body replaced its boilerplate "Use this skill when
   the user mentions ISO 10218, or related requirements" with the actual output
   contract: one row per clause carrying clause/Part/requirement/applicability/
   conformance verdict/evidence reference/responsible party/gap+corrective
   action. Closes polish-log item 6 from 2026-06-02.
2. (high, applied) **Part 1 vs Part 2 split made structural.** Part 1 binds the
   robot manufacturer; Part 2 binds the integrator across integration,
   commissioning, functional testing, programming, operation, maintenance and
   repair. Two matrices, not one. Stated with the reason: a merged list lets
   Part 1 manufacturer evidence appear to discharge a Part 2 integrator duty.
3. (high, applied) Builder now pins ISO 10218-1:2025, ISO 10218-2:2025 and
   ISO/TS 15066:2016, matching the reviewer. `audit_pair_editions.py`
   ASYMMETRY count drops 10 → 9; the pair no longer appears.
4. (med, applied) Boundary against `ansi-r1506-compliance-matrix` drawn in both
   halves, both directions, naming R15.06-2025 and the non-interchangeability.
5. (med, applied) Collaborative-application handling stated as a rule in both
   halves: assess in place against the 2025 clauses; a row reading "see
   ISO/TS 15066" is a **gap, not a conformance route**. Also captured that the
   2025 editions say "collaborative application", not "collaborative robot".
6. (med, applied) Reviewer body gained the checks matching the above, grouped
   Structure / Per clause / Editions. Previously it listed only generic
   "verify compliance against iso10218 requirements".
7. (med, applied) **Closes polish-log item 4 from 2026-06-02** — the
   `## Files in this skill` block in both halves claimed a `references/`
   directory (`methodology.md`, `iso10218_conventions.md`) that is not in
   either archive. Struck. The block now matches the archive exactly.
8. (med, applied) Reviewer now requires a justification for every
   "not applicable" — an unjustified N/A was the one way to make every clause
   pass without evidence, and neither half previously caught it.

**What was NOT fixed (descoped, repo-wide):**

9. (high, NOT applied — repo-wide, needs a human decision) **Every script in
   this pair is a stub.** `generate_iso10218.py`, `generate_checklist.py` and
   `iso10218_probe.py` all print "Placeholder". This is not specific to this
   pair: `audit_reviewer_impl.py` puts 32 of 38 reviewers in tier B (stub
   generator) or tier C (no generator), with only 6 implemented. Both SKILL.md
   files now carry an **`## Implementation status`** section saying so plainly,
   so the documented contract cannot be mistaken for working code. Implementing
   the generators is a project, not a polish pass.
10. (low, NOT applied) `generate_iso10218.py` carries a comment with an
    absolute path from an unrelated machine —
    `/sessions/…/CL work/automotive-skills-suite/source/hara-builder/…`.
    Cosmetic, but it leaks a local path and points at a suite that is not this
    repo. **Present in 6 skills**, so it is a one-line sweep across all six
    rather than a single-file edit here. Carried as a W38 candidate.

**Severity:** high — the builder was the unpinned half of the compliance
keystone pair, and its body did not state the Part 1 / Part 2 split that is the
skill's entire reason to exist. Both are now closed.

**Follow-ups:**

- Correct the W37/W38 standing reference table: ISO/TS 15066:2016 is "current
  edition, being superseded" — not "still current".
- `ansi-r1506-compliance-matrix` should state that R15.06-2025 has a Part 3
  with no ISO counterpart. Verified this run; that pair was not touched.
- Six-skill sweep for the leaked `/sessions/…` path comment (item 10).
- Reviewer description is 22 chars from the 1024 ceiling.
