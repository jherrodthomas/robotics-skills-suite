# safety-io-matrix-builder — polish log

## 2026-08-13 (POLISH, autonomous)

**Context:** W33 target #45 (W32 carryover; import baseline, untouched since 2026-05-03). Safety-critical domain (cell-design) → standard-edition verification performed.

**What's good**
- Description already covers the right content scope: F-DI/F-DO, dual-channel wiring, diagnostic coverage, response times, controller mapping.
- 11-tab workbook structure mirrors the polished interlock-estop-architecture pair, so cell-design outputs stay consistent.
- Scripts (recalc.py, office helpers) match the suite-standard scaffold; no drift found.

**What was fixed (this pass)**
- Standard editions were unpinned ("ISO 13849-1", "IEC 62061"). Pinned to ISO 13849-1:2023 and IEC 62061:2021; added ISO 10218-2:2025 and IEC 60204-1:2016 to the Standards section (edition mismatch — severity: med).
- Added OSSD/dual-channel wiring convention language reconciled with interlock-estop-architecture (polished 2026-06-17), including cross-circuit fault detection.
- Added per-row ISO 13849-1 PL/Category ↔ IEC 62061 SIL CL cross-reference convention, per the W33 definition of done.
- Reviewer updated in lockstep: edition pins, EDM/feedback monitoring check, SIL CL cross-reference consistency check, standards baseline section.

**Suggested edits (future, not applied — larger than a polish pass)**
- Builder could accept a JSON input schema doc the way newer builders do; currently input shape is implied only.
- Consider adding a PFHd budget column referencing ISO 13849-1:2023 Annex K.

**Severity:** med (edition mismatch on a safety-critical pair, now resolved)
