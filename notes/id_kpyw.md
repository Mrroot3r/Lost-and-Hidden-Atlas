# id_kpyw: Idaho: a first scatter from Bear Lake to Sandpoint
state: Idaho
region: id
date: 2026-11-23
places: 17
file: data_id_kpyw.py

## What this batch is
Seventeen places spread over the parts of Idaho the Atlas had nothing in (Idaho had 36 places, all round Boise, the Boise Basin, the Owyhee country and the Silver Valley; it now has 53). Southeast: the Paris Tabernacle, the Hatch House and the Relic Hall/Co-op in Franklin, the Oneida Stake Academy in Preston, Chesterfield townsite, the Standrod House in Pocatello, the Rexburg Tabernacle. Central: the Birch Creek charcoal kilns and Custer ghost town. Magic Valley: Albion Normal School campus, Rock Creek Station, Minidoka. North-central and north: St. Joseph's Mission (Slickpoo), the Monastery of St. Gertrude at Cottonwood, the McConnell Mansion in Moscow, the Sandpoint depot; west: the Intermountain Institute in Weiser. Sources: Wikipedia county Register lists and articles (`wiki_raw.py`), Register forms from NPGallery (`page.py`), and the managing bodies' own pages (Idaho State Historical Society for Franklin and Rock Creek, NPS for Minidoka and St. Joseph's, Forest Service for Custer, the church's Paris Tabernacle page, Latah County Historical Society, the St. Gertrude museum, the Oneida Stake Academy Foundation), with the Idaho Heritage Trust, SAH Archipedia and the Ensign Peak Foundation for the rest. Not checked: hours for the Paris Tabernacle (the church's page says only to contact it), Chesterfield (the foundation's own site would not open), the Rexburg Tabernacle (the city's page sits behind a browser challenge), the Snake River Heritage Center in Weiser and the Sandpoint waiting room; the Forest Service's own page for the Birch Creek kilns was not found, so the road and season there are not checked; whether the Rexburg flood museum is still in the tabernacle basement. Pins: Chesterfield marks a road junction among the town's buildings (`area`); Albion marks the campus generally; St. Joseph's Mission falls on a small building among farm buildings, not confirmed as the chapel; Rock Creek is on the group of old buildings but which is the store was not settled. St. Joseph's Mission lies inside the Nez Perce Reservation, on private land; it is written up because the National Park Service has a visitor page for it (look from the road and read the sign). No place was seen on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Leesburg ghost town | Lemhi County, ID (45.22389, -114.11389) | 1866 gold camp, Register district since 1975; Wikipedia says little remains | A Forest Service or other source on what stands and how to reach it |
| Yankee Fork Gold Dredge | Custer County, ID, near Custer | Dredge in Land of the Yankee Fork State Park, shown by volunteers in summer (only third-party pages found) | The state park's or the dredge association's own page; the park's info page answered 404 |
| Our Lady of Limerick Catholic Church | Glenns Ferry, ID (42.95028, -115.29778) | 1915 white brick church, Register 1982 (Wikipedia) | A parish page with service times |
| Birch Creek kilns' Forest Service page | Leadore, ID | Caribou-Targhee lists the kilns on its "explore the forest" page | The site's own page for road and season |

## Tips
- `page.py` could not read PDFs at first: `pypdf` failed on a missing `_cffi_backend`; `python3 -m pip install --break-system-packages cffi` fixed it.
- `rexburgid.gov` answers `page.py` with a "Client Challenge" page; `visitpocatello.com` with "please wait while your request is being verified"; `chesterfieldfoundation.org` did not connect; `parksandrecreation.idaho.gov/parks/land-yankee-fork/info` is 404.
- `history.idaho.gov/franklin/` and `history.idaho.gov/stricker/` read cleanly with `page.py --all` and give hours, owner and address.
- `nom.py` sometimes answers "HTTP Error 629"; asking again a few seconds later works.
- The ArcGIS geocoder gave PointAddress results for most Idaho street addresses; the Paris and Rock Creek ones were close to but not on the building.
