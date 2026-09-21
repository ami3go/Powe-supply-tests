# Electronic Power — Industry Coverage Map

**Date:** 2026-09-21  
**Purpose:** Provide a broad industry taxonomy showing where electronic power supplies, converters, chargers, inverters, UPS systems, DC/DC converters, AC/DC supplies, battery power systems and power-conditioning electronics are used. This document is intended to guide standards-search coverage for the Power Supply Tests project.

## Standards-column scope

The **Standards** column lists standards and standard families identified as directly or materially relevant to the power source, power input/output interface, converter, charger, battery system, UPS, electrical safety, power-port EMC, or powered-equipment qualification for that industry.

This is a **living cross-reference**, not a claim that every national, OEM, operator, military-programme or product-specific standard in the world has been captured. Exact applicability depends on product type, voltage, installation, jurisdiction and contract. Where a product standard invokes a generic power, EMC or safety method, both may be listed. Historical standards should be checked against the current edition before use.

Common cross-sector families repeatedly used below include:

- **IEC 61204-3 / IEC 61204-7** — low-voltage switch-mode power supplies, EMC / safety.
- **IEC 61558-1** — transformers, reactors and power-supply units, safety.
- **IEC 62477-1** — safety requirements for power electronic converter systems and equipment.
- **IEC 62040-1 / -2 / -3** — UPS safety, EMC, performance and test requirements.
- **IEC 61000-4-x** — EMC immunity methods including ESD, EFT/burst, surge, RF, voltage dips and interruptions.
- **IEC 61000-6-x** — generic EMC standards where no dedicated product-family EMC standard governs.
- **IEC 62133-2 / IEC 62619** — rechargeable battery safety for portable / industrial applications.
- **IEC 60068 series** — environmental testing where invoked by the product/platform standard.

## Detailed industry list

