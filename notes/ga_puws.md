# ga_puws: Georgia: Rome to Thomasville, Toccoa to the Okefenokee
state: Georgia
region: ga
date: 2026-11-22
places: 20
file: data_ga_puws.py

## What this batch is
Twenty places spread over the parts of Georgia the first two batches left empty (Georgia had 35 places, the fewest of any state or province; now 55). Northwest: Barnsley Gardens manor ruins (Adairsville), Rome Clock Tower, John Ross House (Rossville). Atlanta edge: Roswell Mill ruins. Northeast: Traveler's Rest (Toccoa). Athens: the double-barreled cannon. Middle Georgia: Cannonball House and the Grand Opera House in Macon, Jarrell Plantation, High Falls ghost town ruins, Indian Springs Hotel. Southwest: Springer Opera House (Columbus), Clay County Courthouse (Fort Gaines), Windsor Hotel (Americus), Plains High School and depot, Bridge House (Albany), Lapham-Patterson House and Pebble Hill (Thomasville). South-east: Chesser Island Homestead (Okefenokee; the lead from ga_mhty) and the Georgia State Railroad Museum in Savannah. Facts from Wikipedia (`wiki_raw.py`, Register list rows with `--rows`), and hours from the managing bodies' pages read with `page.py`: Georgia State Parks, the National Park Service, US Fish and Wildlife Service, the Rome tourism office, Barnsley Resort, Cannonball House, Springer Opera House, Pebble Hill and the Village at Indian Springs. Not checked: anything on the ground; hours for Barnsley Gardens (day passes sold, no times given), the Windsor's public rooms, Bridge House, the Grand Opera House, the Railroad Museum (chsgeorgia.org answered 403), the John Ross House (owned by a nonprofit; whether it opens not found), Rome Clock Tower tour times, the Okefenokee refuge's hours and fee. Pins marking only an area: Roswell Mill ruins (no ruin visible under trees), Barnsley Gardens (Wikipedia point by a pond; ruin not picked out), High Falls (pin by the falls; mill foundation and powerhouse ruins not located). Jarrell Plantation and Indian Springs Hotel pins are site-level: the buildings were not singled out on the aerial. Travelers Rest, Jarrell Plantation and Indian Springs Hotel have dates that differ between sources and are conf=mixed. Springer Opera House draws check.py's coarse-border warning; on the aerial it is a downtown Columbus building on the Georgia side.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Ivy Mill ruins | Roswell, GA (Riverside Park, parking 34.00679, -84.34502) | NPS: stone walls of the Ivy cotton mill near the mouth of Big Creek, Vickery Creek unit; a guide site says they are reached by a boardwalk from the city's Riverside Road park | The ruin's position; OpenStreetMap shows the park as under construction, so present access is not settled |
| Old Market, Louisville | Louisville, GA (32.99994, -82.40929) | Wikipedia: open-air market shed of about 1795–98, used also to sell enslaved people; the city council voted in 2020 to remove it | Whether it was removed or still stands, and where it is now |
| Butler Island Plantation | near Darien, GA (31.35472, -81.44649) | Wikipedia: Pierce Butler's rice plantation, Fanny Kemble's journal; DNR land open daily; the 1927 Huston House burned on June 26, 2024 | What is left to see (rice-mill remains?) from a source |
| Lee and Gordon Mill | Chickamauga, GA (34.88361, -85.26694) | Wikipedia: grist mill and store built 1867 on Chickamauga Creek | Present use and whether it opens |
| Fort King George | Darien, GA (31.36384, -81.41493) | Wikipedia: British fort of 1721, now a state historic site | Not read beyond the opening; hours on gastateparks.org |

## Tips
- Georgia State Parks pages give hours in one run after "Hours."; `page.py --all <url> | grep -oE '.{0,150}Hours.{0,350}'` prints them in one line. Addresses that worked: `TravelersRest`, `JarrellPlantation`, `LaphamPattersonHouse`, `HighFalls`.
- Wikipedia's "Lapham–Patterson House" article reads empty through `wiki_raw.py`; the Thomas County Register list row and the state park page carry the facts.
- chsgeorgia.org (Coastal Heritage Society: Georgia State Railroad Museum, Savannah History Museum) answers 403 to `page.py`.
- `photo_find.py look` on four places took more than two minutes: run it in the background as the prompt says.
- `parking.py` listed a lot named "Historic Trail (yellow)" at High Falls that is the river on the aerial; check every lot it gives on the tile.
