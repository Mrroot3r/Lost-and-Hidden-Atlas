#!/bin/bash
# Bring a workspace back in step with main after somebody else's work was merged, keeping this session's own new work:
# its new and changed files in tools/ and src/, the old-map crops it cut for new places, and its LiDAR verdicts.
#   ATLAS=<workspace> bash tools/resync.sh <path-to-repo-clone> [<commit the work started from>]
# publish.sh tells you when this is needed. Afterwards build (tools/all.sh) and publish again.
# The second argument is only for work that exists as a branch and no longer as a workspace: set the workspace up from
# that branch first, then give the commit where the branch left main (git merge-base <branch> origin/main).
set -e
W="${ATLAS:-/home/claude/atlas}"; REPO="$(cd "$1" && pwd)"
[ -d "$REPO/.git" ] || { echo "usage: resync.sh <repo clone> [<start commit>]"; exit 1; }
cd "$REPO"
[ -z "$(git status --porcelain)" ] || { echo "The clone has uncommitted changes. Commit them on their branch (or discard them) first."; exit 1; }
SC="${2:-$(cat "$W/.setup_commit" 2>/dev/null || true)}"
git cat-file -e "$SC^{commit}" 2>/dev/null || { echo "Cannot tell where this workspace started (no $W/.setup_commit, or that commit is not in this clone)."; echo "Give the starting commit as the second argument, or start again with source/tools/setup.sh and copy your new files in by hand."; exit 1; }
git fetch --depth=50 origin main -q
# 1. set this session's own work aside: every file in tools/ and src/ that is new or differs from where the workspace started
rm -rf "$W/mine"; mkdir -p "$W/mine/tools" "$W/mine/src" "$W/mine/topo"
for d in tools src; do
  for f in "$W/$d"/*; do
    [ -f "$f" ] || continue; rel="source/$d/$(basename "$f")"
    if ! git cat-file -e "$SC:$rel" 2>/dev/null || ! git show "$SC:$rel" | cmp -s - "$f"; then cp "$f" "$W/mine/$d/"; fi
  done
done
for f in "$W"/build/topo/*.webp; do [ -e "$f" ] || continue; git cat-file -e "$SC:topo/$(basename "$f")" 2>/dev/null || cp "$f" "$W/mine/topo/"; done
cp "$W/build/topo/meta.json" "$W/mine/topo-meta.json" 2>/dev/null || true
# 2. a clean workspace from today's main (the LiDAR ledger is folded together, not replaced)
git checkout -q --detach origin/main
bash source/tools/setup.sh "$W" | grep -v "^NOTE\|^  \|Workspace ready" || true
# 3. put this session's work back. A file that main changed too is not overwritten: it is left in mine/ and named.
BOTH=""
for d in tools src; do
  for f in "$W/mine/$d"/*; do
    [ -f "$f" ] || continue; rel="source/$d/$(basename "$f")"
    if git cat-file -e "$SC:$rel" 2>/dev/null && ! git diff --quiet "$SC" origin/main -- "$rel"; then BOTH="$BOTH $d/$(basename "$f")"; else cp "$f" "$W/$d/"; fi
  done
done
N=0; for f in "$W"/mine/topo/*.webp; do [ -e "$f" ] || continue; cp "$f" "$W/build/topo/"; N=$((N+1)); done
python3 - "$W" <<'PY'
import json,sys,os
W=sys.argv[1]; a=os.path.join(W,'mine','topo-meta.json'); b=os.path.join(W,'build','topo','meta.json')
if os.path.exists(a) and os.path.exists(b):
    mine=json.load(open(a)); now=json.load(open(b)); add={k:v for k,v in mine.items() if k not in now and os.path.exists(os.path.join(W,'build','topo',k+'.webp'))}
    now.update(add); json.dump(now,open(b,'w'))
PY
echo "Caught up with main. Kept from this session: $(ls "$W/mine/tools" "$W/mine/src" 2>/dev/null | grep -v ':' | grep -c . ) file(s) in tools/ and src/, $N old-map crop(s), and the LiDAR ledger."
if [ -n "$BOTH" ]; then
  echo "NEEDS A DECISION: main changed these files and so did this session. The workspace now has main's version; yours is in $W/mine/:"; for f in $BOTH; do echo "  $f"; done
  echo "Put your change into the workspace copy by hand, then build."
fi
echo "Anything you added to GUIDE.md, LEADS.md or CLAUDE.md on an unmerged branch must be added again after publish.sh makes the new branch."
echo "Next:  ATLAS=$W bash $W/tools/all.sh   then publish.sh to a NEW branch name."
