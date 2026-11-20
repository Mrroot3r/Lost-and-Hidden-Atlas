# nv_clty: Nevada: forts, camps and courthouses across the state
state: Nevada
region: nv
date: 2026-11-20
places: 18
file: data_nv_clty.py

## What this batch is
A first scatter of 18 places across Nevada, which had only Rhyolite: Fort Churchill and Buckland Station on the Carson River; Piper's Opera House and the Fourth Ward School in Virginia City; Berlin, the Belmont Courthouse, Tonopah's mining park and the Mizpah Hotel in Nye County; Stokes Castle (Austin), the Eureka Opera House, the Ward charcoal ovens and the East Ely railway yards on and off U.S. 50; the Million Dollar Courthouse and Delamar in Lincoln County; the Goldfield Hotel; the Pershing County Courthouse in Lovelock; and the Old Las Vegas Mormon Fort and drowned St. Thomas in Clark County. Facts from Wikipedia (`wiki_raw.py`), Nevada State Parks pages (`page.py` reads parks.nv.gov well: hours, fees, rules), the NPS St. Thomas trail page, the Nevada SHPO marker page for Stokes Castle, the museums' own pages (fourthwardschool.org, elyrailroadmuseum.org, tonopahminingpark.com, mizpahhotel.net) and a BLM announcement on Delamar. Where the runner's own page would not open, Travel Nevada (state tourism) was read, its hours put in the access note, and `hours='?'`: Piper's Opera House, Eureka Opera House (Eureka County's page answered 403), Million Dollar Courthouse, Belmont Courthouse (tours by appointment with its Friends). No National Register forms were read. Not checked: anything on the ground; parking for the town buildings; who owns the Delamar townsite (marked view; the federal land map puts the Wikipedia coordinate on BLM land) and where its ruins are (pin is the general area); whether Stokes Castle opens inside; which parts of the Mormon Fort walls are original; which building in the East Ely yard is the depot (pin is the Wikipedia point). The St. Thomas trailhead point is the end of a track on the aerial, not a marked lot. Red brick: only the Goldfield Hotel is 'yes' (Wikipedia: red brick above a granite ground floor); the Mizpah and Pershing courthouse are brick of an unknown colour ('?').

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hamilton (Treasure Hill) | White Pine County, NV (39.25306, -115.485) | Silver boomtown of 1868–69, first county seat; "only scattered ruins remaining" (Wikipedia: Hamilton, Nevada) | What stands, road and land owner |
| Fort Ruby | Ruby Valley, NV (40.06778, -115.52944) | Army post 1862–1869, NHL 1961; two of four log buildings burned 1992; federal since 2002 (Wikipedia) | Which agency, what is left, legal access |
| Tuscarora | Elko County, NV (41.31417, -116.22167) | Mining town from 1867 with a large Chinese placer community (Wikipedia) | What survives and who owns it |
| Unionville | Pershing County, NV (40.44583, -118.12222) | First Humboldt County seat 1861–1873; Mark Twain prospected here 1862 (Wikipedia) | What old buildings stand, owners |
| Belmont mills and Cosmopolitan Saloon | Belmont, NV (near 38.596, -116.876) | Monitor-Belmont Mill chimney and the saloon still stand (Wikipedia; Travel Nevada) | Pins and owners for each |
| Nelson / Techatticup Mine | Eldorado Canyon, NV (35.70722, -114.82611) | Gold camp from about 1861 (Wikipedia) | What is open to visitors, owner's page |
| Esmeralda County Courthouse | Goldfield, NV (37.70861, -117.23417) | 1907, still the county courthouse (Wikipedia) | Anything on its fabric or visiting |

## Tips
- parks.nv.gov park pages read in full with `page.py`; the hours and fees are in the "Park Detail" block (`--all` and grep "Hours").
- travelnevada.com pages read with `page.py` and often give hours and fees where the runner's site fails; several of its old addresses (`/ghost-town/belmont/`) answer 404, so use the address a web search returns.
- nnry.com (Nevada Northern Railway) and eurekacountynv.gov answer 403 to `page.py`; elyrailroadmuseum.org gives the depot museum's hours.
- shpo.nv.gov marker pages (`/nevadas-historical-markers/historical-markers/<slug>`) read cleanly and give each state marker's text.
- In Nevada the pin check has no 1 m LiDAR for several rural pins (Austin, Eureka, Ward, Pioche, Delamar); the aerial is the only check there.
- Web searches in this session returned titles and links only, no quoted text.
