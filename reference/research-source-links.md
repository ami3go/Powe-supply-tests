# Automotive Power-Supply Validation — Research Source Links

_Last verified: 2026-09-20_

This file is the source/provenance index for the deep research behind [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md), including the later reference audit and the Keysight N6700 + N6775A + N6791A equipment mapping.

The index intentionally prefers standards publishers, OEM/laboratory overviews, instrument manufacturers, semiconductor manufacturers, or original/publisher bibliographic records. Unofficial full-text mirrors of copyrighted standards are not treated as authoritative references.

A source can be present here even when it is not cited in every matrix row: some sources were used to verify standard status, equipment capability, measurement limitations, or design-verification methods during the deep-search/review process.

## Standards and primary publisher pages

| # | Category | Source / document | Main use in test plan | Access / status | Link |
|---:|---|---|---|---|---|
| 1 | ISO 16750 | ISO 16750-1:2023 — General | General automotive environmental-test framework, operating modes, terminology and functional-status context | ISO official page; published standard | https://www.iso.org/standard/77578.html |
| 2 | ISO 16750 | ISO 16750-2:2023 — Electrical loads | Direct-current supply ranges; overvoltage; jump start; superimposed alternating voltage; slow decrease/increase; interruptions; reset; starting profile; load dump; reverse voltage; ground offset; open circuit; short circuit; withstand voltage; insulation resistance | ISO official page; published standard | https://www.iso.org/standard/76119.html |
| 3 | ISO 16750 | ISO 16750-3:2023 — Mechanical loads | Vibration, mechanical shock, free fall and related mechanical qualification | ISO official page; published standard | https://www.iso.org/standard/77579.html |
| 4 | ISO 16750 | ISO 16750-4:2023 — Climatic loads | High/low temperature, temperature steps/cycling, humidity, condensation and climatic qualification | ISO official page; published standard | https://www.iso.org/standard/77580.html |
| 5 | ISO 16750 | ISO 16750-5:2023 — Chemical loads | Chemical exposure where the power-supply assembly is qualified as an automotive component | ISO official page; published standard | https://www.iso.org/standard/77581.html |
| 6 | ISO 7637 | ISO 7637-1:2023 — Vocabulary and general considerations | Definitions and framework for conducted/coupled transient testing | ISO official page; published standard | https://www.iso.org/standard/83230.html |
| 7 | ISO 7637 | ISO 7637-2:2011 — Electrical transient conduction along supply lines | Supply-line transient pulses 1/2/3 and DUT-generated transient-emission measurement. Load-dump pulses 5a/5b and the old starting pulse were removed from this edition and are handled by ISO 16750-2 | ISO official page; published standard; confirmed current by ISO | https://www.iso.org/standard/50925.html |
| 8 | ISO 7637 | ISO 7637-3:2016 — Transient coupling via non-supply lines | Capacitive/direct-capacitive/inductive transient coupling to signal and input/output harness lines | ISO official page; published standard | https://www.iso.org/standard/59603.html |
| 9 | Electrostatic discharge | ISO 10605:2023 — Automotive electrostatic discharge | Component and vehicle electrostatic-discharge test methods | ISO official page; published standard | https://www.iso.org/standard/79094.html |
| 10 | Radio-frequency immunity | ISO 11452-1:2025 — General principles and terminology | General component radio-frequency immunity framework | ISO official page; published standard | https://www.iso.org/standard/83225.html |
| 11 | Radio-frequency immunity | ISO 11452-2:2019 — Absorber-lined shielded enclosure | Radiated radio-frequency immunity of automotive components | ISO official page; current published edition while a replacement project is under development | https://www.iso.org/standard/68557.html |
| 12 | Radio-frequency immunity | ISO 11452-4:2020 — Harness excitation methods | Bulk-current-injection / harness-coupled radio-frequency immunity | ISO official page; published standard | https://www.iso.org/standard/74108.html |
| 13 | Radio-frequency immunity | ISO 11452-8:2015 — Immunity to magnetic fields | Low-frequency/narrowband magnetic-field immunity; radiating-loop and Helmholtz-coil context for EMC-008 | ISO official page; published edition, revision under development | https://www.iso.org/standard/59605.html |
| 14 | Radio-frequency immunity | ISO 11452-9:2021 — Portable transmitters | Close-proximity portable-transmitter immunity for EMC-007 | ISO official page; published standard | https://www.iso.org/standard/76117.html |
| 15 | Electromagnetic emissions | CISPR 25:2021 — Radio disturbance characteristics | Conducted and radiated emissions for protection of on-board receivers; basis for formal emissions and pre-compliance work | IEC official page; published standard | https://webstore.iec.ch/en/publication/64645 |
| 16 | 48-volt systems | ISO 21780:2020 — Supply voltage of 48 V | 48-volt automotive electrical requirements, test profiles and functional-status framework | ISO official page; published standard, confirmed current in 2026 | https://www.iso.org/standard/71607.html |
| 17 | High-voltage / voltage class B | ISO 21498-2:2024 — Electrical tests for voltage class B components | Electrical behaviour/tests for components connected to electric-vehicle voltage-class-B systems | ISO official page; published standard | https://www.iso.org/standard/84542.html |
| 18 | High-voltage electrical safety | ISO 6469-3:2021 — Electrical safety | Electrical-safety requirements for voltage-class-B circuits; used to separate HV functional/electrical tests from isolation/discharge/interlock safety verification | ISO official page; published standard, revision under development | https://www.iso.org/standard/81746.html |
| 19 | Functional safety | ISO 26262-5:2018 — Product development at the hardware level | Hardware safety requirements, hardware integration/verification and safety-mechanism context for ASIL-relevant power supplies | ISO official page; published edition, revision under development | https://www.iso.org/standard/68387.html |
| 20 | Environmental sealing | ISO 20653:2023 — Road-vehicle ingress protection | Dust, water and enclosure ingress tests where required by component qualification | ISO official page; published standard | https://www.iso.org/standard/76116.html |
| 21 | Standards discovery | ISO/TC 22/SC 32 catalogue — Electrical/electronic components and general system aspects | Checking current editions, amendments and work items for automotive electrical/electronic component standards | ISO committee catalogue | https://www.iso.org/committee/5383636/x/catalogue/ |

