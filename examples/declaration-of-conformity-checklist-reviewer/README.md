# Example — declaration-of-conformity-checklist-reviewer

**What this skill produces:** a 7-tab XLSX confirmation checklist with a visual dashboard, rating every check FC / LC / PC / NO / NA, with findings, evidence references, and recommended actions.

**Typical input shape:** the path to a DoC or Declaration of Incorporation workbook — from `declaration-of-conformity-builder` or any other source.

**Expected output:** `declaration-of-conformity-checklist-<machine-id>.xlsx`. The source workbook is never modified.

**Sample I/O:** in → a DoC citing *Directive 2006/42/EC* for machinery placed on the market in March 2027, listing "ISO 13849-1" with no edition; out → two high findings — wrong legal instrument for the placing-on-market date, and a harmonised standard listed without edition or OJEU citation check.

**Pair:** fix findings with `declaration-of-conformity-builder`.
