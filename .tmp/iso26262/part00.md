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
- **Matrix visibility:** during the review the matrix was readable only up to TH-001. Rows TH-002 to FUSA-001 were classified from their titles and previous classification; confirm them against their full descriptions.
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