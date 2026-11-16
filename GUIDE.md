# Working on the Lost & Hidden Atlas

This is the handoff guide. It tells a new contributor, human or AI model, what the Atlas is, how it is built, how to add places without lowering its quality, and how a change gets published. Read it before changing anything.

## 1. What the Atlas is

A phone-first map tool for finding lost buildings, ruins and abandoned sites, made for a YouTube creator who explores them on foot. It began around Albany, New York and is deepest in upstate New York, Massachusetts and Rhode Island, with a batch for Kansas City, Missouri. Since November 2026 every US state and seven Canadian provinces hold at least one place, and every state and province has an outline, a region and a start city, so work can begin anywhere without setup.

Live site: https://mrroot3r.github.io/Lost-and-Hidden-Atlas/

What makes it useful, and what every change must protect:

- **It helps find the actual spot.** Each place can be viewed on leaf-off aerials, LiDAR terrain and an old USGS survey map laid over the modern one. Old rail, trolley and canal lines are drawn because buildings sat beside them.
- **It is honest about what it knows.** Every pin has a precision rating and a note saying where the coordinate came from. Unconfirmed facts are flagged, not smoothed over.
- **It keeps the user legal.** Each place states access. Public-land and parcel-owner lookups are built in. Nothing in the Atlas tells anyone to enter a building or cross a fence.
- **It works in the field.** Used on a phone, often with weak signal: offline saving, a GPS dot, a field log.

## 2. How it works

The site is static files on GitHub Pages. There is no server and no account. A visitor's notes, progress, added places and field logs live in their own browser (`localStorage` key `lost-hidden-atlas-v1`); map tiles they have viewed are cached in IndexedDB.

| File | Role |
|---|---|
| `index.html` | Page, styles, and two inline JSON blocks: `d-sites` (places, batches, start cities, guide text) and `d-base` (outline map used only if tiles cannot load) |
| `app.js` | The whole app: one plain-JavaScript file, no framework, Leaflet for the map |
| `sw.js` | Service worker: page is fetched fresh when online, served from cache when not; versioned files and `topo/` images are cached once |
| `data/lines.json` | Old rail, trolley and canal lines; fetched after load |
| `data/pockets.json` | Historic pockets: every state's old town centres and other pockets of markers and National Register listings, one row each. Small; fetched only when the layer is turned on |
| `data/pock/<state>.json` | One state's single markers, listings and district outlines; fetched only when the map is zoomed in on that state |
| `data/leads.json` | Unchecked leads from OpenStreetMap; fetched when the Leads layer is turned on |
| `topo/<place-id>.webp` | One cropped old USGS map per place; fetched when the place is opened |
| `boot.js`, `version.json` | Used only by the Android app (section 12): its start-up script, and the small file it reads to see whether the places have changed |
| `android-app/` | The Android app: the same page in an app shell, plus a background recorder for the field log |
| `source/` | Everything the site is generated from |
| `source/tools/states.py` | The base for every state: its regions, start cities and what is wired up for it |
| `LEADS.md` | Places someone read about but did not add, and why |

**Never edit the files in the repository root by hand.** They are build output. Edit `source/` and rebuild.

Map layers come from public services, chosen per state. `regionOf()` in `app.js` works out the state of any point from simplified Census outlines of the nine Northeast states (`source/build/states.json`), so nobody has to describe a border by hand.

