# ok_wtca: Oklahoma: a first scatter
state: Oklahoma
region: ok
date: 2026-11-21
places: 19
file: data_ok_wtca.py

## What this batch is
Nineteen places scattered across Oklahoma, the state with the fewest places when `choose.py --thinnest` was run (19 places, nearly all in Logan County): the forts Washita, Towson (with the Doaksville town site next to it), Gibson, Supply and Reno; the Arcadia Round Barn, the Marland Mansion in Ponca City, the McCully sod house near Cleo Springs, Hunter's Home at Park Hill and the Overholser Mansion in Oklahoma City; the Choctaw capitol at Tuskahoma and the Cherokee National Capitol at Tahlequah; Wheelock Academy and Wheelock Mission Church near Millerton; Boggy Depot; Medicine Park's cobblestone town; the Coleman Theatre in Miami; and Boston Avenue Methodist Church in Tulsa. Sources: Wikipedia as raw text (`wiki_raw.py`); the Oklahoma Historical Society's site pages and their `visit-<site>` pages (hours, fees, closings); the Chickasaw, Choctaw and Cherokee Nations' own pages; fortreno.org, arcadiaroundbarn.com and marlandmansion.com; the National Park Service's Route 66 place pages; TravelOK for Boggy Depot only. Pins from ArcGIS PointAddress or OpenStreetMap points, all looked at on the aerial (and the LiDAR sheet): the Choctaw capitol was moved 107 m off the road onto the building with `pix.py`, and Medicine Park 4 km from a Wikipedia point on Fort Sill onto Cobblestone Row. Not checked: anything on the ground; the Coleman Theatre's tour times and Boston Avenue's service times (both sites answer 403); hours at Wheelock Academy (tours by telephone only) and Wheelock church (look only); whether Fort Washita's south barracks was rebuilt after its 2010 fire; which body runs Boggy Depot Park (Wikipedia says both Choctaw and Chickasaw; TravelOK says Chickasaw) and where its foundations are; which Medicine Park buildings are original; red brick at Fort Gibson, Fort Supply, Fort Reno, Hunter's Home, Wheelock Academy, Boggy Depot, Doaksville and Medicine Park (left `?`). Fort Supply and the Overholser Mansion are closed (until further notice, and until 2027). Pins on the general area only: Doaksville (cemetery trailhead), Boggy Depot (park point), Medicine Park (one building in town), Fort Supply (address point).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pawnee Bill Ranch | Pawnee, OK | Oklahoma Historical Society site, home of Gordon Lillie, with original outbuildings (Wikipedia; okhistory.org/sites/pawneebill) | Temporarily closed for restoration (society page, November 2026); coordinate and reopening date |
| Frank and Jane Phillips House | Bartlesville, OK (36.74194, -95.975, Wikipedia) | 1908-1909 Greek Revival house given to the Oklahoma Historical Society in 1973 (Wikipedia) | `okhistory.org/sites/phillipshome` answers 404: who runs it now, and hours |
| Price Tower | Bartlesville, OK (36.74778, -95.97611) | Frank Lloyd Wright's 1956 tower, National Historic Landmark (Wikipedia) | Present owner and whether the public may go in |
| Fort Sill Old Post | Lawton, OK | Army post founded 1869 (Wikipedia) | Visitor access rules for the active base, from the Army's own page |
| Choctaw and Chickasaw sites: Chickasaw Council House, Tishomingo; Cherokee Supreme Court Museum, Tahlequah | Johnston and Cherokee counties | Named in search results only | Articles and managing pages not read |
| Spiro Mounds | LeFlore County | An Oklahoma Historical Society site (listed on its site menu) | Not read; a Native American site, to be written only from the society's own visiting page |

## Tips
- Oklahoma Historical Society hours are not on a site's main page (`okhistory.org/sites/<site>`) but on `okhistory.org/sites/visit-<site-with-hyphens>` (visit-fort-gibson, visit-fort-towson, visit-sod-house, visit-hunters-home); `page.py --all` reads them. The site menu in any cached page lists every site's address.
- Wikipedia's Doaksville coordinate is about 18 km east of the site; the society's directions put the trailhead in Fort Towson Cemetery.
- Wikipedia's Medicine Park town point falls inside Fort Sill on the highway; the pin check's `CHECK ACCESS` line caught it.
- colemantheatre.org and bostonavenue.org answer 403 to `page.py`; the National Park Service's `nps.gov/places/<name>.htm` pages covered the Route 66 places (Coleman Theatre, Fort Reno, Arcadia Round Barn).
- fortreno.org carries a planted casino advertisement in its text; ignore it.
