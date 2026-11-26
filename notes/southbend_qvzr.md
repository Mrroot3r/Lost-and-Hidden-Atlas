# southbend_qvzr: South Bend, Indiana: downtown, the west side and Notre Dame
state: Indiana
region: in
date: 2026-11-26
places: 16
file: data_southbend_qvzr.py

## What this batch is
The first Atlas places in downtown South Bend and at Notre Dame beyond Copshaholm: 16 standing buildings. Downtown: the Old (second) and the domed third St. Joseph County courthouses, the Citizens Bank, J.M.S., Knights of Columbus and LaSalle Hotel buildings, the Morris Performing Arts Center (Palace Theater), the former First Church of Christ, Scientist (now the Civic Theatre) and the North Pumping Station in Leeper Park; on the west side St. Patrick's, St. Paul's Memorial and St. Adalbert churches and the Studebaker Administration Building; at Notre Dame the Main Building, the Basilica of the Sacred Heart and Washington Hall. The names came from one Old World Exploration video, worked as job 9 (record: `source/videos/20250516_DwVktNBQRwQ.md`); the video was a tip only. Sources: Wikipedia (`wiki_raw.py`), National Register records and forms (`form.py`), the Indiana nomination PDF for St. Adalbert, Notre Dame's Building South Bend survey, the Near West Side neighbourhood's church page, Visit South Bend's Studebaker-Bendix trail page, and the own pages of the Basilica, the Morris Center, the Civic Theatre, St. Paul's and the St. Patrick and St. Hedwig parish, all read with `page.py`. Pins are address points (ArcGIS geocoder) or Wikipedia coordinates, checked on the aerial; three were moved (the third courthouse, St. Adalbert, the Basilica). The pin check was run without `--lidar`: every pin is a city building. NOT checked: present use and owners of Citizens Bank, LaSalle, J.M.S., Knights of Columbus and the Studebaker Administration Building; the Civic Theatre building's date and architect; St. Adalbert's Mass times (taken from a web search quoting the parish page, which `page.py` read as empty); St. Adalbert's pin (moved onto the building the aerial suggests is the church, prec site); red brick for eight places; Notre Dame tour times.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Farmers Trust building | South Bend, IN | Named in the video as standing; the Register lists a Farmers Security Bank (85001210) at 41.675278, -86.251944 | Whether the two are one building, and a source |
| Studebaker fountain | South Bend, IN | Named in the video | Where it is now and whether it stands |
| St. Joseph Hospital, old building | South Bend, IN | Named in the video (two front turrets) | Whether it stands |
| Saint Mary's College campus | Notre Dame, IN (41.70674, -86.25703) | Wikipedia: on this site since 1855 | Which old buildings stand and visitor access |
| St. Hedwig Church | 331 S. Scott St., South Bend, IN | 1881 Renaissance Revival church with stained glass (westwashington.org); same parish as St. Patrick's | A pin check and a second source |
| Former First Presbyterian Church (Ambassadors for Christ) | 302 W. Washington St., South Bend, IN (Register 85001211) | 1889 Richardsonian Romanesque by J. P. Bailey (westwashington.org; Wikipedia article exists) | Not reached |

## Tips
- `stadalbertparish.org` reads as one character to `page.py` (drawn by script); the web search result quoted its Mass times.
- Notre Dame's Building South Bend survey (`buildingsouthbend.nd.edu/properties/nd-sb-NNNNN/`) gives date, style, architect and materials for downtown and near-west-side buildings, and reads well with `page.py`; its own search box does not, so find the property number with a web search.
- The Register list point for the Old Courthouse (70000007) is about 3 km south of the building; the address 112 S. Lafayette Blvd. lands on it.
