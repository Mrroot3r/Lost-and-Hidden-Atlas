# tn_mwqe: Tennessee: battlefield monuments, houses and old resorts
state: Tennessee
region: tn
date: 2026-11-24
places: 11
file: data_tn_mwqe.py

## What this batch is
Eleven places in Middle and East Tennessee, the thinnest state when claimed (`choose.py --thinnest`): the Hazen Brigade Monument and Oaklands Mansion in Murfreesboro, the Carter House in Franklin, Rattle and Snap near Mount Pleasant, Fort Negley, Union Station and the Ryman in Nashville, the Sam Houston Schoolhouse in Maryville, Tipton-Haynes in Johnson City, the Beersheba Springs resort and the Elkmont Historic District in the Smokies. Sources: Wikipedia, the National Park Service, the Tennessee Historical Commission's state-site pages and Nashville's parks page, all read in the session. Hours came from the commission's and the city's pages (Carter House, Sam Houston, Tipton-Haynes, Fort Negley). Not checked: hours for Oaklands (its page would not open), the Ryman, Union Station and Elkmont; interiors; parking (no `th=` points were set); the Beersheba and Elkmont pins mark the district in woods, not one building. Wikipedia's Carter House point was 1.5 km off, in woods, and the Sam Houston one 200 m off: both were replaced by the address lookup. Wikipedia and OpenStreetMap disagreed with an address lookup by 800 m for the Hazen monument; the OpenStreetMap point is on the walled graveyard.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Red Clay State Historic Park | Cleveland, TN (34.9916, -84.9503) | Last Cherokee council ground before removal; state park page read | Most structures are replicas; what original fabric remains is not known |
| Cades Cove Primitive Baptist Church | Great Smoky Mountains NP (35.5942, -83.8419 area) | Congregation formed 1825, renamed 1841 (Wikipedia, Cades Cove) | Date of the standing building and park access page |
| Murfreesboro square and East Main Street district | Murfreesboro, TN (35.846, -86.390) | Old town centre in start.py with no Atlas place; 85-building district | A Register form for the district |

## Tips
- `tools/page.py` on oaklandsmuseum.org and nps.gov/grsm Elkmont pages failed (the latter 404, the former no connection); the archived copies could not be fetched either.
- The Tennessee Historical Commission pages (`.../state-historic-sites/<slug>.html`) work for carter-house, sam-houston-schoolhouse and tipton-haynes and print the hours cleanly with `page.py --all`.
- `wiki_raw.py` raw text for long articles is full of wiki markup; `-g` with a pattern gives readable sentences.
- Wikipedia coordinates for a house museum can be a kilometre or more off (Carter House): `geo.py` with the street address was right.
