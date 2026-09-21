# Automotive Power-Supply Validation — Research Source Links (v2)

_Last verified: 2026-09-21 · Extends [`research-source-links.md`](research-source-links.md) (entries 1–43, verified 2026-09-20)_

This revision keeps all 43 existing curated entries unchanged and adds **entries 44–91** found during a second research pass. It follows the provenance rules already established in the repository:

- Standards publishers, accreditation bodies, instrument and semiconductor manufacturers, and original bibliographic records are preferred.
- Unofficial full-text mirrors of copyrighted standards are not treated as authoritative.
- **No URL is invented.** Where a document is real but no stable public page was verified, the entry is listed with `— (no verified public URL; look up in the publisher catalogue)` rather than a plausible-looking guess.

New columns in this revision:

- **Access** — `Free` means the full document itself is publicly downloadable at no cost; `Catalogue` means only the abstract/metadata page is public; `Commercial` means paid.
- **Status** — publication status as verified on 2026-09-21.

---

## A. Standards and primary publisher pages — existing (1–21)

Unchanged from `research-source-links.md`. Re-verified 2026-09-21: **no status changes**. In particular CISPR 25:2021 Edition 5.0 remains current with no amendment, ISO 11452-2:2019 remains published pending replacement, and ISO 16750-1/-2/-3/-4/-5:2023 remain the published editions.

## B. OEM / LV context — existing (22–29)

Unchanged.

## C. Keysight N6700 / N6775A / N6791A equipment sources — existing (30–36)

Unchanged.

## D. Converter characterization references — existing (37–43)

Unchanged.

---

## E. NEW — Conducted transients: missing ISO 7637 parts

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 44 | **ISO/TS 7637-4:2020** — Electrical transient conduction along **shielded high-voltage supply lines** only | Conducted transient injection **and** measurement for equipment on >60 V DC to 1 500 V DC systems with supply isolated from the body (BEV/HEV/PHEV). Basis for proposed `TR-007`. | Catalogue | Published; **reviewed and confirmed 2024** | https://www.iso.org/standard/72067.html |
| 45 | **ISO 7637-5:2016** — Enhanced definitions and **verification methods for harmonisation of pulse generators** according to ISO 7637 | Verification of the ISO 7637-2 transient generator itself, so that `TR-001…TR-004` results are comparable between labs. Basis for proposed `TR-008`. | Catalogue | Published | — (no verified public URL captured; look up "ISO 7637-5:2016" in the ISO catalogue) |
| 46 | EMC Directory — *What is ISO 7637?* overview of parts 1–5 | Free orientation to how parts 1/2/3/4/5 divide the transient problem, and confirmation that ISO/TS 7637-4 first edition remains current | Free | Third-party overview; planning aid only | https://www.emc-directory.com/community/what-is-iso-7637-and-understanding-its-sub-parts-iso-7637-1-iso-7637-2-iso-7637-3-iso-7637-4-and-iso-7637-5 |

