# Automotive Power Supply Validation Test Matrix

_Last updated: 2026-09-20_

## Scope

This matrix is intended for validation of an automotive DC power supply, DC-DC converter, or ECU power stage using a programmable DC source, electronic load, oscilloscope and thermal chamber. It combines converter characterization, automotive battery disturbances, fault/protection tests, thermal/endurance testing, EMC/transient qualification, and 48 V / voltage-class-B references.

> **Important:** this is a planning matrix, not a substitute for the licensed standard or customer/OEM component requirement specification. Exact severity, waveform, source impedance, repetitions, functional-status requirement, sample count and acceptance limits shall be taken from the applicable contract specification and standard edition.

### Setup legend

- **YES** — can normally be executed with the present bench.
- **PARTIAL** — useful pre-compliance testing is possible, but a compliant fixture/generator/instrument is needed for the full method.
- **NO** — requires dedicated EMC/environmental/HV equipment or an external laboratory.

### Equipment legend

The **Equipment required** column lists the complete practical setup for each test, not only equipment that is missing from the present bench.

| Code | Equipment |
|---|---|
| PSU | Programmable DC power supply / battery source |
| BPS | Bipolar or 4-quadrant automotive battery simulator |
| EL | Programmable electronic load |
| OSC | Digital oscilloscope |
| DMM | Precision digital multimeter |
| PA | Power analyzer |
| CP | Current probe or calibrated current shunt |
| TC | Thermal chamber |
| TEMP | Thermocouples / temperature logger / IR camera as applicable |
| DL | Data logger / DAQ / automated test controller |
| FIU | Fault-insertion unit, relay matrix or MOSFET interrupter |
| FGEN | Function/arbitrary waveform generator |
| SMU | Source-measure unit |
| LISN/AN | CISPR 25 line-impedance-stabilization/artificial network |

## Test matrix

