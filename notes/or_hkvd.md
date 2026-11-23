# or_hkvd: Oregon, a second scatter
state: Oregon
region: or
date: 2026-11-23
places: 10
file: data_or_hkvd.py

## What this batch is
Ten places in ten Oregon counties, claimed with `choose.py --thinnest` (Oregon had 37 places): Fort Stevens and Battery Russell (Clatsop), Umpqua River Lighthouse (Douglas), Cape Blanco Lighthouse (Curry), Hangar B at Tillamook, Oregon Caves Chateau (Josephine, closed), Crater Lake Lodge (Klamath), Timberline Lodge (Clackamas), Pittock Mansion (Multnomah), the Chambers covered railroad bridge (Lane) and the Butteville Store (Marion). Read with `wiki_raw.py`, `page.py` on Oregon State Parks, NPS, Umpqua Valley Museums, Pittock Mansion and Tillamook Air Museum pages, and web-search snippets. Not checked: the BLM Cape Blanco page (403) and Timberline's own pages (404 or unread), so Cape Blanco and Timberline hours are `?`; Tillamook and Butteville pages gave no hours; nothing was checked on the ground. Sources disagree on the Umpqua tower's date (1890 museum, 1892 to 1894 Wikipedia), the Chambers bridge date (1925, or 1936 on a 1976 form) and the Chateau's bark (redwood or Port Orford cedar). Pittock Mansion's pin sits under leaf-on trees on the aerial and rests on OpenStreetMap's building point.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Yamhill blockhouse | Dayton, OR (45.2187, -123.0640 approx.) | Wikipedia and the Oregon Encyclopedia: the 1856 fort's blockhouse stands in Dayton's Courthouse Square Park; the fort site is a state heritage area | A source opened for the blockhouse's present state and pin |
| Pendleton old centre | Pendleton, OR (45.6718, -118.7866) | `start.py` lists it as an old town centre with 13 listed places and none on the Atlas | Nothing read yet |
| Elgin Opera House | Elgin, OR (45.56575, -117.91772) | Wikipedia stub: on the Register as Elgin City Hall and Opera House | Any source beyond the stub |

## Tips
- Wikipedia's coordinates were off in four of ten places here (Timberline, Pittock, Chambers bridge, Butteville): `osmnear.py ... buildings -g '<name>'` and `geo.py` fixed each.
- `nps.gov/places/<name>.htm` worked for Crater Lake Lodge but 404'd for the Chateau, whose page is `nps.gov/orca/learn/historyculture/chateau.htm`: search with `allowed_domains` nps.gov for the real address.