## F. NEW — EMC: missing ISO 11452 parts and regulatory layer

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 47 | **ISO 11452-10:2009** — Immunity to conducted disturbances in the **extended audio frequency range, 15 Hz – 250 kHz** | Per-lead conducted immunity on all power and output leads; distinct from the ISO 16750-2 §4.4 superimposed-AC test used by `AUTO-006`. Basis for proposed `EMC-009`. | Catalogue | Published; **reviewed and confirmed 2020** | https://www.iso.org/standard/42944.html |
| 48 | ISO 11452-10:2009 — published sample extract | Confirms 15 Hz–250 kHz range, audio oscillator, ≤2 Ω source impedance, isolation-transformer coupling and instrumentation requirements | Free (extract) | Publisher sample | https://cdn.standards.iteh.ai/samples/42944/bcb892b02a7248ea8dce10a1b7186747/ISO-11452-10-2009.pdf |
| 49 | **ISO 11452-11** — Reverberation chamber | Alternative to the ALSE method of `EMC-004`; **now recognised by UN R10 Rev 7**. Basis for proposed `EMC-011`. | Catalogue | Published | — (no verified public URL captured; look up in the ISO catalogue) |
| 50 | **ISO 11452-3 / -5 / -7** — TEM cell / stripline / direct RF power injection | Sub-200 MHz component immunity alternatives where ALSE is impractical; ISO 11452-2 itself points below 200 MHz to parts 4, 3 and 5. Basis for proposed `EMC-012`. | Catalogue | Published | — (no verified public URLs captured; look up in the ISO catalogue) |
| 51 | ATE Corp — ISO 11452 series overview | Free consolidated list of all ISO 11452 parts including -10 and -11, with severity-level context | Free | Third-party overview | https://www.atecorp.com/compliance-standards/iso/iso-11452 |
| 52 | **UN Regulation No. 10 (UNECE R10)** — Uniform provisions concerning the approval of vehicles with regard to electromagnetic compatibility | The type-approval regulation that gates market access. **Revision 7 in force 17 June 2025**; 07-series transition to **1 Sep 2029**. Adds DC-DC converter, on-board charger, REESS charging/driving-mode, BMS and WPT provisions; recognises ISO 11452-11; Annexes 15/16 add EFT-burst and surge. Basis for proposed `EMC-010`/`EMC-011`. | Free | Rev 7 current; Rev 6 approvals valid during transition | https://unece.org/fileadmin/DAM/trans/main/wp29/wp29regs/2015/R010r5e.pdf *(Rev 5 consolidated text — structural reference; obtain Rev 7 from the UNECE WP.29 catalogue)* |
| 53 | Applus+ Laboratories — *Key changes in ECE R.10 Revision 007* | Independent laboratory summary of what Rev 7 changed and why | Free | Laboratory publication | https://www.appluslaboratories.com/global/en/news/publications/key-changes-in-ece-r10-revision-007 |
| 54 | SAMD Solutions — ECE R10 type approval, detailed walkthrough | Identifies the two tests unique to R10 — Annex 15 EFT/burst (±2 kV, 5 ns/50 ns, 5 kHz) and Annex 16 surge (1.2/50 µs) — and the 1 Sep 2029 date | Free | Third-party technical article | https://samd-solutions.de/wissen/ece-r10-typgenehmigung/en.html |
| 55 | In Compliance Magazine — *Automotive EMC Testing: CISPR 25, ISO 11452-2 and Equivalent Standards, Part 1* | Maps CISPR/ISO/SAE automotive EMC standards against each other and explains ALSE/chamber rationale | Free | Trade publication | https://incompliancemag.com/automotive-emc-testing-cispr-25-iso-11452-2-and-equivalent-standards-part-1/ |
| 56 | **SAE J1113 series** (e.g. J1113-2, conducted immunity 15 Hz–250 kHz, cancelled Aug 2010) | US counterpart family to ISO 11452; J1113-2 was superseded by ISO 11452-10 — useful when a legacy customer specification still cites the SAE number | Commercial | J1113-2 cancelled; other parts active | https://webstore.ansi.org/standards/sae/sae11132010j1113 |
| 57 | Applus+ Keystone — ISO 11452-10 conducted immunity overview | Free description of setup, severity levels and applicability | Free | Laboratory overview | https://keystonecompliance.com/iso-11452-10/ |
| 58 | Applus+ Keystone — CISPR 25 conducted emissions overview | Confirms CISPR 25:2021 Ed 5.0 scope 150 kHz – 5 925 MHz, §6.3/§6.4 voltage (AN/LISN) and current-probe methods | Free | Laboratory overview | https://keystonecompliance.com/cispr-25-conducted-emissions/ |
| 59 | CISPR 25:2021 — published sample extract | Confirms fifth edition cancels and replaces the 2016 fourth edition; annex and uncertainty-budget structure | Free (extract) | Publisher sample | https://cdn.standards.iteh.ai/samples/103028/81d3c4d3a2484c4091f04f7305870091/CISPR-25-2021.pdf |

