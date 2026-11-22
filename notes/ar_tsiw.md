# ar_tsiw: Arkansas: a first scatter across the state
state: Arkansas
region: ar
date: 2026-11-22
places: 18
file: data_ar_tsiw.py

## What this batch is
Eighteen places spread over the parts of Arkansas the map had nothing in (it had 22, nearly all in Cleburne, Van Buren and Stone counties): Monte Ne (Coin Harvey's drowned resort), the Crescent Hotel at Eureka Springs, the Parker–Hickman farmstead on the Buffalo River, Fort Smith National Historic Site, Mather Lodge at Petit Jean, the Fordyce Bathhouse in Hot Springs, the McCollum–Chidester House in Camden, the Helena Depot (Delta Cultural Center), Dyess Colony, Lakeport Plantation, the Rohwer camp cemetery, Arkansas Post, Union Station in Pine Bluff, the Old Mill in North Little Rock, the Jacksonport and Powhatan courthouses, and the Frisco depot and the dam at Mammoth Spring. Facts come from Wikipedia articles and county Register lists (`wiki_raw.py`), the Encyclopedia of Arkansas (Monte Ne, Helena Depot), and the managers' own pages read with `page.py`: Arkansas State Parks, the NPS (Fort Smith hours page, Arkansas Post superintendent's compendium, Fordyce, Parker–Hickman, Rohwer cemetery), Arkansas State University Heritage Sites (Lakeport, Dyess, Rohwer), the City of North Little Rock, the Ouachita County Historical Society, the Department of Arkansas Heritage, Explore Pine Bluff. No nomination forms were read. Nothing was checked on the ground. Not checked: hours for the Crescent Hotel and the Fordyce (the NPS hours page lists every bathhouse but the Fordyce); Monte Ne's Corps rules, and whether anything of Oklahoma Row still stands after the 2023 removal (Wikipedia and the Encyclopedia of Arkansas disagree; conf='mixed'); who owns the Rohwer cemetery ground; parking almost everywhere. The Pine Bluff museum's page says it is closed after winter weather damage, so that place is view-only. Pins: Jacksonport courthouse and the Mammoth Spring depot are area pins on the buildings by the park lots (Commons photos show both are long red brick buildings, but the aerial does not tell which roof); Arkansas Post is an area pin in the memorial's woods (visitor center not found on the aerial); Monte Ne is an area pin on the shore by the old Oklahoma Row site; Lakeport is on the farm-building cluster, the house itself not picked out. Red brick from Commons photos for the Frisco depot, the Jacksonport courthouse and the Mammoth Spring power house; from sources for the Helena Depot (red), the Fordyce (cream: no), the log and frame houses (no); the rest `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Davidsonville townsite | Davidsonville Historic State Park, Randolph County, AR (36.15835, -91.05689) | Wikipedia: frontier town with Arkansas Territory's first courthouse (1822); the townsite is a grassy field, few remains above ground; guided tours of the platted site | The state park's own page for hours and what is marked on the ground |
| Pea Ridge, Prairie Grove, Poison Spring battlefields | Benton, Washington and Ouachita counties, AR | Register lists name Poison Spring State Park (69000036) near Chidester | Not researched this session; NPS and state park pages |
| Petit Jean State Park CCC works beyond the lodge | Petit Jean Mountain, Conway County, AR | Arkansas State Parks page: CCC trails, roads, bridges and cabins from 1933 | Individual structures and pins |
| Jerome Relocation Center | Chicot/Drew County, AR | NPS Rohwer page: second Arkansas camp 30 miles southwest of Rohwer | A source for what is left and who owns it |
| Kemp Cotton Gin Historic District | Rohwer, AR (33.763333, -91.276667) | Desha County Register list | Its article or form, owner and access |

## Tips
- `nom.py` (Nominatim) answered three queries and then returned HTTP 629 for the rest of the session; county Register lists from `wiki_raw.py --rows -g` gave the coordinates instead.
- The NPS Arkansas Post hours page draws its hours by script (`page.py` reads only headings); the superintendent's compendium on nps.gov gives the grounds and visitor center hours in plain text.
- Arkansas State Parks pages list several buildings' hours one after the other; `page.py -g` loses which line belongs to which building. Read the cached copy in `research/pages/` around the word "Hours" instead.
