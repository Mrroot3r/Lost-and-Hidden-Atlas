# ak_nwfc: Alaska: a first scatter, Sitka to Unalaska
state: Alaska
region: ak
date: 2026-11-21
places: 16
file: data_ak_nwfc.py

## What this batch is
Sixteen places spread across Alaska, which before this batch had 21 places, 20 of them round Juneau. Southeast: St. Michael's Cathedral and the Russian Bishop's House in Sitka, Creek Street in Ketchikan, Fort William H. Seward in Haines and the Dyea townsite near Skagway. Southcentral: the Oscar Anderson House and Nike Site Summit at Anchorage, Independence Mine at Hatcher Pass, the Talkeetna Historic District, Holy Assumption Church in Kenai, the Million Dollar Bridge on the Copper River. Kodiak: the Russian-American Magazin (Kodiak History Museum) and Fort Abercrombie. Interior: Goldstream Dredge No. 8 near Fox and Fort Egbert at Eagle. Aleutians: the Church of the Holy Ascension in Unalaska. Facts come from Wikipedia (`wiki_raw.py`) and the managing bodies' pages read with `page.py`: Alaska State Parks, the Park Service (Sitka NHP, Klondike Gold Rush NHP), the BLM, the Orthodox Church in America parish pages, the Kodiak History Museum, Friends of Nike Site Summit, the Talkeetna Historical Society, Gold Dredge 8, the City of Cordova and Alaska DOT&PF. Pins were set from OpenStreetMap points (`nom.py`), an ArcGIS PointAddress, or Wikipedia, and every one was looked at on the aerial; Site Summit and Fort Egbert were moved with `pix.py`. Alaska has no 1 m LiDAR in most of these places. Not checked: any interior; hours for the Russian Bishop's House (the park gives a season, no times), the Oscar Anderson House, Gold Dredge 8 and Fort Egbert's buildings; whether the cathedrals in Kenai and Unalaska open outside services; parking in most towns. The Dyea pin is area precision on the townsite road in trees; the ruins themselves are not mapped. Two pictures were chosen with `photo_find.py` (an 1898 view of Dyea, the Fort Egbert mule barn).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Chatanika Gold Camp | Chatanika, AK (65.11167, -147.48028) | 1925 Fairbanks Exploration Company camp, 13 buildings, NRHP 1979 (Wikipedia) | Present state and owner; whether it still takes visitors |
| Dutch Harbor Naval Operating Base and Fort Mears | Unalaska, AK (53.88806, -166.54194) | WWII bases bombed June 1942 (Wikipedia) | What survives and who manages it; the Aleutian WWII visitor centre's page |
| Transfiguration of Our Lord Chapel | Nushagak, AK (58.94644, -158.49074) | 1904 Orthodox church, abandoned, NRHP 1980 (Wikipedia) | Owner, access (fly-in), whether it still stands |
| Chief Shakes Historic Site | Wrangell, AK (56.46571, -132.38062) | 1940 rebuilt Tlingit community house with original house posts (Wikipedia) | The managing tribe's own page inviting visitors (rule for Native sites) |

## Tips
- Web search results gave titles and links only, no quoted text; read every page with `page.py --all`.
- The Orthodox Church in America parish pages (`oca.org/parishes/OCA-AK-...`) read cleanly and give service times, addresses and parish history for Alaska's Orthodox churches.
- nps.gov hours pages for Sitka NHP are drawn by script and give no times; the park's things-to-do page gives only the season.
- `kodiakhistorymuseum.org/visit` is flagged DRAWN BY SCRIPT by `page.py`, but the 455 characters it returns hold the hours and admission in full.
- `pincheck.py --ids` does not exist: give the ids as bare arguments (`pincheck.py id1 id2`).
- The Wikipedia coordinate for Site Summit falls on bare tundra 650 m from the launch area; OpenStreetMap maps the launch-area ruins.
