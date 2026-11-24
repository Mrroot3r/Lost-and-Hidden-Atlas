# fortwayne_cukl: Fort Wayne, Indiana: courthouse, churches and old downtown
state: Indiana
region: in
date: 2026-11-24
places: 12
file: data_fortwayne_cukl.py

## What this batch is
The first Atlas places in Fort Wayne: 12 standing buildings, ten downtown (Allen County Courthouse, Old City Hall / History Center, the Cathedral of the Immaculate Conception, St. Paul's Lutheran, Engine House No. 3 / Firefighters Museum, the Embassy Theatre and Indiana Hotel, Baker Street Station, Lincoln Bank Tower, the Masonic Temple) plus St. Peter's Church on the south side, the General Electric works now Electric Works on Broadway, and North Side High School. The names came from one Old World Exploration video, worked as job 9 (record: `source/videos/20241018_nhecz_gOrFI.md`); the video was a tip only. Sources: Wikipedia articles (`wiki_raw.py`), National Register forms on NPGallery (`page.py`: City Hall, Engine House No. 3, Embassy, Pennsylvania station, St. Peter's Square), the cathedral's, St. Peter's and St. Paul's own pages for service times, the Firefighters Museum's own page, Indiana Landmarks and the National Trust on Electric Works. Not checked: the History Center's and the courthouse's own sites answered 403, so their hours are as a web search quoted those sites (said so in the access notes); the Firefighters Museum's page gives no hours (`?`); Electric Works has no hours on a page of its own (`?`); the Embassy's two pages disagree on box office closing time (5 or 6 p.m.; `conf='mixed'`). Interiors not checked except where a Register form or Wikipedia describes them. Downtown parking given only in general terms. Pins: St. Peter's moved about 60 m from a parking lot onto the church, Engine House No. 3 about 15 m onto the roof; the Masonic Temple is pinned from OpenStreetMap (216 E. Washington Blvd.) because the Register list point is about 1 km west.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Vincent Villa (former Catholic orphanage) | Fort Wayne, IN, 2000 N. Wells St. (41.0931, -85.1442) | National Register district (94000587): campus of 1925–1944 buildings, later the YWCA; form read | Current owner and use, and whether anything can be seen from the street |
| Three Rivers Filtration Plant (city waterworks, 1931) | Fort Wayne, IN | Named in the video only | Any source opened; owner page |
| Scottish Rite Center | Fort Wayne, IN | Named in the video only; no Wikipedia article under the titles tried | A register or owner source and the address |
| Concordia College old campus | Fort Wayne, IN | Named in the video only | Which buildings stand, and a source |
| Fort Wayne Club, Elks Temple, First Baptist, First Methodist, Trinity English Lutheran, Lyric and Temple theaters, Wayne Hotel, Carnegie library, Lincoln National Life building, Hoagland School | Fort Wayne, IN | Named in the video; rows "not checked" in the record | Whether each stands, and a source |

## Tips
- `allencountycourthouse.org` and `fwhistorycenter.org` answer 403 to `page.py`, and the Internet Archive copy of the History Center could not be fetched either.
- `fwembassytheatre.org` sub-pages (tours, `?p=130`) answer 404 to `page.py`; the home page reads but lists only shows.
- The Wikipedia search API refused quick repeated queries (empty answers) after two or three; space them out.
- The National Register list point for the Masonic Temple (91000273) is about 1 km off; OpenStreetMap has the building.
