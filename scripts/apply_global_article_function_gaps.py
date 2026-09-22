#!/usr/bin/env python3
from pathlib import Path

p = Path('Test-matrix/global-power-supply-test-matrix.md')
s = p.read_text(encoding='utf-8')

s = s.replace(
    '_Last updated: 2026-09-21 · cross-industry extension of the 135-row automotive matrix_',
    '_Last updated: 2026-09-22 · cross-industry extension of the 135-row automotive matrix · article-derived function review integrated_',
    1,
)

anchor = '> **Important:** exact voltage levels, waveforms, source impedances, durations, repetition counts, environmental severities, sample counts and acceptance criteria shall come from the exact applicable standard edition, customer specification and regulatory/contract basis. This matrix defines reusable test intent and traceability; it does not reproduce licensed normative text.\n'
addition = anchor + '\n> **Article-derived refinement:** the generic matrix was cross-checked against the 131-resource multilingual test-method corpus summarized in [`../reference/power-supply-test-functions-from-articles-2026-09-22.md`](../reference/power-supply-test-functions-from-articles-2026-09-22.md). Dedicated rows were added only where the corpus exposed a distinct DUT function; oscilloscope/probe/FRA setup practices remain measurement-method controls rather than separate DUT tests.\n'
if addition not in s:
    assert anchor in s
    s = s.replace(anchor, addition, 1)

old6 = '| GEN-006 | Input | Inrush / input current profile | Verify source, connector, fuse and rectifier stress | Energize at worst phase angle/voltage/temp; repeat starts | peak current, charge, I²t, settling | Product/standard limits | All | IEC 62040; ETSI EN 300 132; IEC 62368-1; IEC 62477-1 | DV/TYPE | P |'
new6 = '| GEN-006 | Input | Input inrush / energization current | Verify source, connector, fuse, rectifier and input-capacitor stress specifically during energization | Energize at worst phase angle/voltage/temp; repeat starts and short off-times where applicable | peak current, charge, I²t, settling, precharge timing | Product/standard limits | All | IEC 62040; ETSI EN 300 132; IEC 62368-1; IEC 62477-1 | DV/TYPE | P |'
assert old6 in s
s = s.replace(old6, new6, 1)