| ID | Category | Test | Purpose / failure mechanism | Typical stimulus / conditions | Measure / record | Acceptance / target | Present setup | Equipment required | Main reference |
|---|---|---|---|---|---|---|---|---|---|
| PS-001 | DC characterization | Input operating range | Verify regulation across specified battery/input range and identify UVLO/OVLO boundaries. | Slow Vin sweep below minimum through maximum at light/nominal/full load; repeat key temperature corners. | Vin, Iin, Vout, Iout, state/faults | Meets product operating-range and regulation requirements | YES | PSU; EL; OSC; DMM; TC; DL recommended | ISO 16750-2:2023; product specification |
| PS-002 | DC characterization | Output voltage accuracy | Establish absolute output accuracy. | Nominal Vin; 0/10/50/100% load; hot/room/cold. | Vout mean/min/max | Within output-voltage tolerance | YES | PSU; EL; DMM; TC; DL | Keysight DC-DC Converter Testing Fundamentals |
| PS-003 | DC characterization | Line regulation | Quantify Vout sensitivity to Vin. | Sweep Vin across operating range at fixed loads. | ΔVout vs ΔVin; % line regulation | Within design requirement | YES | PSU; EL; DMM; OSC; DL | Keysight DC-DC Converter Testing Fundamentals |
| PS-004 | DC characterization | Load regulation | Quantify Vout sensitivity to load. | Sweep load from minimum to full load at low/nominal/high Vin. | Vout vs Iout; % load regulation | Within design requirement | YES | PSU; EL; DMM; OSC; DL | Keysight DC-DC Converter Testing Fundamentals |
| PS-005 | DC characterization | Efficiency map | Establish efficiency, loss and thermal worst cases. | Sweep Vin × load × temperature. | Pin, Pout, efficiency, case/component temperature | Meets efficiency and thermal budget | YES | PSU; EL; DMM or PA; TC; TEMP; DL | Keysight DC-DC Converter Testing Fundamentals |
| PS-006 | DC characterization | No-load / standby consumption | Verify key-off/standby consumption. | No load and defined sleep/key-off states across Vin and temperature. | Iin average, peaks, wake events | Customer/OEM current budget met | YES | PSU; µA-capable DMM or SMU; TC; DL | LV 124 E-19; product requirement |
| PS-007 | DC characterization | Output ripple and noise | Check switching ripple, burst/PFM artifacts and broadband noise. | Min/nom/max Vin; light/nom/full load; hot/cold. | Vout ripple p-p/RMS; dominant frequencies | Within rail/noise specification | YES | PSU; EL; OSC; low-inductance probe/coax tip; TC | Keysight DC-DC Converter Testing Fundamentals |
| PS-008 | Dynamic | Load transient response | Verify control-loop response to rapid load changes. | Load steps such as 10→90% and 90→10%; multiple slew rates. | Undershoot/overshoot; recovery time; ringing | No reset/protection; within transient-voltage requirement | YES | PSU; dynamic EL; OSC; CP/shunt; TC for corners | Keysight DC-DC Converter Testing Fundamentals |
| PS-009 | Dynamic | Line transient response | Verify immunity to rapid non-destructive input changes. | Step Vin between representative low/nominal/high values. | Vout excursion; recovery time; state/faults | Meets regulation/recovery requirement | YES | Fast programmable PSU or BPS; EL; OSC; CP | ISO 16750-2:2023; product requirement |
| PS-010 | Dynamic | Start-up / turn-on | Verify soft-start, monotonic startup and sequencing. | Power-on at multiple Vin/load/temp combinations; enable-pin startup if present. | Inrush; rise time; overshoot; sequencing; PGOOD | Correct sequencing/timing; no excessive overshoot | YES | PSU; EL; OSC; CP/shunt; TC | Keysight DC-DC Converter Testing Fundamentals |
| PS-011 | Dynamic | Shutdown / power-down | Check controlled turn-off and reverse current. | Disable or remove input at multiple loads and Vin. | Fall time; negative excursion; backfeed; fault state | Safe shutdown; no damaging reverse current | YES | PSU; EL; OSC; CP/shunt; DMM | Product requirement; LV 124 E-21 |
| PS-012 | Dynamic | Input inrush current | Verify capacitor charging and switch/FET stress. | Repeated hot-plug or programmed fast Vin edges at cold/room/hot. | Peak current; charge; I²t; Vin dip | Connector/fuse/FET/cap limits not exceeded | YES | PSU; OSC; wide-band CP or calibrated shunt; FIU/relay optional; TC | Keysight DC-DC Converter Testing Fundamentals; OEM requirement |
| PS-013 | Dynamic | Repeated restart / hiccup behavior | Verify deterministic recovery from UVLO/overload/fault. | Repeated enable cycles and fault-clear cycles. | Restart period; peak current; Vout overshoot | No latch-up or uncontrolled repeated stress | YES | PSU; EL; OSC; automation switch/FIU; DL | Product requirement |
| PS-014 | Protection | Current limit / overload | Verify current-limit threshold and thermal behavior. | Increase load beyond rated output; test Vin and temperature corners. | Limit current; Vout; temperature; protection mode | Threshold within specified band; no damage | YES | PSU; EL; OSC; DMM; TC; TEMP | LV 124 E-22; product requirement |
| PS-015 | Protection | Output short circuit | Verify short-circuit withstand and recovery. | Short output while off and operating for controlled durations. | Peak/steady short current; Iin; temperatures; recovery | No unsafe damage; required recovery | YES | PSU; OSC; CP/shunt; low-ohmic short fixture/FIU; TC; TEMP | LV 124 E-17/E-22; product requirement |
| PS-016 | Protection | Output over-voltage protection | Verify OVP threshold and safe state. | Inject feedback fault or externally force output where safe. | Trip threshold; response time; latch/recovery | Downstream voltage stays within allowed limit | PARTIAL | PSU; EL; OSC; DMM; FIU; second source/SMU where needed | Product safety requirement |
| PS-017 | Protection | Reverse output / backfeed | Check behavior when output is externally driven. | Apply allowed external Vout while input is absent/lower; vary enable state. | Reverse current into output/input; heating | Within reverse-current/backfeed requirement | PARTIAL | PSU; second PSU/SMU or source-capable EL; DMM; OSC; TEMP | LV 124 E-21 |
| PS-018 | Protection | Reverse input polarity | Verify survival under battery reversal where applicable. | Apply specified negative input voltage/current limit. | Input current; component stress; post-test function | Required functional status; no unsafe damage | PARTIAL | BPS/4Q source or polarity-reversal contactor; EL; OSC; CP; fusing/safety fixture | ISO 16750-2:2023; LV 124 E-15 |
| PS-019 | Fault injection | Open supply / connector interruption | Check intermittent connector/battery-contact behavior. | Open supply for controlled durations including repeated interruptions. | Hold-up; reset point; recovery; DTCs | Defined reset/recovery; no undefined state | YES | PSU; EL; OSC; FIU/fast MOSFET or relay; DL | LV 124 E-10/E-13/E-14 |
| PS-020 | Fault injection | Ground offset | Verify tolerance to DUT/system ground differences. | Insert specified offset or resistance in return path. | Vout; communications; currents; DTCs | Meets functional requirement without unsafe current | PARTIAL | Floating PSU/BPS; EL; OSC; DMM; offset-injection/FIU; comms logger | LV 124 E-16 |
| AUTO-001 | Automotive supply | Long-term overvoltage | Simulate charging/generator-control fault. | Apply OEM-defined elevated DC voltage for required duration, often at elevated temperature. | Iin/Iout; Vout; temperatures; function | Functional status per OEM; no overstress/damage | YES | PSU with required voltage/current; EL; OSC; DMM; TC; TEMP; DL | ISO 16750-2:2023; LV 124 E-01 |
| AUTO-002 | Automotive supply | Transient overvoltage | Verify immunity to short high-voltage supply excursion. | Program specified step/pulse when source bandwidth allows. | Vout; reset/faults; peak device stress | Functional status per requirement | PARTIAL | Fast PSU/BPS or power amplifier; EL; OSC; HV differential probe as needed; CP | ISO 16750-2:2023; LV 124 E-02 |
| AUTO-003 | Automotive supply | Transient undervoltage | Verify operation through temporary battery sag. | Apply specified low-voltage level and duration. | Vout; reset threshold; hold-up/recovery | No undefined behavior; required status | YES | PSU; EL; OSC; DL; TC for corner testing | ISO 16750-2:2023; LV 124 E-03 |
| AUTO-004 | Automotive supply | Jump start | Verify survival of elevated battery voltage during jump starting. | Apply specified jump-start level/duration for architecture. | Vout; Iin; temperature; post-test function | No damage; required function/status | YES if source range permits | High-voltage-range PSU if needed; EL; OSC; DMM; TC; TEMP | ISO 16750-2:2023; LV 124 E-04 |
| AUTO-005 | Automotive supply | Load dump | Verify immunity to energy-rich alternator transient after load disconnection. | Apply specified load-dump waveform and source impedance. | Clamp V/I; absorbed energy; Vout; survival | No unsafe damage; functional status per requirement | NO | Automotive transient/load-dump generator; coupling network; OSC; HV probe; CP; EL; safety enclosure | ISO 16750-2:2023; ISO 7637-2:2011; LV 124 E-05 |
| AUTO-006 | Automotive supply | Superimposed AC / alternator ripple | Check susceptibility to AC ripple on battery rail. | Sweep specified sinusoidal/defined ripple over DC input. | Ripple transfer; resets; faults; input current | Required functional status; no abnormal oscillation | PARTIAL | BPS/4Q source or coupling amplifier + FGEN; EL; OSC; DMM | ISO 16750-2:2023; LV 124 E-06 |
| AUTO-007 | Automotive supply | Slow decrease and increase | Simulate battery discharge/charge and determine reset thresholds. | Slow ramp from upper operating voltage toward 0 V and back. | Reset/off/on thresholds; hysteresis; DTCs; Vout | Defined behavior; no unstable reset cycling | YES | PSU; EL; OSC; DMM; DL; TC optional | ISO 16750-2:2023; LV 124 E-07 |
| AUTO-008 | Automotive supply | Slow decrease / fast increase | Verify recovery after near-dead battery then rapid restoration. | Slow ramp down followed by abrupt return. | Reset/recovery time; inrush; overshoot | Deterministic recovery; no latch-up | YES if PSU slew is adequate | Fast programmable PSU/BPS; EL; OSC; CP | LV 124 E-08 |
| AUTO-009 | Automotive supply | Reset behavior / brownout map | Characterize functional boundary near reset voltage. | Sweep/dwell around UVLO and reset threshold at several loads/temps. | Reset threshold; hysteresis; boot time; memory/DTC state | Repeatable thresholds; no corrupt state/NVM | YES | PSU; EL; OSC; DMM; TC; DUT comms/logger | LV 124 E-09 |
| AUTO-010 | Automotive supply | Short supply interruptions | Verify hold-up for contact bounce/micro-interruptions. | Interrupt Vin for specified durations from µs/ms upward. | Minimum Vin; Vout droop; reset/no-reset boundary | Required status; deterministic recovery | PARTIAL | PSU; EL; OSC; fast MOSFET interruption FIU; CP; timing generator | LV 124 E-10; ISO 16750-2:2023 |
| AUTO-011 | Automotive supply | Engine start / cold crank | Simulate starter-motor battery sag and recovery profile. | Replay OEM-defined cranking waveform at cold and warm conditions. | Vout; reset; current; boot time; state continuity | Start-relevant functions meet required status | YES/PARTIAL | Arbitrary-waveform PSU/BPS; EL; OSC; CP; TC; DL | ISO 16750-2:2023; LV 124 E-11 |
| AUTO-012 | Automotive supply | Generator / smart charging voltage profile | Verify operation under dynamic alternator control. | Replay defined battery-voltage profile. | Vout; Iin; mode transitions; faults | Required functional status | YES/PARTIAL | Arbitrary-waveform PSU/BPS; EL; OSC; DMM; DL | LV 124 E-12 |
| AUTO-013 | Automotive supply | Pin interruption | Detect sensitivity to intermittent individual supply/ground pins. | Open one supply/ground pin at a time if multiple pins exist. | Pin currents; Vout; thermal imbalance; DTCs | No connector/pin overstress; defined function | PARTIAL | PSU; EL; OSC; multi-pole FIU/relay matrix; CP; DUT logger | LV 124 E-13 |
| AUTO-014 | Automotive supply | Connector interruption | Simulate complete connector disconnect/reconnect. | Open/reconnect supply and relevant signals under defined state. | Inrush; reset/recovery; arcing-related behavior | Defined recovery; no damage | PARTIAL | PSU; EL; OSC; automotive connector/relay FIU; CP | LV 124 E-14 |
| AUTO-015 | Automotive supply | Closed-circuit / quiescent current | Verify sleep current over voltage and temperature. | Measure long-term current after all timers expire. | Sleep current; periodic wakeups; energy/day | OEM current budget met | PARTIAL | PSU; high-dynamic-range ammeter/SMU/current logger; TC; DL | LV 124 E-19 |
| AUTO-016 | Automotive supply | Backfeed into vehicle rail | Ensure output or I/O does not unintentionally power vehicle rails. | Remove Vin and energize output/I/O paths as applicable. | Reverse current; unintended rail voltage | Below allowed backfeed limits | PARTIAL | PSU; second source/SMU; DMM/ammeter; OSC; FIU | LV 124 E-21 |
| AUTO-017 | Automotive supply | Repetitive ON/OFF endurance | Find wear-out and marginal restart behavior. | Thousands to millions of controlled power cycles; combine with hot/cold as needed. | Failures; drift; inrush distribution; boot time | No unacceptable drift/failure over required cycles | YES | PSU; EL; automation relay/MOSFET; OSC for periodic captures; TC; DL | LV 124 derivative/OEM endurance requirements; product DV plan |
| TR-001 | Conducted transient immunity | ISO pulse 1 | Simulate negative transient from interruption of inductive loads sharing the supply. | Standardized pulse on supply line. | DUT function; Vout; clamp V/I | Functional performance status per plan | NO | ISO 7637-2 transient generator; coupling network; PSU; EL; OSC; HV probe; CP | ISO 7637-2:2011 |
| TR-002 | Conducted transient immunity | ISO pulse 2a | Simulate positive transient from interruption in parallel inductive paths. | Standardized positive pulse. | DUT function; electrical stress | Status per test plan | NO | ISO 7637-2 transient generator; coupling network; PSU; EL; OSC; HV probe; CP | ISO 7637-2:2011 |
| TR-003 | Conducted transient immunity | ISO pulse 2b | Simulate transient related to DC motor generating after ignition-off. | Standardized pulse/profile. | DUT function/restart | Status per test plan | NO/PARTIAL | Automotive transient generator or capable BPS; PSU; EL; OSC; HV probe | ISO 7637-2:2011 |
| TR-004 | Conducted transient immunity | ISO pulses 3a / 3b | Simulate fast switching/contact-bounce transients. | Fast negative and positive burst pulses. | Functional upset; resets; latent damage | Functional performance status per plan | NO | Fast ISO 7637-2 transient generator; coupling network; PSU; EL; OSC; HV probe | ISO 7637-2:2011 |
| TR-005 | Coupled transient immunity | Signal/control-line transient coupling | Verify immunity of enable/communication/sense lines to coupled switching transients. | CCC/DCC/ICC methods on non-supply lines. | State; communication errors; resets | FPSC per plan | NO | Transient generator; CCC/DCC/ICC coupling fixtures; PSU; EL; OSC; DUT comms logger | ISO 7637-3:2016 |
| EMC-001 | Emissions | Conducted emissions on power leads | Measure RF noise returned to vehicle supply. | Operate representative modes/loads using standardized measurement network. | dBµV spectrum vs frequency | Below applicable CISPR 25/OEM limits | NO | LISN/AN; EMI receiver or compliant spectrum analyzer; PSU; EL; shielded setup/ground plane; cables | CISPR 25:2021 |
| EMC-002 | Emissions | Radiated emissions | Measure electromagnetic radiation from converter/harness. | Representative operating modes and standardized harness configuration. | Electric-field spectrum | Below applicable CISPR 25/OEM limits | NO | ALSE/semi-anechoic chamber; antennas; EMI receiver; LISN/AN; PSU; EL; turntable/fixtures as required | CISPR 25:2021 |
| EMC-003 | RF immunity | Bulk current injection (BCI) | Verify immunity to RF current coupled into harness. | Sweep RF current with injection probe. | Function; Vout; communications; faults | Required functional status throughout sweep | NO | RF generator; RF power amplifier; BCI injection and monitor probes; calibration fixture; power meter; PSU; EL; OSC/logger | ISO 11452-4:2020 |
| EMC-004 | RF immunity | Radiated immunity (ALSE) | Verify immunity to continuous narrowband RF fields. | Expose DUT+harness in absorber-lined shielded enclosure. | Function; Vout; communications; faults | Required functional status | NO | ALSE chamber; RF generator; amplifiers; antennas; field probes; power meters; PSU; EL; monitoring equipment | ISO 11452-2:2019; ISO 11452-1:2025 |
| EMC-005 | ESD | ESD immunity | Verify resistance to electrostatic discharge. | Contact/air discharges to defined points and coupling structures. | Resets; damage; communication faults | Functional status per ISO/customer requirement | NO | Automotive ESD simulator; ISO 10605 ground plane/coupling setup; PSU; EL; DUT monitor | ISO 10605:2023 |
| TH-001 | Thermal | High-temperature operation | Verify full-load operation at maximum ambient. | Soak chamber; operate at defined Vin/load; include hot start. | Vout; efficiency; temperatures; faults | Meets function/derating limits | YES | TC; PSU; EL; DMM; OSC; TEMP/thermocouples; DL | ISO 16750-4:2023; product requirement |
| TH-002 | Thermal | Low-temperature operation / cold start | Verify startup and regulation at minimum ambient. | Cold soak powered/unpowered as required, then start at low Vin and rated load. | Startup time; Vout; inrush; oscillation | Starts and regulates per requirement | YES | TC; PSU; EL; OSC; CP; TEMP; DL | ISO 16750-4:2023 |
| TH-003 | Thermal | Thermal derating characterization | Determine output-current capability vs ambient/case temperature. | Sweep chamber temperature and load to rating/limit boundary. | Max continuous load; Tj estimate; shutdown margin | Safe derating curve established | YES | TC; PSU; EL; DMM; TEMP; optional IR camera; DL | ISO 16750-4:2023; component limits |
| TH-004 | Thermal | Thermal shutdown and recovery | Verify OTP threshold, hysteresis and safe recovery. | Force worst-case load/ambient until protection triggers where safe. | Shutdown temperature proxy; current; restart threshold | Controlled protection; no destructive cycling | YES | TC; PSU; EL; OSC; TEMP/thermocouples; optional IR camera | Product protection requirement |
| TH-005 | Thermal | Temperature cycling | Stress solder joints, connectors and materials. | Chamber cycles between specified Tmin/Tmax, powered/unpowered per plan. | Functional checks; drift; visual inspection | No crack/failure; parameters remain within limits | YES if chamber meets profile | TC; PSU/EL for powered cycling; DMM; DL; TEMP; inspection tools | ISO 16750-4:2023 |
| TH-006 | Thermal | Rapid temperature change / thermal shock | Stress interfaces and solder joints with high ΔT rate. | Rapid transitions between temperature extremes. | Functional checks; post-test inspection | No damage or unacceptable drift | PARTIAL | Two-zone thermal-shock chamber or equivalent rapid-transfer setup; DMM; PSU; EL; inspection tools | ISO 16750-4:2023 |
| TH-007 | Environmental | Damp heat / humidity | Find leakage, corrosion and insulation weaknesses. | High humidity with specified temperature profile. | Leakage/current; insulation behavior; function | Meets functional/insulation requirements | PARTIAL | Humidity chamber; PSU; EL; DMM; insulation resistance meter if applicable; DL | ISO 16750-4:2023 |
| TH-008 | Combined stress | Electrical stress at temperature corners | Catch interactions missed by separate electrical/thermal tests. | Repeat line/load/start/overload tests at Tmin, room and Tmax. | Electrical metrics; temperatures; faults | Required status with allowed temperature derating | YES | TC; PSU; EL; OSC; DMM; CP; TEMP; DL | ISO 16750-2:2023 + ISO 16750-4:2023 |
| LIFE-001 | Endurance | High-temperature operating life | Accelerate thermally driven wear-out under electrical load. | Extended powered operation at agreed elevated temperature/load. | Drift; failures; efficiency; temperatures | No failure; drift within DV limits | YES | TC; PSU; EL; DMM; TEMP; DL; independent over-temperature/current safety cutoff | OEM DV/PV plan; ISO 16750-4 context |
| LIFE-002 | Endurance | Power / thermal cycling | Stress semiconductors, solder and magnetics through repeated ΔTj. | Alternate high/low load and/or power state at temperature corners. | Vout; loss proxies; ΔT; failures | No degradation beyond limits | YES | TC; PSU; programmable EL; automation switching; TEMP; DL; OSC periodic capture | OEM reliability plan |
| LIFE-003 | Endurance | Worst-case continuous operation | Verify no cumulative thermal runaway. | Max permitted Vin/load at worst thermal point for extended duration. | Temperatures; Vout; efficiency; fault events | Stable temperatures and parameters | YES | PSU; EL; TC; DMM; TEMP; DL; safety cutoff | Product DV plan |
| ENV-001 | Mechanical | Vibration | Find fatigue/intermittent connections. | Vehicle-location-specific vibration profile. | Function during test; post-test inspection | No loss of function or damage | NO | Electrodynamic shaker; controller; fixture; control accelerometers; PSU; EL or representative load; DUT monitor/logger | ISO 16750-3:2023 |
| ENV-002 | Mechanical | Mechanical shock | Verify robustness to road/handling shocks. | Specified shock pulses and axes. | Functional interruptions; mechanical damage | Meets location-specific requirement | NO | Shock table/shaker; fixture; accelerometers; PSU; representative load; DUT monitor | ISO 16750-3:2023 |
| ENV-003 | Ingress | Dust / water / IP | Verify enclosure protection where applicable. | IP-code test appropriate to mounting location. | Ingress; function; insulation | Required IP code | NO | ISO 20653 dust/water test equipment; IP chamber/nozzles; insulation meter; functional test bench | ISO 20653:2023 |
| ENV-004 | Chemical | Automotive fluids exposure | Check materials, seals, coatings and labels against fluids. | Apply location-relevant agents; condition; inspect and functionally retest. | Visual/material change; electrical function | No unacceptable degradation | NO | Chemical exposure facility; specified fluids; PPE/fume handling; balance/inspection tools; post-test electrical bench | ISO 16750-5:2023 |
| 48V-001 | 48 V architecture | 48 V supply voltage range and slow transients | Validate components on nominal 48 V vehicle electrical system. | Apply defined 48 V ranges, fluctuations and operating modes. | Vout; Iin; state; protection | Meets ISO/customer requirements | YES/PARTIAL | 48 V-capable programmable PSU/BPS; EL rated for power/voltage; OSC with suitable probes; DMM; TC | ISO 21780:2020 |
| HV-001 | HV / voltage class B | HV DC terminal electrical behavior | Validate traction-system component terminal behavior. | Apply customer/ISO-defined voltage-class-B profiles and operating conditions. | Terminal V/I; function; insulation monitoring | Meets component requirement | NO/PARTIAL | HV source; HV electronic load; HV differential probes; HV DMM; insulation tester; interlocks; emergency stop; barriers/PPE; TC as required | ISO 21498-2:2024 |

