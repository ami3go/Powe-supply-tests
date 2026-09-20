- **References.** R4 clause 8 (LFM); R1 (multiple-point fault detection interval); R12 (analog BIST).

### FUSA-005 · Regulator/monitor independence (dependent failures)

- **Purpose.** Show that a fault in a shared resource cannot corrupt regulation and its monitoring at the same time.
- **Method.** From the DFA, inject: reference or bandgap drift; feedback-divider open and short; feedback pin shorted to neighbouring pins; loss or degradation of the monitor's supply and ground; clock failure; local overtemperature. Verify that the monitor, or a second mechanism, still detects the resulting output deviation.
- **Acceptance.** No single shared-resource fault leads to an undetected output excursion beyond the safety limit.
- **References.** R6 clause 7; R12 (shared bandgap and feedback node).

### FUSA-006 · FMEDA-derived component fault-injection campaign

- **Purpose.** Where the FMEDA or safety case claims diagnostic coverage that needs experimental substantiation, verify the claimed detection of representative component failure modes used in the SPFM/LFM argument.
- **Method.** For each FMEDA line that claims coverage, physically inject the failure mode where it is safe to do so (fixtures, zero-ohm links, relays): high-side switch drain–source short (output rises towards the input voltage), output capacitor open (oscillation), feedback divider open or short, current-sense resistor drift, inductor short, reference drift.
- **Acceptance.** The observed effect and detection match the FMEDA; correct the FMEDA where they do not.
- **References.** R4 clause 10 (fault injection testing), clause 8, Annex D (power-supply failure modes).

### FUSA-007 · Safe-state path and safe-state maintenance

- **Purpose.** Verify the path from fault detection to safe state, independently of the monitored function, and that the safe state is held until the specified recovery condition.
- **Method.** Trigger each safety mechanism and verify the safe-state outputs (error or fail-safe pin, reset, enable of downstream drivers), including with the microcontroller unresponsive. Verify latched versus retry behaviour and retry counters, and that PS-013 hiccup restart or TH-004 thermal restart cannot exit a latched safe state.
- **Acceptance.** Safe state reached and maintained as specified; recovery only through the specified condition.
- **References.** R3 clause 6.

### FUSA-008 · Digital safety mechanisms (PMIC/SBC)

- **Purpose.** Verify the digital safety mechanisms of an integrated power-management device, where present.
- **Method.** Corrupt configuration registers or their OTP shadow through test modes and verify CRC detection at start-up and periodically; inject CRC and framing errors on SPI or I²C; stop or skew the clock; apply early, late and wrong-answer watchdog faults; run the logic BIST.
- **Acceptance.** Every fault is detected, with the reaction specified in the device safety manual.
- **References.** R12; R8; device safety manual.

### FUSA-009 · Redundant-supply switchover and emergency operation

- **Purpose.** For fail-operational or decomposed supplies, verify that loss of one supply path does not interrupt the safety function beyond its tolerance and that the paths stay independent.
- **Method.** Fail each path under load (open, short to ground, short to battery, overvoltage). Measure switchover time and hold-up; verify isolation of the faulted path (ideal-diode or OR-ing function; AUTO-018 cross-currents); verify the emergency-operation duration against the EOTTI.
- **Acceptance.** No interruption beyond specification; faulted path isolated; emergency operation sustained for at least the EOTTI.
- **References.** R1 (EOTTI); R3 clause 6; R6 clauses 5 and 7.

### FUSA-010 · Expanded functional testing: rare and out-of-specification inputs

- **Purpose.** Check behaviour under inputs that are rare or outside the specification, as the clause-10 robustness methods describe.
- **Method.** Invalid or corrupted commands; enable toggling during start-up and shutdown; a fault during start-up; combined stresses such as crank plus load step, or maximum temperature plus minimum input plus maximum load; enable glitches at threshold.
- **Acceptance.** Behaviour matches the requirements; no undefined or latched unsafe state.
- **References.** R4 clause 10.

### FUSA-011 · 12 V-network overvoltage from 48 V or HV converter faults

- **Purpose.** For 48 V-to-12 V and HV-to-LV converters, verify protection of the 12 V network against converter-internal faults.
- **Method.** Inject a high-side switch short or power-stage bypass; simulate a 48 V-to-12 V cross-short at the converter output; for isolated converters, combine with the AUTO-019 and AUTO-020 insulation evidence. Verify output disconnection or clamping and its reaction time.
- **Acceptance.** The 12 V network voltage stays within the limit and duration defined by the safety concept.
- **References.** R6 clause 7; R18; CHG-15.

### LIFE-005 · Over-limit (step-stress) margin test

