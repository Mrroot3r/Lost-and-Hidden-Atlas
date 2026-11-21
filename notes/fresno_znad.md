# fresno_znad: California: downtown Fresno, Kearney Park and the Underground Gardens
state: California
region: ca
date: 2026-11-21
places: 14
file: data_fresno_znad.py

## What this batch is
A "videos" session (PROMPTS.md job 9). The names came from one video, "Old World Fresno California" by Old World Exploration (https://www.youtube.com/watch?v=hlwluCCauT4), whose transcript was read on the owner's computer; the record of all 48 names is source/videos/20250926_hlwluCCauT4.md. The video was a tip only: no fact here rests on it. Added 14 standing places, the first in Fresno: the Bank of Italy, the Fresno Brewing Company office, the Hotel Californian, the Forestiere Underground Gardens, the Hotel Fresno, Kearney Mansion, the Liberty (Hardy's) Theatre, the Rowell Building, the San Joaquin Light and Power building, the Southern Pacific Depot, St. John's Cathedral, the Mattei Building, the Pantages (Warnors) Theatre and the Old Fresno Water Tower. Sources were read with tools/page.py and tools/wiki_raw.py: historicfresno.org (its National Register, Local Register and driving-tour pages, adapted from the nominations), Wikipedia, the Pacific Coast Architecture Database, KVPR, ABC30, a Fresno Bee column, and the own pages of the gardens, the historical society and the cathedral for hours. Pins are ArcGIS PointAddress lookups, each looked at on the aerial; the LiDAR sheet was made but not studied, since every place is a building in a city or a park. NOT checked: anything on the ground; every interior; whether the water tower is open and when (the Arts Council page gives hours only for its Van Ness office); the Warnors Theatre's own page (would not open), so its event and tour times; the present use of the Mattei and Light and Power buildings; how much of the Southern Pacific depot can be seen through the high-speed rail works; garage hours and fees; Kearney Park's hours; Forestiere ticket prices. The brewery pin is an address point among several industrial roofs (prec site); the Kearney Mansion pin is an OpenStreetMap building at the end of the park drive, matched to the house only by the aerial. Red brick is from photographs or sources for 11 places and left "?" for the gardens, the Liberty Theatre and the Light and Power building. Years disagree between sources for the Bank of Italy, the brewery office, the Hotel Fresno, the Mattei Building and the Pantages; each entry gives both and is conf mixed. The Liberty Theatre's condition (roof collapse, gutted interior) rests on one newspaper column.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Santa Fe Passenger Depot | Fresno, CA (36.738333, -119.781944 from the Register list; 2650 Tulare Street) | On the National Register and the Local Register; Wikipedia says trains have used it since 1974 | Not read this session: its article, station hours, a look at the pin |
| Fresno Republican Printery (the Archive on Kern) | Fresno, CA (2130 Kern Street) | 1919, Glass and Butner; the historical society's page offers group tours with the 1919 newspaper press | Tour terms, a pin, a fuller source |
| Holy Trinity Armenian Apostolic Church | Fresno, CA (2226 Ventura Avenue; 36.731667, -119.781667 from the Register list) | 1914, by Lawrence Karekin Cone; Historic Fresno calls it the first church in the United States built in the Armenian tradition | Service times from the parish's page, a look at the pin |
| Warehouse Row | Fresno, CA (702 to 764 P Street) | Three warehouses of 1903 to 1910; the brick parts of the ice company were demolished in 2008 (Historic Fresno tour page) | What stands now, pins |
| Meux Home, Brix Mansion, Physicians Building, Twining Laboratories, Fresno Memorial Auditorium, Tower Theatre | Fresno, CA | All on the Register list and Historic Fresno's driving tour (historicfresno.org/tours/nrhp.htm), which gives addresses and a paragraph each | Not read beyond the tour page; hours for the Meux Home museum |
| Fifteen names from the video left "not checked" | Fresno, CA | Listed in source/videos/20250926_hlwluCCauT4.md: an Advent church, First Methodist Church, the 1896 high school, K Street School, the county orphanage, the federal building, the Forsyth house, the Temple Bar Building, a Sun-Maid hotel, a YMCA, fairground buildings and others; the narrator did not say whether they stand | A source for each; most are probably gone |

## Tips
- historicfresno.org reads cleanly with page.py: `nrhp/<name>.htm` for Register pages (names are in `nrhp/nrhp.htm`), `lrhr/<street>.htm` for the Local Register by street and `lrhr/<number>.htm` for each property; `tours/nrhp.htm` (36,000 characters, use -n 40000) gives an address, a paragraph and driving directions for every Register site in the city.
- Wikipedia gives the Bank of Italy and the San Joaquin Light and Power building the same coordinate; ArcGIS PointAddress lookups landed on every downtown building tried.
- `photo_find.py` candidates near a downtown pin are mostly the neighbours: the Kearney Mansion photograph is tagged with the Register list point, 232 m from the house.
- `publish.sh` stopped once because app files changed on main; after `resync.sh` the first branch name was already taken locally, so the branch is video-hlwluCCauT4a.
- The video channel shows mostly demolished buildings (16 of 48 names here were gone by the narrator's own account), so a video yields fewer standing places than its name count suggests.
