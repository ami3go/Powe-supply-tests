# Deep Review and Gap Analysis — `ami3go/Powe-supply-tests`

_Review date: 2026-09-21 · Reviewed commit: `a4c4198` (2026-09-20 21:10 +0300) · 34 commits, 7 documents_

This review covers every file in the repository, cross-checks the four test artefacts against each other, and compares the standards coverage against the current published landscape. It is a companion to:

- [`research-source-links-v2.md`](research-source-links-v2.md) — updated research source index
- [`test-matrix-additions-2026-09-21.md`](test-matrix-additions-2026-09-21.md) — 21 proposed new test rows (+ `.csv`)
- [`check_matrix_consistency.py`](check_matrix_consistency.py) — the CI check the matrix asks for

---

## 1. What is in the repository

| File | Size | Content |
|---|---:|---|
| `README.md` | 1.7 kB | Project front page; lists **2** of the 7 documents |
| `docs/automotive-power-supply-test-matrix.md` | 88 kB | 100-row, 15-column validation matrix |
| `docs/automotive-power-supply-test-matrix.csv` | 75 kB | Machine-readable copy of the same 100 rows |
| `docs/iso26262-asil-test-mapping.md` | 62 kB | Revision 2 ASIL mapping, 20-item change log, classification scheme, 11 new-row outlines |
| `docs/iso26262-test-classification.csv` | 11 kB | Per-test CORE/ROB/TRIG/QUAL/SUPP classification |
| `docs/research-material-full-index.md` | 23 kB | 156-link research trail (43 Used / 8 Audit / 105 Supporting) |
| `docs/research-source-links.md` | 17 kB | 43-entry curated bibliography |
| `docs/automated-power-supply-validation-bench.md` | 14 kB | Bench automation architecture, relay topology, safety state machine |

### Overall assessment

This is a strong, unusually disciplined body of work. Three things in particular stand out and should be preserved in any future edit:

1. **Separation of method from limit.** Every row repeats that severities and pass/fail criteria come from the licensed standard and the customer specification. That is the correct posture for a public repository and it is applied consistently.
2. **Honest equipment mapping.** The N6775A/N6791A column says plainly where the bench *cannot* substitute for compliant equipment (3 mA current resolution vs microamp sleep current; no negative voltage; N6791A is not a hard short; not a load-dump generator). Most internal test plans overstate bench capability; this one does not.
3. **The ASIL revision was the right call.** Replacing Mandatory\*/Conditional\* with CORE/ROB/TRIG/QUAL/SUPP and graded cells (`REQ`, `++`, `T`, `—`) fixes a genuine misreading risk — the old scheme invited "run the 22 mandatory tests and we are compliant". `CHG-01`'s reasoning is sound.

The defects below are all fixable and none of them undermine the technical content.

---

## 2. Verified defects

### D-1 · Editorial style has diverged between the `.md` and the `.csv` (regression)

Commit `015136a` — *"Expand equipment names and remove short-form codes"* — deliberately removed abbreviations. Commit `bd9483f` — *"integrate 100-row power-supply validation matrix"* — reintroduced them into the Markdown only. The CSV, created at `569531d` from the expanded text, kept the long form. Measured occurrences at HEAD:

| Token | `.md` | `.csv` |
|---|---:|---:|
| `Vin` | 51 | 0 |
| `Vout` | 43 | 0 |
| `DUT` | 56 | 0 |
| `UVLO` | 6 | 0 |
| `DMM` | 9 | 0 |
| `PGOOD` | 5 | 0 |
| `ALSE` | 5 | 0 |
| `ESD` | 15 | 0 |

The two files are now in opposite editorial styles. A later commit silently undid an earlier deliberate one.

There is one inconsistency in the opposite direction too: the CSV expanded every abbreviation except `BCI`, which it keeps as a parenthetical after "bulk current injection". That form is fine; it is noted only because a naive style check will flag it.

**Recommendation.** Pick one style and generate the other file from it. Given that the CSV is the machine-readable artefact and the Markdown is the human-readable one, the cleanest rule is: abbreviations allowed in the `.md` **only after first expansion in the Scope section**, and the `.csv` generated from the `.md` by script so it can never drift again.

### D-2 · Test titles differ across the four artefacts

IDs are perfectly consistent — all four artefacts contain exactly the same 100 IDs, with no orphans in either direction. That is genuinely good. Titles are not.

- **15** titles differ between `matrix.md` and `matrix.csv`
- **16** titles differ between `matrix.md` and `iso26262-test-classification.csv`

(Counts after normalising case, whitespace and slash spacing. The raw count against the classification CSV is 17; one difference is pure spacing.)

Most are cosmetic (`ESD immunity` vs `electrostatic-discharge immunity`), but two are semantic:

