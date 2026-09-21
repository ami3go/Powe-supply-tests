#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TM = ROOT / "Test-matrix"
MD = TM / "automotive-power-supply-test-matrix.md"
CSV = TM / "automotive-power-supply-test-matrix.csv"
CLASS = TM / "iso26262-test-classification.csv"
MAP = TM / "iso26262-asil-test-mapping.md"
GLOBAL = TM / "global-power-supply-test-matrix.md"
TM_README = TM / "README.md"
ROOT_README = ROOT / "README.md"
BENCH = ROOT / "docs" / "automated-power-supply-validation-bench.md"
SOURCES = ROOT / "reference" / "research-source-links-v2.md"

ROWS = [
["CHG-001","Charging / OBC","AC input voltage and frequency operating range","Verify an on-board charger across the declared external AC supply envelope and identify transfer, derating and shutdown boundaries","Sweep rated single-phase or three-phase input voltage and frequency over the project range at light, nominal and full charging power and temperature corners","AC voltage/current/power, power factor, DC-link/HV output, charge power, state and faults","Charging function and protection remain within the product, market and vehicle requirements throughout the declared range","Additional equipment required","Programmable AC/grid simulator; HV battery simulator or regenerative DC load; precision power analyzer; isolation and safety interlocks; thermal chamber","N6700 can power low-voltage auxiliaries and controls only. It cannot emulate the mains input or traction-battery power path of a normal OBC.","++*","++*","++*","++*","ISO 5474-1:2024; ISO 5474-2:2024; IEC 61851-21-1:2017; product and market requirements"],
["CHG-002","Charging / OBC","AC brownout and voltage-dip immunity","Verify controlled charging behavior through reduced mains voltage without undefined state, unsafe current or corrupted charging control","Apply project/market voltage dips and reduced-voltage plateaus at several phase angles, loads and temperatures; include repeated dips near the charger dropout boundary","Input current, charge power, DC output, state transitions, diagnostics and recovery","Required charging state is maintained or exited deterministically; no unsafe current, latch-up or undefined recovery","Additional equipment required","Programmable AC/grid simulator with dip capability; HV battery simulator/load; oscilloscope; power analyzer","N6700 may support auxiliary rails and monitoring, but the AC disturbance requires a grid simulator or compliant immunity generator.","++*","++*","++*","++*","ISO 5474-2:2024; IEC 61000-4-11:2020 and IEC 61000-4-34 where applicable; vehicle/market requirement"],
["CHG-003","Charging / OBC","AC interruption and restart","Verify deterministic behavior and recovery after complete loss of external AC during charging","Interrupt one or all AC conductors for the required durations at multiple charging powers and phases of operation; restore the source with controlled phase and voltage","Hold-up, contactor state, DC-link decay, charge termination, restart delay, diagnostics and communication state","No unsafe energy transfer or contactor state; restart/recovery follows the specified sequence without corrupted state","Additional equipment required","Programmable AC/grid simulator or synchronized contactor; HV battery simulator/load; oscilloscope; communications monitor","N6700 can maintain low-voltage support if required, but it does not generate the AC interruption on the charger input.","++*","++*","++*","++*","ISO 5474-1:2024; ISO 5474-2:2024; IEC 61000-4-11:2020 / IEC 61000-4-34 as applicable; product requirement"],
["CHG-004","Charging / OBC","Three-phase phase loss and voltage unbalance","Verify that a three-phase OBC detects and safely handles a missing phase, phase-voltage unbalance and phase restoration","At representative charge powers remove each phase in turn and apply specified voltage unbalance; repeat during startup and steady charging","Per-phase voltage/current, neutral current where applicable, DC-link ripple, output power, diagnostics and recovery","No component overstress or uncontrolled current; defined derating/shutdown and deterministic recovery","Additional equipment required","Three-phase programmable grid simulator with independent phase control; power analyzer; HV battery simulator/load; oscilloscope","N6700 can power auxiliary electronics only. Independent three-phase source control is external.","++*","++*","++*","++*","ISO 5474-2:2024; IEC 61000-4-27:2000+A1:2009+A2:2025 where applicable; product/grid requirement"],
["CHG-005","Charging / OBC","AC input inrush and precharge","Verify mains-side inrush, DC-link precharge and repeated energization stress for the on-board charger","Energize at worst source voltage and phase angle with discharged and partially charged DC link; repeat hot/cold and after short off-times","Peak and RMS input current, charge, current-squared-time, DC-link rise, relay/contactor timing and component stress","Inrush, fuse/relay stress and precharge timing remain within design limits; no nuisance protection or welded contactor","Additional equipment required","Programmable AC source or synchronized mains switch; wide-band current probe; power analyzer; HV battery simulator/load; safety enclosure","N6700 is not the AC source. It can support auxiliary/control rails and synchronized logging only.","T","T","T","T","ISO 5474-2:2024; IEC 61851-21-1:2017; product/fuse/contactor requirements"],
["CHG-006","Charging / OBC","AC input power factor and efficiency map","Characterize charger power factor, apparent power and conversion efficiency over the charging envelope","Sweep AC voltage/frequency, charge power, HV battery voltage and temperature; include single-phase and three-phase modes where supported","True power, apparent power, reactive power, displacement/total power factor, AC-to-DC efficiency and temperature","Meets project, market and thermal-efficiency targets over the declared operating envelope","Additional equipment required","Precision multi-channel power analyzer; programmable grid source; regenerative HV battery simulator/load; thermal chamber","N6700 may power auxiliaries but cannot substitute for the mains source, regenerative HV load or precision AC power analyzer.","—","—","—","—","ISO 5474-2:2024; product energy-efficiency and grid-interface requirements"],
["CHG-007","Charging / OBC","Harmonic current and flicker on the AC charging input","Verify that the OBC does not inject excessive low-frequency harmonic current or objectionable voltage fluctuation into the public supply","Operate the charger in the prescribed power states and execute the applicable harmonic-current and voltage-fluctuation/flicker methods for its rated current and connection class","Current harmonic spectrum, total harmonic distortion, voltage changes and flicker metrics","Within the applicable public-supply limits for the charger rating and market","Additional equipment required","Compliant AC source/reference impedance; harmonic/flicker-capable power analyzer; HV battery simulator/load","N6700 has no formal role in the AC harmonic/flicker measurement other than optional auxiliary-power support.","—","—","—","—","IEC 61000-3-2:2018+A1:2020+A2:2024 and IEC 61000-3-3:2013+A1:2017+A2:2021 for <=16 A/phase; IEC 61000-3-11/-3-12 as applicable above that range; ISO 5474-2:2024"],
["CHG-008","Charging safety","Protective-earth continuity through the vehicle charging path","Verify the protective bonding path used while conductively connected to external power and detect excessive resistance or an open protective-earth path","Measure protective-bond continuity with the vehicle/OBC in the specified connection states; inject an open/high-resistance PE fault where the architecture provides monitoring","Bond resistance or voltage drop, PE monitor response, charge inhibit and diagnostic timing","Protective bonding and monitoring meet the applicable vehicle power-transfer safety requirement; unsafe charging is inhibited","Additional equipment required","Protective-bond/ground-continuity tester; charging inlet/EVSE interface fixture; HV safety enclosure","N6700 cannot perform the required protective-earth continuity test; it may power low-voltage controls during monitoring checks.","T","T","T","T","ISO 5474-1:2024; ISO 5474-2:2024; ISO 6469-3:2021; applicable charging-interface requirement"],
["CHG-009","Charging safety","Leakage, isolation and residual-current behavior while charging","Verify that mains-to-chassis/HV leakage and isolation-monitor behavior remain safe in normal operation and relevant single-fault conditions","Measure leakage/isolation in defined charging states and inject representative insulation or leakage faults through controlled impedances; repeat across AC/HV voltage and temperature corners","Leakage/residual current, isolation resistance, monitor threshold and reaction time, contactor state","Within applicable shock-protection limits; faults are detected and charging is inhibited/disconnected within the specified time","Additional equipment required","Leakage-current measurement network; insulation-resistance tester; programmable fault impedance; grid simulator; HV battery simulator; safety interlocks","N6700 only supports low-voltage auxiliaries. Formal leakage/isolation testing needs dedicated mains/HV safety instrumentation.","T","T","T","T","ISO 5474-1:2024; ISO 5474-2:2024; ISO 6469-3:2021; charging-system safety concept"],
["CHG-010","Charging control","Charger and battery-management-system coordination","Verify charging current/voltage limits, contactor sequencing and protection coordination between OBC and battery-management system","Exercise requested current/voltage boundaries, battery-temperature/voltage limits, contactor delays and BMS inhibit/derating commands; inject stale, inconsistent and boundary values through supported interfaces","Commanded vs actual current/voltage, contactor timing, limit enforcement, diagnostics and final state","No command or timing condition can exceed battery/OBC allocated limits; inhibit and derating commands are honored within required reaction time","Partial","HV battery simulator or BMS emulator; vehicle communications interface; oscilloscope; fault-injection/test hooks; safety interlocks","N6700 may emulate low-voltage auxiliaries and some signal-level conditions, but the HV battery interface and BMS emulation are external.","REQ*","REQ*","REQ*","REQ*","ISO 26262 safety requirements and interfaces; vehicle battery/OBC requirement; ISO 5474 power-transfer context"],
["CHG-011","Charging safety / fault injection","Charging single-fault and abnormal-operation response","Verify that credible charger faults do not create hazardous HV/mains exposure, uncontrolled battery current or unsafe contactor state","Inject representative sensor, feedback, control, cooling, contactor and power-stage faults identified by FMEA/FMEDA/DFA while charging at worst relevant operating corners","Fault electrical effect, detection time, protection reaction, contactor/isolation state, temperatures and recovery","Each credited safety mechanism detects the allocated fault and reaches/maintains the specified safe or degraded state within the allocated timing","Additional equipment required","HV grid/battery simulators; protected fault-injection fixture; isolated probes; thermal instrumentation; interlocked enclosure","N6700 is useful for low-voltage auxiliary fault conditions only. High-energy charger faults require dedicated protected equipment.","REQ* · FI+","REQ* · FI+","REQ* · FI++","REQ* · FI++","ISO 26262-5/-9; ISO 5474-1:2024; ISO 5474-2:2024; ISO 6469-3:2021; project safety analysis"],
["CHG-012","Bidirectional charging","V2G/V2H power-flow direction change and four-quadrant transition","Verify safe and stable transition between grid-to-vehicle charging and vehicle-to-grid/home export modes","Command repeated direction changes at AC/HV voltage, power and temperature corners; include reversal during load/grid disturbances and near zero power","Transition time, AC and HV current, DC-link excursion, contactor state, cross-conduction, exported/imported power and communication state","No uncontrolled current or rail excursion; deterministic handover and protection behavior; power direction matches negotiated state","Additional equipment required","Regenerative four-quadrant grid simulator; regenerative HV battery simulator; multi-channel power analyzer; isolated oscilloscope probes; ISO 15118 communication stack/emulator","N6700 cannot provide regenerative mains/HV operation. It can support low-voltage auxiliary rails and synchronized control/monitoring.","T*","T*","REQ*","REQ*","ISO 5474-1:2024 and ISO 5474-2:2024 reverse power transfer; ISO 15118-20:2022 bidirectional power-transfer communication; applicable grid requirements"],
["CHG-013","Bidirectional charging / grid protection","Grid loss and anti-islanding response during exported power","Verify that a V2G-capable vehicle stops or transitions exported power correctly when the external grid becomes unavailable or leaves allowed conditions","While exporting power, open the grid connection and apply out-of-range grid voltage/frequency conditions defined by the applicable market/interconnection rule","Export current and power, disconnect/transition time, contactor state, island voltage/frequency and reconnection behavior","Meets the applicable grid interconnection protection and reconnection requirements; no unintended energized island","Additional equipment required","Regenerative grid simulator with anti-islanding test capability or certified grid-interconnection test system; HV battery simulator; power analyzer","N6700 has no role in the grid-protection stimulus except auxiliary/control support.","—","—","—","—","Applicable national grid/interconnection requirements for bidirectional EV charging; ISO 5474-1/-2 power-transfer framework; ISO 15118-20:2022 communication context"],
["CHG-014","Charging control / communications","Charging recovery after communication loss or invalid charging sequence","Verify that loss, corruption or invalid ordering of EV-EVSE charging communication cannot leave uncontrolled energy transfer or an undefined recovery state","Interrupt communication at each major charging phase; inject timeout, malformed/unsupported state and inconsistent power-limit sequences through a compliant emulator where supported","Power flow, contactor state, timeout/detection time, diagnostics, restart/re-authentication sequence and retained state","Energy transfer stops or transitions to the defined safe state within the required timeout; restart requires the specified valid sequence and never resumes from stale limits","Partial","ISO 15118/charging-communication emulator; EVSE interface; grid and HV battery simulators; oscilloscope; fault injection at communication link","N6700 may power auxiliary electronics and log low-voltage behavior; charging communication and high-power interfaces require dedicated emulation.","REQ* · FI+","REQ* · FI+","REQ* · FI++","REQ* · FI++","ISO 15118-20:2022; ISO 5474-1:2024; ISO 5474-2:2024; ISO 26262 where communication loss is safety-related"],
]

