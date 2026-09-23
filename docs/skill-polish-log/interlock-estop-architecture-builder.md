# Polish log — interlock-estop-architecture-builder

## 2026-06-17 (POLISH, autonomous)

**Domain:** cell-design (safety-critical — standard-edition verification required)
**Severity of findings:** medium
**Action taken:** anchored standard editions + added three essential missing standards; re-packaged .skill

### What's good
- Clear, well-scoped description that enumerates the full device network (E-stops, interlocked gates, safety mats, light curtains, two-hand controls, enabling switches, trip wires).
- Correctly ties device architecture to ISO 13849-1 Categories B/1/2/3/4 and Performance Levels.
- Concrete, useful output spec (11-tab XLSX with response times, zone groupings, safety function matrix).
- Strong trigger phrasing ("E-stop architecture", "safety interlock plan", "gate interlock", "robot stop categories").

### What was fixed this run
1. **Edition anchoring** (small obvious fix, matches repo "anchor on edition" pattern): `ISO 13849-1` → `ISO 13849-1:2023` (current edition) in both the frontmatter description and the Standards section; `ISO 10218-1` → `ISO 10218-1:2025`.
2. **Missing essential standards added to the Standards reference list** (additive, no behavior change):
   - **ISO 13850:2015** — Emergency stop function, principles for design. This is THE E-stop design standard and was absent from an E-stop architecture builder.
   - **IEC 60204-1:2016** — Electrical equipment of machines; defines stop categories 0/1/2. The description markets "robot stop categories" but no standard governing stop categories was referenced.
   - **ISO 14119:2013** — Interlocking devices associated with guards. THE standard for gate-interlock design/selection; was absent from an interlock architecture builder.
3. **Terminology clarification note** added: architecture *Categories* (B/1/2/3/4, ISO 13849-1) vs *stop categories* (0/1/2, IEC 60204-1) — these are commonly conflated and the skill now distinguishes them.

### Suggested edits NOT taken this run (follow-ups)
- Consider surfacing stop-category (0/1/2) selection guidance inside the generated workbook tabs (would require touching recalc.py — out of scope for POLISH; needs a builder-logic review).
- Consider whether the description should explicitly name ISO 13850 / IEC 60204-1 as trigger context (frontmatter is already 454 chars; room remains under the 1024 limit but added length should be weighed against trigger precision).
- Verify the paired reviewer (interlock-estop-architecture-checklist-reviewer) checks for stop-category assignment and ISO 14119 interlock-defeat resistance; if not, file a reviewer-finding.

### Edition verification (safety-critical domain gate)
| Standard | Edition referenced | Current edition | Status |
|----------|-------------------|-----------------|--------|
| ISO 13849-1 | 2023 | 2023 | OK |
| ISO 13850 | 2015 | 2015 | OK |
| IEC 60204-1 | 2016 | 2016 | OK |
| ISO 14119 | 2013 | 2013 (+Amd 1:2024) | OK (base edition) |
| ISO 10218-1 | 2025 | 2025 | OK |

## 2026-09-23 (POLISH, autonomous) — W39 Wednesday target, issue #61

**Domain:** cell-design (safety-critical — edition verification required)
**Severity of findings:** **high** — one withdrawn standard edition was pinned, and the 06-17 entry above recorded it as OK
**Action taken:** reviewer rewritten into five rated check groups; builder brought into lockstep; ISO 14119 edition corrected; example README corrected; both archives re-zipped

### Edition error found — and the earlier verification in this log was wrong

The 06-17 table above records `ISO 14119 | 2013 | 2013 (+Amd 1:2024) | OK`. **That was incorrect.**
ISO 14119:2024 is a new edition, not an amendment: 3rd edition, published 2024-09-10, and the ISO
catalogue now lists ISO 14119:2013 as **withdrawn**. The builder has been pinning a withdrawn standard
since June and the log said it was fine. The 2024 edition folds in ISO/TS 19837 (trapped-key, Type 5
devices) and ISO/TR 24119 (fault masking in series-connected interlocks) — exactly the topics an
interlock-architecture workbook needs. Fixed in both halves and in `examples/.../README.md`. A
repo-wide grep found no other skill pinning `14119:2013`.

### Issue #61 also had an edition wrong

