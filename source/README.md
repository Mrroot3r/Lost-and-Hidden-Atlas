# Source

The site in the repository root is generated from these files. `GUIDE.md` in the root explains how; `tools/setup.sh` turns a clone into a working build folder.

- `src/` holds the app (`app.js`, `app.css`, `app.body.html`, `sw.js`) and the original catalogue the first places came from.
- `tools/` holds the build scripts and the place lists (`data_*.py`).
- `build/` holds small prebuilt inputs: the outline map, start cities, cached public-land lookups, the old-map index and Leaflet's stylesheet.
