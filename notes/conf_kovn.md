# conf_kovn: Cohoes mills and churches, the Waterford Flight, Halfmoon
state: New York
region: conf, sar
date: 2026-11-19
places: 14
file: data_conf_kovn.py

## What this batch is
Fourteen places, region `conf` drawn at random by `choose.py --state ny`, with two north of it filed under `sar`. Full entries replace three of the first catalogue's one-line pins: Harmony Mills (`was='lm-harmony-mills'`, Mill No. 3 and the mill village, red brick from the National Historic Landmark nomination 78003151), the Van Schaick Mansion (`was='lm-van-schaick-mansion'`, DAR-owned, open by appointment; red brick from a Commons photograph) and the Waterford Flight (`was='lm-waterford-flight-barge-canal'`, Locks E-2 to E-6). From the Spindle City Historic Society's 2023 downtown tour: the 1854 Hayward grist mill (barber shop, 94 Remsen St; this was a LEADS.md row), the 1848 Cataract firehouse, the 1852 Mohawk River (Clifton) Mill, the Methodist church (Vineyard Community Church), the Dutch Reformed church (United Church of Cohoes), St. Bernard's (privately owned) and the First Baptist church. From its Erie Canal tour: Lock 15 with the towpath park, and Locks 9 and 10 in George Street Park (pin on Lock 10, seen as a trench on the LiDAR sheet; the brochure and eriecanal.org disagree on whether Lock 10 survives, so `conf='mixed'`). North: the Ellsworth monument and grave in Hudson View Cemetery, Mechanicville, and the empty Clifton Park Hotel (sold in 2025 for redevelopment). Sources were read with `wiki_raw.py` and `page.py`. Not checked: every interior, church service times, lock hours and the canal season, cemetery hours and owner, the owners of the downtown buildings, and whether First Baptist is still a church. The seven downtown entries rest on the one historical-society brochure. Brick is '?' for the downtown buildings and the Ellsworth monument: no picture of them was opened.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cohoes Waterworks pump house | Cohoes, NY (near the falls, Harmony Mills district) | Spindle City Harmony Mills tour (2023): pump house begun 1857, still working, built on a lock of the original Erie Canal | Where it is (not found in OpenStreetMap by name) and whether it can be seen from a public way |
| Harmony Mills Office and Sunday School | Cohoes, NY (Harmony Mills district) | Spindle City tour and the NHL nomination: 1854 company office with a millworkers' library upstairs | Exact building; mentioned inside the harmony-mills-cohoes entry for now |
| William Moore House (former YWCA) | 135 Mohawk St, Cohoes, NY | Spindle City downtown tour: red brick Second Empire house of about 1874 with its iron fence, YWCA from 1892 through the 1980s, now a design studio | A second source; a pin check |
| Church Hill Historic District | Halfmoon, NY | Saratoga County Register list: listed (100006512), no coordinates; the Wikipedia title tried does not exist | Any source on what is there and a coordinate |

## Tips
- `brick.py look <id> <picture address>` works for a place that is only in the workspace build, but not for an `lm-` id once a new entry with `was=` replaces it: look the new id up instead. `Special:FilePath/<file>?width=800` fetched where the plain file address got HTTP 429.
- `start.py` lists the `lm-` pins well; three of them in Cohoes and Waterford were still waiting for full entries.