- **Purpose.** Determine the margin between the specification limits and the functional and destruct limits.
- **Method.** Step temperature, input voltage and, where available, vibration beyond the specification until functional failure; record operating and destruct limits on sacrificial samples.
- **Acceptance.** Margins meet the project target; failure modes are analysed and fed back into the FMEDA and DFA.
- **References.** R4 clause 10.

## 6. Safety-oriented pass criteria

Apply to every CORE and ROB row used as functional-safety evidence, in addition to its ISO 16750-1 functional status or ISO 7637 / ISO 11452 performance class (CHG-04).

1. **No undetected excursion.** The output never leaves the load's valid operating range without the monitor detecting it.
2. **Timely reaction.** Every detected fault reaches the specified safe or degraded state within the FTTI (FDTI + FRTI ≤ FTTI).
3. **Defined reset.** RESET and power-good are asserted and held cleanly through slow ramps, interruptions and brown-outs, with no glitch or floating output at low supply voltage.
4. **No undefined end state.** After the stress, the supply is back in normal operation or held in the specified safe state.
5. **Availability budget.** Where loss of the function is itself hazardous (for example fail-operational steering or braking), spurious safe-state transitions stay within the specified limit.
6. **No latent damage to safety mechanisms.** Before and after each stress, re-measure OV/UV thresholds, deglitch and reaction times and self-test status, not only the output parameters.
7. **Safety-relevant monitoring.** During EMC and transient tests, monitor the safety-relevant signals and the safe-state reaction, not only the qualification class. Where feasible, repeat selected immunity tests on aged samples from the LIFE rows [R11].

## 7. ASIL-dependent evidence and process requirements

- **Hardware metrics.** When SPFM, LFM or PMHF are claimed (§3.4), every diagnostic-coverage value used must be backed by FUSA-004 or FUSA-006 evidence, or by a documented justification.
- **Sample size.** Statistical testing is graded o / o / + / ++ (§3.3). When statistical testing is selected as the verification method, determine and justify the sample size statistically. Otherwise derive sample count from the applicable qualification standard, verification strategy, safety requirement and project evidence needs; ASIL C/D does not by itself make every bench test a statistical test.
- **Test tools.** Automation that drives the instruments and decides pass/fail generates verification evidence. Classify it per ISO 26262-8 clause 11: the tool confidence level follows from tool impact and tool error detection [R5], [R13], and the qualification methods for higher confidence levels depend on the ASIL. Keep scripts under configuration management and store instrument calibration and measurement uncertainty with each evidence record.
- **Independence.** ISO 26262 independence levels (I0 to I3) govern confirmation measures (confirmation reviews, functional-safety audit and assessment) [R2 clause 6, Table 1], not who executes a bench test (CHG-19).
- **Verification, not validation.** The rows in this file are verification evidence (ISO 26262-5 clause 10; ISO 26262-4 clause 7). Safety validation is performed on the item integrated in the vehicle [R3 clause 8].

## 8. QM supplies and safety elements out of context

- **QM supply feeding ASIL elements.** Rows marked CF provide evidence that a QM supply cannot cause failures that violate the safety requirements of the ASIL elements it feeds: overvoltage, backfeed, loss of ground with I/O connected, cross-feeds between inputs, insulation failure [R6 clauses 6, 7].
- **Safety element out of context.** For a converter or PMIC developed as an SEooC, traceability starts from the assumed technical and hardware safety requirements instead of a safety goal [R7 clause 9]. Publish the assumptions of use the tests rely on, for example the allowed output-capacitance range for loop stability (PS-021), external divider tolerances (FUSA-002, FUSA-005), the monitor-threshold configuration and the required reaction to the error output, so the integrator can verify them.
- **Hardware not developed to ISO 26262.** For an off-the-shelf converter or PMIC, use the evaluation of hardware elements in ISO 26262-8 clause 13 [R5].

## 9. Interpretation for the safety case

For every executed row, the project test specification records the chain:

`Safety goal (or assumed safety requirement for an SEooC) → technical safety requirement → hardware safety requirement → ASIL → safety mechanism and its FMEDA/DFA line → test ID → stimulus or injected fault → expected safe or degraded state → FDTI + FRTI vs FTTI → §6 pass criteria → sample count and rationale → tool (TCL) and calibration record → evidence/report`

- **TRIG rows:** record the applicability decision and the analysis item behind it (HARA, FMEA/FMEDA or DFA line), whether or not the row is executed.
- **ROB rows:** record the mission-profile basis for applicability and a rationale for every omission.
- **QUAL and SUPP rows:** not functional-safety evidence, but keep the results; post-stress parametric data may be needed for §6 criterion 6.

That project-specific matrix, not this generic map, is the auditable functional-safety verification evidence.

## 10. Maintenance

