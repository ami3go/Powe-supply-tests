# Automotive Power Supply Validation Test Matrix

_Last researched: 2026-09-20_

## Scope

This matrix is intended for validation of an automotive DC power supply / DC-DC converter / ECU power stage using a programmable DC source, electronic load, oscilloscope and thermal chamber.

It combines:

- core converter characterization;
- automotive supply-disturbance tests;
- protection and fault-injection tests;
- thermal and endurance tests;
- EMC/transient tests that require additional equipment;
- 48 V and high-voltage references where applicable.

> **Important:** the values below are a planning matrix, not a replacement for a licensed standard or the customer/OEM component requirement specification. Exact severity, duration, source impedance, number of cycles, functional-status requirement and sample count shall be taken from the applicable contract specification and standard edition.

### Setup legend

- **YES** — can normally be executed with the present bench: programmable supply + electronic load + oscilloscope + thermal chamber.
- **PARTIAL** — useful pre-compliance test is possible, but a compliant fixture/generator/instrument is needed for formal testing.
- **NO** — requires dedicated EMC/environmental equipment or an external laboratory.

## Test matrix

| ID | Category | Test | Purpose / failure mechanism | Typical stimulus / conditions | Measure / record | Acceptance / target | Present setup | Additional equipment | Main reference |
|---|---|---|---|---|---|---|---|---|---|
| PS-001 | DC characterization | Input operating range | Verify regulation over the intended battery/input range and identify UVLO/OVLO boundaries | Sweep input slowly from below minimum to above maximum at light, nominal and full load | Vin, Iin, Vout, Iout, state/faults | Output and functions remain within product requirements throughout specified operating range | YES | Optional DMM/data logger | ISO 16750-2:2023; product specification |
| PS-002 | DC characterization | Output voltage accuracy | Establish absolute output accuracy | Nominal Vin; 0%, 10%, 50%, 100% load; hot/room/cold | Vout mean, min/max | Within output-voltage tolerance | YES | Precision DMM recommended | Keysight DC-DC Converter Testing Fundamentals |
| PS-003 | DC characterization | Line regulation | Quantify Vout sensitivity to Vin | Sweep Vin across operating range at fixed loads | ΔVout vs ΔVin; % line regulation | Within design requirement | YES | Precision DMM recommended | Keysight DC-DC Converter Testing Fundamentals |
| PS-004 | DC characterization | Load regulation | Quantify Vout sensitivity to load | Sweep load from minimum to full load at low/nominal/high Vin | Vout vs Iout; % load regulation | Within design requirement | YES | Precision DMM recommended | Keysight DC-DC Converter Testing Fundamentals |
| PS-005 | DC characterization | Efficiency map | Establish efficiency, loss and thermal worst cases | Sweep Vin × load × temperature | Pin, Pout, efficiency, case/component temperature | Meets efficiency and thermal budget; no thermal limit violation | YES | Accurate current/voltage measurement; power analyzer optional | Keysight DC-DC Converter Testing Fundamentals |
| PS-006 | DC characterization | No-load / standby consumption | Verify key-off/standby consumption | No load and defined sleep/key-off states across Vin and temperature | Iin average, peak/wake events | Customer/OEM current budget met | YES | µA-capable ammeter may be needed | LV 124 E-19 Closed-circuit current; product requirement |
| PS-007 | DC characterization | Output ripple and noise | Check switching ripple, burst/PFM artifacts and broadband noise | Min/nom/max Vin; light/nom/full load; hot/cold | Vout ripple p-p/RMS; dominant frequencies | Within rail/noise specification | YES | Proper low-inductance probe or coax tip | Keysight DC-DC Converter Testing Fundamentals |
| PS-008 | Dynamic | Load transient response | Verify control-loop response to rapid load changes | Load steps e.g. 10→90% and 90→10%; several slew rates | Vout undershoot/overshoot, recovery time, ringing | No reset/protection; within transient-voltage requirement | YES | Electronic load with dynamic mode; current probe helpful | Keysight DC-DC Converter Testing Fundamentals |
| PS-009 | Dynamic | Line transient response | Verify immunity to rapid but non-destructive input changes | Step Vin between representative low/nominal/high values | Vout excursion, recovery time, state/faults | Meets regulation/recovery requirement | YES | Source with adequate slew/bandwidth | ISO 16750-2:2023; product requirement |
| PS-010 | Dynamic | Start-up / turn-on | Verify monotonic startup, soft-start and sequencing | Power-on at multiple Vin/load/temp combinations; enable-pin startup if present | Inrush, rise time, overshoot, sequencing, PGOOD | No excessive overshoot; correct sequencing and timing | YES | Current probe useful | Keysight DC-DC Converter Testing Fundamentals |
| PS-011 | Dynamic | Shutdown / power-down | Check controlled turn-off and reverse current | Disable/power removal at different loads and Vin | Fall time, negative voltage, backfeed, fault state | Safe monotonic shutdown; no damaging reverse current | YES | Current probe useful | Product requirement; LV 124 E-21 Backfeeds |
| PS-012 | Dynamic | Input inrush current | Verify input capacitor charging and switch/FET stress | Repeated hot-plug or programmed fast Vin edges at cold/room/hot | Peak current, charge, I²t, Vin dip | Connector/fuse/FET/cap limits not exceeded | YES | Current probe/shunt with suitable bandwidth | Keysight DC-DC Converter Testing Fundamentals; product/OEM requirement |
| PS-013 | Dynamic | Repeated restart / hiccup behavior | Verify deterministic recovery from UVLO/overload/fault | Repeated enable cycles and fault-clear cycles | Restart period, peak current, Vout overshoot | No latch-up or uncontrolled repeated stress | YES | — | Product requirement |
| PS-014 | Protection | Current limit / overload | Verify current-limit threshold and thermal behavior | Increase load beyond rated output; test hot/cold and Vin corners | Limit current, Vout, temperature, mode | Threshold inside specified band; no damage | YES | — | LV 124 E-22 Overcurrents; product requirement |
| PS-015 | Protection | Output short circuit | Verify short-circuit withstand and recovery | Short output while off and while operating; controlled duration | Iout peak/steady, input current, temperatures, recovery | No fire/damage; recovery matches requirement | YES | Low-ohmic high-current short fixture / relay recommended | LV 124 E-17 / E-22; product requirement |
| PS-016 | Protection | Output over-voltage protection | Verify OVP threshold and safe state | Force feedback fault where safely possible or inject external output voltage | Trip threshold, response time, latch/recovery | No downstream overvoltage beyond allowed limit | PARTIAL | Fault-injection fixture; external source may be needed | Product safety requirement |
| PS-017 | Protection | Reverse output / backfeed | Check behavior when output is externally driven while input is absent or lower | Apply allowed external Vout; vary Vin/enable state | Reverse current into output/input; internal heating | Within backfeed/reverse-current requirement | PARTIAL | Source-capable load or second DC source | LV 124 E-21 Backfeeds |
| PS-018 | Protection | Reverse input polarity | Verify survival under battery reversal where applicable | Apply specified negative input voltage/current limit | Input current, component stress, post-test function | Required functional status and no unsafe damage | PARTIAL | Bipolar/4-quadrant source or polarity-reversal contactor | ISO 16750-2:2023; LV 124 E-15 Reverse polarity |
| PS-019 | Fault injection | Open supply / connector interruption | Check behavior under intermittent connector/battery contact | Open supply for controlled durations, including repeated interruptions | Vout hold-up, reset point, recovery, DTCs | Defined reset/recovery; no undefined state | YES | Fast relay/MOSFET interruption fixture for sub-ms work | LV 124 E-10, E-13, E-14 |
| PS-020 | Fault injection | Ground offset | Verify tolerance to differences between DUT ground and system ground | Insert programmable/specified offset or resistance in return path | Vout, communications, currents, DTCs | Meets functional requirement without unsafe current | PARTIAL | Floating/bipolar source or offset injection fixture | LV 124 E-16 Ground offset |
| AUTO-001 | Automotive supply | Long-term overvoltage | Simulate charging/generator-control fault | Apply OEM-defined elevated DC voltage for the required duration, typically at elevated temperature | Input/output currents, Vout, component temperature, function | Functional status per OEM; no overstress/damage | YES | — | ISO 16750-2:2023; LV 124 E-01 |
| AUTO-002 | Automotive supply | Transient overvoltage | Verify immunity to short high-voltage supply excursion | Program specified step/pulse when source bandwidth permits | Vout, reset/faults, peak device stress | Functional status per requirement | PARTIAL | Fast source/amplifier may be needed | ISO 16750-2:2023; LV 124 E-02 |
| AUTO-003 | Automotive supply | Transient undervoltage | Verify operation through temporary battery sag | Apply specified low-voltage level and duration | Vout, reset threshold, hold-up/recovery | No undefined behavior; status per requirement | YES | — | ISO 16750-2:2023; LV 124 E-03 |
| AUTO-004 | Automotive supply | Jump start | Verify survival of elevated battery voltage during jump starting | Apply specified jump-start level/duration for 12/24 V architecture | Vout, Iin, temperature, post-test function | No damage; function/status per OEM | YES, if source voltage range permits | Higher-voltage source if bench source range is insufficient | ISO 16750-2:2023; LV 124 E-04 |
| AUTO-005 | Automotive supply | Load dump | Verify immunity to energy-rich alternator transient after load disconnection | Apply specified load-dump pulse and source impedance | Clamp voltage/current, absorbed energy, Vout, survival | No unsafe damage; functional status per requirement | NO | ISO 7637/load-dump pulse generator or automotive transient generator | ISO 16750-2:2023; ISO 7637-2:2011; LV 124 E-05 |
| AUTO-006 | Automotive supply | Superimposed AC / alternator ripple | Check susceptibility to AC ripple on battery rail | Sweep sinusoidal/defined AC ripple on DC input over specified frequency/amplitude | Vout ripple transfer, resets, faults, input current | Functional status A where required; no abnormal oscillation | PARTIAL | Arbitrary/4-quadrant supply or coupling amplifier for full frequency range | ISO 16750-2:2023; LV 124 E-06 |
| AUTO-007 | Automotive supply | Slow decrease and increase | Simulate battery discharge/charge and determine reset thresholds | Slowly ramp from upper operating voltage toward 0 V and back | Reset/off/on thresholds, hysteresis, DTCs, Vout | Defined behavior; no unstable reset cycling | YES | — | ISO 16750-2:2023; LV 124 E-07 |
| AUTO-008 | Automotive supply | Slow decrease / fast increase | Verify recovery after near-dead battery followed by rapid restoration | Slow ramp down followed by abrupt return | Reset/recovery time, inrush, overshoot | Deterministic recovery; no latch-up | YES if source slew is adequate | — | LV 124 E-08 |
| AUTO-009 | Automotive supply | Reset behavior / brownout map | Characterize functional boundary around reset voltage | Sweep/dwell around UVLO and reset threshold under several loads/temps | Reset threshold, hysteresis, boot time, memory/DTC status | Repeatable thresholds; no corrupt state/NVM | YES | DUT communications/logger useful | LV 124 E-09 |
| AUTO-010 | Automotive supply | Short supply interruptions | Verify hold-up for contact bounce / micro-interruptions | Interrupt Vin for specified durations from µs/ms upward | Minimum Vin, Vout droop, reset/no-reset boundary | Required functional status; deterministic recovery | PARTIAL | Fast MOSFET/relay interruption fixture for short durations | LV 124 E-10; ISO 16750-2:2023 |
| AUTO-011 | Automotive supply | Engine start / cold crank | Simulate starter-motor battery sag and recovery profile | Reproduce OEM-defined cranking waveform at cold and warm conditions | Vout, reset, current, boot time, control-state continuity | Start-relevant functions meet required status | YES/PARTIAL | Arbitrary source/4-quadrant amplifier if bench PSU cannot reproduce waveform | ISO 16750-2:2023; LV 124 E-11 |
| AUTO-012 | Automotive supply | Generator / smart charging voltage profile | Verify operation under dynamic alternator control | Replay defined battery-voltage profile | Vout, Iin, mode transitions, faults | Required functional status | YES/PARTIAL | Arbitrary waveform-capable supply recommended | LV 124 E-12 |
| AUTO-013 | Automotive supply | Pin interruption | Detect sensitivity to intermittent individual power/ground pins | Open one supply/ground pin at a time if multiple pins exist | Pin currents, Vout, thermal imbalance, DTCs | No connector/pin overstress; defined function | PARTIAL | Multi-pole relay matrix / fault-insertion unit | LV 124 E-13 |
| AUTO-014 | Automotive supply | Connector interruption | Simulate complete connector disconnect/reconnect | Open/reconnect supply and relevant signals under defined state | Inrush, reset/recovery, arcing-related behavior | Defined recovery; no damage | PARTIAL | Automotive relay/fault insertion fixture | LV 124 E-14 |
| AUTO-015 | Automotive supply | Closed-circuit/quiescent current | Verify sleep current over voltage and temperature | Measure long-term current after all timers expire | Sleep current, periodic wakeups, energy/day | OEM current budget met | PARTIAL | High-dynamic-range ammeter/current logger | LV 124 E-19 |
| AUTO-016 | Automotive supply | Backfeed into vehicle rail | Ensure output or I/O does not unintentionally power the ECU/vehicle rail | Remove Vin and energize output/I/O paths as applicable | Reverse current and unintended rail voltage | Below allowed backfeed limits | PARTIAL | Additional source(s), ammeters | LV 124 E-21 |
| AUTO-017 | Automotive supply | Repetitive ON/OFF endurance | Find wear-out and marginal restart behavior | Thousands to millions of controlled power cycles; combine with hot/cold as needed | Failures, drift, inrush distribution, boot time | No unacceptable drift/failure over required cycles | YES | Automated switching/logger recommended | LV 124 derivative/OEM endurance requirements; product DV plan |
| TR-001 | Conducted transient immunity | ISO pulse 1 | Simulate negative transient caused by interruption of inductive loads sharing the supply | Standardized pulse applied to supply line | DUT function, Vout, clamp current/voltage | Functional performance status per test plan | NO | ISO 7637-2 transient generator/coupling network | ISO 7637-2:2011 |
| TR-002 | Conducted transient immunity | ISO pulse 2a | Simulate positive transient caused by sudden interruption of current in parallel inductive paths | Standardized positive pulse | DUT function and stress | Status per test plan | NO | ISO 7637-2 transient generator | ISO 7637-2:2011 |
| TR-003 | Conducted transient immunity | ISO pulse 2b | Simulate supply transient related to DC motor acting as a generator after ignition-off | Standardized pulse/profile | DUT function/restart | Status per test plan | NO/PARTIAL | Automotive transient generator / arbitrary source | ISO 7637-2:2011 |
| TR-004 | Conducted transient immunity | ISO pulses 3a / 3b | Simulate fast switching/contact-bounce transients | Fast negative and positive burst pulses | Functional upset, resets, latent damage | Functional performance status per test plan | NO | Fast transient generator and coupling network | ISO 7637-2:2011 |
| TR-005 | Coupled transient immunity | Signal/control-line transient coupling | Verify immunity of enable/communication/sense lines to coupled switching transients | CCC/DCC/ICC coupling methods on non-supply lines | Functional state, communications errors, resets | FPSC per plan | NO | CCC/DCC/ICC coupling fixtures and generator | ISO 7637-3:2016 |
| EMC-001 | Emissions | Conducted emissions on power leads | Measure RF noise returned to vehicle supply | Operate DUT at representative modes/loads and measure with standardized network/receiver | dBµV spectrum vs frequency | Below applicable CISPR 25/OEM class limits | NO | LISN/AN, EMI receiver/spectrum analyzer, chamber/table setup | CISPR 25:2021 |
| EMC-002 | Emissions | Radiated emissions | Measure electromagnetic radiation from converter/harness | Representative operating modes and harness configuration | Electric-field spectrum | Below applicable CISPR 25/OEM limits | NO | ALSE/semi-anechoic chamber, antennas, EMI receiver | CISPR 25:2021 |
| EMC-003 | RF immunity | Bulk current injection (BCI) | Verify immunity to RF current coupled into harness | Sweep RF current through harness using injection probe | Function, Vout, communications, faults | Required functional status throughout sweep | NO | RF generator, amplifier, injection/monitor probes, calibration fixture | ISO 11452-4:2020 |
| EMC-004 | RF immunity | Radiated immunity (ALSE) | Verify immunity to continuous narrowband RF fields | Expose DUT+harness in absorber-lined shielded enclosure | Function, Vout, communications, faults | Required functional status | NO | ALSE chamber, RF generator/amplifiers/antennas/field probes | ISO 11452-2:2019 + ISO 11452-1:2025 |
| EMC-005 | ESD | ESD immunity | Verify resistance to electrostatic discharge during assembly/service/occupant interaction | Contact/air discharges to defined points and coupling structures | Resets, damage, communication faults | Functional status per ISO/customer requirement | NO | Automotive ESD simulator and ISO 10605 bench setup | ISO 10605:2023 |
| TH-001 | Thermal | High-temperature operation | Verify full-load operation at maximum ambient | Soak chamber, operate at defined Vin/load; include hot-start | Vout, efficiency, component/case temperatures, faults | Meets function/derating limits; no thermal overstress | YES | Thermocouples/data logger recommended | ISO 16750-4:2023; product requirement |
| TH-002 | Thermal | Low-temperature operation / cold start | Verify startup and regulation at minimum ambient | Cold soak unpowered and/or powered, then start at low Vin and rated load | Startup time, Vout, inrush, oscillation | Starts and regulates per requirement | YES | Thermocouples/data logger recommended | ISO 16750-4:2023 |
| TH-003 | Thermal | Thermal derating characterization | Determine output-current capability vs ambient/case temperature | Sweep chamber temperature and load until rating/limit boundary | Max continuous load, Tj estimate, thermal shutdown margin | Defined derating curve with safe margin | YES | Thermocouples/IR camera helpful | ISO 16750-4:2023; component limits |
| TH-004 | Thermal | Thermal shutdown and recovery | Verify OTP threshold, hysteresis and safe recovery | Force worst-case load/ambient until protection triggers, where safe | Shutdown temperature proxy, current, restart threshold | Controlled protection; no oscillatory destructive cycling | YES | Thermocouples/thermal camera recommended | Product protection requirement |
| TH-005 | Thermal | Temperature cycling | Expose solder joints, connectors and materials to repeated temperature extremes | Chamber cycles between specified Tmin/Tmax, powered or unpowered per plan | Functional checks, parameter drift, visual inspection | No crack/failure; parameters remain within limits | YES if chamber supports required ramps/range | — | ISO 16750-4:2023 |
| TH-006 | Thermal | Rapid temperature change / thermal shock | Stress interfaces and solder joints with high ΔT rate | Rapid transition between temperature extremes | Functional checks and post-test inspection | No damage or unacceptable drift | PARTIAL | Two-zone shock chamber may be required for specified transfer time | ISO 16750-4:2023 |
| TH-007 | Environmental | Damp heat / humidity | Find leakage, corrosion and insulation weaknesses | High humidity with temperature profile as specified | Leakage/current, insulation behavior, function | Meets functional/insulation requirements | PARTIAL | Humidity-controlled chamber required unless present chamber supports RH | ISO 16750-4:2023 |
| TH-008 | Combined stress | Electrical stress at temperature corners | Catch interactions missed by separate electrical/thermal tests | Repeat line/load/start/overload tests at Tmin, room and Tmax | All electrical metrics and temperatures | Same functional-status requirement with allowed temperature derating | YES | Automated control/logging recommended | ISO 16750-2:2023 + ISO 16750-4:2023 |
| LIFE-001 | Endurance | High-temperature operating life | Accelerate thermally driven wear-out under electrical load | Extended powered operation at agreed elevated temperature/load | Drift, failures, efficiency, temperatures | No failure; drift within DV limits | YES | Automated logging; independent safety cutoffs | OEM DV/PV plan; ISO 16750-4 context |
| LIFE-002 | Endurance | Power/thermal cycling | Stress power semiconductors, solder and magnetics through repeated ΔTj | Alternate high/low load and/or power state at temperature corners | Vout, Rds/on-loss proxies, temperature swing, failures | No degradation beyond limits | YES | Current/temperature logging | OEM reliability plan |
| LIFE-003 | Endurance | Worst-case continuous operation | Verify no cumulative thermal runaway | Max permitted Vin/load at worst thermal point for extended duration | Temperatures, Vout, efficiency, fault events | Stable temperatures and parameters | YES | — | Product DV plan |
| ENV-001 | Mechanical | Vibration | Find fatigue/intermittent connections | Vehicle-location-specific vibration profile | Function during test; post-test inspection | No loss of function or damage | NO | Electrodynamic shaker, fixture, control accelerometers | ISO 16750-3:2023 |
| ENV-002 | Mechanical | Mechanical shock | Verify robustness to road/handling shocks | Specified shock pulses and axes | Functional interruptions; mechanical damage | Meets location-specific requirement | NO | Shock table/shaker | ISO 16750-3:2023 |
| ENV-003 | Ingress | Dust/water/IP | Verify enclosure protection where applicable | IP-code test appropriate to mounting location | Water/dust ingress; function/insulation | Required IP code | NO | IP test equipment | ISO 20653:2023 |
| ENV-004 | Chemical | Automotive fluids exposure | Check plastics, seals, coatings and labels against fluids | Apply location-relevant agents, then condition and inspect/test | Visual/material change, electrical function | No unacceptable degradation | NO | Chemical test facilities | ISO 16750-5:2023 |
| 48V-001 | 48 V architecture | 48 V supply voltage range and slow transients | Validate components connected to nominal 48 V vehicle electrical system | Apply defined 48 V ranges, slow transients/fluctuations and operating modes | Vout, input current, state, protection | Meets ISO/customer functional requirements | YES/PARTIAL depending source range | 48 V-capable programmable source / 4-quadrant source as needed | ISO 21780:2020 |
| HV-001 | HV / voltage class B | HV DC terminal electrical behavior | Validate DC-link-connected component against traction-system electrical behavior | Apply customer/ISO-defined voltage class B profiles and operating conditions | Terminal V/I, function, insulation monitoring as applicable | Meets component requirement | NO/PARTIAL | HV source/load, safety interlocks, isolation measurement | ISO 21498-2:2024 |

