# Polish log — iso12100-risk-assessment-builder

## 2026-06-09 (POLISH, foundation domain)

**Severity:** low (applied) + med (follow-ups captured)

**Picked because:** Open weekly-target issue #13 (W24, foundation). Tied least-recently-touched
builder (2026-05-03). Foundation domain had not been polished in the recent cycle
(prior three logs: iso10218 / iso15066 / operating-envelope — compliance, cobot, amr).

**Edition verification (required for safety-critical domain):**
- ISO 12100:**2010** "Safety of machinery — General principles for design — Risk assessment and
  risk reduction" is the current edition. It consolidated ISO 12100-1:2003, ISO 12100-2:2003 and
  ISO 14121-1:2007. No superseding edition exists. ✅ Correct anchor is :2010.

**What's good:**
- Description accurately summarizes the ISO 12100 3-step iterative method (hazard identification →
  risk estimation → risk evaluation → risk reduction) and stays well under the 1024-char limit.
- Frontmatter (`name`, `description`) is well-formed; trigger phrasing is reasonable.
- Builder is paired with iso12100-risk-assessment-checklist-reviewer (no orphan).

**What to fix:**
1. (APPLIED) Description named only "ISO 12100" with no edition — added explicit **ISO 12100:2010**
   anchor and a clause reference (Clauses 5–6), and added "ISO 12100:2010" to the trigger list.
   431 → 485 chars, still < 1024.
2. (FOLLOW-UP, med) SKILL.md body is generic boilerplate ("Generates a complete, audit-ready
   workbook for iso12100 compliance assessment", "Use this skill when the user mentions iso12100,
   or related requirements"). Body heading reads "Iso12100 Builder" (mis-cased). Worth a content
   pass to describe the actual tabs/method — out of scope for a small POLISH edit.
3. (FOLLOW-UP, med) The "Files in this skill" tree advertises a `references/` directory with
   `methodology.md` and `iso12100_conventions.md`, but the packaged archive contains no
   `references/` folder (only SKILL.md, scripts/, and a `_coy0eze` placeholder). Either ship the
   reference files or correct the tree. Documentation/content mismatch — descoped.

**Suggested edits (next time):** rewrite body prose to name the workbook tabs and the
severity/probability rating tables; fix "Iso12100" casing; reconcile the references/ tree.
