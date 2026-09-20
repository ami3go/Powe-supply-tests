# Automated Power-Supply Validation Bench — Test Coverage and Architecture

_Last updated: 2026-09-20_

## Purpose

This document assesses how much of the automotive power-supply validation matrix can be automated with the following bench:

- Ethernet-controlled thermal chamber
- Keysight N6700-series programmable power supply
- Programmable electronic load
- Tektronix DPO4000-series oscilloscope
- Relay/fault-injection board able to connect/disconnect power, load, and individual wiring, and to apply controlled short circuits

The intent is to turn the bench into an unattended electrical/thermal validation station with repeatable fault injection, synchronized waveform capture, evidence collection, and safe recovery.

## Overall automation potential

The current validation matrix contains 100 test rows. The highest automation potential is in DC characterization, dynamics, protection, automotive electrical disturbances, thermal testing, endurance, and selected functional-safety fault-injection work.

| Automation class | Approx. tests | Meaning |
|---|---:|---|
| Directly automatable | 36 | Can run unattended after one-time DUT wiring/probe setup |
| Automatable with small fixture/capability additions | 18 | Requires relay topology, additional measurement range, second source/channel, or similar minor additions |
| Partially automatable | 27 | Software can orchestrate and capture evidence, but specialized equipment or manual fault setup is still required |
| Not covered by this bench | 19 | Requires EMC, mechanical, hipot, ESD, humidity/ingress, or other dedicated facilities |

The practical result is that roughly half of the full matrix can be highly automated, and the most frequently repeated design-verification tests are concentrated in that group.

## Coverage by test family

| Family | Total | Direct automation | Easy / conditional | Partial | Not covered |
|---|---:|---:|---:|---:|---:|
| PS electrical | 31 | 21 | 4 | 6 | 0 |
| AUTO automotive electrical | 20 | 5 | 7 | 6 | 2 |
| ISO transient TR | 6 | 0 | 0 | 2 | 4 |
| EMC | 8 | 0 | 0 | 1 | 7 |
| Thermal | 11 | 7 | 1 | 2 | 1 |
| Lifetime / endurance | 5 | 3 | 2 | 0 | 0 |
| Environmental / mechanical | 5 | 0 | 0 | 1 | 4 |
| 48 V | 1 | 0 | 1 | 0 | 0 |
| HV | 2 | 0 | 0 | 1 | 1 |
| Functional safety | 11 | 0 | 3 | 8 | 0 |

## Highest-priority tests to automate

| Tests | Automated activity |
|---|---|
| PS-001 / PS-002 / PS-003 / PS-004 | Vin × load × temperature sweeps; calculate accuracy, line regulation, and load regulation |
| PS-005 | Full efficiency map over Vin × load × temperature |
| PS-007 | Automated scope ripple/noise acquisition at each operating point |
| PS-008 | Electronic-load step generation; scope measures undershoot, overshoot, ringing, and settling |
| PS-009 | N6700 Vin step; scope captures output response |
| PS-010 | Controlled turn-on; capture startup, overshoot, inrush, and rise time |
| PS-011 | Controlled power removal; measure shutdown behavior and backfeed |
| PS-012 | Repeated power application; capture inrush |
| PS-013 | Repeated restart / hiccup cycles |
| PS-014 | Load ramp until current limit is detected |
| PS-015 | Controlled output short; capture current, Vout collapse, timing, and recovery |
| PS-019 | Automated supply disconnect / reconnect |
| PS-023 | Vin/load corner sweep while checking for oscillation |
| PS-024 | Controlled hot-plug with oscilloscope armed before switching |
| PS-025 | Switching-frequency extraction vs Vin/load/temperature |
| PS-026 | Vin ramp through dropout/UVLO and back |
| PS-029 | Automatic stress capture during severe tests |
| PS-031 | Multi-output load combinations when sufficient load channels are available |
| AUTO-001 | Long-term overvoltage at controlled temperature |
| AUTO-003 | Undervoltage dips |
| AUTO-007 | Slow decrease/increase profile |
| AUTO-009 | Detailed brownout/reset threshold mapping |
| AUTO-017 | High-cycle ON/OFF endurance |
| TH-001 / TH-002 | Hot/cold soak followed by automatic electrical tests |
| TH-003 | Automated load derating vs temperature |
| TH-004 | Automatic OTP trip/recovery threshold search |
| TH-005 | Temperature cycling with electrical checks |
| TH-008 | Electrical test suite repeated at temperature corners |
| TH-009 | Temperature stepping with functional verification |
| LIFE-001 / LIFE-002 / LIFE-003 | Long unattended endurance campaigns |