- Streets and satellite: Esri. Current and old topo: USGS and Esri.
- Leaf-off aerial and LiDAR: New York (NYS ITS, slow export services, heavily cached), Massachusetts (MassGIS tiles), Vermont (VCGI tiles), Rhode Island (RIGIS image services at `maps.edc.uri.edu/rigis`: the March 2026 flight and the 2022 LiDAR elevation service, shaded on request like New York's). Other states fall back to Esri satellite and world hillshade.
- Public land: USGS PAD-US. Owner lookup and lot lines: NYS tax parcels (only some counties share owner names), NYS DEC, MassGIS parcels (statewide). None yet for Rhode Island.
- Drive times: OSRM, precomputed at build time from the start cities in `tools/drive.py`.

## 3. How a change gets published

**Nothing goes straight to `main`.** Merging to `main` publishes the site within about a minute, so every change travels as a pull request that the owner merges.

1. Start from a fresh clone of `main` and build a workspace (commands below).
2. Make the change in the workspace, rebuild, run the checks and tests.
3. `publish.sh` puts the result on a **new branch**. Commit once, push the branch, open a pull request into `main`.
4. **Stop there.** Do not merge your own pull request, even if you can. Say in the pull request what changed, what you verified, and what you could not.
5. GitHub runs `check` on the pull request (place-list validation, source and build in step, a phone-size test that the site opens). The owner merges when it is green, using **Squash and merge** so each change is one commit.

**If the push is refused.** A cloud session's built-in GitHub login is often read-only or expired, and `git push` fails with a 401 or 403 or "invalid credentials". Do not retry and do not look for another login. Attach the repository to the session with write access first (in Claude: the `add_repo` tool with `access: "push"`, then `register_repo_root`), then push again. If attaching is declined, stop and tell the owner; never paste a token into a file or a command.

**Undoing a change.** Each merged pull request is one commit that holds both the source and the built site, so undoing it restores the previous site exactly.

- Owner: open the merged pull request on GitHub, press **Revert**, and merge the pull request it creates.
- Model: `git revert <commit>` on a new branch, then a pull request as usual. Never force-push or reset `main`.
- Visitors' saved notes are untouched by a revert. Notes on a place that disappears stay stored and return if the place does.

**If `main` moved while you worked.** Build output always conflicts. Take `main`'s version of everything outside `source/`, merge `source/` by hand, then run setup, build and publish again. Keep one data pull request open at a time to avoid this.

### Commands

```bash
git clone --depth 1 https://github.com/mrroot3r/lost-and-hidden-atlas repo
bash repo/source/tools/setup.sh /path/to/work     # builds a clean working folder; reports missing dependencies
export ATLAS=/path/to/work
# ... edit $ATLAS/src and $ATLAS/tools ...
bash $ATLAS/tools/all.sh                          # rebuilds everything into $ATLAS/dist/web
(cd $ATLAS/dist && python3 -m http.server 8766) &
node $ATLAS/tools/smoke.js http://localhost:8766/web/ [place-id]   # phone-size test; give a new place's id to test its tiles
bash $ATLAS/tools/publish.sh repo my-branch-name  # copies build and sources onto a new branch, stages, runs check.py
git -C repo commit && git -C repo push -u origin my-branch-name
# open the pull request (REST works where the gh pr commands do not):
gh api repos/mrroot3r/Lost-and-Hidden-Atlas/pulls -f title="..." -f head=my-branch-name -f base=main -f body="..."
```

`setup.sh` replaces the workspace's `src/`, `tools/` and `build/topo/` so nothing stale survives from an earlier session; files it does not recognise are moved to `stray/` and listed. It keeps `cache/` and `research/`.

Needs Python 3 with `requests`; `Pillow` and `rasterio` for old-map crops and pin checks; `shapely` only for rebuilding lines; Node with Playwright for tests.

What `all.sh` runs, in order: `build_sites.py` (merge place lists) → `drive.py` (drive times) → `padus.py` (public-land status per pin) → `leads.py` → `make.py` (assemble the site) → `export.py` (CSV and KML).

Run only when needed:

- `python3 tools/topo_all.py <id> <id> …` cuts old-map crops for new places. It downloads large USGS scans, so run it only for new ids.
- `python3 tools/pincheck.py --batch <key>` makes contact sheets of every new pin on an aerial (section 6).
- `tools/lines.py` rebuilds the rail, trolley and canal lines, and `tools/leads.py` the leads. The raw downloads they read are not in the repository, and neither needs all of them: each rebuilds only the areas whose raw files are in `cache/osm/` and keeps what is already in `build/lines.json` and `build/leads.json` for everywhere else. Run them only when adding a state (section 8, "Lines and leads for a new state").
- `tools/osm_layers.py <key>` and `tools/ohm_state.py <key>` download a whole state's old railways, canals and mapped ruins.
- `tools/osm_leads.py`, `tools/osm_worc.py` download leads from Overpass.

### What a cloud session usually cannot reach

Check these once and move on; do not spend time retrying.

| Service | What happens | Do instead |
|---|---|---|
| Wikipedia search and query API | HTTP 429 for minutes at a time, even batched and paced | `tools/wiki_raw.py`, which reads one article at a time as raw text |
| Overpass (OpenStreetMap queries) | Blocked or timing out on every mirror. `maps.mail.ru` sometimes answers, but cuts any request off at about 57 seconds, which is too short for even a quarter-degree box. Geofabrik extracts are blocked too | `tools/osm_layers.py`, which reads the copies of OpenStreetMap that Esri hosts as feature layers (updated daily). OpenHistoricalMap's own Overpass server works: `tools/ohm_state.py` |
| Everything else used here (ArcGIS geocoder, state image services, OSRM, USGS TNM, PAD-US) | Has worked | |

## 4. The place record

Places are Python calls to `N(...)` in `source/tools/data_*.py`. Each file is one **batch**. `data_ri.py` and `data_worc.py` are the cleanest examples. `data_a.py` and `data_b.py` are the original catalogue and have an older shape; leave them alone.

A batch file must define three names, and then `build_sites.py` picks it up by itself. No other code changes are needed:

```python
BATCH={'key':'ct','label':'Connecticut','added':'2026-12-01'}   # key: short and unique; added: sorts batches, newest last
PLACES=[ N(...), N(...) ]
PIN_NOTES={'place-id':'One sentence on where the coordinate came from.'}
```

The app shows the newest batch as a quick filter and lists every batch under Filters, "Added in".

```python
N(id, name, town, reg, cat, st, lat, lon, prec, acc, eff, tags, years,
  story, look='', hook='', accn='', links=None, conf=None, th=None, thn=None)
```

| Field | Meaning and allowed values |
|---|---|
| `id` | Unique lowercase slug with hyphens. Ids are shared across every state, and common names repeat (`queens-fort` exists in New York), so give a new place a town or state suffix when in doubt: `queens-fort-exeter`. **Never rename a published id**: saved notes are keyed to it |
| `reg` | Region code from `tools/states.py`. Every Northeast state already has regions; pick the one the place is in. `check.py` fails if the pin is not inside that region's state |
| `cat` | `amuse` `hotel` `canal` `rail` `industry` `burial` `town` `civic` `fort` `water` `inst` `light` `landmark`, and `lidar` for a place found on LiDAR that nobody has written up (section 13; always `conf='lead'` until someone has stood on it) |
| `st` | What is left: `ruins` `traces` (grades, piers, earthworks) `standing` `marker` `gone` `water` (drowned) |
| `prec` | `exact` (on the structure, about 30 m) · `site` (inside the footprint, about 150 m) · `area` (right vicinity only, about 500 m) |
| `acc` | `public` · `view` (see it from a public way) · `ask` (private, permission needed) · `permit` · `boat` |
| `eff` | `drive` `walk` `hike` `boat` |
| `tags` | Comma-separated series tags: `trolleyparks` `amusements` `hotels` `burned` `inclines` `canal` `stations` `drowned` `forts` `cemeteries` `renewal` `stove` `monitor` `now` |
| `years` | Short span such as `1897–1963`, or empty if not sourced |
| `story` | Two to four plain sentences: what it was, what happened to it |
| `look` | What a visitor can actually see or should search for |
| `hook` | Optional one-line video angle |
| `accn` | Access note: who owns or manages it, hours, fees, hazards |
| `links` | Sources as `[label, url]` pairs. `W('Article title')` makes a Wikipedia link |
| `conf` | Empty when sourced. `'mixed'` when the outline is sourced but a detail is unconfirmed or sources disagree. `'lead'` when the entry is unverified |
| `th`, `thn` | Parking or trailhead `[lat, lon]` and its name, when the pin is not where you park |

`python3 source/tools/check.py` validates all of this without a network. `publish.sh` runs it, and so does GitHub on every pull request.

## 5. Research rules

These are what keep the Atlas trustworthy. They are not optional.

1. **Every fact needs a source you actually read.** Dates, names, numbers and "what remains" claims come from the linked source. If you cannot source a detail, leave it out or write "not confirmed" and set `conf`.
2. **Do not fill gaps from memory.** A model's recollection of a place is a lead to check, never a fact to publish. This matters most for what survives on the ground, which changes.
3. **When sources disagree, say so.** Give both versions in the text ("the closing year is not confirmed: the articles give both 1995 and November 1994"), set `conf='mixed'`, and do not pick one.
4. **Be honest about the pin, and look at it.** A coordinate from a Wikipedia infobox, an OpenStreetMap feature, an address lookup or a trail log is fine if the pin note says so. But such coordinates are often off the structure: in the Rhode Island batch 5 of 28 were visibly wrong on the aerial. Run the pin check in section 6 on every new pin. Move a pin only when you can see the right spot; otherwise keep it, use `prec='area'`, and say what the aerial showed. Never invent or nudge a coordinate blind.
5. **Say what is left, not what was there.** A demolished site is `gone`, however famous. Check for recent demolition, fire or redevelopment.
6. **Access is part of the entry.** Legal access detail is wanted and useful: who owns or manages the land, where to park, which trail or public path reaches it, hours, fees, permits, who to ask. Private or unknown means `ask` or `view`. Active railroads, mines, tunnels and sealed buildings get a plain warning. The one thing that stays out is how to get past a barrier into somewhere closed: a fence, a locked gate, a sealed building, a closed bridge. If that is the only "access" a source describes, write that the place is closed.
7. **Write plainly.** Short sentences, no hype, no filler. Put the facts in your own words; do not copy source sentences.
8. **Prefer places with something to find.** Ruins and traces first, then standing landmarks with a story, then vanished sites that matter to a series.
9. **Record what you did not add.** A place you read about but could not source or locate goes in `LEADS.md` with one line on what is missing.

## 6. Research workflow

1. **Collect exact titles.** Guessed article titles fail (the Ladd School is "The Ladd School"). Open a list page first and copy names from it: "National Register of Historic Places listings in *county*", "List of amusement parks in *state*", a state's "Category:" pages, state park and land-trust site indexes.
2. **Read each article:** `python3 tools/wiki_raw.py "Exact title" …` prints its coordinates and opening text; add `-g 'closed|demol|remain|ruin'` to pull only the sentences about what happened and what is left. Other sources that have worked: state park and land-trust pages (access, trail maps), National Park Service pages, town historical societies, the ArcGIS geocoder (`findAddressCandidates`) for addresses and named places, and `python3 tools/nom.py "name, town, state"` for a ruin, trail feature or building that someone has mapped in OpenStreetMap.
3. **Write the entries** in a new `data_<area>.py` with its `BATCH`, `PLACES` and `PIN_NOTES`.
4. **Build the list:** `python3 tools/build_sites.py`. It stops on a duplicate id or a missing pin note.
5. **Check every pin:** `python3 tools/pincheck.py --batch <key>` writes contact sheets to `research/`: one 300 m aerial square per pin with a 30 m ring. Look at every tile. Fix what you can see, downgrade what you cannot, and record in the pin note what the aerial showed. When the ring is off the structure, `python3 tools/look.py out.jpg label,lat,lon,300` draws a wider view with a grid so you can read off where the structure is, and `python3 tools/pad.py label,lat,lon` tells you which public-land unit a point is in (US only). A managing agency's page that the fetch tool refuses can usually be read with `python3 tools/page.py <url>`, which prints the sentences about hours, fees, trails and closures.
6. **Cut old maps** for the new ids with `topo_all.py`, then run `all.sh`.
7. **Test:** the smoke test with one of the new place ids, then open a few new places in a browser at phone size.
8. **Publish** as a pull request (section 3). List in it anything you could not verify.

## 7. Handing research to a cheaper model

Give it sections 4, 5 and 6 and a prompt like the one below. Have a stronger model, or a person, spot-check a sample before the pull request is merged; "what remains today" and coordinates are where cheaper models slip.

```
You are adding places to the Lost & Hidden Atlas, a map of ruins and lost
buildings. Area: <county or region>. Find <N> candidate places that have
ruins, traces or a standing landmark with a story.

For each place, read at least one source and return one Python N(...) call
in the format below, plus one pin-note line. Rules:
- Use only facts stated in a source you opened. Link every source.
- If sources disagree, give both versions and set conf='mixed'.
- If you cannot confirm what remains today, say "Not confirmed" in `look`
  and set conf='mixed' or conf='lead'.
- Give the coordinate's origin in the pin note. If it marks a town, road or
  park and not the site itself, say so and use prec='area'.
- Give legal access detail when a source has it: owner or manager, parking,
  trail, hours, fees. Otherwise acc='ask' or 'view'. Do not describe how to
  get past a fence, a lock or a sealed entrance.
- Use a region code from tools/states.py for the state the place is in.
- Plain short sentences in your own words. No hype.
- Skip a place rather than guess, and list it with what was missing.

<paste the field table from section 4 and one example entry>
```

## 8. Opening a new state or area

The base is already in place for every US state, the District of Columbia and the ten Canadian provinces. For each, `tools/states.py` lists its regions and start cities (the capital and the main cities), the map covers it, state detection works, and satellite imagery and a world hillshade load as a fallback. **To start work in any of them, you only add a batch of places** (section 6) using that state's region codes.

| State | Places so far | Leaf-off and LiDAR | Owner lookup | Law note in the app |
|---|---|---|---|---|
| New York | Capital Region outward; none yet in NYC, central, western or northern regions | State services | Some counties | Yes |
| Massachusetts | Statewide first pass, Worcester County deeper | State services | Statewide | Yes |
| Rhode Island | First pass | State services | No | Yes |
| Vermont | A few in the south, two farther north | State services | No | No |
| Connecticut | Five | Fallback only | No | No |
| New Hampshire, Maine, New Jersey, Pennsylvania | A first handful each, all woods ruins on public or preserve land (the "Ruins in the woods" batch) | Fallback only | No | No |
| Missouri | Kansas City only (region `kcmo`, start city Kansas City), first batch November 2026 | Fallback only | No | No |
| The other 40 states | One place each, in `data_states.py` ("A first place in every state"). Each has one statewide region whose code is the state's two letters (`tx`, `ca`) and one or two start cities | Fallback only | No | No |
| Ontario, Quebec, New Brunswick, Nova Scotia, Manitoba, Alberta, British Columbia | One place each, in the same batch. Region code is the province's two letters (`on`, `qc`) | Fallback only. No USGS old maps and no public-land lookup in Canada | No | No |
| District of Columbia, Prince Edward Island, Newfoundland and Labrador, Saskatchewan | None yet. Outline, region and start city are ready | Fallback only | No | No |

Beyond adding places, these make a state better. Do them when asked, or note in section 10 that they are still open.

| Step | When | What to do |
|---|---|---|
| Law note | **Optional. Only when the owner asks** | Add the state's trespass basics to the in-app Guide and set `legal` to `True` in `states.py`. Read the statute; do not paraphrase from memory. A batch is complete without it: the owner's position is that knowing the local law is up to whoever visits. What is never optional is the access line on each place (who owns it, whether it is open, closed or posted) |
| State imagery | When the state publishes it | Add its leaf-off and LiDAR services to `leafUrl()` and `lidarUrl()`. Check they send CORS headers, note their deepest zoom, and look at a tile over open water (some services return black there). Then test with `node tools/smoke.js <url> <place-id>` |
| Rail and canal lines, and leads | When the owner asks for a state | See "Lines and leads for a new state" below. Done for all of New York and Massachusetts |
| Owner lookup and lot lines | Can wait | Add to `lookup()` and `drawLots()` if the state publishes parcels with owner names |
| A new region or start city | When a state's regions are too coarse, or its one statewide region holds more than a few dozen places | Add it in `states.py`: for example `('txw','West Texas')` beside the statewide `('tx','Texas')`. Leave the statewide code in place for the places already using it; never rename a region code that published places use. Check a new start city's coordinate with a geocoder, not from memory |

### Starting a new chat from nothing

A new session knows nothing about this project. With the repository attached, this prompt is enough to go from an empty area to documented pins in a pull request:

```
Read CLAUDE.md and GUIDE.md in the Lost-and-Hidden-Atlas repository, then add a batch of places for
<city, county or region, and state>. Follow GUIDE.md sections 3 to 6 exactly: build the workspace with
setup.sh, find candidates from list pages, read a source for every fact, write one data_<area>.py batch,
look at every pin with pincheck.py and say in each pin note what the aerial showed, cut old maps, run
all.sh, check.py and the smoke test, add what you could not source to LEADS.md, and open a pull request
that says what you verified and what you could not. Do not push to main or merge. Aim for <N> places,
ruins and traces first.
```

Name the area and a number; everything else is in the guide. If the area is a city the Atlas has no start city for, the session should add one to `tools/states.py` (the table above).

### Lines and leads for a new state

The old rail, trolley and canal lines and the leads layer exist for all of New York and Massachusetts, with a strip of western Connecticut and Vermont. Every other state has none yet. To add a state (its outline must already be in `build/states.json`):

1. `python3 tools/osm_layers.py <key>` downloads the state's abandoned, disused and razed railways, its canals, and its mapped ruins from the OpenStreetMap layers Esri hosts. It looks each old railway up in the highways layer to tell which are rail trails today. About ten minutes for New York.
2. `python3 tools/ohm_state.py <key>` downloads OpenHistoricalMap's railways and canals, which carry opening and closing years.
3. Add the key to `STATE_KEYS` at the top of **both** `tools/lines.py` and `tools/leads.py`.
4. `python3 tools/lines.py` (several minutes) and `python3 tools/leads.py`, then `all.sh`. Both keep the existing lines and leads for every area whose raw files you do not have, so a fresh workspace only rebuilds the new state. Railroads in use come from the federal rail network and are fetched for the new state by `lines.py` itself.
5. Look at the result at phone size over the state's cities, and tap a few lines. Trolley and interurban lines are recognised by name (`TROL` in `lines.py`): add the state's interurban company names there if they show as plain abandoned railroad. Canals still in use are listed by name in the same file.
6. Say in the pull request how many kilometres of each kind were added (`lines.py` prints them).

What the layer route loses compared with a full OpenStreetMap download: a line tagged only as `abandoned:railway=…` with no `railway=abandoned` is missing (about 5% by length in the Capital Region, where both were available to compare), and old names kept in tags such as `old_name` are missing, so more lines are unnamed. Leads from the layers are thinner than from Overpass: only mapped historic points and ruined or abandoned buildings.

### Historic pockets for a new state

The owner's idea: showing every historical plaque is clutter, and most plaques mark something that is gone, but where many sit close together, with listed buildings among them, there is usually an old town centre worth walking ("some of my best finds as far as buildings have been just walking through old towns"). The layer ("Historic pockets" in Map options) therefore puts **old town centres** first:

- An **old town centre** is one purple disc per town, carrying the town's name, ranked by a score. The best ones in view are labelled, and Map options lists the ones within 40 miles of the start place, richest or nearest first.
- Every **other pocket** (an estate, a mill site, a battlefield, a campus, a city neighbourhood away from the centre) is a dashed grey ring. "Old town centres only" in Map options hides them.
- The single markers and listings appear only from zoom 15. Zoomed out, only the richest discs show, so a state full of old villages is not one purple smear (`pockFrom` in `app.js`).

Done so far:

| State | Old town centres | Other pockets | Markers held | Register listings | Counties whose marker list is cut at 500 (markers they have) |
|---|---|---|---|---|---|
| New York | 555 | 753 | 14,908 | 6,563 | Albany (597), Erie (678), Kings (684), Nassau (543), New York (2311), Orange (619), Saratoga (653), Suffolk (532) |
| Massachusetts | 358 | 413 | 3,526 | 4,509 | Middlesex (570), Suffolk (627) |
| Vermont | 142 | 48 | 1,110 | 913 | none |
| Connecticut | 220 | 194 | 2,747 | 1,662 | Capitol Region (726), South Central Region (545) |
| New Hampshire | 94 | 43 | 965 | 821 | none |
| New Jersey | 215 | 220 | 4,900 | 1,815 | none |
| Pennsylvania | 385 | 477 | 12,612 | 3,671 | Adams (1533), Allegheny (1192), Chester (506), Cumberland (528), Lancaster (625), Philadelphia (1922), York (511) |

To add a state (about an hour, nearly all of it waiting on step 4):

1. `python3 tools/nrhp_state.py "<STATE NAME>" <key>` downloads the National Register listings from the National Park Service (public domain).
2. `python3 tools/wd_nrhp.py <key>` cuts the same listings out of Wikidata (public domain), which `pockets.py` uses to put the Park Service file right. The first run in a workspace asks a public copy of Wikidata **once** for the whole country and keeps the answer in `cache/wd/nrhp_all.json`. Never put that question in a loop: when this was written Wikidata's own query service was refusing all but one request a minute.
3. `python3 tools/osm_places.py <key>` downloads the state's settlement points (city, town, village, hamlet) from the copy of OpenStreetMap that Esri hosts.
4. `python3 tools/hmdb_state.py "<State Name>" <key>` downloads each county's list of markers from HMdb.org: number, title, town, position, the earliest year the title or first line names (as a number), and whether it is filed as a war memorial. It waits between pages: ten minutes for a small state, forty for New York or Pennsylvania. The county names come from HMdb.org's own page of geographical names, because not every state is filed by county (Connecticut is filed by planning region).
5. Add the key to `KEYS` in `tools/pockets.py`, run it, then `all.sh`. It rebuilds the states whose raw files you have and keeps every other state as it is (`setup.sh` copies the built layer from the repository into the workspace for exactly this).
6. `python3 tools/pock_report.py <lat> <lon> <miles>` prints the ranking round a town you know. Read it: are the top names the places a person would walk for old buildings? Then look at a few towns at phone size with the layer on.

**The rules for HMdb.org data, which are not optional:**

- Its copyright page allows copying its information without asking only for uses that are **not commercial**, and only when it is **credited to HMdb.org with a link**. The app credits and links every marker it shows and names HMdb.org in the Guide. Never store inscriptions or photos. Do not reuse the marker data in anything that earns money without written permission from HMdb.org.
- It shows the first 500 markers of any list without signing in and asks for a sign-in beyond that. **Never sign in and never work around that limit** (for example by cutting a county into towns). A county with more than 500 markers stays incomplete, and `hmdb_state.py` prints which ones. The owner can register (free) and download a full list by hand if a county matters.
- Wait several seconds between pages, as the tool does, and run one state at a time.

**How a pocket is made and ranked** (`tools/pockets.py`; every number below is a named constant at the top of that file):

1. *The listings are put right first.* The Park Service file has three faults that matter here, and Wikidata mends them: a listing the two sources place more than 250 m apart takes Wikidata's position (checked against town points for listings named after a town, Wikidata was the closer about twice in three); a "building" that counts eight or more contributing buildings is a district filed under one of its houses (Hudson's whole downtown is "Robert Jenkins House") and takes Wikidata's name; and a listing the Park Service file lacks is added, without a building count.
2. *Chains.* Markers within 30 m of each other are one spot (a memorial walk with hundreds of plaques counts as a handful of spots). Spots and listings within 220 m of each other chain together.
3. *Old town centres.* A chain that comes within 300 m of a hamlet's point (400 m village, 500 m town, 600 m city) belongs to that settlement, out to 500 m from the point (700, 800, 1100). A district named after the settlement ("Cobleskill Historic District", "Kingston Stockade District") belongs to it up to 2.5 km away (3.5 km for a city), because the Register's coordinate for a district is the middle of a rough box and is often a kilometre off. Everything a settlement gathers is **one** pocket with the settlement's name. It is kept as a town centre only with evidence: a district of eight or more buildings, or listed buildings worth four points, or three plaque spots about things from before 1901 (the exact test is `is_centre`). A district whose own name says Village, Downtown, Main Street, Commercial, Business or Central is a centre even with no settlement point (an old village swallowed by a city, such as Lansingburgh in Troy).
4. *Other pockets.* What is left over, if it weighs enough (a spot 1, a listed place 2, a district 3 to 30). A leftover chain longer than 900 m is cut into 600 m blocks.
5. *The score* (about 56 at most) counts what still stands before what is only remembered: up to 22 for the contributing buildings of districts (4 × log2(1 + buildings ÷ 15), so 45 buildings is 8 and 450 is 20), up to 15 for individually listed buildings (a church, courthouse, bank, hotel, depot, store, mill or hall counts 2, anything else 1), up to 15 for plaque spots (1.5 each for a year up to 1830, 1.2 up to 1900, 0.6 up to 1945, 0.3 later, 0.7 undated, 0.4 for a war memorial), and 4 when a district's name marks a centre.

