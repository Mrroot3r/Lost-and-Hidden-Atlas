# sd_ikte: South Dakota: windmills, a thatched cottage, a petrified-wood park and a log church
state: South Dakota
region: sd
date: 2026-11-22
places: 14
file: data_sd_ikte.py

## What this batch is
A second statewide scatter for South Dakota (claimed with `choose.py --thinnest`; 35 places before, 49 after), kept away from Sioux Falls and the places `sd_ibgk` added. North and central: the Lemmon Petrified Wood Park, the Mobridge Auditorium with Oscar Howe's 1942 murals, the Selby Opera House, the Verendrye lead-plate site at Fort Pierre. East River: the Shakespeare Garden and thatched Anne Hathaway Cottage and the Hawkeye Valley Mill (Wessington Springs), the Hollands grist windmill (Milbank), the 1877 Brown Earth log church (Stockholm), the Stock Judging Pavilion / Agricultural Heritage Museum (Brookings), the Austin-Whittemore House (Vermillion). Black Hills: the 1881 Custer County Courthouse museum, the Jewel Cave historic ranger cabin and natural entrance, the Pig Tail spiral bridge in Wind Cave National Park, the Homestake Opera House in Lead. Sources: Wikipedia via `wiki_raw.py`, NPGallery Register form texts (`page.py`), HMdb markers, NPS pages, and the pages of the city of Lemmon, the city of Mobridge, the Wessington Springs chamber, SDSU, the Clay County Historical Society, the 1881 Courthouse Museum and the Homestake Opera House. Not checked: nothing was seen on the ground. Selby Opera House's present use and opening; Homestake Opera House tour times (only a Deadwood visitor guide gives them, so hours='?'); tour days at the Milbank mill; how much mill machinery survived the 1997–2009 rebuild; Pig Tail Bridge's material; the Hawkeye Valley Mill barn could not be seen under the trees on the aerial (pin is the Register point, prec area, private farm, view only); the Jewel Cave cabin could not be picked out on the aerial (pin area; Commons photos of the cabin were taken 45–67 m from it). Mill dates differ: 1884 (Register form, southdakota.com) or 1885 (SDPB), set conf='mixed'. Custer museum opening is 1975 (society) or September 6, 1976 (Wikipedia). Lemmon has no picture chosen: `photo_find.py look` hung on its sheet.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Allen Bank Building and Cascade Springs Bath House-Sanitarium | Cascade Springs near Hot Springs, SD (43.337196, -103.556000, Register list) | Register list: only surviving building of a failed resort community (84003285) | NPGallery has only the placeholder; southdakotamagazine.com/cascade-falls served the home page; no source opened says what stands or who owns it |
| St. Martin's Catholic Church and Grotto | Oelrichs, SD (43.180034, -103.231323) | Register form 03000764: store of 1885 made a church in 1907, rectory 1925, grotto; closed 1999 and sold to a private owner | Grotto description and present condition; private, view only |
| Chilson Bridge | Edgemont, SD (43.32972, -103.73389) | 1929 Pratt deck truss over the BNSF (Wikipedia); article says closed to traffic, then "rebuilt and reopened in July 2023" | A source on what the 2023 work left of the 1929 truss |
| Wessington Springs Opera House, Carnegie Library, Vessey House | Wessington Springs, SD | On the Register list and the chamber's historical tours page | Not researched; worth a town batch |
| Fort Pierre old school, Stockgrowers Bank, Congregational church | Fort Pierre, SD | Register list points near the Verendrye site | Not researched |

## Tips
- `photo_find.py look` hung on the Lemmon Petrified Wood Park sheet (ten Commons candidates found by name, no sheet drawn in over six minutes) and held up the places after it in the same command; looking at the others one or three at a time worked.
- NPGallery forms for South Dakota read well with `page.py --all -n 200000` (10 of 11 tried); 84003285 is a placeholder. A small script that splits the cached text into sentences and greps them saves reading whole forms.
- travelsouthdakota.com answers 403 to `page.py`, and custersd.com shows a "please wait" challenge; the 1881 Courthouse Museum's own site (1881courthousemuseum.com) and the city and chamber sites read fine.
- The ArcGIS geocoder gave PointAddress hits on the building for every South Dakota street address tried; the Register list point for the Selby Opera House is about 1 km east, in fields.
