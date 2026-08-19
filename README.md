# Project Airstream — Master Report

Rollup of every sub-project in this repo. Each project lives in its own folder under
[`projects/`](projects/) with its own notes, bill of materials, and build log. This
page is the single place to see where everything stands.

**Last updated:** 2026-08-15

---

## Status board

| Project | What it is | Status |
| --- | --- | --- |
| [Electrical box update](projects/electrical-box-update/) | Update electrical box | Not started |
| [280Ah battery box](projects/battery-box-280ah/) | Battery box with MPPT, shunt and DC outlets | Planning |
| [Pickup solar](projects/pickup-solar/) | Add solar to the pickup | Not started |

Status values: `Not started` → `Planning` → `In progress` → `Done` → `On hold`

---

## Published site

Every push or merge to `main` rebuilds this repo into a browsable HTML site and
publishes it to GitHub Pages via
[`.github/workflows/publish.yml`](https://github.com/adrianj98/Project_airstream/blob/main/.github/workflows/publish.yml).
Each `.md` file becomes a page; anything in `assets/` (photos, diagrams, existing
`.html` files) is copied through as-is.

Site: https://adrianj98.github.io/Project_airstream/

To preview locally before pushing:

```sh
pip install markdown
python tools/build_site.py --out _site
open _site/index.html
```

`_site/` is generated output and is git-ignored — never commit it.

## Repo layout

```
.
├── README.md            # this master report
├── projects/            # one folder per sub-project
│   └── <project-name>/
│       ├── README.md    # what the project is, notes, tasks
│       ├── BOM.md       # bill of materials + costs
│       ├── LOG.md       # dated build log, newest first
│       └── assets/      # photos, diagrams, datasheets
├── templates/
│   └── project-template/  # copy this to start a new sub-project
├── tools/build_site.py  # markdown -> html site builder
└── docs/                # notes that span more than one project
```

## Adding a sub-project

```sh
cp -r templates/project-template projects/<new-project-name>
```

Then fill in the README, add a row to the status board above, and start logging.

## Conventions

- Folder names are lowercase and hyphenated (`battery-box-280ah`).
- Project-specific material stays in that project's folder; only things spanning
  projects go in `docs/`.
- Log entries are newest-first with an ISO date (`2026-08-15`).
- Update the status board in the same commit that changes a project's status — the
  master report is only useful if it's true.
