# Global Power Supply Validation Test Matrix

_Last updated: 2026-09-21 · cross-industry extension of the 121-row automotive matrix_

## Purpose

This document extends [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md) into a global, cross-industry validation matrix for electronic power supplies, converters, chargers, inverters, UPS systems, battery-backed supplies, DC/DC and AC/DC converters, power-conditioning electronics and powered equipment interfaces.

The detailed industry/standards discovery map is maintained in [`../docs/electronic-power-industry-coverage.md`](../docs/electronic-power-industry-coverage.md). The standards research index is maintained in [`global-power-supply-testing-standards-research-2026-09-21.md`](global-power-supply-testing-standards-research-2026-09-21.md).

> **Important:** exact voltage levels, waveforms, source impedances, durations, repetition counts, environmental severities, sample counts and acceptance criteria shall come from the exact applicable standard edition, customer specification and regulatory/contract basis. This matrix defines reusable test intent and traceability; it does not reproduce licensed normative text.

## Inheritance from the automotive matrix

The complete **121-row automotive matrix is part of this global matrix by inheritance**. It is not copied here verbatim because maintaining two physical copies would create revision drift. All rows `PS-*`, `AUTO-*`, `TR-*`, `EMC-*`, `TH-*`, `LIFE-*`, `ENV-*`, `48V-*`, `HV-*`, `FUSA-*`, `SYS-*`, `BI-*`, `RV-*` and `QUAL-*` from the automotive matrix remain applicable whenever the global row or product architecture calls for the same test primitive.

The global rows below add tests that are either absent from automotive validation or materially different because another industry defines a different power interface, failure mechanism, environment or qualification method.

### Bench legend

The intended reusable bench is the project setup: programmable Keysight N6700-series source/e-load capability, DPO4000 oscilloscope, Ethernet thermal chamber and relay/fault matrix.

- **A — Automatable:** normally executable with the existing bench, within voltage/current/power limits.
- **P — Partial:** bench supplies/loads/monitors the DUT but an additional fixture or instrument is required.
- **E — External:** formal test requires specialist equipment/facility.

### Qualification legend

- **CHAR** — characterization / engineering margin.
- **DV** — design verification.
- **TYPE** — formal type/qualification test where invoked.
- **PV** — production/periodic verification where required.
- **SAFETY** — potentially destructive safety/fault test; independent protection/interlocks required.

## Global test matrix

