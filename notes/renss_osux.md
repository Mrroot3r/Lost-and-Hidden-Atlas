# renss_osux: Rensselaer County: Hoosick, Pittstown, Schaghticoke and Brunswick
state: New York
region: renss
date: 2026-11-18
places: 16
file: data_renss_osux.py

## What this batch is
Sixteen places in northern and eastern Rensselaer County outside Troy (region `renss`, drawn at random by `choose.py --state ny`; it held 13 places, most of them LiDAR leads). Hoosick: Bennington Battlefield State Historic Site at Walloomsac, the Delaney Hotel at North Hoosick, the David Mathews (State Line) House, the Buskirk covered bridge, the Tibbits House at Hoosac School, and in Hoosick Falls the armory, the Estabrook Octagon House, St. Mark's Episcopal Church, the 1925 post office and the downtown historic district. Pittstown: the burned Thompson textile mill at Valley Falls (the one ruin) and the 1845 Tomhannock church. Also the Knickerbocker Mansion (Schaghticoke), the Petersburgh Methodist church, and in Brunswick the Garfield School (historical society) and the District No. 6 "Little Red" schoolhouse. Sources: Wikipedia as raw text (`wiki_raw.py`, and `--rows` for the county Register list), the Tomhannock Register form (text layer), and through `page.py` the NYS Parks Bennington page, the Knickerbocker Historical Society site, the Brunswick Historical Society contact page and a Rensselaer Land Trust news item on the Thompson mill. Every pin was looked at on the leaf-off aerial and LiDAR; five were moved (Knickerbocker, octagon house, Tomhannock church, Petersburgh church, Thompson mill). Red brick was settled from Wikipedia photographs for five places; six stay `'?'`. Not checked: anything on the ground; the Thompson mill's present state and owner (the Land Trust item is undated and spoke of county foreclosure); whether the Delaney Hotel became a bed and breakfast; whether HAYC3 still runs the armory; church service times; post office hours; parking at the Knickerbocker Mansion, the Garfield School and Tomhannock; whether the Tibbits House can be seen from a public road. The downtown district pin is an area pin, the middle of the district.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sampson Station | Grafton, NY (OpenStreetMap ruin, 42.79453, -73.44664) | Mapped as a ruin in OpenStreetMap, 2.9 km north of Grafton | Any source on what it was, and the owner |
| Valley Falls Historic District | Valley Falls, NY (42.8992, -73.5613) | Register list: properties in the core of the mill village date to the 1830s; no Wikipedia article | A source on which buildings stand; would sit beside the Thompson mill entry |
| Sand Lake Baptist Church | Averill Park, NY (42.63528, -73.54972) | Wikipedia: 1805 Federal frame church, 1840 Greek Revival tower, Palladian window, 1846 parsonage | Church page for services, interior; pin check |
| Muitzes Kill and Schodack Landing historic districts | Schodack, NY (42.4764, -73.7228 and 42.4828, -73.7686) | On the Register list (1974, 1977) | Articles were not read; what stands and what can be seen from the road |
| Hoosick Township Historical Society (Louis Miller Museum) | 166 Main Street, Hoosick Falls, NY | Address from the society's site footer | hoosickhistory.com reset the connection to `page.py`; hours and what the building is |

## Tips
- `brick.py look` worked on new places once `build_sites.py` had run, before publishing, so new places can be settled with it too; Wikimedia refused the sixth picture in a row (429) twice, a minute apart.
- `places_test.js` on main fails on `onesquethaw-valley` (years "18th century") in "Standing, from before 1800", besides the `zion-cemetery-baynard-mausoleum` case other notes give; this batch changes nothing it reads.
- `publish.sh` stopped because another batch (`data_mes_vpdi.py`) merged while this one was being written; `resync.sh` then a fresh batch time and rebuild fixed it in about five minutes.
- hoosickhistory.com: `page.py` reads `places-%26-spaces` but the home page resets the connection.
