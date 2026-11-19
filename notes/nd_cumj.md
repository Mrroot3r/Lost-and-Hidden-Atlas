# nd_cumj: North Dakota: Bismarck, Mandan and the Missouri villages
state: North Dakota
region: nd
date: 2026-11-19
places: 18
file: data_nd_cumj.py

## What this batch is
Eighteen places round Bismarck and Mandan (Burleigh and Morton counties), with the Bismarck-Deadwood stage road south through Flasher to the Cannonball Stage Station in Grant County. Region drawn at random by `choose.py` (nd). Earthlodge towns and forts as traces (On-A-Slant, Huff, Double Ditch, Menoken, Chief Looking's, Fort Rice, Fort McKeen and the Fort Abraham Lincoln cavalry post), stage-road traces, the Steamboat Warehouse marker, and standing buildings (Camp Hancock, the Former Governors' Mansion, the Northern Pacific depot, the Patterson and Lewis and Clark hotels, the State Capitol, St. John's church in Hebron). Facts come from the SHSND site pages (`history.nd.gov/historicsites/<slug>/index.html`, read in full with `page.py --all`), the ND Parks page for Fort Abraham Lincoln, Bismarck Parks' Chief Looking's page, OMB's 2025 Capitol tour notice, National Register forms (NPGallery `_text`), HMdb marker texts and Wikipedia. Brick for the Patterson, Lewis and Clark Hotel and Governors' Mansion is from the Wikipedia photographs (`brick.py look`); the Custer House is left `?`. Not checked: anything on the ground, interiors (unless a form describes them, dated), parking at the rural SHSND sites (none is mapped: Huff, Double Ditch, Menoken, Fort Rice, Cannonball, the Flasher marker), the Fort Abraham Lincoln entrance fee amount, and the depot's and Lewis and Clark Hotel's present use. The Flasher stage-trail pin is the roadside marker, not the ruts (prec area). The date of the CCC blockhouses at Fort McKeen differs between sources (1933, 1934, 1935: conf mixed).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Lincoln (1895 post, WWII internment camp) | Bismarck, ND (46.77232, -100.76437, Wikipedia) | Post of 1895–1900s, internment camp 1941–45; now United Tribes Technical College, with the Snow Country Prison memorial dedicated 2025 (Wikipedia, uttc.edu) | Which original buildings stand, and whether visitors may walk the campus; the NPS places page guessed was 404 |
| Mandan Northern Pacific depot and beanery | Mandan, ND, Main Street | Mandan Historical Society has pages on both (search results) | mandanhistory.org refused `page.py` (connection errors); dates and condition unread |
| Old Mandan High School | Mandan, ND (46.83019, -100.89623) | 1917 and 1924 Collegiate Gothic buildings, NRHP 2017 (Wikipedia) | Present use and access; only Wikipedia read |
| Bismarck-Deadwood stage ruts | near Flasher, ND, by the ND 21 marker | SHSND says a few ruts are found near the marker | A position for the ruts themselves |
| Ingersoll School, Former McLean County Courthouse | Washburn, ND | On the state Register list | Not read; outside the two counties worked |

## Tips
- `wiki_raw.py --rows` for "National Register of Historic Places listings in Morton County, North Dakota" redirects to the whole-state list; Burleigh County has its own page. Grep the state list's rows for the town names.
- SHSND site pages read fully with `page.py --all`; the slugs are not the obvious ones (Former Governors' Mansion is `fgm`, Fort Rice is `rice`, Cannonball Stage Station is `cannonballss`, Bismarck-Deadwood Stage Trail is `bdst`). The full list of slugs is in the drop-down on `history.nd.gov/historicsites/index.html` (grep the cached page for `value="/historicsites/`).
- HMdb nearby lists round Fort Abraham Lincoln, Bismarck and Fort Rice gave positions for nearly every site in two requests; the Commanding Officer's Quarters marker sits by the visitor centre, about 750 m from the Custer House, which OpenStreetMap maps as a building (`osmnear.py ... buildings`).
- The pin check's LiDAR sheet shows the earthlodge pits at On-A-Slant, Huff, Double Ditch and Chief Looking's plainly, though they are open prairie: worth running even where there are no trees.
- `publish.sh` stopped once because another batch merged a few minutes after setup; `resync.sh` then a new branch name worked.