| ID | Domain | Test | Purpose / failure mechanism | Typical stimulus / conditions | Measure / record | Acceptance basis | Industries | Main standards / references | Qual. | Bench |
|---|---|---|---|---|---|---|---|---|---|---|
| GEN-001 | Input | AC/DC input operating range | Verify operation across the declared normal source range | Sweep minimum-to-maximum input voltage; for AC include frequency range and phase configuration | input V/I/P, output regulation, state/faults | Product/platform requirement | All electronic power | IEC 61204; IEC 62477-1; IEC 62040-3; IEC 62368-1; IEC 61010-1; sector standard | DV | A/P |
| GEN-002 | Input | Brownout / undervoltage boundary | Identify functional boundary and recovery during reduced supply | Slow and stepped reduction through normal, abnormal and shutdown bands | reset/off thresholds, hysteresis, output, restart | Governing product/platform standard | All | IEC 61000-4-11/-34; IEC 62040-3; SEMI F47; EN 50155; RTCA DO-160; automotive inherited rows | DV/TYPE | A/P |
| GEN-003 | Input | Short interruption / hold-up | Verify stored-energy ride-through and deterministic reset | Remove source for µs-to-s durations required by standard | hold-up time, output droop, reset, state recovery | Sector functional criterion | All; telecom; rail; medical; aviation; UPS | IEC 61000-4-11/-34; EN 50155; IEC 60601-1-2; RTCA DO-160; IEC 62040-3 | DV/TYPE | P |
| GEN-004 | Input | Frequency variation | Verify AC-input behavior over allowed source frequency | Sweep declared frequency range at min/nom/max voltage and load | output, input current, PF, faults | Product/platform requirement | AC equipment; UPS; marine; aviation | IEC 62040-3; IEC 60945; IEC 60092; RTCA DO-160 | TYPE | P |
| GEN-005 | Input | Phase loss / phase imbalance | Verify three-phase equipment under abnormal supply | Remove one phase; apply phase-voltage imbalance where applicable | currents, DC link, output, trip/recovery | Product/sector requirement | Industrial; semiconductor; drives; large UPS | IEC 61800; IEC 62477-1; SEMI F47/F49; IEC 61000-4-34 | DV/TYPE | P |
| GEN-006 | Input | Inrush / input current profile | Verify source, connector, fuse and rectifier stress | Energize at worst phase angle/voltage/temp; repeat starts | peak current, charge, I²t, settling | Product/standard limits | All | IEC 62040; ETSI EN 300 132; IEC 62368-1; IEC 62477-1 | DV/TYPE | P |
| GEN-007 | Output | Output accuracy and regulation | Verify steady-state output compliance | Load and line matrix at temperature corners | Vout/Iout, line/load regulation | Product requirement | All | IEC 62040-3; IEC 61204; IEC 62477-1 | CHAR/DV | A |
| GEN-008 | Output | Ripple / noise | Verify switching ripple and broadband noise | Min/nom/max input and load; all operating modes | pk-pk/RMS ripple, spectrum | Product/sector limit | All | IEC 61204-3; ETSI EN 300 132; telecom/OEM requirements | CHAR/DV | A/P |
| GEN-009 | Dynamic | Load transient | Verify control response to rapid demand changes | Defined load steps/slew at voltage/temp corners | overshoot, undershoot, settling, ringing | Product/platform limit | All | IEC 62040-3; IEC 61204; product standards | DV | A |
| GEN-010 | Dynamic | Line transient | Verify output stability during rapid source changes | Step/ramp source within non-destructive envelope | output excursion, recovery, faults | Product/platform limit | All | IEC 62040-3; EN 50155; RTCA DO-160; MIL-STD-704; MIL-STD-1275 | DV/TYPE | A/P |
| GEN-011 | Dynamic | Startup / sequencing | Verify monotonic startup and rail sequence | Power-on/enable at source/load/temp corners | rise time, overshoot, sequence, PGOOD | Product requirement | All | IEC 61204; IEC 62477-1; product standard | DV | A |
| GEN-012 | Dynamic | Shutdown / discharge | Verify controlled power-down and stored-energy discharge | Remove source/enable under min/max load | fall time, reverse current, residual voltage | Product/safety requirement | All; HV; EV; industrial | IEC 62477-1; ISO 6469-3; product standard | DV/SAFETY | A/P |
| GEN-013 | Protection | Overload/current limit | Verify limiting mode and thermal behavior | Increase load beyond rating at voltage/temp corners | limit current, Vout, temperature, recovery | Product/safety standard | All | IEC 61204-7; IEC 62477-1; IEC 62368-1; IEC 60601-1; IEC 61010-1 | DV/TYPE | A/P |
| GEN-014 | Protection | Output short circuit | Verify safe withstand and recovery | Low-ohmic short while off/running; required duration | peak/steady current, energy, temperature, restart | Safety/product standard | All | IEC 61204-7; IEC 62477-1; IEC 61558-1; IEC 62368-1 | SAFETY | P |
| GEN-015 | Protection | Output overvoltage protection | Verify downstream protection on control failure | Fault feedback or externally drive output where safe | trip level/time, clamp, latch/recovery | Safety/product requirement | All | IEC 62477-1; IEC 62368-1; IEC 60601-1; product standard | SAFETY | P |
| GEN-016 | Protection | Reverse energy / backfeed | Verify externally powered output or parallel-source behavior | Drive output/secondary source with input removed/low | reverse current, internal heating, rail voltage | Product/sector requirement | Telecom; redundant feeds; converters; vehicles; UPS | ETSI EN 300 132; IEC 62477-1; automotive inherited rows | DV | P |
| GEN-017 | Parallel operation | Current sharing | Verify load sharing between parallel modules | Parallel units at tolerance/temp corners; step load | current-share error, circulating current, stability | System specification | Telecom; data centre; redundant supplies | ETSI EN 300 132; IEC 62040-3; vendor/system standard | DV | P |
| GEN-018 | Redundancy | N+1 module removal / insertion | Verify uninterrupted service during module fault/service | Hot-remove/hot-insert one module at rated system load | bus excursion, share recovery, alarms | Availability requirement | Telecom; data centre; medical; industrial | IEC 62040-3; ETSI EN 300 132; system requirements | DV/TYPE | P |
| GEN-019 | Transfer | Alternate-source transfer | Verify transfer to battery, bypass or standby source | Fail primary source at multiple phase/load points | transfer time, output excursion, loss of function | Sector criterion | UPS; medical; emergency; nuclear | IEC 62040-3; IEC 60601/80601; IEEE/IEC 63332-387 | TYPE | P |
| GEN-020 | Efficiency | Efficiency / loss map | Determine operating losses and thermal worst case | Input × load × temperature sweep; bidirectional where applicable | Pin/Pout, efficiency, loss, temp | Product/energy requirement | All | IEC 62040-3; IEC 62477-1; product requirement | CHAR/DV | A |
| SAF-001 | Safety | Dielectric withstand | Verify insulation barrier withstand | Apply required AC/DC test voltage between prescribed circuits | leakage, flashover/breakdown | Exact product safety standard | All isolated/mains/HV | IEC 62368-1; IEC 61010-1; IEC 60601-1; IEC 61558-1; IEC 62477-1 | TYPE/SAFETY | E |
| SAF-002 | Safety | Insulation resistance | Detect moisture/contamination/insulation degradation | DC insulation test before/after environment | resistance, leakage trend | Product/platform standard | All isolated/HV; marine; nuclear | IEC 61558-1; IEC 60601-1; IEC/IEEE 62582-6; sector standard | TYPE | E |
| SAF-003 | Safety | Protective-earth continuity | Verify low-impedance fault-current path | Apply prescribed high current through PE path | resistance/voltage drop, heating | Safety standard | Mains industrial/medical/ICT | IEC 62368-1; IEC 61010-1; IEC 60601-1; IEC 62477-1 | TYPE | E |
| SAF-004 | Safety | Touch / leakage / patient current | Verify accessible-current limits | Measure required leakage networks in normal and single-fault conditions | touch/leakage/patient currents | Safety standard | Consumer; ICT; lab; medical | IEC 62368-1; IEC 61010-1; IEC 60601-1 | TYPE | E |
| SAF-005 | Safety | Abnormal operation / single fault | Verify no hazardous outcome after one credible fault | Short/open protective component; block fan; overload; control fault | temperature, smoke/fire, hazardous voltage, recovery | Product safety standard | All safety-regulated equipment | IEC 62368-1; IEC 60601-1; IEC 61010-1; IEC 60335-1; IEC 62477-1 | SAFETY | E/P |
| SAF-006 | Safety | Clearance / creepage / impulse coordination | Verify insulation geometry against working/transient voltage | Document measurement plus impulse withstand where required | distances, impulse result, PD if applicable | IEC/product safety standard | Mains; HV; industrial; rail | IEC 60664-1; IEC 62477-1; product standard | DV/TYPE | E |
| SAF-007 | Safety | Stored-energy accessibility | Verify capacitors/outputs discharge to safe levels | Remove input; measure energy/voltage vs time | residual voltage/energy, discharge time | Safety standard | Mains; HV; UPS; EV | IEC 62368-1; IEC 62477-1; ISO 6469-3 | TYPE | P/E |
| SAF-008 | Safety | Overtemperature / fire enclosure behavior | Verify safe response to thermal fault | Worst load/ambient; blocked cooling; component fault | hotspot temp, protection, enclosure behavior | Product safety standard | All | IEC 62368-1; IEC 60601-1; IEC 61010-1; IEC 60335-1; IEC 62477-1 | SAFETY | P/E |
| EMC-001 | EMC | Conducted emissions on AC/DC power ports | Measure noise injected into source wiring | Standard LISN/artificial network and receiver | spectrum vs limit | Applicable EMC/product standard | All | IEC 61204-3; CISPR 32; CISPR 25; IEC 60533; IEC 62236; IEC 61800-3 | TYPE | E |
| EMC-002 | EMC | Radiated emissions | Measure enclosure/harness radiation | Standard chamber/site, operating modes and load | field spectrum | Applicable limit | All | CISPR 32; CISPR 25; IEC 60533; IEC 62236; MIL-STD-461; ECSS-E-ST-20-07 | TYPE | E |
| EMC-003 | EMC | ESD immunity | Verify immunity to electrostatic discharge | Contact/air discharge to prescribed points/coupling planes | resets, errors, damage | Product/platform criterion | Consumer; ICT; medical; industrial; automotive | IEC 61000-4-2; IEC 60601-1-2; ISO 10605 | TYPE | E |
| EMC-004 | EMC | EFT/burst immunity | Verify fast repetitive power-port transients | Apply burst through coupling network | upset, reset, output disturbance | Product criterion | Mains/DC industrial; medical; charging | IEC 61000-4-4; IEC 60601-1-2; UNECE R10 where applicable | TYPE | E |
| EMC-005 | EMC | Surge immunity | Verify high-energy line transient withstand | Combination-wave surge at required modes/levels | clamp stress, function, damage | Product criterion | Mains; telecom; medical; industrial; charging | IEC 61000-4-5; IEC 60601-1-2; ITU-T K.20/K.21 | TYPE | E |
| EMC-006 | EMC | Conducted RF immunity | Verify RF entering through power/signal wiring | Inject swept RF with CDN/clamp/coupling method | output, errors, communications | Product criterion | ICT; telecom; medical; industrial; rail | IEC 61000-4-6; IEC 60601-1-2; IEC 62236 | TYPE | E |
| EMC-007 | EMC | Radiated RF immunity | Verify field immunity | Sweep required frequency/field/modulation | output, errors, resets | Product criterion | All | IEC 61000-4-3; IEC 60601-1-2; ISO 11452; MIL-STD-461; RTCA DO-160 | TYPE | E |
| EMC-008 | EMC | Power-frequency magnetic field | Verify immunity of sensors/protection to magnetic field | Apply calibrated magnetic field | errors, false trips, output | Product criterion | Medical; industrial; metering; automotive | IEC 61000-4-8; IEC 60601-1-2; ISO 11452-8 | TYPE | E |
| EMC-009 | Power quality | AC voltage dips / short interruptions | Formal immunity to grid disturbances | Apply specified residual voltage/duration/phase | function, reset, recovery | Product criterion | AC equipment; semiconductor; medical | IEC 61000-4-11; IEC 61000-4-34; SEMI F47 | TYPE | E/P |
| EMC-010 | Power quality | Harmonic current / flicker | Verify input current compatibility with public mains | Operate prescribed load states and measure harmonics/flicker | harmonic spectrum, Pst/Plt | Applicable limits | Consumer; ICT; lighting; appliances | IEC 61000-3-2; IEC 61000-3-3; product family | TYPE | E |
| BAT-001 | Battery | Charge performance / protection | Verify charge algorithm and protection boundaries | Charge at voltage/current/temp limits | charge current/voltage, cutoff, temp | Battery/application standard | Portable; industrial; medical; UPS | IEC 62133-2; IEC 62619; RTCA DO-311A | TYPE | P/E |
| BAT-002 | Battery | Discharge / capacity | Verify delivered capacity and low-voltage protection | Controlled discharge at required rates/temp | capacity, energy, cutoff, cell spread | Battery standard | Portable; industrial; aviation; BESS | IEC 62133-2; IEC 62619; RTCA DO-311A | TYPE | P |
| BAT-003 | Battery | External short circuit | Verify pack/cell protection and thermal safety | Apply prescribed low resistance | current, temperature, vent/fire, protection | Battery standard | Portable; industrial; aviation; BESS | IEC 62133-2; IEC 62619; RTCA DO-311A | SAFETY | E |
| BAT-004 | Battery | Overcharge / abnormal charge | Verify safe response to charger/BMS fault | Exceed normal charge condition as defined | V/I/temp, vent/fire, isolation | Battery standard | Portable; industrial; aviation; BESS | IEC 62133-2; IEC 62619; RTCA DO-311A | SAFETY | E |
| BAT-005 | Battery | Forced discharge / overdischarge | Verify reversal/deep-discharge safety | Force discharge beyond normal cutoff where required | cell voltage, temp, protection | Battery standard | Portable/industrial | IEC 62133-2; IEC 62619 | SAFETY | E |
| BAT-006 | Battery | BMS fault / contactor isolation | Verify detection and isolation of cell/sensor/contactor faults | Inject cell-voltage/temp/current sensor faults and contactor faults | detection time, isolation, pack voltage | BESS/product safety basis | BESS; EV; industrial storage | IEC 62933-5-2/-5-3; IEC 62619; UL 1973/9540 where applicable | SAFETY | P/E |
| TEL-001 | Telecom | -48 V DC operating range | Verify ICT equipment on telecom -48 V interface | Sweep normal/abnormal service voltage range at load/temp corners | input current, output, state | ETSI interface requirements | Telecom; networking; data centre | ETSI EN 300 132-2 | TYPE | A/P |
| TEL-002 | Telecom | -48 V inrush / current drain | Verify current profile does not destabilize plant | Energize at nominal/min/max interface voltage | peak/current-time profile, input collapse | ETSI requirement | Telecom; networking | ETSI EN 300 132-2 | TYPE | P |
| TEL-003 | Telecom | AC input interface | Verify ICT equipment on telecom AC feeds | Range, dips/interruptions, inrush as specified | input/output behavior | ETSI requirement | Telecom/data centre | ETSI EN 300 132-1 | TYPE | P/E |
| TEL-004 | Telecom | HVDC input up to 400 V | Verify high-voltage DC telecom/data-centre interface | Sweep normal/abnormal HVDC ranges; interruptions/inrush | input current, output, faults | ETSI/ITU requirement | Telecom/data centre | ETSI EN 300 132-3; ITU-T L.1200 family | TYPE | E |
| RAIL-001 | Rail | Rolling-stock supply range / changeover | Verify operation on train DC bus and source changeover | Apply supply range, variations and changeover cases | output/function/reset | Rail functional class | Railway; metro; tram | EN 50155; IEC 60571 | TYPE | P/E |
| RAIL-002 | Rail | Supply interruption | Verify ride-through/recovery for rail interruption classes | Apply prescribed interruption durations | output, reset, recovery | EN/IEC class | Railway | EN 50155; IEC 60571 | TYPE | P |
| RAIL-003 | Rail | Rail overvoltage / transient | Verify DC-bus disturbance withstand | Apply platform-defined overvoltage/transients | clamp, function, damage | Rail standard | Railway | EN 50155; EN 50163; IEC 60571 | TYPE | E |
| RAIL-004 | Rail | Rail EMC and powered vibration | Verify apparatus under railway EM/mechanical environment | EMC tests plus powered vibration/shock | errors, output, interruptions | Applicable rail criteria | Railway/infrastructure | IEC 62236 / EN 50121; IEC 61373; EN 50125 | TYPE | E |
| AVI-001 | Aviation | Aircraft power input | Verify equipment against aircraft AC/DC bus characteristics | Apply normal/abnormal voltage/frequency categories | output/function | Equipment category | Civil aviation | RTCA DO-160G/ED-14G Section 16 | TYPE | E |
| AVI-002 | Aviation | Voltage spike | Verify fast aircraft-bus spike immunity | Apply category-specific spike | upset/damage | Equipment category | Civil aviation | RTCA DO-160G Section 17 | TYPE | E |
| AVI-003 | Aviation | Audio-frequency conducted susceptibility | Verify power-input ripple susceptibility | Inject swept audio-frequency disturbance | function/output | Equipment category | Civil aviation | RTCA DO-160G Section 18 | TYPE | E |
| AVI-004 | Aviation | Rechargeable aviation battery qualification | Verify charge/discharge, abuse and containment | Execute battery qualification sequence | capacity, temp, vent/fire/containment | DO-311A | Civil aviation | RTCA DO-311A | TYPE/SAFETY | E |
| MIL-001 | Military aviation | Aircraft electric-power characteristics | Verify utilization equipment at platform power terminals | Apply normal/abnormal AC/DC characteristics by power type | function/output | MIL interface requirement | Military aviation/UAV | MIL-STD-704; MIL-HDBK-704-1…-8 | TYPE | E |
| MIL-002 | Military ground | 28 V vehicle input | Verify military vehicle DC input environment | Apply normal range, starting, surge, spike, ripple/noise | function/output/stress | Interface standard | Military ground vehicles | MIL-STD-1275F/current contract edition | TYPE | E/P |
| MIL-003 | Naval | Shipboard electric power | Verify naval utilization equipment power interface | Apply shipboard voltage/frequency variation, interruptions and transients | function/output | Interface standard | Naval/military marine | MIL-STD-1399-300-1 | TYPE | E |
| MIL-004 | Defence EMC | Conducted/radiated emissions and susceptibility | Verify mission equipment EMC | Execute applicable CE/CS/RE/RS methods | spectrum/function | Contract class | Defence electronics | MIL-STD-461 | TYPE | E |
| MAR-001 | Marine | Ship supply variation / failure | Verify operation during shipboard source variation and failure | V/f variation, interruption/failure at prescribed states | function/output/recovery | Marine equipment criterion | Commercial marine; navigation | IEC 60945; IEC 60092-504 | TYPE | E/P |
| MAR-002 | Marine | Shipboard EMC / low-frequency conducted immunity | Verify marine power/signal compatibility | IEC marine EMC methods on power/signal ports | emissions, susceptibility, function | IEC marine criteria | Marine/offshore | IEC 60533; IEC 60945 | TYPE | E |
| MAR-003 | Marine | IACS type-approval electrical/environmental sequence | Verify equipment under ship class environment | Power variation/failure plus temp, humidity, vibration, EMC | function before/during/after | IACS/class acceptance | Marine/offshore | IACS UR E10; DNV/ABS/LR/BV rules | TYPE | E |
| MAR-004 | Small craft | DC system / charger interaction | Verify onboard converter/charger with craft electrical installation | Battery/charger/shore-power conditions | V/I/backfeed/grounding | Small-craft standard | Marine leisure | ISO 13297; IEC 60945 where navigation equipment | DV/TYPE | P/E |
| MED-001 | Medical | Power input / basic safety | Verify ME equipment power behavior and basic safety | Rated range, abnormal/single fault, leakage/dielectric | essential performance, currents, temperature | IEC 60601-1 | Medical/life support | IEC 60601-1 | TYPE/SAFETY | E/P |
| MED-002 | Medical | Power-port EMC with essential performance | Verify essential performance during EMC disturbances | ESD, EFT, surge, RF, dips/interruptions | essential performance and recovery | IEC 60601-1-2 | Medical/life support | IEC 60601-1-2 | TYPE | E |
| MED-003 | Life support | Loss/change of electrical source | Verify ventilator/life-support operation during source loss/transfer | Remove/change external power; battery transition | alarms, continued operation, transfer time | Particular standard | Ventilators/life support | ISO 80601-2-12; IEC 60601-1-8 | TYPE | P/E |
| MED-004 | Imaging | Imaging high-power supply transients | Verify source during pulsed imaging load and line variation | Representative CT/X-ray/MRI/US operating cycles | DC-link/input current/output stability/temp | Particular standard/product requirement | Medical imaging | IEC 60601-2-44/-2-33/-2-54/-2-37 | TYPE | P/E |
| MED-005 | Implantable support | External programmer/charger source safety | Verify external accessories powering implant systems | Source fault, isolation, battery/charger abnormal states | currents, isolation, thermal behavior | Implant/product standard | Implantable medical | ISO 14708 series; applicable IEC 60601 | TYPE | E |
| IND-001 | Industrial | Machinery supply interruption / restart | Verify safe response of machine controls and power converters | Remove/reapply supply under operating states | stop category, restart, outputs | Machine/product requirement | Factory; packaging; textile; food; postal | IEC 60204-1 | DV/TYPE | P |
| IND-002 | Drives | Drive input/output power performance | Verify PDS over input/load/speed corners | Line/load changes and motor operating points | DC link, output current, trip, thermal | Drive specification | HVAC; robotics; pumps; machinery | IEC 61800-5-1; IEC 61800-3 | DV/TYPE | P/E |
| IND-003 | Drives | Regenerative / braking energy | Verify safe handling of returned energy | Command decel/overhauling load; line loss cases | DC-link rise, brake current, trip | Drive/system requirement | Elevators; cranes; robotics; machinery | IEC 61800; IEC 62477-1 | SAFETY | E/P |
| IND-004 | Converter safety | PECS abnormal operation | Verify generic power converter safety where no product standard exists | Overload, short, cooling loss, control fault | hazardous voltage/temp/fire/energy | IEC 62477-1 | Industrial converters; renewables; chargers | IEC 62477-1 | TYPE/SAFETY | E/P |
| IND-005 | PLC/control | 24 V supply immunity and retention | Verify controller/I/O behavior under DC variation/interruption | Sweep/interrupt 24 V control supply | outputs, retained state, diagnostics | Product standard | Industrial automation | IEC 61131-2; IEC 61010-2-201 | TYPE | A/P |
| IND-006 | ATE/lab | Measurement equipment source safety/immunity | Verify test equipment power behavior | Rated range, dips, surge/EFT/RF, single fault | measurement integrity, safety | IEC 61010/61326 | Laboratory; ATE; instrumentation; metrology | IEC 61010-1/-2-030; IEC 61326-1 | TYPE | E |
| EX-001 | Hazardous area | Intrinsic-safety power limitation | Verify circuit cannot release ignition-capable electrical energy | Worst supply/component faults with entity parameters | V/I/P, stored energy, temperatures | Ex ia/ib/ic requirements | Chemical; oil/gas; mining; hazardous equipment | IEC 60079-11; IEC 60079-25 | TYPE/SAFETY | E |
| EX-002 | Hazardous area | Increased-safety / encapsulated power equipment | Verify temperatures, clearances and fault behavior | Rated/abnormal operation in Ex construction | surface temp, insulation, fault outcome | Ex protection concept | Oil/gas; chemical; offshore | IEC 60079-7; IEC 60079-18; IEC 60079-0 | TYPE | E |
| EX-003 | Mining | Cap-lamp battery and supply safety | Verify underground portable lighting power system | Charge/discharge/fault/thermal/mechanical sequence | lamp function, battery safety, temp | Mining/caplamp standard | Mining/underground | IEC 60079-35-1; IEC 62133-2/62619 as applicable | TYPE | E |
| EX-004 | Hazardous area | Faulted barrier / associated apparatus | Verify external power fault cannot defeat intrinsic safety | Apply mains/DC faults to associated apparatus and barrier | IS-side energy/voltage/current | IEC 60079 requirement | Process/mining | IEC 60079-11/-25 | SAFETY | E |
| GRID-001 | Utility | Substation DC supply range / interruption | Verify IED/protection equipment on station battery systems | DC range, ripple, dips/interruptions, polarity where applicable | function, trip logic, communication | Utility equipment requirement | Electrical utilities; substations | IEC 61850-3; IEEE 1613; IEC 60255-26/-27 | TYPE | P/E |
| GRID-002 | Utility | Protection-relay power-port EMC | Verify relay immunity while preserving protection function | Surge/EFT/RF/ESD/dips on ports | protection operation, false trip, reset | IEC 60255 criterion | Utilities/grid | IEC 60255-26/-27 | TYPE | E |
| GRID-003 | Utility | Station battery charger / DC auxiliary performance | Verify charger, bus and battery coordination | Load steps, source loss, recharge, redundant charger failure | bus voltage, battery current, transfer | Station design standard | Utilities; nuclear conventional systems | IEEE 946; IEEE 485/1115; IEC 62040 where UPS | DV/TYPE | P/E |
| REN-001 | PV | PV inverter electrical safety | Verify converter safety across PV/DC-link conditions | Min/max DC, faults, insulation, thermal conditions | currents, isolation, protection | PV converter safety standard | Solar PV | IEC 62109-1/-2; IEC 62477-1 | TYPE/SAFETY | E |
| REN-002 | PV/grid | Anti-islanding / grid interaction | Verify converter response to grid loss/abnormal conditions | Grid voltage/frequency/load balance scenarios | trip time, current, reconnection | Grid/PV standard | Solar PV; distributed energy | IEC 62116; IEC 61727; IEEE 1547/UL 1741 where applicable | TYPE | E |
| REN-003 | Wind | Wind converter grid-disturbance behavior | Verify electrical characteristics under grid events | Voltage/frequency events and operating points | active/reactive power, current, recovery | Wind standard/grid code | Wind power | IEC 61400-21 series | TYPE | E |
| BESS-001 | Energy storage | PCS charge/discharge / four-quadrant operation | Verify bidirectional converter performance and transition | Charge/discharge sweeps, direction changes, grid/load transients | power, efficiency, DC/AC excursion | System requirement | BESS; microgrids | IEC 62933; IEC 62477-1; IEEE 1547 where grid connected | DV/TYPE | E/P |
| BESS-002 | Energy storage | Battery-system electrical safety | Verify industrial battery abnormal electrical conditions | Charge/discharge/short/overcharge as applicable | current, temp, protection, isolation | Battery/system standard | BESS; UPS; telecom | IEC 62619; IEC 62933-5-2/-5-3; UL 1973/9540 where applicable | SAFETY | E |
| BESS-003 | Energy storage | Loss of auxiliary power / black start | Verify controls/contactors/PCS recover after total auxiliary loss | Remove auxiliary and grid/source power; restore in defined sequences | boot, precharge, contactor state, bus voltage | System requirement | BESS; microgrid; emergency power | IEC 62933; project/grid requirements | DV | P/E |
| BUILD-001 | Fire safety | Fire-alarm PSU mains fail / battery transfer | Verify alarm system continues on standby battery | Remove mains at max alarm load; restore and recharge | bus voltage, transfer, alarm indication, autonomy | EN 54 requirement | Fire detection/alarm | EN 54-4; EN 54-2; EN 54-13 | TYPE | P |
| BUILD-002 | Security | Intrusion-system PSU standby / battery supervision | Verify standby source, charger and fault indication | Mains fail, battery low/open/short, load changes | autonomy, supervision, output | Security standard | Security/access | EN 50131-6; EN 50130-4 | TYPE | P |
| BUILD-003 | Emergency | Central emergency power transfer/autonomy | Verify central safety-services supply after mains failure | Fail mains at rated emergency load; duration test | transfer time, voltage/frequency, autonomy | Emergency supply standard | Buildings; tunnels; emergency systems | EN 50171; EN 50172 | TYPE | P/E |
| BUILD-004 | Emergency lighting | Emergency driver/battery operation | Verify luminaire operation on source loss | Remove normal supply; endurance/recharge sequence | light output, battery, transfer | Luminaire standard | Street/building/tunnel lighting | IEC 60598-2-22; IEC 61347 series | TYPE | P/E |
| BUILD-005 | Lighting | LED driver abnormal / dimming power behavior | Verify driver safety and regulation | Input range, output open/short, dimming, thermal fault | output current, temp, protection | Lighting controlgear standard | LED/stage/street/signage | IEC 61347-1; IEC 61347-2-13; IEC 62031 | TYPE | P/E |
| BUILD-006 | HVAC/appliances | Inverter appliance supply variation | Verify compressor/motor/control behavior during mains variations | Dips/restarts, line variation, load/temp corners | motor current, DC link, restart, thermal | Appliance/product standard | HVAC; home appliances; cold chain | IEC 60335-1; IEC 60335-2-40; IEC 60730-1; IEC 61800 | TYPE | P/E |
| SEMI-001 | Semiconductor | Voltage sag immunity | Verify process tool remains operational through common grid sags | Apply defined single/two-phase sag profiles; characterize three-phase where required by project | tool trip, subsystem dropout, recovery | SEMI F47 | Semiconductor manufacturing; ATE | SEMI F47; IEC 61000-4-34 methods as applicable | TYPE | E |
| SEMI-002 | Semiconductor | Subsystem sag localization | Identify which PSU/drive/RF subsystem causes tool dropout | Sag while instrumenting internal DC rails and interlocks | dropout point, rail collapse, trip chain | Tool robustness target | Semiconductor manufacturing | SEMI F47; SEMI F49; SEMI S22 | DV | E/P |
| PROC-001 | Welding | Welding power-source load / short / thermal test | Verify high-current source under welding duty and abnormal load | Standard duty cycles, open-circuit and short conditions | output V/I, temp, protection | Welding standard | Welding; plasma | IEC 60974-1; IEC 60974-10 EMC | TYPE | E |
| PROC-002 | Electroheating | Induction/electroheating power-converter safety | Verify high-frequency/high-power source under process load and faults | Rated process cycles, cooling loss, load mismatch/fault | V/I/P, temp, protection | Electroheating standard | Industrial heating; steel; induction | IEC 60519-1; IEC 60519-3; IEC 62477-1 | TYPE | E |
| PROC-003 | Electrolysis | Rectifier continuous-load / fault test | Verify high-current DC rectifier under cell-stack operating envelope | Current sweep, load change, stack open/short scenarios | current ripple, efficiency, thermal, protection | Process/product requirement | Electroplating; electrolysis; hydrogen | IEC 60146; IEC 62477-1; ISO 22734 for hydrogen systems | DV/TYPE | E |
| SPACE-001 | Space | Conducted emission/susceptibility on spacecraft power lines | Verify converter compatibility with spacecraft bus | ECSS-defined conducted EMC methods | spectrum, function, bus disturbance | ECSS requirement | Spacecraft; satellites; launch | ECSS-E-ST-20-07 | TYPE | E |
| SPACE-002 | Space | Power subsystem functional/performance verification | Verify power conversion/distribution across mission modes | Mission-mode load/source matrix including safe mode | bus V/I, efficiency, switching, fault recovery | Mission/ECSS requirements | Spacecraft/satellites | ECSS-E-ST-20; ECSS-E-ST-10-03 | DV/TYPE | P/E |
| SPACE-003 | Space | Thermal-vacuum powered operation | Verify converter in vacuum and mission thermal extremes | Powered hot/cold vacuum plateaus and cycles | output, temp, faults, drift | Qualification/acceptance level | Spacecraft/satellites | ECSS-E-ST-10-03; GSFC-STD-7000 | TYPE | E |
| SPACE-004 | Space | Powered vibration/shock functional checks | Verify no intermittent electrical failure through launch loads | Vibration/shock with pre/post and, where required, live monitoring | output interruptions, latch/faults | Qualification/acceptance level | Space/launch | ECSS-E-ST-10-03; GSFC-STD-7000 | TYPE | E |
| NUC-001 | Nuclear | Standby diesel start / acceleration | Verify emergency source starts on demand | Initiate start under required initial conditions | start time, speed, voltage/frequency | Nuclear standard/licensing basis | Nuclear | IEEE/IEC 63332-387; NRC RG 1.9 | TYPE/PV | E |
| NUC-002 | Nuclear | Sequential load acceptance | Verify standby source accepts safety loads in sequence | Apply prescribed load blocks/timing | V/f dip/recovery, current, engine/generator state | Licensing basis | Nuclear | IEEE/IEC 63332-387; NRC RG 1.9 | TYPE/PV | E |
| NUC-003 | Nuclear | Load rejection / recovery | Verify stability after sudden loss of load | Remove large load blocks | overspeed, V/f excursion, recovery | Licensing basis | Nuclear | IEEE/IEC 63332-387; IEEE 2420 | TYPE | E |
| NUC-004 | Nuclear | Standby endurance / capacity | Verify long-duration rated emergency operation | Rated load/endurance sequence | V/f, temperature, fuel/auxiliaries, failures | Licensing basis | Nuclear | IEEE/IEC 63332-387; IEEE 2420; NRC RG 1.9 | TYPE/PV | E |
| NUC-005 | Nuclear | Safety-related equipment environmental qualification | Verify powered electrical equipment after ageing/DBE environments | Qualified ageing plus environmental/accident simulation | function during/after exposure | Qualification programme | Nuclear | IEEE/IEC 60780-323 | TYPE | E |
| NUC-006 | Nuclear | Insulation condition monitoring | Trend insulation degradation and accident survivability | Insulation resistance per monitoring/accident sequence | resistance vs time/environment | Condition-monitoring criterion | Nuclear | IEC/IEEE 62582-6 | PV | E |

