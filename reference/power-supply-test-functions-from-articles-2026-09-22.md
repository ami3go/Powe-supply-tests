# Power-Supply Test Functions Synthesized from the Multilingual Article Corpus

_Last updated: 2026-09-22_

## Purpose

This document reorganizes the material in [`multilingual-power-supply-testing-articles-2026-09-21.md`](multilingual-power-supply-testing-articles-2026-09-21.md) by **tested function** rather than by publisher or language. The intent is to expose the recurring test primitives described across the 131 collected articles/resources and make them easier to compare with the project test matrices.

## Review method and limitations

All 131 indexed URLs were individually attempted during this review. Where the public page was retrievable, its technical content was reviewed. Where a page/PDF was blocked, moved, cache-inaccessible, login-gated or otherwise not retrievable, classification used the retained title/topic tags from the source index and, when the item was a localized version of the same publisher material, the accessible equivalent-language article. Therefore this is a **corpus synthesis**, not a claim that every byte of every linked page was accessible in the review session.

The table normalizes repeated test descriptions into common engineering functions. Localized translations and articles that repeat the same method are intentionally not converted into duplicate test rows.

### Article-ID convention

`A001`…`A131` correspond to entries 1…131 in the multilingual article index. The `Representative corpus IDs` column is intentionally representative rather than exhaustive; the complete source set remains in the article index.

### Matrix mapping convention

- `PS-*`, `AUTO-*`, `TR-*`, `EMC-*`, `TH-*`, `LIFE-*`, `HV-*`, `CHG-*`, etc. refer to inherited automotive rows.
- `GEN-*`, `SAF-*`, `BAT-*`, `TEL-*`, `RAIL-*`, etc. refer to explicit rows in [`../Test-matrix/global-power-supply-test-matrix.md`](../Test-matrix/global-power-supply-test-matrix.md).
- **Covered** means the test intent already exists in the global matrix, even if the article uses a different instrument or procedure.
- **Partial** means the matrix contains the broad intent but the corpus suggests a useful dedicated sub-test or metric.

---

## Function-oriented master table

