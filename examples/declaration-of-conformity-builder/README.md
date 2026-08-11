# Example — declaration-of-conformity-builder

**What this skill produces:** a multi-tab XLSX EU Declaration of Conformity (or Declaration of Incorporation) workbook, with the legal instrument, harmonised standards register, notified body block, technical file reference, and signatory block.

**Typical input shape:** manufacturer and authorised-representative details; machinery identification (denomination, function, model, type, serial); placing-on-market date; list of applicable Union legislation; standards applied with editions; conformity-assessment route and notified body if any; technical file compiler.

**Expected output:** `declaration-of-conformity-<machine-id>.xlsx` — signature-ready, with an OJEU-citation-status column recording which standard editions were verified as cited.

**Sample I/O:** in → *"Robot welding cell WC-04, placed on EU market Q1 2027, ISO 10218-2:2025 and ISO 13849-1:2023 applied, no notified body"*; out → workbook generated against **Regulation (EU) 2023/1230** (not the Directive — the date is after 20 Jan 2027), with both standards listed pending OJEU citation verification.

**Pair:** audit the result with `declaration-of-conformity-checklist-reviewer`.
