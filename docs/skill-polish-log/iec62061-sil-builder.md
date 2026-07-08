# Polish log: iec62061-sil-builder

## 2026-07-08

**Domain:** compliance (safety-critical — standard edition verified)

**What's good**
- Clear, specific frontmatter description covering the SIL determination method (severity / frequency / probability / avoidance) plus HFT and SFF analysis.
- Standard support-script layout (generate script, recalc.py, office/soffice.py) consistent with the rest of the suite.
- Description well under the 1024-char limit; trigger phrases cover the common user vocabulary.

**What to fix**
1. **HIGH — generator is a placeholder stub.** `scripts/generate_iec62061.py` is 19 lines and only prints "Placeholder: implement builder for iec62061". The skill cannot produce any workbook. This is precisely W28 target issue #34 — implementation is a large change, deliberately NOT done in this polish pass.
2. **MED — standard edition missing (fixed).** Description said "IEC 62061" with no edition. Anchored to **IEC 62061:2021**. Also note the 2021 edition replaced the term "SRECS" with "safety-related control systems (SCS)"; description now uses SCS while keeping SRECS as a legacy trigger keyword.
3. **MED — file tree mismatch (fixed).** SKILL.md listed `references/methodology.md` and `references/iec62061_conventions.md`, which do not exist in the archive. Tree corrected to actual contents.
4. **LOW — generic H1/body (partially fixed).** H1 was "Iec62061 Builder"; renamed to "IEC 62061 SIL Determination Builder" and tightened the when-to-use line. Body remains generic boilerplate — should be rewritten with real tab structure once the generator is implemented (#34).

**Suggested edits (deferred)**
- Implement the generator per issue #34: SIL assignment matrix (Se × Cl where Cl = Fr + Pr + Av per IEC 62061:2021 clause 6), subsystem architectural constraints (HFT/SFF, Table 6), and PFHd aggregation per safety function.
- Add a `references/` directory for real methodology notes, or keep the tree as-is.

**Severity:** high (non-functional generator) — tracked in issue #34.