CLASS_ROWS = [
["CHG-001","AC input voltage and frequency operating range","new","ROB","ET","—","++*","++*","++*","++*","CHG-22 · OBC/AC charging interface only"],
["CHG-002","AC brownout and voltage-dip immunity","new","ROB","ET","—","++*","++*","++*","++*","CHG-22 · OBC/AC charging interface only"],
["CHG-003","AC interruption and restart","new","ROB","ET, FT","—","++*","++*","++*","++*","CHG-22 · OBC/AC charging interface only"],
["CHG-004","Three-phase phase loss and voltage unbalance","new","ROB","ET","—","++*","++*","++*","++*","CHG-22 · three-phase OBC only"],
["CHG-005","AC input inrush and precharge","new","TRIG","ET","—","T","T","T","T","CHG-22 · trigger when precharge/inrush can affect a safety requirement"],
["CHG-006","AC input power factor and efficiency map","new","QUAL","—","—","—","—","—","—","CHG-22 · performance/grid-quality evidence, not ISO 26262 driven"],
["CHG-007","Harmonic current and flicker on the AC charging input","new","QUAL","—","—","—","—","—","—","CHG-22 · public-grid compliance, not ISO 26262 driven"],
["CHG-008","Protective-earth continuity through the vehicle charging path","new","TRIG","FT","CF","T","T","T","T","CHG-22 · trigger when PE monitoring/bonding is part of allocated malfunction safety behavior"],
["CHG-009","Leakage, isolation and residual-current behavior while charging","new","TRIG","ET, FT","CF","T","T","T","T","CHG-22 · electric-shock safety is primarily ISO 5474/6469; ISO 26262 only when malfunction behavior is allocated"],
["CHG-010","Charger and battery-management-system coordination","new","CORE*","FT, DFA","CF","REQ*","REQ*","REQ*","REQ*","CHG-22 · when charging coordination enforces a safety-related battery/current/voltage limit"],
["CHG-011","Charging single-fault and abnormal-operation response","new","CORE*","FT, FI, DFA","CF","REQ* · FI+","REQ* · FI+","REQ* · FI++","REQ* · FI++","CHG-22 · safety-analysis-derived charger faults"],
["CHG-012","V2G/V2H power-flow direction change and four-quadrant transition","new","CORE*","FT, ET, DFA","CF","T*","T*","REQ*","REQ*","CHG-22 · bidirectional chargers only; grade follows safety allocation"],
["CHG-013","Grid loss and anti-islanding response during exported power","new","QUAL","—","—","—","—","—","—","CHG-22 · grid-interconnection compliance; separate from ISO 26262"],
["CHG-014","Charging recovery after communication loss or invalid charging sequence","new","CORE*","FT, FI","CF","REQ* · FI+","REQ* · FI+","REQ* · FI++","REQ* · FI++","CHG-22 · where charging communication participates in safety-related energy-transfer control"],
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write(path: Path, text: str, bom: bool = False) -> None:
    path.write_text(text, encoding="utf-8-sig" if bom else "utf-8")


def md_row(cells: list[str]) -> str:
    assert len(cells) == 15
    assert all("|" not in c for c in cells)
    return "| " + " | ".join(cells) + " |"


def update_matrix() -> None:
    text = read(MD)
    if "| CHG-001 |" in text:
        raise SystemExit("CHG rows already present")
    text = text.replace("121-row validation matrix", "135-row validation matrix", 1)
    text = text.replace(
        "- 48 V and voltage-class-B/high-voltage references where applicable;",
        "- 48 V and voltage-class-B/high-voltage references where applicable;\n- external AC/DC charging, on-board-charger and bidirectional V2G/V2H power-transfer validation where applicable;",
        1,
    )
    block = "\n".join(md_row(r) for r in ROWS) + "\n"
    marker = "| FUSA-001 | Functional safety |"
    if marker not in text:
        raise SystemExit("FUSA insertion marker not found")
    text = text.replace(marker, block + marker, 1)

    text = text.replace(
        "5. **Automotive supply profiles:** AUTO-001…AUTO-018, starting with non-destructive voltage ramps before severe pulses.\n6. **Temperature corners:**",
        "5. **Automotive supply profiles:** AUTO-001…AUTO-018, starting with non-destructive voltage ramps before severe pulses.\n6. **Charging / OBC / V2G:** CHG-001…CHG-014 when the product connects to an external charging circuit; start with AC operating-range and controlled interruption tests before abnormal/single-fault or bidirectional export cases.\n7. **Temperature corners:**",
        1,
    )
    text = text.replace("7. **Functional-safety / combined corners:**", "8. **Functional-safety / combined corners:**", 1)
    text = text.replace("8. **Endurance and margin:**", "9. **Endurance and margin:**", 1)
    text = text.replace("9. **EMC pre-compliance:**", "10. **EMC pre-compliance:**", 1)
    text = text.replace("10. **Formal qualification:**", "11. **Formal qualification:**", 1)
    text = text.replace("48V-*, HV-* plus any safety rows", "48V-*, HV-*, CHG-* plus any safety rows", 1)
    text = text.replace(
        "The largest gaps for formal automotive qualification are a compliant **ISO 7637 transient generator**",
        "For OBC/V2G products, the present DC bench also needs a **programmable AC/grid simulator**, **precision AC power analyzer**, **regenerative HV battery simulator/load** and an **interlocked charging-interface/communications emulator**.\n\nThe largest gaps for formal automotive qualification are a compliant **ISO 7637 transient generator**",
        1,
    )

    ref_marker = "28. **R. D. Middlebrook** — \"Measurement of loop gain in feedback systems\" (Int. J. Electronics, 1975) and \"Input filter considerations in design and application of switching regulators\" (IEEE IAS Annual Meeting, 1976); background for PS-021 and PS-023."
    refs = """29. **ISO 5474-1:2024** — Electrically propelled road vehicles — Functional and safety requirements for power transfer between vehicle and external electric circuit — Part 1: General requirements for conductive power transfer. Replaces the general vehicle-side role previously covered by withdrawn ISO 17409:2020.  
    https://www.iso.org/standard/81296.html
30. **ISO 5474-2:2024** — Part 2: AC power transfer; applies to vehicle power-supply circuits, including on-board charger configurations and reverse power transfer.  
    https://www.iso.org/standard/81298.html
31. **ISO 15118-20:2022** — Vehicle-to-grid communication interface — 2nd generation network/application layer; includes communication messages and sequences for bidirectional power transfer.  
    https://www.iso.org/standard/77845.html
32. **IEC 61851-21-1:2017** — EV on-board charger EMC requirements for conductive connection to AC/DC supply.  
    https://webstore.iec.ch/en/publication/32045
33. **IEC 61000-4-27:2000+A1:2009+A2:2025** — Voltage-unbalance immunity method for applicable three-phase equipment.  
    https://webstore.iec.ch/en/publication/109827
34. **IEC 61000-3-2:2018+A1:2020+A2:2024** and **IEC 61000-3-3:2013+A1:2017+A2:2021** — public low-voltage supply harmonic-current and voltage-fluctuation/flicker limits for equipment within their rated-current scopes.  
    https://webstore.iec.ch/en/publication/92799  
    https://webstore.iec.ch/en/publication/68776"""
    if ref_marker not in text:
        raise SystemExit("reference insertion marker not found")
    text = text.replace(ref_marker, ref_marker + "\n" + refs, 1)

    text = text.replace(
        "**Execution-model improvements:** added mandatory applicability/operating-state/sample/pre-post/timing-recovery/evidence/measurement-traceability/N6700-capability metadata; combined-corner campaign; evidence/traceability rules; explicit post-stress drift and recovery-state requirements.",
        "**Charging/V2G extension (2026-09-21):** added CHG-001…CHG-014 for OBC AC input behavior, dips/interruptions, three-phase faults, inrush, power quality, PE/leakage safety, BMS coordination, charging single faults, V2G/V2H reversal, anti-islanding and charging-communication loss. ISO 5474-1/-2:2024 are used instead of withdrawn ISO 17409:2020. The matrix now contains 135 test rows.\n\n**Execution-model improvements:** added mandatory applicability/operating-state/sample/pre-post/timing-recovery/evidence/measurement-traceability/N6700-capability metadata; combined-corner campaign; evidence/traceability rules; explicit post-stress drift and recovery-state requirements.",
        1,
    )
    write(MD, text)


def regenerate_csv() -> None:
    text = read(MD)
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and len(line) > 2:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and cells[0].count("-") == 1 and cells[0].split("-")[-1].isdigit() and len(cells) == 15:
                rows.append(cells)
    if len(rows) != 135:
        raise SystemExit(f"expected 135 matrix rows, got {len(rows)}")
    with CSV.open("r", encoding="utf-8-sig", newline="") as f:
        header = next(csv.reader(f))
    if len(header) != 15:
        raise SystemExit("unexpected automotive CSV header")
    with CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def update_classification() -> None:
    with CLASS.open("r", encoding="utf-8-sig", newline="") as f:
        data = list(csv.reader(f))
    if any(r and r[0] == "CHG-001" for r in data[1:]):
        raise SystemExit("classification already contains CHG rows")
    if len(data[0]) != 11:
        raise SystemExit("unexpected classification header")
    data.extend(CLASS_ROWS)
    with CLASS.open("w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(data)


def update_mapping() -> None:
    text = read(MAP)
    if "| CHG-001 | ROB |" in text:
        raise SystemExit("mapping already contains CHG-22 additions")
    text = text.replace("This file maps the 121 tests", "This file maps the 135 tests", 1)
    change_row = "| CHG-21 | Claude deep-review integration: 21 coverage rows, title/style reconciliation, source expansion and consistency CI | PS-032…QUAL-001; §4; repository CI | Deep review 2026-09-21; research-source-links-v2; test-matrix-additions-2026-09-21 |"
    add_change = "| CHG-22 | OBC / charging / V2G expansion from the global matrix; current ISO 5474 references replace withdrawn ISO 17409 | CHG-001…CHG-014; §4.2 | ISO 5474-1/-2:2024; ISO 15118-20:2022; IEC 61851-21-1; IEC 61000 charging/grid methods |"
    if change_row not in text:
        raise SystemExit("CHG-21 mapping change marker not found")
    text = text.replace(change_row, change_row + "\n" + add_change, 1)

    section = """### 4.2 CHG-22 charging / OBC / V2G additions

These conditional rows extend the automotive matrix to products with an external conductive charging interface. Grid-quality and anti-islanding rows are not automatically ISO 26262 evidence; rows involving malfunctioning charger control, battery limits, contactors or safety-related communication become required only when allocated by the safety concept.

| ID | Class | ASIL A | ASIL B | ASIL C | ASIL D | Note |
|---|---|---|---|---|---|---|
| CHG-001 | ROB | ++* | ++* | ++* | ++* | AC OBC input range/frequency where an external charging interface exists |
| CHG-002 | ROB | ++* | ++* | ++* | ++* | AC brownout/dip immunity for OBC products |
| CHG-003 | ROB | ++* | ++* | ++* | ++* | AC interruption/restart for OBC products |
| CHG-004 | ROB | ++* | ++* | ++* | ++* | three-phase OBC only |
| CHG-005 | TRIG | T | T | T | T | precharge/inrush becomes safety evidence only when analysis allocates a relevant limit |
| CHG-006 | QUAL | — | — | — | — | performance/efficiency/grid-quality evidence |
| CHG-007 | QUAL | — | — | — | — | public-grid harmonic/flicker compliance |
| CHG-008 | TRIG | T | T | T | T | PE monitoring/bonding if part of malfunction safety behavior |
| CHG-009 | TRIG | T | T | T | T | primarily ISO 5474/6469 electrical safety; ISO 26262 only when malfunction behavior is allocated |
| CHG-010 | CORE* | REQ* | REQ* | REQ* | REQ* | charger/BMS coordination enforcing safety-related limits |
| CHG-011 | CORE* | REQ* · FI+ | REQ* · FI+ | REQ* · FI++ | REQ* · FI++ | safety-analysis-derived charger single faults |
| CHG-012 | CORE* | T* | T* | REQ* | REQ* | bidirectional charging only; exact grade follows the safety allocation |
| CHG-013 | QUAL | — | — | — | — | grid-interconnection anti-islanding compliance |
| CHG-014 | CORE* | REQ* · FI+ | REQ* · FI+ | REQ* · FI++ | REQ* · FI++ | charging communication participates in safety-related energy transfer |

"""
    if "## 5. New rows: test outlines" not in text:
        raise SystemExit("section 5 marker not found")
    text = text.replace("## 5. New rows: test outlines", section + "## 5. New rows: test outlines", 1)
    write(MAP, text)


def update_related_docs() -> None:
    text = read(GLOBAL)
    text = text.replace("cross-industry extension of the 121-row automotive matrix", "cross-industry extension of the 135-row automotive matrix", 1)
    text = text.replace("complete **121-row automotive matrix is part", "complete **135-row automotive matrix is part", 1)
    text = text.replace("`FUSA-*`, `SYS-*`, `BI-*`, `RV-*` and `QUAL-*`", "`FUSA-*`, `SYS-*`, `BI-*`, `CHG-*`, `RV-*` and `QUAL-*`", 1)
    old = "| `HV-*` | Voltage-class-B, isolation, partial discharge, CMTI | ISO 21498; ISO 6469-3; IEC 60664-1; IEC 62477-1 |"
    new = old + "\n| `CHG-*` | OBC AC input, charging safety/control and V2G/V2H behavior | ISO 5474-1/-2; ISO 15118-20; IEC 61851-21-1; IEC 61000 grid/power-quality methods; applicable grid rules |"
    if old in text:
        text = text.replace(old, new, 1)
    write(GLOBAL, text)

    text = read(TM_README).replace("detailed 121-row automotive validation matrix", "detailed 135-row automotive validation matrix", 1)
    write(TM_README, text)
    text = read(ROOT_README).replace("detailed 121-row automotive validation matrix", "detailed 135-row automotive validation matrix", 1)
    write(ROOT_README, text)

    text = read(BENCH)
    text = text.replace(
        "The current validation matrix contains 121 test rows. The highest automation potential is in DC characterization, dynamics, protection, automotive electrical disturbances, thermal testing, endurance, and selected functional-safety fault-injection work.",
        "The automation counts below were made against the original 121-row matrix. The automotive matrix now contains 135 rows after the CHG-001…CHG-014 charging/V2G extension; those 14 mains/HV charging rows are not included in the counts below and generally require a programmable AC/grid simulator, HV battery simulator/load, power analyzer and charging-interface emulation. The highest automation potential of the original bench remains in DC characterization, dynamics, protection, automotive electrical disturbances, thermal testing, endurance, and selected functional-safety fault-injection work.",
        1,
    )
    write(BENCH, text)


def update_sources() -> None:
    text = read(SOURCES)
    if "## M. NEW — OBC / conductive charging / V2G" in text:
        return
    section = """
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

"""
    marker = "## Provenance notes for v2"
    if marker not in text:
        raise SystemExit("source provenance marker not found")
    text = text.replace(marker, section + marker, 1)
    write(SOURCES, text)


def main() -> None:
    update_matrix()
    regenerate_csv()
    update_classification()
    update_mapping()
    update_related_docs()
    update_sources()

    # Basic set consistency before invoking the repository checker.
    ids = []
    for line in read(MD).splitlines():
        if line.startswith("|"):
            first = line.strip().strip("|").split("|", 1)[0].strip()
            if first.count("-") == 1 and first.split("-")[-1].isdigit():
                ids.append(first)
    if len(ids) != 135 or len(set(ids)) != 135:
        raise SystemExit(f"matrix ID check failed: {len(ids)} rows / {len(set(ids))} unique")
    print("charging expansion applied: 135 unique automotive test rows")


if __name__ == "__main__":
    main()
