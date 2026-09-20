# ISO 26262 ASIL Mapping for Automotive Power-Supply Validation Tests

_Last reviewed: 2026-09-20_

This file maps the 89 tests in [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md) to functional-safety relevance under ISO 26262.

> **Important:** ISO 26262 does not define a universal list of bench tests that becomes mandatory solely because an item is ASIL A, ASIL B, ASIL C or ASIL D. The mandatory verification activities are derived from the safety goals, technical safety requirements, hardware safety requirements, safety mechanisms, safety analyses and item operating environment. ISO 26262-4 requires item integration/testing and safety validation; ISO 26262-5 requires hardware integration and verification; ISO 26262-8 defines verification as a supporting process; ISO 26262-9 covers ASIL-oriented and safety-oriented analyses.

Therefore the mapping below uses:

- **Mandatory\*** — include this test when it verifies an allocated safety requirement, fault reaction, safe-state behavior or safety mechanism for the safety-related power supply. Once applicable, verification is required at **all four ASIL levels**; higher ASIL changes rigor, coverage, independence and evidence, not simply the existence of the test.
- **Conditional\*** — mandatory only when the hazard analysis, safety analysis, technical safety concept, hardware safety requirements, identified dependent failure, or customer operating environment makes this failure mode/stress safety-relevant.
- **Not ASIL-specific** — ISO 26262 does not make this test mandatory merely because of ASIL. It can still be mandatory under ISO 16750, ISO 7637, CISPR 25, ISO 11452, LV 124/VW 80000, ISO 6469, customer specifications, or the product design-validation plan.

The four ASIL columns are intentionally often identical. This is not an omission: ISO 26262 primarily scales the **assurance rigor and required evidence** with ASIL rather than prescribing a progressively larger fixed list of electrical bench tests.

## ASIL mapping

| Test ID | Test | ISO 26262 — ASIL A | ISO 26262 — ASIL B | ISO 26262 — ASIL C | ISO 26262 — ASIL D |
|---|---|---|---|---|---|
| PS-001 | Input operating range | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-002 | Output voltage accuracy | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-003 | Line regulation | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-004 | Load regulation | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-005 | Efficiency map | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| PS-006 | No-load / standby consumption | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-007 | Output ripple and noise | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-008 | Load transient response | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-009 | Line transient response | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-010 | Start-up / turn-on | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-011 | Shutdown / power-down | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-012 | Input inrush current | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-013 | Repeated restart / hiccup behavior | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-014 | Current limit / overload | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-015 | Output short circuit | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-016 | Output over-voltage protection | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-017 | Reverse output / backfeed | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-018 | Reverse input polarity | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-019 | Open supply / connector interruption | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-020 | Ground offset | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-021 | Control-loop stability | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-022 | Power-supply rejection and output impedance | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-023 | Input-filter / harness interaction | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-024 | Hot-plug input overshoot | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-025 | Switching frequency, spread spectrum and pulse-skipping map | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| PS-026 | Dropout and low-input tracking | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-027 | Start-up into pre-bias and capacitive load | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-028 | Enable/wake input and power-good/reset outputs | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| PS-029 | Component stress and derating | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-030 | Output short to battery | Conditional* | Conditional* | Conditional* | Conditional* |
| PS-031 | Cross-regulation and sequencing for multi-output supplies | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-001 | Long-term overvoltage | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-002 | Transient overvoltage | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-003 | Transient undervoltage | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-004 | Jump start | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-005 | Load dump | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-006 | Superimposed alternating voltage / alternator ripple | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-007 | Slow decrease and increase | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-008 | Slow decrease / fast increase | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-009 | Reset behavior / brownout map | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-010 | Short supply interruptions | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-011 | Engine start / cold crank | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-012 | Generator / smart-charging voltage profile | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-013 | Pin interruption | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-014 | Connector interruption | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| AUTO-015 | Closed-circuit / quiescent current | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-016 | Backfeed into vehicle rail | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-017 | Repetitive on/off endurance | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| AUTO-018 | Equalizing currents between supply inputs | Conditional* | Conditional* | Conditional* | Conditional* |
| AUTO-019 | Insulation resistance | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| AUTO-020 | Withstand voltage / dielectric strength | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| TR-001 | ISO pulse 1 immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| TR-002 | ISO pulse 2a immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| TR-003 | ISO pulse 2b immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| TR-004 | ISO pulses 3a / 3b immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| TR-005 | Signal/control-line transient coupling | Conditional* | Conditional* | Conditional* | Conditional* |
| TR-006 | Transients generated by the device under test | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| EMC-001 | Conducted emissions on power leads | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| EMC-002 | Radiated emissions | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| EMC-003 | Bulk current injection immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| EMC-004 | Radiated radio-frequency immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| EMC-005 | Electrostatic-discharge immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| EMC-006 | Conducted-emission pre-scan and near-field scan | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| EMC-007 | Portable-transmitter immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| EMC-008 | Magnetic-field immunity | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-001 | High-temperature operation | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| TH-002 | Low-temperature operation / cold start | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| TH-003 | Thermal derating characterization | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-004 | Thermal shutdown and recovery | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| TH-005 | Temperature cycling | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-006 | Rapid temperature change / thermal shock | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-007 | Damp heat / humidity | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-008 | Electrical stress at temperature corners | Mandatory* | Mandatory* | Mandatory* | Mandatory* |
| TH-009 | Temperature step test | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-010 | Condensation | Conditional* | Conditional* | Conditional* | Conditional* |
| TH-011 | Location-dependent climatic tests | Conditional* | Conditional* | Conditional* | Conditional* |
| LIFE-001 | High-temperature operating life | Conditional* | Conditional* | Conditional* | Conditional* |
| LIFE-002 | Power / thermal cycling | Conditional* | Conditional* | Conditional* | Conditional* |
| LIFE-003 | Worst-case continuous operation | Conditional* | Conditional* | Conditional* | Conditional* |
| LIFE-004 | Capacitor lifetime verification | Conditional* | Conditional* | Conditional* | Conditional* |
| ENV-001 | Vibration | Conditional* | Conditional* | Conditional* | Conditional* |
| ENV-002 | Mechanical shock | Conditional* | Conditional* | Conditional* | Conditional* |
| ENV-003 | Dust / water / ingress protection | Conditional* | Conditional* | Conditional* | Conditional* |
| ENV-004 | Automotive fluids exposure | Conditional* | Conditional* | Conditional* | Conditional* |
| ENV-005 | Free fall | Conditional* | Conditional* | Conditional* | Conditional* |
| 48V-001 | 48-volt supply voltage range and slow transients | Conditional* | Conditional* | Conditional* | Conditional* |
| HV-001 | Voltage-class-B direct-current terminal electrical behavior | Conditional* | Conditional* | Conditional* | Conditional* |
| HV-002 | High-voltage isolation, discharge and interlock | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific | Not ASIL-specific |
| FUSA-001 | Functional-safety mechanisms and fault reaction | Mandatory* | Mandatory* | Mandatory* | Mandatory* |

