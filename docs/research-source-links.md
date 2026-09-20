# Automotive Power-Supply Validation — Research Source Links

_Last verified: 2026-09-20_

This file is the link index for the deep research behind the automotive power-supply validation matrix in [`automotive-power-supply-test-matrix.md`](automotive-power-supply-test-matrix.md).

It intentionally prefers the standards publisher, OEM/laboratory overview, instrument manufacturer, or semiconductor manufacturer as the canonical link. Unofficial full-text mirrors of copyrighted standards are not treated as authoritative references.

## Standards, OEM requirements, test-equipment documentation and application material

| # | Category | Source / document | Main use in test plan | Access / status | Link |
|---:|---|---|---|---|---|
| 1 | ISO 16750 | ISO 16750-1:2023 — General | General automotive environmental-test framework and terminology | ISO official page; published standard | https://www.iso.org/standard/77578.html |
| 2 | ISO 16750 | ISO 16750-2:2023 — Electrical loads | Supply-voltage range, over/undervoltage, starting, interruption, ripple and other electrical-load tests | ISO official page; published standard | https://www.iso.org/standard/76119.html |
| 3 | ISO 16750 | ISO 16750-3:2023 — Mechanical loads | Vibration, mechanical shock and related mechanical qualification | ISO official page; published standard | https://www.iso.org/standard/77579.html |
| 4 | ISO 16750 | ISO 16750-4:2023 — Climatic loads | High/low temperature, cycling, humidity and climatic qualification | ISO official page; published standard | https://www.iso.org/standard/77580.html |
| 5 | ISO 16750 | ISO 16750-5:2023 — Chemical loads | Chemical exposure where the power-supply assembly is qualified as an automotive component | ISO official page; published standard | https://www.iso.org/standard/77581.html |
| 6 | ISO 7637 | ISO 7637-1:2023 — Vocabulary and general considerations | Definitions and framework for conducted/coupled transient testing | ISO official page; published standard | https://www.iso.org/standard/83230.html |
| 7 | ISO 7637 | ISO 7637-2:2011 — Electrical transient conduction along supply lines | Pulse 1/2/3/load-dump-type conducted transient immunity on 12 V / 24 V supply lines | ISO official page; published standard, confirmed current by ISO | https://www.iso.org/standard/50925.html |
| 8 | ISO 7637 | ISO 7637-3:2016 — Transient coupling via non-supply lines | Capacitive/inductive transient coupling to signal and I/O harness lines | ISO official page; published standard | https://www.iso.org/standard/59603.html |
| 9 | ESD | ISO 10605:2023 — Automotive electrostatic discharge | Component and vehicle ESD test methods | ISO official page; published standard | https://www.iso.org/standard/79094.html |
| 10 | RF immunity | ISO 11452-1:2025 — General principles and terminology | General component RF-immunity framework | ISO official page; published standard | https://www.iso.org/standard/83225.html |
| 11 | RF immunity | ISO 11452-2:2019 — Absorber-lined shielded enclosure | Radiated RF immunity of automotive components | ISO official page; current published edition while a replacement project is under development | https://www.iso.org/standard/68557.html |
| 12 | RF immunity | ISO 11452-4:2020 — Harness excitation methods | Bulk-current-injection / harness-coupled RF immunity | ISO official page; published standard | https://www.iso.org/standard/74108.html |
| 13 | EMC emissions | CISPR 25:2021 — Radio disturbance characteristics | Conducted and radiated emissions for protection of on-board receivers | IEC official page; published standard | https://webstore.iec.ch/en/publication/64645 |
| 14 | 48 V systems | ISO 21780:2020 — Supply voltage of 48 V | 48 V automotive electrical requirements and tests | ISO official page; published standard, confirmed current in 2026 | https://www.iso.org/standard/71607.html |
| 15 | High-voltage / Class B | ISO 21498-2:2024 — Electrical tests for voltage class B components | Electrical tests for components connected to EV voltage-class-B systems | ISO official page; published standard | https://www.iso.org/standard/84542.html |
| 16 | Environmental sealing | ISO 20653:2023 — Road-vehicle IP protection | Dust, water and enclosure ingress tests where required by component qualification | ISO official page; published standard | https://www.iso.org/standard/76116.html |
| 17 | OEM / LV 124 | TÜV SÜD — Volkswagen VW 80000 | Public overview of VW 80000 / LV 124 test families, including electrical E-01…E-22, climatic, mechanical and life tests | Public laboratory overview; not the licensed OEM specification itself | https://www.tuvsud.com/en-us/industries/automotive/automotive-testing-solutions/vw80000 |
| 18 | OEM / LV 124 | Weiss Technik — LV 124 Technical Information Sheet | Public overview of LV 124 environmental and electrical qualification | Public technical overview; not the licensed OEM specification itself | https://backend.weiss-technik.com/webapp/weisstechnik/detailpages/LV124/Weiss-Technik-Technical-information-sheet-LV-124.pdf |
| 19 | Test equipment | Keysight N6775A — 60 V, 5 A, 300 W DC power module | Defines source limits and features available in the present bench | Manufacturer product page | https://www.keysight.com/us/en/product/N6775A/dc-power-module-60v-5a-300w.html |
| 20 | Test equipment | Keysight N6791A — 60 V, 20 A, 100 W DC electronic-load module | Defines sink limits, CV/CC/CR/CP modes, slew rate and digitization capability | Manufacturer product page | https://www.keysight.com/us/en/product/N6791A/dc-electronic-load-module-1u-height-60-v-20-a-100w.html |
| 21 | Test equipment | Keysight N6700 Modular Power System Family — Specifications Guide | Accuracy, resolution, programming, measurement and load-module limits | Manufacturer technical specification | https://www.keysight.com/us/en/assets/9018-04533/technical-specifications/9018-04533.pdf |
| 22 | Test equipment | Keysight N6700C Series — User Guide | Remote control, list/ARB operation, triggering, logging and module behavior | Manufacturer user manual | https://www.keysight.com/us/en/assets/9018-50006/user-manuals/9018-50006.pdf |
| 23 | Application note | Keysight — DC-DC Converter Testing Fundamentals | Output accuracy, line/load regulation, efficiency, transient response, startup/shutdown, ripple/noise and inrush test methods | Manufacturer application note | https://www.keysight.com/us/en/assets/3125-1397/application-notes/DC-DC-Converter-Testing-Fundamentals.pdf |
| 24 | Application note | Keysight — Performing DC-DC Converter Test Using DC Power Analyzers | Practical DC/DC converter automation and characterization examples | Manufacturer application note | https://www.keysight.com/us/en/assets/7018-05723/application-notes/5992-2278.pdf |
| 25 | Application note | Keysight — How to Test DC-DC Converter Efficiency | Efficiency-test setup and supporting resources | Manufacturer use-case page | https://www.keysight.com/ca/en/use-cases/test-dc-dc-converter-efficiency.html |
| 26 | Reference design | Texas Instruments TIDA-00699 — Front End Power Supply Reference Design with Cold Crank Operation, Transient Protection, EMI Filter | Real automotive front-end example covering cold crank, reverse battery, ISO 7637 transients and CISPR 25 emissions testing | TI reference design with design guide and test data | https://www.ti.com/tool/TIDA-00699 |
| 27 | Standards discovery | ISO/TC 22/SC 32 catalogue — Electrical and electronic components and general system aspects | Check current editions, amendments and work items for automotive electrical/electronic component standards | ISO committee catalogue | https://www.iso.org/committee/5383636/x/catalogue/ |

## Notes on use

- The links above are references for planning and traceability. Exact severity levels, waveforms, source impedances, durations, repetition counts, functional-status classes and pass/fail criteria must come from the applicable licensed standard and the customer/OEM requirement.
- For ISO/IEC standards, the public publisher page normally exposes the title, edition, publication status and abstract; the full normative text is generally licensed material.
- `VW 80000` and `LV 124` public pages are useful for mapping test families, but they are not substitutes for the applicable controlled OEM specification.
- The N6775A/N6791A documentation is included because the matrix explicitly maps each test to what the existing N6700 bench can perform and where dedicated automotive transient, EMC, ESD, environmental or four-quadrant equipment is still required.

## Related project document

- [Automotive Power Supply Validation Test Matrix](automotive-power-supply-test-matrix.md)
