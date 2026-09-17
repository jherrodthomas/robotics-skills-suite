# Polish log — zone-conduit-plan pair

Covers `zone-conduit-plan-builder.skill` and `zone-conduit-plan-checklist-reviewer.skill`.

---

## 2026-09-17 — first pass (severity: med)

Picked as the least-recently-touched builder in the repo (untouched since 2026-05-03, tied with
`perception-test-catalog` and `wireless-coexistence-plan`, none of which had a polish log). No open
issues and no orphan builders, so selection fell through to rule (3). Domain is cybersecurity, which
is safety-critical, so the standard editions were verified explicitly.

### What's good

- The reviewer is one of only **6 tier-A reviewers** in the suite (`scripts/audit_reviewer_impl.py`):
  7,463-byte generator with a real `CHECKS` table of exactly 27 entries, nine per assessment tab,
  each carrying a High/Medium/Low confidence. The description's "27 standard checks" is a promise the
  package can actually keep — unusual here, and worth protecting.
- Check IDs are clean and stable (ZD1-9 / CP1-9 / RM1-9) and the categories map 1:1 onto the output tabs.
- CP6 ("unused protocols and ports explicitly denied") and RM2 ("implicit deny at end") encode
  deny-by-default properly rather than gesturing at it.
- The builder's 11-tab structure is sound and in a sensible order — scope, zones, conduits, then rules.

### What was wrong

1. **No standard edition anywhere, in either skill (med).** Both descriptions said a bare "IEC 62443".
   That family spans a dozen parts, and the two this skill actually depends on say different things:
   zone and conduit partitioning is **IEC 62443-3-2:2020** (requirements ZCR 1-7), while the SL1-SL4
   scale and FR1-FR7 come from **IEC 62443-3-3:2013**. Component capability is **IEC 62443-4-2:2019**.
   A reader could not tell which document to open.

2. **SL-T / SL-C / SL-A were conflated (med).** The builder said only "Security Level per Zone —
   assigned SL1-SL4". Those are three different quantities: SL-T is the target the zone must reach,
   SL-C is what a product is capable of, SL-A is what the built system achieves. A plan records SL-T.
   Collapsing them invites the classic failure where a gap between target and achieved gets closed by
   quietly lowering the target instead of being raised as a finding.

3. **ZCR 3 partitioning rules absent (med — the substantive one).** Step 1 asked for "proposed zones"
   as free-form user input. But 62443-3-2 ZCR 3.1-3.5 makes four partitions mandatory: safety-related
   systems in their own zone, IACS separated from non-IACS, wireless in its own zone, remote-access
   devices in their own zone, and the rationale documented. The builder never stated them, so a plan
   that merges the safety PLC into the control zone would pass the builder's own review prompts. The
   reviewer did carry this as ZD8 but never named the requirement it implements.

4. **Both file manifests were fiction (low, but corrosive).** The builder advertised
   `references/methodology.md`, `references/firewall_patterns.md` and
   `examples/sample_input_robotic_cell.json`; none are in the archive. The reviewer advertised a
   `references/` directory of four files (absent), named its probe `zone_conduit_probe.py` when the
   shipped file is `zone-conduit-plan-checklist_probe.py`, and omitted `dashboard.py` entirely. This is
   the repo-wide phantom-`references/` defect from 2026-08-25; this pair was one of 16 carrying it.

5. **Reviewer Step 3 didn't match its own tab table (low).** The walkthrough enumerated five assessment
   tabs — "Firewall & Rule Completeness", "High-Assurance Boundaries", "Monitoring & Logging" — against
   an output table listing three, with different names. Neither matched the `CHECKS` categories.

### Applied this run

- Both descriptions rewritten with dated editions (62443-3-2:2020, 62443-3-3:2013, 62443-4-2:2019),
  SL-T named explicitly. Builder 758 chars, reviewer 902 chars, both under the 1024 limit.
- Builder Step 1 now states ZCR 3.1-3.5 as five checkable conditions with a one-line consequence.
- Builder Step 2 distinguishes SL-T from SL-C and SL-A, and says a target/achieved gap is a finding.
- Builder gained a short "Standards this plan is written against" table with editions and what each supplies.
- Both manifests corrected to the actual archive contents; the three placeholder scripts in the reviewer
  are now labelled as placeholders not called by the workflow, rather than presented as working parts.
- Reviewer Step 3 collapsed to the three real tabs, keyed to ZD1-9 / CP1-9 / RM1-9, with ZD8 identified
  as the ZCR 3.1 check. Added a scope note stating the review covers the plan and not the running
  network, so SL-A is out of scope.

**Gotcha for future runs:** the reviewer description initially failed YAML parse — `(9: zones defined…)`
put a `": "` inside an unquoted scalar. Validate frontmatter with `yaml.safe_load` after any description
rewrite; the `.skill` is a zip, so a broken header is invisible to `git diff`.

### Not done — follow-ups

- **(med)** `check_definitions.py`, `dashboard.py` and the probe are one-line stubs. For a tier-A
  reviewer the check table should live in `check_definitions.py` and be imported, not be inlined in the
  generator. Real refactor; needs its own session.
- **(med)** Re-key the 27 checks to the ZCR requirement each implements (ZD8 → ZCR 3.1, and so on) so
  findings cite a clause. Mechanical but touches every row.
- **(low)** Builder ships no example input JSON, yet Step 3 invokes the generator with one. A
  `sample_input_robotic_cell.json` for a cobot cell plus AMR fleet would make the skill runnable as
  documented. Was advertised in the old manifest; now simply absent rather than falsely promised.
- **(low)** 15 other skills still advertise a phantom `references/`. Worth one sweep rather than
  15 polish passes.
