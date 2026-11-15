#!/bin/bash
# Copy a finished build into the repository clone and stage it. Review, commit and push yourself.
#   ATLAS=<workspace> bash tools/publish.sh <path-to-repo-clone>
set -e
W="${ATLAS:-/home/claude/atlas}"; REPO="$1"
[ -d "$REPO/.git" ] || { echo "usage: publish.sh <repo clone>"; exit 1; }
rm -rf "$REPO/data" "$REPO/topo"
cp -a "$W/dist/web/." "$REPO/"
mkdir -p "$REPO/source/src" "$REPO/source/tools" "$REPO/source/build"
cp "$W"/src/* "$REPO/source/src/"
cp "$W"/tools/*.py "$W"/tools/*.sh "$W"/tools/*.js "$REPO/source/tools/" 2>/dev/null || true
cp "$W/build/base.json" "$W/build/hubs.json" "$W/build/padus.json" "$REPO/source/build/"
cp "$W/build/topo/meta.json" "$REPO/source/build/topo-meta.json"
cp "$W/cache/leaflet.min.css" "$REPO/source/build/leaflet.min.css"
git -C "$REPO" add -A && git -C "$REPO" status --short | awk '{print $1}' | sort | uniq -c
