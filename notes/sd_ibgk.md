# sd_ibgk: South Dakota: forts, gold-rush towns, a sod house and a missile silo
state: South Dakota
region: sd
date: 2026-11-21
places: 17
file: data_sd_ibgk.py

## What this batch is
A first scatter of 17 places across South Dakota, chosen as the thinnest state on the map (18 places, all but two round Sioux Falls). East River: Fort Sisseton (Marshall County), the Fort Randall chapel ruins (Gregory County), the Corn Palace (Mitchell), the Meridian Bridge (Yankton), the Fort Pierre Chouteau site, the Mellette House (Watertown) and the Ingalls House (De Smet). West River: the Prairie Homestead sod house and the Minuteman sites Delta-09 and Delta-01 by the Badlands; in the Black Hills the Historic Adams House and Mount Moriah Cemetery (Deadwood), the Mount Roosevelt Friendship Tower, the D.C. Booth hatchery (Spearfish), Fort Meade (Sturgis), the Battle Mountain Sanitarium (Hot Springs) and the Tinton ghost town. Sources: Wikipedia through `wiki_raw.py`, the Fort Sisseton Register form, NPS pages (Fort Randall, Minuteman, Battle Mountain), HMdb markers (Fort Randall, Fort Pierre Chouteau), SD Game, Fish and Parks, the Fish and Wildlife Service, the City of Deadwood, Deadwood History Inc., the Corn Palace's page and the SHPO's Black Hills hikes itinerary, all read with `page.py`. Not checked: hours for Prairie Homestead, the two Minuteman sites, the Mellette House, the Old Fort Meade Museum and the Ingalls House (pages drawn by script or not opening); Meridian Bridge and Mount Roosevelt trail hours; present use of the Battle Mountain campus (the VA has proposed closing it); access at Tinton beyond Wikipedia (private, mining company); red brick for most places ('?'). Nothing was seen on the ground. Pins moved on the aerial: Fort Randall chapel (onto the sheltered building, taken to be the chapel), Delta-09 (onto the silo), Delta-01 (onto the topside building). Area pins: Mount Moriah (the aerial shows only pines at the mapped point), Fort Meade (the museum lookup) and Tinton.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Surveyors' House | De Smet, SD | Wikipedia's Ingalls House article says the family lived in the surveyors' house in town in 1879-80; the Memorial Society shows it | A source read in the session and the society's hours (discoverlaura.org reset the connection) |
| Old Finnish Lutheran Church | Lead, SD (44.3525, -103.763889) | Register list, Lawrence County (85003487) | Any text on what stands and whether it is used |
| Homestake Hydroelectric Plant No. 2 | Spearfish Canyon, SD (44.39754, -103.89796) | Register list, Lawrence County (100008619) | The nomination text and whether it can be seen from the canyon road |
| Lead Historic District / Homestake Opera House | Lead, SD (44.351667, -103.7625) | Register list (74001892) | Exact Wikipedia titles; the opera house's own page and hours |
| Battle Mountain Sanitarium status | Hot Springs, SD | NPS article: the VA proposed closing the campus | Whether it is still a VA hospital in 2026 |

## Tips
- Several South Dakota attraction sites are drawn by script (prairiehomestead.com, the Old Fort Meade Museum's Google Sites page, nps.gov/mimi hours page); `page.py` gets nothing from them. Plan on hours='?' or find a state or NPS page that names the times.
- discoverlaura.org (Ingalls homes, De Smet) resets the connection from `page.py`, and fws.gov's old "visit-us" address answers 404; `fws.gov/locations/dc-booth-national-fish-hatchery/tours` works.
- `photo_find.py new` found Wikipedia pictures for 16 of 17 places; only Delta-01 needed a Commons pick.
- `pincheck.py --lidar` on 17 pins takes more than two minutes, longer than a foreground command may run; start it in the background and read its log.