## OEM, LV and vehicle-manufacturer requirement context

| # | Category | Source / document | Main use in test plan | Access / status | Link |
|---:|---|---|---|---|---|
| 22 | OEM / LV 124 | TÜV SÜD — Volkswagen VW 80000 | Public overview of VW 80000 / LV 124 test-family context | Public laboratory overview; not the controlled OEM specification | https://www.tuvsud.com/en-us/industries/automotive/automotive-testing-solutions/vw80000 |
| 23 | OEM / LV 124 | Weiss Technik — LV 124 overview page | Public overview of LV 124 scope and its relationship to OEM standards such as VW 80000 and BMW GS 95024-3-1 | Public technical overview; not the licensed LV 124 specification | https://www.weiss-technik.com/environmental-simulation/en/detailpages/lv-124 |
| 24 | OEM / LV 124 | Weiss Technik — LV 124 Technical Information Sheet | Public mapping of the 24 electrical tests E-01 through E-24 and environmental/lifetime groups; used heavily during the reference audit | Public technical information sheet; not the licensed LV 124 specification | https://backend.weiss-technik.com/webapp/weisstechnik/detailpages/LV124/Weiss-Technik-Technical-information-sheet-LV-124.pdf |
| 25 | 48-volt OEM context | testxchange — LV 148 and VDA 320 laboratory testing overview | Public context linking LV 148 and VDA 320 for 48-volt on-board electrical systems | Third-party laboratory/testing overview; planning aid only | https://www.testxchange.com/magazine/lab-testing-lv-148-en/ |
| 26 | 48-volt OEM context | GlobalSpec — VDA 320 catalogue entry | Bibliographic confirmation of VDA 320 title/scope for 48-volt on-board power-supply requirements and tests | Standards catalogue metadata; not the standard text | https://standards.globalspec.com/std/9974834/vda-320 |
| 27 | 48-volt / HV laboratory scope | Applus+ IMA / DAkkS accreditation annex | Independent laboratory scope showing VDA 320/LV 148 and LV 123-family automotive electrical test standards in accredited testing context | Public accreditation document; useful cross-check, not normative text | https://www.ima-dresden.de/files/2025/12/Applus-IMA-ISO-17025-Test-Laboratory-PL-13119-02-01-english-Annex.pdf |
| 28 | High-voltage OEM context | Applus+ IMA — LV 123 | Public laboratory page describing LV 123 as electrical characteristics and electrical safety of high-voltage components in road vehicles | Public laboratory overview; not the controlled OEM specification | https://www.ima-dresden.de/en/norm/lv-123/ |
| 29 | High-voltage OEM context | EMC Live — LV 123 test-requirements Q&A | Supporting context for proprietary OEM HV requirements and practical generation of some LV 123/VW high-voltage profiles | Third-party technical discussion; background only | https://emc.live/2019/test-requirements-lv123-qa/ |

