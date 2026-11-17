#!/bin/bash
# Copy a finished build from a workspace into a checkout of the repository: the hosted site into the root, and what the
# build worked out (drive times, land status, old-map crops) into source/build so the next build need not ask again.
#   bash tools/into_repo.sh <workspace> <path-to-repo-clone>
# Used by tools/ci_build.sh (GitHub builds the site after a merge) and by "FULL=1 tools/publish.sh".
set -e
W="$1"; REPO="$2"
[ -f "$W/dist/web/index.html" ] && [ -d "$REPO/source" ] || { echo "usage: into_repo.sh <workspace with a build> <repo clone>"; exit 1; }
cd "$REPO"
rm -rf data topo
cp -a "$W/dist/web/." ./
mkdir -p source/build
cp "$W/build/base.json" "$W/build/hubs.json" "$W/build/padus.json" "$W/build/states.json" source/build/
[ -f "$W/build/drive.json" ] && cp "$W/build/drive.json" source/build/drive.json
cp "$W/build/topo/meta.json" source/build/topo-meta.json
[ -f "$W/build/topo/none.json" ] && cp "$W/build/topo/none.json" source/build/topo-none.json
cp "$W/cache/leaflet.min.css" source/build/leaflet.min.css
