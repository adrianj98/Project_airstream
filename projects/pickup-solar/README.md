# Pickup solar

**Status:** Planning
**Started:** 2026-08-15
**Target:** TBD

## Goal

Add solar to the pickup so the house battery keeps charging while parked, without
depending on shore power or idling the truck.

## Requirements

- Must: panels mounted so they survive highway speed and weather
- Must: controller sized to the array and matched to the battery chemistry
- Must: no roof penetrations that leak; sealed and serviceable if they exist
- Should: enough daily harvest to cover the typical daily load — size against a real
  power budget, not a guess
- Should: disconnect between array and controller for servicing
- Won't: grid-tie or AC output — DC charging only

## Constraints

- Mounting surface and usable area: TBD (measure the roof / rack / bed cover)
- Height clearance after mounting (garages, drive-throughs, trailheads)
- Shading from the cab, rack, or the trailer when hitched
- Cable run from panels to the controller and on to the battery: TBD

## Design

Decide and record:

- Array: panel count, watts, dimensions, and series vs. parallel wiring
- Controller: MPPT sizing — array Voc at coldest expected temperature must stay under
  the controller's max input voltage
- Mounting: rack, tilt mounts, or adhesive on a bed cover; hardware and sealant
- Cable gauge and fusing between array, controller, and battery
- Where the controller lives, and how it ties into the
  [electrical box](../electrical-box-update/) and the
  [300Ah battery](../battery-box-300ah/)

## Open questions

- [ ] Daily power budget — what actually needs to be covered? (see [docs/power-budget.md](../../docs/power-budget.md))
- [ ] Panels on the truck, the trailer, or both?
- [ ] Portable/suitcase panel as a supplement for shaded parking?
- [ ] Does the truck also need a DC-DC charger from the alternator? (separate project if so)

## Tasks

- [ ] Fill in the power budget to size the array
- [ ] Measure the mounting area and check clearances
- [ ] Select panels and controller; verify voltage/current match
- [ ] Plan the cable route, gauge, and fusing
- [ ] Finalize [BOM.md](BOM.md)
- [ ] Mount panels; seal all penetrations
- [ ] Wire array → controller → battery, fused at both ends of the battery cable
- [ ] Commission: verify Voc, charge current, and controller settings for the chemistry
- [ ] Log a few days of real-world harvest and compare against the budget

## Safety notes

- Panels are live whenever there's light on them — cover them while wiring.
- Connect controller to battery **before** connecting the array; disconnect in the
  reverse order. Many controllers are damaged by ignoring this.
- Fuse the battery side close to the battery.
- Anything on the roof at highway speed is a projectile if it lets go — use rated
  hardware and check torque after the first trip.

## References

- <panel and controller datasheets to add>