## Keysight N6700 / N6775A / N6791A equipment sources

| # | Category | Source / document | Main use in test plan | Access / status | Link |
|---:|---|---|---|---|---|
| 30 | Test equipment | Keysight N6775A — 60 V, 5 A, 300 W direct-current power module | Defines source voltage/current/power limits and source features available in the present bench | Manufacturer product page | https://www.keysight.com/us/en/product/N6775A/dc-power-module-60v-5a-300w.html |
| 31 | Test equipment | Keysight N6791A — 60 V, 20 A, 100 W direct-current electronic-load module | Defines sink limits, constant-current/constant-voltage/constant-resistance/constant-power modes, slew control and digitization capability | Manufacturer product page | https://www.keysight.com/us/en/product/N6791A/dc-electronic-load-module-1u-height-60-v-20-a-100w.html |
| 32 | Test equipment | Keysight N6791A/N6792A Data Sheet | Low-voltage sink capability, current/voltage/power ranges, programming and measurement accuracy used to qualify the N6791A mapping | Manufacturer data sheet | https://www.keysight.com/zz/en/assets/7018-05460/data-sheets/5992-1880.pdf |
| 33 | Test equipment | Keysight N6700 Modular Power System Family — Specifications Guide | N6775A/N6791A accuracy, resolution, programming, measurement and module limits | Manufacturer technical specification | https://www.keysight.com/us/en/assets/9018-04533/technical-specifications/9018-04533.pdf |
| 34 | Test equipment | Keysight N6700C Series — User Guide | Remote control, list/arbitrary-waveform operation, triggering and external data logging; confirms the approximately 20-second internal FIFO and need for continuous computer retrieval | Manufacturer user manual | https://www.keysight.com/us/en/assets/9018-50006/user-manuals/9018-50006.pdf |
| 35 | Test equipment | Keysight — Power Products Solutions | Supporting overview of N6790-series integrated voltage/current measurement, simultaneous digitization and use without a separate digital multimeter for many production/characterization measurements | Manufacturer technical overview | https://www.keysight.com/us/en/assets/7018-01863/technical-overviews/5989-8853.pdf |
| 36 | Test equipment | Keysight — Understanding N6700C Measurement Accuracy | Explains integration time and how faster sampling changes measurement uncertainty; supports the precision-multimeter caveat in the matrix | Manufacturer technical article | https://www.keysight.com/blogs/en/tech/bench/2025/03/05/understanding-n6705c-measurement-accuracy |

## Converter characterization and automotive power-design references

