# wi_kzdf: Wisconsin: houses, a brewery and a village site in the south and east
state: Wisconsin
region: wi
date: 2026-11-23
places: 12
file: data_wi_kzdf.py

## What this batch is
Twelve places in southern and eastern Wisconsin outside the lead region and the first two batches: Milton House and the Lincoln-Tallman House (Rock County), Aztalan (Jefferson), Stonefield at Cassville, the Potosi Brewery and the Mitchell-Rountree Stone Cottage at Platteville (Grant), the Beloit water tower, Kemper Hall in Kenosha, Galloway House at Fond du Lac, Hazelwood at Green Bay, the Ringling winter quarters at Baraboo and the pulpwood stacker at Cornell. Facts come from Wikipedia raw text and the Register county lists (wiki_raw.py), the Wisconsin DNR and Wisconsin Historical Society pages, the Milton House and Brown County Historical Society pages. Hours for the Lincoln-Tallman House, Potosi Brewery, Mitchell-Rountree cottage, Kemper Center, Circus World and Galloway House are only as web search results quoted them (several own pages would not open); Stonefield and Aztalan hours were not found. Not checked: interiors and original fabric for most houses, parking lots (except Stonefield's), who owns the Cornell stacker park beyond Wikipedia, and red brick for six places (brick='?'). Stonefield's and the Circus World pin were moved off Register points that fell on a road and downtown streets. The Mitchell-Rountree and Hazelwood pins sit on a house of the right size but no source showed the building's own picture. Galloway House has no Wikipedia article and rests on the Register row and listings (conf mixed).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Palm Tree Road Bridge | Marshfield (Fond du Lac County), WI (43.8143, -88.1647) | Register row: nine-arch fieldstone bridge of 1901 by Alphonse Halter, longest stone-arch bridge in the state | A source beyond the Register row, access and a pin check |
| J. & C. Wipf Mills | Iola, WI (44.5097, -89.1306) | Register row: three-storey water-powered mill begun about 1860 | Any source beyond the row, and whether it can be visited |
| Potosi Badger Huts Site | Potosi, WI (42.6861, -90.7125) | Register row: lead-mining remains on a ridge from 1833, two structures and test pits | Whether the public may visit |
| Vernon County Courthouse and Bekkedal Tobacco Warehouse | Viroqua, WI (43.5567, -90.8931) | Register rows: 1880 limestone courthouse; 1906 brick tobacco warehouse | Sources and hours; Viroqua is an old town centre with no Atlas place yet |

## Tips
- Register county lists via `wiki_raw.py --rows` saved to files gave the whole candidate list for a dozen counties in one go; grep them by name.
- `wiki_raw.py` returned nothing for "Lincoln-Tallman House" with a hyphen (the article is titled with an en dash and the redirect gave an empty page); the web fetch tool read it.
- Register points fell on roads, in woods or on downtown streets for Stonefield and the Ringling quarters; the OpenStreetMap museum points and a wider look.py picture put them right.
- `page.py` could not read miltonhouse.org's home page (connection reset) but read /tours; circusworldbaraboo.org gave HTTP 526 (the site is circusworld.wisconsinhistory.org).
