# Build log — 280Ah battery box

Newest entry first.

## 2026-08-15

- Battery is a **WattCycle 12V 280Ah Mini** — 15.12" × 7.64" × 10.04", 59.5 lb,
  200A BMS, EVE LF280K A+ cells, 3584Wh. Renamed the project from 300Ah to 280Ah
  to match.
- **Fit confirmed in person — the battery goes in.** The published 7.64" width is
  the widest point and the case is tapered, so it seats fine against the 7-3/8"
  interior. Enclosure stays as-is.
- Worked out the distribution scheme: Class T (~250A) at the battery positive into a
  positive bus bar, blade fuse block for small loads, MRBF/MIDI for the 120A Anderson
  outlets, separate fuse on the PV input. Negative side is an unfused common bus bar
  fed from the shunt's SYSTEM MINUS, with every return landing there so nothing
  bypasses the shunt.
- Flagged a space constraint: the ~6.4" × 7.6" × 11" equipment bay won't take the
  MPPT, shunt, Class T holder and fuse block all flat on the floor. MPPT goes on the
  end wall vertically. Also flagged the sealed-vs-vented tension between the IP-rated
  fittings and MPPT cooling.
- Layout: with a 15.12" battery in a 21.5" box there is ~6.4" of length spare for
  the MPPT and shunt to sit alongside it — the reason a double box suits a single
  battery.
- Added the missing safety parts to the BOM as a "still needed" list: Class T fuse,
  disconnect switch, solar fuse, bus bars, cable, lugs, crimper.
- Corrected an earlier fit concern that had used the older 20.55 × 9.33 × 8.58"
  300Ah form factor.
- Identified all five parts from the supplied links and filled in the BOM: RVSPARK
  30V bulkhead pass-through, Camco 55375 double battery box, Victron SmartSolar
  MPPT 100/20 48V, Zhushan 120A Anderson SB120 quick disconnects, Victron
  SmartShunt IP65 500A.
- Prices not recorded — Amazon listing prices did not render in the build
  environment.
- Started the project. Recorded the part links that make up the box — four
  initially, a fifth (the SmartShunt) added the same day.
