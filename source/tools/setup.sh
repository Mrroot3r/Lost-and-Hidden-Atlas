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
# The leads' second file (Native American sites and leads on reservation land, which a reader must switch on): on the site it
# is data/leads/native-<stamp>.json, the stamp being in data/leads.json; tools/leads.py and tools/make.py know it as
# build/leads_native.json.
rm -f "$W/build/leads_native.json"
python3 - "$REPO/data" "$W/build/leads_native.json" <<'PYEOF'
import json,os,sys,shutil
d,out=sys.argv[1],sys.argv[2]
x=(json.load(open(os.path.join(d,'leads.json'),encoding='utf-8')).get('x') or {}).get('native')
if x:
    f=os.path.join(d,'leads','native-%s.json'%x['h'])
    if not os.path.exists(f): sys.exit('setup.sh: data/leads.json names leads/native-%s.json but the file is missing'%x['h'])
    shutil.copyfile(f,out)
PYEOF
# The optional lead layers travel with the site in pieces: data/<layer>/index.json and one file per state named with its stamp.
# Put together again here into build/<layer>.json, the whole layer, which tools/vanished.py, tools/mines.py and tools/start.py
# read and tools/make.py cuts up again. (data/<layer>.json is NOT the whole layer: it is frozen at eleven states for old
# copies of the Android app. It is used only when a repository has no pieces yet.)
for f in vanished mines; do
  if [ -f "$REPO/data/$f/index.json" ]; then python3 - "$REPO/data/$f" "$W/build/$f.json" <<'PYEOF'
import json,os,sys
d,out=sys.argv[1],sys.argv[2]; ix=json.load(open(os.path.join(d,'index.json'),encoding='utf-8')); p=[]; s={}
for k,o in ix['s'].items():
    f=os.path.join(d,'%s-%s.json'%(k,o['h']))
    if not os.path.exists(f): sys.exit('setup.sh: %s is listed in %s/index.json but the file is missing'%(os.path.basename(f),d))
    rows=json.load(open(f,encoding='utf-8'))['p']; p+=rows; s[k]=len(rows)
json.dump({'v':1,'t':ix['t'],'p':p,'s':s},open(out,'w',encoding='utf-8'),separators=(',',':'),ensure_ascii=False)
PYEOF
  elif [ -f "$REPO/data/$f.json" ]; then cp "$REPO/data/$f.json" "$W/build/$f.json"; fi
done
# historic pockets: the built layer travels with the site, so a workspace without the raw downloads keeps every state
# Since November 20, 2026 it travels in pieces (tools/make.py): data/pock/index.json, each state's discs in
# data/pock/<state>-k-<stamp>.json and its markers and listings in data/pock/<state>.json. build/pockets.json is the whole
# layer put together again, which tools/pockets.py, tools/nearby.py and tools/make.py read. (data/pockets.json is NOT the
# whole layer: it is frozen at fifteen states for old copies of the Android app, and used only when there are no pieces.)
if [ -f "$REPO/data/pock/index.json" ]; then
  mkdir -p "$W/build/pock"; for f in "$REPO"/data/pock/??.json; do [ -f "$f" ] && cp "$f" "$W/build/pock/"; done
  python3 - "$REPO/data/pock" "$W/build/pockets.json" <<'PYEOF'
import json,os,sys
d,out=sys.argv[1],sys.argv[2]; ix=json.load(open(os.path.join(d,'index.json'),encoding='utf-8')); k=[]; s={}
for st,o in ix['s'].items():
    f=os.path.join(d,'%s-k-%s.json'%(st,o['kh']))
    if not os.path.exists(f): sys.exit('setup.sh: %s is listed in data/pock/index.json but the file is missing'%os.path.basename(f))
    k+=json.load(open(f,encoding='utf-8'))['k']; s[st]={a:b for a,b in o.items() if a not in('kh','n','b')}
k.sort(key=lambda p:(p[10]!='c',-p[11]))
json.dump({'v':3,'k':k,'s':s},open(out,'w',encoding='utf-8'),separators=(',',':'),ensure_ascii=False)
PYEOF
elif [ -f "$REPO/data/pockets.json" ]; then
  cp "$REPO"/data/pockets.json "$W/build/pockets.json"
  mkdir -p "$W/build/pock"; [ -d "$REPO/data/pock" ] && cp "$REPO"/data/pock/*.json "$W/build/pock/"
fi
# the LiDAR ledger (LIDAR.md): the repository's copy is folded into the workspace's, never over it, so verdicts a
# session has recorded and not yet published survive a second setup
[ -d "$REPO/source/lidar/walls" ] && { mkdir -p "$W/lidar/walls"; for f in "$REPO"/source/lidar/walls/*.json; do [ -f "$f" ] && { [ -f "$W/lidar/walls/$(basename "$f")" ] || cp "$f" "$W/lidar/walls/"; }; done; }   # stone walls per unit; a unit mapped in this workspace is not overwritten
[ -d "$REPO/source/lidar" ] && (cd "$W" && mkdir -p lidar && for f in "$REPO"/source/lidar/*; do [ -f "$f" ] && cp "$f" lidar/; done; python3 tools/lidar.py pull "$REPO/source/lidar/units" --base)
echo "$REPO" > "$W/.repo"                                                 # tools/start.py reads LEADS.md and GUIDE.md from here
git -C "$REPO" rev-parse HEAD > "$W/.setup_commit" 2>/dev/null || true    # publish.sh uses it to notice that main has moved on since
# what this machine can and cannot do
MISS=""
PKG() { case $1 in PIL) echo Pillow;; *) echo $1;; esac; }
# Each module is tried the way the tools use it, and installed for the python3 that will run them. A bare "import PIL" passes
# on a machine whose system copy of Pillow is broken (the pin check then dies on "cannot import name '_imaging'"), and plain
# "pip" may belong to another Python than "python3" does: both cost sessions an hour in November 2026 (their notes say so).
TRY() { case $1 in PIL) python3 -c "from PIL import Image, ImageDraw; Image.new('RGB',(2,2)).resize((1,1))" 2>/dev/null;; *) python3 -c "import $1" 2>/dev/null;; esac; }
for m in requests PIL rasterio shapely numpy scipy pypdf; do
  TRY $m && continue
  echo "installing the Python module $m ..."; EXTRA=""; [ "$m" = PIL ] && EXTRA="--ignore-installed"
  python3 -m pip install -q --break-system-packages $EXTRA "$(PKG $m)" >/dev/null 2>&1 || python3 -m pip install -q $EXTRA "$(PKG $m)" >/dev/null 2>&1 || pip install -q --break-system-packages "$(PKG $m)" >/dev/null 2>&1 || true
  TRY $m || MISS="$MISS $m"
done
[ -n "$MISS" ] && echo "MISSING Python modules:$MISS  (requests: everything; PIL + rasterio: old-map crops and pin checks; shapely: rebuilding lines). Install: python3 -m pip install --break-system-packages --ignore-installed requests Pillow rasterio shapely"
node -e "require('playwright')" 2>/dev/null || echo "MISSING Playwright for Node: the smoke test cannot run. Install: npm i playwright && npx playwright install chromium"
(cd "$W" && python3 tools/build_sites.py >/dev/null 2>&1) || true         # the place list, so nearby.py and start.py work at once
echo "Workspace ready at $W. Build with: ATLAS=$W bash $W/tools/all.sh"
echo "Research session? Begin with:  cd $W && python3 tools/start.py \"Town, State\""
