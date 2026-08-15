# Power budget

Shared across [electrical-box-update](../projects/electrical-box-update/),
[battery-box-300ah](../projects/battery-box-300ah/), and
[pickup-solar](../projects/pickup-solar/). Fill this in before buying panels, a
controller, or sizing the main fuse — every one of those decisions depends on it.

## Loads

| Load | Volts | Amps | Hours/day | Wh/day | Notes |
| --- | --- | --- | --- | --- | --- |
| Fridge | 12 | | | | duty cycle, not runtime |
| Lights | 12 | | | | |
| Water pump | 12 | | | | |
| Fan / vent | 12 | | | | |
| Laptop / devices | | | | | via inverter or 12V |
| Inverter idle draw | 12 | | | | counts even with nothing plugged in |

**Total Wh/day:** TBD

## Storage

- Battery: 300Ah @ 12V = 3600 Wh nominal
- Usable depth of discharge: TBD (chemistry-dependent)
- Usable Wh: TBD
- Days of autonomy with no charging: usable Wh ÷ daily Wh

## Generation

- Target daily harvest: daily Wh ÷ realistic sun-hours for where the rig actually parks
  (be pessimistic — shading, panel angle, and heat all cut output)
- Array size needed: TBD
- Charge sources: solar, shore power converter, alternator/DC-DC (if added)

## Conclusions

Once the numbers are in, record here:

- Array watts to buy:
- Controller rating:
- Main battery fuse size:
- Cable gauges per run:
