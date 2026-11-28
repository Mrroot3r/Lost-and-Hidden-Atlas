# tampa_aosf: Tampa, Florida (downtown and Ybor City)
state: Florida
region: fl
date: 2026-11-28
places: 12
file: data_tampa_aosf.py

## What this batch is
Twelve standing buildings in downtown Tampa, Ybor City, Tampa Heights and across the river on Kennedy Boulevard, taken from the names in one Old World Exploration video ("Old World Tampa"; the record is source/videos/20230812_kv4fTv-adzM.md, 34 names, 15 of them not checked). Added: Sacred Heart Catholic Church, the 1915 City Hall, the 1905 federal courthouse and post office (now a hotel), El Círculo Cubano, El Centro Español de Tampa, the Tampa Theatre, Tampa Union Station, the old Hillsborough County High School, Masonic Temple No. 25, the 1913 Lafayette Street (Kennedy Boulevard) bascule bridge, the Ybor City Historic District and the First Baptist Church. Sources: Wikipedia articles and the Tampa Register list (wiki_raw.py), the Park Service's records and forms (form.py), the parish, church, station and theatre pages for hours, Great American Stations, AIA Tampa Bay's architecture tour. Nothing was checked on the ground. Not checked: office hours at City Hall, the hotel's front desk, any opening of the Cuban Club or the Masonic Temple, what restaurant is now in El Centro Español, and red brick at five places (no source or picture was opened that settles it). The cornerstone words at the high school were read from a Commons photograph. Downtown parking is metered streets and private lots; no `th=` was given except where a page names parking in the access note.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Centro Asturiano de Tampa | Tampa, FL (27.962, -82.4509) | 1914 clubhouse by M. Leo Elliott, Register 74000631; its hospital closed 1990 (Wikipedia) | Owner's page and opening hours; not named in the video, so left for a places session |
| El Centro Español of West Tampa | Tampa, FL (27.961389, -82.483333) | Register 74000632; the society's later clubhouse (Wikipedia, El Centro Español de Tampa article) | Its own source read and a pin check |
| Ybor City Museum State Park | Tampa, FL (27.962, -82.439) | In the Ferlita Bakery; brick oven survived a 1922 fire (Wikipedia) | Park hours: state park pages answer 403 |
| Old Union Depot Hotel, Floridan Hotel, S. H. Kress Building | Downtown Tampa | On the Tampa Register list (the depot hotel marked demolished) | Not read |

## Tips
- `W('Title')` from data_ma already returns a whole `[label, url]` link: wrapping it as `['Wikipedia', W(...)]` builds fine but makes `photo_find.py new` crash in `photos.title_of` with "expected string ... got 'list'".
- tampatheatre.org answers 403 to `page.py`; the web fetch tool read its Know Before You Go page (`?p=187`).
- The ArcGIS address lookup and the Register list disagreed by about 1 km for 2704 North Highland Avenue (the old high school); the aerial showed the Register point on the building.