## Automotive coverage retained from the 121-row source matrix

The global matrix inherits the complete automotive groups below without changing their IDs or detailed stimulus definitions:

| Automotive group | Imported coverage | Principal standards |
|---|---|---|
| `PS-*` | DC characterization, regulation, dynamics, protection, stability, hot-plug, component stress | ISO 16750; product requirements; IEC 60664/62477 where HV isolation applies |
| `AUTO-*` | Long/transient OV/UV, jump start, load dump, superimposed AC, crank, interruptions, pin/connector faults, quiescent current | ISO 16750-2; LV 124/VW 80000; VDA/OEM requirements |
| `TR-*` | Automotive conducted transient immunity/emissions and generator verification | ISO 7637-2/-3/-5; ISO/TS 7637-4 |
| `EMC-*` | Conducted/radiated emissions, BCI, RF immunity, ESD, charging-line EFT/surge | CISPR 25; ISO 11452; ISO 10605; UNECE R10 |
| `TH-*` | Hot/cold operation, derating, cycling, humidity/condensation, combined corners | ISO 16750-4; LV 124 |
| `LIFE-*` | Operating life, cycling, robustness margin, power-module cycling, biased humidity | Mission-profile/OEM; AQG 324; AEC families |
| `ENV-*` | Vibration, shock, ingress, fluids, free fall, altitude | ISO 16750-3/-5; ISO 20653; IEC 60068 where applicable |
| `48V-*` | 48 V vehicle electrical architecture | ISO 21780; VDA 320/LV 148 |
| `HV-*` | Voltage-class-B, isolation, partial discharge, CMTI | ISO 21498; ISO 6469-3; IEC 60664-1; IEC 62477-1 |
| `FUSA-*` | Safety mechanisms, timing, latent faults, dependent failures, fault injection | ISO 26262 |
| `SYS-*`, `BI-*`, `RV-*`, `QUAL-*` | Fuse coordination, NVM integrity, realistic quiescent current, bidirectional faults, robustness, component qualification | ISO/OEM/AEC/mission-profile basis |

