# Electrical box update

**Status:** Planning
**Started:** 2026-08-15
**Target:** TBD

## Goal

Rework the existing electrical box so the DC and AC distribution is safe, fused
correctly, labeled, and has room for the upgrades coming next (300Ah battery,
added solar).

## Requirements

- Must: every circuit individually fused/breakered and sized to its wire gauge
- Must: main battery disconnect reachable without opening the box
- Must: all terminations torqued and labeled; a wiring diagram that matches reality
- Should: room to add circuits later without a full rebuild
- Should: shunt/monitor so state of charge is actually visible
- Won't: replace the shore power inlet or the existing converter (separate project)

## Constraints

- Physical envelope of the current box: TBD (measure before ordering anything)
- Existing wire runs stay in place where gauge allows
- Work happens with the rig disconnected from shore power and battery isolated

## Current state

Document what's in there today before changing anything:

- [ ] Photograph the box as-found (wide + close on every terminal) → `assets/`
- [ ] Trace and list every existing circuit: load, wire gauge, run length, current protection
- [ ] Note existing bus bars, breakers, converter/charger model

## Design

To be filled in after the audit. Things to decide:

- DC distribution: fuse block type and position count
- AC side: breaker panel, GFCI placement
- Bus bar layout and negative/ground bonding point
- Wire gauge per circuit vs. length (voltage drop, not just ampacity)
- Battery main fuse (Class T or MRBF) sized to the new 300Ah bank — coordinate with
  [battery-box-300ah](../battery-box-300ah/) and [pickup-solar](../pickup-solar/)

## Open questions

- [ ] Is the existing converter/charger compatible with the new battery chemistry?
- [ ] Does the box need forced ventilation once loads increase?
- [ ] Keep the box in its current location, or relocate closer to the battery?

## Tasks

- [ ] Audit and photograph as-found wiring
- [ ] Draw the target one-line diagram
- [ ] Size main fuse, branch fuses, and wire gauges
- [ ] Finalize [BOM.md](BOM.md)
- [ ] Order parts
- [ ] Rebuild box (battery disconnected, shore power unplugged)
- [ ] Continuity + polarity check before energizing
- [ ] Energize, load test each circuit, verify no hot terminations
- [ ] Label everything and file the final diagram in `assets/`

## Safety notes

- Disconnect shore power **and** isolate the battery before opening the box.
- Battery negative off first, on last.
- Never leave an unfused conductor connected to the battery positive.
- Torque terminals to spec — loose lugs are the usual cause of fires here.
- Verify de-energized with a meter; don't trust a switch position.

## References

- <datasheets and code references to add>
