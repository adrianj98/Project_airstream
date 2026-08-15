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

## Open questions

- [ ] **Will the battery fit the Camco 55375?** Its interior is 21-1/2" long but only
      7-3/8" wide. Many common 12V 300Ah LiFePO4 batteries are wider than that. Measure
      the battery before cutting anything.
- [ ] Battery dimensions and weight
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
