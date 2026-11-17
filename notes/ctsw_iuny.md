# ctsw_iuny: New Haven County, Connecticut: canal locks, mills and forts
state: Connecticut
region: ctsw
date: 2026-11-17
places: 16
file: data_ctsw_iuny.py

## What this batch is
First pass over New Haven County (region drawn at random by `choose.py`). 16 places: the two surviving Farmington Canal locks (13 in Hamden, unrestored; 12 in Cheshire, restored), the Hammonasset paper mill and North Madison bog iron works ruins on Madison Land Conservation Trust trails, the New England Cement Company kiln (Woodbridge), the Sleeping Giant quarry crusher ruins and WPA tower, Castle Craig, Fort Nathan Hale/Black Rock Fort, the Fort Wooster earthworks, Five Mile Point Light, Judges Cave, the Henry Whitfield House, the Red Bridge in Meriden, the Diamond Match site at Southford Falls and the Brewster estate at Edgerton Park. Sources: the county Register list (`wiki_raw.py --rows`), Wikipedia articles, Register forms through `page.py` (Lock 13 and Fort Nathan Hale have text layers; the Hammonasset paper mill, cement kiln and Wooster sawmill forms are scans and were not read), and the managers' own pages (CT DEEP for Sleeping Giant, West Rock, Southford Falls and the canal trail; CT DECD for the Whitfield museum; City of Meriden; Madison Land Conservation Trust; Town of Woodbridge trail map and handbook; Sleeping Giant Park Association). Not checked: anything on the ground; hours for Fort Nathan Hale, Fort Wooster, Edgerton Park, the Red Bridge and the cement kiln trail; who owns the strip Lock 13 stands on (the 1982 form named AT&T Long Lines); the Lighthouse Point Park hours and fees come from search-result text because the city's page answered 403. Southford Falls rests on two hiking write-ups and a paywalled news headline and is `conf='mixed'`; where the mill stood was not found. Pins that are not on the thing itself: Southford Falls (area pin on the pond shore), North Madison iron works (an OSM sign post; LiDAR shows the dam embankment), Lock 13 and Lock 12 (the chambers were not picked out on LiDAR), Henry Whitfield House (lawn beside the buildings).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Indigo Woods sawmill dam and sluiceway | Madison, CT (trailhead at the Riverside Terrace cul-de-sac) | Madison Land Conservation Trust page: ruins of a dam, sluiceway and lumber mill on the Neck River, on a trail through a conservation easement on private land | Any date or history for the mill, and a coordinate for the dam |
| Maltby-Stevens Factory Site | Northford, North Branford, CT (on the Farm River) | Wikipedia: button and dried-coconut factory, foundations and water-power remains; demolished about 1935 | Register lists it as address restricted; no public way in found |
| Wooster Sawmill and Gristmill Site | Park Road, Oxford, CT (41.4097, -73.0983) | Wikipedia: mills from 1747 to 1965, breached dam; mill building now a private house | View only at best; Register form is a scan; whether anything shows from Park Road not checked |
| Savin Rock amusement park | West Haven, CT (41.25972, -72.94528) | Wikipedia: seaside resort and amusement park, closed 1966; now a shore path | What, if anything, survives on the ground, and a source for it |
| Stevenson Dam powerhouse | Oxford/Monroe, CT (41.384167, -73.171111) | Register list: 1917 dam, bridge and powerhouse on the Housatonic | Not researched; standing, view from Route 34 |

## Tips
- Connecticut DEEP park pages read well with `page.py --all`; the hours sit in a "Details Open Daily" line that `-g` filters miss, so grep the `--all` text for "Sunset".
- `newhavenct.gov` facility pages answer 403 to `page.py` with no archived copy; search-result text quoting them was the only way to read Lighthouse Point Park's hours and fees.
- The Madison Land Conservation Trust pages and the SCRCOG trail brochures (`scrcog.org/wp-content/uploads/2026/04/<Name>.pdf`) both read cleanly and cover most town and land-trust trails in the county, with parking and ruins marked.
- HMdb marker pages give the marker's position in the cached page as `41.xxxxx,-72.xxxxx' target=_blank>Touch`; that is how the Sleeping Giant crusher was pinned.
- `pincheck.py --lidar` for 16 places took a little over two minutes, longer than the default command timeout: run it in the background.