| Industry / sector | Typical electronic power equipment | Standards with power-supply / power-interface relevance |
|---|---|---|
| Consumer electronics | AC/DC adapters, USB-C chargers, TV/monitor PSUs, game consoles, audio equipment | IEC 62368-1; IEC 61558-1; IEC 61204-3; IEC 61204-7; IEC 61000-3-2; IEC 61000-3-3; CISPR 32; CISPR 35; IEC 61000-4-11; IEC 61000-4-5; IEC 62133-2; IEC 62680-1-3 (USB Type-C/USB Power Delivery) |
| Information technology / computing | PC PSUs, servers, workstations, storage systems, GPU systems | IEC 62368-1; IEC 61204-3; IEC 61204-7; IEC 62040-1/-2/-3; CISPR 32; CISPR 35; IEC 61000-4-11; IEC 61000-4-5 |
| Data centres / cloud infrastructure | Server PSUs, rack power shelves, UPS, 48 V DC systems, battery backup | IEC 62368-1; IEC 62040-1/-2/-3; IEC 62477-1; EN 50600 series; ISO/IEC 22237 series; ETSI EN 300 132-1/-2/-3; IEC 62619; IEC 62933 series |
| Telecommunications | -48 V rectifiers, base-station PSUs, telecom UPS, remote radio power | ETSI EN 300 132-1; ETSI EN 300 132-2 (-48 V DC); ETSI EN 300 132-3 (up to 400 V DC); ITU-T L.1200 family; ITU-T K.20; ITU-T K.21; IEC 62368-1; IEC 62040 series; IEC 61204 series |
| Networking | Routers, switches, PoE injectors/switches, optical networking power | IEC 62368-1; IEEE 802.3 PoE clauses; IEC 61204-3/-7; CISPR 32; CISPR 35; IEC 62040 series |
| Automotive | 12/24/48 V DC/DC converters, onboard chargers, ECU supplies, infotainment power | ISO 16750-1/-2/-3/-4/-5; ISO 7637-1/-2/-3; ISO 21780; ISO 21498-1/-2; CISPR 25; ISO 11452 series; UNECE R10; LV 124; VW 80000; VDA 320; ISO 26262 where safety-related |
| Electric vehicles | Traction inverters, onboard chargers, HV/LV DC/DC converters, battery chargers | ISO 6469-1/-2/-3; ISO 21498-1/-2; ISO 16750 series for LV equipment; ISO 7637 series; IEC 61851-1/-23/-24; IEC 62196 series; ISO 15118 series; UNECE R100; UNECE R10; IEC 62477-1; ISO 26262 |
| Commercial vehicles | Truck/bus DC systems, converters, auxiliaries, charging systems | ISO 16750-2; ISO 7637-2/-3; ISO 21780 where 48 V applies; UNECE R10; ISO 26262 where safety-related; OEM commercial-vehicle electrical specifications |
| Agricultural vehicles | Tractor electronics, implement power, autonomous farming equipment | ISO 14982; ISO 25119 series where safety-related; IEC 60204-1 for machinery; ISO 16750/ISO 7637 where road-vehicle electrical requirements are contractually adopted; IEC 62477-1 for converter systems |
| Off-highway machinery | Excavators, loaders, cranes, forestry equipment | ISO 13766-1/-2; ISO 19014 series where functional safety applies; IEC 60204-1; IEC 61800-3; IEC 61800-5-1; IEC 62477-1 |
| Railway | Traction auxiliaries, onboard converters, battery chargers, signalling supplies | EN 50155; IEC 60571; EN 50121 / IEC 62236 series; EN 50163; EN 50124 series; IEC 61373; IEC 62477-1; EN 50526/EN 50129 where signalling/safety applications apply |
| Metro / tram / light rail | Traction auxiliaries, communications and control supplies | EN 50155; IEC 60571; EN 50121 / IEC 62236; EN 50163; IEC 61373; IEC 62477-1 |
| Railway infrastructure | Signalling PSUs, point machines, communications backup systems | EN 50121 / IEC 62236; EN 50124; EN 50125 series; EN 50126; EN 50128/EN 50716; EN 50129; IEC 62040 series; IEC 62477-1 |
| Civil aviation | Avionics PSUs, 28 V DC / 115 V AC equipment, converters, battery systems | RTCA DO-160G / EUROCAE ED-14G; RTCA DO-311A; SAE AS50881 for aircraft wiring; aircraft/OEM power-interface specifications |
| Military aviation | Mission electronics, radar power, avionics converters | MIL-STD-704; MIL-HDBK-704-1 through -8 test guidance; MIL-STD-461; MIL-STD-810; MIL-STD-1275 only where vehicle-derived DC systems are involved |
| Unmanned aircraft / drones | Battery systems, motor drives, flight-controller supplies, payload converters | RTCA DO-160 where certification basis invokes it; ASTM F3322/F38-family standards as applicable; IEC 62133-2 for portable batteries; UN 38.3 transport testing; IEC 62368-1 for payload/ICT-type equipment; military UAVs may invoke MIL-STD-704/-461/-810 |
| Spacecraft | Satellite power-conditioning/distribution units, DC/DC converters | ECSS-E-ST-20; ECSS-E-ST-20-07; ECSS-E-ST-10-03; ECSS-Q-ST-20; NASA GSFC-STD-7000 (GEVS); NASA-STD-4003 electrical bonding; mission-specific EEE/power standards |
| Satellites | Solar-array regulators, battery electronics, payload PSUs | ECSS-E-ST-20; ECSS-E-ST-20-07; ECSS-E-ST-10-03; NASA GSFC-STD-7000; mission-specific spacecraft electrical power subsystem requirements |
| Launch vehicles | Avionics power, telemetry power, pyrotechnic power-control electronics | ECSS-E-ST-20; ECSS-E-ST-20-07; ECSS-E-ST-10-03; NASA/launch-provider environmental and electrical interface standards; MIL-STD-461/-810 where contractually invoked |
| Marine / commercial shipping | Navigation equipment, communications PSUs, converters, UPS | IEC 60945; IEC 60092 series, especially IEC 60092-504; IEC 60533; IEC 62040 series; IEC 62477-1; IACS UR E10; classification-society rules (DNV, ABS, LR, BV) |
| Naval / military marine | Radar, sonar, combat systems, mission-critical UPS and converters | MIL-STD-1399-300-1 shipboard electric power; MIL-STD-461; MIL-STD-810; IEC 60945/IEC 60533 where commercially derived marine equipment applies; naval programme specifications |
| Offshore platforms | Instrumentation power, control systems, hazardous-area supplies | IEC 61892 series; IEC 60079 series; IEC 61511; IEC 62477-1; IEC 62040 series; classification-society offshore rules |
| Subsea equipment | Subsea converters, high-voltage distribution, sensor and actuator power | IEC 61892 where applicable to offshore installations; IEC 60079 series where hazardous areas apply; API 17F / ISO 13628-6 for subsea production control systems; IEC 62477-1 for topside/converter equipment; project-specific subsea power specifications |
| Medical equipment | Patient monitors, imaging equipment, pumps, laboratory equipment | IEC 60601-1; IEC 60601-1-2; applicable IEC/ISO 60601/80601 particular standards; IEC 62133-2 for rechargeable portable batteries |
| Life-support equipment | Ventilators, oxygen systems, dialysis, critical-care equipment | IEC 60601-1; IEC 60601-1-2; ISO 80601-2-12 for critical-care ventilators; IEC 60601-1-8 alarms; device-specific IEC/ISO 80601 particular standards; IEC 62133-2 where battery powered |
| Implantable medical devices | Battery-management and ultra-low-power conversion | ISO 14708 series; IEC 60601 family for external programmers/accessories where applicable; IEC 62133-2 generally does not substitute for implant-specific battery requirements |
| Medical imaging | CT, MRI, X-ray, ultrasound power systems | IEC 60601-1; IEC 60601-1-2; IEC 60601-2-44 (CT); IEC 60601-2-33 (MRI); IEC 60601-2-54 (radiography/radioscopy); IEC 60601-2-37 (ultrasound) |
| Laboratory / analytical equipment | Instrument PSUs, precision rails, high-voltage supplies | IEC 61010-1; applicable IEC 61010-2-x; IEC 61326-1; IEC 61204 series; IEC 62477-1 where power converters are integral products |
| Industrial automation | PLC supplies, I/O power, industrial 24 V supplies | IEC 61131-2; IEC 60204-1; IEC 61010-1/-2-201; IEC 61326-1; IEC 61204-3/-7; IEC 62477-1; IEC 61800-3/-5-1 for drives |
| Factory automation | Servo drives, robotics power, machine-control supplies | IEC 60204-1; IEC 61800-3; IEC 61800-5-1; IEC 62477-1; IEC 61000-6-2/-4; ISO 10218 where industrial robots apply |
| Robotics | Motor drives, battery systems, embedded converters | IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; ISO 10218 series industrial robots; ISO 3691-4 for mobile robots/AGVs; IEC 62133-2/IEC 62619 depending battery class |
| Process industry | Instrumentation supplies, distributed control systems | IEC 61010-1; IEC 61326-1; IEC 61511; IEC 60079 where hazardous; IEC 62477-1; IEC 62040 series for critical UPS |
| Chemical industry | Hazardous-area/intrinsically safe supplies | IEC 60079-0; IEC 60079-7; IEC 60079-11; IEC 60079-25; IEC 60079-18; IEC 61511; IEC 62477-1 for non-Ex converter equipment |
| Petrochemical industry | Instrumentation, analyzers, control and safety systems | IEC 60079 series; IEC 61511; IEC 61010-1; IEC 61326-1; IEC 62040 series; IEC 62477-1 |
| Oil and gas | Drilling electronics, pipeline equipment, monitoring systems | IEC 60079 series; IEC 61511; IEC 61892 offshore installations; IEC 61010-1; IEC 61326-1; IEC 62477-1 |
| Mining | Underground power supplies, intrinsically safe electronics | IEC 60079-0/-1/-7/-11/-18/-25; IEC 60079-35-1 for caplights; IEC 62133-2/IEC 62619 for batteries where applicable; national mine-safety regulations/certification rules |
| Underground equipment | Communications, sensors, lighting, machinery control | IEC 60079 series; IEC 60079-35-1 for caplights; IEC 60204-1 for machinery where applicable; IEC 62133-2/IEC 62619 for batteries; national mining regulations |
| Tunnel infrastructure | Emergency systems, communications, lighting supplies | EN 50171 central power supply systems; EN 50172 emergency escape lighting; IEC 60598-2-22 emergency luminaires; IEC 62040 series; NFPA 502 where adopted; EN 54-4 for fire-alarm power equipment |
| Construction equipment | Machine electronics, battery tools, site power systems | IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; IEC 62841 series for electric tools; IEC 60335-2-29 battery chargers |
| Power generation | Control systems, excitation systems, protection equipment | IEC 62477-1; IEC 61800 series; IEC 60255 series for protection relays; IEC 61000-6 series; IEC 62040 series; IEC 60034 series for generators/motors; plant-specific generation standards |
| Electrical utilities | Substation DC supplies, protection relays, battery chargers | IEC 61850-3; IEEE 1613; IEC 60255-26; IEC 60255-27; IEEE 946 DC auxiliary power systems; IEEE 485/IEEE 1115 battery sizing; IEC 62040 series; IEC 62477-1 |
| Transmission systems | HVDC controls, protection, monitoring supplies | IEC 62747 terminology for voltage sourced converters; IEC 61975 HVDC tests; IEC 61850-3; IEC 60255 series; IEC 62477-1; IEC 61000-6 series |
| Distribution grids | Smart-grid electronics, reclosers, meters, control PSUs | IEC 61850-3; IEEE 1613; IEC 60255-26/-27; IEC 62052/62053 smart-meter families; IEC 62477-1; IEC 61000-4-x |
| Renewable energy | Solar inverters, wind-turbine converters, storage converters | IEC 62477-1; IEC 62109-1/-2; IEC 61727; IEC 62116; IEC 61400-21 series; IEC 62933 series; IEC 61800 series for drive/converter subsystems |
| Solar photovoltaic | String/central/micro-inverters, optimizers, battery interfaces | IEC 62109-1; IEC 62109-2; IEC 61727; IEC 62116; IEC 62477-1; IEC 61000-6/IEC 61000-3 families; UL 1741 and IEEE 1547 in North America |
| Wind power | Converter systems, pitch-control supplies, auxiliary PSUs | IEC 61400-21 series; IEC 61400-24; IEC 62477-1; IEC 61800-3/-5-1; IEC 62040 series for auxiliary/backup systems |
| Hydroelectric | Control, excitation and protection power systems | IEC 62477-1; IEC 60255 series; IEC 62040 series; IEC 60034 series; IEC 61362 turbine control guidance; plant/grid-code requirements |
| Energy storage | BESS converters, battery chargers, PCS, BMS auxiliary supplies | IEC 62933-5-2; IEC 62933-5-3; IEC 62619; IEC 62477-1; IEC 62040 where UPS topology applies; UL 9540; UL 1973; NFPA 855; IEEE 1547 where grid-interactive |
| Nuclear power | Safety-related DC systems, emergency supplies, UPS, diesel-generator controls | IEEE/IEC 63332-387; IEEE 387 legacy licensing bases; IEEE 2420; IEEE 308; IEEE 946; IEEE/IEC 60780-323; IEC/IEEE 62582 series; NRC RG 1.9; IEC 62040 where non-Class-1E UPS is used |
| Fusion research | High-current/high-voltage supplies, magnet supplies | IEC 62477-1; IEC 61010-1; IEC 60204-1; IEC 61326-1; IEC 61000-6 series; facility-specific accelerator/fusion standards |
| Scientific research | Precision/high-voltage/current supplies, accelerator systems | IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 60204-1; IEC 61000-6 series; facility-specific research infrastructure standards |
| Particle accelerators | Magnet PSUs, RF power, pulsed-power systems | IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 60204-1; IEC 61000-6 series; IEC 61558 where transformers/power units are used; facility-specific accelerator rules |
| Semiconductor manufacturing | RF generators, precision supplies, process-tool PSUs | SEMI F47; SEMI F42; SEMI F49; SEMI S2; SEMI S22; IEC 61000-4-11/-34; IEC 61010-1; IEC 61326-1; IEC 62477-1 |
| Electronics manufacturing | Test supplies, burn-in racks, production testers | IEC 61010-1; IEC 61326-1; IEC 60204-1; IEC 62477-1; IEC 61204 series; SEMI F47 when equipment is used in semiconductor fabs |
| PCB manufacturing | Plating rectifiers, process-control supplies | IEC 62477-1; IEC 60204-1; IEC 61010-1; IEC 61326-1; IEC 61000-6 series |
| Battery manufacturing | Formation chargers, cyclers, test systems | IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 62619; IEC 62133-2; IEC 60204-1; battery-product standards applicable to the chemistry/product under test |
| Automated test equipment | Programmable PSUs, electronic loads, source-measure units | IEC 61010-1; IEC 61010-2-030; IEC 61326-1; IEC 61204 series where PSU product requirements apply; SEMI F47/F42 for semiconductor ATE |
| Instrumentation | Bench supplies, precision converters, measurement equipment | IEC 61010-1; IEC 61010-2-030; IEC 61326-1; IEC 61204-3/-7; IEC 61558-1 |
| Metrology | Ultra-low-noise and precision regulated supplies | IEC 61010-1; IEC 61326-1; ISO/IEC 17025 for calibration/test laboratories; IEC 61204 series for standalone supplies |
| Broadcasting | Transmitter supplies, studio electronics, UPS | IEC 62368-1; IEC 62040 series; CISPR 32; CISPR 35; IEC 61204 series; IEC 62477-1 for high-power converter systems |
| Professional audio | Amplifier supplies, mixing equipment, stage systems | IEC 62368-1; CISPR 32; CISPR 35; IEC 61204 series; IEC 61558-1 |
| Cinema / entertainment | Projection systems, lighting drivers, control power | IEC 62368-1; IEC 61347 series; IEC 60598 series; IEC 62040 series; CISPR 32/35; CISPR 15/IEC 61547 for lighting |
| Stage lighting | LED drivers, dimmers, control supplies | IEC 61347-1; IEC 61347-2-13; IEC 60598-1; IEC 60598-2-17 where relevant; CISPR 15; IEC 61547; IEC 62477-1 for larger converters |
| LED lighting | LED drivers, emergency-lighting supplies | IEC 61347-1; IEC 61347-2-13; IEC 62031; IEC 60598-1; IEC 60598-2-22; CISPR 15; IEC 61547; EN 50171 for central emergency supplies |
| Building automation | HVAC controls, access systems, BMS supplies | IEC 60730-1; EN 50491 series; IEC 62368-1 for ICT-type controllers; IEC 61558-1; IEC 62040 series; IEC 61000-6 series |
| HVAC | Inverter drives, compressor drives, control PSUs | IEC 60335-1; IEC 60335-2-40; IEC 61800-3; IEC 61800-5-1; IEC 60730-1; IEC 62477-1 |
| Elevators / escalators | Motor drives, braking electronics, emergency supplies | EN 81-20/EN 81-50; EN 12015; EN 12016; IEC 61800-3/-5-1; IEC 62040 series; IEC 62477-1 |
| Fire detection / alarm | Battery-backed PSUs, control panels | EN 54-4 (Power supply equipment); EN 54-2; EN 54-13; NFPA 72 where adopted; IEC 62040 for separate UPS systems |
| Security systems | CCTV supplies, access control, intrusion systems | EN 50131-6 (Power supplies); IEC 62368-1 for ICT/video equipment; IEC 62040 series; EN 50130-4 EMC |
| Emergency systems | Emergency lighting, communications and backup supplies | EN 50171; EN 50172; IEC 60598-2-22; IEC 62040 series; EN 54-4 for fire systems; IEC 62368-1 for emergency communications equipment |
| Smart buildings | PoE, sensors, controllers, distributed DC power | IEC 62368-1; IEEE 802.3 PoE; EN 50491; IEC 61558-1; IEC 62040 series; IEC 61000-6 series |
| Home appliances | Washer, dryer, dishwasher, refrigerator, oven electronics | IEC 60335-1 plus applicable IEC 60335-2-x; IEC 60730-1; IEC 61558-1; CISPR 14-1/-2; IEC 61000-3-2/-3 |
| Kitchen appliances | SMPS, motor drives, induction heating | IEC 60335-1; applicable IEC 60335-2-x (including IEC 60335-2-6 for cooking ranges/hobs); IEC 60730-1; IEC 61558-1; CISPR 14 series |
| Heating systems | Boiler controls, heat-pump drives, pumps | IEC 60335-1; IEC 60335-2-40 for heat pumps; IEC 60730-1; IEC 61800 series for drives; IEC 61558-1 |
| Air conditioning | Inverter compressors, fan drives, control power | IEC 60335-1; IEC 60335-2-40; IEC 61800-3/-5-1; IEC 60730-1; IEC 62477-1 |
| Portable tools | Battery chargers, motor drives, converters | IEC 62841-1 and applicable IEC 62841-2-x; IEC 60335-2-29 battery chargers; IEC 62133-2; IEC 61558-1 |
| Power tools | Battery management, brushless motor drives | IEC 62841 series; IEC 60335-2-29; IEC 62133-2; UN 38.3 for lithium battery transport |
| Gardening equipment | Battery packs, chargers, motor controllers | IEC 62841 series / IEC 60335-2-x as applicable; IEC 60335-2-29; IEC 62133-2; IEC 62477-1 for larger converter/charger systems |
| Agriculture | Irrigation control, autonomous machinery, sensor networks | ISO 14982; ISO 25119 series; IEC 60204-1; IEC 61800 series; IEC 62477-1; IEC 61000-6 series |
| Food processing | Automation, motor drives, instrumentation power | IEC 60204-1; IEC 61800-3/-5-1; IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 61000-6 series |
| Pharmaceutical manufacturing | Process control and validated instrumentation | IEC 60204-1; IEC 61010-1; IEC 61326-1; IEC 61511 where SIS applies; IEC 62040 series; IEC 62477-1 |
| Cold-chain systems | Refrigeration power electronics, monitoring and backup | IEC 60335-1; IEC 60335-2-24 or product-specific refrigeration part; IEC 60335-2-40 where applicable; IEC 62040 series; IEC 61800 series |
| Logistics / warehousing | Robotics, AGVs, scanners, conveyor drives | IEC 60204-1; IEC 61800-3/-5-1; ISO 3691-4 for driverless industrial trucks/AGVs; IEC 62477-1; IEC 62619 for industrial batteries |
| Automated guided vehicles | Battery systems, traction drives, onboard converters | ISO 3691-4; IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; IEC 62619; IEC 62133-2 for smaller portable battery systems |
| Material handling | Forklifts, cranes, conveyors, hoists | EN 1175 industrial-truck electrical requirements; ISO 3691 series; IEC 60204-1; IEC 61800 series; IEC 62477-1; IEC 62619 |
| Ports / container terminals | Crane drives, automation and communications power | IEC 60204-32 for hoisting machines; IEC 61800 series; IEC 62477-1; IEC 62040 series; IEC 61000-6 series |
| Public transportation | Ticketing, communication, vehicle electronics | IEC 62368-1; IEC 62040 series; EN 50155/IEC 60571 for rail vehicles; ISO 16750/UNECE R10 for road vehicles; relevant platform EMC standard |
| Road infrastructure | Traffic lights, toll systems, variable-message signs | EN 50556 road traffic signal systems; EN 12966 variable message signs; IEC 62368-1; IEC 62040 series; IEC 61000-6 series |
| Traffic management | Controllers, cameras, communications, UPS | IEC 62368-1; IEC 62040 series; EN 50556; EN 12966; CISPR 32/35; IEC 61000-4-x |
| Street lighting | LED drivers, smart-lighting controllers | IEC 61347-1; IEC 61347-2-13; IEC 60598-1; IEC 60598-2-3; CISPR 15; IEC 61547 |
| Charging infrastructure | EVSE AC chargers, DC fast chargers, converters | IEC 61851-1; IEC 61851-23; IEC 61851-24; IEC 62196 series; ISO 15118 series; IEC 62752; IEC 60364-7-722; IEC 62477-1 |
| Fuel stations | Pump electronics, POS, monitoring, hazardous-area systems | IEC 60079 series; IEC 61511 where SIS applies; IEC 60204-1; IEC 62368-1 for POS/ICT; IEC 62040 series; national petroleum-station rules |
| Aerospace ground support | Ground power units, test equipment, charging systems | SAE AS5808/ground-power interface specifications as applicable; IEC 61010-1 for test equipment; IEC 62477-1; IEC 62040 series; military ground-support equipment may invoke MIL-STD-704/461/810 |
| Defence electronics | Radar, communications, electronic warfare, mission systems | MIL-STD-461; MIL-STD-810; platform power standard such as MIL-STD-704, MIL-STD-1275 or MIL-STD-1399-300-1; applicable programme specifications |
| Military ground vehicles | 28 V DC equipment, converters, power distribution | MIL-STD-1275; MIL-STD-461; MIL-STD-810; applicable vehicle platform specifications |
| Weapons-system electronics | Control electronics, sensing and mission power systems | MIL-STD-461; MIL-STD-810; platform power standard MIL-STD-704 / MIL-STD-1275 / MIL-STD-1399-300-1 as applicable; programme-specific requirements |
| Radar systems | High-power RF supplies, pulsed power | MIL-STD-461/-810 for defence radar; IEC 62368-1 or IEC 61010-1 for commercial/test radar depending classification; IEC 62477-1 for converter systems; platform power standard |
| Electronic warfare | Wideband/high-power supplies | MIL-STD-461; MIL-STD-810; MIL-STD-704 or MIL-STD-1275 or MIL-STD-1399-300-1 according to platform |
| Military communications | Rugged DC/DC converters, battery chargers | MIL-STD-461; MIL-STD-810; MIL-STD-1275 for ground vehicles; MIL-STD-704 for aircraft; MIL-STD-1399-300-1 for ships; IEC 62133-2/UN 38.3 where commercial batteries are used |
| Civil protection | Emergency communications, portable power systems | IEC 62368-1; IEC 62133-2; IEC 62040 series; ETSI EN 301 489 family for radio EMC; IEC 60529; IEC 60068 series |
| Police equipment | Radios, vehicle electronics, body cameras, charging | IEC 62368-1; IEC 62133-2; ETSI EN 301 489 series; ISO 16750/ISO 7637/UNECE R10 for vehicle-installed equipment; IEC 60335-2-29 for standalone chargers where applicable |
| Firefighter equipment | Radios, thermal cameras, breathing-system electronics | IEC 62368-1; IEC 62133-2; ETSI EN 301 489; IEC 60529; IEC 60068; product/PPE standards such as EN 137/EN 136 where electronics are integrated |
| Search and rescue | Portable radios, GNSS, lighting, battery systems | IEC 62368-1; IEC 62133-2; ETSI EN 301 489; IEC 60529; IEC 60068; COSPAS-SARSAT/ETSI beacon standards where applicable |
| Mountain / rescue equipment | Avalanche beacons, satellite communicators, headlamps | ETSI EN 300 718 series for avalanche beacons; IEC 62368-1 for communicators; IEC 62133-2; IEC 60529; IEC 60068; ETSI EN 301 489 family |
| Diving equipment | Dive computers, rebreather electronics, underwater lighting | EN 14143 for rebreathers where applicable; IEC 60529/IP or product-specific pressure/watertight requirements; IEC 62133-2; IEC 62368-1 for communication electronics where applicable |
| Life-safety systems | Alarm, emergency power, monitoring | EN 54-4; EN 50171; EN 50172; EN 50131-6; IEC 62040 series; IEC 60598-2-22 |
| Personal protective equipment | Powered respirators, smart helmets, communications | EN 12941 / EN 12942 for powered filtering respiratory devices; IEC 62133-2; IEC 62368-1 for integrated ICT; IEC 60079 where used in explosive atmospheres |
| Hazardous-area equipment | Intrinsically safe barriers and power supplies | IEC 60079-0; IEC 60079-7; IEC 60079-11; IEC 60079-18; IEC 60079-25; IEC 60079-26; IECEx certification rules; ATEX EN adoptions in Europe |
| Explosive-atmosphere equipment | ATEX/IECEx-certified supplies and electronics | IEC 60079 series; EN IEC 60079 national/regional adoptions; IECEx scheme; ATEX 2014/34/EU in the EU |
| Marine leisure | Yacht converters, battery chargers, navigation power | IEC 60092 family where applicable; IEC 60945 navigation electronics; ISO 13297 small-craft electrical systems; ISO 10133 legacy DC installations; IEC 62040 series; IEC 62477-1 |
| Recreational vehicles | Inverters, chargers, solar controllers | IEC 62477-1; IEC 62109 for PV converters; IEC 60335-2-29 chargers; IEC 62133-2/IEC 62619; EN 1648-1/-2 for leisure accommodation vehicle DC installations |
| Camping / outdoor electronics | Portable power stations, solar chargers, lighting | IEC 62368-1; IEC 62133-2; IEC 62619 for larger stationary/industrial packs; IEC 62109 for PV converters; IEC 60529; IEC 60068 |
| Sports equipment | Sensors, battery-powered instruments, training systems | IEC 62368-1 for ICT-type products; IEC 62133-2; IEC 60529; IEC 60068; product-specific sporting-equipment standards |
| Scientific field equipment | Remote instruments, solar/battery power systems | IEC 61010-1; IEC 61326-1; IEC 62133-2/IEC 62619; IEC 62109 where PV-powered; IEC 60529; IEC 60068 |
| Meteorology | Weather stations, radiosondes, remote telemetry | IEC 61010-1; IEC 61326-1; IEC 62368-1 for telemetry; IEC 62133-2; IEC 60529; IEC 60068; WMO requirements where applicable |
| Geophysics | Seismic instruments, remote sensing power | IEC 61010-1; IEC 61326-1; IEC 62133-2/IEC 62619; IEC 60529; IEC 60068; IEC 62368-1 for communication subsystems |
| Oceanography | Buoys, underwater instruments, autonomous vehicles | IEC 61010-1; IEC 61326-1; IEC 60945 for marine navigation/radio equipment; IEC 62133-2/IEC 62619; IEC 60529; IEC 60068 |
| Environmental monitoring | Remote sensor power, solar/battery systems | IEC 61010-1; IEC 61326-1; IEC 62133-2; IEC 62109 where PV conversion applies; IEC 60529; IEC 60068 |
| Geological monitoring | Seismic, landslide and volcano monitoring | IEC 61010-1; IEC 61326-1; IEC 62133-2; IEC 60529; IEC 60068; IEC 62368-1 for telemetry/networking |
| Remote sensing | Ground stations, airborne and satellite electronics | IEC 62368-1/IEC 61010-1 for ground equipment; RTCA DO-160 for airborne; ECSS-E-ST-20/-20-07 and ECSS-E-ST-10-03 for spaceborne; IEC 62040 series for ground UPS |
| Navigation systems | GNSS receivers, inertial navigation, marine/aviation navigation | IEC 60945 for maritime; RTCA DO-160 for airborne; IEC 62368-1 for consumer/ground GNSS; MIL-STD-461/-704/-810 for military platform equipment |
| Timing infrastructure | Atomic clocks, GNSS timing, telecom synchronization | IEC 62368-1; IEC 61010-1 for laboratory timing equipment; ETSI EN 300 132 series for telecom power interfaces; IEC 62040 series |
| Banking / financial infrastructure | UPS, ATMs, server power | IEC 62368-1; IEC 62040-1/-2/-3; CISPR 32; CISPR 35; IEC 61204 series |
| Retail | POS systems, digital signage, refrigeration controls | IEC 62368-1 for POS/signage; IEC 60335 family for refrigeration/appliances; IEC 62040 series; CISPR 32/35; IEC 61204 series |
| Hospitality | Building automation, kitchen equipment, IT infrastructure | IEC 60335 series; IEC 62368-1; IEC 62040 series; IEC 60730-1; IEC 61558-1; EN 50171 for central emergency power where used |
| Education | Laboratory equipment, IT and audiovisual systems | IEC 61010-1; IEC 61326-1; IEC 62368-1; IEC 62040 series; IEC 61204 series |
| Government infrastructure | Communications, data centres, security equipment | IEC 62368-1; IEC 62040 series; ETSI EN 300 132 where telecom DC power applies; EN 50131-6 for intrusion-system supplies; sector-specific continuity requirements |
| Postal systems | Sorting automation, scanners, conveyors | IEC 60204-1; IEC 61800 series; IEC 62477-1; IEC 62368-1 for scanner/ICT subsystems; IEC 62040 series |
| Printing industry | Industrial printers, servo drives, high-voltage supplies | IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; IEC 62368-1 for office/IT-class printing equipment; IEC 61000-6 series |
| Packaging | Machine automation, servo/motor drives | IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; IEC 61000-6 series |
| Textile industry | Machine drives, automation, heating controls | IEC 60204-1; IEC 61800-3/-5-1; IEC 62477-1; IEC 61000-6 series |
| Paper / pulp | Process automation and large drives | IEC 60204-1; IEC 61800 series; IEC 62477-1; IEC 61511 where SIS applies; IEC 62040 series |
| Steel industry | High-power drives, furnaces, instrumentation | IEC 61800 series; IEC 62477-1; IEC 60519 series for electroheating; IEC 60204-1; IEC 61000-6 series |
| Mining / metallurgy | Drives, rectifiers, control and instrumentation | IEC 60079 where explosive atmosphere applies; IEC 61800 series; IEC 62477-1; IEC 60204-1; IEC 60519 series for electroheating; national mining standards |
| Welding | High-current inverter power supplies | IEC 60974-1 (welding power sources); IEC 60974-10 EMC; IEC 60974 series; IEC 62477-1 where applicable |
| Plasma cutting | High-current/high-voltage switching supplies | IEC 60974-1; IEC 60974-7 torches; IEC 60974-10 EMC; IEC 62477-1 |
| Electroplating | High-current rectifiers | IEC 62477-1; IEC 60146 series semiconductor converters; IEC 60204-1 for machinery; IEC 61000-6 series |
| Electrolysis | High-current DC supplies | IEC 62477-1; IEC 60146 series; IEC 60204-1; IEC 61000-6 series; process-specific safety standards |
| Hydrogen production | Electrolyzer rectifiers and DC converters | ISO 22734 hydrogen generators using water electrolysis; IEC 62477-1; IEC 60146 series; IEC 60079 where hazardous areas apply; IEC 61511 where SIS applies |
| Industrial heating | Induction-heating inverters | IEC 60519-1; IEC 60519-3 for induction and conduction heating; IEC 62477-1; IEC 61000-6 series |
| Induction cooking | High-frequency inverter power stages | IEC 60335-1; IEC 60335-2-6; CISPR 14-1/-2; IEC 61000-3-2/-3 |
| Laser systems | Laser-diode drivers and high-voltage supplies | IEC 60825-1; IEC 61010-1 for laboratory/measurement lasers; IEC 61326-1; IEC 62477-1 for converter systems |
| Photonics | Precision laser and detector power | IEC 60825-1; IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 61204 series |
| X-ray systems | High-voltage generators | IEC 60601-1 and IEC 60601-2-x for medical X-ray; IEC 61010-1 / applicable IEC 61010-2-x for industrial/lab X-ray; IEC 62477-1 for converter subsystems where applicable |
| Electron microscopes | Precision high-voltage supplies | IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 61204 series |
| Mass spectrometry | Precision/high-voltage rails | IEC 61010-1; IEC 61326-1; IEC 62477-1; IEC 61204 series |
| Vacuum systems | Turbopump drives, ion-pump HV supplies | IEC 61010-1; IEC 61326-1; IEC 61800 series for drives; IEC 62477-1; IEC 61204 series |
| RF / microwave systems | RF amplifier supplies, bias supplies | IEC 62368-1 for communications/AV equipment; IEC 61010-1 for lab equipment; IEC 62477-1; IEC 61204 series; CISPR 11 or CISPR 32 depending product class |
| Wireless communications | RF PA supplies, baseband and digital rails | IEC 62368-1; ETSI EN 300 132 series for telecom infrastructure; ETSI EN 301 489 family; CISPR 32/35; IEC 61204 series |
| IoT | Low-power DC/DC, energy harvesting, battery management | IEC 62368-1; IEC 62133-2; IEC 62680-1-3 for USB-C powered products; CISPR 32/35 or applicable radio EMC standard; IEC 61204 series for external PSUs |
| Smart meters | Isolated supplies, backup energy storage | IEC 62052-11; IEC 62053 series; IEC 62056 series; IEC 61000-4-x immunity methods; IEC 62133-2 for internal rechargeable batteries where applicable |
| Wearables | Battery chargers and ultra-low-power converters | IEC 62368-1 where ICT/consumer classification applies; IEC 62133-2; IEC 62680-1-3 for USB-C; IEC 60529 where ingress rating claimed |
| Mobile phones / tablets | PMICs, chargers, USB power | IEC 62368-1; IEC 62133-2; IEC 62680-1-3; CISPR 32/35; IEC 61000-4-2; USB-IF USB Power Delivery specifications where certification applies |
| Cameras / imaging | Sensor rails, motor drives, flash power | IEC 62368-1; IEC 62133-2; CISPR 32/35; IEC 61204 series for external power supplies |
| Gaming systems | Console PSUs, VR equipment | IEC 62368-1; IEC 62133-2 for battery accessories; CISPR 32/35; IEC 61204 series; IEC 62680-1-3 for USB-C power |
| AR / VR | Battery systems, display and compute power | IEC 62368-1; IEC 62133-2; CISPR 32/35; IEC 62680-1-3; IEC 60529 where ingress protection is claimed |
| Electronic signage | LED drivers, display PSUs | IEC 62368-1 for display electronics; IEC 61347-1/-2-13 for LED drivers; IEC 60598 family where classified as luminaire; CISPR 32/35 or CISPR 15/IEC 61547 depending product function |
| Vending machines | Control and refrigeration power | IEC 60335-1; IEC 60335-2-75; IEC 61558-1; IEC 62040 where UPS is used; CISPR 14 family |
| ATMs | Embedded PSUs and UPS | IEC 62368-1; IEC 62040-1/-2/-3; CISPR 32/35; IEC 61204 series |
| Payment terminals | Chargers and embedded power supplies | IEC 62368-1; IEC 62133-2; IEC 62680-1-3 where USB-C powered; CISPR 32/35; IEC 61204 series |
| Telematics | Vehicle DC/DC and backup battery systems | ISO 16750-2; ISO 7637-2/-3; CISPR 25; ISO 11452 series; UNECE R10; ISO 21780 where 48 V applies; IEC 62133-2 for backup batteries where applicable |
| Satellite communications | Ground-station RF and modem supplies | IEC 62368-1; IEC 62040 series; IEC 62477-1 for larger RF/converter equipment; ETSI EN 301 489 family; CISPR 32/35 |
| Cable / broadband networks | Network power, remote amplifier supplies | IEC 62368-1; IEC 62040 series; ETSI EN 300 132 family where telecom powering is used; ITU-T K.20/K.21; CISPR 32/35 |
| Undersea communications cables | Constant-current high-voltage feeding equipment | ITU-T G.971; ITU-T G.972; ITU-T G.973/G.974/G.977 families; ITU-T G.976; ITU-T G.978; ITU-T G-series Supplement 41 (power-feeding subsystem design); system/vendor PFE specifications |
| Emergency communications | Battery-backed and generator-backed supplies | IEC 62368-1; IEC 62040 series; IEC 62133-2; ETSI EN 301 489 family; ETSI/COSPAS-SARSAT beacon standards where applicable; EN 50171 where central emergency supply used |
| Cyber / IT security infrastructure | Servers, appliances, UPS systems | IEC 62368-1; IEC 62040-1/-2/-3; IEC 61204-3/-7; CISPR 32/35; ETSI EN 300 132 where telecom/data-centre DC feeds are used |