## G. NEW — Electric-propulsion environmental and HV electrical series

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 60 | **ISO 19453-1:2018** — Environmental conditions and testing for E/E equipment for **drive system of electric propulsion vehicles** — General | Voltage-class-B counterpart to ISO 16750-1. Note the series has **no Part 2**: electrical loads for class B are in ISO 21498-2. | Catalogue | Published | https://www.iso.org/standard/64930.html |
| 61 | **ISO 19453-3:2018** — Mechanical loads | Governs `ENV-001/-002/-005` for propulsion-system components instead of ISO 16750-3 | Catalogue | Published | https://www.iso.org/standard/65931.html |
| 62 | **ISO 19453-4:2018** — Climatic loads | Governs `TH-001…TH-011` for propulsion-system components instead of ISO 16750-4 | Catalogue | Published | https://www.iso.org/standard/65932.html |
| 63 | **ISO 19453-5:2018** — Chemical loads | Governs `ENV-004` for propulsion-system components | Catalogue | Published | — (no verified public URL captured; look up in the ISO catalogue) |
| 64 | **ISO 19453-6:2020** — Traction battery packs and systems | Applies if the converter is integrated into a traction battery pack or system | Catalogue | Published | https://www.boutique.afnor.org/en-gb/standard/iso-1945362020/road-vehicles-environmental-conditions-and-testing-for-electrical-and-elect/xs135285/132157 |
| 65 | Test-Navi — *Outline of ISO 19453* (English technical report) | Free summary of the four-part structure and why Part 2 is omitted; useful before buying the set | Free | Third-party technical report | https://www.test-navi.com/eng/report/pdf/OutlineOf_RoadVehicles-EnvironmentalConditionsAndTestingForElectricalAndElectronicEquipmentForDriveSystemOfElectricPropulsionVehicles_AndDescriptionOfRelatedProducts.pdf |
| 66 | **ISO 21498-1:2021** — Voltage class B — **Voltage sub-classes and characteristics** | Defines the sub-classes that determine which ISO 21498-2 levels apply to `HV-001`. Replaces ISO/PAS 19295:2016. Explicitly excludes electrical safety (points to ISO 17409 and the ISO 6469 series). | Catalogue | Published | https://www.iso.org/standard/78209.html |
| 67 | ISO 21498-1:2021 — published sample extract | Confirms sub-class rationale and the relationship to ISO 21498-2 | Free (extract) | Publisher sample | https://cdn.standards.iteh.ai/samples/78209/90efec1cdfcc44028ed656e46d057766/ISO-21498-1-2021.pdf |
| 68 | **ISO 17409** — Electrically propelled road vehicles — conductive power transfer — safety requirements | Named by ISO 21498-1 alongside ISO 6469 as the electrical-safety route excluded from 21498. Relevant to `HV-002`. | Catalogue | Published | — (no verified public URL captured; look up in the ISO catalogue) |

## H. NEW — Component and power-module qualification

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 69 | **AEC-Q100 Rev J** (11 Aug 2023) — Failure-mechanism-based stress-test qualification for integrated circuits | Grades 0–4 by ambient (Grade 0 −40…+150 °C through Grade 4 0…+70 °C); zero failures across three non-consecutive production lots. Anchors `PS-029` derating to a real component-qualification basis. Rev J made Q006 data mandatory and adjusted ESD targets for advanced CMOS. | **Free** | Current revision | http://www.aecouncil.com/Documents/AEC_Q100_Rev_J_Base_Document.pdf |
| 70 | **AEC document archive** — Q100, Q101, Q102, Q103, Q104, Q200 and sub-documents | Full free library. **AEC-Q101-006** (short-circuit reliability characterization of smart power devices for 12 V systems) is directly relevant to `PS-015`/`PS-030`; **AEC-Q104** covers multichip modules. | **Free** | Maintained | http://www.aecouncil.com/AECDocuments.html |
| 71 | AEC 2025 European Workshop — AEC-Q200 session | Records AEC-Q200 **Rev E** (2023) as current and Q200-001 Rev C expected 2025 | **Free** | Workshop material | http://www.aecouncil.com/files/Workshops/2025_European_AEC_Workshop/W2%20AEC%202025%20EU%20Workshop%20-%20Q200%20Workshop.pdf |
| 72 | Panasonic — *What is AEC-Q200?* | Notes that AEC-Q200 Rev E added test items for automotive fuses, and that jump-start and load-dump resistance are applied at passive-component level | Free | Manufacturer technical article | https://industrial.panasonic.com/ww/ds/ss/technical/b17 |
| 73 | MPS — *Fundamentals of AEC-Q100* webinar | Free orientation to the Q100/Q101/Q200 split and where AEC-Q101-006 sits | Free | Manufacturer webinar | https://media.monolithicpower.com/mps_cms_document/w/e/Webinar_-_Fundamentals_of_AEC-Q100-6Nov2018.pdf |
| 74 | **ECPE Guideline AQG 324** — Qualification of power modules for use in power-electronics converter units in motor vehicles | Based on the German OEM supply specification **LV 324**. Release **04.1/2025** (31 Mar 2025) is current: major SiC-annex additions (dynamic gate stress, dynamic reverse bias, dynamic H3TRB) and a fully revised Delta Qualification Matrix (DeQuMa). Supplies `PCsec`/`PCmin` power cycling, `HTS`/`LTS`, `HTRB`/`HTGB`/`H3TRB`. Basis for proposed `LIFE-006`/`LIFE-007`. | **Free (CC BY-ND)** | Rel. 04.1/2025 current | https://www.ecpe.org/research/working-groups/automotive-aqg-324/ |
| 75 | ECPE Guideline AQG 324 Release 03.1/2021 — full text | Previous release, useful for diffing against 04.1/2025 | **Free (CC BY-ND)** | Superseded | https://www.ecpe.org/index.php?eID=dumpFile&t=f&f=30359&token=cbab0d6a7844bb815684bcae699892313b924ddb |
| 76 | ECPE — *Guideline for Lifetime Calculation of Power Modules* (Annex of AQG 324) | Explains how power-cycling results verify a manufacturer lifetime model against a vehicle mission profile; pairs with `LIFE-004` | Free (record) | Published annex | https://www.researchgate.net/publication/357602459_Guideline_for_Lifetime_Calculation_of_Power_Modules_Annex_of_ECPE_GUIDELINE_AQG_324 |