| ID | `matrix.md` | `iso26262-test-classification.csv` |
|---|---|---|
| `FUSA-001` | Safety mechanisms (ASIL-relevant supplies) | Functional-safety mechanisms and fault reaction (**umbrella**) |
| `HV-001` | HV DC terminal electrical behavior | **Voltage-class-B** direct-current terminal electrical behavior |

`FUSA-001` matters: after `CHG-16` split it into `FUSA-002…009`, the classification CSV correctly reframes it as an umbrella row, but the matrix still describes it as a test. A reader working from the matrix alone will plan to execute `FUSA-001` as a discrete test.

`iso26262-asil-test-mapping.md` §10 states that row titles follow the matrix "to reduce naming drift". They currently do not.

### D-3 · The matrix asks for a CI check that would fail today

The matrix's own *Suggested next repository additions* asks for "automated consistency checks that fail CI on duplicate/missing IDs, inconsistent classifications, missing requirement links or incomplete evidence metadata."

That check is implemented and supplied as [`check_matrix_consistency.py`](check_matrix_consistency.py). Run against commit `a4c4198` from the repository root it **exits 1** with:

```
100 rows checked · 15 errors · 16 warnings
```

All 15 errors are the D-2 title drift. Everything else the checker tests **passes cleanly**, which is worth stating explicitly because it is the good news:

- no duplicate IDs;
- all four artefacts contain exactly the same 100 IDs, with no orphans in either direction;
- every row has exactly 15 columns;
- every ASIL cell uses a token from the declared legend;
- every row has a non-empty `Main reference`.

`--fix-csv` regenerates the CSV from the Markdown so the two can no longer diverge. This is the highest-value next commit in the repository and it is small.

### D-4 · `README.md` lists 2 of 7 documents

`iso26262-asil-test-mapping.md`, `iso26262-test-classification.csv`, `automotive-power-supply-test-matrix.csv`, `research-material-full-index.md` and `automated-power-supply-validation-bench.md` are all unlinked from the front page. The ASIL mapping is the single most substantial document in the repo (62 kB) and is discoverable only through an inline link inside the matrix.

### D-5 · The 156-link index is not reachable from the curated index

`research-source-links.md` does not link to `research-material-full-index.md`, although the full index links back to it. One-line fix.

---

## 3. Standards status — re-verified 2026-09-21

Every status claim in `## Standards status notes as of 2026-09-20` was re-checked. **No corrections needed.** Specifically confirmed still accurate:

- CISPR 25:2021 Edition 5.0 remains the current published edition (150 kHz – 5 925 MHz). No amendment.
- ISO 11452-2:2019 remains published while a replacement is in development.
- ISO 11452-8:2015 revision remains in progress.
- ISO 16750-1/-2/-3/-4/-5:2023 remain the published editions.

One addition worth recording: **ISO/TS 7637-4:2020 was reviewed and confirmed in 2024**, so it is current — relevant because it is a new recommended reference (§4.1 below).

---

## 4. Coverage gaps

The matrix is strong on ISO 16750, ISO 7637-2/-3, CISPR 25, ISO 11452-2/-4/-8/-9, ISO 10605, ISO 21780, ISO 21498-2 and LV 124/VW 80000. The gaps below are families that are *absent*, not rows that are merely thin.

### 4.1 · Conducted transients — two missing parts of ISO 7637

| Missing | Why it matters here |
|---|---|
| **ISO/TS 7637-4:2020** — transient conduction along *shielded high-voltage* supply lines (>60 V DC to 1 500 V DC, supply isolated from body); injection **and** measurement | `HV-001`/`HV-002` cover HV terminal behaviour and electrical safety but nothing covers HV conducted transients. For an HV→LV DC/DC this is the direct analogue of `TR-001…TR-004`. |
| **ISO 7637-5:2016** — enhanced definitions and **verification methods for harmonising pulse generators** | The matrix mandates measurement traceability (instrument ID, calibration, uncertainty) but never verifies the transient generator itself. Two labs with "compliant" ISO 7637-2 generators can produce materially different pulses; -5 exists precisely to close that. |

### 4.2 · EMC — ISO 11452 parts 3, 5, 7, 10 and 11 are all absent

Most significant is **ISO 11452-10:2009** (confirmed 2020): conducted immunity in the extended audio frequency range, **15 Hz – 250 kHz**, applied per-lead to all power and output leads.

This looks like `AUTO-006` (superimposed AC) but is not the same test. `AUTO-006` is an ISO 16750-2 §4.4 supply-quality test; ISO 11452-10 is an EMC immunity test with its own coupling arrangement (audio oscillator, ≤2 Ω source, isolation transformer, per-lead application) and its own severity levels. A converter can pass one and fail the other. The overlap should be *stated* in the matrix, not assumed away.

**ISO 11452-11** (reverberation chamber) has become materially more important — see §4.3.