## Industry-family coverage

The detailed industries in `electronic-power-industry-coverage.md` map to the global matrix as follows. An individual product normally selects only the applicable rows.

| Industry family | Global rows |
|---|---|
| Consumer / mobile / wearables / gaming / AV | GEN-*, SAF-*, EMC-*, BAT-* |
| IT / data centre / banking / cyber infrastructure | GEN-*, SAF-*, EMC-*, TEL-*, BAT-* |
| Telecom / networking / cable / satellite ground | GEN-*, EMC-*, TEL-* |
| Automotive / EV / commercial vehicles / telematics | Inherited automotive rows + GEN-*/SAF-* where applicable |
| Commercial/off-highway/agricultural machinery | GEN-*, SAF-*, EMC-*, IND-* |
| Railway / metro / rail infrastructure | GEN-*, SAF-*, EMC-*, RAIL-* |
| Civil aviation / drones | GEN-*, SAF-*, EMC-*, AVI-*, BAT-* |
| Military aerospace / ground / naval / defence | GEN-*, EMC-*, MIL-* |
| Space / satellites / launch | GEN-*, SAF-*, SPACE-* |
| Marine / leisure / offshore / subsea | GEN-*, SAF-*, EMC-*, MAR-*, EX-* where hazardous |
| Medical / life support / imaging / implant accessories | GEN-*, SAF-*, EMC-*, MED-*, BAT-* |
| Industrial automation / robotics / logistics / material handling | GEN-*, SAF-*, EMC-*, IND-*, BAT-* |
| Oil / gas / chemical / petrochemical / fuel stations | GEN-*, SAF-*, IND-*, EX-* |
| Mining / underground / tunnels | GEN-*, SAF-*, EX-*, BUILD-* for emergency services |
| Utility / grid / substations / power generation | GEN-*, SAF-*, EMC-*, GRID-* |
| Renewable / solar / wind / hydro | GEN-*, SAF-*, EMC-*, REN-* |
| Energy storage / UPS battery systems | GEN-*, SAF-*, EMC-*, BAT-*, BESS-* |
| Nuclear | GEN-*, SAF-*, EMC-* as applicable + NUC-* |
| Building / HVAC / elevators / appliances / emergency systems | GEN-*, SAF-*, EMC-*, IND-*, BUILD-* |
| Semiconductor/electronics manufacturing / ATE | GEN-*, SAF-*, EMC-*, IND-*, SEMI-* |
| Welding / plasma / electroplating / electrolysis / hydrogen / industrial heating | GEN-*, SAF-*, EMC-*, PROC-* |
| Scientific/lab/metrology/field monitoring | GEN-*, SAF-*, EMC-*, IND-006, BAT-* as applicable |
| Outdoor/rescue/PPE/navigation/environmental monitoring | GEN-*, SAF-*, EMC-*, BAT-* plus product-specific radio/environmental standards |