## Interpretation for the safety case

The **Mandatory\*** rows are the first tests to trace directly to hardware safety requirements and technical safety requirements. For each applicable row, the test specification should record the requirement identifier, ASIL, operating mode, initial condition, fault/stimulus, expected safe-state or degraded-state behavior, diagnostic response, reaction time, fault-tolerant time interval where applicable, acceptance criteria, sample count and evidence artifact.

For **Conditional\*** rows, do not automatically omit the test. Use the hazard analysis and risk assessment, failure-mode analysis, dependent-failure analysis, hardware safety analysis and customer environmental specification to decide applicability. If the analysis shows that the disturbance can violate a safety goal, the corresponding verification becomes part of the safety plan regardless of whether the row originated from ISO 16750, ISO 7637, ISO 11452 or another qualification standard.

The **Not ASIL-specific** rows remain valuable design-validation and qualification evidence. ISO 26262 explicitly does not replace nominal-performance or environmental/EMC standards, and high-voltage electrical-shock safety is handled by standards such as ISO 6469-3 rather than by ISO 26262 itself.

## Highest-priority ISO 26262 power-supply tests

For a safety-related power supply, the rows currently classified **Mandatory\*** are:

- PS-001, PS-002, PS-010, PS-011, PS-013, PS-014, PS-015, PS-016, PS-019, PS-026 and PS-028;
- AUTO-003, AUTO-007, AUTO-009, AUTO-010, AUTO-013 and AUTO-014;
- TH-001, TH-002, TH-004 and TH-008;
- FUSA-001.

These 22 rows should be the starting point for direct safety-requirement traceability. The 57 **Conditional\*** rows then become mandatory wherever the item-specific safety analysis identifies the corresponding stress or failure mode as safety relevant.

## ISO 26262 references

- ISO 26262-4:2018 — Product development at the system level: https://www.iso.org/standard/68386.html
- ISO 26262-5:2018 — Product development at the hardware level: https://www.iso.org/standard/68387.html
- ISO 26262-8:2018 — Supporting processes: https://www.iso.org/standard/68390.html
- ISO 26262-9:2018 — ASIL-oriented and safety-oriented analyses: https://www.iso.org/standard/68391.html
- ISO 26262 package overview: https://www.iso.org/publication/PUB200262.html

As of 2026-09-20, the 2018 editions remain the published editions while third-edition Draft International Standards are under development. Use the edition required by the customer/project safety plan.

## Recommended next step

The next useful refinement is to replace the generic `Mandatory*` / `Conditional*` mapping with a **project-specific traceability matrix** containing:

`Safety goal → Technical safety requirement → Hardware safety requirement → ASIL → Test ID → Fault injection/stimulus → Expected safe state → Reaction-time limit → Evidence/report`.

That project-specific mapping is what turns this generic ISO 26262 applicability map into auditable functional-safety verification evidence.