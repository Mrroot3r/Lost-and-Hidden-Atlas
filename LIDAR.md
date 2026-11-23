# Finding places on LiDAR: the runbook

This file is everything a model needs to find cellar holes and farm sites that nobody has written up, and add them to the Atlas as leads. It assumes you have read nothing else and remember nothing from earlier sessions. Read it through once before you run anything. `CLAUDE.md` still applies; where this file is more specific, follow this file.

**What you are doing.** New York State bought thousands of worn-out hill farms and let them go back to woods. The houses are gone but the cellars are still holes in the ground, and the state's LiDAR ground model shows them through the trees. The tools scan a unit of public land for cellar-sized pits, keep the pits that lie beside a building drawn on a USGS map from about 1900, and show them to you. **You look at the pictures and decide.** A few in every hundred become a place on the map, marked as an unverified lead for the owner to walk to.

**One command does everything:** `python3 tools/lidar.py`. It keeps a ledger of every unit swept and every candidate with its verdict, in the repository, so each session starts where the last one stopped. It covers New York, Massachusetts, Missouri and Kansas; the sections "Massachusetts" and "Missouri and Kansas" below say what is different there.

## Rules that do not bend

1. **Never merge, never push to `main`.** You finish with one pull request and stop. The owner merges.
2. **Say only what you saw.** Every sentence in a place text comes from a picture you opened in this session or a number the tool printed. If you could not make something out, write that you could not.
3. **A pit is a pit.** Write "pit", not "cellar hole", unless walls show. Every text ends with "Not checked on the ground." Every place is `conf='lead'`.
4. **Private land is never published**, and a private owner's name or address is never written anywhere. The tools do not show you names. Do not go looking for them.
5. **No public record, no place.** `lidar.py check` decides. Do not argue with it.
6. **Do not edit the files in `lidar/units/` by hand**, do not change the scanning tools during a research session, and do not sweep a unit or judge a candidate a second time because you would like a different answer.
7. **Look at every picture the tool tells you to look at.** A verdict you give without opening the picture is a made-up verdict.

## 0. Setup, once a session

```bash
export REPO=/home/claude/lost-and-hidden-atlas ATLAS=/home/claude/atlas   # REPO: the clone this session started with
[ -d $REPO/.git ] || git clone --depth 50 https://github.com/mrroot3r/Lost-and-Hidden-Atlas $REPO
git -C $REPO fetch -q origin main && git -C $REPO checkout -q main && git -C $REPO reset -q --hard origin/main
gh api "repos/mrroot3r/Lost-and-Hidden-Atlas/pulls?state=open" --jq '.[] | [.number,.title] | @tsv'
bash $REPO/source/tools/setup.sh $ATLAS     # prints what is missing; install what it names
cd $ATLAS && bash tools/all.sh              # builds the site once (under a minute)
python3 tools/lidar.py status
```

Every command below is run from `$ATLAS`. A new shell forgets the two variables: set them again.

If the `gh api` line lists an open pull request whose title starts with "LiDAR", an earlier session's work is not merged yet. Tell the owner in your first message and carry on: your ledger will be behind by that session's verdicts, so **sweep new units** and use `next --unit` on them instead of the general `next`.

Open `lidar/examples.jpg` now and look at it once. It shows six candidates that were kept (A to F) and eight that were set aside (G to N), each as the same kind of picture you are about to judge.

## 1. See where things stand

```bash
python3 tools/lidar.py status
```

It prints how many candidates nobody has looked at, anything half finished, and what to do next. Follow its "Next:" lines in order: finish what is unfinished, write up what is marked yes, settle what is marked maybe, and only then start new ground.

## 2. Sweep new ground

Unless the owner named a place, pick units that are old farm country:

```bash
python3 tools/lidar.py near 42.55 -74.45 12        # units within 12 miles of a point, not yet swept
python3 tools/lidar.py find "Burnt-Rossman"        # or by name
python3 tools/lidar.py sweep "Burnt-Rossman Hills State Forest"
```

