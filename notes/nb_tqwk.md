# nb_tqwk: New Brunswick: a first scatter
state: New Brunswick
region: nb
date: 2026-11-19
places: 19
file: data_nb_tqwk.py

## What this batch is
Nineteen places spread across New Brunswick, the province's first real batch (Fort Beauséjour was the only place before). North and west: the Petit-Sault blockhouse (Edmundston, a 2001 reconstruction on the 1841 site), the Hartland Covered Bridge, the McAdam CPR station-hotel, Kings Landing. Fredericton: the Marysville cotton mill, Old Government House, Christ Church Cathedral. Centre and south: the Reid's Mill smokestack at Gagetown (the one ruin of a sawmill), Loyalist House and Carleton Martello Tower in Saint John, the Seal Cove smoked-herring stands on Grand Manan, the St. Andrews Blockhouse, Ministers Island (Van Horne's estate, reached across the sea floor at low tide). Southeast: Monument-Lefebvre at Memramcook and the earthworks of Fort Gaspareaux at Port Elgin. Northeast: Doak House at Doaktown, Boishébert and Beaubears Island on the Miramichi, the Village Historique Acadien, and the Miscou Island lighthouse. Sources: the Canadian Register of Historic Places statement for every place (historicplaces.ca with `page.py --all -n 60000`; its character-defining elements give what survives, and they are the main source for fabric and brick); Wikipedia through `wiki_raw.py`; hours from the operators' own pages (Parks Canada for Carleton, the Blockhouse, Gaspareaux, Monument-Lefebvre and Boishébert; kingslanding.nb.ca; villagehistoriqueacadien.com; ministersisland.net; gnb.ca for Government House; the Anglican diocese and cccath.ca for the cathedral); UNB's Military Heritage Project for Petit-Sault; Lighthouse Friends for Miscou. **Not checked:** anything on the ground; hours for McAdam (its site answered 403), Loyalist House (403), Doak House (no provincial page found), Kings Landing's summer hours (its page said only "closed for the season" in November), the Petit-Sault blockhouse and the Miscou lighthouse (only Lighthouse Friends says May to October) — all `hours='?'`; whether the Seal Cove stands still stand and work as listed in 2005; who owns the Reid's Mill ground (32-34 Old Mill Road, view only); where the Beaubears Island ferry leaves from. Pins that mark an area, not the thing: Reid's Mill (Register point by the river; the stack was not seen on the aerial), Seal Cove (moved onto the shed cluster at the east breakwater), Beaubears Island (middle of the island), Village Historique Acadien and Kings Landing (museum points inside large sites). Register coordinates fell off the place twice (Seal Cove in forest, Village Historique Acadien in marsh 1 km off). There is no 1 m LiDAR and no public-land layer for New Brunswick, so every pin printed "not on mapped public land". Red brick: yes only for the Marysville mill; `?` for Kings Landing, the Village Historique Acadien, Ministers Island, Beaubears and Petit-Sault; no for the rest, each from the Register's materials.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Partridge Island Quarantine Station | Saint John harbour, NB | National Historic Site (Register 12721) and light tower (13264) | Whether the public may go on the island now; a source for what stands |
| Fort Howe | Saint John, NB (45.2765, -66.0728 from the Register list) | National Historic Site (Register 13001) | What is on the ground and access |
| Fort Nashwaak (Naxoat) site | Fredericton, NB (45.9618, -66.6254) | National Historic Site (Register 13272) | Anything to see above ground |
| Swallowtail Lighthouse | Grand Manan, NB | Lightkeeper's house on the Register (16105) | Register statement not read; access |
| MacDonald Farm Provincial Historic Site | Bartibog, Miramichi, NB (47.0971, -65.3555) | Register idp 6244 | Statement and opening not read |
| Sir Samuel Leonard Tilley House | Gagetown, NB (45.7845, -66.1448) | National Historic Site (Register 12662) | Statement and opening not read |
| Miramichi Marine (Seamen's) Hospital | Miramichi, NB (47.022, -65.5102) | Federal heritage building (Register 11707) | Statement not read; what it is now |
| St. Croix Cotton Mill site | Milltown, St. Stephen, NB (45.1758, -67.2946) | Local historic place (Register 10612) | What is left and access |

## Tips
- The Wikipedia "List of historic places in <County>, New Brunswick" pages (15 counties plus a separate St. Andrews list) carry each row's Register id in `idf`/`idp`/`idm` inside `{{HPC row}}`; splitting the raw text from `research/wikiraw/` on `{{HPC row` gives a sortable table of the whole province in seconds. Rows with `idf` (federal) are the national historic sites.
- historicplaces.ca reset about half the connections from `page.py` in a burst (and the Internet Archive copy then failed too); one at a time with a 60-second timeout, retried a few minutes later, every page read.
- Parks Canada's New Brunswick pages: the site's front page (`parks.canada.ca/lhn-nhs/nb/<name>`) carries "Hours of operation"; `/visit/heures-hours` answered 404. Monument-Lefebvre is `/nb/lefebvre`, not `/nb/monumentlefebvre`.
- mcadamstation.ca and loyalisthouse.com answered 403 to `page.py`.
- `tools/choose.py` does not know `--thinnest` (the scheduled prompt asks for it); it drew at random among the provinces and states with one place each, which gave New Brunswick.
- `parking.py` points in Fredericton, Saint John and Edmundston fell on houses or a business twice in three tries; check every one.
