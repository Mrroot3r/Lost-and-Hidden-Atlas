# Working on the Lost & Hidden Atlas

This is the handoff guide. It tells a new contributor, human or AI model, what the Atlas is, how it is built, how to add places without lowering its quality, and how a change gets published. Read it before changing anything.

## 1. What the Atlas is

A phone-first map tool for finding lost buildings, ruins and abandoned sites, made for a YouTube creator who explores them on foot. It began around Albany, New York and now covers upstate New York and Massachusetts, with a first pass at Rhode Island. The plan is to grow across the Northeast.

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
- `tools/lines.py` rebuilds the rail and canal lines. It needs raw downloads that are not in the repository. Run it only when adding a region.
- `tools/osm_leads.py`, `tools/osm_worc.py` download leads from Overpass.

### What a cloud session usually cannot reach

Check these once and move on; do not spend time retrying.

| Service | What happens | Do instead |
|---|---|---|
| Wikipedia search and query API | HTTP 429 for minutes at a time, even batched and paced | `tools/wiki_raw.py`, which reads one article at a time as raw text |
| Overpass (OpenStreetMap queries) | Blocked or timing out on most mirrors | Skip leads for now and record it in section 10; try small boxes on the `maps.mail.ru` mirror |
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
| `cat` | `amuse` `hotel` `canal` `rail` `industry` `burial` `town` `civic` `fort` `water` `inst` `light` `landmark` |
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
2. **Read each article:** `python3 tools/wiki_raw.py "Exact title" …` prints its coordinates and opening text; add `-g 'closed|demol|remain|ruin'` to pull only the sentences about what happened and what is left. Other sources that have worked: state park and land-trust pages (access, trail maps), National Park Service pages, town historical societies, the ArcGIS geocoder (`findAddressCandidates`) for addresses and named places.
3. **Write the entries** in a new `data_<area>.py` with its `BATCH`, `PLACES` and `PIN_NOTES`.
4. **Build the list:** `python3 tools/build_sites.py`. It stops on a duplicate id or a missing pin note.
5. **Check every pin:** `python3 tools/pincheck.py --batch <key>` writes contact sheets to `research/`: one 300 m aerial square per pin with a 30 m ring. Look at every tile. Fix what you can see, downgrade what you cannot, and record in the pin note what the aerial showed.
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

The base is already in place for all nine Northeast states: New York, Massachusetts, Rhode Island, Vermont, Connecticut, New Hampshire, Maine, New Jersey and Pennsylvania. For each, `tools/states.py` lists its regions and start cities (the capital and the main cities), the map covers it, state detection works, and satellite imagery and a world hillshade load as a fallback. **To start work in any of them, you only add a batch of places** (section 6) using that state's region codes.

| State | Places so far | Leaf-off and LiDAR | Owner lookup | Law note in the app |
|---|---|---|---|---|
| New York | Capital Region outward; none yet in NYC, central, western or northern regions | State services | Some counties | Yes |
| Massachusetts | Statewide first pass, Worcester County deeper | State services | Statewide | Yes |
| Rhode Island | First pass | State services | No | Yes |
| Vermont | A few in the south | State services | No | No |
| Connecticut | Two in the northwest | Fallback only | No | No |
| New Hampshire, Maine, New Jersey, Pennsylvania | None | Fallback only | No | No |

Beyond adding places, these make a state better. Do them when asked, or note in section 10 that they are still open.

| Step | When | What to do |
|---|---|---|
| Law note | With the first batch for a state | Add the state's trespass basics to the in-app Guide and set `legal` to `True` in `states.py`. Read the statute; do not paraphrase from memory |
| State imagery | When the state publishes it | Add its leaf-off and LiDAR services to `leafUrl()` and `lidarUrl()`. Check they send CORS headers, note their deepest zoom, and look at a tile over open water (some services return black there). Then test with `node tools/smoke.js <url> <place-id>` |
| Rail and canal lines | Can wait | Widen the box in `lines.py`, add the state's old lines, rebuild `lines.json` |
| Leads | Can wait | Overpass download for the state |
| Owner lookup and lot lines | Can wait | Add to `lookup()` and `drawLots()` if the state publishes parcels with owner names |
| A new region or start city | When a state's regions are too coarse | Add it in `states.py`. Do not rename a region code that published places use |

A state outside these nine also needs its outline added to `source/build/states.json`, an entry in `states.py`, and wider `maxBounds` in `initMap()`.

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
- Vermont, Connecticut, New Hampshire, Maine, New Jersey and Pennsylvania have the base only: regions, start cities and fallback imagery. They have no law note in the app, and the last four have no places.
- Rhode Island is a first pass: no owner lookup or lot lines (the state has a tax-parcel map service at `risegis.ri.gov`; whether it carries owner names was not checked), no leads, no rebuilt rail and canal lines.
- The Rhode Island LiDAR service returns black or blank tiles over open water.
- Leads are missing for greater Boston, the South Shore, Cape Cod and Rhode Island.
- The Massachusetts rail layer comes from a state file with unlabeled numeric line types; "abandoned" there is a best reading.
- Drive times to far-eastern places can look long; the Google directions button is the truth.
- GPS smoothing and the field log were tested with simulated location only.
- The Android app's background recorder was compiled and its page logic tested against a stand-in, but nothing here can run it on a real phone. Whether it survives a long walk with the screen off depends on the phone maker's battery rules, and only field use will show it.
- A web page cannot record location with the screen off; that is what the app is for. The website's own field log still needs the page open.
- Photo and video matching was tested with made-up files only. How a given camera app stamps its files (above all videos) can differ by phone maker; if matches look shifted, that is the first thing to check.
- The recorder's settings (track detail, vibrate on mark, units in the notification) compile but have not run on a real phone.
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