- **Single source of truth.** Keep one data file (CSV or YAML) with ID, title, class, evidence method and the QM and A–D cells, and generate both this table and the ISO 26262 columns of the matrix from it (CHG-20).
- **Naming drift already present.** Titles differ between the matrix [R14] and the previous mapping [R15], for example PS-019 ("(bench screen)" only in the matrix), PS-021 ("(Bode plot)" only in the matrix), PS-022 ("PSRR" versus "Power-supply rejection"), AUTO-006 ("AC" versus "alternating voltage"), EMC-003 and EMC-004. This revision uses the matrix titles where the matrix was readable (§1).
- **Matrix synchronization.** The master matrix is synchronized with this revision: FUSA-002 to FUSA-011 and LIFE-005 are included with stimulus, equipment and N6700 mapping, and the four ISO 26262 columns use the §3 legend.
- **Automated checks.** In CI, fail the build if an ID is missing, duplicated or classified differently in the two files, or if the totals in §4.1 do not match the table.

## 11. References

- **[R1]** ISO 26262-1:2018, *Road vehicles — Functional safety — Part 1: Vocabulary*. Clause 1 (scope: electric shock and similar hazards excluded unless directly caused by malfunctioning behaviour of safety-related E/E systems; nominal performance not addressed) and definitions of FTTI, FDTI, FRTI, EOTTI and the multiple-point fault detection interval. <https://www.iso.org/standard/68383.html>
- **[R2]** ISO 26262-2:2018, *Part 2: Management of functional safety*. Clause 6 and Table 1 (confirmation measures and required independence levels).
- **[R3]** ISO 26262-4:2018, *Part 4: Product development at the system level*. Clause 6 (technical safety concept: safety mechanisms, safe states, FTTI, emergency operation), clause 7 (system and item integration and testing), clause 8 (safety validation). <https://www.iso.org/standard/68386.html>
- **[R4]** ISO 26262-5:2018, *Part 5: Product development at the hardware level*. Clause 6 (hardware safety requirements), clause 7 (hardware design, non-functional causes of failure, design verification), clause 8 (SPFM and LFM target tables), clause 9 (PMHF), clause 10 (hardware integration and verification method tables), Annex D (diagnostic coverage and power-supply failure modes). <https://www.iso.org/standard/68387.html>
- **[R5]** ISO 26262-8:2018, *Part 8: Supporting processes*. Clause 9 (verification), clause 11 (confidence in the use of software tools), clause 13 (evaluation of hardware elements). <https://www.iso.org/standard/68390.html>
- **[R6]** ISO 26262-9:2018, *Part 9: ASIL-oriented and safety-oriented analyses*. Clause 5 (requirements decomposition with respect to ASIL tailoring), clause 6 (criteria for coexistence of elements), clause 7 (analysis of dependent failures). <https://www.iso.org/standard/68391.html>
- **[R7]** ISO 26262-10:2018, *Part 10: Guidelines on ISO 26262*. Clause 9 (safety element out of context).
- **[R8]** ISO 26262-11:2018, *Part 11: Guidelines on application of ISO 26262 to semiconductors* (analogue, mixed-signal and power-management components).
- **[R9]** ISO/DIS 26262-5, *Road vehicles — Functional safety — Part 5: Product development at the hardware level* (Edition 3). Status page: DIS registered 2026-08-04, enquiry phase; will replace ISO 26262-5:2018. <https://www.iso.org/standard/90024.html>
- **[R10]** ISO 16750-1, *Road vehicles — Environmental conditions and testing for electrical and electronic equipment — Part 1: General* (functional status classification).
- **[R11]** J. J. Nelson, W. Taylor, R. Kado, "Impact on EMC for Electrical Powertrains with Respect to Functional Safety: ISO 26262", *In Compliance Magazine*. <https://incompliancemag.com/impact-on-emc-for-electrical-powertrains-with-respect-to-functional-safety-iso-26262/>
- **[R12]** "Applying ISO 26262 to Power Management in Advanced Driver Assistance Systems", *In Compliance Magazine*. <https://incompliancemag.com/applying-iso-26262-to-power-management-in-advanced-driver-assistance-systems/>
- **[R13]** Semiconductor Engineering, ISO 26262 knowledge center (location of the SPFM and LFM target tables; tool confidence level from tool impact and tool error detection). <https://semiengineering.com/knowledge_centers/automotive/automotive-standards/iso-26262/>
- **[R14]** [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md), this repository, as of 2026-09-20.
- **[R15]** Previous revision of this file (`iso26262-asil-test-mapping.md`), as of 2026-09-20.
- **[R16]** ISO 6469-3, *Electrically propelled road vehicles — Safety specifications — Part 3: Electrical safety*.
- **[R17]** ISO 16750-2:2023, *Road vehicles — Environmental conditions and testing for electrical and electronic equipment — Part 2: Electrical loads* (as cited in the matrix).
- **[R18]** ISO 21780, *Road vehicles — Supply voltage of 48 V — Electrical requirements and tests*.
