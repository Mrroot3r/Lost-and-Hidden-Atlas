# adk_iqcx: Hamilton County: Speculator, Piseco, Blue Mountain and Raquette lakes
state: New York
region: adk
date: 2026-11-21
places: 16
file: data_adk_iqcx.py

## What this batch is
Sixteen standing places in Hamilton County, New York (region `adk`, drawn at random by `choose.py --state ny`, which offered Speculator); `start.py` found only Griffin within 30 km of Speculator. Four fire towers on DEC trails (Blue Mountain, Pillsbury, Wakely, Snowy), the Log Hotel at the Adirondack Experience, the log Church of the Transfiguration, Great Camp Sagamore (replaces `lm-great-camp-sagamore` with `was=`), Camp Pine Knot and St. William's on Long Point (both seen by boat), CCC Camp S-90 (private camp, view from the road), Speculator's 1894 town hall museum and Grace Methodist Church, the Hamilton County courthouse and 1848 stone jail, Wells Baptist Church (now a private venue), the Riley Tavern museum and the Irondequoit Inn at Piseco. Sources: Wikipedia by `wiki_raw.py`; DEC unit pages (Blue Mountain Wild Forest, Jessup River Wild Forest, Moose River Plains Complex) for trail lengths; the Adirondack Experience, Great Camp Sagamore and Town of Lake Pleasant pages for hours; the Diocese of Albany page; the CCC camp's Register form on NPGallery; HMdb markers; two Adirondack Life articles. Not checked: anything on the ground; church service times (no own page found for Transfiguration or Grace Methodist); the Piseco museum's hours come from Hamilton County tourism, not the society's own page; the Irondequoit Inn's season; parking at Sagamore, the town hall and the Piseco museum. The Wells church pin marks only the street (`prec='area'`): the church was not picked out on the aerial. The fire tower pins are the mapped summits; the Wikipedia coordinates for Wakely and Snowy sit at the trailhead lots, kilometres away. Dates that disagree are given both ways (the Transfiguration church: 1855, 1881 or 1885; the town hall's library years; the jail 1848 or 1849; the Wells church closing 1949 or 1950).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Nehasane station | Lake Lila, Long Lake, NY (William C. Whitney Wilderness) | Wikipedia's Lake Lila article says the station that served Webb's Forest Lodge still stands; Forest Lodge was razed in 1979 | Its position, and whether the public may walk to it from the Lake Lila lot (the rail corridor's status) |
| Pioneer Bridge marker | Eagle Nest Road, Blue Mountain Lake, NY (43.85222, -74.47056) | HMdb 96914: a plaque under the bridge put up in 1891 by W. W. Durant to his father; seen only by boat from underneath | A source for the bridge itself (date, builder) and whether it is the 1891 bridge |
| Camp Uncas | Lake Mohegan, Raquette Lake, NY (43.74472, -74.64806) | Wikipedia: Durant's second Great Camp, sold to J. P. Morgan in 1896, private since 1975 | Any public way to see it; private land |
| Echo Camp, Dollar Island Camp, Camp Taiga, Whelan Camp | Raquette Lake, Fourth Lake (Inlet), Long Lake | Register-listed private camps (Wikipedia) | A public view point; all private |
| Gate House Ruins and Sugar Shack Ruins | Near Sagamore Lake (43.77245, -74.63811 and 43.7713, -74.61888) | OpenStreetMap ruin points (`start.py`) | Any source saying what they were and who owns the ground |
| Methodist church, Indian Lake | Indian Lake hamlet, NY | Wikipedia's Grace Methodist article says the 1903 Indian Lake church has the same Price plan and steeple | Its own source and position |

## Tips
- The Register list's coordinates for the Wakely and Snowy towers (and the Wikipedia infoboxes) sit at the trailhead lots, 3 to 4 km from the summits; `nom.py "<Mountain>, New York"` gives the peak.
- DEC unit pages (`dec.ny.gov/places/<unit-name>`) give trail lengths and climbs for every fire tower; `page.py -g` returned nothing on them, but `page.py --all -n 200000` into a file and a grep worked. The William C. Whitney page is `william-c-whitney-wilderness-and-round-lake-wilderness`.
- The Town of Lake Pleasant's history page (`lakepleasantny.gov/our-history/`) gives the historical museum's hours near its end and a dated timeline of Speculator buildings.
- Hamilton County's tourism site (`experienceouradirondacks.com`) lists the small historical societies with hours where their own pages could not be found.
- HMdb nearby lists round Speculator and Piseco turned up the Riley Tavern museum, which no Register list or article names.
