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
