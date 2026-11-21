# ut_pbty: Utah: a first scatter across the state, from Promontory to Bluff
state: Utah
region: ut
date: 2026-11-21
places: 18
file: data_ut_pbty.py

## What this batch is
Eighteen places spread across Utah, which had 17, all round Tintic and the West Desert Pony Express stations: the Big Fill at Golden Spike, the Logan Tabernacle, Ogden Union Station, the Cottonwood Paper Mill, Iosepa, Swett Ranch, Thistle, Fort Deseret, the Topaz camp site, the Territorial Statehouse, Cove Fort, the Fruita Schoolhouse, Sego, Bluff Fort, the Frisco kilns, Silver Reef, Grafton and the Brigham Young Winter Home. Facts are from Wikipedia (tools/wiki_raw.py), two Register forms read as text from NPGallery (Frisco Charcoal Kilns 1982, Fort Deseret 1970), and the pages of whoever runs each place, read with tools/page.py (Utah State Parks, the church's historic-site pages, the Forest Service, the NPS, the Hole in the Rock Foundation, the Topaz Museum, Union Station, the Grafton Heritage Partnership), plus the Utah Geological Survey, Preservation Utah, Utah Humanities, the state historic preservation office and HMdb. Every pin was looked at on the aerial and LiDAR sheets; the Logan Tabernacle and the Old Mill were moved onto their buildings with tools/pix.py; Cove Fort and Silver Reef are site-only because the aerial did not settle which building is which. Not checked: anything on the ground; who owns the Frisco kilns today (1982 form says a mining company, a BLM release describes BLM work there), Sego, Grafton's parcels and Iosepa; the Silver Reef Museum's regular hours (its own page would not open); the Logan Tabernacle's visiting hours; park fees at Golden Spike, Capitol Reef and the Territorial Statehouse; current Fort Deseret rules (the only owner statement is the 1970 form, though the federal land map shows Fort Deseret State Park). Union Station's hours page carries notices several years old. Pins that mark an area only: Thistle (locality point; parking at a US 89 lot that may or may not be the view area).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Spring City historic district | Spring City, UT | Whole-town Register district of stone houses (not read this session) | Sources and a pick of buildings |
| Corinne | Corinne, UT | Railroad town near Promontory; Methodist church said to survive (memory only) | Any source opened |
| Mercur | Tooele County, UT (40.32078, -112.21217, vanished-places layer) | Vanished mining town | Whether anything is left and whether it is reachable (mine land) |
| Intermountain Indian School / Bushnell Hospital | Brigham City, UT (41.49, -112.01, OpenStreetMap ruins) | Mapped as ruins | Current state (demolition reported in the past, not checked) and access |
| Hole-in-the-Rock crossing | Glen Canyon NRA, UT | Bluff Fort page says the cut is still visible at Lake Powell | NPS page, coordinate, road and boat access |

## Tips
- The church's historic-site pages (churchofjesuschrist.org/learn/locations/... and /learn/historic-sites/...) read well with page.py --all and give weekly hours; the -g filter misses them because the clock times sit in a long run-on line.
- In Utah the federal land map holds few places: state parks show, but private nonprofit sites (Topaz, Grafton, Iosepa) all come back "not on mapped public land".
- wchsutah.org (Washington County Historical Society) refused connection from page.py; the county's own washco.utah.gov pages answered.
- tools/photo_find.py "by name" matching on a common word (Thistle) brings back flowers only.