| Functional group | Test function | What is being verified | Typical stimulus / method | Primary measurements | Representative corpus IDs | Current matrix mapping | Coverage |
|---|---|---|---|---|---|---|---|
| Input/source interface | Input operating-voltage range | Regulation and correct operation across declared source range | Sweep Vin from below minimum through nominal to maximum at several loads/temperatures | Vin, Iin, Vout, Iout, state/faults | A002, A003, A021, A039, A045, A065, A080, A092, A098, A120 | GEN-001; PS-001 | Covered |
| Input/source interface | AC input frequency range | Operation over utility/generator frequency variation | Sweep frequency at min/nom/max AC voltage and load | Vout, input current, PF, faults | A009, A021, A051, A089 | GEN-004; CHG-001 | Covered |
| Input/source interface | Line regulation | Sensitivity of output to source-voltage change | Sweep input voltage with fixed load | ΔVout/ΔVin, line-regulation % | A002, A022, A039, A045, A065, A099 | GEN-007; PS-003 | Covered |
| Input/source interface | Brownout / UVLO boundary | Controlled behavior as input falls below normal range | Slow and stepped reduction around UVLO/reset region | trip/release thresholds, hysteresis, restart | A006, A021, A051, A065 | GEN-002; PS-026; AUTO-007/009 | Covered |
| Input/source interface | Line transient response | Output immunity to rapid source change | Fast Vin steps/ramps; line transient capture | output excursion, recovery time, ringing, state | A001, A006, A022, A095 | GEN-010; PS-009 | Covered |
| Input/source interface | Short interruption / hold-up | Stored-energy ride-through and reset threshold | Remove input for controlled intervals | hold-up time, output droop, reset/recovery | A006, A022, A051, A057, A063 | GEN-003; AUTO-010 | Covered |
| Input/source interface | Input inrush current | Rectifier, fuse, connector and input-capacitor stress | Energize at worst line phase/voltage and temperature | peak current, charge, I²t, settling | A001, A006, A009, A051, A057 | GEN-006; PS-012; CHG-005 | Covered |
| Input/source interface | Input current waveform / crest factor | Shape and peakiness of AC/DC source current | Capture input current over cycle / switching period | RMS, peak, crest factor, waveform | A001, A008, A009, A089 | GEN-006/020 | Partial |
| Static output performance | Output-voltage accuracy | Absolute DC output compliance | Measure at nominal and corner conditions | mean/min/max Vout, error % | A002, A003, A039, A045, A058, A065, A099, A120 | GEN-007; PS-002 | Covered |
| Static output performance | Load regulation | Output sensitivity to load current | Sweep load from minimum to rated/full load | Vout vs Iout, regulation % | A002, A022, A039, A058, A065, A099, A124 | GEN-007; PS-004 | Covered |
| Static output performance | Cross-regulation / cross-load | Interaction between outputs of multi-rail supplies | Sweep load combinations on each rail | each rail voltage/current, cross-reg error | A057, A073, A090 | PS-031; GEN-007 | Covered |
| Static output performance | No-load / standby consumption | Power/current drawn with little or no output load | No-load, sleep, disabled or standby states | input current, input power, wake events | A046, A057, A073, A076 | PS-006; AUTO-015; SYS-003 | Covered |
| Static output performance | Maximum continuous output capability | Ability to sustain rated load without droop/overtemperature | Increase load to rating at source/temp corners | Vout, Iout, temperature, protection margin | A039, A041, A057, A063, A073, A100 | GEN-007/013; TH-001 | Covered |
| Static output performance | Output current accuracy / current regulation | Accuracy of current-regulated supplies/chargers | Program or load across current range | Iout error, ripple, compliance voltage | A039, A045, A051, A127 | GEN-007; BAT-001; CHG-010 | Partial |
| Static output performance | DC output droop / remote-sense behavior | Distribution/harness drop compensation | Vary load and wiring drop, enable/disable remote sense | local/remote Vout, sense error, stability | A002, A039, A041 | GEN-007; PS-023 | Partial |
| Efficiency and energy | Conversion efficiency map | Energy conversion performance over operating envelope | Vin × load × temperature sweep | Pin, Pout, efficiency, loss | A001, A002, A009, A021, A025, A044, A046, A059, A074-A076, A082, A089, A094, A098, A100, A113, A116, A119, A125-A131 | GEN-020; PS-005 | Covered |
| Efficiency and energy | No-load efficiency / standby power | Light-load energy performance | No-load and low-load points | Pin, Pout, standby W | A010, A046, A059, A076 | PS-006; GEN-020 | Covered |
| Efficiency and energy | Loss breakdown | Where converter losses occur | Measure input/output power plus device waveforms/temperatures | switching, conduction, magnetic/capacitor loss estimates | A001, A011, A048, A115, A122 | GEN-020; PS-029 | Partial |
| Efficiency and energy | Power factor | Real/apparent power utilization on AC input | Measure AC input over load/line points | W, VA, var, PF | A001, A009, A047, A051, A089, A130 | CHG-006; EMC-010 | Covered for charging; Partial generically |
| Efficiency and energy | Harmonic current | Distortion of AC input current | FFT/harmonic analysis under prescribed load | individual harmonics, THD | A001, A009, A051, A130 | EMC-010; CHG-007 | Covered |
| Dynamic response / timing | Load transient response | Control response to rapid output-demand change | Electronic-load steps at defined amplitude/slew | overshoot, undershoot, settling, ringing | A001, A002, A006, A015, A021-A024, A033, A038, A040-A043, A061, A064-A067, A086, A090, A094-A097 | GEN-009; PS-008 | Covered |
| Dynamic response / timing | High-slew-rate load transient | Behavior under very fast modern CPU/server loads | Fast pulsed/user-defined load waveform | droop, recovery, slew tracking, protection interaction | A038, A041, A049, A061, A090, A091 | GEN-009; PS-008 | Covered |
| Dynamic response / timing | Startup / turn-on | Soft-start, overshoot and start reliability | Power-on at source/load/temp corners | rise time, overshoot, inrush, state | A001, A006, A022, A057, A063 | GEN-011; PS-010 | Covered |
| Dynamic response / timing | Shutdown / turn-off | Controlled output decay and reverse-current behavior | Disable/remove input at several loads | fall time, undershoot, reverse current | A001, A006, A057 | GEN-012; PS-011 | Covered |
| Dynamic response / timing | Rail sequencing / PGOOD timing | Correct order and timing of multiple rails | Capture all rails on power-up/down | rail timing, PGOOD, monotonicity | A022, A057, A063, A073 | GEN-011; PS-031 | Covered |
| Dynamic response / timing | Recovery after fault | Deterministic return after overload/short/brownout | Apply/clear fault repeatedly | restart time, overshoot, latch/hiccup state | A041, A051, A057, A062, A129 | PS-013; GEN-013/014 | Covered |
| Dynamic response / timing | Long-record transient capture | Rare/intermittent disturbances and burst behavior | Triggered long-memory acquisition | event timing, waveform detail, repetition | A022, A063 | Supporting method | Method, not separate product test |
| Ripple / spectral quality | Output ripple (PARD) | Periodic deviation on DC output | AC-coupled/high-offset time-domain capture | pk-pk/RMS ripple | A001, A002, A006, A014-A015, A019-A020, A022, A028, A060, A067, A090, A094-A095, A108, A123-A124, A129 | GEN-008; PS-007 | Covered |
| Ripple / spectral quality | Broadband output noise | Random/non-periodic rail noise | Wide-band low-noise probing | RMS noise, noise floor, spectral density | A001, A006, A014-A015, A022, A060, A067 | GEN-008; PS-007 | Covered |
| Ripple / spectral quality | Spectral ripple / FFT | Harmonic content of ripple/noise | FFT of output rail | dominant frequencies/harmonics | A001, A020, A022, A060 | GEN-008; PS-007/025 | Covered |
| Ripple / spectral quality | Switching-node waveform quality | Ringing, overshoot and switching behavior | High-bandwidth differential probing of switch node | Vds/Vce, ringing, dv/dt, frequency | A001, A014, A011, A115 | PS-025/029 | Covered through inherited PS rows |
| Ripple / spectral quality | Capacitor ripple current | Thermal/electrical stress in capacitors | Current probe/shunt + FFT/RMS analysis | RMS ripple current, spectrum, temperature | A020, A048 | PS-029; LIFE-004 | Covered |
| Control-loop stability | Loop gain / Bode response | Closed-loop transfer behavior | Small-signal injection and swept FRA/Bode measurement | gain/phase vs frequency | A001, A016-A018, A026-A037, A064, A066, A068-A072, A077-A079, A081, A086, A088, A093, A096, A101-A107, A109-A112, A117-A118 | PS-021 | Covered |
| Control-loop stability | Phase margin | Stability robustness to tolerances/corners | Derive from Bode crossover | degrees phase margin | Same LOOP corpus as above | PS-021/032 | Covered |
| Control-loop stability | Gain margin | Distance to instability at phase crossover | Bode/FRA analysis | gain margin dB | Same LOOP corpus as above | PS-021/032 | Covered |
| Control-loop stability | Crossover frequency / loop bandwidth | Control-loop speed | Bode response | 0 dB crossover frequency | A016-A018, A068-A072, A101-A112 | PS-021 | Covered |
| Control-loop stability | Output impedance | Dynamic stiffness and hidden resonances | Small-signal current injection / VNA-FRA | Zout magnitude/phase | A027-A028, A031, A034 | PS-022/032 | Covered |
| Control-loop stability | Input impedance / filter interaction | Risk of source/filter-converter oscillation | Impedance measurement / source injection | Zin/Zsource, minor-loop gain | A028, A031-A032, A035 | PS-023/032 | Covered |
| Control-loop stability | PSRR / audiosusceptibility | Rejection of input ripple/disturbance | Inject swept AC at input and measure output | PSRR/audio susceptibility vs frequency | A001, A032, A081 | PS-022 | Covered |
| Control-loop stability | Non-invasive stability estimate | Stability when control-loop injection point is inaccessible | Output-impedance based method | derived margin / resonance Q | A027-A028, A034 | PS-032 | Covered |
| Switching-stage characterization | Switching frequency / operating mode map | Frequency, pulse-skipping/burst/spread-spectrum behavior | Sweep input/load/temp; capture switch node | fsw, dither, pulse patterns | A001, A007, A014, A094, A114 | PS-025 | Covered |
| Switching-stage characterization | Switching loss | Energy dissipated during switching transitions | Correlated voltage/current waveform math | Eon/Eoff, switching W | A001, A011, A048, A115, A122 | PS-029; GEN-020 | Partial dedicated characterization |
| Switching-stage characterization | Conduction loss | On-state semiconductor loss | Measure current and Rds(on)/Vce(sat) | conduction voltage, loss W | A001, A011, A122 | PS-029 | Partial dedicated characterization |
| Switching-stage characterization | Slew rate / dv/dt / di/dt | Edge speed and stress/EMI tendency | High-bandwidth V/I capture | dv/dt, di/dt | A001, A011, A048, A115 | PS-029; HV-004 | Covered |
| Switching-stage characterization | Modulation / duty-cycle behavior | Control behavior across operating points | Capture PWM vs load/input | duty cycle, modulation, burst mode | A001, A007, A014, A094 | PS-025 | Covered |
| Protection / abnormal behavior | Overcurrent / current-limit threshold | Output current protection accuracy and mode | Increase load beyond rating | threshold, limit current, output, temp | A041, A057, A062, A129 | GEN-013; PS-014 | Covered |
| Protection / abnormal behavior | Overpower / overload | Safe response above rated power | High load or combined line/load stress | input/output power, trip, thermal | A041, A057, A062 | GEN-013; SAF-005 | Covered |
| Protection / abnormal behavior | Output short circuit | Fault-current control and survival | Low-ohmic short during off/on states | peak/steady current, energy, recovery | A041, A057, A062, A129 | GEN-014; PS-015 | Covered |
| Protection / abnormal behavior | Overvoltage protection | Downstream safety under regulation failure | Feedback fault or externally driven output | trip level/time, latch/recovery | A057, A062 | GEN-015; PS-016 | Covered |
| Protection / abnormal behavior | Undervoltage protection | Defined state at too-low source/output | Sweep through UV threshold | trip/release, restart, state | A057, A062 | GEN-002; AUTO-009 | Covered |
| Protection / abnormal behavior | Overtemperature protection | Thermal fault shutdown/recovery | Raise load/ambient or block cooling | hotspot, trip temp, hysteresis | A041, A057, A062 | SAF-008; TH-004 | Covered |
| Protection / abnormal behavior | Hiccup / retry behavior | Repetitive fault recovery does not overstress DUT | Sustained overload/short with repeated retries | period, peak current, thermal rise | A041, A057, A129 | PS-013/014/015 | Covered |
| Protection / abnormal behavior | Reverse current / backfeed | Behavior when output or parallel source is energized | Drive output with input absent/low | reverse current, heating, rail voltage | A041, A057 | GEN-016; PS-017/AUTO-016 | Covered |
| Thermal performance | Full-load thermal operation | Thermal equilibrium at rated load | Operate at high ambient/full load | component/case temp, efficiency, Vout | A041, A048, A057, A063 | TH-001; GEN-020 | Covered |
| Thermal performance | Thermal derating | Available power/current vs temperature | Temperature/load sweep | max load, temp, protection margin | A041, A057, A063 | TH-003 | Covered |
| Thermal performance | Hotspot / component temperature | Local stress on semiconductors, magnetics, capacitors | IR/thermocouple under worst case | temperatures vs ratings | A011, A041, A048, A057 | PS-029; TH-001 | Covered |
| Reliability / robustness | Burn-in | Screening of early-life failures | Extended powered operation at elevated stress | failures, drift, temperature | A050, A052-A054 | LIFE-001/003 | Covered |
| Reliability / robustness | HALT | Determine operational/destructive margins and weak links | Progressive thermal/vibration/electrical stress | limit points, failure modes | A012, A055 | LIFE-005; RV-001 | Covered |
| Reliability / robustness | HASS / production stress screen | Detect manufacturing weaknesses without consuming life | Controlled screen derived from HALT | failures, drift, yield | A012 | LIFE/RV framework | Partial as explicit production screen |
| Reliability / robustness | Accelerated life / test-to-failure | Quantify degradation and failure mechanisms | Elevated stress, cycling or mission-derived profiles | cycles/time-to-failure, drift | A056, A097, A125 | LIFE-001/002/005/006; RV-001 | Covered |
| Reliability / robustness | Parameter drift before/after stress | Detect latent degradation that still passes absolute limit | Baseline, stress, repeated characterization | ΔV, ΔI, efficiency/ripple drift | A050-A056, A097 | Mandatory matrix metadata; LIFE-* | Covered |
| EMC / power quality | Conducted emissions pre-compliance | Noise returned on input/output cables | LISN/artificial network + spectrum/EMI receiver | dBµV spectrum, margin | A005, A013, A090 | EMC-001/006 | Covered |
| EMC / power quality | Radiated emissions pre-compliance | Converter/harness radiation | Near-field scan/chamber/antenna methods | field/spectrum, hotspots | A005, A013, A090 | EMC-002/006 | Covered |
| EMC / power quality | EFT/burst / surge / spike immunity | Survival/function under fast/high-energy input transients | Compliant transient generator/coupling network | output upset, reset, clamp stress | A051 | EMC-004/005; CHG-002/003 | Covered |
| EMC / power quality | Voltage dips / grid disturbance | Function under reduced/interrupted AC supply | Grid simulator/dip generator | state, output, recovery | A051 | EMC-009; CHG-002/003 | Covered |
| EMC / power quality | Harmonics / flicker compliance | Compatibility with public AC supply | Prescribed load states + power-quality analyzer | harmonics, THD, Pst/Plt | A001, A009, A051, A130 | EMC-010; CHG-007 | Covered |
| EMC / power quality | EMI source localization | Find switching nodes/components dominating emissions | Near-field probes + spectral correlation | hotspot amplitude/frequency | A005, A013 | EMC-006 | Covered |
| Multi-output / server / UPS | Multi-rail cross-load | Regulation with highly unbalanced rail loading | Load matrix across rails | per-rail regulation, efficiency | A057, A073, A090 | PS-031 | Covered |
| Multi-output / server / UPS | Power-good / timing | Correct ATX/server rail timing | Capture rails and control signals | PWR_OK timing, rise/fall, sequence | A057, A063, A073, A090 | GEN-011; PS-028/031 | Covered |
| Multi-output / server / UPS | High-dynamic server load profile | Response to CPU/GPU pulsed loads | Fast programmable load waveform | droop, recovery, protection | A041, A048, A061 | GEN-009; PS-008 | Covered |
| Multi-output / server / UPS | N+1/current-sharing behavior | Parallel PSU sharing and hot-service behavior | Parallel modules; insert/remove; load steps | share error, bus transient, alarms | A041, A063 | GEN-017/018 | Covered |
| Multi-output / server / UPS | UPS transfer / hold-up | Continuity on mains failure or source transfer | Fail primary input, transfer to battery/bypass | transfer time, output excursion, autonomy | A057, A063 | GEN-003/019 | Covered |
| Charging / OBC / bidirectional | OBC AC input range | Charger operation over line/frequency range | Programmable AC/grid simulator | power, PF, charge output, faults | A047, A051, A130 | CHG-001 | Covered |
| Charging / OBC / bidirectional | OBC efficiency map | Grid-to-battery conversion performance | AC line × battery voltage × charge power | AC/DC power, efficiency, temperature | A047, A051, A130 | CHG-006 | Covered |
| Charging / OBC / bidirectional | Charger CC/CV transition | Charging control behavior and battery protection | Battery simulator/SOC profile | I/V trajectory, transition point, thermal | A051 | BAT-001; CHG-010 | Covered |
| Charging / OBC / bidirectional | Charger/BMS coordination | Correct requested voltage/current and fault inhibition | Emulate BMS commands/sensor/fault states | commands, delivered V/I, contactor state | A051 | CHG-010/011/014 | Covered |
| Charging / OBC / bidirectional | Grid disturbance immunity | OBC behavior during dips, frequency/phase abnormalities | Grid simulator with dips/phase control/harmonics | state, charge power, recovery | A051 | CHG-002/003/004 | Covered |
| Charging / OBC / bidirectional | OBC harmonics / PF | Grid power quality during charging | Harmonic injection/measurement over charge power | PF, harmonics, flicker | A047, A051, A130 | CHG-006/007 | Covered |
| Charging / OBC / bidirectional | V2G/V2H four-quadrant transition | Stable reversal between charge and export | Regenerative grid/battery simulator | transition excursion, current direction, timing | A051 | CHG-012/013 | Covered |
| Charging / OBC / bidirectional | Charging communication-loss recovery | Safe behavior when charging control link fails | Drop/invalid PWM/PLC/BMS sequence | power cessation, state, diagnostics, restart | A051 | CHG-014 | Covered |

