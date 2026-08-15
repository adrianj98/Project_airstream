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

### Fit — the battery is ~1/4" too wide for the box

| | Battery | Box interior | Result |
| --- | --- | --- | --- |
| Length | 15.12" | 21.50" | Fits, 6.4" spare |
| Height | 10.04" | 11.19" | Fits, 1.15" above the case |
| **Width** | **7.64"** | **7.375"** | **Over by ~0.27" (7mm)** |

The 55375 is a "double" box in the sense of two Group 24 batteries end to end, and
Group 24 is 6.8" wide — so the 7-3/8" interior was never sized for a 7.64" case.

Worth checking in person before giving up on it, because published interior
dimensions are usually the floor measurement:

- Molded polymer boxes taper for draft, so the opening is often wider than the base.
  Measure at the height the battery actually sits.
- Many battery boxes have vertical ribs moulded into the side walls. If the 7-3/8"
  is measured across the ribs, relieving them could recover the 1/4" needed.

If it genuinely will not fit, the length and height both have room to spare, so the
fix is a slightly wider enclosure rather than a rethink — a Group 8D box or a
similar case, keeping every other part and the whole layout unchanged.

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

### Not yet in the BOM

No overcurrent protection is in the parts list yet. A 280Ah LiFePO4 can deliver
enormous short-circuit current, so before this gets wired:

- Class T main fuse on the battery positive (its high interrupt rating is the
  reason it's the usual call for LiFePO4 over ANL)
- Fuse on the solar input, plus a battery disconnect switch
- Positive and negative bus bars, 2/0–4/0 cable, lugs, hydraulic crimper
- Wiring note: every negative load must return through the shunt or the
  state-of-charge reading will be wrong

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
