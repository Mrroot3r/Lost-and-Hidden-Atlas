# Finding places on LiDAR: the runbook

This file is everything a model needs to find cellar holes and farm sites that nobody has written up, and add them to the Atlas as leads. It assumes you have read nothing else and remember nothing from earlier sessions. Read it through once before you run anything. `CLAUDE.md` still applies; where this file is more specific, follow this file.

**What you are doing.** New York State bought thousands of worn-out hill farms and let them go back to woods. The houses are gone but the cellars are still holes in the ground, and the state's LiDAR ground model shows them through the trees. The tools scan a unit of public land for cellar-sized pits, keep the pits that lie beside a building drawn on a USGS map from about 1900, and show them to you. **You look at the pictures and decide.** A few in every hundred become a place on the map, marked as an unverified lead for the owner to walk to.

**One command does everything:** `python3 tools/lidar.py`. It keeps a ledger of every unit swept and every candidate with its verdict, in the repository, so each session starts where the last one stopped. New York State only.

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

Unless the owner named a place, pick units near where he explores (he is based near Albany) that are old farm country:

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
2. The state's leaf-off aerial photograph, same frame.
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
- **DO NOT PUBLISH** — private, or no public record. It prints the `mark` command to run. A sharp, convincing pit that fails only for lack of a record earns one row in `LEADS.md` in the repository clone (what it is, coordinates, why it was not added), with no owner named.

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

Plain words, short sentences, no "nestled", no "hidden gem", no guesses about who lived there. Then cut the old-map crops the app shows and check the pins:

```bash
python3 tools/build_sites.py | tail -1                   # takes the new file into the place list; an error here names the line to fix
python3 tools/topo_all.py lidar-rossman-hill-road-house-site lidar-monkey-run-house-site
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
bash tools/publish.sh $REPO lidar-burnt-rossman-hills        # a NEW branch name of your own; it also runs check.py
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
- **Then stop.** Tell the owner: what was swept, how many were looked at, what was added, and that nothing has been seen on the ground.

**If the owner says a pull request "has conflicts"** (he merged another one first): in a session with a clone, `git checkout` that branch, set the workspace up from it (`bash source/tools/setup.sh`), then `bash tools/resync.sh $REPO $(git -C $REPO merge-base HEAD origin/main)`, build, publish to a new branch name, open a new pull request and ask him to close the old one.

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
| `NO GROUND MODEL` | The unit is outside New York, or the state's elevation service is down. Try another unit; try this one later. |
| A chip is solid dark red | The ground model did not load for it. Leave it unmarked; it comes round again. |
| `sheet` says a map could not be fetched | Run it again. The USGS download service has bad minutes. |
| The later map panel is blank or shows a margin | No large-scale sheet from 1925 to 1965 covers the spot. Judge on three panels and write "No later map was looked at." |
| `check` says a service did not answer | Run `check` again for that id. |
| `status` warns that a published candidate has no place | A draft was thrown away. Run the `mark ... yes` line it prints, then draft again. |
| `check.py` says a text still says TODO | Finish the draft (step 6). |
| A tool crashes with a Python error twice running | Stop. Do not patch the tool mid-session. Publish what the ledger holds and tell the owner what failed, with the error text. |

## For the owner: what to paste

> Read `LIDAR.md` in the repository `mrroot3r/Lost-and-Hidden-Atlas` and do one LiDAR session exactly as it says. Area for this session: **[name a state forest, or "within 15 miles of Middleburgh", or "whatever status says is next"]**. Open one pull request and stop; do not merge it.

Run one session at a time and merge its pull request before starting the next. If two overlap, the second pull request will say it has conflicts; the paragraph above the table tells a session how to fix that.

## How it works, for whoever changes the tools

- `tools/lidar_unit.py` fetches a unit's outline from PAD-US. `tools/lidar_scan.py` reads the state's 1 m ground model in 1 km tiles and keeps closed hollows 4 to 16 m across and 0.6 to 3.5 m deep on gentle ground away from streams; what each tile gave is kept, so a scan can stop and resume. `tools/lidar_buildings.py` finds building symbols on the oldest 15-minute USGS sheet. `tools/lidar_sweep.py` pairs pits with buildings within 90 m. `tools/lidar_triage.py` and `tools/lidar_sheet.py` draw the pictures. `tools/parcel.py` and `tools/pad.py` are the ownership checks.
- `tools/lidar.py` is the front door and owns the ledger: one file per unit in `lidar/units/` (in the repository as `source/lidar/units/`), one candidate per line, so two sessions' changes merge. Candidate ids are the unit's initials and a number in rank order (`brhsf3`) and never change once a unit is swept. `setup.sh` and `publish.sh` fold the repository's ledger and the workspace's together; neither overwrites the other.
- Rank is depth (capped at 1.5 m) × 1 for a house-sized pit, 0.5 otherwise × 1 within 50 m of the map building, 0.7 beyond.
- After changing `tools/lidar.py` run `python3 tools/lidar_test.py`. `tools/lidar_examples.py` redraws `lidar/examples.jpg`; add a chip when a new kind of false alarm turns up.
- Not built: stone walls, mill races and charcoal hearths as their own detectors (one wall detector was tried and marked road banks; see GUIDE.md section 10), and any state but New York (each needs its own elevation service in `tools/lidar_dem.py` and its own parcel source).
