# co_eehq: Colorado: a second scatter
state: Colorado
region: co
date: 2026-11-21
places: 15
file: data_co_eehq.py

## What this batch is
Fifteen places spread across Colorado, which had 19: the Ashcroft ghost town above Aspen (a lead from co_qmtv), the Kit Carson County Carousel at Burlington, Fort Vasquez at Platteville, the Holzwarth Historic Site and the Lulu City ruins in Rocky Mountain National Park, the Argo Mill at Idaho Springs, the Central City Opera House, Cliff Palace at Mesa Verde, the Mayflower Mill at Silverton, the Baca House in Trinidad, Miramont Castle at Manitou Springs, Rosemount in Pueblo, the Alpine Tunnel station above Pitkin, the Hahns Peak Schoolhouse and the Lodore School in Browns Park. Sources: Wikipedia as raw text (`wiki_raw.py`); with `page.py` the managers' pages (Aspen Historical Society, History Colorado for Fort Vasquez and the Trinidad History Museum, NPS pages for Holzwarth, the Colorado River Trailhead and the Mesa Verde tours, the Forest Service's Alpine Tunnel page, the San Juan County Historical Society, miramontcastle.org, rosemount.org, hahnspeakhistoric.com, kitcarsoncountycarousel.com, centralcityopera.org, argomilltour.com) and SAH Archipedia. Not checked: nothing on the ground; hours and fares at the carousel (only the 2026 opening day), the Argo (its site gives no times) and the Central City Opera House (group tours by reservation, performance dates not read); the Mayflower Mill's summer times; the national park entrance fees; who owns the Lodore School now and whether it opens; parking at Ashcroft, Central City, Miramont, Rosemount, the Mayflower Mill, Hahns Peak and the Cliff Palace overlook (OpenStreetMap's Cliff Palace lot point fell on the road and was dropped). Lulu City is an `area` pin on Wikipedia's coordinate in trees; the Holzwarth cabins could not be made out on the aerial. Red brick is `?` where no source or picture said.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bloom Mansion | Trinidad, CO (OpenStreetMap 37.16942, -104.50230) | Part of History Colorado's Trinidad History Museum, next to the Baca House, open Tuesday to Saturday 10 to 4 (History Colorado page) | Its own history and build date from a source; it is mentioned in the Baca House entry |
| Teller House | Central City, CO | Central City Opera's page lists Teller House tours (centralcityopera.org/project/teller-house-tours/) | Page not read; history and current access |
| Victor gold camp | Victor, CO (Wikipedia 38.71, -105.14) | Wikipedia: founded 1891, peak 18,000 people, mining resumed on Battle Mountain | Which mine headframes or buildings to pin and how they are reached |
| Sand Creek Massacre National Historic Site | near Eads, CO (Wikipedia 38.54083, -102.52861) | NPS site, a sacred place; a few visitor facilities | Whether it belongs on this map at all and how the NPS asks visitors to treat it; no building to see |

## Tips
- argomilltour.com reads with `page.py` (argomillandtunnel.com returns nothing), but gives no tour times.
- The CPR article on the Alpine Tunnel road reopening (cpr.org) gives HTTP 403 and only an archived-copy address.
- `parking.py`'s OpenStreetMap lots at Cliff Palace and the Argo Mill fell on a road and an equipment yard: look at every TRAILHEAD tile.
- `wiki_raw.py "Kit Carson County Carousel"` redirects to "Elitch Gardens Carousel", and "Old Ladore School" is the Lodore School's article title.
