#!/bin/bash
# Put a finished build on a NEW BRANCH of the repository clone, ready to become a pull request.
# It never touches main. See GUIDE.md section 3.
#   ATLAS=<workspace> bash tools/publish.sh <path-to-repo-clone> <branch-name>
# To build on work that is in an open pull request and not yet merged, name its branch as the base:
#   BASE=origin/<that-branch> ATLAS=<workspace> bash tools/publish.sh <path-to-repo-clone> <branch-name>
# (and set the workspace up from that branch first: git checkout it, then source/tools/setup.sh).
set -e
W="${ATLAS:-/home/claude/atlas}"; REPO="$1"; BR="$2"
[ -d "$REPO/.git" ] && REPO="$(cd "$REPO" && pwd)"      # a relative path must still work after the cd below
[ -d "$REPO/.git" ] && [ -n "$BR" ] || { echo "usage: publish.sh <repo clone> <branch-name>   e.g. add-connecticut-first-pass"; exit 1; }
[ "$BR" != "main" ] || { echo "Refusing: changes go on a branch, never straight to main."; exit 1; }
[ -f "$W/dist/web/index.html" ] || { echo "No build at $W/dist/web. Run tools/all.sh first."; exit 1; }
cd "$REPO"
CUR=$(git rev-parse --abbrev-ref HEAD)
if [ "$CUR" != "$BR" ]; then
  [ -z "$(git status --porcelain)" ] || { echo "The clone has uncommitted changes. Commit or discard them first."; exit 1; }
  git fetch --depth=50 origin main -q
  BASE="${BASE:-origin/main}"
  [ "$BASE" = "origin/main" ] || git fetch --depth=50 origin "${BASE#origin/}:refs/remotes/$BASE" -q
  git checkout -q -B "$BR" "$BASE"
fi
# A workspace set up before somebody else's work was merged would undo that work here: publishing copies the whole of
# tools/ and src/ over the repository's. So: every source file that changed on the base since this workspace was set up
# must be the same in the workspace. If one is not, stop and say how to catch up.
BASE="${BASE:-origin/main}"; SC=$(cat "$W/.setup_commit" 2>/dev/null || true)
if [ -n "$SC" ] && git cat-file -e "$SC^{commit}" 2>/dev/null && git rev-parse -q --verify "$BASE" >/dev/null; then
  STALE=""
  for f in $(git diff --name-only "$SC" "$BASE" -- source/tools source/src); do
    git cat-file -e "$BASE:$f" 2>/dev/null || continue
    if [ ! -e "$W/${f#source/}" ] || ! git show "$BASE:$f" | cmp -s - "$W/${f#source/}"; then STALE="$STALE $f"; fi
  done
  if [ -n "$STALE" ]; then
    echo "STOP: these files changed in the repository after this workspace was set up, and publishing now would undo that:"; for f in $STALE; do echo "  $f"; done
    echo "Catch up (it keeps your own new work), then publish again:"
    echo "  git -C $REPO checkout -q main 2>/dev/null; ATLAS=$W bash $W/tools/resync.sh $REPO"
    exit 1
  fi
fi
# the LiDAR ledger: fold the repository's copy into the workspace's first, so another session's verdicts are kept
[ -d source/lidar/units ] && (cd "$W" && python3 tools/lidar.py pull "$REPO/source/lidar/units")
rm -rf data topo
cp -a "$W/dist/web/." ./
mkdir -p source/src source/tools source/build
rm -f source/tools/*.py source/tools/*.sh source/tools/*.js source/tools/*.java
cp "$W"/src/* source/src/
cp "$W"/tools/*.py "$W"/tools/*.sh "$W"/tools/*.js "$W"/tools/*.java source/tools/
if [ -d "$W/lidar" ]; then rm -rf source/lidar; mkdir -p source/lidar/units; cp "$W"/lidar/units/*.json source/lidar/units/; for f in "$W"/lidar/*; do [ -f "$f" ] && cp "$f" source/lidar/; done; fi
cp "$W/build/base.json" "$W/build/hubs.json" "$W/build/padus.json" "$W/build/states.json" source/build/
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
