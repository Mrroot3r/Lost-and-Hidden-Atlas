# wv_gkkh: West Virginia: Harpers Ferry, Charles Town and Shepherdstown
state: West Virginia
region: wv
date: 2026-11-19
places: 15
file: data_wv_gkkh.py

## What this batch is
Fifteen places in Jefferson County, the first real batch for West Virginia's eastern panhandle. Harpers Ferry: Virginius Island mill ruins, John Brown's Fort, St. Peter's church, the Storer College campus, the B&O bridge piers and the Bolivar Heights earthworks. Charles Town: the courthouse, Zion Episcopal and its Washington graves, and Happy Retreat. Also the Halltown chapel, Duffields Depot, the Shannondale Springs resort ruins, the Shepherdstown cement mill ruins, Shepherd's Mill with its 40-foot wheel, and the Fountain Rock remains in Morgan's Grove Park. Sources were Wikipedia (`wiki_raw.py`), NPS park and "places" pages, the Jefferson County Historic Landmarks Commission's cement-mill page and brochure, the 1997 Shannondale Register form (a wvculture.org PDF with a text layer), the WVDNR map of the wildlife management area, and the Friends of Happy Retreat, St. James parish, Zion Episcopal, Clio, SAH Archipedia and local news pages, all read with `page.py`. Not checked: anything on the ground; whether the cement mill grounds are open to walk (marked view only); the hours of the courthouse, Zion's churchyard, Shannondale WMA and Morgan's Grove Park; which lot is nearest the Shannondale ruins; whether John Brown's Fort can be entered. Pins that mark only an area or a trailhead: Bolivar Heights (the NPS lot at the trailhead), Shannondale Springs (Register point, on the riverbank, ruins not made out on LiDAR), Fountain Rock (on the park's playing field), Virginius Island (the island as a whole). Red brick settled by a photograph for John Brown's Fort (yes) and Storer's Lockwood House (some); Wikipedia's text calls the courthouse red brick.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Opera House | Charles Town, WV (39.28996, -77.86077, OSM building) | 1911 theatre by T. A. Mullett, closed 1948, reopened as a community theatre (Wikipedia) | Hours or tours: oldoperahouse.org gave almost no text to page.py; brick not settled |
| Shannondale Springs hotel foundation | Shannondale Springs WMA, WV | Register form puts the bathhouse 50 ft NE and the fountain 50 ft S of the hotel ruin, midway up the hill | A position for the hotel ruin, and the nearest hunter-access lot (WVDNR map marks lots but its text gives no positions) |
| Harewood, Blakeley, Claymont Court and other Washington family houses | Charles Town area, WV (Register list coordinates) | Register list rows; Happy Retreat's page mentions owners restoring Harewood and Blakeley | Private homes: an opened source on what can be seen from a public road |
| Rumsey Monument | Shepherdstown, WV (lot on Rumsey Monument Road, 39.43266, -77.79946, parking.py) | A lot is mapped by that name near Shepherd's Mill | No source opened for the monument |

## Tips
- `parking.py` listed the "Storer College Place" and "Fillmore Street" lots at Harpers Ferry; on the aerial both points were on buildings. The Hartzog Road lot was a real lot.
- NPS "places" addresses for Harpers Ferry often carry `/places/000/<name>.htm`; a web search for the place's name with nps.gov found them when guessed addresses answered 404.
- The Wikipedia coordinate for Bolivar Heights Battlefield lands among houses in Bolivar; the NPS lot on Prospect Avenue is the trailhead.
- A WVDNR wildlife-area map PDF has no usable text for `page.py`; rendering it with `pdftoppm -r 60` and looking at it shows the parking and gate symbols.
- `lidar_dem.dem()` and `shade()` can be called directly for a wider bare-ground view than the pin-check tile, when a ruin is somewhere in a big wooded tract.
