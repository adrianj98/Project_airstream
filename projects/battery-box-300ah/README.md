# 300Ah battery box

**Status:** Planning
**Started:** 2026-08-15
**Target:**

## Goal

Build a box for the 300Ah battery.

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

**Layout.** A Group 31 300Ah battery is about 13-3/4" long at the base in a 21-1/2"
box, leaving roughly 7-3/4" of length spare. That spare bay is where the MPPT and
the shunt go — which is why a *double* box for a *single* battery.

### Sizing sanity check

- 300Ah at 12V is ~3.6kWh. Starlink Mini draws ~20–40W, so a full box is on the
  order of days of continuous Starlink, not hours.
- MPPT 100/20 at 12V is ~270W of charge — replaces a day of Starlink in about an
  hour of good sun, but is a bottleneck for a full recharge from empty (~15h).
- The 500A shunt is sized well above anything else here. Fine, but it implies an
  inverter may be on the roadmap.

### Not yet in the BOM

No overcurrent protection is in the parts list yet. A 300Ah LiFePO4 can deliver
enormous short-circuit current, so before this gets wired:

- Class T main fuse on the battery positive (its high interrupt rating is the
  reason it's the usual call for LiFePO4 over ANL)
- Fuse on the solar input, plus a battery disconnect switch
- Positive and negative bus bars, 2/0–4/0 cable, lugs, hydraulic crimper
- Wiring note: every negative load must return through the shunt or the
  state-of-charge reading will be wrong

## Open questions

- [ ] **Battery width vs box.** Current Group 31 300Ah batteries run 7.56–7.68" wide
      against the Camco's stated 7-3/8" interior — marginal. Molded boxes taper wider
      toward the top, so measure at actual seating depth before assuming either way.
- [ ] **Height clearance for lugs.** Battery is ~10–10.5" tall with terminals in an
      11-3/16" interior, leaving ~1" for lugs and cable bend. Right-angle lugs may be
      needed to close the lid.
- [ ] Battery dimensions and weight — confirm make/model
- [ ] Where the box mounts
- [ ] MPPT is the 48V variant — confirm it is being run at the system voltage intended
- [ ] SmartShunt is listed at 500A; one US listing for the same ASIN shows 300A.
      Confirm which arrived
- [ ] Solar panel wattage and Voc, to check against the 100V/20A controller limits

## Tasks

- [x] Name the five parts in the BOM
- [ ] Record battery dimensions and check fit against the box interior
- [ ] Fill in prices from the order confirmation
- [ ] Plan panel layout on the lid/enclosure face for the two Victron units and the
      Anderson plates