`python3 tools/pock_panel.py` is the panel the numbers were tuned on: 63 towns round Albany that ought to be centres and ten estates, battlefields and cemeteries that ought not. It needs New York's raw files. When this was written 57 of the 63 were centres under their own name; the other six (Castleton-on-Hudson, Stillwater, New Lebanon, Tivoli, Windham, Waterville) have no Register district and too few plaques for any rule to find. Run it after changing a number.

**The files.** `data/pockets.json` is the index: `k` is one row per pocket, `[lat, lon, radius m, markers, listed places, districts, contributing buildings, name, state, marker spots, type, score, era, settlement kind]` (type `c` = old town centre, `p` = other; rows are sorted centres first, best score first, and `app.js` relies on that), and `s` holds each state's counts and `h`, a stamp of its detail file. `data/pock/<state>.json` is the detail: `m` markers `[lat, lon, HMdb number, title]`, `r` listings `[lat, lon, reference, name, kind, contributing buildings or -1, year listed]`, `d` district outlines. The website fetches a detail file when the map is zoomed to 15 near that state's pockets. The Android app carries the files it was built with; `boot.js` fetches a state's detail from the site when the app does not have it, and after a data update downloads again only the states whose stamp changed. `node source/tools/app_pockets.js` checks those three cases; run it after touching any of this.