- **Run `sweep` again and again until it says `DONE`.** By default it works for about 100 seconds and stops cleanly, because a command that runs longer is usually cut off. It says `NOT FINISHED ... Run the same command again`; do exactly that. If your command tool allows a 10-minute limit, add `--minutes 9` and set that limit.
- A scan takes about a minute for every 2,000 acres. Several names can go in one command.
- **Good ground:** state forests and wildlife management areas on hill land between about 1,000 and 2,500 feet. In Burnt-Rossman Hills State Forest eight of the first 23 candidates held up.
- **Poor ground:** city and town parks (their own earthworks), anything under 300 acres, flat valley floors, and the high Adirondacks, where the ground model is coarse and only 5 of the first 94 held up.
- Leave alone names that belong to many places at once ("Memorial Park", "Conservation Area", "New York State Lands", "Unknown Park", "Erie Canal"). `sweep` refuses a name whose pieces lie more than 90 km apart.
- Sweep only units whose access column says OA or RA.
- `find` and `near` list units in New York, Massachusetts, Missouri and Kansas alike; `find "name" --state ma` (or `ny`, `mo`, `ks`) searches one state. `sweep` works out which state a unit is in and says so. A unit in any other state is refused.

### Sweeping on the owner's own computer

The sweep is the half of this work that needs no model: it downloads the ground model, finds pits and walls, and reads the old survey sheets. The owner can run it on his own PC for as long as he likes, at no cost in usage, with `tools/atlas_sweep.py` (November 20, 2026). It is a single file that he keeps in a folder of its own with a `units.txt` (one unit name on each line): each time it starts it fetches the current LiDAR tools and the ledger from GitHub, then calls `lidar.py sweep` on each unit over and over until the tool says DONE. It writes `STATUS.txt` as it goes and `FINISHED.txt` at the end, and it carries on where it stopped. `python atlas_sweep.py near <lat> <lon> <miles>` and `find "<name>"` list units, as `lidar.py` does.

When the owner says a sweep is finished, bring its results in from that folder: copy `work/lidar/units/*.json` and `work/lidar/walls/*.json` out of it, then in the workspace `python3 tools/lidar.py pull <the copied units folder>` and add the wall files to `lidar/walls/` (never over an existing one). Then go on at section 3. It ran on the owner's Windows 10 PC for the first time on November 20, 2026: 15 state forests in 42 minutes, 336 candidates and their walls, brought in the same evening. Two names in that list were refused, Bear Swamp State Forest and South Hill State Forest, because New York has two forests of each name more than 90 km apart and `sweep` has no way yet to say which one is meant (`--state` does not help when both are in New York); that needs a change to `lidar.py`, not a longer `units.txt`. Since the owner sweeps, the sessions only judge: his scheduled task "Atlas LiDAR: judge the swept candidates" has no timetable and runs when he starts it, skips section 2, keeps off any unit an open "LiDAR" pull request touches, and works one unit with `next --unit`. Its pull request does not merge by itself; the maintainer looks at it and merges. Why not through Claude's link to the PC: a command sent that way is cut off after three minutes, nothing keeps running between commands, and the box gets two processor cores.

## 3. Look at the candidates, 36 at a time

```bash
python3 tools/lidar.py next                 # best-ranked first, from every unit
python3 tools/lidar.py next --unit "Burnt"  # or only from units whose name contains this
```

It prints a table and the path of one picture. **Open the picture.** It is a grid of grey shaded-relief chips, six to a row, in table order, each labelled with its id. A chip is 140 m across, north up, lit from the north-west, so a pit is dark on its north-west side and light on its south-east; a mound is the reverse. The pit the scanner found is between the four pink ticks.

Give every chip one of two verdicts:

- **`maybe`** when the pit is sharp-edged and compact, the size of a small room, and above all when something made by people is beside it: straight banks meeting at right angles (field or yard walls), a raised rim, a spoil mound, a second pit, the two parallel banks of an old road. Examples A to F. Be generous here; step 4 is where you get strict.
- **`no`** with one reason word:

| word | when | example |
|---|---|---|
| `faint` | a soft dimple with no edge, or nothing you can see at all | N |
| `water` | on a pond, lake or stream edge, or in a wet hollow | G |
| `road` | in a roadside ditch, a road cut, a parking or turning area | I, J |
| `modern` | square fresh earthworks, a building, a park facility | K |
| `natural` | stream gullies, rock ledges, many pits scattered on rough ground | H, M |
| `coarse` | the ground is drawn in big flat triangles, so the "pit" is an accident of the model | L |
| `dup` | the same site as a candidate or place already dealt with (the table flags these with `<--`) | |
| `other` | anything else; say what in the note | |

Record all 36 in one go. The words after the reason are a note for whoever comes next; write what you saw.