## Relay and fault-injection fixture

The relay board should be treated as a dedicated fault-insertion unit rather than only as a power switch.

A useful minimum topology is:

| Switch | Function | Main tests enabled |
|---|---|---|
| K1 | DUT VIN connect/disconnect | Startup, shutdown, interruptions, endurance |
| K2 | DUT GND connect/disconnect | Ground-pin interruption |
| K3 | Electronic-load connection | Load removal/application |
| K4 | Output-to-GND short | PS-015 and protection/recovery testing |
| K5 | Output/sense positive open | Sense/wiring fault |
| K6 | Output/sense negative open | Sense/ground fault |
| K7 | EN/Wake connect/disconnect | Startup, enable fault, recovery |
| K8 | Configurable fault path | Second input, feedback fault, redundant supply, other project-specific injection |

For a multi-pin automotive DUT, the preferred long-term design is a larger fault matrix in which every relevant supply pin, ground pin, sense line, and load path can be independently opened or rerouted.

## Mechanical relay versus fast solid-state switching

Mechanical relays are appropriate for:

- static disconnects;
- long-duration supply interruptions;
- power cycling;
- pin-open faults;
- load disconnect;
- persistent short circuits;
- galvanic isolation.

They are not sufficient for precise microsecond/sub-millisecond fault injection. The existing relay-control implementation is sequential and non-atomic, with switching commands on the order of tens of milliseconds. Therefore a second switching layer should be added for fast events.

Use MOSFET or other solid-state fault switches for:

- 10 µs / 100 µs / 1 ms / 10 ms supply interruptions;
- precise FTTI/FDTI/FRTI timing tests;
- synchronized short/open events;
- deterministic fault injection during startup or load transients.

The preferred architecture is therefore **mechanical relays for static/galvanic faults plus solid-state switches for deterministic fast faults**.

## Trigger and synchronization architecture

A hardware trigger path is preferable to relying on Ethernet/USB software latency for timing-critical tests.

```text
                    Test Controller
                         |
        +----------------+----------------+
        |                |                |
     Ethernet          Ethernet        Ethernet
        |                |                |
 Thermal chamber    N6700 + e-load     DPO4000
        |                |                |
        |                +---- Trigger ---+
        |                                 |
        +--------- Relay/Fault Controller
                          |
                       +--+--+
                       | DUT |
                       +-----+
```

A small deterministic fault controller can provide:

```text
TRIG OUT  --------> DPO4000 EXT TRIG
FAULT OUT --------> fast power/load fault switch
SYNC IN/OUT ------> N6700 trigger path
```

An RP2040-class controller is sufficient if the design includes deterministic GPIO timing, watchdog supervision, safe default outputs, and isolated interfaces where required.

This makes it possible to timestamp separately:

1. fault onset;
2. DUT fault detection;
3. protection reaction;
4. final safe/degraded state.

That timing model directly supports functional-safety reaction-time measurements.

## Automated thermal campaign example

A high-value campaign is a nested temperature/voltage/load sweep.

```text
Temperatures:
-40, -20, 0, +25, +60, +85 °C

At every temperature:

    Vin:
    minimum / nominal / maximum

        x

    Load:
    0 / 10 / 25 / 50 / 75 / 100 %

        x

    Run:
    - output accuracy
    - efficiency
    - ripple
    - switching frequency
    - startup
    - load transient
    - current limit
    - UVLO
    - shutdown
```

Six temperatures × three input voltages × six load points gives **108 steady-state operating points** before dynamic tests are added.

The controller should wait for chamber stabilization and soak before starting the electrical sequence, for example:

```text
abs(Tactual - Tset) <= temperature_tolerance
AND
stable_for >= soak_time
```

The complete electrical suite can then run without an operator present.

## Automated short-circuit sequence

A safe automatic PS-015 sequence can be implemented as follows:

```text
Set PSU voltage/current protection limits
Set electronic load OFF
Power DUT
Verify nominal Vout

Arm DPO4000 single acquisition

Trigger short-circuit switch

Measure:
    peak Iout
    peak Iin
    Vout minimum
    protection response delay
    hiccup period
    short-circuit steady current

Remove short

Measure:
    restart delay
    recovery overshoot
    final recovery state

Verify nominal Vout
Save waveform and measurements
Return bench to safe state
```

