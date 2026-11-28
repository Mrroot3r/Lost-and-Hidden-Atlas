#!/bin/bash
# Put a change on a NEW BRANCH of the repository clone, ready to become a pull request.
# It never touches main. See GUIDE.md section 3.
#   ATLAS=<workspace> bash tools/publish.sh <path-to-repo-clone> <branch-name>
# The branch carries SOURCES ONLY (source/tools, source/src, the LiDAR ledger). GitHub builds the site after the merge
# (tools/ci_build.sh), so two pull requests can never disagree over the built files. Build and test in the workspace
# first all the same: that is how you know the change works.
#   LAYERS=1 ...   also carry the layer files (lines, leads, vanished places, mines, historic pockets). Use it after
#                  rebuilding one of those layers; GitHub cannot rebuild them, their raw downloads are not in the repository.
#   FULL=1 ...     the old way: carry the whole built site too. Only if the build on GitHub is broken.
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
  STALE=""; CAUGHT=0
  for f in $(git diff --name-only "$SC" "$BASE" -- source/tools source/src); do
    git cat-file -e "$BASE:$f" 2>/dev/null || continue
    w="$W/${f#source/}"
    if [ -e "$w" ] && git show "$BASE:$f" | cmp -s - "$w"; then continue; fi
    # Another session's place list, pictures, hours or brick file (or the list of settled warnings) that this session never
    # touched is simply taken into the workspace: no stop, no resync, no rebuild. Research batches merge every few minutes,
    # and stopping for each one cost a session about four minutes a time (the sessions' notes, November 2026). The site this
    # workspace built does not show those places, which does not matter: the branch carries sources, GitHub builds the site,
    # and check.py below reads all of them together. Anything else that changed (the app, a tool) still stops.
    if echo "$f" | grep -q -E '^source/tools/((data|pics|hours|bricks|legos|archs)_[a-z0-9_]+\.py|checked_ok\.json)$' && { [ ! -e "$w" ] || { git cat-file -e "$SC:$f" 2>/dev/null && git show "$SC:$f" | cmp -s - "$w"; }; }; then
      git show "$BASE:$f" > "$w"; CAUGHT=$((CAUGHT+1)); continue
    fi
    STALE="$STALE $f"
  done
  if [ -z "$STALE" ] && [ "$CAUGHT" -gt 0 ]; then
    git rev-parse "$BASE" > "$W/.setup_commit"
    echo "Caught up by itself: $CAUGHT data file(s) other sessions merged while you worked were taken into the workspace. Nothing of yours was touched and nothing needs rebuilding."
  fi
  if [ -n "$STALE" ]; then
    echo "STOP: these files changed in the repository after this workspace was set up, and publishing now would undo that:"; for f in $STALE; do echo "  $f"; done
    echo "Catch up (it keeps your own new work), then publish again:"
    echo "  git -C $REPO checkout -q main 2>/dev/null; ATLAS=$W bash $W/tools/resync.sh $REPO"
    exit 1
  fi
fi
# the LiDAR ledger: fold the repository's copy into the workspace's first, so another session's verdicts are kept
[ -d source/lidar/units ] && (cd "$W" && python3 tools/lidar.py pull "$REPO/source/lidar/units")
if [ -n "$FULL" ]; then bash "$W/tools/into_repo.sh" "$W" "$REPO"; fi
if [ -n "$LAYERS" ] && [ -z "$FULL" ]; then
  mkdir -p data/pock
  for f in lines leads vanished mines pockets; do [ -f "$W/dist/web/data/$f.json" ] && cp "$W/dist/web/data/$f.json" "data/$f.json"; done
  for f in vanished mines; do      # these two travel in pieces (an index and one file per state): the pieces replace the old ones whole
    [ -d "$W/dist/web/data/$f" ] && { rm -rf "data/$f"; mkdir -p "data/$f"; cp "$W"/dist/web/data/$f/*.json "data/$f/"; }
  done
  [ -d "$W/dist/web/data/pock" ] && { rm -rf data/pock; mkdir -p data/pock; cp "$W"/dist/web/data/pock/*.json data/pock/; }      # the index, each state's discs (named with a stamp) and its detail: the pieces replace the old ones whole
  [ -d "$W/dist/web/data/leads" ] && { rm -rf data/leads; mkdir -p data/leads; cp "$W"/dist/web/data/leads/*.json data/leads/; }      # the leads' second file, named with its stamp
fi
mkdir -p source/src source/tools source/build
rm -f source/tools/*.py source/tools/*.sh source/tools/*.js source/tools/*.java
cp "$W"/src/* source/src/
cp "$W"/tools/*.py "$W"/tools/*.sh "$W"/tools/*.js "$W"/tools/*.java source/tools/
[ -f "$W/tools/checked_ok.json" ] && cp "$W/tools/checked_ok.json" source/tools/      # warnings a session looked at and accepted (tools/check.py)
if [ -d "$W/lidar" ]; then
  mkdir -p source/lidar/units source/lidar/walls; rm -f source/lidar/units/*.json
  cp "$W"/lidar/units/*.json source/lidar/units/; for f in "$W"/lidar/*; do [ -f "$f" ] && cp "$f" source/lidar/; done
  for f in "$W"/lidar/walls/*.json; do [ -f "$f" ] && cp "$f" source/lidar/walls/; done        # walls are added to, never removed: another session's units stay
fi
git add -A
# A last guard: nothing here may take another session's place list, pictures, hours or brick file off the map. If the
# workspace lacks one that the base has (it was set up, or marked as caught up, without it), the file is put back, in the
# branch and in the workspace, and the publish goes on (the maintainer lost two files this way on November 21, 2026,
# before anything merged, by marking a workspace as caught up by hand).
for f in $(git diff --cached --name-only --diff-filter=D -- source/tools | grep -E '^source/tools/((data|pics|hours|bricks|legos|archs)_[a-z0-9_]+\.py|checked_ok\.json)$' || true); do
  if git cat-file -e "$BASE:$f" 2>/dev/null; then git checkout -q "$BASE" -- "$f"; cp "$f" "$W/${f#source/}"; echo "Put back $f: the workspace did not have it, and publishing would have deleted it."; fi
done
git add -A
python3 "$W/tools/note.py" --new "$REPO" && git add -A      # an empty note file for a new batch (notes/<batch key>.md)
echo "--- staged on branch $BR ---"; git status --short | awk '{print $1}' | sort | uniq -c
echo "--- checks ---"; if [ -n "$FULL" ]; then python3 source/tools/check.py "$REPO"; else python3 source/tools/check.py "$REPO" --sources; fi
cat <<MSG
--- next ---
0. A research batch: fill in its note file now, $REPO/notes/<batch key>.md (what the batch is, leads, tips). Do NOT
   edit GUIDE.md, LEADS.md or PROMPTS.md: sessions run side by side and those edits collide. Any other change: this
   is the time to edit GUIDE.md or CLAUDE.md in the clone, on this branch. Then: git -C $REPO add -A
1. git -C $REPO commit            (say what changed, what you verified and what you could not)
2. git -C $REPO push -u origin $BR
3. Open a pull request into main and stop. The owner merges it. Do not merge it yourself.
   GitHub builds the site on the pull request to test it, and again after the merge to publish it.
MSG