### A province, territory or country that is not listed yet

Every US state and Canadian province was set up this way in November 2026, so this is only needed for somewhere new (a Canadian territory, Mexico, Puerto Rico). It needs five things besides its batch of places, all in the same pull request:

1. **Outline.** `python3 tools/outlines.py <key>` writes it into `build/states.json` (needs `pip install pyshp shapely`). It reads the Census 1:20,000,000 state file for the US and Natural Earth 1:10,000,000 for Canada, pushes the shape out about 3 km so that pins on a shore or a near island still fall inside, cuts away every neighbour's land, simplifies it, and stores each ring closed as a flat list `[lon, lat, lon, lat, …]`. For another country, add its source to `load()` in that file. State detection (which imagery and which law note apply) and `check.py` read these outlines; nothing draws them, so they are coarse. Outlines already in the file are left alone unless you name their key.
2. **Entry in `tools/states.py`:** key, name, `imagery` (say "fallback" unless you add state services), `owners`, `legal: False`, its region codes, and at least one start city (`hubs`) with coordinates. The build works out drive times from every start city.
3. **Map limits.** `MAXB` near the top of `source/src/app.js` is the box the map can be moved inside, as `[[south, west], [north, east]]`. It now runs from 17.5° N to 72° N and from 170° W to 50° W, which holds Hawaii, Alaska and Newfoundland. Widen it only for somewhere outside that. If a pin is outside the box, `check.py` fails and the map springs back before reaching it. `minZoom` is 3, which shows the whole box on a phone.
4. **`tools/pincheck.py`** picks an aerial service by a rough box per state. Anything outside those boxes falls back to Esri satellite. If you add state imagery, add its box; check that the New York box (it once swallowed everything west of New York) does not cover the new state.
5. **Known gaps.** Write in section 10 what the state does not have yet (state imagery, owner lookup, lines, leads).

