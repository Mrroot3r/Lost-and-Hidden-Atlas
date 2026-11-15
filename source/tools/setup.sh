#!/bin/bash
# Turn a clone of the repository into a working build folder.
#   bash source/tools/setup.sh [workspace]     (default workspace: /home/claude/atlas)
# Then:  ATLAS=<workspace> bash <workspace>/tools/all.sh
set -e
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
W="${1:-/home/claude/atlas}"
mkdir -p "$W"/{src,tools,build/topo,cache/osm,dist,research,test}
cp "$REPO"/source/src/* "$W/src/"
cp "$REPO"/source/tools/* "$W/tools/"
cp "$REPO"/source/build/base.json "$REPO"/source/build/hubs.json "$REPO"/source/build/padus.json "$W/build/"
cp "$REPO"/source/build/topo-meta.json "$W/build/topo/meta.json"
cp "$REPO"/source/build/leaflet.min.css "$W/cache/leaflet.min.css"
cp "$REPO"/leaflet.js "$W/cache/leaflet.min.js"
cp "$REPO"/topo/*.webp "$W/build/topo/"
cp "$REPO"/data/lines.json "$W/build/lines.json"
cp "$REPO"/data/leads.json "$W/build/leads.json"
echo "Workspace ready at $W. Build with: ATLAS=$W bash $W/tools/all.sh"
