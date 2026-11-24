# bc_jnpm: British Columbia: a first scatter from Victoria to the Peace
state: British Columbia
region: bc
date: 2026-11-21
places: 19
file: data_bc_jnpm.py

## What this batch is
Nineteen places spread across British Columbia, claimed with `choose.py --thinnest` (BC had 17 places, all in the West Kootenay): on Vancouver Island the Fisgard Lighthouse, Fort Rodd Hill, Craigflower Manor, the Nanaimo Bastion and McLean Mill; round Vancouver Fort Langley, the Gulf of Georgia Cannery and the Britannia Mines concentrator; in the Fraser Canyon the 1863 church at Yale and the Alexandra Bridge; on the Cariboo road Hat Creek Ranch, Cottonwood House, Barkerville and the Quesnel Forks ghost town; in the north Fort St. James, the North Pacific Cannery at Port Edward and the 1942 Kiskatinaw curved wooden bridge on the old Alaska Highway; in the east Fort Steele and the Loop Brook stone piers of the 1885 CPR line in Rogers Pass. Facts come from the Canadian Register statements (historicplaces.ca, read with a short script that pulls the `PlaceLatitude`/`PlaceLongitude` meta tags, the construction date, the statement and the character-defining elements), Wikipedia (`wiki_raw.py`), and the managing bodies' pages read with `page.py` (Parks Canada for Fort Rodd Hill/Fisgard, Fort Langley, Fort St. James and Glacier National Park; BC Parks for Alexandra Bridge and Kiskatinaw; Barkerville; Fort Steele; Nanaimo Museum; McLean Mill; North Pacific Cannery; the Victoria Highland Games page for Craigflower tours). Hours NOT checked (hours='?'): Gulf of Georgia Cannery, Britannia Mine Museum, Hat Creek Ranch, Cottonwood House, the Yale church, North Pacific Cannery (only "closed Mondays in May, June and September"). Craigflower tour dates are the 2025 ones; Fort Steele only fall hours; Fort Rodd Hill's page gives two sets of hours without naming the seasons. Pins moved off the Register point onto what the aerial shows: Britannia (Register point is 28 km off, in North Vancouver), Cottonwood House, Barkerville, Fort St. James, Fort Steele, Craigflower Manor (OpenStreetMap building points or `pix.py`). Loop Brook is an area pin on the trail; the piers were not picked out on a snowy aerial. Parking not checked on the ground anywhere; no lot mapped for Cottonwood House, Kiskatinaw or Fort Rodd Hill (OpenStreetMap parking aisles there sit under trees). Red brick: Fisgard 'some' (red brick keeper's house, from the Register's photographs); Fort Rodd Hill, Craigflower, Barkerville and Fort Steele '?'; the rest 'no' from the Register's descriptions of wood, log, stone, steel and concrete. Whether a national park pass is needed at Loop Brook was not checked. Nothing was seen on the ground.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Glacier House ruins | Rogers Pass, Glacier National Park, BC, near Illecillewaet campground | Parks Canada itinerary page: guided walks pass "the stone ruins of western Canada's first mountain resort hotel" | A pin on the ruins and a source on what is left |
| Fort Rodd Hill batteries as separate pins | Colwood, BC (OpenStreetMap leads: Upper, Lower and Belmont batteries, Golf Hill Battery) | Register listings for the Lower Battery casemate barracks (4296), canteen (4346), battery commander's post (4348) | Separate entries would need each battery pinned; Golf Hill Battery and McLoughlin Point need an owner |
| Chee Kung Tong building, Barkerville | Barkerville, BC (Register id 11971) | A National Historic Site of its own inside Barkerville | Could be its own entry with the building pinned |
| Old Yale Wagon Road | Yale, BC (Register id 25189) | Listed on the Register | Not read |

## Tips
- historicplaces.ca place pages carry their coordinate in `<meta name="PlaceLatitude">` and `<meta name="PlaceLongitude">`; reading those is more reliable than grepping numbers. One Register coordinate (Britannia Mines Concentrator, id 7561) is 28 km off, in North Vancouver: look at every one.
- Several Register points fell on parking lots or in trees beside the place (Barkerville, Cottonwood House, Fort St. James 570 m off); `nom.py "<site name>"` gave OpenStreetMap points on the right building for Fort St. James, the Nanaimo Bastion, the Yale church and Craigflower Manor.
- hatcreekranch.ca, the old Hat Creek Ranch address that search results still give, now carries gambling spam; the ranch's current site historichatcreek.ca did not answer `page.py`.
- Parks Canada hours pages (`parks.canada.ca/lhn-nhs/bc/<site>/visit/heures-hours`) read well with `page.py`; the Gulf of Georgia Cannery's (`.../georgia/visit/...`) answered 404.
- BC Parks pages (`bcparks.ca/<park>-park/`) read in full with `page.py --all` and say who maintains a structure (the Alexandra Bridge is the Ministry of Transportation's, not the park's).