**The live site and the installed app do not show any of this until the pull request is merged.** The Android app carries its own copy of `app.js`, so a change to the map limits or settings reaches the phone only with the next app build (the pull request's `app` check publishes a test build; the merge publishes the release). New places alone arrive through the app's data refresh without a new build.

**Where the map opens.** Nobody has to pick a start city for a far-away area. The map reopens where it was last left, and until the reader chooses a start place by hand, drive times count from the start city nearest to their location (or last known location). A reader whose device has no location (a desktop with location turned off) can choose a start city, pick a spot on the map, or type a town, address, ZIP code or coordinates under the gear in Map options. Typed names are looked up with OpenStreetMap's Nominatim; typed coordinates are not sent anywhere.

**Drive times.** `tools/drive.py` gives each place a drive time only from the start cities within 450 miles in a straight line. Beyond that, and where no road joins the two (Hawaii's other islands from Honolulu), the app shows its own rough estimate marked `~`. Adding a start city to `states.py` is enough; the next build works out its times.

**Canada.** The app, the pin check, the place lookup (`tools/nom.py`) and drive times work the same there. Three things do not exist for it: USGS old maps (`topo_all.py` prints `no map`, which is expected), the PAD-US public-land lookup (so a Canadian place never shows a land line; say who manages the land in the access note), and any law note.

**Old-map crops.** `tools/topo_all.py` cuts a crop for every new place except those in the `landmark` category, which it skips on purpose (a standing landmark is on the current map). If a `landmark` place is really a trace on the ground, such as trail ruts, and an old map would help, give it a more specific category or pass its id after removing the skip for that run; do not report the missing crop as a failure.


## 9. Changing the app

- `app.js` is one file with sections marked by comments. State is the object `U`; `save()` persists it. Add new saved fields to `U0()` so old backups still load.
- The phone layout is the main one: a scrolling icon bar under the map, an options sheet with a fixed Done button, four tabs (Places, Trip, Log, Guide). Keep touch targets large. Test at phone size first.
- The app must still work when a data file fails to load or the phone is offline. Show a short message; never a blank screen.
- Bump nothing by hand: `make.py` stamps a version into `index.html`, the script URL and `sw.js` on every build.
- The app also builds as a single self-contained file (`dist/Lost-and-Hidden-Atlas.html`). It detects that mode by the presence of an inline `d-topo` block.
- **Settings** live under the gear in the map options sheet (`buildSettings()`). Each one is a key in `SET0`, read with `pref(key)` and stored in `U.set`; add a new setting by adding its default to `SET0`, a row in `buildSettings()`, and a `pref()` call where it applies. Distances go through `fmtMi()`/`miTxt()` and clock times pass `hour12:H12()`, so new text respects the units and clock settings. Backups, the app's data source and offline storage are the collapsible sections at the end of Settings (`dataSections()`), not in the Guide.
- The same `app.js` runs inside the Android app. Anything app-only sits behind `AT` (running in the app) or `NATIVE` (the phone's recorder is available); the website must behave exactly as before when both are false. Run `tools/app_smoke.js` as well as `tools/smoke.js` after touching the field log, old maps, or data loading.
- Installed apps keep their copy of `app.js` until the owner installs a new build, but they fetch new place data straight away. So place data must stay readable by older app code: **add fields, never rename or remove one the app reads.**

## 10. Known gaps

- Most pins added in November 2026 for New York and Massachusetts were not checked against imagery; their pin notes say so. Rhode Island pins were each looked at once on the state aerial, and none was moved.
- Vermont, Connecticut, New Hampshire, Maine, New Jersey and Pennsylvania have regions, start cities, fallback imagery and a first handful of places each, and no law note in the app (optional, see section 8).
- The "Ruins in the woods" batch (November 2026) has no trailhead coordinates: access notes name the road or lot. Most of its pins sit under tree cover and could not be confirmed on an aerial; `tools/pincheck.py` had no leaf-off imagery outside New York. Its Pennsylvania and Maine entries were written from one Wikipedia article each.
- The LiDAR tools (section 13) work in New York only, were tried on one wildlife area, and are tuned for 1:62,500 sheets and cellar-hole-sized pits. Stone walls, mill races and charcoal hearths are not detected. The four `lidar` places have not been visited.
- Pins taken from OpenStreetMap through Nominatim (`tools/nom.py`) are a named mapped feature, which is usually closer than an article coordinate, but for a tunnel or a long path the point is the middle of the line.
- Rhode Island is a first pass: no owner lookup or lot lines (the state has a tax-parcel map service at `risegis.ri.gov`; whether it carries owner names was not checked), no leads, no rebuilt rail and canal lines.
- The Rhode Island LiDAR service returns black or blank tiles over open water.
- Leads are missing for greater Boston, the South Shore, Cape Cod, Rhode Island and Missouri.
- The start-place changes of November 2026 (map reopens where it was left, nearest start city chosen from location, typed start place) were tested in a desktop browser at phone size only, not on a phone or in the Android app. The typed lookup depends on OpenStreetMap's public Nominatim service, which is for light use.
- The "A first place in every state" batch (November 2026, `data_states.py`) is one place for each of 40 states and 7 provinces, meant as a worked example per state, not coverage. Each was written from one Wikipedia article plus, for most, the managing agency's own page; 17 have Wikipedia as their only source, which the links on each place make plain. Agency pages that would not open from the cloud session are named as such in the entry (Florida State Parks). Pins were looked at on Esri satellite only; about a third sit under tree cover and could not be confirmed, and the pin notes say which. `new-manchester-mill` marks the park and not the ruins. `daniels-md`, `spokane-sd` and `piedmont-charcoal-kilns` are `mixed` because access or a count is unsettled. Only two have a trailhead coordinate.
- Canada has no old-map crops, no public-land status and no law note. Hawaii's only start city is Honolulu, so a place on another island shows a rough drive estimate that means little.
- State and province outlines added in November 2026 are coarse (simplified to roughly 1 to 5 km) and pushed about 3 km out to sea. A pin within a kilometre or two of a state line can be read as the neighbouring state; `check.py` will say so. If the coordinate is right, remake that outline more finely with `outlines.py` (lower its tolerance) before changing the pin.
- Rail, trolley and canal lines and leads (November 2026) cover all of New York and Massachusetts. Outside the Capital Region and the Hudson Valley, New York's come from the hosted OpenStreetMap layers (see section 8 for what that loses). Buffalo's and New York City's yards show as dense bundles of parallel abandoned tracks, and many street-railway lines in New York City are drawn as plain abandoned railroad because OpenStreetMap does not name them. None of the new lines was checked on the ground or against an old map. No other state has lines yet.
- **Come back to: Overpass.** New York's old lines and leads outside the Capital Region and Hudson Valley were built from Esri's hosted copies of OpenStreetMap because Overpass could not be reached (November 16, 2026). That loses lines tagged only as `abandoned:railway=…` (about 5% by length where both could be compared), old names kept in tags such as `old_name`, and most leads. Run `python3 tools/overpass_check.py` at the start of a session that touches lines. When it reports a usable mirror: download New York with the queries in `tools/osm_fetch.py` (in tiles of half a degree or less), save the results in the same shape as `cache/osm/ny_rail.json`, `ny_canal.json` and `ny_leads.json`, rerun `lines.py` and `leads.py`, and compare the kilometre totals that `lines.py` prints with the ones in pull request 10. Do the same for any state added from the hosted layers since.
- Historic pockets (November 2026) cover New York, Massachusetts, Vermont, Connecticut, New Hampshire, New Jersey, Pennsylvania. They were made from lists and were not walked: a town centre's score says how much is on record there, not how much is left to see, and it rewards record-keeping as much as old fabric. A town whose main street was never put on the National Register and has few plaques ranks low or is missing altogether (Castleton-on-Hudson, Stillwater, Tivoli and Windham are missing in New York), so absence from the layer says nothing about a town. National Register positions are approximate even after the Wikidata corrections, district outlines are rough boxes from the nomination forms, and some listings no longer stand. A few settlement points in OpenStreetMap are oddities (a "hamlet" called Fort Putnam inside West Point is counted as a small town centre). HMdb.org shows only the first 500 markers of a list without a sign-in, so the counties in the table in section 8 are short and their plaque counts low; Adams County, Pennsylvania (Gettysburg) holds fewer than 500 of 1,533. Marker counts are also only as good as HMdb.org's volunteers have made them. An Android app built before November 16, 2026 still draws the discs from the new data but shows no single markers or listings when zoomed in, and none of the new lists; installing the new app fixes that.
- Missouri (Kansas City) is a first pass: no law note in the app, no state leaf-off or LiDAR, no owner lookup, no rail lines. Pins were checked on Esri satellite only. Old-map crops are cut for every new place except `landmark` ones (section 8).
- The Massachusetts rail layer comes from a state file with unlabeled numeric line types; "abandoned" there is a best reading.
- Drive times to far-eastern places can look long; the Google directions button is the truth.
- GPS smoothing and the field log were tested with simulated location only.
- The Android app's background recorder was compiled and its page logic tested against a stand-in, but nothing here can run it on a real phone. Whether it survives a long walk with the screen off depends on the phone maker's battery rules, and only field use will show it.
- A web page cannot record location with the screen off; that is what the app is for. The website's own field log still needs the page open.
- Photo and video matching was tested with made-up files only. How a given camera app stamps its files (above all videos) can differ by phone maker; if matches look shifted, that is the first thing to check.
- Still to confirm on a real walk: the coarse track-detail setting (a point every 10 m, GPS every 5 s) and kilometres in the recording notification. Vibrate on "Mark here" was confirmed by the owner.
- Marks, walk sharing, the edit sheet and the backup file were tested in a browser against a stand-in; the notification button and the Downloads file have not run on a real phone.
- A shared walk has to be opened from inside the Atlas (Log tab); tapping the file in another app does not open the Atlas yet. Shared walks carry small previews, not the photos themselves.
- Not built yet: historical-markers layer, full-size photos in exports, telling the user a newer app build exists.

## 11. Privacy

The repository and site are public. Do not commit anything personal about the owner or about private landowners: no email addresses, no mailing addresses, no notes exported from someone's browser. The owner lookup deliberately shows owner names from public parcel files but not mailing addresses. `check.py` fails if it finds an email address in the repository.

## 12. The Android app

The app is the same Atlas page inside an Android shell (Capacitor 8), in `android-app/`. It exists for three things a web page cannot do: record a field log with the screen off or the app in the background, open with no signal from the very first launch, and stay installed on the phone.

**What is where**

| Path | Role |
|---|---|
| `source/src/boot.js` | Start-up inside the app. Picks the newest place data on the phone, starts `app.js`, and exposes `window.ATLAS`: data refresh, old maps, calls to the recorder |
| `android-app/scripts/make-www.js` | Copies the built site into `android-app/www/` and makes the page start through `boot.js`. Old maps and `sw.js` are left out |
| `android-app/android/app/src/main/java/com/losthiddenatlas/app/TrackService.java` | The recorder: a foreground service that listens to GPS, smooths fixes, and appends points to a file |
| `.../FieldLogPlugin.java` | What the page can ask the phone to do: `start`, `stop`, `points`, `status`, `remove`, `share`, `battery`, `appSettings`, for photos `media`, `thumb`, `openMedia`; `marks` (pins from the notification), `saveBackup`, and `configure` (the recorder's settings: units, point spacing, GPS interval, vibrate) |
| `.../TrackStore.java`, `MainActivity.java` | The track files (`lat,lon,seconds` per line); the Back button |
| `.github/workflows/app.yml` | Builds, signs and publishes the app |

`android-app/www/`, `node_modules/` and Gradle build folders are generated and not committed.

**Where the app gets places.** The page, `app.js`, the lines and the leads are built into the app, so it always opens. A few seconds after start, and when a connection returns, it reads `version.json` from the Atlas address. If the build number there is newer, it downloads `index.html` (for the `d-sites` block), `data/lines.json` and `data/leads.json`, keeps them on the phone, and offers to reload. Old maps are fetched one at a time from `topo/` the first time a place is opened and kept after that.

**The Atlas address** defaults to the GitHub Pages site (`DEF` in `boot.js`) and can be changed in the app under Guide, "Where the app gets its places". To move the Atlas to another host: copy the whole built site there, make the server send `Access-Control-Allow-Origin: *` (the app's page runs at `https://localhost`, so without that header every fetch is refused), then either type the new address into the app or change `DEF` and release a new build.

**How recording works.** The page calls `start`; the plugin asks for location and notification permission and starts `TrackService`, which records on its own from then on. The page is only a viewer: while visible it asks for `points` it has not seen every few seconds, and catches up in one go when reopened. If Android kills the service, the points already written are safe; when the app is next opened, `resumeLog()` sees "should be recording, is not running" and starts the service again in the same log. Android may also restart the service by itself, which only works if the user chose "Allow all the time" for location.

**Photos and video.** When a log ends (or on "Find photos and video"), the page asks the phone for the photos and videos its camera saved during the log (`media`), and `placeMedia()` in `app.js` files them. Nothing is copied; a log keeps a short reference per item in `l.media`. The rules:

- A photo's place is where the track was at the second it was taken (`trackPos()`), not the camera's own GPS tag.
- A photo joins the next note written within 25 m of that place (photo first, then the note), else the note before it within 25 m; otherwise it stays on the track by itself. Distance, not time, decides, so standing and talking between the photo and the note does not break the match. A choice the user makes by hand (`fx`) survives a rescan.
- A video is a stretch of time, drawn as the part of the track walked while it ran. Its end is the file's last-written time and its start is that minus its length; the "taken" time is the fallback. Each note inside a video shows its position in that video, which is what an editor needs.
- Screenshots and screen recordings are ignored. Photos need the Android "Photos and videos" permission; with "selected photos only", items are missing and the app says so.

**Marks, sharing and backups.**

- The recording notification has a **Mark here** button. The service writes the time and position to `<log>.marks.csv`; the page reads new ones with `marks` alongside the points and turns each into a note called "Mark N", which can be renamed from its card on the map.
- A note's card has Rename, Delete and **Add to the Atlas**, which opens the add-a-place form filled in from the note. The place remembers its note (`from: {log, t}`) and shows that note's photos.
- **Share this walk** packs one log into a `.atlas.json` file (`walkFile()`): track, notes, video stretches and 400-pixel photo previews. **Open a shared walk or GPX file** in the Log tab reads it (`readWalk()`), on the website as well as in the app. Opened logs are marked `imp`; their media carry `x` and are never looked up on the receiving phone, because another phone's photo numbers mean nothing there.
- **Edit sheet** lists, per video, the time inside it of every note and photo.
- When a log ends, the app writes everything to `Download/Lost Hidden Atlas/atlas-backup.json` (`saveBackup`), which survives uninstalling. It is restored through the normal backup restore.

**Building.** Every pull request that touches the app is compiled by the `app` workflow. After a merge it publishes a release with `lost-hidden-atlas.apk`; the newest is always at `https://github.com/mrroot3r/Lost-and-Hidden-Atlas/releases/latest`. Pull requests get a pre-release marked TEST so the owner can install the change before merging. To build locally (Node 22, JDK 21, Android SDK 36):

```
cd android-app && npm ci && node scripts/make-www.js && npx cap sync android
cd android && ./gradlew assembleDebug        # app/build/outputs/apk/debug/app-debug.apk
```

**Signing.** Android only installs an update over an existing app if both are signed with the same key. The key is not in the repository. The workflow reads it from two repository secrets, `ATLAS_KEYSTORE_B64` and `ATLAS_KEYSTORE_PASSWORD`; without them it still compiles the app but does not publish it. Never commit the key or print it in a log. If the key is lost, every user has to uninstall and reinstall, which wipes their notes unless they exported a backup first.

**Testing, and its limits.** `tools/app_smoke.js` runs the app's page in a desktop browser against a stand-in recorder and checks start, a refused permission, catching up after the page was away, recovery after a kill, stop, share, delete and the Back button. It does not run any Java. Nothing in this workflow can install the app on a phone, so permission prompts, the notification, recording with the screen off, and each phone maker's battery rules can only be checked by the owner. Say exactly that in the pull request, and tell the owner what to try. The app's Guide tab has a "Copy app status" button whose output (permissions, GPS fixes received and kept, last error) is the first thing to ask for when a recording goes wrong.

**Keep it small.** No analytics, no accounts, no extra permissions. The app asks for location, notifications (for the recording notice), exemption from battery optimisation, and read access to photos and videos (asked only when the user taps "Find photos and video"), and nothing else.

## 13. Finding places nobody has written up (LiDAR)

Old farm country that the state reforested is full of cellar holes that appear in no article. They can be found from a desk. The method below found the first four `lidar` places in Partridge Run, Berne, in November 2026. It is New York only for now: `tools/lidar_dem.py` reads the state's "Latest_DEM" ground model, and other states need their own elevation service added there.

**What does not work:** scanning LiDAR for pits alone. In the first trial that gave 326 pits in one wildlife area, nearly all tree-throw hollows, stream pockets, or noise under dense conifers, and the best-looking one had no house on any map. **What works:** start from the buildings drawn on an old survey sheet, then look at LiDAR and the aerial at each.

1. **Pick a unit of public land** that was farmland: `python3 tools/lidar_unit.py "Partridge Run"` lists matching units; add the exact name and `save` to write its outline.
2. **Scan it for pits:** `python3 tools/lidar_scan.py research/lidar/unit_X.json research/lidar/x`. About one request per square kilometre; tiles are cached.
3. **Get an old sheet:** `python3 tools/lidar_sheet.py maps <lat> <lon>` lists the historic USGS sheets over a point; `get <url>` downloads one. Use the oldest 1:62,500 sheet (often 1890 to 1905) to find buildings, and a 1940s 1:24,000 sheet to see which were gone by then.
4. **Find the buildings:** `python3 tools/lidar_buildings.py research/lidar/unit_X.json research/lidar/x cache/topo/<old sheet>.tif` lists every building symbol inside the unit and any pit within 90 m.
5. **Look:** `python3 tools/lidar_sheet.py sheet out.jpg 70 <old.tif>,<1940s.tif> "label,lat,lon" …` draws LiDAR, the leaf-off aerial and both maps side by side for each spot. Open the image and judge each row yourself.
6. **Check the parcel for every find:** `python3 tools/parcel.py <lat> <lon>`. This is not optional. Public land is a patchwork with private lots inside and beside it, and an outline simplified to speed up a scan will swallow some of them: the best find of the first trial was reported as state land and turned out to be on a private 60-acre lot.

**What counts as a find.** All four of: a sharp-edged pit, platform or wall on LiDAR; a building at that spot on an old map; nothing standing on the leaf-off aerial (one strong LiDAR pattern in the trial was an occupied house); and a parcel record. Then say how sure you are. Old 15-minute sheets can be 50 to 100 m off, and a pit can be a borrow pit, a spring box or a pond dam.

**Writing it up.** `cat='lidar'`, `st='traces'`, `conf='lead'`, in a `data_*.py` batch like any other place (`data_lidar.py` is the model). The story says only what the maps show. `look` says what the LiDAR and the aerial show and that nobody has checked it on the ground. `accn` gives the parcel result: state land by name, or "PRIVATE LAND" with `acc='ask'`. Never write a private owner's name or address into the repository; the app's owner lookup shows it to the person standing there. The pin note says whether the pin is the pit itself or the old map's symbol.

When the owner visits one and reports back, change `conf`, `st` and `look` to what was found, and move it to the category it really belongs in if it turns out to be more than a cellar hole.

## 14. Reviewing a pull request

Cheaper models add common places in bulk; a stronger model or a person reviews before the owner merges. A review answers one question: is every new entry true, honestly pinned and legal to visit as written?

To ask a Claude session to do it, attach the repository and say: *"Review pull request #N in Lost-and-Hidden-Atlas following GUIDE.md section 14. Do not merge."*

1. Check out the pull request's branch and run `python3 source/tools/review.py . origin/main`. It lists every place added or changed, with its sources, and flags the usual trouble spots. A removed or renamed id is a blocker.
2. Run `python3 source/tools/check.py .`; GitHub's own check must be green too.
3. **Open the sources.** For every new place if there are up to about 20; otherwise for every flagged entry plus a random third of the rest. Read the linked page (`tools/wiki_raw.py` for Wikipedia) and compare each date, name, number and "what remains" claim with it. Wrong, unsupported, or copied sentences get listed by place id.
4. **Look at the pins.** Rebuild the workspace from the branch (`setup.sh`) and run `tools/pincheck.py --batch <key>`. Compare each tile with the pin note. An `exact` pin with no visible structure, or a pin in the wrong town, gets listed.
5. **Check access claims.** `review.py` flags `public` places that the public-land map does not confirm. For New York, `tools/parcel.py` settles it. An entry that tells the reader how to get past a barrier is a blocker.
6. **Report as a comment on the pull request**, not as commits to someone else's branch: a short verdict (ready, ready with fixes, or not ready), then findings by place id with the source line that contradicts the entry, then what you could not check. If asked to fix as well, push fixes as separate commits and say so.
7. Do not merge. The owner merges.

GitHub can also start a review without opening a chat: Anthropic's Claude GitHub app answers a `@claude review` comment on a pull request once it is installed for the repository. That gives a code review; for place data it needs to be pointed at this section.
