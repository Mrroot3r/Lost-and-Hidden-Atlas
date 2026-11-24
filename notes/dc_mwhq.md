# dc_mwhq: Washington, D.C.: a third scatter, Lafayette Square to Deanwood
state: District of Columbia
region: dc
date: 2026-11-24
places: 13
file: data_dc_mwhq.py

## What this batch is
Thirteen standing buildings the first two District batches left out, spread over the city: Decatur House and St. John's (Lafayette Square), the Smithsonian Castle, the Pension Building, the Old Naval Observatory, the Heurich mansion, Halcyon House, the Peirce-Klingle mansion, the Belmont-Paul house, the Uline Arena, Wheat Row, the St. Elizabeths Center Building and the Strand Theater in Deanwood. Chosen from Wikipedia's five National Register lists for the District (read with wiki_raw.py --rows). Facts come from the Wikipedia articles read as raw text; hours come from the managers' own pages read with page.py (White House Historical Association, National Building Museum, National Park Service for Belmont-Paul, St. John's, Heurich House Museum). Not checked: anything on the ground; Heurich House's tour days (its tours page loads them by script, so none are given); the Castle's hours (si.edu returned 403; the building is shut for renovation); St. Elizabeths West Campus tour dates for 2026; the present use of the Uline Arena and the Strand Theater (sources conflict, so both are marked conf=mixed); parking for the downtown places (none given; transit-served). Red brick is recorded only where an article names the material (Pension Building and Wheat Row yes; Castle, St. John's, Peirce-Klingle and the arena no); the rest are '?'. Two pins were moved after the aerial and OpenStreetMap showed Wikipedia's or the Register's point was off: the Peirce-Klingle mansion (about 250 m) and the St. Elizabeths Center Building (the Register point fell on the East Campus).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Brick Capitol bricks / Sewall-Belmont garden | Belmont-Paul house, Capitol Hill | Wikipedia: the Party paved its garden patio with bricks saved from the Old Brick Capitol | Whether the patio can be seen on the tours |
| Howard Theatre | 620 T Street NW (38.91524, -77.02371) | Wikipedia: 1910, restored and reopened 2012 | Whether any old fabric is on show; hours of tours, if any |
| Washington Aqueduct and Dalecarlia works | Palisades (38.9358, -77.1118) | Register listing | A source for what can be seen from the public road |
| Jesse Reno School | Tenleytown (38.9525, -77.0772) | Register row; LEADS.md already has the Fort Reno row | A source opened for the school itself |

## Tips
- choose.py --thinnest drew the District again (63 places by the end of this batch); the Register list pages (central, upper NW, western, Northeast, Southeast) are quick to scan with wiki_raw.py --rows, and one pass at 13 places was enough to find only buildings the earlier batches lacked.
- The Register and Wikipedia coordinates for big sites can fall in the wrong place: check the aerial, then OpenStreetMap through nom.py (it confirmed the Peirce-Klingle house; the St. Elizabeths Center Building had to be found by eye on a look.py picture).
- Museum pages in DC often load times by script; WebSearch results that quote the page, plus the page.py lines, were enough for Decatur House, Belmont-Paul and the National Building Museum.