## Condensed standards-search taxonomy

For standards research, the detailed list can be reduced to the following 25 top-level industry families:

1. Consumer
2. IT / data centre
3. Telecom / networking
4. Automotive
5. Commercial / off-highway vehicles
6. Railway
7. Civil aviation
8. Military aerospace
9. Space / satellites
10. Marine
11. Offshore / subsea
12. Medical
13. Life support
14. Industrial automation
15. Oil / gas / chemical
16. Mining / underground / hazardous area
17. Utility / grid
18. Renewable energy
19. Energy storage
20. Nuclear
21. Defence
22. Scientific / laboratory
23. Building / HVAC / safety systems
24. Transport infrastructure
25. Outdoor / rescue / harsh-environment equipment

## Standards families newly surfaced by this industry mapping

The expanded mapping adds important power-related families beyond the original cross-industry baseline, including:

- IEC 62368-1 — AV/ICT product safety;
- ETSI EN 300 132-1/-2/-3 — telecom/ICT power-supply interfaces;
- ITU-T L.1200 family — telecom/data-centre DC power;
- IEC 62477-1 — power electronic converter systems and equipment;
- IEC 61800-3/-5-1 — power drive EMC and safety;
- IEC 60204-1 — electrical equipment of machines;
- IEC 62109-1/-2 — photovoltaic converter safety;
- IEC 62933 series — electrical energy storage systems;
- IEC 60079 series — explosive-atmosphere equipment and intrinsic safety;
- IEC 61850-3 / IEEE 1613 / IEC 60255-26/-27 — utility/substation electronics;
- EN 54-4 — fire-alarm power-supply equipment;
- EN 50131-6 — intrusion-system power supplies;
- EN 50171 — central emergency power-supply systems;
- IEC 61347 series — lamp/LED controlgear;
- IEC 60974-1/-10 — welding power sources and EMC;
- IEC 60519 series — industrial electroheating;
- SEMI F42/F47/F49 and SEMI S22 — semiconductor-tool power quality/electrical design;
- ITU-T G.97x / G Suppl. 41 — submarine telecom power feeding;
- ISO 22734 — hydrogen generators using water electrolysis.

## Priority gaps for the next standards-search pass

Even with the expanded column, dedicated deep verification is still warranted for:

- national mining standards and mine-safety certification schemes;
- naval and country-specific military power-interface standards outside the US;
- national nuclear Class-1E / safety-system standards outside IEC/IEEE/NRC coverage;
- offshore/subsea electrical power distribution and wet-mate/high-voltage connector standards;
- country-specific fire/security/emergency-power national adoptions;
- China GB/GB-T, Japan JIS, India BIS, Russia/EAEU GOST, Brazil ABNT NBR, Australia/New Zealand AS/NZS, South Africa SANS and South Korea KS equivalents;
- detailed battery standards by chemistry, transport class and stationary/mobile use;
- OEM/private standards for automotive, aerospace, rail, telecom and industrial equipment.

## Scope note

This is an industry-coverage and standards-discovery map, not a compliance determination. Individual products can require multiple overlapping standards covering electrical safety, EMC, input-power quality, transients, environmental qualification, reliability, battery safety, functional safety, fault tolerance and regulatory certification. Exact edition, severity level, waveform, source impedance and acceptance criterion must be taken from the applicable normative document and contract/regulatory basis.
