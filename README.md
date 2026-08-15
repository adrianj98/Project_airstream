# Project Airstream — Master Report

Rollup of every sub-project in this repo. Each project lives in its own folder under
[`projects/`](projects/) with its own plan, bill of materials, and build log. This
page is the single place to see where everything stands.

**Last updated:** 2026-08-15

---

## Status board

| Project | What it is | Status | Blocked on | Spend |
| --- | --- | --- | --- | --- |
| [Electrical box update](projects/electrical-box-update/) | Rework the distribution panel: proper fusing, labeling, room to grow | Planning | As-found wiring audit | $0 |
| [300Ah battery box](projects/battery-box-300ah/) | Enclosure + hold-down for the 300Ah battery | Planning | Battery dimensions & mount location | $0 |
| [Pickup solar](projects/pickup-solar/) | Solar array on the truck feeding the house battery | Planning | Power budget → array sizing | $0 |

**Totals:** 3 projects · 0 done · 3 planning · $0 spent

Status values: `Idea` → `Planning` → `In progress` → `Done` → `On hold`

---

## How the projects connect

All three touch the same DC system, so the order matters:

```
300Ah battery box ──┐
                    ├──► Electrical box update ──► loads
Pickup solar ───────┘        (fusing, bus bars, monitoring)
```

- The **battery** sets the main fuse size and the bus bar rating in the electrical box.
- The **solar controller** output lands in the electrical box and must match the
  battery's chemistry and charge profile.
- So: confirm the battery first, design the electrical box around it, and size solar
  against a real power budget. Doing the panel first means opening it twice.

Shared numbers live in [`docs/power-budget.md`](docs/power-budget.md) — fill that in
before ordering anything expensive.

---

## Next actions

The one thing to do next per project:

1. **Electrical box** — photograph the box as-found and trace every existing circuit.
2. **Battery box** — get the exact model, dimensions, weight, and chemistry; pick the mount location.
3. **Pickup solar** — fill in the power budget so the array can be sized honestly.

All three are measurement tasks. None of them cost money, and all of them block spending.

---

## Repo layout

```
.
├── README.md            # this master report
├── projects/            # one folder per sub-project
│   └── <project-name>/
│       ├── README.md    # goal, requirements, design, tasks
│       ├── BOM.md       # bill of materials + costs
│       ├── LOG.md       # dated build log, newest first
│       └── assets/      # photos, diagrams, datasheets, cut lists
├── templates/
│   └── project-template/  # copy this to start a new sub-project
└── docs/                # cross-project notes (power budget, vendors, specs)
```

## Adding a sub-project

```sh
cp -r templates/project-template projects/<new-project-name>
```

Then fill in the README header, add a row to the status board above, and start logging.

## Conventions

- Folder names are lowercase and hyphenated (`battery-box-300ah`).
- Project-specific material stays in that project's folder; only things spanning
  projects go in `docs/`.
- Log entries are newest-first with an ISO date (`2026-08-15`).
- Update the status board in the same commit that changes a project's status — the
  master report is only useful if it's true.
