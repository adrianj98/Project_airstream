# Bill of Materials — 280Ah battery box

| # | Part | Spec / part no. | Qty | Unit cost | Total | Source | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | WattCycle 12V 280Ah Mini LiFePO4 battery | 15.12" × 7.64" × 10.04" (384 × 194 × 248mm), 59.5 lb, 200A BMS, EVE LF280K A+ cells, 3584Wh, low-temp protection | 1 | | | | |
| 2 | RVSPARK 30V bulkhead pass-through power supply | Step-up converter, DC 10–28V in → 30V out, IP68 aluminum socket. For Starlink Mini. ASIN B0GY8TP5GZ | | | | https://a.co/d/0dK2yxeC | |
| 3 | Camco Double Battery Box | Model 55375, corrosion-resilient polymer, interior 21-1/2" × 7-3/8" × 11-3/16". ASIN B07V4482W1 | | | | https://a.co/d/0bT6FOiA | |
| 4 | Victron Energy SmartSolar MPPT charge controller | 100/20, 100V max PV, 20A, 48V, Bluetooth. ASIN B075NPQHQK | | | | https://a.co/d/0i8d4S4g | |
| 5 | Zhushan battery quick-disconnect connectors | 120A, Anderson SB120 compatible, flush mount plates + dust covers, 4 sets. ASIN B0F6TTMF3G | | | | https://a.co/d/0dvaA9yu | |
| 6 | Victron Energy SmartShunt IP65 battery monitor | SHU065500BT, 6.5–70V, 500A, Bluetooth. ASIN B0BF636VBX | | | | https://a.co/d/0dEQpOSZ | |

**Status values:** Needed → Ordered → On hand → Installed

**Running total:**

Prices are not recorded — Amazon listing prices were not readable from the build
environment. Fill in from the order confirmation.

## Still needed

Not yet sourced. See the safety notes in [README.md](README.md).

| # | Part | Spec | Why | Status |
| --- | --- | --- | --- | --- |
| — | Class T fuse + holder | ~250A | Main battery protection. Above the 200A BMS ceiling, below 2/0 ampacity. Class T for the ~20kA interrupt rating LiFePO4 needs | Needed |
| — | Positive bus bar | 250A+ | Distribution after the Class T | Needed |
| — | Negative bus bar | 250A+ | Common return, fed from the shunt's SYSTEM MINUS. Never fused | Needed |
| — | Blade fuse block | 6 circuits, ~30A/circuit | Starlink feed and other small loads | Needed |
| — | MRBF or MIDI fuses | Sized per outlet | The 120A Anderson outlets exceed a blade block | Needed |
| — | Fuse or breaker for PV input | Per panel Voc/Isc | Protect the solar run ahead of the MPPT | Needed |
| — | Battery disconnect switch | 300A+ | Isolate the battery for service | Needed |
| — | 2/0–4/0 cable, lugs, heat shrink | | Main runs | Needed |
| — | Hydraulic lug crimper | | To make the above up properly | Needed |
