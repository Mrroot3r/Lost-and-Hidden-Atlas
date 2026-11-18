# nhw_cbfa: Southern Grafton County, NH: Livermore Falls mill ruins, Old Hill Village, Shakers and meeting houses
state: New Hampshire
region: nhl, nhw
date: 2026-11-18
places: 17
file: data_nhw_cbfa.py

## What this batch is
Second pass at region `nhw` (drawn at random by `choose.py`), on southern and western Grafton County, which had nothing on the map within 30 km of Plymouth: 17 places. Ruins and traces: the Livermore Falls pulp mill foundations and the closed 1885/1886 lenticular "Pumpkinseed" bridge (state forest), Old Hill Village (the village Hill abandoned for the Franklin Falls flood dam in 1941; Army Corps land, in Merrimack County, so `reg='nhl'`), and the 1875 bridge pier beside the 1928 Piermont truss. Standing: Enfield Shaker Village, the Lyme horse sheds (27 stalls, 1810–14), the Ridge at Orford, Trinity Church in Holderness (1797), the 1774 Old Grafton County Courthouse, Blair covered bridge, Ashland's gristmill, railroad station and Whipple House, Canaan Street, the Enfield Center and Dorchester meeting houses, and stone arch bridges in Hanover and Lebanon. Sources read in this session: Wikipedia with `wiki_raw.py` (the Grafton Register list with `--rows`), the state's 2015 Livermore Falls Cultural Landscape Report (PDF, read in full with `page.py -n 200000 --all`), the Lyme Common Register nomination, NH State Parks, the Enfield Shaker Museum, HMdb, the Concord Monitor and the Weirs Times through `page.py`. Not checked: anything on the ground; most interiors; hours for the Plymouth courthouse museum, Whipple House, Canaan museum, the churches and Old Hill Village (the Army Corps page answered 403); Ashland station hours are from a 2020 article. Old Hill Village's remains (cellar holes, sidewalks, steps) rest on ghosttowns.com, a reader-written page, plus what the LiDAR shows; set `conf='mixed'`. Livermore Falls bridge date: the state says 1885, the Concord Monitor 1886; both given. Ashland station's address is 39 Depot Street (Wikipedia) or 69 (Weirs Times). Pins: Livermore Falls and Old Hill are `area` (on the gorge rim and in the woods of the old village); the Orford pin is on the Congregational church, not the Ridge houses; Enfield Shaker is on the building group, not a confirmed Great Stone Dwelling; Courthouse, Ashland mill and station are `site`. Brick is `?` for Old Hill, Enfield Shaker, Lyme, Orford and the Whipple House (Wikipedia says brick but no colour, and no picture was opened); `some` for Livermore Falls (the 2015 report names brickwork in the mill ruin).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| B-18 bomber crash site, Mount Waternomee | Woodstock, NH | 1942 crash; a memorial and protected heritage site on the White Mountain National Forest (HMdb, "The Night the Bomber Crashed") | A wreck rather than a building; trail and position if wanted |
| Livermore Falls fish hatchery site | Holderness/Campton, NH (south end of the Hollow) | First state fish hatchery, 1877; hatch house burned (2015 Cultural Landscape Report) | Whether anything is visible; the report places it only roughly |
| Canaan Union Academy (Canaan Historical Museum) | Canaan, NH | 1839 academy, now the town museum (Wikipedia, Canaan Street HD) | Opening times; folded into the Canaan Street entry for now |
| Mary Baker Eddy house, Rumney | Rumney, NH | Not researched | Any source |
| Ruggles Mine | Grafton, NH | Old mica and feldspar mine, a tourist attraction in the past (memory only) | A source for its present state and access |

## Tips
- `page.py --all` stops at about 12,000 characters; add `-n 200000` to get a whole long PDF (the Livermore Falls report is 126,000 characters).
- `parking.py` near Blair Bridge returned a "lot" that is the road at the bridge end; check every lot on the aerial.
- The Army Corps New England District pages (`nae.usace.army.mil`) answer 403 to `page.py`; the Corps Lakes Gateway page (`corpslakes.erdc.dren.mil/visitors/projects.cfm?ID=...`) reads and lists a project's recreation areas.
- Register list coordinates in this county fell in rivers twice (Piermont, Blair) and in a private yard once (Orford district); look at every one.
- `gh api .../pulls` printed nothing again; `start.py` showed 0 open pull requests.
