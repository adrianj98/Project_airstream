# 300Ah battery box

**Status:** Planning
**Started:** 2026-08-15
**Target:** TBD

## Goal

Build an enclosure for the 300Ah battery that holds it securely while traveling,
keeps the terminals protected, and makes the battery serviceable without
dismantling anything around it.

## Requirements

- Must: battery restrained against movement in all directions, including rollover
- Must: terminals covered / non-contactable when the lid is off
- Must: main fuse mounted at the battery, as close to the positive post as practical
- Must: cable entry with strain relief and no chafe points
- Should: removable lid, hand-tool access to terminals for torque checks
- Should: room for the shunt and battery monitor wiring
- Won't: house the inverter or distribution — that lives in the
  [electrical box](../electrical-box-update/)

## Constraints

- Battery: 300Ah, make/model TBD → confirm exact L×W×H, weight, and terminal type
- Mounting location and available envelope: TBD (measure before cutting)
- Weight matters — record where it lands relative to the axle for tongue weight

## Design

Decide and record:

- Material: plywood + fiberglass, or an off-the-shelf poly case
- Base fastening: what it bolts to and whether that structure is rated for the load
- Hold-down: strap over the top vs. cleats + threaded rod
- Ventilation: depends on chemistry — LiFePO4 needs no vent for hydrogen but does
  want heat management; lead-acid/AGM has different rules
- Temperature: does the location go below freezing? LiFePO4 must not charge below 0°C
  without a heater or BMS cutoff
- Terminal covers and the fuse holder mount

## Open questions

- [ ] Exact battery model, dimensions, weight, chemistry, and BMS behavior
- [ ] Where does it mount, and is that structure strong enough for the weight?
- [ ] Cold-weather charging protection needed?
- [ ] Cable run length to the electrical box (drives cable gauge)

## Tasks

- [ ] Confirm battery dimensions and weight from datasheet, then measure the actual unit
- [ ] Measure the mounting envelope; check clearances for lid removal
- [ ] Sketch the box with a cut list → `assets/`
- [ ] Choose hold-down method and verify the mounting structure
- [ ] Finalize [BOM.md](BOM.md)
- [ ] Build the box, dry-fit the battery
- [ ] Mount, install main fuse and cables, torque terminals
- [ ] Road-test and re-check fasteners and torque afterwards

## Safety notes

- 300Ah of stored energy will vaporize a wrench — remove rings/watch, use insulated
  tools, cover the positive post whenever you're working near it.
- Fuse at the battery, not at the far end of the cable.
- Get help lifting; note the actual weight in the log once measured.
- Re-torque terminals after the first few hundred miles.

## References

- <battery datasheet and hold-down hardware specs to add>
