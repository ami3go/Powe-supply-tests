# ISO 26262 ASIL Mapping for Automotive Power-Supply Validation Tests

*Revision 2 (merged with review corrections) · 2026-09-20 · supersedes the version reviewed in [R15] · every change is listed with its rationale and references in [§2](#2-change-log)*

This file maps the 89 tests in [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md), plus 11 proposed additions, to their functional-safety role under ISO 26262.

> **Unchanged principle.** ISO 26262 does not define a fixed list of bench tests per ASIL. Verification obligations flow from the safety goals (or, for a safety element out of context, the assumed safety requirements), the technical and hardware safety requirements, the safety mechanisms and the safety analyses. Every safety requirement has to be verified, whatever its ASIL.
>
> **What changed.** The previous version showed the same entry in all four ASIL columns for every row. ISO 26262 does grade part of the verification by ASIL: through the hardware-integration method tables of ISO 26262-5 clause 10, and through hardware architectural metrics that exist only for ASIL B to D. This revision:
>
> 1. replaces Mandatory\* / Conditional\* / Not ASIL-specific with explicit classes (§3);
> 2. fills the ASIL columns with graded expectations (§3.3, §4);
> 3. fixes row-level inconsistencies (§2);
> 4. adds safety-oriented pass criteria for tests reused as safety evidence (§6);
> 5. splits the single FUSA-001 row into explicit safety-mechanism tests (§5).

**Contents:** [1 Review basis](#1-review-basis-and-limitations) · [2 Change log](#2-change-log) · [3 Classification](#3-classification-scheme) · [4 Mapping](#4-revised-asil-mapping) · [5 New rows](#5-new-rows-test-outlines) · [6 Pass criteria](#6-safety-oriented-pass-criteria) · [7 ASIL-dependent evidence](#7-asil-dependent-evidence-and-process-requirements) · [8 QM and SEooC](#8-qm-supplies-and-safety-elements-out-of-context) · [9 Safety case](#9-interpretation-for-the-safety-case) · [10 Maintenance](#10-maintenance) · [11 References](#11-references)

## 1. Review basis and limitations

- **Inputs reviewed:** the previous mapping [R15] and the test matrix [R14].
- **Matrix visibility:** Claude’s initial review had partial visibility after TH-001. Before this merge, rows TH-002 through FUSA-001 were checked against the complete current matrix and the four review corrections in §2.2 were applied.
- **Reading of the standard:** clause and table pointers refer to the 2018 edition. The ASIL grades of the ISO 26262-5 clause-10 methods (§3.3) and the content attributed to specific clauses are the reviewer's reading of the 2018 text. Confirm them against your licensed copy before quoting them in a safety case. No normative text is reproduced here.
- **Edition status:** the 2018 edition is the current published edition. The third-edition ISO/DIS 26262-5 was registered on 2026-08-04 and is in the enquiry phase [R9]. Re-check §3.3 when the third edition is published.
- **Titles:** row titles follow the matrix where it was readable, to reduce naming drift (§10).

## 2. Change log

| ID | Change | Rows | Main references |
|---|---|---|---|
| CHG-01 | Classification scheme replaced: CORE, CORE\*, ROB, TRIG, QUAL, SUPP | All | R15; R5 cl. 9; R4 cl. 10 |
| CHG-02 | ASIL columns show graded expectations instead of identical labels | All | R4 cl. 8, 9, 10; R12; R13 |
| CHG-03 | Standardized robustness stresses: Conditional\* → ROB | PS-018, PS-020, AUTO-001/002/004/005/006/012, TR-001–005, EMC-003/004/005/007/008, TH-005/006/007/009/010/011, ENV-001–005, 48V-001, HV-001 | R4 cl. 7, 10; R11 |
| CHG-04 | Safety-oriented pass criteria for CORE and ROB rows | CORE, ROB rows | R1; R10; R11 |
| CHG-05 | PS-019 Mandatory\* → SUPP | PS-019 | R14 |
| CHG-06 | AUTO-008 → CORE; AUTO-011 → CORE\* | AUTO-008, AUTO-011 | R14; R17 |
| CHG-07 | Transient response → CORE\* | PS-008, PS-009 | R4 cl. 10, Annex D; R12 |
| CHG-08 | Loop stability and derating remain analysis-driven at all ASILs; higher ASIL increases evidence rigor but does not automatically mandate these exact bench methods | PS-021, PS-029 | R4 cl. 7, 8, 9, 10, Annex D; R12 |
| CHG-09 | Backfeed and short to battery → CORE\* under stated conditions | PS-017, PS-030, AUTO-016 | R3 cl. 6; R6 cl. 7; R14 |
| CHG-10 | Equalizing currents → CORE\* for redundant feeds | AUTO-018 | R6 cl. 5, 7; R14 |
| CHG-11 | Quiescent current → QUAL | PS-006, AUTO-015 | R9; R15 |
| CHG-12 | Life and endurance rows graded; AUTO-017 aligned with LIFE-002 | AUTO-017, LIFE-001–004 | R4 cl. 10; R15 |
| CHG-13 | PS-031 sequencing aligned with PS-010 | PS-031 | R14 |
| CHG-14 | Restart behaviour must match the safe-state strategy | PS-013, TH-004 | R3 cl. 6; R14 |
| CHG-15 | HV and isolation rows re-evaluated; FUSA-011 added | HV-002, AUTO-019, AUTO-020, FUSA-011 | R1; R9; R6 cl. 7; R16; R18 |
| CHG-16 | FUSA-001 split into explicit safety-mechanism rows | FUSA-002 to FUSA-009, FUSA-011 | R1; R3 cl. 6; R4 cl. 8, 10, Annex D; R6 cl. 7; R12 |
| CHG-17 | New robustness rows | FUSA-010, LIFE-005 | R4 cl. 10 |
| CHG-18 | QM column and SEooC path | All; §8 | R6 cl. 6, 7; R7 cl. 9 |
| CHG-19 | Text corrections: independence, validation, edition, references | Preamble; §7; §11 | R2 cl. 6; R3 cl. 7, 8; R9; R15 |
| CHG-20 | Evidence process: sample size, tool confidence, single source of truth | §7; §10 | R4 cl. 10; R5 cl. 11; R13; R14; R15 |

### 2.1 Rationale per change

#### CHG-01 · Classification scheme replaced

**Change.** The labels Mandatory\*, Conditional\* and Not ASIL-specific are replaced by CORE, CORE\*, ROB, TRIG, QUAL and SUPP (§3.1).

**Why.** In the previous version a Mandatory\* test was required when it verifies an allocated safety requirement or safety mechanism, and a Conditional\* test became required when the analyses made its stress or failure mode safety-relevant [R15]. Both were therefore required exactly when they trace to a safety requirement: the labels encoded how *likely* that trace is, not an obligation. The asterisk caveat is easily lost when a table is skimmed, which invites the reading "run the 22 Mandatory tests and the supply is compliant". The label "Not ASIL-specific" described whether ISO 26262 drives a test at all, not whether the test depends on the ASIL. The new classes name the reason a test is needed: it verifies a safety mechanism or safe state (CORE), it supplies robustness evidence that ISO 26262-5 expects (ROB), it is needed only when an analysis says so (TRIG), or ISO 26262 does not drive it (QUAL, SUPP).

**References.** R15 (previous class definitions); R5 clause 9 (verification); R4 clause 10 (hardware integration and verification).

#### CHG-02 · Graded ASIL columns

**Change.** The A–D columns now carry REQ for required verification, the ISO 26262-5 clause-10 grade (++, +, o) of the row's evidence method, or n/a where the underlying requirement does not exist at that ASIL (legend in §3.2).

**Why.** All 89 rows had identical A–D entries [R15], so the columns carried no ASIL information. ISO 26262 grades verification by ASIL in two places that matter for a power supply:

- *Hardware architectural metrics.* SPFM and LFM targets exist only for ASIL B, C and D (SPFM ≥ 90 / 97 / 99 %, LFM ≥ 60 / 80 / 90 %), with PMHF targets alongside [R12], [R13]. At ASIL B they are recommendations, and nothing applies at ASIL A [R4 clauses 8, 9]. Evidence that substantiates diagnostic-coverage claims (fault injection) and latent-fault detection (self-tests) is therefore largely a B–D obligation.
- *Clause-10 method tables.* Fault injection testing, accelerated life testing, statistical testing, expanded functional testing and worst-case testing carry different recommendation levels at different ASILs (§3.3).

**References.** R4 clauses 8, 9, 10; R12 (metric targets); R13 (location of the SPFM and LFM target tables).

#### CHG-03 · Standardized robustness stresses become ROB

**Change.** Standardized environmental, mechanical, chemical, EMC/ESD and supply-voltage stresses move from Conditional\* to ROB: expected at every ASIL **when applicable to the defined operating environment, interfaces, mission profile or vehicle requirement**, with a documented rationale for any omission. The ASIL cells use a trailing `*` to make this applicability condition explicit.

**Why.** ISO 26262-5 clause 10 specifies hardware integration tests of robustness under external stresses. EMC and ESD testing is one of the ten methods listed there and is highly recommended at every ASIL [R11]. In the same clause, environmental testing with basic functional verification, mechanical testing, mechanical endurance testing and chemical testing are also highly recommended at every ASIL, and so is electrical testing of the safety mechanisms over the specified static and dynamic supply-voltage range [R4]. Clause 7 additionally requires non-functional causes of failure, such as temperature, vibration, water, dust, EMI and crosstalk, to be considered in the hardware design [R4]. A highly recommended method is applied, or its omission is justified; the previous Conditional\* label reversed that burden by requiring an analysis trigger first. Applicability still comes from the mission profile (mounting location, supply-voltage code, 48 V or voltage-class-B system), not from the safety analysis. Existing ISO 16750, ISO 7637, ISO 11452 and ISO 10605 campaigns can serve as the evidence when the CHG-04 criteria are applied.

**References.** R4 clauses 7 and 10; R11; R17.

#### CHG-04 · Safety-oriented pass criteria

**Change.** Every CORE and ROB row used as functional-safety evidence gets the pass criteria of §6 in addition to its qualification criterion.

**Why.** ISO 16750-1 functional status classes describe availability, not safety: status B lets functions leave their tolerance during exposure and status C lets them stop, provided they recover automatically afterwards [R10]. For a safety-related rail, an excursion that is neither prevented nor detected and reacted to within the fault tolerant time interval can violate a safety goal even though the qualification test passes [R1]. For functional safety, R11 recommends monitoring the safety-critical signals and the safe-state reaction during immunity testing, and adding immunity tests on aged samples.

**References.** R10; R1 (FTTI, FDTI, FRTI); R11.

#### CHG-05 · PS-019 becomes SUPP

**Change.** PS-019 moves from Mandatory\* to SUPP.

**Why.** The matrix defines PS-019 as an early bench screen of intermittent connector or battery contact, run before the formal AUTO-010, AUTO-013 and AUTO-014 tests [R14]. A development screen with a bench fixture is not the formal verification evidence; the formal rows stay CORE.

**References.** R14 (PS-019, AUTO-010, AUTO-013, AUTO-014).

#### CHG-06 · AUTO-008 and AUTO-011

**Change.** AUTO-008 moves from Conditional\* to CORE. AUTO-011 moves from Conditional\* to CORE\*: required for vehicles with start-stop or with functions that restart the engine while moving; otherwise ROB.

**Why.** AUTO-008 (slow decrease, fast increase) exercises the same reset and brown-out mechanisms as AUTO-007 and AUTO-009, which were already Mandatory\* [R14]: incomplete power-on reset, a stuck supply state machine, non-volatile memory corruption. For AUTO-011, PS-026 (Mandatory\*) explicitly covers cranking and cites ISO 16750-2 §4.6.3, the same clause as AUTO-011 [R14]; rating the realistic crank profile lower than the generic dropout test was inconsistent. With start-stop, and especially with coasting functions that restart the engine while rolling, the crank dip can coincide with active steering or braking.

**References.** R14 (PS-026, AUTO-007, AUTO-008, AUTO-009, AUTO-011); R17.

#### CHG-07 · PS-008 and PS-009 become CORE\*

**Change.** Load- and line-transient response become required for every rail that feeds a safety-related load.

**Why.** Output-voltage monitors use deglitch or filter times to avoid false trips, so excursions shorter than the filter are undetectable by design. The safety argument, and the diagnostic coverage claimed for voltage monitoring (which depends on the quality of the monitor [R12]), rests on the premise that such short excursions stay inside the load's valid operating range. Only transient tests demonstrate that premise. Power spikes and oscillation are among the power-supply failure modes that ISO 26262-5 Annex D expects a high-coverage monitor to address [R4], and they are the output-rail behaviours safety teams focus on when assessing power devices [R12].

**References.** R4 clause 10 (electrical testing over the dynamic range), Annex D; R12.

#### CHG-08 · PS-021 and PS-029 remain analysis-driven

**Change.** PS-021 (control-loop stability) and PS-029 (component stress and derating) remain TRIG at ASIL A through D. A higher ASIL raises the required confidence in the hardware design and in the architectural-metric evidence, but ISO 26262 does not state that a Bode-plot measurement or a physical component-stress measurement becomes automatically mandatory at ASIL C or D.

**Why, PS-021 (control-loop stability).** Oscillation is a relevant power-supply failure mode [R4 Annex D], and a marginal loop can invalidate a safety argument. However, the project may verify the corresponding hardware safety requirement using analysis, simulation, measured loop gain, transient testing, design margin, or a justified combination. Make the Bode-plot test REQ when the hardware safety requirement, FMEDA, dependent-failure analysis or claimed design margin requires physical loop verification.

**Why, PS-029 (component stress and derating).** FMEDA and PMHF calculations depend on stress and mission-profile assumptions, so those assumptions need verification. That verification can use calculation, simulation, component qualification data and/or measurement. Worst-case testing has its own ASIL-dependent recommendation grade (§3.3); where worst-case physical testing is selected at ASIL D, record the WC+ evidence, but do not turn PS-029 into an automatic ASIL-C/D bench requirement.

**References.** R4 clauses 7, 8, 9, 10 and Annex D; R12.

#### CHG-09 · Backfeed and short to battery

**Change.** PS-017 and AUTO-016 become CORE\* when the safe state is "de-energized". PS-030 becomes CORE\* for outputs that leave the module.

**Why.** When the technical safety concept defines the safe state as removal of power, backfeed through outputs or I/O can keep the switched-off domain partially powered, so the safe state is never reached or maintained [R3 clause 6]. Outputs that leave the module, such as sensor supplies, can be shorted to battery during assembly or service [R14]; the resulting overvoltage can propagate into the ECU's ADC or microcontroller domain, a cascading failure that dependent-failure analysis has to address [R6 clause 7].

**References.** R3 clause 6; R6 clause 7; R14 (PS-017, PS-030, AUTO-016).

#### CHG-10 · AUTO-018 for redundant feeds

**Change.** AUTO-018 becomes CORE\* when two supply inputs form part of an ASIL decomposition or a fail-operational architecture.

**Why.** The matrix applies AUTO-018 to devices with two or more supply inputs, including redundant feeds [R14]. ASIL decomposition requires sufficient independence between the redundant elements, shown through dependent-failure analysis [R6 clauses 5, 7]. Equalizing currents between the inputs, or one feed powering the other, directly undermine that independence.

**References.** R6 clauses 5 and 7; R14 (AUTO-018).

#### CHG-11 · Quiescent current becomes QUAL

**Change.** PS-006 and AUTO-015 move from Conditional\* to QUAL. They return to TRIG only if a safety function of the parked vehicle depends on the battery's state of charge.

**Why.** Closed-circuit current is an energy-budget requirement that rarely traces to a safety goal, and ISO 26262 does not address the nominal performance of E/E systems [R9]. Keeping such rows in the analysis-triggered class diluted it: 57 of the 89 rows were Conditional\* [R15].

**References.** R9 (scope statement, unchanged in intent from the 2018 edition); R15.

#### CHG-12 · Life and endurance rows graded

**Change.** LIFE-001, LIFE-002, LIFE-004 and AUTO-017 carry the accelerated-life grade (+ / + / ++ / ++). LIFE-003 carries the worst-case-testing grade (o / o / o / +). AUTO-017 moves from Not ASIL-specific to ROB, matching LIFE-002.

**Why.** AUTO-017 (repetitive on/off) and LIFE-002 (power/thermal cycling) stress the same wear-out mechanisms but sat in different classes [R15]. ISO 26262-5 clause 10 grades accelerated life testing by ASIL and rates mechanical endurance testing highly recommended at every ASIL (§3.3). If AUTO-017 is used to qualify relays or contactors, apply the mechanical-endurance grade instead. LIFE-003 was graded from its title only (§1); if it is used as life evidence rather than as a worst-case check, apply the accelerated-life grade.

**References.** R4 clause 10; R15.

#### CHG-13 · PS-031 sequencing aligned with PS-010

**Change.** The sequencing part of PS-031 becomes CORE\* for multi-rail supplies feeding a microcontroller or SoC; cross-regulation stays TRIG.

**Why.** PS-010 (Mandatory\*) already verifies sequencing [R14]. PS-031 extends the same check to input-voltage and temperature corners for multi-output supplies, so rating it lower was inconsistent. Out-of-order rails can leave a processor in an undefined state or trigger latch-up.

**References.** R14 (PS-010, PS-031).

#### CHG-14 · Restart behaviour must match the safe-state strategy

**Change.** PS-013's acceptance criterion adds: *restart behaviour matches the safe-state strategy of the technical safety concept (latched, counter-limited retry or automatic retry)*. The same applies to thermal restart in TH-004. New row FUSA-007 verifies the safe-state path.

**Why.** The technical safety concept defines the safe state and how it is reached and maintained [R3 clause 6]. A converter that hiccup-restarts automatically after an overvoltage or overcurrent fault can undo a safe state the concept requires to be latched. PS-013 currently checks only for latch-up and uncontrolled repeated stress [R14].

**References.** R3 clause 6; R14 (PS-013).

#### CHG-15 · HV and isolation rows

**Change.** HV-002 moves from Not ASIL-specific to TRIG. AUTO-019 and AUTO-020 become TRIG\* for galvanically isolated HV-to-LV converters (QUAL otherwise). New row FUSA-011 covers 12 V-network overvoltage caused by 48 V-to-12 V or HV-to-LV converter faults.

**Why.** ISO 26262 does not address electric-shock hazards *unless they are directly caused by malfunctioning behaviour of safety-related E/E systems* [R9], [R1]. Active discharge, the high-voltage interlock loop, contactor opening and insulation monitoring are E/E functions whose malfunction can directly cause such hazards, and OEM hazard analyses commonly assign them ASILs; the protection requirements themselves remain in ISO 6469-3 [R16]. Separately, an insulation breakdown in an isolated HV-to-LV converter, or a shorted high-side switch in a 48 V-to-12 V converter, can overvoltage the whole 12 V network: a common-cause failure for every ECU on it, which dependent-failure analysis has to cover [R6 clause 7].

**References.** R1 and R9 (scope); R6 clause 7; R16; R18.

#### CHG-16 · FUSA-001 split into explicit rows

**Change.** FUSA-001 remains as the umbrella row; FUSA-002 to FUSA-009 and FUSA-011 are added (outlines in §5).

**Why.** One row titled "functional-safety mechanisms and fault reaction" hides the evidence an assessor looks for:

- threshold coordination between regulation band, monitor window and load operating range, since the coverage of voltage monitoring depends on the quality of the monitor [R12] (FUSA-002);
- fault reaction time within the fault tolerant time interval, FDTI + FRTI ≤ FTTI [R1], [R3 clause 6] (FUSA-003);
- latent-fault detection of the monitors, which drives the LFM at ASIL B–D [R4 clause 8]; a comparator stuck in its no-fault state misses real faults, which is why power-management ICs run an analog BIST at start-up [R12] (FUSA-004);
- independence of regulation and monitoring; a shared bandgap, or a feedback node shared by regulator and monitor, lets one fault shift both together [R12], [R6 clause 7] (FUSA-005);
- physical fault injection that substantiates diagnostic-coverage claims [R4 clause 10, Annex D] (FUSA-006);
- the safe-state path and its maintenance [R3 clause 6] (FUSA-007);
- digital mechanisms of PMICs and system-basis chips: CRC on configuration memory and serial communication, clock monitoring, logic BIST [R12] (FUSA-008);
- redundant-supply switchover and emergency operation within the emergency operation tolerance time interval (EOTTI) [R1], [R3 clause 6], [R6 clauses 5, 7] (FUSA-009);
- network-level overvoltage from 48 V or HV converters, see CHG-15 (FUSA-011).

**References.** As listed per item.

#### CHG-17 · New robustness rows

**Change.** FUSA-010 (expanded functional testing) and LIFE-005 (over-limit testing) are added.

**Why.** ISO 26262-5 clause 10 lists expanded functional testing (behaviour under rare or out-of-specification inputs, graded o / + / + / ++) and over-limit testing (stress increased beyond the specification to establish the robustness margin, recommended at every ASIL) (§3.3). The matrix had no row for either.

**References.** R4 clause 10.

#### CHG-18 · QM column and SEooC path

**Change.** A QM column marks rows (CF) whose evidence supports the cascading-failure and coexistence argument when a QM supply feeds ASIL elements. §8 adds a traceability path for a supply developed as a safety element out of context (SEooC).

**Why.** An element with a lower integrity level, including QM, that coexists with ASIL elements must not cause failures that violate their safety requirements; this is argued with coexistence criteria and dependent-failure analysis [R6 clauses 6, 7]. Many converters and power-management ICs are developed as SEooC against assumed safety requirements, so their traceability starts from those assumptions and the integrator verifies the assumptions of use [R7 clause 9]. The previous traceability chain started only from the safety goal [R15].

**References.** R6 clauses 6 and 7; R7 clause 9; R15.

#### CHG-19 · Text corrections

- *Independence.* The previous preamble listed independence among the things a higher ASIL changes for tests [R15]. ISO 26262 independence levels (I0 to I3) apply to confirmation measures, meaning confirmation reviews, functional-safety audit and functional-safety assessment [R2 clause 6, Table 1], not to who executes a bench test. Corrected in §7.
- *"Often identical".* The previous ASIL columns were identical in every row, not often [R15]; superseded by CHG-02.
- *Verification versus validation.* The bench tests in this matrix are verification evidence (ISO 26262-5 clause 10; ISO 26262-4 clause 7). Safety validation is performed on the item integrated in the vehicle [R3 clause 8]. Clarified in §7.
- *Edition.* Status updated with the ISO/DIS 26262-5 registration date [R9].
- *References.* Added Parts 1, 2, 10 and 11, Part 5 Annex D, Part 8 clauses 11 and 13, ISO 16750-1, ISO 6469-3 and ISO 21780 (§11).

**References.** R2; R3; R9; R15.

#### CHG-20 · Evidence process

- *Sample size.* Statistical testing is graded o / o / + / ++ (§3.3). **When statistical testing is selected as the verification method**, determine and justify the sample size statistically. Otherwise derive sample count from the applicable qualification standard, verification strategy, safety requirement and project evidence needs; ASIL C/D does not by itself make every bench test a statistical test.
- *Tool confidence.* Scripts that drive the instruments and decide pass/fail produce verification evidence. ISO 26262-8 clause 11 requires such tools to be classified; the tool confidence level follows from tool impact and tool error detection [R5], [R13], and the qualification methods required for higher confidence levels depend on the ASIL.
- *Single source of truth.* The ASIL classification lives in both this file and the matrix [R14], [R15], and titles have already drifted (§10). Generate both from one data file.

**References.** R4 clause 10; R5 clause 11; R13; R14; R15.

### 2.2 Review corrections applied before merge

Before merging Revision 2 into `main`, four points were tightened:

1. PS-021 and PS-029 remain analysis-driven at every ASIL; higher ASIL increases evidence rigor but does not automatically mandate these exact physical bench methods.
2. ROB method grades carry a trailing `*` to show that the specific environmental/electrical stress is applicable only when the defined operating environment, interface, mission profile or vehicle requirement calls for it.
3. FUSA-004 is conditional at ASIL A rather than `n/a`; absence of an LFM metric does not prevent an ASIL-A safety requirement from allocating a latent-fault/self-test mechanism.
4. FUSA-006 is conditional on diagnostic-coverage claims needing experimental substantiation, and statistical sample-size justification is required only when statistical testing is actually selected as the method.

## 3. Classification scheme

### 3.1 Classes

| Class | Meaning | When it applies |
|---|---|---|
| **CORE** | Verifies a safety mechanism, safe state, reset/restart behaviour or safety-relevant electrical behaviour of the supply | Always, when the supply or rail is safety-related and the behaviour is part of the safety concept |
| **CORE\*** | As CORE, under the condition stated in the row | Condition true → required; otherwise as stated in the row note (default TRIG) |
| **ROB** | Standardized robustness stress expected by ISO 26262-5 clause 10 | When the defined operating environment, interfaces, mission profile or vehicle requirement makes it applicable; ASIL cells carry a trailing `*`; record a rationale for any omission; apply §6 |
| **TRIG** | Needed only when the HARA, FMEA/FMEDA, DFA or the architecture makes the stress or failure mode safety-relevant | Record the applicability decision and the analysis item behind it, whether or not the test is run |
| **QUAL** | Qualification or performance test not driven by ISO 26262 | Still required where ISO 16750, LV 124, CISPR 25 or the customer specification requires it |
| **SUPP** | Development screen or pre-compliance check; not formal evidence | Formal evidence comes from the row named in the note |

### 3.2 Cell legend (QM and ASIL A–D columns)

| Entry | Meaning |
|---|---|
| REQ | Required: execute and trace to the safety requirement or safety mechanism |
| ++ | ISO 26262-5 clause-10 method highly recommended at this ASIL: apply, or record a rationale for omission |
| + | Recommended at this ASIL |
| o | No recommendation for or against at this ASIL |
| FI+, FI++, WC+ | Fault injection testing (FI) or worst-case testing (WC) called out with its grade at this ASIL |
| T | Only if triggered by analysis; once triggered, treat as REQ |
| n/a | The underlying requirement does not exist at this ASIL |
| — | Not driven by ISO 26262 |
| trailing \* | Applies only under the condition in the row note |
| CF | QM column only: evidence supports the cascading-failure / coexistence argument when a QM supply feeds ASIL elements |

Where the class and the ASIL cells differ (for example a CORE row with + at ASIL A), the cells govern.

### 3.3 ISO 26262-5 clause-10 evidence methods and their ASIL grades

Reviewer's reading of ISO 26262-5:2018 clause 10; confirm against your licensed copy before citing.

| Code | Method | A | B | C | D |
|---|---|---|---|---|---|
| FT | Functional testing of safety mechanisms | ++ | ++ | ++ | ++ |
| FI | Fault injection testing | + | + | ++ | ++ |
| ET | Electrical testing over the specified static and dynamic voltage range | ++ | ++ | ++ | ++ |
| ENV | Environmental testing with basic functional verification | ++ | ++ | ++ | ++ |
| EXP | Expanded functional testing (rare or out-of-specification inputs) | o | + | + | ++ |
| STAT | Statistical testing (sample-based) | o | o | + | ++ |
| WC | Worst-case testing | o | o | o | + |
| OL | Over-limit testing | + | + | + | + |
| MECH | Mechanical testing | ++ | ++ | ++ | ++ |
| ALT | Accelerated life test | + | + | ++ | ++ |
| MEND | Mechanical endurance test | ++ | ++ | ++ | ++ |
| EMC | EMC and ESD testing | ++ | ++ | ++ | ++ |
| CHEM | Chemical testing | ++ | ++ | ++ | ++ |

In the standard, ENV, EXP and STAT are alternative entries to be combined as appropriate for the ASIL. Two further evidence types used in §4 are not clause-10 methods: **DV** is hardware design verification (ISO 26262-5 clause 7) and **DFA** is dependent-failure analysis evidence (ISO 26262-9 clause 7).

### 3.4 Hardware architectural metrics

These targets drive stronger evidence expectations at higher ASILs, especially for FUSA-004 and FUSA-006. PS-021 and PS-029 remain analysis-driven at all ASILs; architectural-metric targets do not automatically mandate those exact bench methods.

| Metric | ASIL A | ASIL B | ASIL C | ASIL D |
|---|---|---|---|---|
| Single-point fault metric (SPFM) | n/a | ≥ 90 % (recommendation) | ≥ 97 % | ≥ 99 % |
| Latent-fault metric (LFM) | n/a | ≥ 60 % (recommendation) | ≥ 80 % | ≥ 90 % |
| Probabilistic metric for random hardware failures (PMHF) | n/a | < 100 FIT (recommendation) | < 100 FIT | < 10 FIT |

Sources: R4 clause 8 (SPFM and LFM target tables) and clause 9 (PMHF); summarized in R12 and R13.

## 4. Revised ASIL mapping

Column key: **Was** = previous class (M\* Mandatory\*, C\* Conditional\*, NAS Not ASIL-specific, new = proposed row). **Evidence** = ISO 26262-5 evidence method (§3.3). **QM** = relevance when a QM supply feeds ASIL elements (§8). Cell entries follow §3.2.

| ID | Test | Was | Class | Evidence | QM | A | B | C | D | Change · note |
|---|---|---|---|---|---|---|---|---|---|---|
| PS-001 | Input operating range | M\* | CORE | ET, FT | — | REQ | REQ | REQ | REQ | CHG-01 |
| PS-002 | Output voltage accuracy | M\* | CORE | ET | — | REQ | REQ | REQ | REQ | CHG-01 · extend to the worst-case band; feeds FUSA-002 |
| PS-003 | Line regulation | C\* | TRIG | ET | — | T | T | T | T | CHG-16 · worst-case result is an input to FUSA-002 |
| PS-004 | Load regulation | C\* | TRIG | ET | — | T | T | T | T | CHG-16 · worst-case result is an input to FUSA-002 |
| PS-005 | Efficiency map | NAS | QUAL | — | — | — | — | — | — | CHG-01 · thermal consequences covered by TH-001 and TH-004 |
| PS-006 | No-load / standby consumption | C\* | QUAL | — | — | — | — | — | — | CHG-11 · TRIG if a parked-vehicle safety function depends on battery charge |
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
| TRIG* | 2 |
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

- **Single source of truth.** [`iso26262-test-classification.csv`](iso26262-test-classification.csv) is the machine-readable classification source with ID, title, class, evidence method, QM relevance and A–D cells. Keep it synchronized with this rationale document and the master matrix (CHG-20).
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