### 4.3 · No regulatory type-approval layer at all — and UN R10 Rev 7 changed things

The repository maps to ISO/CISPR standards and OEM specifications but contains no reference to the regulation that actually gates market access. **UN Regulation No. 10 Revision 7 entered into force on 17 June 2025**, with the 07 series transition running to **1 September 2029**. Rev 7 is directly relevant to a power converter:

- It formally recognises the **ISO 11452-11 reverberation-chamber method** as an alternative to ALSE for ESA immunity.
- It adds provisions specifically covering **DC-DC converters, on-board chargers, REESS charging/driving modes, BMS immunity and wireless power transfer**.
- Annexes 15 and 16 specify **electrical fast transient / burst (±2 kV, 5/50 ns, 5 kHz)** and **surge (1.2/50 µs, ±2 kV line-to-earth, ±1 kV line-to-line on AC; ±0.5 kV on DC)** on charging lines. **Neither test exists anywhere in ISO 7637 or CISPR 25**, so a plan built only from ISO references will miss them entirely for any charging-coupled product.

### 4.4 · No electric-propulsion environmental series

**ISO 19453** parts 1, 3, 4, 5 (2018) and 6 (2020) are the voltage-class-B counterpart to ISO 16750 for electric-propulsion equipment. Note the deliberate structure: **there is no Part 2** — electrical loads for class B live in ISO 21498-2 instead. If the converter is an HV→LV unit inside the propulsion system, ISO 19453-3/-4/-5 govern its mechanical, climatic and chemical qualification rather than ISO 16750-3/-4/-5. `ENV-*` and `TH-*` currently cite only ISO 16750.

**ISO 21498-1:2021** (voltage sub-classes and characteristics; replaces ISO/PAS 19295:2016) is also missing — `HV-001` cites only Part 2, but Part 1 defines the sub-classes that determine which test levels Part 2 applies.

### 4.5 · Component-level qualification is never referenced

`PS-029` verifies derating against "component datasheets; company derating guideline", but nothing anchors the components themselves:

- **AEC-Q100 Rev J** (11 Aug 2023) — ICs; grades 0–3 by ambient; Rev J made Q006 data mandatory and adjusted ESD targets
- **AEC-Q101** (discretes) and **AEC-Q101-006** (short-circuit reliability of smart power devices for 12 V systems) — directly relevant to `PS-015`/`PS-030`
- **AEC-Q200 Rev E** (2023, passives; Rev C of Q200-001 expected 2025) — MLCCs, inductors, fuses; includes jump-start and load-dump resistance for some part types
- **AEC-Q104** (multichip modules)

All are **free downloads** from aecouncil.com. A Grade-1 part in a Grade-0 location is a classic silent gap that no bench test in the matrix would catch.

### 4.6 · No power-module qualification path

If any stage uses a power module, **ECPE Guideline AQG 324** applies. Release **04.1/2025** (31 Mar 2025) is current; it is **freely available under CC BY-ND**. It contributes tests the matrix has no equivalent for: `PCsec`/`PCmin` power cycling against a manufacturer lifetime model, `HTS`/`LTS`, `HTRB`/`HTGB`/`H3TRB`, and — new in 04.1/2025 — dynamic gate stress, dynamic reverse bias and dynamic H3TRB for SiC, plus a fully revised Delta Qualification Matrix.

`LIFE-002` ("power/thermal cycling", referenced only to "OEM reliability plan") is the natural anchor point.

### 4.7 · Methodological gap: test-to-pass vs test-to-fail

`LIFE-005` (over-limit step-stress margin) is the only row that measures *margin* rather than compliance, and it is graded `+` at every ASIL. The framework it belongs to is missing: **SAE J1211:2012 / ZVEI Handbook for Robustness Validation of Automotive Electrical/Electronic Modules** (and **SAE J1879** for semiconductors). J1211 supplies mission profile → knowledge matrix → test-to-fail → margin mapping. Given that the matrix already has a *Combined-corner campaign* section and mandatory pre/post-stress drift checks, it is most of the way to a robustness-validation plan without naming the method.

### 4.8 · Isolation is verified by hipot only

`AUTO-019` (insulation resistance) and `AUTO-020` (dielectric withstand) are pass/fail one-shot tests. For an isolated converter switching at tens of kHz with fast edges across the barrier, the wear-out mechanism is **partial discharge** in voids within the insulation system — which a hipot test passes without detecting. Insulation coordination per **IEC 60664-1** (clearance, creepage, pollution degree, overvoltage category, impulse withstand) and PD extinction-voltage measurement are the missing verifications.

### 4.9 · No China market path

