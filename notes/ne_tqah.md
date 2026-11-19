# ne_tqah: Nebraska: Brownville, Auburn and Nebraska City
state: Nebraska
region: ne
date: 2026-11-19
places: 18
file: data_ne_tqah.py

## What this batch is
Eighteen standing places in the old Missouri River towns of southeast Nebraska, the state's first real batch (it had one
place before): Brownville (the historic district, the 1859 Methodist church, the Brown-Carson, Furnas, Muir and Bailey
houses, the dredge Captain Meriwether Lewis, the 1939 bridge), Auburn (Nemaha County Courthouse) and Nebraska City
(Arbor Lodge, Wildwood, Mayhew Cabin, the Kregel windmill factory, the G.A.R. hall, the 1865 courthouse, St. Benedict's,
the 1855 Methodist wall, the Russell, Majors & Waddell house). Facts came from the 1970 Brownville Historic District
nomination (NPGallery text, read with `page.py`), HMdb marker pages, SAH Archipedia, Wikipedia (`wiki_raw.py`), the
Brownville visitor site, the Nemaha County tourism museum page, the Nebraska City Museum Association page and the
museums' own pages. Pins are geocoder PointAddresses, HMdb positions or OpenStreetMap points, all looked at on the
aerial; the Auburn courthouse pin was moved onto the building. Not checked: any interior; hours for the dredge, the
Furnas House, the G.A.R. hall, the Mayhew Cabin and the two courthouses; the Arbor Lodge mansion's hours; current
ownership of the Furnas and Muir houses; parking for most places (street parking in small towns). Wildwood is pinned
by an interpolated address (`prec='area'`). Red brick was settled from Wikimedia photographs for five places; eleven
are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Brewery Cave | Brownville, NE | 1970 Brownville nomination: used by the Brownville Brewery about 1866–1900, then a summer coffee house; just outside the district | A position and whether it is open or on private land |
| Gates House and other 1859–1873 brick houses (Lowman, McLaughlin-Parks, Beehive, Bratton-Minick, Nace, Hoover) | Brownville, NE | Each described in the 1970 Brownville nomination; the Gates House may be the oldest house in town | Addresses; most are private homes |
| Nelson House (Taylor-Wessel-Bickel-Nelson House) | 711 3rd Corso, Nebraska City, NE | An 1857 brick house run as a museum by the Nebraska City Historical Society (Nebraska City Museum Association page) | A second source for its date; hours could not be matched on the page |
| Atlas F missile site | About half a mile west of 225 North 56th Road, near Nebraska City, NE (marker 40.67604, -95.93530) | HMdb 54341: one of twelve Atlas-F sites of the 551st Strategic Missile Squadron, 1961–65 | The site's position, owner and whether anything shows; probably private |
| Bridge over the Little Nemaha River | Lorton, NE (40.566944, -96.090556) | National Register 92000733 | Wikipedia had no article under the list's title; condition and access not read |
| Wolf Creek Bridge | near Dunbar, NE (40.78415, -95.91576) | National Register 92000738 | Same: no article read; condition not checked |
| Thomas J. Majors Farmstead | near Peru, NE (40.484444, -95.735833) | National Register 78001707 | No source read; likely private |

## Tips
- Brownville's 1970 district nomination (`npgallery.nps.gov/NRHP/GetAsset/NRHP/70000374_text`) has a good text layer and describes 24 buildings one by one, with dates and builders.
- The Nebraska City Museum Association page (`NebraskaCityMuseums.org/museums`) lists every museum, but in `page.py`'s text the hours blocks fall between descriptions and cannot be matched to one museum with certainty; use each museum's own site where it has one (Wildwood's and Kregel's read well).
- visitnebraska.com, nebraskapassport.com and history.nebraska.gov answered 403 to `page.py`; lewisdredge.org would not connect.
- The ArcGIS geocoder gave PointAddresses for most Nebraska City and Brownville addresses; Wildwood's (420 Steinhart Park Road) came back interpolated and off the house.
- `check.py` warns that the dredge and bridge pins are just outside Nebraska's outline; both are on the Nebraska bank on the aerial.
