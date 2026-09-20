| PS-007 | Output ripple and noise | C\* | TRIG | ET | — | T | T | T | T | CHG-01 · trigger: ripple can mask excursions, trip monitors or corrupt safety-relevant ADC readings |
| PS-008 | Load transient response | C\* | CORE\* | ET | — | REQ\* | REQ\* | REQ\* | REQ\* | CHG-07 · rails feeding safety-related loads |
| PS-009 | Line transient response | C\* | CORE\* | ET | — | REQ\* | REQ\* | REQ\* | REQ\* | CHG-07 · rails feeding safety-related loads |
| PS-010 | Start-up / turn-on | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-01 · include the start-up self-test (FUSA-004) |
| PS-011 | Shutdown / power-down | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-01 |
| PS-012 | Input inrush current | C\* | TRIG | ET | — | T | T | T | T | CHG-01 |
| PS-013 | Repeated restart / hiccup behavior | M\* | CORE | FT | — | REQ | REQ | REQ | REQ | CHG-14 · acceptance amended |
| PS-014 | Current limit / overload | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-01 |
| PS-015 | Output short circuit | M\* | CORE | FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| PS-016 | Output over-voltage protection | M\* | CORE | FT, FI | CF | REQ · FI+ | REQ · FI+ | REQ · FI++ | REQ · FI++ | CHG-02, CHG-16 |
| PS-017 | Reverse output / backfeed | C\* | CORE\* | FT | CF | REQ\* | REQ\* | REQ\* | REQ\* | CHG-09 · safe state = de-energized |
| PS-018 | Reverse input polarity | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 · where the supply specification requires it |
| PS-019 | Open supply / connector interruption (bench screen) | M\* | SUPP | — | — | — | — | — | — | CHG-05 · formal evidence: AUTO-010, AUTO-013, AUTO-014 |
| PS-020 | Ground offset | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 |
| PS-021 | Control-loop stability (Bode plot) | C\* | TRIG | DV | — | T | T | T | T | CHG-08 · REQ when the hardware safety requirement, FMEDA/DFA or claimed design margin requires physical loop verification |
| PS-022 | PSRR and output impedance | C\* | TRIG | DV | — | T | T | T | T | CHG-01 |
| PS-023 | Input-filter / harness interaction | C\* | TRIG | DV | — | T | T | T | T | CHG-01 · oscillation mode; review together with PS-021 |
| PS-024 | Hot-plug input overshoot | C\* | TRIG | ET | — | T | T | T | T | CHG-01 |
| PS-025 | Switching frequency, spread spectrum and pulse-skipping map | NAS | QUAL | — | — | — | — | — | — | CHG-01 · subharmonic findings feed PS-021 |
| PS-026 | Dropout and low-input tracking | M\* | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| PS-027 | Start-up into pre-bias and capacitive load | C\* | TRIG | FT | — | T | T | T | T | CHG-01 |
| PS-028 | Enable/wake input and power-good/RESET outputs | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-04 · RESET valid down to low VDD |
| PS-029 | Component stress and derating | C\* | TRIG | DV, WC | — | T | T | T | T · WC+ | CHG-08 · REQ when the safety case needs physical stress verification; WC+ applies at D when worst-case testing is selected |
| PS-030 | Output short to battery | C\* | CORE\* | FT, FI | CF | REQ\* | REQ\* | REQ\* | REQ\* | CHG-09 · outputs that leave the module |
| PS-031 | Cross-regulation and sequencing (multi-output) | C\* | CORE\* | FT, ET | — | REQ\* | REQ\* | REQ\* | REQ\* | CHG-13 · sequencing REQ for multi-rail supplies feeding an MCU/SoC; cross-regulation T |
| AUTO-001 | Long-term overvoltage | C\* | ROB | ET, ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| AUTO-002 | Transient overvoltage | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 · CORE if the input over-voltage lockout is a specified safety mechanism |
| AUTO-003 | Transient undervoltage | M\* | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| AUTO-004 | Jump start | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 · 12 V systems |
| AUTO-005 | Load dump | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 · test variant per the vehicle's load-dump clamping concept |
| AUTO-006 | Superimposed AC / alternator ripple | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 |
| AUTO-007 | Slow decrease and increase | M\* | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| AUTO-008 | Slow decrease / fast increase | C\* | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-06 |
| AUTO-009 | Reset behavior / brownout map | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-01 |
| AUTO-010 | Short supply interruptions | M\* | CORE | FT, ET | — | REQ | REQ | REQ | REQ | CHG-01 |
| AUTO-011 | Engine start / cold crank | C\* | CORE\* | ET, FT | — | REQ\* | REQ\* | REQ\* | REQ\* | CHG-06 · start-stop or engine restart while moving; otherwise ROB (++*) |
| AUTO-012 | Generator / smart charging voltage profile | C\* | ROB | ET | — | ++* | ++* | ++* | ++* | CHG-03 |
| AUTO-013 | Pin interruption | M\* | CORE | FT | CF | REQ | REQ | REQ | REQ | CHG-01 · include loss of ground with I/O connected |
| AUTO-014 | Connector interruption | M\* | CORE | FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| AUTO-015 | Closed-circuit/quiescent current | C\* | QUAL | — | — | — | — | — | — | CHG-11 · TRIG if a parked-vehicle safety function depends on battery charge |
| AUTO-016 | Backfeed into vehicle rail | C\* | CORE\* | FT | CF | REQ\* | REQ\* | REQ\* | REQ\* | CHG-09 · safe state = de-energized |
| AUTO-017 | Repetitive ON/OFF endurance | NAS | ROB | ALT | — | +* | +* | ++* | ++* | CHG-12 · use the MEND grade (++) for relays and contactors |
| AUTO-018 | Equalizing currents between supply inputs | C\* | CORE\* | FT, DFA | CF | REQ\* | REQ\* | REQ\* | REQ\* | CHG-10 · redundant feeds (decomposition or fail-operational) |
| AUTO-019 | Insulation resistance | NAS | TRIG\* | DFA | CF | T\* | T\* | T\* | T\* | CHG-15 · isolated HV-to-LV converters; otherwise QUAL |
| AUTO-020 | Withstand voltage (dielectric strength) | NAS | TRIG\* | DFA | CF | T\* | T\* | T\* | T\* | CHG-15 · isolated HV-to-LV converters; otherwise QUAL |
| TR-001 | ISO pulse 1 | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TR-002 | ISO pulse 2a | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TR-003 | ISO pulse 2b | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TR-004 | ISO pulses 3a / 3b | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TR-005 | Signal/control-line transient coupling | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TR-006 | Transients generated by the device under test | NAS | QUAL | — | — | — | — | — | — | CHG-01 |
| EMC-001 | Conducted emissions on power leads | NAS | QUAL | — | — | — | — | — | — | CHG-01 |
| EMC-002 | Radiated emissions | NAS | QUAL | — | — | — | — | — | — | CHG-01 |
| EMC-003 | Bulk current injection (BCI) | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| EMC-004 | Radiated immunity (absorber-lined shielded enclosure) | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| EMC-005 | Electrostatic-discharge immunity | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| EMC-006 | Conducted-emission pre-scan and near-field scan | NAS | SUPP | — | — | — | — | — | — | CHG-01 · formal evidence: EMC-001 |
| EMC-007 | Portable transmitter immunity | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| EMC-008 | Magnetic-field immunity | C\* | ROB | EMC | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-001 | High-temperature operation | M\* | CORE | ENV, ET | — | REQ | REQ | REQ | REQ | CHG-01 · verify monitor thresholds and timing at maximum ambient |
| TH-002 | Low-temperature operation / cold start | M\* | CORE | ENV, ET | — | REQ | REQ | REQ | REQ | CHG-01 · verify monitor thresholds and timing at minimum ambient |
| TH-003 | Thermal derating characterization | C\* | TRIG | DV | — | T | T | T | T | CHG-01 · coordinate thermal foldback with UV monitoring (FUSA-002) |
| TH-004 | Thermal shutdown and recovery | M\* | CORE | FT | — | REQ | REQ | REQ | REQ | CHG-14 · restart per the safe-state strategy |
| TH-005 | Temperature cycling | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-006 | Rapid temperature change / thermal shock | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-007 | Damp heat / humidity | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-008 | Electrical stress at temperature corners | M\* | CORE | ET, WC | — | REQ | REQ | REQ | REQ · WC+ | CHG-02 |
| TH-009 | Temperature step test | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-010 | Condensation | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| TH-011 | Location-dependent climatic tests | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| LIFE-001 | High-temperature operating life | C\* | ROB | ALT | — | +* | +* | ++* | ++* | CHG-12 |
| LIFE-002 | Power / thermal cycling | C\* | ROB | ALT | — | +* | +* | ++* | ++* | CHG-12 |
| LIFE-003 | Worst-case continuous operation | C\* | ROB | WC | — | o* | o* | o* | +* | CHG-12 · use the ALT grade if used as life evidence |
| LIFE-004 | Capacitor lifetime verification | C\* | ROB | ALT | — | +* | +* | ++* | ++* | CHG-12 |
| ENV-001 | Vibration | C\* | ROB | MECH | — | ++* | ++* | ++* | ++* | CHG-03 |
| ENV-002 | Mechanical shock | C\* | ROB | MECH | — | ++* | ++* | ++* | ++* | CHG-03 |
| ENV-003 | Dust / water / ingress protection | C\* | ROB | ENV | — | ++* | ++* | ++* | ++* | CHG-03 |
| ENV-004 | Automotive fluids exposure | C\* | ROB | CHEM | — | ++* | ++* | ++* | ++* | CHG-03 |
| ENV-005 | Free fall | C\* | ROB | MECH | — | ++* | ++* | ++* | ++* | CHG-03 |
| 48V-001 | 48-volt supply voltage range and slow transients | C\* | ROB | ET | — | ++\* | ++\* | ++\* | ++\* | CHG-03 · 48 V devices only |
| HV-001 | Voltage-class-B direct-current terminal electrical behavior | C\* | ROB | ET | — | ++\* | ++\* | ++\* | ++\* | CHG-03 · voltage-class-B devices only |
| HV-002 | High-voltage isolation, discharge and interlock | NAS | TRIG | FT, FI | CF | T | T | T | T | CHG-15 |
| FUSA-001 | Functional-safety mechanisms and fault reaction (umbrella) | M\* | CORE | FT, FI | — | REQ · FI+ | REQ · FI+ | REQ · FI++ | REQ · FI++ | CHG-16 · detailed in FUSA-002 to FUSA-011 |
| FUSA-002 | Threshold coordination and tolerance stack-up | new | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-16 |
| FUSA-003 | Fault reaction time vs FTTI | new | CORE | FT, FI | — | REQ · FI+ | REQ · FI+ | REQ · FI++ | REQ · FI++ | CHG-16 |
| FUSA-004 | Latent-fault detection of safety mechanisms | new | CORE\* | FT, FI | — | T | +\* | REQ\* | REQ\* | CHG-16 · triggered wherever latent-fault/self-test behaviour is an allocated safety requirement; LFM targets apply at B–D |
| FUSA-005 | Regulator/monitor independence (dependent failures) | new | CORE\* | FI, DFA | — | REQ\* · FI+ | REQ\* · FI+ | REQ\* · FI++ | REQ\* · FI++ | CHG-16 · wherever independence of regulation and monitoring is claimed |
| FUSA-006 | FMEDA-derived component fault-injection campaign | new | CORE\* | FI | — | FI+\* | FI+\* | FI++\* | FI++\* | CHG-16 · required where FMEDA/safety-case diagnostic-coverage claims need experimental substantiation |
| FUSA-007 | Safe-state path and safe-state maintenance | new | CORE | FT, FI | — | REQ | REQ | REQ | REQ | CHG-14, CHG-16 |
| FUSA-008 | Digital safety mechanisms (PMIC/SBC) | new | CORE\* | FT, FI | — | REQ\* · FI+ | REQ\* · FI+ | REQ\* · FI++ | REQ\* · FI++ | CHG-16 · devices with configuration memory, serial interface or watchdog |
| FUSA-009 | Redundant-supply switchover and emergency operation | new | CORE\* | FT, FI, DFA | — | REQ\* | REQ\* | REQ\* | REQ\* | CHG-16 · fail-operational or decomposed supply |
| FUSA-010 | Expanded functional testing: rare and out-of-specification inputs | new | ROB | EXP | — | o* | +* | +* | ++* | CHG-17 |
| FUSA-011 | 12 V-network overvoltage from 48 V or HV converter faults | new | CORE\* | FI, FT | CF | REQ\* · FI+ | REQ\* · FI+ | REQ\* · FI++ | REQ\* · FI++ | CHG-15 · 48 V-to-12 V and HV-to-LV converters |
| LIFE-005 | Over-limit (step-stress) margin test | new | ROB | OL | — | +* | +* | +* | +* | CHG-17 |

