# nv_nwjq: Nevada: mansions, kilns, depots and a prison
state: Nevada
region: nv
date: 2026-11-21
places: 17
file: data_nv_nwjq.py

## What this batch is
A second scatter of 17 places across Nevada (20 before): Bowers Mansion, the Nevada State Prison, the Sutro Tunnel portal and the Rock Point mill ruins in Dayton State Park round the Comstock; Mormon Station at Genoa and the Dangberg Home Ranch in the Carson Valley; the Elgin Schoolhouse, Thompson's Opera House, the Caliente depot and the Panaca Summit charcoal kilns in Lincoln County; the Tybo charcoal kilns (Nye); St. George's Episcopal Church in Austin; the McGill Drugstore Museum; Hawthorne's shut 1883 courthouse; the Lovelock depot; and Kiel Ranch and the Boulder Dam Hotel in Clark County. Facts from Wikipedia (`wiki_raw.py`), parks.nv.gov (Dayton, Mormon Station, Elgin, with their history pages), Washoe County's Bowers Mansion page (2027 tour dates), the prison preservation society's and Friends of Sutro Tunnel's Ticket Tailor pages, dangberg.org, the BLM Panaca kilns page, the Tybo kilns' 1974 Register form, the SHPO Kiel Ranch marker, the Episcopal Diocese of Nevada church list, the City of Caliente page and a 2024 Mineral County Independent-News article. Travel Nevada was used, with `hours='?'`, where the runner's page failed: Sutro Tunnel (thesutrotunnel.org reset the connection), Thompson's Opera House (piochenevada.com 403), McGill Drugstore (wpmuseum.org 404), Boulder City/Hoover Dam Museum (no own page found). Not checked: anything on the ground; Kiel Ranch's hours (city site 403); Dangberg Open House dates; who holds the Tybo kilns now (the 1974 form is a federal BLM filing; pin check says BLM Tonopah field office) and their state; whether shops still use the Lovelock depot; the Rock Point ruins themselves on the aerial (pin is the park, area); the Tybo kilns on the aerial (pin area); parking for town buildings. Red brick: St. George's 'yes' and the old Mineral County courthouse 'no' (painted) from the article photographs; Bowers, Sutro, Dangberg, Elgin, Thompson's and McGill '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bristol Wells town site and kilns | Lincoln County, NV (38.1027, -114.69138) | Mining town from 1870 with a smelter and stone charcoal ovens; NRHP 1972 (Wikipedia: Bristol Wells Town Site) | What stands, land owner and road |
| Humboldt County Courthouse | Winnemucca, NV (40.96639, -117.73639) | 1921 Classical Revival courthouse by Frederick DeLongchamps (Wikipedia) | Visiting, fabric |
| Unionville | Pershing County, NV (40.44583, -118.12222) | First Humboldt County seat; abandoned cabins and a schoolhouse stand in disrepair; one inn (Wikipedia) | Owners, which ruins can be seen from the road |
| Metropolis | Elko County, NV (41.22806, -115.05611) | 1910s farm town; ruins of the hotel and school and a cemetery remain, ranches round it (Wikipedia) | Land owner, legal access to the ruins |
| Nevada Central turntable and St. Augustine's Church | Austin, NV (39.497108, -117.08385; 39.49306, -117.06972) | NRHP; St. Augustine's 1866, Nevada's oldest Catholic church building (Wikipedia) | Owners' pages, opening |
| Fort Schellbourne | White Pine County, NV (39.789167, -114.685) | NRHP listing (Wikipedia list) | Everything: what is left, owner |
| Lehman Orchard and Rhodes Cabin | Great Basin National Park, NV (39.0061, -114.218) | NRHP listings in the park (Wikipedia list) | NPS page on both |

## Tips
- washoecounty.gov park pages read with `page.py --all`; Bowers Mansion's page carries next year's tour dates and times in one block after "Tour Information".
- Ticket Tailor event pages (tickettailor.com/events/<org>/<n>) read cleanly with `page.py` and give tour start times; the Nevada State Prison society and Friends of Sutro Tunnel sell tours there.
- ednv.org/find-a-church lists every Episcopal church in Nevada with its service time; grep the town name in `page.py --all`.
- cityofnorthlasvegas.com, piochenevada.com and recordcourier.com answer 403 to `page.py`; wpmuseum.org pages answered 404; thesutrotunnel.org reset the connection.
- BLM visit pages (blm.gov/visit/<site>) give the site's coordinate; the Panaca kilns point was within 13 m of BLM photographs on Commons.
- Web searches again returned titles and links only, no quoted text.
