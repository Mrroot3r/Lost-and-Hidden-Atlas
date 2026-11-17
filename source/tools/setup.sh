#!/bin/bash
# Turn a clone of the repository into a working build folder.
#   bash source/tools/setup.sh [workspace]     (default workspace: /home/claude/atlas)
# Then:  ATLAS=<workspace> bash <workspace>/tools/all.sh
# The workspace's src/, tools/ and build/topo/ are replaced, so nothing stale survives from an earlier session.
# Downloads under cache/ and notes under research/ are kept.
set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
W="${1:-/home/claude/atlas}"
if [ -d "$W/tools" ]; then
  STRAY=$(cd "$W/tools" && ls | while read f; do [ -e "$REPO/source/tools/$f" ] || echo "$f"; done | grep -v __pycache__ || true)
  if [ -n "$STRAY" ]; then
    mkdir -p "$W/stray"; for f in $STRAY; do mv "$W/tools/$f" "$W/stray/"; done
    echo "NOTE: these files were in $W/tools but are not in the repository. Moved to $W/stray/:"; echo "$STRAY" | sed 's/^/  /'
  fi
fi
rm -rf "$W/src" "$W/tools" "$W/build/topo"
mkdir -p "$W"/{src,tools,build/topo,cache/osm,dist,research,test}
cp "$REPO"/source/src/* "$W/src/"
find "$REPO"/source/tools -maxdepth 1 -type f -exec cp {} "$W/tools/" \;   # files only: a __pycache__ folder left by running a tool in the clone must not stop the setup
cp "$REPO"/source/build/base.json "$REPO"/source/build/hubs.json "$REPO"/source/build/padus.json "$REPO"/source/build/states.json "$W/build/"
cp "$REPO"/source/build/topo-meta.json "$W/build/topo/meta.json"
[ -f "$REPO/source/build/topo-none.json" ] && cp "$REPO/source/build/topo-none.json" "$W/build/topo/none.json"   # places known to have no old map
[ -f "$REPO/source/build/drive.json" ] && cp "$REPO/source/build/drive.json" "$W/build/drive.json"               # drive times already worked out
cp "$REPO"/source/build/leaflet.min.css "$W/cache/leaflet.min.css"
cp "$REPO"/leaflet.js "$W/cache/leaflet.min.js"
cp "$REPO"/topo/*.webp "$W/build/topo/"
cp "$REPO"/data/lines.json "$W/build/lines.json"
cp "$REPO"/data/leads.json "$W/build/leads.json"
for f in vanished mines; do [ -f "$REPO/data/$f.json" ] && cp "$REPO/data/$f.json" "$W/build/$f.json"; done   # optional lead layers, kept when their raw downloads are absent
# historic pockets: the built layer travels with the site, so a workspace without the raw downloads keeps every state
if [ -f "$REPO/data/pockets.json" ]; then
  cp "$REPO"/data/pockets.json "$W/build/pockets.json"
  mkdir -p "$W/build/pock"; [ -d "$REPO/data/pock" ] && cp "$REPO"/data/pock/*.json "$W/build/pock/"
fi
# the LiDAR ledger (LIDAR.md): the repository's copy is folded into the workspace's, never over it, so verdicts a
# session has recorded and not yet published survive a second setup
[ -d "$REPO/source/lidar" ] && (cd "$W" && mkdir -p lidar && for f in "$REPO"/source/lidar/*; do [ -f "$f" ] && cp "$f" lidar/; done; python3 tools/lidar.py pull "$REPO/source/lidar/units" --base)
git -C "$REPO" rev-parse HEAD > "$W/.setup_commit" 2>/dev/null || true    # publish.sh uses it to notice that main has moved on since
# what this machine can and cannot do
MISS=""
for m in requests PIL rasterio shapely; do python3 -c "import $m" 2>/dev/null || MISS="$MISS $m"; done
[ -n "$MISS" ] && echo "MISSING Python modules:$MISS  (requests: everything; PIL + rasterio: old-map crops and pin checks; shapely: rebuilding lines). Install: pip install requests Pillow rasterio shapely"
node -e "require('playwright')" 2>/dev/null || echo "MISSING Playwright for Node: the smoke test cannot run. Install: npm i playwright && npx playwright install chromium"
echo "Workspace ready at $W. Build with: ATLAS=$W bash $W/tools/all.sh"
