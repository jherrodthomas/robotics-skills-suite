# Polish log: ansi-r1506-compliance-matrix-builder

## 2026-07-15

**Picked because:** least-recently-touched builder (2026-05-03 cohort; alphabetically first of the 23 tied builders). No open skill-bug / reviewer-finding issues and no orphan builders today.

**What's good**
- Trigger phrases in the description are specific (ANSI R15.06, RIA R15.06, US market compliance) and the OSHA 1910 cross-reference framing is exactly what US integrators need.
- Clean, minimal script layout (generator + recalc + soffice helper) consistent with the rest of the suite.
- Description length well under the 1024-char limit.

**What to fix**
1. **Standard edition outdated (safety-critical domain check).** Description cited "ANSI/RIA R15.06 2012 R2017". Verified via web (automate.org, ANSI webstore, ANSI blog): **ANSI/A3 R15.06-2025** was published September 2025 as the U.S. national adoption of **ISO 10218-1:2025 and ISO 10218-2:2025**, superseding R15.06-2012 (R2017); a Part 3 (R15.06-3-2025, end-user requirements) now also exists. FIXED — description and "When to use" section re-anchored on R15.06-2025 with the superseded edition noted; added "A3 R15.06" trigger phrase (RIA is now A3).
2. **File tree inaccurate.** SKILL.md listed `references/methodology.md` and `references/ansi-r1506_conventions.md` that do not exist in the archive, and omitted `scripts/office/__init__.py`. FIXED — tree now matches actual archive contents.
3. **Title casing.** "# Ansi R1506 Builder" → "# ANSI/A3 R15.06 Compliance Matrix Builder". FIXED.

**Suggested edits (deferred — too large for a polish pass)**
- The 2025 revision restructured clause numbering and roughly doubled the safety-function catalog (Part 1: 50→95 pages; Part 2: 72→223 pages). The generator's clause list in `generate_ansi-r1506.py` almost certainly still reflects the 2012 clause structure and needs a full remap to the 2025 clauses — this is a real content refactor, not a polish fix.
- Consider adding coverage for R15.06-3-2025 (end-user/operational requirements) as either a tab or a companion skill target for a future PLAN week.
- Consider restoring the deleted `references/` notes as actual files (methodology + conventions) rather than leaving the skill script-only.

**Severity:** high (compliance-domain skill cited a superseded standard edition) — description-level issues resolved this run; generator clause remap deferred and flagged as a follow-up.
