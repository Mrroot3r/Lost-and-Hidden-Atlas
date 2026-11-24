# sk_rbnw: Saskatchewan: Eastend, Weyburn, Fort San, the east and the north
state: Saskatchewan
region: sk
date: 2026-11-24
places: 10
file: data_sk_rbnw.py

## What this batch is
The fourth Saskatchewan batch: ten places spread over the southwest (Eastend), south and southeast (Lang, Weyburn), the Qu'Appelle valley (Fort San), the east (Melville, Canora, Pelly), the centre (Muenster) and the north (Cumberland House, Prince Albert National Park). Picked from Wikipedia's list of historic places in Saskatchewan and each read in the Canadian Register of Historic Places (historicplaces.ca, ids in the links). Access and hours came from the City of Weyburn's museum page, Parks Canada (Fort Pelly, Grey Owl's Cabin), stegnerhouse.ca, Tourism Saskatchewan and the National Trust for Canada's Fort San page. Not checked: anything on the ground, parking (said so in each entry), the fee at Fort Pelly, day-use rules and park fees for Grey Owl's Cabin, whether Fort San's four buildings still stand (newest source is 2015), the inside of every church and the Muenster Hotel's hours. Pins marked only as an area: Cumberland House (the park, not the magazine), Grey Owl's Cabin (the lake's mapped point; the cabin is on its north shore, not found on the aerial), Fort Pelly (cellars not visible on the aerial; Parks Canada's own point is 8 km from the register's). Pictures: Stegner House, Muenster Hotel and Grey Owl's Cabin got one; Commons had nothing for the rest.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cattle Barn, Indian Head Agricultural Research Farm | Indian Head, SK (register point 50.5331, -103.656 is a crossroads) | Register id 18717: gambrel-roofed 1912-14 barn, federal heritage building | The barn's true position; visitor access |
| Kristiania Lutheran Church | Atwater, SK (register point 50.7783, -102.226 is in a marsh) | Register id 6611: 1920 wood church, services ended early 1980s | The church's true position |
| Arcola Court House | 619 Souris Avenue, Arcola, SK (register point on a road) | Register id 7504: 1908-09 brick-faced court house by Storey and Van Egmond | Which building on the aerial it is |
| Yorkton Court House | 29 Darlington Street East, Yorkton, SK (register point in a house block) | Register id 2872: 1919-21 Beaux-Arts court house, Tyndall Stone and Claybank brick | True position; public access to the stained glass inside |
| Fleming Lake of the Woods Grain Elevator | Fleming, SK | Register id 12141: one of the oldest prairie elevators; burned February 2010 | Nothing standing; not added |
| Biggar Railway Station | Biggar, SK | Grand Trunk Pacific station of 1909, demolished 2018 (Wikipedia) | Nothing standing; not added |
| Battle of Cut Knife Hill | Poundmaker Cree Nation, SK | Register id 18923: no visible remains; Poundmaker's grave, monument and a small museum | Whether the nation invites visitors, on its own page |

## Tips
- historicplaces.ca pages open with page.py --all; the Wikipedia list's idf/idp/idm fields hold the id for each row, so build the page address from them.
- Register points were off the building at four of fourteen places (Fort San by 250 m, Indian Head, Atwater and Arcola by more); the Wikipedia list gives Grey Owl's Cabin the coordinates of the park townsite, 40 km from Ajawaan Lake.
- Web searches for Saskatchewan places returned page titles only; managers' pages read with page.py gave the hours.
- app_smoke.js tests the Android copy; the phone-size check of dist/web is tools/smoke.js, served with python3 -m http.server -d dist 8766 and the address http://localhost:8766/web/.
