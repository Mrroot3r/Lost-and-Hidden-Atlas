# va_wulp: Virginia: a first scatter across the state
state: Virginia
region: va
date: 2026-11-20
places: 15
file: data_va_wulp.py

## What this batch is
Fifteen places spread across Virginia, which had only Belle Isle: Bacon's Castle (Surry), the Jamestown church tower, St. Luke's Church near Smithfield, Assateague Lighthouse (Chincoteague), Blandford Church and its Tiffany windows (Petersburg), Aldie Mill (Loudoun), Elizabeth Furnace (Fort Valley), the Barboursville ruins (Orange), Poplar Forest (Forest), the Appomattox Court House village, Prestwould (Clarksville), Mabry Mill (Blue Ridge Parkway), the Humpback Covered Bridge (Covington), Roaring Run Furnace (Botetourt) and the Pocahontas Exhibition Coal Mine (Tazewell). Facts come from Wikipedia (`wiki_raw.py`) and the managing bodies' pages read with `page.py` (Preservation Virginia, NOVA Parks, City of Petersburg, Barboursville Vineyards, Poplar Forest, NPS for Jamestowne, Appomattox and Mabry Mill, the Forest Service for Roaring Run and Elizabeth Furnace, Virginia Energy for the Pocahontas mine). Not checked: hours for St. Luke's (its site answers 403) and Prestwould (connection reset), so both have `hours='?'`; Assateague refuge hours and fees (the refuge's visit page is 404) and current lighthouse climbing days; Humpback Bridge wayside hours; parking at Blandford Church, Prestwould and St. Luke's. Pins that mark only an area: Elizabeth Furnace (the stack was not picked out on the aerial or LiDAR) and the Pocahontas mine (in woods; parking is the lot by the street address). Red brick was settled from Wikipedia photographs opened with `brick.py look`. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Poplar Springs Church (Original Site) and Parsonage Ruins | Henrico County, VA (37.46981, -77.26072; 37.41906, -77.247) | OpenStreetMap leads listed by `start.py` | Any source at all, and the owner |

## Tips
- `geo.py` gave PointAddress hits in Virginia (Blandford Church, Bacon's Castle, the Pocahontas mine).
- The Forest Service's new recreation pages (`fs.usda.gov/r08/gwj/recreation/<name>`) read fully with `page.py --all`: "Operational Hours", fees and directions. The "Hours: Monday - Friday 8:00 AM - 4:30 PM" line on them is the ranger district office, not the site.
- stlukesmuseum.org answers 403 to `page.py` and prestwould.org resets the connection; a later session may get the hours by another route.
- `parking.py`'s point for Barboursville Vineyards ("Mansion Road") was on the estate road, not a lot.