## Mandatory safety architecture for unattended fault testing

The relay/fault system should include hardware protections that do not depend on the automation PC:

- independent hardware current limiting/fusing;
- emergency disconnect;
- break-before-make switching rules;
- maximum short-circuit duration enforced in hardware;
- hardware watchdog that removes injected faults if the controller stops responding;
- normally safe relay states;
- interlocks preventing electrically incompatible relay combinations;
- auxiliary-contact or electrical continuity feedback;
- chamber over-temperature protection independent of test software;
- PSU and e-load safety limits configured before DUT connection.

Commanded relay state is not sufficient evidence that a contact actually changed. For unattended fault injection, the bench should verify the resulting electrical state or use relays/contactors with auxiliary contacts.

## Tests that remain outside this bench

The following areas still require specialized equipment or facilities:

| Area | Additional capability required |
|---|---|
| ISO 7637 standardized pulses | Dedicated transient generator / coupling network |
| Formal load dump | Defined load-dump generator and source impedance |
| High-frequency superimposed AC | Fast amplifier / 4-quadrant source and appropriate coupling hardware |
| CISPR 25 conducted emissions | Artificial network/LISN, EMI receiver, compliant setup |
| BCI immunity | RF generator, amplifier, injection/monitor probes, calibration fixture |
| Radiated immunity | ALSE chamber and RF system |
| ESD | ISO 10605 simulator and test setup |
| Insulation resistance | Insulation resistance tester |
| Dielectric withstand | Hipot tester and safety enclosure |
| Vibration / shock | Shaker / shock equipment |
| IP / fluid / salt / humidity-specific testing | Dedicated environmental facilities |

## Recommended automated bench state machine

Every automated test should run through a common safety state machine.

```text
BENCH SAFE
    |
Instrument self-check
    |
Relay/fault-state verification
    |
Chamber conditioning
    |
DUT pre-test parameter check
    |
Configure PSU/e-load
    |
Configure + arm oscilloscope
    |
Apply stimulus/fault
    |
Capture waveform + measurements
    |
Remove fault
    |
Verify recovery
    |
Post-test parameter check
    |
PASS / FAIL / ABORT
    |
Save raw evidence
    |
BENCH SAFE
```

Any communication error, failed precondition, chamber alarm, instrument protection event, watchdog timeout, or invalid relay state should force the bench back toward the safe state rather than continuing the campaign.

## Evidence package for every automated run

Each result should retain at least:

- test ID and test-definition version;
- DUT serial number and hardware/software revision;
- date/time and automation software commit;
- chamber setpoint, actual temperature, stability/soak data;
- PSU configuration and measured Vin/Iin;
- electronic-load configuration and measured V/I/P;
- oscilloscope acquisition configuration;
- raw oscilloscope waveform(s);
- calculated measurements;
- relay/fault state and injected-fault timing;
- acceptance limits;
- uncertainty/guard-band information where applicable;
- PSU/e-load/scope/chamber error queues and status;
- pre-test and post-test parameter checks;
- PASS / FAIL / ABORT verdict;
- defined final DUT state.

## Suggested unattended regression campaign

A practical overnight campaign could expose a configuration such as:

```text
DUT: Rev C / SN012
Campaign: Full Power Validation

Temperatures: -40 / +25 / +85 °C
Vin: minimum / nominal / maximum
Load: 0 ... 100 %

[x] DC characterization
[x] startup/shutdown
[x] load transients
[x] UVLO
[x] current limit
[x] short circuit
[x] power interruption
[x] sense-wire faults
[x] power cycling
[x] thermal protection
```

The output should be a machine-readable result set plus human-readable HTML/PDF summary, with links to raw waveforms and logs.

## Highest-value next hardware addition

Beyond the chamber, N6700, programmable load, DPO4000, and mechanical relay matrix, the highest-value addition is a **deterministic fast fault-injection controller with solid-state switches and hardware trigger outputs**.

This addition closes the gap between ordinary bench automation and precise automotive interruption/fault-timing work, and substantially improves the usefulness of the setup for functional-safety verification.

## Related project document

See also:

- [Automotive Power Supply Validation Test Matrix](automotive-power-supply-test-matrix.md)