## Standards families covered by the global matrix

The matrix now has explicit test rows or inherited automotive rows for the power-related content of these standard families:

- IEC 61204-3/-7; IEC 61558-1; IEC 62477-1; IEC 62040-1/-2/-3;
- IEC 62368-1; IEC 61010 family; IEC 60601/80601 family; IEC 60335/60730 family;
- IEC 61000-3-x / 4-x / 6-x and relevant CISPR product families;
- IEC 62133-2; IEC 62619; IEC 62933 series;
- ETSI EN 300 132-1/-2/-3; ITU-T L.1200; ITU-T K.20/K.21;
- ISO 16750; ISO 7637; ISO 21780; ISO 21498; ISO 6469; ISO 11452; ISO 10605; CISPR 25; UNECE R10; LV 124/VW 80000; VDA 320/LV 148;
- EN 50155; IEC 60571; IEC 62236/EN 50121; EN 50163; IEC 61373;
- RTCA DO-160G / EUROCAE ED-14G; RTCA DO-311A;
- MIL-STD-704 + MIL-HDBK-704 series; MIL-STD-1275; MIL-STD-1399-300-1; MIL-STD-461; MIL-STD-810 where environmental qualification applies;
- IEC 60945; IEC 60092; IEC 60533; IACS UR E10; ISO 13297;
- IEC 60079 series and IECEx/ATEX-adopted equivalents;
- IEC 60204-1; IEC 61131-2; IEC 61800-3/-5-1; IEC 61326-1;
- IEC 61850-3; IEEE 1613; IEC 60255-26/-27; IEEE 946/485/1115;
- IEC 62109-1/-2; IEC 62116; IEC 61727; IEC 61400-21; IEEE 1547/UL 1741 where invoked;
- EN 54-4; EN 50131-6; EN 50171/50172; IEC 60598-2-22; IEC 61347 series;
- SEMI F47/F49/S22;
- IEC 60974-1/-10; IEC 60519 series; IEC 60146; ISO 22734;
- ECSS-E-ST-20/-20-07/-10-03; GSFC-STD-7000;
- IEEE/IEC 63332-387; IEEE 2420; IEEE/IEC 60780-323; IEC/IEEE 62582-6; NRC RG 1.9.

