# dc_uzsg: Washington, D.C.: Rock Creek, Georgetown canal and the Fort Circle
state: District of Columbia
region: dc
date: 2026-11-19
places: 19
file: data_dc_uzsg.py

## What this batch is
The first places in the District of Columbia (region `dc`, drawn by `choose.py`): Peirce Mill, the Joaquin Miller Cabin, Fort DeRussy, Fort Stevens and Battleground National Cemetery in the Rock Creek valley; the Old Stone House, C&O Canal Locks 1 to 4, the Aqueduct Bridge abutment, the Godey Lime Kilns, the canal's Tide Lock, the Mount Zion and Female Union Band Society cemeteries, Tudor Place and Holt House (Georgetown and the Zoo); the Lockkeeper's House on the Mall; Christ Church, Washington Parish and Congressional Cemetery on Capitol Hill; and Battery Kemble, Fort Totten and Fort Dupont on the ridges. Sources: Wikipedia through `wiki_raw.py`, NPS `nps.gov/places/...` pages and the Rock Creek Park visitor-center pages through `page.py --all`, HMdb marker pages (NPS signs), and the pages of the Trust for the National Mall, Tudor Place, Congressional Cemetery, the Mount Zion - Female Union Band memorial park, Christ Church and the National Zoo. Pins from OpenStreetMap (`nom.py`) or HMdb; Fort DeRussy, Fort Totten and Fort Dupont were moved onto earthworks that show plainly on the LiDAR sheet (the aerial shows only woods). Brick from Wikipedia photographs opened with `brick.py look` (Peirce Mill, Old Stone House, Lockkeeper's House, Holt House 'some'; Godey kilns, Christ Church 'no') or from what the sources say (earthworks, log cabin, stucco). Not checked: anything on the ground; the opening hours inside Peirce Mill and the Old Stone House (the NPS pages draw them by script); gate hours at Battleground cemetery and Mount Zion; parking at Fort DeRussy, Fort Totten, Fort Dupont and the Joaquin Miller Cabin (the cabin pin is the Wikipedia coordinate, under trees, `prec='site'`); what survives of the Tide Lock itself (the pin is its NPS sign); whether Holt House can be seen from outside the Zoo. Sources disagree, and both versions are given, on Peirce Mill's building date (1820 or 1829), Tudor Place's opening days (its own page says both Wednesday-Saturday and Tuesday-Saturday), the Lockkeeper's House walls (NPS: brick; the photograph: stone), and Fort Dupont's remains (Wikipedia: few; NPS and the LiDAR: a clear hexagon).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Capitol Stones | Rock Creek Park maintenance yard, Washington, DC | Sandstone blocks from the old Capitol's east front, left in the park for decades; news stories (WTOP, NPR, 2022) say most were moved into storage in 2022 and a few kept in the park | Which stones remain and where, and whether the public may see them; not opened in this session beyond search-result titles |
| Fort Reno | Tenleytown, Washington, DC (38.952, -77.0759) | Wikipedia: the ramparts were destroyed when the reservoir was built; the park holds DC's highest point and the old Reno School | Nothing of the fort to see; the Reno School and the vanished Black town of Reno might make an entry with a source |
| Fort Slocum, Fort Bunker Hill, Fort Mahan, Fort Davis, Fort Chaplin | Washington, DC (HMdb markers 110283, 111795, 46083, 40690, 10628) | NPS pages; Fort Bunker Hill: "little evidence" visible | Whether anything shows: try each on the LiDAR sheet as was done for Fort Dupont |
| Washington's boundary stones | the District's edges | Wikipedia: 36 of the 40 stones of 1791-92 survive | Choose the ones on public land with a position and a source on access |
| McMillan Sand Filtration Site | Washington, DC (38.9251, -77.0173 is the reservoir) | Wikipedia article on the reservoir | Current state of the redevelopment and what can be seen from the street |

## Tips
- The NPS Rock Creek Park and C&O Canal visitor-center pages draw "Hours & Seasons" by script: `page.py --all` gets the text but not the hours. The `nps.gov/places/...` pages do give hours when the place has them (the Lockkeeper's House).
- The Rock Creek Park visitor-centers page holds the real addresses of its sub-pages (`old-stone-house-visitor-center.htm`, `peirce-mill-visitor-center.htm`); grep the cached page in `research/pages/` for `href` to find them rather than guessing.
- For the Civil War forts the LiDAR sheet found the earthworks every time (DeRussy, Totten, Dupont) when the marker positions were 40 to 125 m off them.
- An NPS place page can be wrong about a building's material: it calls the Lockkeeper's House brick; the photograph shows stone. Look at a picture before taking brick from a text.
