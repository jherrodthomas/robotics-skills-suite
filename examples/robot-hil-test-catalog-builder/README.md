# robot-hil-test-catalog-builder — example

- **What this skill produces:** a 10-tab HIL test catalog workbook for a robot/safety controller — bench setup, fault-injection cases across sensor/comm/power/E-stop/timing families, state-machine tests, PLr/SIL targets, pass-fail criteria, and execution tracking.
- **Typical input shape:** the safety-function inventory and channel/OSSD rows from `safety-io-matrix-builder`, the PL/SIL claims and DC assumptions from `iso13849-plr-builder` or `iec62061-sil-builder`, and a description of what the HIL bench simulates versus what is real hardware.
- **Expected output:** xlsx catalog anchored on ISO 13849-1:2023 (PLr) / ISO 13849-2:2012 (validation method) / IEC 62061:2021 (SIL), with case IDs following `HIL-<function-id>-<class>-<nn>` and every DC assumption defended by at least one injection case.
- **Sample input:** _TODO — add sample safety-function inventory + PL claim input._
- **Sample output:** _TODO — add generated HIL test catalog xlsx._