### 4.1 Classification summary

| Class | Total |
|---|---:|
| CORE | 25 |
| CORE* | 14 |
| TRIG | 12 |
| ROB | 38 |
| QUAL | 7 |
| SUPP | 2 |
| **Total** | **100** |

Relative to the previous 89-row mapping, this revision adds 11 rows and replaces the old three-class scheme with functional-safety role classes. PS-021 and PS-029 remain TRIG at all ASILs after review correction; FUSA-004 and FUSA-006 are conditional CORE* rows.

## 5. New rows: test outlines

Each outline gives purpose, method and acceptance. Add stimulus levels, equipment and the N6700 mapping when the rows are merged into the matrix (§10).

### FUSA-002 · Threshold coordination and tolerance stack-up

- **Purpose.** Show that the worst-case regulated output never reaches the OV/UV thresholds (no false trips), and that the thresholds, including their tolerance, trip before the load leaves its valid operating range (no undetected unsafe state).
- **Method.** Combine worst-case data from PS-001 to PS-004, PS-008, PS-009, TH-001, TH-002 and TH-008 with measured monitor thresholds, hysteresis and deglitch times over temperature. Add end-of-life drift from the post-stress re-measurements (§6, criterion 6).
- **Acceptance.** Regulation band including transients ⊂ monitor window ⊂ load's valid operating range, with a documented margin at each boundary.
- **References.** R4 clause 6 (hardware safety requirements, including attributes of safety mechanisms); R12.

