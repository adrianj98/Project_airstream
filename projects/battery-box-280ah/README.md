# 280Ah battery box

**Status:** Planning
**Started:** 2026-08-15
**Target:**

## Goal

Build a sealed, portable power box around the WattCycle 280Ah battery, with solar
charging, battery monitoring, exterior DC outlets, and a 30V feed for Starlink Mini.

## Battery

**WattCycle 12V 280Ah Mini LiFePO4**

| Spec | Value |
| --- | --- |
| Dimensions | 15.12" × 7.64" × 10.04" (384 × 194 × 248mm) |
| Weight | 59.5 lb |
| Energy | 3584Wh (12.8V × 280Ah) |
| BMS | 200A continuous charge and discharge |
| Cells | EVE LF280K, grade A+ |
| Cycles | 15,000+ |
| Other | Low-temperature charge protection |

## Parts

Five parts, identified from the supplied links.

1. **RVSPARK 30V bulkhead pass-through power supply** — step-up converter, DC 10–28V
   in to 30V out, IP68 aluminum socket. Sold as a Starlink Mini power feed.
   [link](https://a.co/d/0dK2yxeC)
2. **Camco Double Battery Box (55375)** — polymer enclosure, interior
   21-1/2" × 7-3/8" × 11-3/16". [link](https://a.co/d/0bT6FOiA)
3. **Victron SmartSolar MPPT 100/20 charge controller** — 100V max PV, 20A, 48V,
   Bluetooth. [link](https://a.co/d/0i8d4S4g)
4. **Zhushan 120A quick-disconnect connectors** — Anderson SB120 compatible, flush
   mount plates and dust covers, 4 sets. [link](https://a.co/d/0dvaA9yu)
5. **Victron SmartShunt IP65 battery monitor** — 6.5–70V, 500A, Bluetooth.
   [link](https://a.co/d/0dEQpOSZ)

See [BOM.md](BOM.md) for quantities and costs.

## Notes

The parts add up to a self-contained portable power box: battery in the Camco
enclosure, MPPT controller for solar input, SmartShunt for state-of-charge
monitoring, Anderson connectors for the DC output, and the RVSPARK bulkhead as a
30V feed for Starlink Mini. Both Victron units are Bluetooth, so they pair in the
VictronConnect app.

Everything electrical is panel-mount or bulkhead — flush-mount Anderson plates with
dust covers, an IP68 bulkhead, an IP65 shunt, and two Bluetooth units with no
displays. The box is meant to be closed up and operated entirely from outside and
from the phone.

### Fit — resolved, it fits

| | Battery | Box interior | Result |
| --- | --- | --- | --- |
| Length | 15.12" | 21.50" | Fits, 6.4" spare |
| Height | 10.04" | 11.19" | Fits, 1.15" above the case |
| Width | 7.64" | 7.375" | Fits — battery case is tapered |

Checked in person. The published 7.64" is the widest point; the case tapers, so it
seats fine in the box. No enclosure change needed.

### Layout

The battery is 15.12" long in a 21.5" box, leaving about **6.4" of length spare**.
That bay is where the MPPT and the shunt mount, alongside the battery rather than
above it — which is what makes a double box the right pick for a single battery.

### Sizing sanity check

- 3584Wh usable-ish against a Starlink Mini at ~20–40W is on the order of days of
  runtime, not hours.
- MPPT 100/20 at 12V is ~270W of charge — replaces a day of Starlink in about an
  hour of good sun, but is a bottleneck for a full recharge from empty (~13h).
- The 200A BMS is the real system ceiling. The 120A Andersons sit comfortably under
  it; the 500A shunt is oversized but harmless.

## Distribution — bus bar and fuse block

Both are needed. They do different jobs and are not interchangeable: the positive
side needs *protection*, the negative side needs *joining*.

### Positive — fused

```
Battery (+) ──> Class T fuse ──> positive bus bar ──┬─> [fuse] MPPT
                  (~250A)                           ├─> [fuse] Starlink bulkhead
                                                    ├─> [fuse] Anderson outlet
                                                    └─> [fuse] Anderson outlet
```

- **Class T fuse at the battery post, ~250A.** Sits above the 200A BMS ceiling so
  the BMS trips first on ordinary overcurrent, and below 2/0 cable ampacity. Class T
  rather than ANL because LiFePO4 short-circuit current demands the higher (~20kA)
  interrupt rating.
- **Blade fuse block** (6 circuits, ~30A/circuit) for the Starlink feed and other
  small loads.
- **The 120A Anderson outlets exceed a blade block** — give those their own MRBF or
  MIDI fuses off the positive bus bar.
- **Solar input gets its own fuse or breaker** on the PV side, ahead of the MPPT.

### Negative — not fused

```
Battery (−) ──> SmartShunt [BATTERY MINUS | SYSTEM MINUS] ──> negative bus bar ──> all returns
```

- Plain common bus bar, 250A+. Negatives are never fused.
- **Every** negative return lands on this bus bar, and the only path to battery
  negative is through the shunt. If any load returns straight to the battery post it
  bypasses the shunt and the state-of-charge reading is permanently wrong. This is
  the most common SmartShunt install mistake.

The four Anderson sets map neatly onto this: PV in, DC out, vehicle charge in, spare.

### Candidate products and whether they fit

Equipment bay: **6.38" long × 7.375" wide × 11.19" tall** (box interior minus the
15.12" battery).

| Part | Product | Dimensions | Verdict |
| --- | --- | --- | --- |
| Charge controller | Victron SmartSolar MPPT 100/20-48 | 3.94 × 5.16 × 2.36" (100 × 131 × 60mm) | End wall, vertical |
| Monitor | Victron SmartShunt 500A | 4.7 × 1.8 × 2.1" | Bay side wall |
| Main fuse | Blue Sea 5502 Class T block, 225–400A | ~7.0 × 2.3" | **Crosswise only** — see below |
| Main fuse (alt) | Blue Sea 2151 dual MRBF terminal block | Mounts on the 3/8" battery post | Zero floor space |
| Busbars ×2 | 250–300A 4-stud with cover (e.g. jamgoer 300A) | 5.43 × 2.72 × 1.75" (138 × 69 × 44.5mm) | One floor, one wall |
| Branch fuses | Blue Sea 5025 ST blade block, 6 ckt + neg bus | 3.32W × 4.9H × 1.52D" | Bay side wall |
| High-current branch fuses | Blue Sea 5191 MRBF, 30–300A | Screws onto a 3/8" busbar stud | No extra footprint |

### Two gotchas

**The Class T block is longer than the bay.** At ~7.0" it does not fit along the
6.38" length — it has to go crosswise, where 7.0" against the 7.375" width leaves
under 3/8" total clearance. It fits, but there is no room to be careless. The
alternative is the MRBF terminal block on the battery post, which costs nothing in
floor space.

Class T carries a 20kA interrupt rating and is what ABYC E-13 calls for on lithium.
MRBF fuses are 10kA, which is generally accepted for a single 12V battery — a lone
280Ah pack's prospective short-circuit current sits below that. Class T is the
conservative call and it does fit; MRBF is the defensible space-saver.

**Stud sizes have to match.** The MRBF blocks mount on 3/8" (M10) studs. Plenty of
compact busbars ship with M8 (5/16") studs instead — the jamgoer above is M8. If the
plan is to fuse the high-current branches with MRBF blocks screwed straight onto the
positive busbar, buy a busbar with **3/8" studs**.

### Suggested layout

- **End wall** (7.375 × 11.19") — MPPT, mounted vertically and high, keeping the
  floor beneath it clear
- **Bay side wall A** (6.38 × 11.19") — blade fuse block
- **Bay side wall B** — SmartShunt, plus the negative busbar
- **Floor** (6.38 × 7.375") — Class T block crosswise, positive busbar crosswise
  in front of it

Everything lands with margin, and the wall area is what makes it work — the floor
alone is 47 sq in and the parts total more than that. Mock it up on cardboard before
drilling.

Note the side walls above the battery are not usable: only 1.15" of clearance over
the case.

### Sealed or vented

The MPPT dissipates heat and wants convection clearance, while the Anderson plates
and bulkhead are all sealed fittings. Camco boxes normally carry vent slots for
lead-acid off-gassing — unnecessary for LiFePO4 but useful here for MPPT cooling.
Decide this deliberately rather than discovering it in August.

### Also not yet in the BOM

- Battery disconnect switch
- 2/0–4/0 cable, lugs, heat shrink, hydraulic crimper

## Open questions

- [ ] **Measure the Camco's actual interior width** at battery seating height, and
      check whether the side walls are ribbed. This decides whether the enclosure
      stays or gets swapped.
- [ ] Where the box mounts
- [ ] MPPT is the 48V variant — confirm it is being run at the system voltage intended
- [ ] SmartShunt is listed at 500A; one US listing for the same ASIN shows 300A.
      Confirm which arrived
- [ ] Solar panel wattage and Voc, to check against the 100V/20A controller limits
- [ ] Is an inverter planned? The 500A shunt suggests room for one

## Tasks

- [x] Name the five parts in the BOM
- [x] Record battery dimensions
- [ ] Measure the box and settle the width question
- [ ] Source fusing, bus bars and cable
- [ ] Fill in prices from the order confirmation
- [ ] Plan panel layout for the two Victron units, the Anderson plates and the
      Starlink bulkhead
