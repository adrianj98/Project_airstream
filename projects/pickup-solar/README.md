# Pickup solar

**Status:** Planning
**Started:** 2026-08-19
**Target:**

## Goal

Mount two solar panels on a bed rack on the back of the pickup — a 2001 Ford F-150
SuperCrew — to charge a 12V system.

## Vehicle

**2001 Ford F-150 SuperCrew, 5.5 ft bed**

| Spec | Value |
| --- | --- |
| Generation | 10th gen (1997–2004) |
| Bed, inside length | 67" |
| Bed, width between wheelhouses | 50" |
| Bed, inside height | 22.4" |

The SuperCrew arrived for the 2001 model year on the 138.8" wheelbase and carries the
short 5.5 ft box.

## Parts

Two purchases, identified from the supplied links.

1. **Callsun N-Type 16BB 400W Bifacial Solar Panel** — this is a **2-pack of 200W
   panels**, not one 400W panel. 400W is the pair. N-type, 16BB, bifacial, IP68.
   ASIN B0DC6T55ZK. [link](https://a.co/d/08xj9RN5)
2. **JOYTUTUS Full Size Truck Bed Rack** — 11.8" high, no-drill clamp-on, wider MOLLE
   panel, sold for roof-top tents. ASIN B0D41YH9YL. [link](https://a.co/d/0enyN345)

See [BOM.md](BOM.md).

### Panel specification (per panel — there are two)

| Spec | Value |
| --- | --- |
| Maximum power (Pmax) | 200W |
| Maximum power voltage (Vmp) | 23.74V |
| Maximum power current (Imp) | 8.43A |
| Open-circuit voltage (Voc) | 27.31V |
| Short-circuit current (Isc) | 8.91A |
| Dimensions | 51.34" × 30.31" × 1.4" (1304 × 770 × 35mm) |
| Weight | 23.8 lb (10.8kg) |
| Cells | N-type, 16BB, 182mm monocrystalline |
| Max system voltage | 1000V DC |
| Max series fuse | 25A |
| Power tolerance | 0 to +5% |

Two panels together: **400W, 47.6 lb.**

### Rack specification

| Spec | Value |
| --- | --- |
| Width | Adjustable 62.6" – 64.96" |
| Bottom length | 54.33" |
| Height | 11.81" |
| Static load | 882 lb |
| Dynamic load | 300 lb |
| Mounting | Clamps, no drilling |

## Fit — the panels fit the rack, in one orientation only

Each panel is 51.34" × 30.31". The rack is 54.33" fore-aft by 62.6" wide at its
narrowest setting. That leaves exactly one workable layout.

**Panels portrait — long axis running fore-aft, side by side across the bed:**

| | Panels | Rack | Result |
| --- | --- | --- | --- |
| Fore-aft | 51.34" | 54.33" | Fits, 3.0" spare |
| Across | 2 × 30.31" = 60.62" | 62.6" (min) | Fits, 2.0" spare |

The alternative — long axis across the truck — needs 60.62" fore-aft against the
rack's 54.33", overhanging by more than 6" at front and rear. It stays inside the 67"
bed, but it hangs off the rack's supported footprint. Portrait is the answer.

Two inches of total width margin is not much. Widen the rack past its 62.6" minimum
and the margin grows, so the adjustment range works in our favour here.

Weight is a non-issue: 47.6 lb of panel against a 300 lb dynamic rating.

## The real risk — the rack is not sold for this truck

JOYTUTUS's own site lists this rack's fitment as **Ford F-150 2015–2025**. The Amazon
title says "Compatible with F150 F250 F350 Silverado Sierra Ram" with no year range,
but the manufacturer's own fitment table does not go back to 2001.

The rack is a no-drill clamp-on that grips the inner lip of the bed rails, and it is
width-adjustable, so this is not automatically fatal — clamp-on racks are the most
transferable kind. But two things have to be checked in person before this is a plan:

- **Inside bed width at the top of the rails.** The rack adjusts 62.6"–64.96". If the
  2001 bed's rail-to-rail inside width falls outside that window, the rack does not
  mount, full stop. This is the single measurement that decides the project.
- **The bed rail lip profile.** The 1997–2003 F-150 rail is a different section from
  the 2015+ aluminium bed the clamps were designed around. The clamps need enough lip
  to bite, and enough throat depth to clear the rail's outer flange.

Neither is answerable from a listing. Measure both before assuming anything else here
holds.

## Wiring — series, not parallel

Assuming the array feeds the Victron SmartSolar MPPT 100/20 already bought for the
[280Ah battery box](../battery-box-280ah/) (100V max PV, 20A, 290W nominal at 12V):

| | 2 in series | 2 in parallel |
| --- | --- | --- |
| Array Voc (STC) | 54.62V | 27.31V |
| Array Voc, cold (−10°C) | ~60V | ~30V |
| Array Vmp | 47.48V | 23.74V |
| Array Isc | 8.91A | 17.82A |
| Against 100V limit | Fine, 40V margin | Fine |
| Against 20A PV limit | Fine, 11A margin | **2.2A margin** |

**Series wins.** Parallel puts 17.82A of Isc against the controller's 20A ceiling with
only 2.2A of headroom, and Isc can transiently exceed its STC figure under cloud-edge
irradiance enhancement. Series has margin at both limits, starts the MPPT earlier in
the morning, and lets the run from bed to battery box use thinner cable for the same
loss.

Cold-weather Voc rise is the usual reason a series string fails, and it does not bite
here: even at −10°C the string sits around 60V against a 100V limit.

### The controller is the bottleneck, not the panels

The MPPT 100/20 is rated 290W nominal at 12V — 20A × ~14.4V ≈ 288W of actual charge.
The array is 400W. **Above ~290W the controller clips.**

This is allowed — Victron permits an oversized array and simply limits output — and on
a flat-mounted truck array it matters less than it looks, because flat panels in heat
rarely reach their STC rating anyway. But it is a real ceiling, and it is worth
deciding deliberately:

- Keep the 100/20 and accept clipping on the best hours, or
- Move up to a 100/30 or 100/50 and capture the full 400W.

For scale: refilling the 3584Wh battery from empty at 288W takes about 12.5 hours of
full-output charging. That matches the ~13h figure already recorded in the battery box
notes.

## Bifacial gain is mostly forfeited here

These are bifacial panels — the selling point is a transparent backsheet picking up
light reflected onto the rear face, which the listing puts at up to +30%.

Mounted flat on a bed rack, the rear face looks down at the truck bed 12" below it.
There is almost no reflected light to collect. **Plan on the 400W front-side rating and
treat any bifacial gain as a rounding error.**

That is not an argument against these panels — N-type cells and a 0/+5% tolerance are
good things on their own merits — but the bifacial premium is not buying anything in
this application, and the array should be sized as if it were monofacial.

## Not yet sourced

The BOM covers the panels and the rack. Nothing that actually joins them together is
bought yet:

- Panel-to-rack mounting hardware. The panel frames are 35mm and have factory mounting
  holes — use them; drilling a panel frame voids the warranty.
- MC4-compatible extension cable, bed-to-battery-box, in a gauge sized for the run.
- A PV-side disconnect / breaker. Sizing: Isc × 1.25 = 11.1A, so a **15A** PV breaker.
  With only one string there is no back-feed path, so the fuse is for disconnect and
  fault protection rather than string protection. Panel spec allows up to 25A series.
- A weatherproof route for the cable off the rack and into the bed.

## Open questions

- [ ] **Measure the inside bed width at the top of the rails.** Decides whether the
      rack mounts at all. Must land inside 62.6"–64.96".
- [ ] **Check the bed rail lip against the clamps** — the 2001 rail section is not
      what these were designed for.
- [ ] Measure the usable crossbar span between the rack uprights. The 62.6"–64.96"
      figure is the rack's overall width; the panels need 60.62" of *clear* span.
- [ ] Does this array feed the 280Ah battery box, or a separate controller? The box's
      BOM already reserves an Anderson pair for PV input, which suggests yes — confirm.
- [ ] If it does feed the box: keep the MPPT 100/20 and accept clipping above 290W, or
      step up to a 100/30 / 100/50?
- [ ] Finished height of the truck with panels on the rack — measure against whatever
      it has to park under.
- [ ] Wind loading at highway speed. 10.7 sq ft of flat panel on a rack is a lift
      problem before it is a weight problem; how do the panels get restrained fore-aft?
- [ ] Does the rack obstruct the tailgate, or the rear window?
- [ ] Prices — not recorded, see BOM.

## Tasks

- [x] Identify both parts from the supplied links
- [x] Record panel electrical and physical specs
- [x] Work out panel-on-rack fit and orientation
- [x] Settle series vs parallel against the MPPT 100/20
- [ ] Measure the bed and settle the rack fitment question
- [ ] Source mounting hardware, PV cable and PV breaker
- [ ] Fill in prices from the order confirmation
- [ ] Decide the cable route from rack to battery box