```bash
python3 tools/lidar.py mark - <<'EOF'
brhsf1 maybe sharp pit where two faint old tracks meet
brhsf8 no faint
basf1 no water in a stream ravine
EOF
```

Expect about a third to be `maybe` on good ground and fewer than one in ten on poor ground. If a whole picture is `faint` and `coarse`, that unit is done: move on.

## 4. Settle each maybe on a full sheet

```bash
python3 tools/lidar.py sheet brhsf1 brhsf2 brhsf4 brhsf5
```

It draws pictures of up to three rows and tells you which candidate is on which row. Like `sweep`, it stops when its time is up and prints the command for the rest; so does `check`. **Open each picture.** A row is four panels with pink ticks at the same spot in each:

1. LiDAR, 200 m across.
2. The state's leaf-off aerial photograph, same frame. Its label says which: New York's own, or MassGIS spring 2023 in Massachusetts. A label that says "Esri satellite (leaves may be on)" means the state's aerial did not load: run `sheet` again before you judge "nothing standing".
3. The oldest USGS map (about 1900, 1:62,500), 1,800 m across. A building is a small solid black square or dot, nearly always beside a road (a solid or dashed double line).
4. A USGS map from 1925 to 1965 where one exists. Green is woods, white is open land.

Ask four questions of every row. **All four must be yes.**

1. **Is the shape on LiDAR made by people?** A sharp pit with any of: straight banks, a rim, a mound, an old road. A lone soft hollow is a no.
2. **Does the old map draw a building at the ticks?** Within about 100 m counts; these sheets are that loose. Look hard at what the "building" is. The building finder is fooled by **lettering** (the serif of a letter in a place name), **county and town lines** (long dashes), **bench marks and survey marks** (a cross or triangle with a number), and **the sheet margin**. If the mark at the ticks is one of those, the verdict is `no nomap`.
3. **Is nothing standing there now?** The aerial must show woods, brush or an old field at the ticks. A roof, a mown lawn, a driveway, parked vehicles or a park building is `no modern`. Dense evergreens hide the ground; say so in the text.
4. **Is it away from things that dig pits today?** Ten metres from a paved road, at a pull-off, beside a pond or in a gravel pit is `no road` or `no water`. A pit beside a quiet forest road, on the side where the old map draws the building, can pass: say in the text how close the road is.

```bash
python3 tools/lidar.py mark brhsf3 yes sharp pit 25 m south of the road; two 1898 buildings at the spot, gone on the 1946 sheet
python3 tools/lidar.py mark brhsf12 no coarse the map building is on the sheet lettering
```

Write the note for a `yes` carefully: it is carried into the draft. `mark ... yes` is refused until the sheet has been drawn. If the sheet names something already known within 100 m, it is almost always the same farm: `no dup`.

## 5. Check who owns the ground

```bash
python3 tools/lidar.py check brhsf1 brhsf2 brhsf3
```

For each one it reads the state tax-parcel file, the federal public-land database, the town and county, and the nearest named road, and prints one of:

- **MAY PUBLISH** — the tax parcel is state or other public land.
- **MAY PUBLISH WITH A CAVEAT** — the county publishes no parcel owners (Schoharie, Clinton, Essex, Franklin and Fulton among them), but the public-land database names the unit. The draft writes the caveat.
- **MAY PUBLISH WITH A CAVEAT** (Massachusetts) — the parcel is tax-exempt land that is not government-owned (a land trust, a charity, a school), and the public-land database names it as open. The draft leaves a `TODO` for the owner's own visiting rules: find them on the owner's own page, or leave the place out.
- **DO NOT PUBLISH** — private, or no public record. It prints the `mark` command to run. A sharp, convincing pit that fails only for lack of a record earns one row in `LEADS.md` in the repository clone (what it is, coordinates, why it was not added), with no owner named.

`check` also reads the lots 75 m away in eight directions and prints **`PRIVATE LAND within about 75 m, to the south, south-east`** when one of them is private (where the state file gives owners: all of Massachusetts, some New York counties). A pit on state land can be 40 m from somebody's house lot, and the 200 m sheet does not show a house 130 m off. When you see that line, look at the pin check in step 6 (it shows 300 m), and say in the access text which side of the road or wall is public and that a house stands on the other.

## 6. Write the places

Give each a short name in lower-case words joined by hyphens that says where and what; the nearest road from step 5 is the usual choice:

```bash
python3 tools/lidar.py draft brhsf3:rossman-hill-road-house-site brhsf5:monkey-run-house-site
```

It writes `tools/data_lidar_<date>_<unit>.py` with everything measured already filled in (coordinates, pit size and depth, map year and sheet name, distance to the map building, town, region, the ownership sentence) and the word `TODO` wherever only you can say what the pictures showed. Open the file, look at the sheets again, and replace every `TODO`:

- **name** — plain: "House site south of Rossman Hill Road", "Walled yard and pit on High Knob".
- **years** — `before 1904` means it was there by 1904. Add `–before 1945` only if you saw that the later map no longer draws it.
- **story** (the maps) — what the old map draws beside the building: which side of which road, a lane, a crossroads, a stream. Then what the later map shows at the spot. If you could not make it out, say so.
- **look** (LiDAR and aerial) — the shape in plain words, what is beside it, how far from a road. If it could be something other than a house (a well, a kiln, road works), say so. Then what the aerial shows.
- **hook** — one short line on why it is worth the walk.
- The effort word is `'hike'`; change it to `'walk'` when the pit is within about 100 m of a road a car can use.
- **BATCH label** — "LiDAR finds: " and a few words saying where.

A finished entry reads like this:

```python
N('lidar-rossman-hill-road-house-site','House site south of Rossman Hill Road','Fulton','scho','lidar','traces',42.550295,-74.488698,'exact','public','walk','','before 1898–before 1946',
  'The 1898 USGS survey (Schoharie sheet) draws two buildings here, on the south side of the road where another road joins it; the nearer is about 32 m from the pit. The 1946 survey (Breakabeen sheet) draws both roads as unimproved, the land as woods, and no building here.',
  'On LiDAR: a sharp pit about 8 by 12 m and 1.3 m deep, about 25 m south of a forest road and a little east of where a side road joins it. The leaf-off aerial shows cut-over woods beside an evergreen plantation and nothing standing. Not checked on the ground.',
  'Two buildings on the 1898 map, none on the 1946 one, and a sharp pit between.',
  "No tax-parcel record could be checked: Schoharie County is not in the state's public parcel file. ..."+HUNT,SRC,conf='lead'),
```

Plain words, short sentences, no "nestled", no "hidden gem", no guesses about who lived there. Then check the pins (the old-map crop each place shows in the app is cut by GitHub when it builds the site):

```bash
python3 tools/build_sites.py | tail -1                   # takes the new file into the place list; an error here names the line to fix
python3 tools/pincheck.py --batch lidar_1116_brhsf       # the batch key is in the file; open the picture it writes
```

On the pin-check picture every ring should sit on woods, brush or an old field with nothing built inside it. If a roof or a lawn is in the ring, that place comes out: delete its entry and its pin note from the file and run `python3 tools/lidar.py mark <id> no modern`.

## 7. Build, test, publish, stop

```bash
cd $ATLAS && bash tools/all.sh
(cd dist/web && python3 -m http.server 8766 >/dev/null 2>&1 &) ; sleep 2
node tools/smoke.js http://localhost:8766/index.html lidar-rossman-hill-road-house-site    # one of your new ids
python3 tools/lidar_test.py
python3 tools/lidar.py report > /tmp/report.txt && cat /tmp/report.txt
bash tools/publish.sh $REPO lidar-burnt-rossman-hills        # a NEW branch name of your own; it carries sources only and runs check.py on them
```

If `publish.sh` says **STOP: these files changed in the repository**, somebody else's work was merged while you worked. Run the `resync.sh` line it prints, then `all.sh` and `publish.sh` again. Your new files and verdicts are kept.

`publish.sh` prints a "checks" line that must say `0 errors`. Add any `LEADS.md` rows now, in the clone (`publish.sh` has put it on your branch). Write the commit message to `/tmp/commit.txt`: a first line starting "LiDAR:", then what was swept and added, what you verified and what you could not. Then:

```bash
cd $REPO && git add -A && git commit -F /tmp/commit.txt && git push -u origin lidar-burnt-rossman-hills
gh api repos/mrroot3r/Lost-and-Hidden-Atlas/pulls -f title="LiDAR: Burnt-Rossman Hills, 8 places" -f head=lidar-burnt-rossman-hills -f base=main -F body=@/tmp/report.txt
```