old20 = '| GEN-020 | Efficiency | Efficiency / loss map | Determine operating losses and thermal worst case | Input × load × temperature sweep; bidirectional where applicable | Pin/Pout, efficiency, loss, temp | Product/energy requirement | All | IEC 62040-3; IEC 62477-1; product requirement | CHAR/DV | A |'
new_block = '''| GEN-020 | Efficiency | System efficiency / total-loss map | Determine end-to-end conversion efficiency, total loss and thermal worst case without assuming the internal loss mechanism | Input × load × temperature sweep; bidirectional where applicable | Pin/Pout, efficiency, total loss, temperature | Product/energy requirement; use GEN-024/025 when switching/conduction loss decomposition is needed | All | IEC 62040-3; IEC 62477-1; product requirement | CHAR/DV | A |
| GEN-021 | Input | Input-current waveform / crest factor | Characterize steady-state source-current shape and peakiness separately from energization inrush; expose rectifier/PFC/source stress and source-compatibility issues | Capture input current over representative line and switching cycles at min/nom/max input and load; include relevant operating modes | RMS and peak current, crest factor, waveform, phase relationship, repetition/burst behavior | Product/platform requirement; public-mains harmonic limits remain under EMC-010 | AC/DC supplies; UPS; chargers; high-power converters; server/data-centre PSUs | IEC 62040-3; IEC 61000-3-2 where applicable; product/application requirement; article-derived methodology | CHAR/DV | P |
| GEN-022 | Output | Output-current accuracy / current regulation | Verify constant-current or current-programmed output accuracy, stability and compliance behavior | Command/sweep current setpoints and load/compliance voltage across input and temperature corners | Iout error, current ripple/noise, compliance voltage, transition to voltage limit, drift | Product/application requirement | Chargers; LED drivers; battery equipment; laboratory/ATE supplies; process sources; current-regulated converters | IEC 61204 where applicable; IEC 61347 family for LED drivers; battery/charger/product requirements | CHAR/DV | A/P |
| GEN-023 | Output | Remote-sense / distribution-drop compensation | Verify remote-sense accuracy and stability with realistic harness/bus drop, and safe behavior for sense-open/miswire conditions where relevant | Insert controlled lead resistance/drop; compare local vs remote sense; sweep load; exercise sense open/short/miswire only where design permits | local/remote voltage, compensation error, loop stability/ringing, current, fault/recovery behavior | Product/system requirement and allowed sense-compensation range | Telecom; data centre; server/rack PSUs; high-current industrial/lab supplies | ETSI/system requirements where applicable; IEC 61204; product requirement; article-derived methodology | DV | A/P |
| GEN-024 | Power stage | Switching-loss characterization | Quantify semiconductor switching energy and loss to validate efficiency, thermal design, gate drive and corner margin | Correlated high-bandwidth switch voltage/current capture over line/load/temp corners; de-skew channels before energy math | Eon, Eoff, switching power, transition time, overshoot/ringing, dv/dt/di/dt | Design loss/thermal budget and device SOA with documented measurement uncertainty | Switched-mode converters, inverters, chargers, drives, UPS, high-power supplies | IEC 62477-1/product design basis; device data; article-derived oscilloscope methodology | CHAR/DV | P |
| GEN-025 | Power stage | Conduction-loss characterization | Quantify on-state semiconductor and interconnect loss, including temperature dependence, separately from switching loss | Measure device current and on-state voltage or resistance over load/temp operating points | VCE(sat)/VDS(on), RDS(on), forward drop, RMS current, conduction loss, temperature coefficient | Design loss/thermal budget and device derating/SOA | Switched-mode converters, inverters, chargers, drives, UPS, high-current supplies | IEC 62477-1/product design basis; device data; article-derived methodology | CHAR/DV | P |
| GEN-026 | AC input / power quality | Power factor / apparent and reactive power | Characterize AC input utilization for generic AC-powered converters, not only vehicle charging | Measure true/apparent/reactive power and current/voltage phase across line/load/mode corners | W, VA, var, displacement PF, total PF, RMS V/I | Product/grid/energy requirement; harmonic/flicker compliance remains EMC-010 | AC/DC supplies; UPS; server/data-centre PSUs; industrial converters; chargers | IEC 62040-3; IEC 61000-3-2/-3 where applicable; product/market requirement | CHAR/TYPE | P/E |
| REL-001 | Reliability / production | HASS / production stress screening | Verify a repeatable production screen can precipitate workmanship/process defects without consuming unacceptable product life; distinct from HALT/design-margin discovery | Apply controlled thermal/vibration/electrical screening profile derived from prior characterization/HALT; run functional checks during/after stress | fallout rate, failure mode, parametric drift, functional interruptions, screen limits, cumulative stress exposure | Qualified manufacturing-screen specification with demonstrated precipitating efficiency and acceptable life consumption | High-reliability electronics; aerospace/defence; industrial; medical; telecom/data centre; selected high-volume power products | IEC 60068 methods as applicable; project/manufacturing qualification; HALT/HASS technical literature | PV/REL | E/P |'''
assert old20 in s
s = s.replace(old20, new_block, 1)

p.write_text(s, encoding='utf-8')

# Basic integrity checks.
text = p.read_text(encoding='utf-8')
for test_id in ['GEN-021','GEN-022','GEN-023','GEN-024','GEN-025','GEN-026','REL-001']:
    assert text.count(f'| {test_id} |') == 1, test_id
assert '| GEN-006 | Input | Input inrush / energization current |' in text
assert '| GEN-020 | Efficiency | System efficiency / total-loss map |' in text
print('global matrix article-derived function update applied successfully')
