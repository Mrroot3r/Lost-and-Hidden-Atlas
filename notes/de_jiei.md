# de_jiei: Delaware: New Castle County
state: Delaware
region: de
date: 2026-11-18
places: 15
file: data_de_jiei.py

## What this batch is
First pass over New Castle County, Delaware (region `de`, drawn by `choose.py`): 15 places. Mills on the Brandywine and Red Clay Creek (Garrett Snuff Mill, the Auburn Valley/NVF mills, Breck's Mill, Walker's Mill, the Hagley powder yards), the Eastburn–Jeanes lime kilns, the Iron Hill ore pits, Brandywine Springs amusement park, Fort Delaware, the Fort DuPont batteries, the eastern C&D Canal lock at Delaware City, the Ashland covered bridge, and three small brick survivors in the south of the county (Lum's Mill House, the Old Brick Store, the Appoquinimink Friends Meetinghouse). Sources: Wikipedia through `wiki_raw.py`, the "northern New Castle County", "Wilmington" and "southern New Castle County" Register list pages with `--rows`, Register forms through `page.py` on the npgallery `_text` addresses (all had a text layer), destateparks.com pages (they open with `page.py`), Delaware Public Archives marker pages, HMdb, and search-result text for Hagley's hours. Not checked on the ground: anything. Not checked: the Eastburn–Jeanes kilns' owner and where the kilns stand (pin is the road, `prec='area'`); which Auburn Valley mill buildings still stand (`conf='mixed'`); the Old Brick Store's owner; whether Lum's Mill House or the Odessa meetinghouse open; hours for Battery Park; Fort DuPont and Lums Pond fees; which Fort DuPont battery the pin is on. Breck's and Walker's Mill descriptions come from 1971 and 1972 Register forms plus a 2020 magazine line on their present use. Pins that mark only a parking lot or general area: Auburn Valley mills (lot on the old NVF site), Iron Hill ore pits (marker by the trail lot), Brandywine Springs and Hagley (area pins in woods), Eastburn–Jeanes (road).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Iron Hill ore pit (exact spot) | Newark, DE (39.6395, -75.7555, about 100 m NE of the trail lot) | A large hollow on the LiDAR near the Iron Hill Park lot; HMdb marker 155424 says the pits remain clearly visible | A park trail map or visit that names this hollow as a pit, to pin it exactly |
| Bancroft Mills | Wilmington, DE (39.7683, -75.5631) | Wikipedia: burned 2015 and 2016, then demolished; apartments (The Falls) built on the land | Nothing to see: leave out unless something of the mill survives |
| Coffee Run Mission Site | Hockessin, DE (39.7675, -75.65944) | Wikipedia: Father Kenney house burned 2010, barn demolished 2016; the cemetery and a small block chapel remain | Who owns the cemetery and whether visitors are welcome |
| Liston Range Rear Light and Bellevue Range Rear Light | Port Penn (39.5236, -75.64) and Wilmington (39.7203, -75.5179), DE | Standing range lights on the Register lists | Owner and whether they can be seen from a public road |

## Tips
- `look.py` with no arguments crashes (ZeroDivisionError) instead of printing its usage; give it the full arguments.
- `parking.py` and `pincheck.py` disagree about whether the lot on Old Battery Lane, Fort DuPont, is in the state park (parking.py says yes, the first pin check said no); after the pin moved onto the battery both said the park.
- Delaware's Register list is split into "northern New Castle County", "Wilmington" and "southern New Castle County" pages; the plain county title is a redirect to the northern one.
- destateparks.com pages read well with `page.py` (`/History/FortDelaware`, `/History/FortDupont`, `/History/AuburnValley`, `/WhiteClayCreek`, `/Lums`); guessed addresses such as `/LumsPond` answer 404. New Castle County's own park pages (newcastlede.gov) answered 403; the county park rules (dawn to dusk, all year) are printed on its trail-guide PDFs.