## I. NEW — Robustness validation methodology

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 77 | **SAE J1211:2012** — Handbook for Robustness Validation of Automotive Electrical/Electronic Modules (joint SAE / ZVEI task force) | The framework `LIFE-005` and the combined-corner campaign are implicitly reaching for: mission profile → knowledge matrix → **test-to-fail** → margin mapping, replacing "fit for standard" with "fit for application". Basis for proposed `RV-001`. | Commercial | Current (2012 revision of the 2009 handbook) | https://www.sae.org/standards/j1211_200904-handbook-robustness-validation-automotive-electrical-electronic-modules/ |
| 78 | SAE J1211:2012 — published sample extract | Free excerpt covering the RV rationale and the history from J1211 NOV1978 | Free (extract) | Publisher sample | https://www.normsplash.com/Samples/SAE/171649667/SAE-J-1211-2012-en.pdf |
| 79 | **SAE J1879** — Handbook for Robustness Validation of Semiconductor Devices in Automotive Applications | Component-level companion to J1211; J1211 explicitly recommends it for the semiconductors used inside the module | Commercial | Published | — (no verified public URL captured; look up "SAE J1879" in the SAE catalogue) |
| 80 | ECPE / PSMA — *From Fit for Standard to Fit for Application* (E. Wolfgang) | Free presentation of the robustness-validation paradigm and the mission-profile concept | Free | Conference presentation | https://www.psma.com/sites/default/files/uploads/files/S8_1%20From%20Fit%20for%20Standard%20to%20Fit%20for%20Application;%20Wolfgang,%20ECPE.pdf |

## J. NEW — Isolation coordination and partial discharge

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 81 | **IEC 60664-1** — Insulation coordination for equipment within low-voltage systems: principles, requirements and tests | Clearance, creepage, pollution degree, overvoltage category and impulse-withstand basis for an isolated converter barrier. `AUTO-019`/`AUTO-020` verify resistance and withstand but not coordination. Basis for proposed `HV-003`. | Commercial | Published | — (no verified public URL captured; look up in the IEC webstore) |
| 82 | **IEC 62477-1** — Safety requirements for power electronic converter systems and equipment | Product-level safety standard for converters; applies IEC 60664-1 coordination in a converter context | Commercial | Published | — (no verified public URL captured; look up in the IEC webstore) |
| 83 | SAE 2013-01-1528 — *Application of Insulation Standards to High Voltage Automotive Applications* | Peer-reviewed treatment of adapting IEC 60664-1 (written for stationary mains equipment) to HV automotive components | Commercial | Published paper | https://saemobilus.sae.org/content/2013-01-1528/ |
| 84 | EEPower — *Essential considerations relating to partial discharge* | Free explanation of the insulation-coordination sequence and why a hipot pass does not exclude partial discharge | Free | Technical article | https://eepower.com/technical-articles/essential-considerations-relating-to-partial-discharge/ |
| 85 | Murata Power Solutions — *Partial discharge characteristics of different transformer insulation systems in DC-DC converters* | Directly on point: PD in DC-DC transformer insulation, why hipot misses it, and how barrier construction changes PD behaviour | Free | Manufacturer white paper | https://www.eenewseurope.com/en/white_papers/murata-power-solutions-partial-discharge-characteristics-of-different-transformer-insulation-systems-in-dc-dc-converters/ |

