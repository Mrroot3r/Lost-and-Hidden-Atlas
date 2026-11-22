# nc_iodc: North Carolina: a second scatter, Corolla to Asheville
state: North Carolina
region: nc
date: 2026-11-22
places: 17
file: data_nc_iodc.py

## What this batch is
Seventeen places spread across North Carolina, which had 30: the Roanoke Canal Museum and Trail (Roanoke Rapids), the Newbold-White House (Hertford, 1730), Fort Branch (Hamilton), Bentonville Battlefield and the Harper House, Tryon Palace (New Bern), the Currituck Beach Light (Corolla), the Bellamy Mansion and its brick slave quarters (Wilmington), Rocky Mount Mills, the Old Orange County Courthouse (Hillsborough), the House in the Horseshoe (Moore County), the Spencer Shops roundhouse (NC Transportation Museum), Fort Dobbs (Statesville), Murray's Mill and the Bunker Hill Covered Bridge (Catawba County), the Old Burke County Courthouse (Morganton), Flat Top Manor (Blowing Rock) and the Thomas Wolfe Memorial (Asheville). Facts from Wikipedia (tools/wiki_raw.py), HMdb, and the managing bodies' own pages read with tools/page.py: historicsites.nc.gov, tryonpalace.org, nctrans.org, nps.gov (Blue Ridge Parkway), catawbahistory.org, roanokecanal.com, perquimansrestoration.org, fortbranchcivilwarsite.com, bellamymansion.org. Pins from address lookups (ArcGIS) and OpenStreetMap, all looked at on the aerial; the Morganton courthouse was moved 58 m onto the building. LiDAR in these spots was only the coarse model. Not checked: hours for Fort Branch, the Currituck Beach Light, Flat Top Manor and the Burke courthouse (hours='?'; the Burke County tourism page gives two different weekday schedules and the Historic Burke Foundation's page answered 404); business hours at Rocky Mount Mills; interiors of the Hillsborough courthouse and the House in the Horseshoe. The House in the Horseshoe is closed for building work until early 2027 by the state's notice. Fort Branch is pinned on its street address with prec area; Bentonville is pinned on the visitor center, beside the Harper House. Red brick was set from sources or Commons pictures opened in the session (Currituck, Newbold-White, Tryon Palace, Hillsborough yes; Bellamy some).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Roanoke Canal aqueduct over Chockoyotte Creek | Weldon, NC (an HMdb marker in Weldon at 36.428, -77.595 says 0.75 mile west towards Ponderosa Road) | Wikipedia and roanokecanal.com: the 1821-1823 aqueduct survives on the canal trail | An exact position to pin it on its own; the trail entry pins the museum |
| Cape Lookout Lighthouse | Cape Lookout National Seashore, NC (34.60528, -76.53611) | Wikipedia; NPS: closed since 2021 for a stabilization project expected to take two to three years | Whether it has reopened; then a boat entry with the ferry |
| Market House | Fayetteville, NC (35.05256, -78.87831) | Wikipedia: 1832 market house and town hall on the site of the burned state house, a National Historic Landmark; upper floor a museum | The museum's own hours page |

## Tips
- historicsites.nc.gov slugs are not the site names: House in the Horseshoe is /all-sites/house-horseshoe (a web search found it); guessed addresses 404.
- catawbahistory.org/hours-admission gives day-by-day hours for Murray's Mill, Bunker Hill Covered Bridge and the Catawba County museums on one page.
- The Currituck Beach Light owner's site (currituckbeachlight.com) read with page.py but held no hours text; no other owner page was found.
- The Old Orange County Courthouse's Wikipedia coordinate is about 2 km north of the building; OpenStreetMap (nom.py) had it at 106 East King Street.
