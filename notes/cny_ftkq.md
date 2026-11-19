# cny_ftkq: Madison County, NY: Peterboro, Cazenovia, Oneida and the Chenango Canal summit
state: New York
region: cny
date: 2026-11-19
places: 19
file: data_cny_ftkq.py

## What this batch is
Nineteen places in Madison County, New York, drawn at random by `choose.py --state ny` (region `cny`, which offered Peterboro); the Atlas had only the Chittenango Landing dry docks within 20 km of Peterboro. Peterboro: the Gerrit Smith Estate (land office, barn, laundry, the burned mansion's site) and the 1820 Smithfield Presbyterian Church (National Abolition Hall of Fame). Cazenovia: Lorenzo State Historic Site and the 1894 Lehigh Valley depot. Chittenango: the red brick Chittenango Pottery and St. Paul's Carpenter Gothic church with the lateral canal basin marker. Canastota: the Canal Town Museum. Oneida: the Oneida Community Mansion House and Cottage Lawn. Morrisville: the old county courthouse (Madison Hall). Hamilton: Hascall Hall at Colgate. Bouckville: the Chenango Canal summit level and towpath trail (aqueduct abutments at Oriskany Creek, Lock 76) and the curved cobblestone Coolidge Stores. Hill towns: the Seventh Day Baptist church in DeRuyter, the Spirit House in Georgetown (private, view only), the Muller Hill mansion site in the DEC state forest, the Nelson Welsh church, Fenner Baptist church and the Clockville schoolhouse. Sources: Wikipedia raw text (`wiki_raw.py`, including the county Register list), HMdb nearby lists and marker pages, managing bodies' pages read with `page.py` (State Parks, DEC, gerritsmith.org, NAHOF, oneidacommunity.org, mchs1900.org, chenangocanal.org, canastota.gov, tromptown.github.io), the Spirit House Register form, courthouses.co and a 2020 blog for the courthouse. Not checked: anything on the ground; interiors of most churches; owners and use of the Cazenovia depot, Chittenango Pottery, the Welsh, Fenner and Clockville buildings; parking at Peterboro, Oneida and Hamilton; NAHOF's season hours (closed for the season when read). Pins: the canal entry is the Cottage Museum trailhead, not the aqueduct; the Spirit House pin is an area pin on the right side of Route 26 in Georgetown (the Register point is 10 km south, in Otselic State Forest); the Muller Hill pin is the roadside marker, not a ruin; the Clockville schoolhouse pin was moved onto a building not confirmed to be the school. Brick from Wikipedia photographs opened with `brick.py look` (Pottery, Mansion House, Hascall, NAHOF) or from the building's material in Wikipedia or the Register form.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Oneida Lake Congregational Church | Oneida Lake hamlet, Town of Sullivan, Madison County, NY (Register point 43.15778, -75.82917 falls in a yard) | Wikipedia: gathered 1814, post-and-beam meeting house of 1824 with Greek Revival door frame and two-tier tower, additions 1922 and 1998; Register 2006 | The building's position (no address found; the geocoder and OpenStreetMap had nothing) |
| Chenango Canal aqueduct abutments and Lock 76 | Oriskany Creek at Canal Road, north of Bouckville, NY (Canal Road bridge 42.90883, -75.52589 is a guess) | chenangocanal.org: hand-cut stone aqueduct abutments in excellent condition, Lock 76 just north, room for 2 or 3 cars on Canal Road past the creek | A coordinate for the abutments seen on the aerial or LiDAR; now covered only in the towpath entry's text |
| DeRuyter freight depot | Railroad Street, DeRuyter, NY (HMdb 223326 at 42.75965, -75.89051) | HMdb marker: built 1871 by the Midland Railroad, moved 300 yards east in 1880 by the Lehigh Valley; the ticket station burned in April 1970 | Whether the freight house still stands, and its owner |
| Belmont Powder Mill site | 3248 East Road, New Woodstock, NY (HMdb 268400 at 42.88003, -75.84681) | Pomeroy marker: mill set up 1888 by J. D. Griswold, ended by an explosion in October 1898 heard for 50 miles | Anything left to see, and who owns the ground |
| Morse Mill Dam and Wood, Tabor & Morse engine works | Eaton, NY (HMdb 145690 at 42.84928, -75.61948; 145683 at 42.85041, -75.61104) | State marker: Joseph Morse began developing Eaton Brook water power in 1796, an industrial centre until 1896; WTM made steam engines 1852–1893 | Whether the dam or any works survive |
| Morrisville Engine House | Morrisville, NY (Register 42.8987, -75.6420, ref 100005481) | Listed on the Register; NPGallery returns an empty form | Any source on its date, material and use |

## Tips
- The Register list point for the Spirit House, Georgetown (06000160) is about 10 km south of the hamlet, in Otselic State Forest; the form says east side of Route 26 just south of the Route 80 corner.
- Many Madison County Register articles exist under names `wiki_raw.py --rows` did not show as "article:" (Old Madison County Courthouse, Canal Town Museum, Nelson Welsh Congregational Church, Fenner Baptist Church, Cottage Lawn, Coolidge Stores Building, Lenox District No. 4 Schoolhouse, "Old Biology Hall" redirecting to Hascall Hall): try the row name.
- NPGallery returned the placeholder for nearly every older Madison County form; 06000160 and 100000894 read.
- The Canal Town Museum's own site would not connect; canastota.gov/?p=58 has its hours and fees.
- nom.py gave HTTP 429 after a few calls; the ArcGIS geocoder (`geo.py`) found every street address used here.