## Recommended execution order with the current bench

A practical sequence that minimizes the risk of destroying an uncharacterized prototype is:

1. **Baseline:** PS-001…PS-007.
2. **Dynamic control-loop behavior:** PS-008…PS-013.
3. **Protection:** PS-014…PS-020.
4. **Automotive supply profiles:** AUTO-001…AUTO-017, starting with non-destructive voltage ramps before severe pulses.
5. **Temperature corners:** TH-001…TH-005 and TH-008 while repeating the most important baseline/dynamic tests.
6. **Endurance:** LIFE-001…LIFE-003 after the design has passed the short-duration tests.
7. **Formal transient/EMC/environmental qualification:** TR-*, EMC-* and ENV-* using compliant test equipment or an accredited laboratory.

## What the present bench can cover well

With the programmable power supply, electronic load, oscilloscope and thermal chamber, the highest-value immediately executable work is:

- input/output operating envelope;
- line/load regulation and efficiency;
- ripple/noise and load-transient response;
- startup, shutdown, UVLO, reset and recovery;
- overcurrent, short-circuit and thermal protection;
- jump-start/overvoltage/undervoltage tests when the source has sufficient voltage and slew rate;
- cold-crank and generator-profile replay when the source supports arbitrary waveforms;
- hot/cold operation, derating, thermal cycling and combined electrical/thermal tests;
- long-duration power cycling and operating-life tests.