- The pull request title starts with **"LiDAR"**. Its text is the report, plus one paragraph in your own words on anything you could not verify.
- If `git push` is refused, attach the repository to the session with push access and push again (CLAUDE.md). Do not look for another login.
- **A session that found nothing still publishes**: the ledger changed, and the next session needs it. Skip step 6 and `topo_all`; build, publish and open the pull request the same way.
- GitHub builds the site on the pull request to test it, and again after the owner merges to publish it. You do not commit built files.
- **Then stop.** Tell the owner: what was swept, how many were looked at, what was added, and that nothing has been seen on the ground.

**If the owner says a pull request "has conflicts"** (he merged another one first): in a session with a clone, `git checkout` that branch, set the workspace up from it (`bash source/tools/setup.sh`), then `bash tools/resync.sh $REPO $(git -C $REPO merge-base HEAD origin/main)`, build, publish to a new branch name, open a new pull request and ask him to close the old one.

## Stone walls

`sweep` also maps the stone walls of every unit it scans, in the same pass, and the site shows them as the **Stone walls** layer (Map options, "Found on LiDAR"): the walls themselves when zoomed in, shaded squares where they are thick when zoomed out. That shading is the quickest way to see where the farms were, so glance at it before choosing where to look for cellar holes.

- You do nothing extra for a new unit. For a unit swept before walls were looked for, `status` lists it, and this maps it: `python3 tools/lidar.py walls "Unit Name"` (run again until `DONE`, like `sweep`; about 5 seconds a square kilometre tile).
- The walls of a unit are kept in `lidar/walls/<unit>.json` and travel in your pull request like the ledger. The site build turns them into the layer.
- Nobody looks at the walls one by one. They are what a program found: low straight ridges at least 18 m long that stand above the ground on both sides. It was checked by eye on three known walled yards and on made-up ground (`tools/walls_test.py`), and it traces yards, field walls and walled lanes. It also draws some ditch banks, old road edges and stream banks, and it misses walls that are low, tumbled or standing on a terrace edge. The layer says so.
- **The map shows only part of what the finder drew.** On a rough ground model (conifer plantations, the Adirondack fringe, parts of north-west Massachusetts) the finder draws short pieces at random angles: Shaker Mountain Wild Forest came out with 100 km of "wall", nearly all noise. So `tools/walls_structure.py` keeps a piece for the map only if it lies in a straight run of at least 45 m, meets such a run squarely, or is squared off at both ends (a yard); and it drops every box of about 500 m where less than 35% of the drawn length passes. On November 16, 2026 that kept 13,502 of 30,377 pieces: 557 km. The unit files keep everything, so the rule can change without scanning again. A unit where little survives (`python3 tools/walls_structure.py` lists the share kept) has ground too rough for walls, and usually for pits too.
- Do not publish a place because the layer shows walls. Walls say "a farm was here"; the pit beside a map building is still what makes a lead.

## Massachusetts

The method is the same. What differs:

- **Ground model:** the USGS 3DEP service (1 m LiDAR over the whole state), about as fast as New York's. It was compared with MassGIS's own copy on two chips: the same survey, but the state copy is rougher and gave the wall finder false pieces, so 3DEP is used. In the north-west hills the ground model is softer than New York's (blobby under conifers): expect more "faint" verdicts.
- **Old maps:** Massachusetts was surveyed in the 1880s. The first printings (1886) are poor scans with no place names, on which the building finder sees little but road junctions, so the sweep uses the sharpest printing from before 1916 instead and says so (Hawley 1890, Greylock 1898). In Savoy Mountain State Forest that was the difference between 18 map buildings and 161. The sheets can still be 100 m out. A farm given up before the 1880s is on no sheet: a sharp square pit in a walled lot with no map building near it is still worth a "maybe" and a full sheet.
- **Aerial:** MassGIS 2023, leaf-off (flown 21 February to 28 April 2023).
- **Ownership:** every town is in the state parcel file, so `check` nearly always has a parcel to read, and it tells state land (the Commonwealth) from town land from tax-exempt private land.
- **Region:** Franklin, Hampshire, Worcester and Middlesex counties are each split between two Atlas regions, so the draft leaves `TODO: region` naming the two; choose by the town (Hawley and the Connecticut valley towns are `pv`; the Quabbin towns are `cmass`).
- **Sources:** add the managing body's own page for the forest to the batch's source list (the first batch, `tools/data_lidar_1116_kdmsf.py`, shows how) and take hours, parking and rules from it. Massachusetts DCR's rules say to stay on designated trails and roads: say how far off the road each pit is.
- **What the first four units gave (November 2026):** Kenneth Dubuque Memorial State Forest, Hawley: 131 map buildings, 26 pits beside one, 4 published, all in or near the abandoned village of South Hawley, which DCR itself lists; 33 km of stone wall. Catamount State Forest, Colrain: 24 map buildings, 3 pits, none published (one "maybe"). Monroe State Forest: 57 map buildings, 10 pits, given a first verdict from the contact sheet (six "maybe" waiting for full sheets); 20 km of wall. Savoy Mountain State Forest: 161 map buildings, 47 pits, **none looked at yet**; 48 km of wall. The western edge of the Dubuque forest lies on the Greylock sheet and was read from its 1886 printing before the rule above existed; it was not read again.

