# ak_thin_mwrq: Alaska: Interior, Kenai, Nome and the Panhandle
state: Alaska
region: ak
date: 2026-11-23
places: 14
file: data_ak_thin_mwrq.py

## What this batch is
Fourteen places across Alaska (Alaska had 37 before; it was the thinnest region nobody held): Fairbanks, Big Delta, Chicken, Palmer, Hope, the Seward tunnel, Ninilchik, Seldovia, Chitina, Bethel, Nome (the Council City railroad remains), Skagway, Haines (Eldred Rock Light) and Wrangell. Chosen from the Wikipedia National Register lists for each borough (`wiki_raw.py --rows`), then each article read with `wiki_raw.py`. Operator pages read: Alaska State Parks (Big Delta), Chicken Gold Camp, the City of Wrangell, the National Park Service hours page for Klondike Gold Rush. Hours for Chicken's dredge tours and the Wrangell tribal house came only from web search summaries and are not recorded as hours. Not checked: inside of any church, owners of the Seward tunnel and Eldred Rock beyond what the land map showed, parking for most places, whether the Chitina Tin Shop gallery and the Bethel mission house open. Pins were looked at on the aerial: Eldred Rock moved 39 m onto the tower; Seldovia and Bethel kept at site level (the Bethel tile was under cloud); the Seward tunnel is the Register point in forest, area level. Immaculate Conception's lead row is removed: the parish page still gave 403 (not tried again), so its service times are unchecked. Pictures: 11 articles with pictures; Skagway chosen from Commons; none fit Hope or Palmer.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Point Barrow Refuge Station | Utqiagvik, AK | 1889 Revenue Cutter Service building, oldest wooden building on the Arctic coast (Wikipedia; no coordinates in article) | Coordinates (Register 71.29839, -156.77305), owner, access |
| Fort Mears and Dutch Harbor Naval Operating Base | Unalaska, AK (53.888, -166.542) | WWII bases bombed June 1942 (Wikipedia) | Which ruins can be visited, owners |
| Alaska Nellie's Homestead, Brown & Hawkins Store, Seward Depot | Seward area, AK | On the Register list for Kenai Peninsula | Articles not read |

## Tips
- WebSearch returns summaries of third-party pages; the park and operator pages themselves are better read with page.py (dnr.alaska.gov/parks/aspunits/... worked; the nps.gov /places/ guess gave 404 for Skagway).
- The Register coordinate for the Skagway district lies up the White Pass, not in town; geo.py on a street intersection gave the town centre.
