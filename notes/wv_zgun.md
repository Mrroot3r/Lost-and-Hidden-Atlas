# wv_zgun: West Virginia: a first scatter across the state
state: West Virginia
region: wv
date: 2026-11-20
places: 16
file: data_wv_zgun.py

## What this batch is
Sixteen places spread across West Virginia, which had 16 places, all but Nuttallburg in Jefferson County: the Henry Clay Iron Furnace (Coopers Rock), the Trans-Allegheny Lunatic Asylum (Weston), the West Virginia Penitentiary (Moundsville), the Wheeling Suspension Bridge and West Virginia Independence Hall (Wheeling), the Philippi Covered Bridge, the coke ovens on the Blackwater Canyon Trail (Thomas/Coketon), the Cass company town, Old Stone Presbyterian Church (Lewisburg), Sweet Springs Resort, the Kaymoor mine and coke works and Thurmond (New River Gorge), the Old Roman Bath House (Berkeley Springs), the Beckley Exhibition Coal Mine, the Hinton Historic District and Fort Boreman (Parkersburg). Facts come from Wikipedia (`wiki_raw.py`) and, read with `page.py`, the pages of WV State Parks, the asylum's tour pages, WV Pen Tours' FAQ, the WV Division of Culture and History, Old Stone Presbyterian Church, the Museum of the Berkeley Springs, NPS New River Gorge (Visiting Kaymoor, hours, Thurmond), WV Rails to Trails, e-WV and the City of Parkersburg. Not checked: anything on the ground; how many coke ovens survive by the Blackwater Canyon Trail and whose land the oven bank is on (the federal map says the trailhead is in Blackwater WMA, WV Rails to Trails says the trail is in the Monongahela National Forest; `conf='mixed'`); train times at Cass; tour times at the penitentiary; the Beckley mine's hours (only e-WV gives them; hours='?'); whether Sweet Springs is shown to visitors (the foundation's site would not open); bath hours at Berkeley Springs; parking in Wheeling, Philippi, Lewisburg, Hinton and Thurmond; interiors everywhere. Pins that mark an area or a stretch rather than the thing: the coke ovens (an OSM point on the trail grade), Kaymoor (the Wikipedia point for the whole site, in woods), the Henry Clay furnace (Wikipedia point, under trees). Red brick: 'no' only where a source names stone, wood or earthworks; '?' for the rest, no picture was opened.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grave Creek Mound | Moundsville, WV | A state-run site; the Division of Culture and History notice gives it the same Tuesday to Saturday 9 to 5 hours as Independence Hall | A Native American site: needs the managing body's own page read and the GUIDE section 8 rule for such sites |
| Hinton Railroad Museum | Hinton, WV (Temple Street) | Listed on an NPS "places" page for New River Gorge | Its own hours page; the NPS page gave no text beyond tags |
| Rush Run, Red Ash and Stone Cliff coke ovens | New River Gorge, WV (OSM leads near 37.96, -81.06) | Mapped as ruins in OpenStreetMap | A source on each and the NPS trail that reaches it |
| Fort Boreman magazine | Parkersburg, WV (39.26134, -81.56855, OSM lead) | Mapped as a ruin inside Fort Boreman park | A source on the magazine itself |

## Tips
- `sweetspringsresortpark.org` refused the connection from `page.py`, and its archived copy could not be fetched either.
- No operator page for the Beckley Exhibition Coal Mine turned up in a web search; e-WV and coalheritage.wv.gov were the only official-looking hits, and the latter has no hours text.
- `pincheck.py --batch ... --lidar` for 16 pins ran longer than the two-minute shell limit; run it in the background and read the log.
- West Virginia's Wikipedia infobox points for districts and parks (Hinton, Cass, Sweet Springs) fell among houses, on a road junction and on a lawn; `nom.py` found the station and company store directly.