Standards in the industry map that govern a broader product function but do **not** define a unique power-supply test are retained as supporting cross-references rather than being converted into artificial test rows. Examples include communication protocols, general functional-safety frameworks and equipment-specific mechanical standards.

## Mandatory execution metadata

Every executed global row shall record:

- applicable industry/product and exact standard edition/clause;
- DUT source topology and nominal voltage/frequency;
- operating mode and expected functional state;
- sample identity/count and pre/post parameter checks;
- stimulus generator configuration and verification status;
- raw measured values, limits, uncertainty/guard band and verdict;
- fault onset, detection, protection and recovery timing when applicable;
- instrument IDs/calibration/ranges/probe bandwidth;
- automation software version/commit and instrument error/status queues;
- evidence artifacts: waveforms, logs, chamber profile, EMC receiver files, photos and inspection results.

## Automation architecture

The global matrix intentionally separates **test intent** from **stimulus severity**. This allows the same automation primitives to be reused across industries:

```text
set_source_range()
set_load_state()
apply_voltage_profile()
apply_interruption()
apply_fault_matrix_state()
set_temperature()
wait_for_stability()
capture_scope()
measure_input_output()
read_dut_status()
evaluate_against_project_limit()
store_evidence()
```

Specialist generators (surge/EFT/ESD/RF/transient/HV), shakers, humidity/altitude/vacuum chambers and safety test equipment can be integrated as additional drivers without changing the requirement/test-ID model.

## Next engineering step

For machine execution, the next repository layer should split each applicable matrix row into:

```text
requirements/<project>.yaml
profiles/<standard-or-customer-waveform>.csv
tests/<global-test-id>.yaml
reports/<global-test-id>/...
```

The YAML must hold licensed/customer-specific severity and acceptance values outside this public generic matrix, while retaining the global test ID and standards traceability.