| # | Category | Source / document | Main use in test plan | Access / status | Link |
|---:|---|---|---|---|---|
| 37 | Application note | Keysight — DC-DC Converter Testing Fundamentals | Output accuracy, line/load regulation, efficiency, transient response, startup/shutdown, ripple/noise and inrush-current methods | Manufacturer application note | https://www.keysight.com/us/en/assets/3125-1397/application-notes/DC-DC-Converter-Testing-Fundamentals.pdf |
| 38 | Application note | Keysight — Performing DC-DC Converter Test Using DC Power Analyzers | Practical DC/DC converter automation and characterization examples | Manufacturer application note | https://www.keysight.com/us/en/assets/7018-05723/application-notes/5992-2278.pdf |
| 39 | Application note | Keysight — How to Test DC-DC Converter Efficiency | Efficiency-test setup and supporting measurement guidance | Manufacturer use-case page | https://www.keysight.com/ca/en/use-cases/test-dc-dc-converter-efficiency.html |
| 40 | Reference design | Texas Instruments TIDA-00699 — Front End Power Supply Reference Design with Cold Crank Operation, Transient Protection and EMI Filter | Real automotive front-end example covering cold crank, reverse battery, conducted transients and CISPR 25 emissions work | TI reference design with design guide and test data | https://www.ti.com/tool/TIDA-00699 |
| 41 | Power-converter design | Analog Devices / Linear Technology AN88 — Ceramic Input Capacitors Can Cause Overvoltage Transients | Hot-plug input overshoot and input-network damping; basis for PS-024 | Original manufacturer application note | https://www.analog.com/media/en/technical-documentation/application-notes/an88f.pdf |
| 42 | Control-loop measurement | R. D. Middlebrook — Measurement of loop gain in feedback systems, International Journal of Electronics, 1975 | Closed-loop voltage/current injection methods and loop-gain measurement; basis for PS-021 | Publisher bibliographic/abstract page, DOI 10.1080/00207217508920421 | https://www.tandfonline.com/doi/abs/10.1080/00207217508920421 |
| 43 | Input-filter stability | R. D. Middlebrook — Input filter considerations in design and application of switching regulators, 1976 | Negative incremental input resistance / source-filter interaction and impedance-ratio stability criterion; basis for PS-023 | Bibliographic record for the original 1976 conference paper | https://cir.nii.ac.jp/crid/1571135651465028480 |

## Provenance notes

- The matrix was first built from the ISO/CISPR automotive electrical, EMC and environmental standards plus converter-characterization references, and then expanded through a deeper clause-by-clause audit.
- The later audit added or corrected control-loop stability, input-filter interaction, hot-plug overshoot, pre-biased startup, component stress/derating, short-to-battery, transient emissions, portable-transmitter immunity, magnetic-field immunity, condensation, 48-volt/high-voltage context and functional-safety coverage.
- The N6700 mapping was separately checked against Keysight N6775A/N6791A product documentation, the N6700 specifications guide and N6700C user guide. A separate electrical data logger is normally unnecessary when the control computer continuously retrieves external-log data, but a precision digital multimeter is still appropriate when the required uncertainty is tighter than the module specification or when measuring nodes outside the N6700 channels.
- The user-supplied matrix review and patch were also used as review inputs. Their technical claims were not treated as authoritative by themselves; important corrections were checked against the public sources above before being merged.
- LV 124, LV 148/VDA 320, LV 123 and VW standards are controlled OEM/industry documents. Public laboratory/vendor pages are included only for scope, nomenclature and test-family context. Project qualification shall use the exact controlled edition cited by the customer/OEM.
- Exact severity levels, waveforms, source impedances, durations, repetition counts, functional-status classes, sample counts and pass/fail criteria must come from the applicable licensed standard and product/customer requirement.

## Related project document

- [Automotive Power Supply Validation Test Matrix](automotive-power-supply-test-matrix.md)

## Extended research

- [Research Source Links v2](research-source-links-v2.md) — entries 44–91 from the 2026-09-21 second research pass.
- [Full Research Material Index](research-material-full-index.md) — complete research trail and provenance notes.
