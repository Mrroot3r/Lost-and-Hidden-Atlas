# sc_mzkq: South Carolina: a third scatter, Ashley River to the Upstate
state: South Carolina
region: sc
date: 2026-11-24
places: 10
file: data_sc_mzkq.py

## What this batch is
Ten places in South Carolina (52 places before, 62 after), on ground the first three batches left empty: the Old White Meeting House ruins (Summerville), Prince Frederick's Chapel ruins (Georgetown County), Pelham Mill ruins (Greer), Conestee Mill (Greenville), Walnut Grove Plantation (Roebuck), the Santee Indian Mound and Fort Watson, the Old Colleton County Jail (Walterboro), Stoney Creek Chapel (McPhersonville), Rembert Church (Lee County) and the South Carolina Railroad Museum on the Rockton and Rion granite line. Facts come from Wikipedia raw text and pages read with page.py (SC State Parks, Greenville County Rec, Conestee Nature Preserve, the Liberty Trail, scrm.org). Where a page would not open (Prince Frederick's, Old White Meeting House, the Colleton jail, Fort Watson and refuge hours) the entry rests on Wikipedia plus web search summaries, and says so. Not checked: interiors, parking at most places, owners of the Old White Meeting House, Prince Frederick's, Stoney Creek and Rembert Church. Pins not on the building: Old White Meeting House (moved off the road toward a small structure on LiDAR; area only), Old Colleton County Jail and Rembert Church (area only; no building matched on the aerial). Brick is "?" where no source said. I first wrote Colonial Dorchester and dropped it when the build said sc_bwvu already has it (start.py did not list it, being outside its 15 km); check the id list of the state before choosing.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| White Hall Plantation House Ruins and Oak Avenue | Ridgeland, SC (32.4686, -80.9244) | Wikipedia: brick house with tabby wings, built 1771–76, burned about 1870, NRHP 2000 | Owner and any public access |
| Coopersville Ironworks and Susan Furnace | Gaffney, SC | NRHP: foundations of four factory buildings and three iron furnaces, 1835–43 | Coordinates and access |
| Calhoun Mill (Rogers Mill) | Mount Carmel, SC (34.03417, -82.47472) | Wikipedia: c.1860 three-story brick grist mill, race and dam | Owner and access |
| Shivar Springs Bottling Company cisterns | Winnsboro, SC (34.48861, -81.42083) | Wikipedia: six stuccoed stone cisterns, c.1900 | Owner and access |
| Pottersville kiln site | Edgefield, SC | Wikipedia: kiln mound, alkaline-glazed pottery, NRHP 1975 | Coordinates and access |
| Walterboro Library Society Building | Walterboro, SC (32.90333, -80.65222) | Wikipedia: 1820 Federal frame building, home of the Colleton County Historical Society | Hours and the society's own page |
| Chesterfield, Dillon, Monaghan | SC | Old town centres start.py lists with no Atlas place | Not reached |

## Tips
- start.py reaches only 15 km: Colonial Dorchester was already in sc_bwvu though not listed for Chesterfield. Grep tools/data_sc_*.py for a name before writing it up.
- The Wikipedia coordinate was off the building for Walnut Grove (60 m), Old White Meeting House (on the road) and Rembert Church (in a field); the pin check caught all three.
- southcarolinaparks.com slugs: /colonial-dorchester worked; schpr.sc.gov and the spartanburghistory.org page did not open.
- Web search returned summaries without quoted pages; hours taken from them are marked as such in the entries.
- smoke.js needs a server on port 8766 started first: (cd dist && python3 -m http.server 8766) &.
