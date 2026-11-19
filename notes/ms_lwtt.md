# ms_lwtt: Mississippi river country: Port Gibson, Grand Gulf, Rodney and the Natchez Trace
state: Mississippi
region: ms
date: 2026-11-19
places: 18
file: data_ms_lwtt.py

## What this batch is
Eighteen places in Claiborne and Jefferson counties and along the south end of the Natchez Trace Parkway into Adams County: the river ghost towns of Grand Gulf (park, Fort Cobun, the Sacred Heart church moved from Rodney) and Rodney (the town and its 1832 Presbyterian church); Oakland Chapel and Bethel church near Alcorn; in Port Gibson the First Presbyterian church (the gold hand), Temple Gemiluth Chessed and the Samuel Gibson House; the Shaifer House on the battlefield; on the Trace, Rocky Springs, the Sunken Trace, Mount Locust and the Elizabeth Female Academy ruins; Historic Jefferson College and Longwood near Natchez; Christ Church at Church Hill. Sources were read with `wiki_raw.py`, HMdb marker pages and nearby lists through `page.py`, NPS places and news pages, the Grand Gulf park pages, SAH Archipedia, MDAH, Natchez Pilgrimage Tours, natchez.org, the Natchez Democrat and EPConnection. Not checked: nothing on the ground; Mount Locust's current hours and whether the house (closed for stabilizing in September 2017) has reopened; the Shaifer House's hours; Longwood's hours and fees; the Grand Gulf fee; road conditions into Rodney (it floods); whether Bethel, Rodney Presbyterian and Port Gibson's churches open to visitors; the Samuel Gibson House's present use. Pins that do not sit on the thing itself: Christ Church (on highway 553, about 70 m from a building that may be the church), Samuel Gibson House (on trees beside the house), Fort Cobun (the marker, in woods), Elizabeth Female Academy (the OSM ruins point; the wall is hidden by trees). Brick came from Wikipedia text (Rodney church, the temple), SAH Archipedia (stucco over brick at First Presbyterian and Christ Church) and pictures opened with `brick.py look` (Longwood, Jefferson College, the Elizabeth ruin); Oakland Chapel's only picture is black and white and is left '?'.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Springfield Plantation | near Fayette, MS (marker 31.75229, -91.18925; Wikipedia 31.74611, -91.19306) | Built 1786–1791, early full colonnade; claimed site of Andrew Jackson's 1791 wedding (disputed); tours stopped after the caretaker died in 2008 (Wikipedia) | Owner and whether any public view exists; the marker says the house is a quarter mile south on private land |
| Mount Zion (Rodney) Baptist Church | Rodney, MS, west end of Batchelor Street at Olive Street | 1851 frame church, abandoned, weakened by floods (Wikipedia, Rodney society, HMdb) | Its own pin; folded into the Rodney town entry for now |
| Port Gibson Oil Works mill building | Port Gibson, MS | Cottonseed oil mill from 1882, one of the first in the US; closed 2002 (Wikipedia) | Whether the Register-listed building still stands, a coordinate and the owner |
| Union Church Presbyterian Church | Union Church, MS (31.6828, -90.7906) | 1852 church of the Scotch settlement (Wikipedia stub) | Any source on what survives and whether it is in use |
| Canemount | Alcorn, MS (31.89442, -91.12822) | Antebellum plantation near Bethel church (HMdb) | Owner, use, and whether anything can be seen from the road |
| Emerald Mound | Natchez Trace milepost 10.3 | Second-largest Mississippian ceremonial mound (NPS) | An earthwork, not a building: left out of this batch; could be added if mounds are wanted |

## Tips
- `brick.py look` waits on Wikimedia refusals long enough that four looks in one call ran past the two-minute shell limit: run one look per call, or give it a longer timeout.
- `publish.sh` stopped once because another batch (Albany) merged a few minutes after this session began; `resync.sh` caught up in one step, then a new branch name was needed.
- For Mississippi river towns, the HMdb nearby list round a town gave nearly every building's marker with its position in one request (Port Gibson's "Historic Tour" markers, the Grand Gulf park markers, Rodney).
- Wikipedia gives the Elizabeth Female Academy at milepost 4.1, NPS at 5.1; NPS has a places page for Mount Locust under `mount-locust-historic-house` and for the Sunken Trace under `sunken-trace-milepost-41-5`, which the guessed short names miss.