## Missouri and Kansas

Set up on November 23, 2026 for the country round Kansas City, at the owner's request. The method is the same. What differs:

- **Old maps: up to 1936, and no later.** This country's first surveys are 1:125,000 sheets of the 1890s, too coarse to show a house. The first detailed sheets came between 1910 and 1936, at 1:62,500 (Smithville 1914, Leavenworth 1910, Dearborn 1927), 1:48,000 (Kearney 1936) or 1:24,000 (Blue Springs 1933, Lees Summit 1934). The sweep reads the oldest of those for each spot. The owner's rule: a sheet up to 1936 is old enough; a 1950s sheet is not, because a building on it need not be old. So ground whose first detailed sheet is later than 1936 (Clinton Lake's is 1955, Hillsdale Lake's 1957; on the Kansas side Wyandotte County and the north of Johnson County have sheets from 1934 and 1935, and points tried south of Olathe, at Stilwell and near Tonganoxie had none) gives "0 buildings on the old sheets": that is the rule working, not a fault, and nothing is to be done about it. The comparison sheets still show a later map in their fourth panel where one exists; use it to say how long a building stood, never to accept a candidate the old sheet does not show.
- **How the detailed sheets are read.** A 1:48,000 or 1:24,000 sheet draws roads heavier for the size of a building, and read like a New York sheet the 1936 Kearney sheet gave mostly road junctions, railway ticks and lettering. So on those scales a building must be a solid, nearly square mark with paper round it (`tools/lidar_oldmap.py`). Looked at mark by mark: on Kearney 1936, 23 marks in a 4 km square, nearly all true, with a numeral, a letter and two railway ticks among them; on Blue Springs 1933, 14 marks, every one a true building, with about one true building in three missed (those hard against a lane or a label). Expect a letter or a numeral now and then: on the sheet, look for the black square before believing the pit.
- **Ground model:** the USGS 3DEP service, 1 m, checked on both sides of the state line.
- **Aerial:** Kansas has its own 2024 leaf-off flight. Missouri has none wired in, so the sheets show a satellite picture that may have leaves on: "nothing standing" cannot be read off it under trees, so say so.
- **Ownership:** neither state publishes a tax-parcel file for the whole state. Missouri publishes the parcels the state itself owns: a pit on one comes back `STATE LAND` and may be published plainly (Platte Falls, Weston Bend and Watkins Mill do). Anywhere else, and everywhere in Kansas, `check` says there is no parcel record and the federal public-land record decides: `MAY PUBLISH WITH A CAVEAT`, and the draft writes the caveat. The owner has said that is enough here. `DO NOT PUBLISH` still means what it says.
- **Stone walls:** not looked for. This is hedge and wire country; the wall finder is not run and no wall layer is made.
- **Region:** the Missouri counties round Kansas City go to `kcmo`; Kansas is one region, `ks`. A pit in any other Missouri county leaves `TODO: region`: tell the owner.
- **Which units:** `python3 tools/lidar.py near 39.10 -94.58 40` lists the unswept public land within 40 miles of Kansas City. The good ground is farm country that was bought up whole: the Army Corps lake lands (Smithville, Longview), the state conservation areas, Fleming Park. Leave alone the units whose name belongs to many places at once ("City Park", "Memorial Park", "Unknown Park"): each is hundreds of scattered town parks under one name.
- **Access:** Missouri conservation areas are listed `RA` (open, with seasons and rules): take the hours, the hunting seasons and the parking from the Missouri Department of Conservation's own page for the area, and say in the access line that the area is hunted in season.
- **What the first four units gave (November 23, 2026):** Platte Falls Conservation Area: 135 map buildings, 17 pits beside one, on river bottom where most pits are ditches and levee corners; one farmstead on a lane on the 1910 sheet, still drawn in 1951, is pits and rubble now (`pfca8`, `pfca9`, marked "maybe", ownership checked: state land). Bluffwoods Conservation Area: 51 map buildings, 3 pits; one roadside farm site drawn in 1927 and 1961 is woods now (`bca2`, `bca3`, "maybe"). Watkins Woolen Mill State Park: 7 map buildings, 5 pits, all standing buildings of the historic site or a pond: nothing new, as it should be. Burr Oak Woods Conservation Area: 4 map buildings, 2 pits, not yet judged. In Kansas, Wyandotte County Lake (Wolcott 1934, 1:24,000): 24 map buildings, 5 pits, not yet judged; the sheet shows the farms of the valley before the lake was made, and the two candidates looked at are on mown park ground at the shore. Leavenworth State Fishing Lake: no sheet up to 1936, so nothing. No place has been written from any of them yet.