The largest gaps for formal automotive qualification are a compliant **ISO 7637 transient generator**, **4-quadrant/bipolar battery simulator**, **CISPR 25 LISN/artificial network + EMI receiver**, **BCI RF system**, **ALSE chamber**, **ISO 10605 ESD gun**, and mechanical/humidity/ingress facilities.

## Standards and references verified during research

The editions below were checked against primary standards-body pages where available.

1. **ISO 16750-1:2023** — Road vehicles — Environmental conditions and testing for electrical and electronic equipment — Part 1: General.  
   https://www.iso.org/standard/77578.html
2. **ISO 16750-2:2023** — Part 2: Electrical loads. This is the main ISO reference for low-voltage automotive electrical loading; EMC is explicitly outside its scope.  
   https://www.iso.org/standard/76119.html
3. **ISO 16750-3:2023** — Part 3: Mechanical loads.  
   https://www.iso.org/standard/77579.html
4. **ISO 16750-4:2023** — Part 4: Climatic loads.  
   https://www.iso.org/standard/77580.html
5. **ISO 16750-5:2023** — Part 5: Chemical loads.  
   https://www.iso.org/standard/77581.html
6. **ISO 7637-1:2023** — Electrical disturbances from conduction and coupling — Vocabulary and general considerations.  
   https://www.iso.org/standard/83230.html
