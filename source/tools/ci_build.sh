#!/bin/bash
# Build the site inside a checkout of the repository, in place. GitHub runs this after every merge (site.yml) and on
# every pull request (check.yml), which is why a pull request needs to carry only sources: two of them can then never
# disagree over the built files.
#   bash source/tools/ci_build.sh          from the root of the checkout
# Needs Python with requests, Pillow, numpy and rasterio, and the network for three steps: drive times, land status and
# old-map crops for new places. Each of those keeps what it already knew and carries on if its service does not answer;
# the next build asks again.
# Prints "BUILD: nothing changed" or "BUILD: new version <v>" on its last line.
set -e
REPO="$(pwd)"; [ -f "$REPO/source/tools/setup.sh" ] || { echo "run this from the root of the repository"; exit 1; }
W="${ATLAS_CI_WORK:-${RUNNER_TEMP:-/tmp}/atlas-build}"
rm -rf "$W"; bash source/tools/setup.sh "$W" | grep -v "^MISSING Playwright" || true
export ATLAS="$W"; cd "$W"
python3 tools/safe_data.py tools > /dev/null || { python3 tools/safe_data.py tools | tail -25; exit 1; }   # before any place list is run: each must be only data
out=$(python3 tools/build_sites.py) || { echo "$out" | tail -5; exit 1; }; echo "$out" | tail -1 | cut -c1-80
# The site build (not a pull request's check) looks up the Wikipedia picture of places written since the last build, a few
# hundred at most, so tools/photos.py no longer waits for somebody to remember it: on November 26, 2026 it had not been run
# for six days, 3,500 places had never been asked about, and the pictures job, which takes a place only after this has
# been through it, reported 11 places waiting. What it learns is carried back into the sources and published with the build.
if [ "${ATLAS_PHOTOS:-}" = "1" ]; then
  (timeout 300 python3 tools/photos.py --n 300 | tail -1) || echo "WARNING: the article-photo lookup did not finish; the next build carries on"
  [ -s src/photos.json ] && python3 -c "import json;json.load(open('src/photos.json'))" && cp src/photos.json "$REPO/source/src/photos.json"
fi
python3 tools/topo_all.py --missing || echo "WARNING: the old-map step failed; places added now have no old-map crop until the next build"
# First under the version the repository already has: if nothing comes out different, there is nothing to publish.
OLD=$(python3 -c "import json;j=json.load(open('$REPO/version.json'));print(j['v']+'|'+str(j.get('built','')))" 2>/dev/null || true)
ATLAS_V="${OLD%%|*}" ATLAS_BUILT="${OLD#*|}" bash tools/all.sh
bash tools/into_repo.sh "$W" "$REPO"
if [ -n "$OLD" ] && [ -z "$(git -C "$REPO" status --porcelain)" ]; then echo "BUILD: nothing changed"; exit 0; fi
# Something changed: the same build again under a new version, so phones and browsers know to fetch it.
python3 tools/make.py > /dev/null; python3 tools/export.py > /dev/null; bash tools/into_repo.sh "$W" "$REPO"
echo "BUILD: new version $(python3 -c "import json;print(json.load(open('$REPO/version.json'))['v'])")"