## Recommended execution order with the current bench

1. **Baseline characterization:** PS-001…PS-007.
2. **Dynamic behavior:** PS-008…PS-013.
3. **Protection and fault injection:** PS-014…PS-020.
4. **Automotive supply profiles:** AUTO-001…AUTO-017, beginning with non-destructive ramps before severe pulses.
5. **Temperature corners:** TH-001…TH-005 and TH-008, repeating the most important baseline/dynamic tests.
6. **Endurance:** LIFE-001…LIFE-003 after short-duration validation has passed.
7. **Formal qualification:** TR-*, EMC-* and ENV-* with compliant equipment or an accredited laboratory.

## Current bench coverage and main equipment gaps

The present programmable supply + electronic load + oscilloscope + thermal chamber can cover a large part of the characterization, dynamic, protection and thermal matrix. The most useful additions for automotive power-electronics work are:

- precision DMM and/or power analyzer;
- DC current probe plus calibrated low-ohmic shunt;
- thermocouple/data-logging system;
- automated fault-insertion relay/MOSFET box;
- 4-quadrant automotive battery simulator with arbitrary-waveform capability;
- ISO 7637 transient generator;
- CISPR 25 LISN/artificial network and EMI receiver;
- BCI RF generator/amplifier/injection probes;
- ISO 10605 ESD simulator;
- humidity chamber and mechanical shaker access for environmental qualification.

