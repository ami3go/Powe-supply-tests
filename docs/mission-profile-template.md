# Automotive Power-Supply Mission Profile Template

_Last updated: 2026-09-21_

Use this document as the controlled project input from which lifetime, endurance, combined-corner and robustness-validation stresses are derived. Do not substitute generic standard durations for a project mission profile when a vehicle lifetime or reliability claim is being made.

## 1. Product and installation context

- Product / variant:
- Vehicle platform:
- Mounting location:
- Supply architecture: 12 V / 24 V / 48 V / voltage class B / isolated / bidirectional:
- Cooling concept:
- Safety relevance / ASIL allocation:
- Target vehicle life:
- Target operating hours:
- Target distance:
- Geographic / altitude envelope:

## 2. Electrical collective

Document time-at-level or cycle distributions for:

- supply voltage (minimum, nominal, maximum, overvoltage, undervoltage);
- load current and power;
- startup / shutdown / restart count;
- cold-crank and brownout events;
- load-dump / transient exposure counts where applicable;
- bidirectional power-flow duty where applicable;
- quiescent / key-off duration and network wake activity.

## 3. Thermal and climatic collective

- ambient-temperature histogram;
- case / coolant / baseplate temperature histogram;
- junction-temperature range and ΔTj cycle distribution for power modules;
- temperature ramp rates and soak durations;
- humidity / condensation exposure;
- biased-humidity exposure where service voltage is present;
- maximum operating altitude / minimum pressure;
- solar / under-hood / underbody location modifiers.

## 4. Mechanical and chemical collective

- vibration spectra and duration by axis;
- mechanical-shock counts;
- free-fall / handling assumptions;
- ingress / splash / immersion exposure;
- fluid / salt / corrosion exposure.

## 5. Operating-state model

List the fraction of life and transition counts for OFF, sleep, wake, startup, normal run, degraded mode, shutdown, service / reflash and fault-recovery states.

## 6. Failure-mechanism / knowledge matrix

For every dominant mechanism record:

| Mechanism | Stress driver | Affected component / interface | Existing evidence | Test-to-pass row | Test-to-fail / margin row | Required margin |
|---|---|---|---|---|---|---|
| Example: capacitor wear-out | ripple current + temperature | output bulk capacitor | supplier life model | LIFE-004 | LIFE-005 / RV-001 | project-defined |

## 7. Derived validation quantities

Derive and document, rather than assume:

- LIFE-001 operating-life duration and acceleration rationale;
- LIFE-004 capacitor-life calculation inputs;
- TH-005 temperature-cycle count and dwell/ramp parameters;
- LIFE-006 junction-temperature power-cycle count when applicable;
- RV-001 margin targets and step-stress stop criteria;
- combined-corner combinations and exposure time;
- sample count and rationale.

## 8. Traceability

Every derived stress shall link:

mission-profile datum → requirement / safety-analysis item → matrix test ID → executable test definition → evidence artifact → verdict.

Rows particularly dependent on this document are RV-001, LIFE-001, LIFE-004, LIFE-005, LIFE-006, TH-005, TH-008, ENV-006 and QUAL-001.
