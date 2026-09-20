
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