7. **ISO 7637-2:2011** — Electrical transient conduction along supply lines only. ISO lists the 2011 edition as current/confirmed, with an amendment project under development.  
   https://www.iso.org/standard/50925.html
8. **ISO 7637-3:2016** — Transient transmission by capacitive and inductive coupling via lines other than supply lines.  
   https://www.iso.org/standard/59603.html
9. **ISO 10605:2023** — Automotive ESD test methods.  
   https://www.iso.org/standard/79094.html
10. **ISO 11452-1:2025** — General principles and terminology for component RF-immunity testing.  
    https://www.iso.org/committee/5383636/x/catalogue/
11. **ISO 11452-2:2019** — Absorber-lined shielded enclosure (ALSE) immunity method. ISO shows a replacement work item under development.  
    https://www.iso.org/standard/68557.html
12. **ISO 11452-4:2020** — Harness excitation methods including bulk current injection (BCI).  
    https://www.iso.org/standard/74108.html
13. **CISPR 25:2021** — Limits and methods for radio disturbances for protection of on-board receivers, covering 150 kHz to 5 925 MHz.  
    https://webstore.iec.ch/en/publication/64645
14. **ISO 21780:2020** — 48 V supply voltage — Electrical requirements and tests. ISO confirmed this edition in 2026.  
    https://www.iso.org/standard/71607.html
