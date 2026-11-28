#!/bin/bash
# Rebuild the whole site from the place lists. Run from anywhere; ATLAS is the workspace (see setup.sh).
set -e
cd "${ATLAS:-/home/claude/atlas}"
# One build at a time in a workspace. Helpers working side by side in one workspace ran build_sites.py in the middle of this
# script, which rewrote build/sites.json without its drive times and made export.py fail (the asylum pass, November 28, 2026).
# build_sites.py waits for the same lock when it is run by itself.
mkdir -p build; exec 9>build/.lock; flock 9; export ATLAS_BUILD_LOCKED=1
python3 tools/safe_data.py tools > /dev/null || { python3 tools/safe_data.py tools | tail -25; exit 1; }   # a place list is data and nothing else: read, not run
out=$(python3 tools/build_sites.py) || { echo "$out" | tail -5; echo "all.sh: the place lists could not be merged, so nothing was built"; exit 1; }   # a pipe would hide its failure
echo "$out" | tail -1 | cut -c1-80                    # merge the place lists into build/sites.json
python3 tools/drive.py > /dev/null                    # drive times from each start city (needs network)
python3 tools/padus.py                                # public-land status at each pin (cached)
python3 tools/leads.py | cut -c1-80                   # leads layer, if the raw download is present
python3 tools/walls.py | cut -c1-110                  # the stone-walls layer, from lidar/walls/ (no network)
python3 tools/make.py                                 # writes dist/web (the hosted site) and the single-file copy
python3 tools/export.py                               # CSV and KML
node -e "const fs=require('fs'); new Function(fs.readFileSync('src/app.js','utf8')); console.log('syntax ok')"