**GB/T 28046.x** (MOD of ISO 16750), **GB/T 21437.x** (ISO 7637), **GB/T 18655** (CISPR 25), **GB/T 33014.x** (ISO 11452) and the mandatory **GB 34660-2017** are absent. Important practical point: the GB/T parts are *modified* adoptions of **older** ISO editions — GB/T 28046.1-2011 is MOD of ISO 16750-1:**2006**, GB/T 28046.3-2011 is MOD of ISO 16750-3:**2007** — with documented technical deviations. Testing to ISO 16750:2023 does not automatically satisfy GB/T 28046.

### 4.10 · Smaller method gaps

| Gap | Effect |
|---|---|
| Loop stability requires an injection point | `PS-021` is unexecutable on sealed PMICs, LDOs and multi-loop converters. Non-invasive stability measurement from output impedance solves this and needs no loop access. |
| MLCC DC-bias derating never verified | A 10 µF X7R can lose over half its capacitance at rated DC bias. This moves the `PS-021` crossover, the `PS-007` ripple and the `PS-008` transient — the three tests most likely to be re-run without re-checking effective capacitance. |
| No altitude / low-pressure test | Affects convective cooling **and** clearance withstand (both derate with altitude). |
| No NVM-write-during-brownout test | `AUTO-009` mentions NVM status but nothing injects an interruption during a flash write or OTA reflash. |
| Protection coordination with the vehicle fuse never verified | `PS-014`/`PS-015` test the converter's own limits in isolation, not whether it trips before or after the upstream fuse. |
| Bidirectional operation not covered | `48V-001` and `FUSA-011` assume unidirectional flow. A bidirectional 48 V↔12 V unit needs mode-transition, reverse-power and dual-source arbitration tests. |
| Audible noise | MLCC piezoelectric singing and magnetics noise are common late-stage NVH rejections, especially in pulse-skipping and light-load modes mapped by `PS-025`. |

---

## 5. Notes on the other documents

### `automated-power-supply-validation-bench.md`

Technically the strongest document in the repository. The mechanical-relay-vs-solid-state analysis is correct and unusually candid ("commanded relay state is not sufficient evidence that a contact actually changed"). Two observations:

- The automation-class totals sum to **36 + 18 + 27 + 19 = 100**, which matches the matrix. Good. But the per-family table sums to **PS 31 + AUTO 20 + TR 6 + EMC 8 + TH 11 + LIFE 5 + ENV 5 + 48V 1 + HV 2 + FUSA 11 = 100** as well, while the *columns* of that table sum to 36/18/27/19 only if read carefully — worth adding an explicit total row so a future edit cannot silently break it.
- The 21 rows proposed in the companion additions file change these totals. They are classified in that file so the counts can be updated in one pass.

### `iso26262-asil-test-mapping.md`

The change log discipline (CHG-01…CHG-20, each with rationale and references) is exemplary. §1 is appropriately honest that the clause-10 method grades are "the reviewer's reading of the 2018 text". Note that §1 records ISO/DIS 26262-5 registered 2026-08-04 and in enquiry — that should be re-checked periodically, since a published third edition would invalidate §3.3.

### `research-material-full-index.md`

The provenance note — that the original browsing session was not exported and the file therefore does not reconstruct the historical result set, and that no links were invented to hit a target count — is the right way to handle this. That discipline is carried into `research-source-links-v2.md`: where a document is real but I could not verify a stable public URL, it is listed **without** a URL rather than with a plausible-looking guess.

---

## 6. Recommended commit order

1. **Add the CI consistency check** — `check_matrix_consistency.py` is supplied (fixes D-3, prevents D-1/D-2 recurring). Generate the CSV from the Markdown with `--fix-csv`.
2. **Reconcile titles** across the four artefacts; fix `FUSA-001` to read as an umbrella row.
3. **Expand `README.md`** to list all documents.
4. **Merge the new sources** from `research-source-links-v2.md`.
5. **Merge the new rows** from `test-matrix-additions-2026-09-21.md`, taking only the families that apply to the actual product (HV, charging-coupled, bidirectional and power-module rows are conditional).
6. **Update the automation-class counts** in the bench document.
7. **Add a mission profile document.** Everything in §4.7 depends on one, and the matrix's `LIFE-001` and `LIFE-004` already reference "the mission temperature profile" and "LV 124 temperature collective" as if it existed.

---

## 7. Scope caveats for this review

- Public sources only. LV 124, LV 148/VDA 320, LV 123, VW 80000/80300, GMW3172 and equivalent OEM documents are controlled; nothing in this review reproduces or infers their content beyond what the publicly available laboratory and vendor overviews already state.
- ISO, IEC, SAE, AEC and GB documents were checked against publisher catalogue pages for **title, number, edition, date and status**. Clause-level content was not read from paywalled text and no clause numbers are asserted for the newly added standards.
- ASIL gradings proposed for the new rows follow the conventions already established in the repository and are, like the repository's own gradings, a reading to be confirmed against the licensed standard before use in a safety case.
