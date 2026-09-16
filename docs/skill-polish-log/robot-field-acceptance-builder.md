# Polish log — robot-field-acceptance-builder

_Append only. Do not overwrite earlier entries (see 159b5c5)._

## 2026-09-16 (POLISH pass, W38 target — last inverted pair)

**Selection.** Rule (a) returned nothing: the open-issue list is **empty** — the #37-#59 backlog was bulk-closed 2026-09-11, which retires nine consecutive plan requests but also closed **#59 (the edition-asymmetry sweep) without the work being done**. Rule (b) returned nothing: 38/38 paired. Rule (c) returned this pair on both available measures at once — joint-oldest builder (2026-05-03, 136 days, the surviving import cohort) and the **last inverted pair** in the body-thinness ranking at 9 builder body lines against 14 reviewer lines. W37 named it the W38 lead. Both selectors agreeing is as strong as this task's priority rules get.

**What's good**
- The 11-tab contract was the right decomposition and survives unchanged: plan, re-verification, throughput, OEE, safety-under-load, environment, anomalies, trend, readiness, sign-off, lessons learned. Nothing needed restructuring.
- The pair's *position* in the suite was correct — it is genuinely the post-SAT phase, and `robot-acceptance-protocol` already pointed here.
- Descriptions were well-formed and under limit on both halves.

**What was wrong**
- **The builder named metrics without defining any of them.** Four bullets: "Overall Equipment Effectiveness OEE", "Throughput verification (parts/hour)". OEE is a product of three ratios and the entire dispute at handover is over their denominators; a skill that emits the acronym and stops produces a number nobody can argue with, which is the opposite of audit-ready.
- **Ideal cycle time had no stated source.** The failure mode this domain is built on: taking the *quoted* cycle as the Performance denominator turns a commercial promise into a measured machine loss. Unstated, it is the default.
- **Starved and blocked time was not mentioned at all.** It is the largest source of disputed availability at handover and cannot be reconstructed after the run — it has to be captured as its own state from the first interval.
- **"Safety function validation under load" was ambiguous in the dangerous direction.** Read one way it invites a field observation to stand in for the ISO 13849-2 validation done at FAT. Neither half drew that line.
- **No boundary at all.** Nothing stopped a signed field acceptance report being presented as evidence of safety conformity — which is the integrator's declaration under ISO 10218-2:2025, not a commercial acceptance document.
- Reviewer was eleven bullets restating the builder's tab names as "audit checklist": no rating vocabulary, no NO conditions, no statement of what failure looks like. Same defect class as the ros2 reviewer on 2026-09-15.
- **Neither half pinned a single edition** despite both depending on ISO 10218-2, ISO 13849 and ISO 9283. The edition audit did not flag the pair because asymmetry needs one half to pin — silence on both sides reads as clean.

**Applied**
- Builder rewritten from 4 metric bullets to a method: observation window with shifts and operators as the thing that distinguishes this from an extended SAT; throughput with recorded warm-up exclusion, contracted-vs-run part mix, declared steady-state criterion and declared rate denominator; an **OEE table giving each factor its definition and the denominator that must be declared**, with ideal cycle time required to come from demonstrated rather than quoted performance and one availability convention enforced across tabs; safety functions re-verified at production payload and speed with stopping distance re-measured on any payload/speed/tooling change; **operator defeats named as the expected output of the phase**; anomaly log separating containment from correction with explicit acceptance for every open item; trend read for direction, not average.
- **Boundary section added to both halves**: FAT/SAT belongs to `robot-acceptance-protocol`, manipulator performance to `iso9283-performance-test`, and no safety conformity is granted here.
- Reviewer rewritten as eight numbered check groups with FC/LC/PC/NO/NA. Framing sentence states the domain defect directly — every number here is a ratio, and every handover dispute is about the denominator. Highest-severity NO reserved for a design-level safety defect closed as a field anomaly at sign-off.
- Standards sections added to both halves, pinned and in lockstep.
- `## Implementation status` added to both halves.

**Verification**
- v&v is not on the mandatory safety-critical list, so the edition step did not fire. Run anyway, because the rewrite *introduced* six citations that did not exist before — writing years into a file is exactly the case W37 flagged as propagating rather than sitting still. Two corrections resulted, both caught by checking rather than assuming:
  - **ISO 13855 was retitled at the 2024 edition** to "Positioning of safeguards with respect to the approach of the human body". The 2010/2002 title — "protective equipment ... approach speeds" — is what the first draft carried, and is what most secondary sources still repeat. Both halves now carry the current title and note the retitle. Worth a look across the suite: any skill citing 13855:2024 under the old title has a right year on a wrong name.
  - **ISO 13849-2:2012 is current** (reviewed and confirmed 2018), but **ISO/DIS 13849-2 is at enquiry stage** and will supersede it. Both halves now say so. This affects every 13849-2 citation in the repo, not just this pair — captured as a follow-up, not touched here.
- ISO 10218-1/-2:2025, ISO 9283:1998 (confirmed 2021) and IEC 60204-1:2016 verified consistent with the `robot-acceptance-protocol` pair, which is the upstream this workbook cites.
- `audit_pair_editions.py` re-run: pair not listed before (both halves silent) or after (both halves pinned). The 15-claim asymmetry backlog across 8 other pairs is unchanged and still outstanding.
- Both archives repacked, `unzip -t` clean, round-trip read verified. Descriptions 887 / 840 chars, both under the 1024 ceiling.

**Implementation status**
Builder is tier C (no generator — `recalc.py` and `office/` helpers only); reviewer probe is a one-line stub. `audit_reviewer_impl.py` now reports 6 tier A / 16 tier B / 16 tier C across the suite. Both halves carry an explicit section so the documented contract is not mistaken for working code.

**Severity:** high. Not for factual error — the old files stated almost nothing, and nothing they stated was wrong. High because of what a report built from them would have claimed: an undecomposed OEE figure on a denominator nobody wrote down, and a sign-off with no line between commercial acceptance and safety conformity.

**Follow-ups**
- Builder-thinness is now **exhausted** as a selector — this was the last inverted pair. W38's PLAN slot was missed (see the journal), so the reviewer-thinness ranking W37 proposed as the successor measure has not been run. It should lead the next PLAN.
- ISO 13849-2 supersession watch, suite-wide.
- ISO 13855 title check, suite-wide.
- #59 asymmetry sweep is unfinished and its issue is closed. It needs a new issue or it will fall out of the loop entirely.
