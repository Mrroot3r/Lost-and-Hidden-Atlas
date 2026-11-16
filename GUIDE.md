# Working on the Lost & Hidden Atlas

This is the handoff guide. It tells a new contributor, human or AI model, what the Atlas is, how it is built, and how to add places without lowering its quality. Read it before changing anything.

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
| `index.html` | Page, styles, and two inline JSON blocks: `d-sites` (places, start cities, guide text) and `d-base` (outline map used only if tiles cannot load) |
| `app.js` | The whole app: one plain-JavaScript file, no framework, Leaflet for the map |
| `sw.js` | Service worker: page is fetched fresh when online, served from cache when not; versioned files and `topo/` images are cached once |
| `data/lines.json` | Old rail, trolley and canal lines; fetched after load |
| `data/leads.json` | Unchecked leads from OpenStreetMap; fetched when the Leads layer is turned on |
| `topo/<place-id>.webp` | One cropped old USGS map per place; fetched when the place is opened |
| `source/` | Everything the site is generated from |

**Never edit the files in the repository root by hand.** They are build output. Edit `source/` and rebuild.

Map layers come from public services, chosen per state by `regionOf()` in `app.js`:

- Streets and satellite: Esri. Current and old topo: USGS and Esri.
- Leaf-off aerial and LiDAR: New York (NYS ITS, slow export services, heavily cached), Massachusetts (MassGIS tiles), Vermont (VCGI tiles), Rhode Island (RIGIS image services at `maps.edc.uri.edu/rigis`: the March 2026 3-inch flight, and the 2022 LiDAR elevation service shaded on request the same way as New York's, so the light direction setting works there too). Other states fall back to Esri satellite and world hillshade.
- Public land: USGS PAD-US. Owner lookup and lot lines: NYS tax parcels (only some counties share owner names), NYS DEC, MassGIS parcels (statewide).
- Drive times: OSRM, precomputed at build time from the start cities in `tools/drive.py`.

## 3. Building and publishing

```bash
git clone --depth 1 https://github.com/mrroot3r/lost-and-hidden-atlas repo
bash repo/source/tools/setup.sh /path/to/work     # builds a working folder from the clone
export ATLAS=/path/to/work
bash $ATLAS/tools/all.sh                          # rebuilds everything into $ATLAS/dist/web
(cd $ATLAS/dist && python3 -m http.server 8766) & # serve it
node $ATLAS/tools/smoke.js http://localhost:8766/web/   # phone-size smoke test, needs Playwright
bash $ATLAS/tools/publish.sh repo                 # copies the build and sources into the clone and stages them
```

Then review `git status`, commit, and push to `main`. GitHub Pages redeploys in about a minute. Check that `sw.js` on the live site shows the new version string.

Needs Python 3 with `requests`, plus `rasterio` and `Pillow` for old-map crops, and Node with Playwright for tests.

What `all.sh` runs, in order: `build_sites.py` (merge place lists) → `drive.py` (drive times) → `padus.py` (public-land status per pin) → `leads.py` → `make.py` (assemble the site) → `export.py` (CSV and KML).

Not part of `all.sh`, run only when needed:

- `python3 tools/topo_all.py <id> <id> …` cuts old-map crops for new places. It downloads large USGS scans, so run it only for new ids.
- `tools/lines.py` rebuilds the rail and canal lines. It needs raw downloads that are not in the repository. Run it only when adding a region.
- `tools/osm_leads.py`, `tools/osm_worc.py` download leads. The Overpass servers fail often; the scripts rotate mirrors. Split big areas into small boxes.

## 4. The place record

Places are Python calls to `N(...)` in `source/tools/data_*.py` (`data_c.py`, `data_ma.py` and `data_worc.py` are the cleanest examples). `data_a.py` is the original catalogue and has an older shape; leave it alone.

```python
N(id, name, town, reg, cat, st, lat, lon, prec, acc, eff, tags, years,
  story, look='', hook='', accn='', links=None, conf=None, th=None, thn=None)
```

| Field | Meaning and allowed values |
|---|---|
| `id` | Unique lowercase slug with hyphens. Never rename one: saved notes are keyed to it |
| `reg` | Region code from `REG` in `app.js` (for example `worc`, `pv`, `berk`, `adk`, `cat`). A new region needs a new entry there |
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
| `conf` | Leave empty when sourced. `'mixed'` when the outline is sourced but some details are not. `'lead'` when the entry is unverified |
| `th`, `thn` | Parking or trailhead `[lat, lon]` and its name, when the pin is not where you park |

Each data file also has a pin-note dictionary (`PNC`, `PNM`, `PNX`) mapping id to one sentence on **where the coordinate came from**. Every new place needs one.

To add a batch: create `data_<area>.py`, then import it in `build_sites.py` the way `data_worc.py` is imported.

## 5. Research rules

These are what keep the Atlas trustworthy. They are not optional.

1. **Every fact needs a source you actually read.** Dates, names, numbers and "what remains" claims come from the linked source. If you cannot source a detail, leave it out or write "not confirmed" in the text and set `conf`.
2. **Do not fill gaps from memory.** A model's recollection of a place is a lead to check, never a fact to publish. This matters most for what survives on the ground, which changes.
3. **Be honest about the pin.** Coordinates from a Wikipedia infobox, an OpenStreetMap feature, an address lookup or a trail log are each fine if the pin note says so. If the coordinate marks a town, a road or a park entrance and not the ruin, say that and use `prec='area'`. Never invent or nudge a coordinate.
4. **Say what is left, not what was there.** A demolished site is `gone`, however famous. Check for recent demolition, fire or redevelopment.
5. **Access is part of the entry.** Name the owner or manager when known. Private or unknown means `ask` or `view`. Active railroads, mines, tunnels and sealed buildings get a plain warning. Never describe a way in.
6. **Write plainly.** Short sentences, no hype, no filler. Put the facts in your own words; do not copy source sentences.
7. **Prefer places with something to find.** Ruins and traces first, then standing landmarks with a story, then vanished sites that matter to a series.
8. **Stay inside what the user can reach.** Their base is Albany, New York; a second base is Worcester, Massachusetts.

Sources that have worked: Wikipedia and National Register listings (facts and coordinates), state park and land-trust pages (access, trail maps), OpenStreetMap `historic=ruins` and related tags (leads and coordinates), town historical societies, the ArcGIS geocoder (`findAddressCandidates`) for addresses and named places. Wikipedia rate-limits hard: batch titles (`tools/wiki_ma.py`, `tools/wiki_wt.py`), pause between calls, send a real User-Agent, cache to disk. From a shared cloud address the API answers 429 for minutes at a time even at that pace; fetching one article at a time as raw wikitext (`index.php?title=…&action=raw`), a few seconds apart, got through when the API did not. Before trusting a pin, pull a 300 m square of the state leaf-off aerial around it: that caught a Wikipedia coordinate that lands on the shoreline beside a fort instead of on it.

## 6. Handing research to a cheaper model

Give it this guide's sections 4 and 5 and a prompt like the one below. Have a stronger model, or a person, spot-check a sample before publishing.

```
You are adding places to the Lost & Hidden Atlas, a map of ruins and lost
buildings. Area: <county or region>. Find <N> candidate places that have
ruins, traces or a standing landmark with a story.

For each place, read at least one source and return one Python N(...) call
in the format below, plus one pin-note line. Rules:
- Use only facts stated in a source you opened. Link every source.
- If you cannot confirm what remains today, say "Not confirmed" in `look`
  and set conf='mixed' or conf='lead'.
- Give the coordinate's origin in the pin note. If it marks a town, road or
  park and not the site itself, say so and use prec='area'.
- State who owns or manages the land if a source says. Otherwise acc='ask'
  or 'view'. Never describe how to get into a building or past a fence.
- Plain short sentences in your own words. No hype.
- Skip a place rather than guess.

<paste the field table from section 4 and one example entry>

Finish with a list of anything you could not verify.
```

Then, for the batch: add the file, hook it into `build_sites.py`, run `build_sites.py` to catch duplicate ids, run `topo_all.py` for the new ids, run `all.sh`, run the smoke test, open a few of the new places and compare each pin with the leaf-off aerial and LiDAR.

## 7. Adding a new state or region

1. Add region codes to `REG` in `app.js`.
2. Extend `regionOf()` and its border tables so tiles pick the right state. Test with known cities on both sides of each border.
3. Add that state's leaf-off and LiDAR tile services to `leafUrl()` and `lidarUrl()` if it publishes them. Check they send CORS headers and note their deepest zoom.
4. Widen `maxBounds` in `initMap()`, the box in `lines.py`, and the box in `basegeo.py`.
5. Add old rail and canal lines for the area and rebuild `lines.json`.
6. Add a parcel-owner lookup if the state publishes one (`lookup()` in `app.js`).
7. Consider a new start city in `drive.py`.
8. Update the legal notes in the in-app Guide: trespass law differs by state.

## 8. Changing the app

- `app.js` is one file with sections marked by comments. State is the object `U`; `save()` persists it. Add new saved fields to `U0()` so old backups still load.
- The phone layout is the main one: a scrolling icon bar under the map, an options sheet with a fixed Done button, four tabs (Places, Trip, Log, Guide). Keep touch targets large. Test at phone size first.
- The app must still work when a data file fails to load or the phone is offline. Show a short message; never a blank screen.
- Bump nothing by hand: `make.py` stamps a version into `index.html`, the script URL and `sw.js` on every build.
- The app also builds as a single self-contained file (`dist/Lost-and-Hidden-Atlas.html`). It detects that mode by the presence of an inline `d-topo` block.

## 9. Known gaps

- Most pins added in November 2026 were not checked against imagery. Their pin notes say so.
- Leads are missing for greater Boston, the South Shore and Cape Cod.
- The Massachusetts rail layer comes from a state file with unlabeled numeric line types; "abandoned" there is a best reading.
- Drive times to far-eastern places can look long; the Google directions button is the truth.
- GPS smoothing and the field log were tested with simulated location only.
- A web page cannot record location with the screen off. An Android app wrapper with background location is planned.
- Rhode Island is a first pass: 28 places in `data_ri.py`, each pin looked at once on the state leaf-off aerial but none walked. Not done there: owner lookup and lot lines (the state has a tax-parcel map service at `risegis.ri.gov`; whether it carries owner names was not checked), leads (Overpass could not be reached), and a rebuild of the rail and canal lines.
- Rhode Island leads read about but not added, for want of a source or a coordinate: Ramtail Factory (Foster), Hunt's Mills (East Providence), Enchanted Forest (Hope Valley, 1971–2005), Whale Rock Light foundation, Warren powerhouse ruins, Windswept ruins (Narragansett), Stillwater mill (Smithfield).
- Not built yet: historical-markers layer, photo notes, GPX import.

## 10. Privacy

The repository and site are public. Do not commit anything personal about the owner or about private landowners: no email addresses, no mailing addresses, no notes exported from someone's browser. The owner lookup deliberately shows owner names from public parcel files but not mailing addresses.