## Another state

Not a job for a research session: the owner asks for it. A new state needs, in this order:

1. **An entry in `STATES` in `tools/lidar.py`**: its name, a generous box, where the ground model comes from, and, where the state was not surveyed at 1:62,500 before 1915, which old sheets may be read (`oldmap`; the rule and the numbers are in `tools/lidar_oldmap.py`, and "Missouri and Kansas" above says how that was tested). `3dep` works anywhere the USGS has 1 m LiDAR; run `python3 tools/lidar_dem.py <lat> <lon>` on a wooded hill there and read whether it says `fine (1 m LiDAR)` or `coarse`, then look at `research/lidar/test.png`.
2. **Its tax parcels in `tools/parcel.py`**: the state's own parcel service, and a rule that turns an owner and a use code into `STATE LAND`, `public ...`, a tax-exempt kind that is not government, or `PRIVATE`. Read the state's own code table; do not guess what a code means. Never print an owner's name.
3. **Its leaf-off aerial in `tools/ortho.py`**, if the state publishes one. Without it the sheets fall back to a satellite picture with the leaves on, which hides ruins and cannot show "nothing standing" under trees.
4. **Its counties in `REGION` in `tools/lidar.py`**, each to an Atlas region key from `tools/states.py`.
5. Checks in `tools/lidar_test.py` for the parcel rule, then sweep one small unit with known cellar holes and look at every picture before trusting it. In Massachusetts that test caught a pale map scan on which the building finder saw nothing at all.

## How much fits in a session

| step | time | what it costs you |
|---|---|---|
| `sweep` | 1 min per 2,000 acres, plus under a minute for the maps | a few short commands |
| `next` | 25 s | one picture of 36 chips |
| `sheet` | 5 to 20 s a row | one picture per three rows |
| `check` | 4 s each | text |
| build, test, publish | 3 to 5 min | text |

A good session: sweep 10,000 to 20,000 acres, look at two or three pictures of 36, draw sheets for 15 to 30, publish 3 to 10 places. Stop adding ground when you have enough to write up well; unlooked candidates wait in the ledger.

## When something goes wrong