## Standards and references

1. **ISO 16750-1:2023** — General. https://www.iso.org/standard/77578.html
2. **ISO 16750-2:2023** — Electrical loads. https://www.iso.org/standard/76119.html
3. **ISO 16750-3:2023** — Mechanical loads. https://www.iso.org/standard/77579.html
4. **ISO 16750-4:2023** — Climatic loads. https://www.iso.org/standard/77580.html
5. **ISO 16750-5:2023** — Chemical loads. https://www.iso.org/standard/77581.html
6. **ISO 7637-1:2023** — Vocabulary/general considerations. https://www.iso.org/standard/83230.html
7. **ISO 7637-2:2011** — Electrical transient conduction along supply lines. https://www.iso.org/standard/50925.html
8. **ISO 7637-3:2016** — Transient coupling via non-supply lines. https://www.iso.org/standard/59603.html
9. **ISO 10605:2023** — Automotive ESD. https://www.iso.org/standard/79094.html
10. **ISO 11452-1:2025** — RF-immunity general principles. https://www.iso.org/committee/5383636/x/catalogue/
11. **ISO 11452-2:2019** — ALSE immunity. https://www.iso.org/standard/68557.html
12. **ISO 11452-4:2020** — Harness excitation / BCI. https://www.iso.org/standard/74108.html
13. **CISPR 25:2021** — Automotive radio disturbance. https://webstore.iec.ch/en/publication/64645
14. **ISO 21780:2020** — 48 V supply voltage. https://www.iso.org/standard/71607.html
15. **ISO 21498-2:2024** — Voltage class B component electrical tests. https://www.iso.org/standard/84542.html
16. **ISO 20653:2023** — Automotive IP protection. https://www.iso.org/standard/76116.html
17. **Keysight — DC-DC Converter Testing Fundamentals.** https://www.keysight.com/us/en/assets/3125-1397/application-notes/DC-DC-Converter-Testing-Fundamentals.pdf
18. **TÜV SÜD — VW 80000.** https://www.tuvsud.com/en-us/industries/automotive/automotive-testing-solutions/vw80000
19. **Weiss Technik — LV 124 overview.** https://backend.weiss-technik.com/webapp/weisstechnik/detailpages/environmental-simulation/LV124/Weiss-Technik-Technisches-Informationsblatt_LV-124.pdf

## Suggested repository additions

- `tests/*.yaml` — stimulus profiles, equipment requirements and acceptance limits;
- `profiles/` — CSV waveform definitions for crank, battery dips, ramps and generator-control profiles;
- `reports/` — test-report templates;
- `scripts/` — SCPI automation for source, load, oscilloscope and chamber;
- `requirements/` — project-specific limits mapped to matrix IDs.