### FUSA-003 · Fault reaction time vs FTTI

- **Purpose.** Verify that detection plus reaction completes within the fault tolerant time interval allocated to the supply (FDTI + FRTI ≤ FTTI).
- **Method.** Inject overvoltage, undervoltage and oscillation faults (PS-016 fixture, programmed source steps, feedback-path fault injection) at worst-case temperature and deglitch tolerance. Time-stamp fault onset, detection (flag, interrupt or error pin) and safe state reached (output off, reset asserted or downstream enable removed).
- **Acceptance.** Worst measured FDTI + FRTI ≤ allocated interval, with margin, across all samples.
- **References.** R1 (FTTI, FDTI, FRTI); R3 clause 6.

### FUSA-004 · Latent-fault detection of safety mechanisms

- **Purpose.** Verify that faults in the OV/UV comparators, their reference, the reset path and the safe-state path are found by start-up or periodic self-test within the multiple-point fault detection interval.
- **Method.** Using device test modes or fault-injection hooks, force a comparator stuck in its no-fault state, skew or disconnect the monitor reference, and open the reset or error output path. Confirm that the self-test flags each case and that the system reacts as specified (for example, blocks start-up).
- **Acceptance.** Every latent fault the FMEDA counts as detected is detected, at least once per multiple-point fault detection interval (typically at each drive-cycle start).
- **ASIL note.** No LFM architectural-metric target applies at ASIL A, but latent-fault/self-test verification can still be required at ASIL A when allocated by the safety concept. At ASIL B the LFM target is a recommendation; at ASIL C and D the LFM target applies (§3.4).