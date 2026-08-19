# Bill of Materials — Pickup solar

| # | Part | Spec / part no. | Qty | Unit cost | Total | Source | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Callsun N-Type 16BB bifacial solar panel | Sold as "400W" — is a **2-pack of 200W panels**. Per panel: 200W, Vmp 23.74V, Imp 8.43A, Voc 27.31V, Isc 8.91A, 51.34 × 30.31 × 1.4" (1304 × 770 × 35mm), 23.8 lb, N-type 16BB 182mm mono, IP68, max series fuse 25A. ASIN B0DC6T55ZK | 1 pack (2 panels) | | | https://a.co/d/08xj9RN5 | |
| 2 | JOYTUTUS full size truck bed rack | 11.8" high, no-drill clamp-on, wider MOLLE panel. Width adjustable 62.6"–64.96", bottom length 54.33", height 11.81". 882 lb static / 300 lb dynamic. ASIN B0D41YH9YL | 1 | | | https://a.co/d/0enyN345 | |

**Status values:** Needed → Ordered → On hand → Installed

**Running total:**

Prices are not recorded — Amazon listing prices were not readable from the build
environment. Fill in from the order confirmation.

## Still needed

Nothing that joins the panels to the rack, or the rack to the battery, is sourced yet.

| # | Part | Spec / sizing | Status |
| --- | --- | --- | --- |
| — | Panel-to-rack mounting hardware | For 35mm frames. Use the factory frame mounting holes — do not drill the frame | Needed |
| — | MC4-compatible extension cable | Bed to battery box. Gauge per run length; array carries 8.43A in series | Needed |
| — | PV disconnect / breaker | **15A** (Isc 8.91A × 1.25 = 11.1A). Panel allows up to 25A series | Needed |
| — | Weatherproof cable entry | Off the rack and into the bed | Needed |

## Array figures

Two panels, wired **in series** — see [README.md](README.md) for why.

| | Series (chosen) | Parallel |
| --- | --- | --- |
| Power | 400W | 400W |
| Voc (STC) | 54.62V | 27.31V |
| Voc (−10°C) | ~60V | ~30V |
| Vmp | 47.48V | 23.74V |
| Imp | 8.43A | 16.86A |
| Isc | 8.91A | 17.82A |

Checked against the Victron SmartSolar MPPT 100/20 held for the
[280Ah battery box](../battery-box-280ah/): 100V max PV Voc, 20A max PV Isc, 290W
nominal at 12V. Series clears both limits with margin. The controller clips above
~290W of the array's 400W.