---

## Supporting measurement and execution controls

These recur throughout the articles but should **not** be counted as separate DUT test functions. They determine whether the result is trustworthy.

| Control | Why it matters | Typical implementation | Representative corpus IDs |
|---|---|---|---|
| Probe bandwidth and grounding | Poor probing can make ripple/ringing measurements meaningless | Short ground spring/coax tip; differential probe with adequate bandwidth | A001, A014-A015, A108 |
| Voltage/current channel de-skew | Timing error directly corrupts switching-loss calculation | Deskew probes/current shunts before V×I math | A001, A011, A115 |
| High dynamic range / offset capability | Small ripple must be measured on a large DC rail | High-resolution digitizer, DC offset, DC block only with awareness of LF loss | A022, A060 |
| Shunt/current-probe selection | Bandwidth, burden voltage and common-mode error affect current results | Calibrated shunt, current probe or SMU as appropriate | A003, A022, A045 |
| Instrument synchronization | Efficiency/transient calculations need simultaneous V/I data | Common trigger/timebase; synchronized channels | A001-A003, A022, A041 |
| Source/load settling and slew verification | Programmed values are not necessarily the actual DUT stimulus | Verify at DUT terminals with scope/DMM/power analyzer | A002-A003, A023-A024, A038, A049 |
| Long-record triggered acquisition | Rare events otherwise disappear between acquisitions | Trigger on rail threshold/fault and retain pre/post history | A022 |
| Automation and recipe control | Repeatability and throughput improve with programmed sweeps | SCPI/ATE, scripted source/load/chamber control and report generation | A002-A003, A040-A045, A049-A051, A065, A080/A084/A092/A098/A120/A127 |
| Calibration / uncertainty / guard band | Prevent false pass/fail at tight limits | Calibrated instruments; uncertainty budget; guard-band rule | A003, A044-A047, A076 |
| Thermal stabilization | Efficiency/regulation varies with self-heating | Wait for equilibrium before comparing operating points | A002, A044-A048 |

