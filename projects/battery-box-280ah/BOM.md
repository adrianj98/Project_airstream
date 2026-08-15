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

Dimensions are checked against the 6.38" × 7.375" × 11.19" equipment bay. See the
layout section in [README.md](README.md).

| # | Part | Candidate product | Spec / dimensions | Status |
| --- | --- | --- | --- | --- |
| — | Class T fuse block + fuse | Blue Sea 5502 | 225–400A block, ~7.0 × 2.3". Fit a 250A fuse. Mounts crosswise only | Needed |
| — | *or* MRBF terminal fuse block | Blue Sea 2151 dual | 300A max, mounts on the 3/8" battery post. 10kA vs Class T's 20kA | Alternative |
| — | Positive bus bar | 250–300A, 4 stud, covered | 5.43 × 2.72 × 1.75". **Buy 3/8" studs** if fusing branches with MRBF | Needed |
| — | Negative bus bar | same | Fed from the shunt's SYSTEM MINUS. Never fused | Needed |
| — | Blade fuse block | Blue Sea 5025 | 6 circuits, 30A/circuit, 100A total, negative bus + cover. 3.32 × 4.9 × 1.52" | Needed |
| — | MRBF terminal fuse blocks | Blue Sea 5191 | 30–300A, screws onto a 3/8" busbar stud. For the 120A Anderson branches | Needed |
| — | Fuse or breaker for PV input | | Per panel Voc/Isc — size once panels are chosen | Needed |
| — | Battery disconnect switch | | 300A+ | Needed |
| — | 2/0–4/0 cable, lugs, heat shrink | | Main runs | Needed |
| — | Hydraulic lug crimper | | To make the above up properly | Needed |

Reference dimensions for the parts already owned:

| Part | Dimensions |
| --- | --- |
| Victron SmartSolar MPPT 100/20-48 | 3.94 × 5.16 × 2.36" (100 × 131 × 60mm), 0.65kg |
| Victron SmartShunt 500A | 4.7 × 1.8 × 2.1" |