15. **ISO 21498-2:2024** — Voltage class B systems/components — Electrical tests for components.  
    https://www.iso.org/standard/84542.html
16. **ISO 20653:2023** — Automotive IP-code protection of electrical equipment against foreign objects, water and access.  
    https://www.iso.org/standard/76116.html
17. **Keysight — DC-DC Converter Testing Fundamentals / DC-DC converter testing** — practical reference for input range, output accuracy, line/load regulation, efficiency, transient response, turn-on/off, ripple/noise and inrush-current measurement.  
    https://www.keysight.com/us/en/assets/3125-1397/application-notes/DC-DC-Converter-Testing-Fundamentals.pdf
18. **TÜV SÜD — VW 80000** — confirms VW 80000 is based on LV 124 and provides the OEM test-family context.  
    https://www.tuvsud.com/en-us/industries/automotive/automotive-testing-solutions/vw80000
19. **Weiss Technik — LV 124 overview** — useful public overview of LV 124 electrical/environmental test families.  
    https://backend.weiss-technik.com/webapp/weisstechnik/detailpages/environmental-simulation/LV124/Weiss-Technik-Technisches-Informationsblatt_LV-124.pdf

## Standards status notes as of 2026-09-20

- ISO 21780:2020 was reviewed and confirmed in 2026 and remains current.
- ISO 10605:2023 remains the published ESD standard; ISO lists a draft Amendment 1 under development.
- ISO 7637-2:2011 remains published/current; ISO lists an Amendment 1 project under development.
- ISO 11452-2:2019 remains published while a new edition is under development.
- ISO 16750-1/3/4/5 have newer work items under development, but the 2023 editions listed above remain the published references at the time of this review.

## Suggested next repository additions

For repeatable validation, this matrix can be expanded into machine-executable assets:

- `tests/*.yaml` — stimulus profiles and acceptance limits;
- `profiles/` — CSV waveform definitions for crank, supply dips, ramps and generator-control profiles;
- `reports/` — test report templates;
- `scripts/` — SCPI automation for the source, electronic load, oscilloscope and chamber;
- `requirements/` — project-specific limits mapped to the matrix IDs above.