## K. NEW — Non-invasive control-loop stability measurement

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 86 | OMICRON Lab — *Traditional and Non-Invasive Stability Measurement* (Bode 100 application note) | Validates NISM against classical loop-gain Bode plots and shows the effect of output-capacitor ESR on phase margin. Basis for proposed `PS-032`. | Free | Application note v3.0 | https://www.omicron-lab.com/fileadmin/assets/Bode_100/ApplicationNotes/Noninvasive_Stability/App_Note_Traditional_NoninvasiveStability_V3.0.pdf |
| 87 | OMICRON Lab — *Output Impedance for Stability Analysis* | Method detail: output-impedance peaking → phase margin; records the practical validity ceiling (report ">70°" above roughly 65–70°) and the 25 mA DC load the method imposes | Free | Application note v1.1 | https://www.omicron-lab.com/fileadmin/assets/Bode_100/ApplicationNotes/Output_Impedance/AppNote_OutputImpedance_Stability_V1.1.pdf |
| 88 | Picotest — Non-Invasive Stability Measurement resource set (solution page, NISM manual v2.0, *Making Invasive and Non-Invasive Stability Measurements*) | Origin of the method (S. Sandler); minor-loop-gain basis makes it equally applicable to **input-filter interaction**, so it also supports `PS-023`. Now implemented in Bode 100/500, Keysight E5061B/ADS, R&S ZNL, Copper Mountain VNAs, Tektronix scopes and Cadence PSpice. | Free | Current | https://www.picotest.com/solutions/non-invasive-stability-measurement/ · https://www.picotest.com/wp-content/uploads/2024/05/NISM-Manual-v2.0-PSpice.pdf · https://www.picotest.com/wp-content/uploads/2024/06/Making-Invasive-and-Non-Invasive-Stability-Measurements.pdf |

## L. NEW — China market equivalents

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 89 | **GB 34660-2017** — Road vehicles — requirements and test methods of electromagnetic compatibility | **Mandatory** Chinese EMC standard for M/N/L vehicles and their E/E components; issued 2017-11-01, implemented 2018-01-01. Normatively references GB/T 18655, GB/T 21437.2 and the GB/T 33012/33014 series. | Commercial | Mandatory, current | https://www.chinesestandard.net/PDF/English.aspx/GB34660-2017 |
| 90 | **GB/T 28046.1-2011 … .5** — Road vehicles — environmental conditions and testing for E/E equipment | Chinese counterpart to ISO 16750. **Important:** these are MOD (modified) adoptions of **older** ISO editions — 28046.1 of ISO 16750-1:**2006**, 28046.3 of ISO 16750-3:**2007** — with documented technical deviations. Testing to ISO 16750:2023 does **not** automatically satisfy GB/T 28046. | Commercial | Valid | https://www.chinesestandard.net/PDF/GDOC.aspx/GBT28046.1-2011 |
| 91 | **GB/T 21437.x** (ISO 7637 counterpart), **GB/T 18655** (CISPR 25 counterpart), **GB/T 33014.x** (ISO 11452 counterpart) | Complete the China conducted-transient and EMC set referenced by GB 34660-2017 | Commercial | Valid | — (identified via the GB 34660-2017 normative reference list; obtain from the SAC/national catalogue) |

---


## M. NEW — OBC / conductive charging / V2G

