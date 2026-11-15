# Source

The site in the repository root is generated from these files.

- `src/` holds the app (`app.js`, `app.css`, `app.body.html`, `sw.js`) and the original catalogue the first places came from.
- `tools/` holds the build scripts. `data_a.py`, `data_b.py`, `data_c.py` and `data_ma.py` are the place lists; `make.py` assembles the site; `all.sh` runs the whole build.
- `build/topo-meta.json` records which USGS sheet each old map in `topo/` was cut from.

The scripts expect large downloaded caches (map data, scanned survey sheets) that are not stored here because they can be fetched again.
