# Build log — Pickup solar

Newest entry first.

## 2026-08-19

- Started the project. Two links supplied: a solar panel listing and a truck bed rack,
  to go on a **2001 F-150 SuperCrew** (5.5 ft bed, 67" inside length, 50" between the
  wheelhouses).
- **The "400W" panel listing is a 2-pack of 200W panels**, not a single 400W panel.
  400W is the pair. Worth knowing before ordering a second one.
- Recorded the full panel spec from the manufacturer: per panel 200W, Vmp 23.74V,
  Imp 8.43A, Voc 27.31V, Isc 8.91A, 51.34 × 30.31 × 1.4", 23.8 lb, N-type 16BB.
- Rack is the JOYTUTUS 11.8" no-drill clamp-on: width adjustable 62.6"–64.96", bottom
  length 54.33", 882 lb static / 300 lb dynamic.
- **Fit worked out — the panels fit the rack in one orientation only.** Portrait, long
  axis fore-aft, side by side: 51.34" fore-aft against the rack's 54.33" (3.0" spare)
  and 2 × 30.31" = 60.62" across against the rack's 62.6" minimum width (2.0" spare).
  Landscape needs 60.62" fore-aft on a 54.33" rack and overhangs the supported
  footprint by 6"+, so it is out. Weight is trivial — 47.6 lb on a 300 lb dynamic
  rating.
- **Biggest risk found: the rack is not sold for this truck.** JOYTUTUS's own site
  lists fitment as F-150 2015–2025. The Amazon title gives no year range. It is a
  width-adjustable clamp-on, so it may still work, but two things decide it and
  neither can be answered from a listing:
  - inside bed width at the top of the rails, which has to land inside 62.6"–64.96"
  - the 1997–2003 bed rail lip section against clamps designed for a 2015+ bed
- **Settled series vs parallel against the Victron MPPT 100/20** held for the battery
  box. Series: Voc 54.62V at STC, ~60V at −10°C against a 100V limit, Isc 8.91A
  against 20A. Parallel: Isc 17.82A leaves only 2.2A under the controller's 20A PV
  ceiling, which is too tight given Isc can spike above STC on cloud edges. **Series.**
- The controller, not the panels, is the ceiling: the 100/20 is 290W nominal at 12V
  (20A × ~14.4V ≈ 288W) against a 400W array, so it clips on the best hours. Victron
  allows the oversize and just limits output. Open decision whether to step up to a
  100/30 or 100/50. Refilling the 3584Wh battery from empty at 288W is ~12.5h, which
  lines up with the ~13h already recorded in the battery box notes.
- **Flagged that the bifacial gain is mostly forfeited.** Flat on a bed rack, the rear
  face looks down at the truck bed a foot below it and collects almost nothing. Size
  the array as if the panels were monofacial; ignore the listing's +30% claim.
- Added the unsourced parts to the BOM: frame mounting hardware, MC4 extension, a 15A
  PV breaker (Isc 8.91A × 1.25 = 11.1A), and a weatherproof cable entry.
- Prices not recorded — Amazon listing prices did not render in the build environment.