#61's "Verify" line asks for **IEC 60204-1:2018**. There is no 2018 IEC edition: the IEC edition is
**IEC 60204-1:2016 + AMD1:2021** (consolidated edition 6.1, 2021-09). "2018" is the European
harmonised adoption, EN 60204-1:2018 (now +A1:2025). Both halves now cite
`IEC 60204-1:2016+AMD1:2021` and state the EN equivalent in words. The builder's old `:2016` pin was
not wrong, only incomplete — it omitted the amendment.

### Edition verification (web-checked 2026-09-23)

| Standard | Was (builder / reviewer) | Now (both halves) | Status |
|---|---|---|---|
| ISO 13849-1 | 2023 / unpinned | 2023 | ✅ carried from prior verified passes |
| ISO 13849-2 | absent / absent | 2012, with DIS watch | ✅ ISO/DIS 13849-2 closed enquiry voting May 2026 — **not** cited |
| ISO 13850 | 2015 / unpinned | 2015 | ✅ reviewed and confirmed 2020, no revision in progress found |
| ISO 14119 | **2013** / unpinned | **2024** | ❌→✅ 2013 withdrawn; 3rd edition 2024-09 |
| ISO 14118 | absent / absent | 2017 | ✅ 2nd edition, current — added (unexpected start-up is half of what an interlock document is for) |
| IEC 60204-1 | 2016 / absent | 2016+AMD1:2021 | ⚠️→✅ amendment added |
| ISO 10218-1 | 2025 / unpinned | 2025 | ✅ carried |

### What's good (kept)
- The 06-17 Categories-vs-stop-categories note was the right instinct; it is now the organising rule of both halves.
- Device list (E-stops, gates, mats, curtains, two-hand, enabling, trip wires) is complete; trapped-key systems added to it.

### What was fixed — reviewer half (the real work)
- Body went from six bare topic bullets (zero checks, zero dated standards) to **five rated check groups**:
  E-stop Role and Coverage · Stop Category vs Architecture · Interlocking Guards · Reset and Restart ·
  Channel Integrity and Fault Exclusion.
- **E-stop as a complementary protective measure** made the first check: a hazard closed by "operator presses E-stop" is a finding.
- **Stop category and architecture Category must be separate fields** — a single "Category 3" column is rated as recording neither.
- ISO 14119 device type (1–5), coding level for Types 2/4, and a defeat-motivation assessment per guard; guard locking where run-down time exceeds access time.
- Every fault exclusion must be written as a claim with a justification; an unjustified one is PC regardless of the PL it props up.
- Span of control per E-stop, checked against the `robot-cell-layout` plan rather than a device count.
- Scope boundaries drawn against `robot-cell-layout` (distance), `safety-io-matrix` (wiring), `iso13849-plr` (PL arithmetic), `loto-procedure` (an interlock is not an isolation device).
- "Implementation status" section added, same wording pattern as `robot-cell-layout` — this reviewer is tier C (no generator; placeholder scripts only). Disclaimer avoids naming the generator file so `audit_reviewer_impl.py` stays at 0 phantom-generator hits.
- Description 314 → **959 chars** (65 under the limit; a first draft at 990 was trimmed for headroom).

### What was fixed — builder half (lockstep)
- Tab list expanded so each tab asks for what the reviewer checks (span of control, device type/coding level, fault-exclusion justifications, reset/restart path).
- "Two rules the workbook enforces" section mirrors the reviewer's two conflations.
- Description 454 → 702 chars. No script changes (builder ships no generator; `recalc.py` untouched).

### Audit results
- `audit_pair_editions.py`: ASYMMETRY **8 → 7** (this pair's four asymmetries cleared), MISMATCH unchanged at 2.
- Self-correction mid-run: the first reviewer draft wrote "supersedes ISO 14119:2013", which *created* a new MISMATCH
  (count 2 → 3) — the same false-positive shape as `robot-cell-scope` (#64). Reworded to "replaces the withdrawn 2013
  edition"; count back to 2. Second run in a row where the audit script punished a precise sentence.

### Suggested future edits (NOT done today)
- Wherever a polish log says an edition is "OK", it should record *how* it was checked (catalogue page vs memory). The 06-17 miss was an "OK" with no source.
- A two-hand control line could cite ISO 13851 once its edition is verified — left unpinned deliberately rather than guessed.
- When #63 is answered, the five groups here are specific enough to become a `CHECKS` table directly.
