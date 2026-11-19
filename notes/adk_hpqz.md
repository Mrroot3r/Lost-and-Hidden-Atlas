# adk_hpqz: Saranac Lake, Lake Placid and the Ausable valley
state: New York
region: adk
date: 2026-11-19
places: 15
file: data_adk_hpqz.py

## What this batch is
Fifteen places in Saranac Lake, Lake Placid (North Elba), Wilmington, Jay and Upper Jay (region `adk`, drawn at random by `choose.py --state ny`, which offered Au Sable Forks); `start.py` found no Atlas place within 12 km of any of those towns. All standing. Saranac Lake's tuberculosis century: the Saranac Laboratory museum, the Stevenson Cottage, the Trudeau Sanatorium campus, Little Red at the Trudeau Institute, the Will Rogers Memorial Hospital, plus the Hotel Saranac, Berkeley Square with Harrietstown Town Hall, and the Union Depot. Lake Placid: the John Brown Farm and grave, the old station (History Museum), the 1936 post office with its Billings murals, and the 1930 Olympic bobsled run. Wilmington: the Whiteface Veterans Memorial Highway and the Castle. Jay: the 1857 covered bridge, and the Wells Memorial Library in Upper Jay. Sources: Wikipedia through `wiki_raw.py` (and its Register list rows); with `page.py` the State Parks page for the John Brown Farm, the Stevenson Cottage museum's visit page and robert-louis-stevenson.org, the Saranac Laboratory Museum's brochure PDF, Historic Saranac Lake's LocalWiki page on Little Red, a 2024 WCAX report (via wvmtradio.com) on the sanatorium's conversion to housing, the Lake Placid tourism office's museum page, the historical society's home page, Clio, the NPS page on the Wells library, and the Vermont Covered Bridge Society's account of the Jay bridge. Every pin was looked at on the leaf-off aerial; the John Brown Farm pin was moved onto the farmhouse and the bobsled pin onto a track. Not checked: anything on the ground; hours of the Whiteface highway, the bobsled complex, the Lake Placid post office and the Wells library (their sites refused `page.py`); the Saranac Lab's hours come from an undated pre-2022 brochure and a tourism listing, the Lake Placid museum's from the tourism office (Clio gives other hours); the depot building's date in Lake Placid; which curves at Mount Van Hoevenberg are the 1930 run (pin `area`); Little Red's exact spot on the Trudeau Institute campus (pin `area`, the Register point). Red brick from pictures for the Hotel Saranac (yes) and the Saranac Lake depot (some: a chimney); seven places are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Keith and Branch Ford Motors Factory and Showroom (Old Seed Store) | Upper Jay, NY (Register point 44.3365, -73.7786) | c.1920 three-storey stuccoed frame building for assembling and selling Model Ts; Register 13000329 (Wikipedia) | The Register point is in woods off Springfield Road; the building could not be picked out on the aerial and no address was found |
| Land of Makebelieve | Upper Jay, NY (44.34, -73.77) | Arto Monaco's children's park, 1954 to 1979, closed after Ausable River floods (Wikipedia) | CLUI says the castle ruins and most structures have been removed; only worth adding if something is left to see |
| Au Sable Forks Historic District, Graves Mansion, Tahawus Masonic Lodge | Au Sable Forks, NY (44.4395, -73.6774; 44.4398, -73.6805; 44.4409, -73.6759) | Register listings 100012670, 100008338, 100006216; the Rogers iron and paper company town (Adirondack Life, 2019) | No description of the buildings found; adirondack105.com's listing story is 404 |
| Asgaard Farm | Au Sable Forks, NY (44.4230, -73.6754) | Register 100004907; a working farm and dairy (goadirondack.com) | A source on what survives from Rockwell Kent's time, and the farm store's hours |
| Paul Smith's Electric Light and Power and Railroad Company Complex | Saranac Lake, NY (44.324167, -74.1325) | Register 87001898, headquarters of Paul Smith's 1907 company (Register list) | Not read in this session |
| Keene Valley bridges and Hurricane Mountain fire tower | Keene and Keene Valley, NY | Beer's, Notman, Ranney and Walton bridges (AuSable River Valley Bridges MPS) and the 1919 Hurricane Mountain tower are on the Register list | Not read in this session; the Atlas has nothing in Keene yet |

## Tips
- historicsaranaclake.org reset the connection and its /contact page answered 403; the museum's brochure PDF on cdn.lakeplacid.com and the LocalWiki copy (`localwiki.org/hsl/<Page_Name>`) read fine.
- whiteface.com, orda.org, lakeplacidlegacysites.com and wellsmemoriallibrary.org answered 403 to `page.py`; adirondackdailyenterprise.com answered 429.
- The Stevenson Cottage museum is `rlscottagemuseum.org` (its /visit page reads); stevensoncottage.org does not connect.
- `parking.py` maps no lot at the Jay covered bridge.
- Register points off the thing: John Brown Farm's OpenStreetMap point is 180 m north of the farmhouse in a field; the Mt. Van Hoevenberg bobsled run's Register point is on a sports field.
