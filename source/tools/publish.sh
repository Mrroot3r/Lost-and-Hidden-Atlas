#!/bin/bash
# Put a finished build on a NEW BRANCH of the repository clone, ready to become a pull request.
# It never touches main. See GUIDE.md section 3.
#   ATLAS=<workspace> bash tools/publish.sh <path-to-repo-clone> <branch-name>
set -e
W="${ATLAS:-/home/claude/atlas}"; REPO="$1"; BR="$2"
[ -d "$REPO/.git" ] && [ -n "$BR" ] || { echo "usage: publish.sh <repo clone> <branch-name>   e.g. add-connecticut-first-pass"; exit 1; }
[ "$BR" != "main" ] || { echo "Refusing: changes go on a branch, never straight to main."; exit 1; }
[ -f "$W/dist/web/index.html" ] || { echo "No build at $W/dist/web. Run tools/all.sh first."; exit 1; }
cd "$REPO"
CUR=$(git rev-parse --abbrev-ref HEAD)
if [ "$CUR" != "$BR" ]; then
  [ -z "$(git status --porcelain)" ] || { echo "The clone has uncommitted changes. Commit or discard them first."; exit 1; }
  git fetch --depth=50 origin main -q
  git checkout -q -B "$BR" origin/main
fi
rm -rf data topo
cp -a "$W/dist/web/." ./
mkdir -p source/src source/tools source/build
rm -f source/tools/*.py source/tools/*.sh source/tools/*.js
cp "$W"/src/* source/src/
cp "$W"/tools/*.py "$W"/tools/*.sh "$W"/tools/*.js source/tools/
cp "$W/build/base.json" "$W/build/hubs.json" "$W/build/padus.json" source/build/
cp "$W/build/topo/meta.json" source/build/topo-meta.json
cp "$W/cache/leaflet.min.css" source/build/leaflet.min.css
git add -A
echo "--- staged on branch $BR ---"; git status --short | awk '{print $1}' | sort | uniq -c
echo "--- checks ---"; python3 source/tools/check.py "$REPO"
cat <<MSG
--- next ---
1. git -C $REPO commit            (say what changed, what you verified and what you could not)
2. git -C $REPO push -u origin $BR
3. Open a pull request into main and stop. The owner merges it. Do not merge it yourself.
MSG
