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

### Space check

The equipment bay is roughly 6.4" long × 7.6" wide × 11" tall, and the parts above
will not all sit flat on the floor of it. The MPPT is designed for vertical wall
mounting — put it on the inside end wall, and keep the floor for the shunt, Class T
holder and fuse block. Worth laying out on cardboard before drilling.

Also worth checking: the MPPT dissipates heat and wants convection clearance, while
the Anderson plates and bulkhead are all sealed fittings. Camco boxes normally carry
vent slots for lead-acid off-gassing — those are unnecessary for LiFePO4 but useful
here for MPPT cooling, so decide deliberately whether this box ends up sealed or
vented.

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