| # | Source / document | Main use | Access | Status | Link |
|---:|---|---|---|---|---|
| 92 | **ISO 5474-1:2024** — Functional and safety requirements for power transfer — Part 1: General conductive power-transfer requirements | Current vehicle-side general charging/reverse-power-transfer basis; replaces the role previously covered by withdrawn ISO 17409:2020 | Catalogue | Published | https://www.iso.org/standard/81296.html |
| 93 | **ISO 5474-2:2024** — Part 2: AC power transfer | Vehicle-side AC conductive charging, including on-board charger configurations and reverse power transfer | Catalogue | Published; confirmed 2024 | https://www.iso.org/standard/81298.html |
| 94 | **ISO 15118-20:2022** — 2nd-generation V2G communication | Communication messages and sequences supporting bidirectional power transfer | Catalogue | Published; amendment exists | https://www.iso.org/standard/77845.html |
| 95 | **IEC 61851-21-1:2017** — On-board charger EMC requirements | Conductive charging EMC requirements for EV on-board charging units | Commercial catalogue | Published; IEC stability date 2026 | https://webstore.iec.ch/en/publication/32045 |
| 96 | **IEC 61000-4-27:2000+A1:2009+A2:2025** — Voltage-unbalance immunity | Three-phase OBC voltage-unbalance immunity method where within scope | Commercial catalogue | Current consolidated edition | https://webstore.iec.ch/en/publication/109827 |
| 97 | **IEC 61000-3-2:2018+A1:2020+A2:2024** — Harmonic current limits | Harmonic-current compliance for applicable chargers up to 16 A per phase | Commercial catalogue | Current consolidated edition | https://webstore.iec.ch/en/publication/92799 |
| 98 | **IEC 61000-3-3:2013+A1:2017+A2:2021** — Voltage changes/flicker | Flicker/voltage-fluctuation compliance for applicable chargers up to 16 A per phase | Commercial catalogue | Current consolidated edition; 2025 interpretation sheet incorporated | https://webstore.iec.ch/en/publication/68776 |
| 99 | **ISO 17409:2020** — Conductive power transfer safety requirements | Historical reference only; superseded by the ISO 5474 family | Catalogue | **Withdrawn** | https://www.iso.org/standard/72880.html |

---

## Provenance notes for v2

- Entries 44–91 were verified on 2026-09-21 against publisher catalogue pages, official association sites or accredited-laboratory publications. **Title, number, edition, date and publication status** were checked. Clause-level content was **not** read from paywalled text, and no clause numbers are asserted for any newly added standard.
- Entries 45, 49, 50, 63, 68, 79, 81, 82 and 91 name real documents for which no stable public URL was captured in this pass. They are listed deliberately **without** a link, consistent with the existing rule in `research-material-full-index.md` that links are never invented to fill a row.
- Four entries are genuinely **open-access full documents**, which is unusual in this field and worth flagging to anyone planning a budget: **AEC-Q100 Rev J and the whole AEC document archive** (69–71), and **ECPE AQG 324 under CC BY-ND** (74–75). These are complete normative-style documents, not abstracts.
- The UNECE R10 entry links the Revision 5 consolidated text only. That is a **structural** reference: it shows the annex layout and approval flow, but Revision 7 content must be obtained from the UNECE WP.29 catalogue. The Applus+ and SAMD entries (53, 54) summarise what changed.
- Chinese GB/T documents are distributed commercially through translation resellers rather than a free national portal; the links given are to the reseller catalogue records, not to authoritative government text.
- As in v1: LV 124, LV 148/VDA 320, LV 123, LV 324, VW 80000 and VW 80300 are controlled OEM documents. Public laboratory and vendor pages are cited only for scope, nomenclature and test-family context. Project qualification must use the exact controlled edition named in the customer contract.

## Related project documents

- [Automotive Power Supply Validation Test Matrix](automotive-power-supply-test-matrix.md)
- [Full research material index](research-material-full-index.md)
- [ISO 26262 ASIL test mapping](iso26262-asil-test-mapping.md)
- [Automated validation bench](automated-power-supply-validation-bench.md)
- [Deep review and gap analysis (2026-09-21)](deep-review-and-gap-analysis-2026-09-21.md)
- [Test matrix additions (2026-09-21)](test-matrix-additions-2026-09-21.md)