---

## Main conclusions from the article corpus

1. **The corpus is strongly convergent.** Independent vendors, reviewers and academic sources repeatedly test the same core functions: regulation, efficiency, ripple/noise, load/line transients, startup/timing, loop stability, protection and thermal behavior.
2. **Time-domain transient testing and frequency-domain loop testing are complementary, not interchangeable.** Multiple sources explicitly show that a good-looking load step can coexist with poor phase/gain margin; the matrix correctly retains both `PS-008` and `PS-021/PS-032`.
3. **Ripple/noise measurement quality is frequently limited by the measurement setup rather than the DUT.** Probe grounding, bandwidth, dynamic range and offset strategy are therefore execution controls that should be captured in test metadata.
4. **Switching-loss and conduction-loss measurements deserve explicit characterization even when total efficiency is already measured.** They localize the mechanism behind loss/temperature and are particularly useful for wide-bandgap or high-frequency designs.
5. **Burn-in, HALT/HASS and test-to-failure are different objectives.** Burn-in screens early failures, HALT discovers margins/weak links, HASS is a production screen derived from robustness knowledge, and accelerated-life testing estimates degradation/life.
6. **Server/AI PSU testing is distinguished mainly by load dynamics and parallel/redundant operation**, not by a fundamentally different static characterization model.
7. **OBC testing adds a genuine new source interface:** AC/grid quality, phase behavior, charging coordination and bidirectional operation. These are now represented by the `CHG-*` family.
8. **Most article-derived test functions are already represented in the global matrix.** The most useful areas for further refinement are dedicated generic rows/metrics for input-current crest factor, remote-sense/distribution-drop behavior, semiconductor switching/conduction loss breakdown, and explicit HASS/production stress screening.

## Candidate refinements for the global matrix

These are not necessarily new requirements; they are places where the article corpus suggests making an existing broad row more explicit:

| Candidate | Suggested treatment | Existing parent |
|---|---|---|
| Generic AC input current crest factor / waveform quality | Add metric/sub-test under input characterization rather than a new top-level test unless a product standard requires it | GEN-006 / GEN-020 |
| Remote-sense / distribution-drop compensation | Add conditional sub-test for remotely sensed supplies and long-cable installations | GEN-007 / PS-023 |
| Switching-loss / conduction-loss breakdown | Add dedicated characterization sub-tests for converter development and WBG devices | GEN-020 / PS-029 |
| HASS / production stress screening | Add production-screening row distinct from HALT and life qualification | LIFE-* / RV-001 |
| Output-current regulation accuracy | Add explicit sub-test where the product regulates current as a primary function | GEN-007 / BAT-001 / CHG-010 |

## Relationship to the source index

The original multilingual index remains the provenance record and language-oriented reading list. This document is the normalized engineering view: **article → tested function → existing matrix row**.
