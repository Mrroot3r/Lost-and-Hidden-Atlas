# ctsw_ldel: Lower Connecticut River, Connecticut: castle, lights, viaducts and an opera house
state: Connecticut
region: ctsw
date: 2026-11-18
places: 14
file: data_ctsw_ldel.py

## What this batch is
Fourteen places in the lower Connecticut River valley of Middlesex County (region `ctsw`, drawn at random by `choose.py`; nothing was on the map within 15 km of Old Saybrook). Standing: Lynde Point Light, the 1910 Shore Line Electric Railway power house, the 1878 steamboat warehouse of the Connecticut River Museum and Hill's Academy in Essex, the Ivoryton Playhouse, Chester's 1793 Old Town Hall, Gillette Castle, the Goodspeed Opera House, the Amasa Day House and Comstock's Covered Bridge. Ruins and traces: the roundhouse and turntable foundations on the site of the 1636 Fort Saybrook, Chapman Falls and the Beebe mill site at Devil's Hopyard (with the 1937 stone arch Bridge No. 1603), the buried Rapallo Viaduct on the Air Line trail, and the flooded Portland brownstone quarries. Sources: Wikipedia through `wiki_raw.py` (the Middlesex County Register list), Register forms for the power house and Bridge No. 1603 through `page.py`, the HMdb Fort Saybrook marker, CT DEEP park pages and coastal access sheet, the Friends of Gillette Castle, Connecticut Landmarks, Goodspeed Musicals' tours page, the Essex Historical Society, East Hampton's Air Line Trail brochure and connecticuthistory.org. Not checked: anything on the ground; Fort Saybrook park hours; the Connecticut River Museum's hours with the museum (taken from CTvisit); Brownstone park hours; who owns Lynde Point Light now; the current use of the power house and Chester's Old Town Hall; interiors of the museum, playhouse, opera house and town hall. Red brick is `?` for the museum, Hill's Academy, the playhouse and the opera house. Pins: none marks only a trailhead; Chapman Falls marks the falls, not a found mill ruin. The Rapallo Viaduct has no parking point: the lot mapped on Smith Street is a school's. Dates disagree for Comstock's Bridge (three sources, three stories) and for the end of the Saybrook Point railroad (1915 or 1922); both entries give the versions and are `mixed`.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pratt, Read and Company Factory Complex | Deep River, CT (41.390278, -72.439444) | Ivory piano-key works on the Register (84001117); Wikipedia's Ivoryton article names it as one of the two big ivory makers | No source read on what stands and who owns it |
| Doane's Sawmill / Deep River Manufacturing Company | Westbrook and Deep River, CT (41.3381, -72.4839) | Register listing 85000313 | Form not read; access unknown |
| Cypress Cemetery and Collegiate School site | Old Saybrook, CT (41.2838, -72.3553) | Register listing 100003006; the federal names file has a "Collegiate College" school site nearby | No source opened |
| Lyman Viaduct | Colchester, CT (Air Line trail) | East Hampton's brochure: 1873, once 1,108 ft long, 137 ft over Dickinson's Creek, buried | Belongs to region `cte`; not researched further |
| Saybrook Breakwater Light | Old Saybrook, CT (41.26324, -72.34278) | Wikipedia; mentioned in the Lynde Point entry | Own entry if wanted; boat or distant view only |

## Tips
- `publish.sh`'s check refuses any email address in a data file, even a museum's booking address from its own page; write "by email through its page".
- The ctrivermuseum.org visit page answers 404 with no archived copy; CTvisit's listing carried hours and fees.
- In Old Saybrook the Register list coordinates for Lynde Point Light and the Shore Line power house both fell 70 m off the structures (on houses and a road).
- `parking.py` near the Rapallo Viaduct offers a school lot on Smith Street as the nearest; DEEP names the Air Line trailhead as "Smith Street, near Flanders Road", which needs looking at before pinning.