| what you see | what to do |
|---|---|
| `NOT FINISHED` | Run the command it prints (for `sweep`, the same command again). Nothing is lost. |
| `NO SUCH UNIT` | Copy the name exactly from `find` or `near`, capitals included. |
| `NO GROUND MODEL` | The elevation service for that state is down (New York's own in New York, the USGS national one in Massachusetts). Try another unit; try this one later. |
| `SKIPPED ... it lies in VT` | The unit is in a state the tools are not set up for. Pick another unit. "Another state" below says what a new state needs; that is a job for the owner to ask for, not for a research session. |
| `SKIPPED ... pieces with this name lie 300 km apart` | Two places share the name. If one is in the other state, name the state: `sweep "Name" --state ma`. |
| `WARNING ... tiles have no 1 m LiDAR` | The national ground model is coarse over part of the unit, and nothing can be found there. Say so in your report: for that part, "nothing found" is not a finding. |
| `the 1886 ... sheet is a pale scan; using the 1890 printing instead` | Nothing to do. Some old scans print black as grey and the building finder sees nothing on them, so the sharpest printing of the same sheet from before 1916 is used. Use the year it names when you write the place. |
| A chip is solid dark red | The ground model did not load for it. Leave it unmarked; it comes round again. |
| `sheet` says a map could not be fetched | Run it again. The USGS download service has bad minutes. |
| The later map panel is blank or shows a margin | No large-scale sheet from 1925 to 1965 covers the spot. Judge on three panels and write "No later map was looked at." |
| `check` says a service did not answer | Run `check` again for that id. |
| `sweep` says the public-land service did not answer | Run the same command again in a minute. It is not "no such unit": until November 23, 2026 a bad minute of that service was reported as `NO SUCH UNIT`, and two real units near Kansas City were turned away. |
| `status` warns that a published candidate has no place | A draft was thrown away. Run the `mark ... yes` line it prints, then draft again. |
| `check.py` says a text still says TODO | Finish the draft (step 6). |
| A tool crashes with a Python error twice running | Stop. Do not patch the tool mid-session. Publish what the ledger holds and tell the owner what failed, with the error text. |

## For the owner: what to paste

> Read `LIDAR.md` in the repository `mrroot3r/Lost-and-Hidden-Atlas` and do one LiDAR session exactly as it says. Area for this session: **[name a state forest in New York or Massachusetts, or a unit near Kansas City such as "Smithville Recreation Area", or "within 15 miles of Middleburgh", or "whatever status says is next"]**. Open one pull request and stop; do not merge it.

Run one session at a time and merge its pull request before starting the next. If two overlap, the second pull request will say it has conflicts; the paragraph above the table tells a session how to fix that.

## How it works, for whoever changes the tools

- `tools/lidar_unit.py` fetches a unit's outline from PAD-US. `tools/lidar_dem.py` is the ground model: New York's own service in New York, the USGS 3DEP service everywhere else, with a test (`coarse()`) for ground that is not real 1 m LiDAR. A New York tile that hangs over the state line can come back as a picture that cannot be read; it is taken from 3DEP instead, so border units have no holes. `tools/lidar_scan.py` reads that 1 m ground model in 1 km tiles and keeps closed hollows 4 to 16 m across and 0.6 to 3.5 m deep on gentle ground away from streams; what each tile gave is kept, so a scan can stop and resume. `tools/lidar_buildings.py` finds building symbols on the oldest 15-minute USGS sheet. `tools/lidar_sweep.py` pairs pits with buildings within 90 m. `tools/lidar_triage.py` and `tools/lidar_sheet.py` draw the pictures. `tools/parcel.py` (each state's own tax-parcel file) and `tools/pad.py` are the ownership checks. `tools/ortho.py` is the leaf-off aerial for the state a point is in.
- `tools/lidar_walls.py` is the stone-wall finder (its header gives the method and what was tried and dropped), run on each tile by `lidar_scan.py` when `LIDAR_WALLS` is set. `tools/walls_structure.py` decides which pieces go on the map (runs, corners and yards; not scatter). `tools/walls.py` builds the map layer from `lidar/walls/`: an index (`data/walls.json`) with the wall length in every 0.005-degree box, and one file of walls for each 0.05-degree cell. After changing any number in the finder run `python3 tools/walls_test.py` and look at `python3 tools/lidar_walls.py test` on real chips.
- `tools/lidar.py` is the front door and owns the ledger: one file per unit in `lidar/units/` (in the repository as `source/lidar/units/`), one candidate per line, so two sessions' changes merge. Candidate ids are the unit's initials and a number in rank order (`brhsf3`) and never change once a unit is swept. `setup.sh` and `publish.sh` fold the repository's ledger and the workspace's together; neither overwrites the other.
- Rank is depth (capped at 1.5 m) × 1 for a house-sized pit, 0.5 otherwise × 1 within 50 m of the map building, 0.7 beyond.
- After changing `tools/lidar.py` run `python3 tools/lidar_test.py`. `tools/lidar_examples.py` redraws `lidar/examples.jpg`; add a chip when a new kind of false alarm turns up.
- Verdicts are stamped to the second since November 23, 2026 (`stamp()` in `tools/lidar.py`), and when two copies of the ledger are folded together the later one wins. Before that a verdict carried only its date, and of two given on one day the one "further along" won: a session that changed a "maybe" to "no" in the afternoon had it turned back to "maybe" when it published. A LiDAR pull request carries ledger files, so it does not merge by itself: the maintainer or the owner looks at it and merges it.
- Not built: mill races and charcoal hearths as their own detectors, and any state but New York, Massachusetts, Missouri and Kansas ("Another state" below).
