# ns_hdtv: Nova Scotia: Digby to Cape Breton
state: Nova Scotia
region: ns
date: 2026-11-28
places: 18
file: data_ns_hdtv.py

## What this batch is
Eighteen places across ten counties outside Annapolis and Lunenburg (Digby, Shelburne, Yarmouth, Kings, Cumberland, Pictou, Antigonish, Guysborough, Richmond, Inverness), drawn with `choose.py --thinnest` (Nova Scotia had 59 places). Every text rests on the place's Canadian Register of Historic Places statement, read with `page.py --all` (one page at a time, 3 s apart: no resets). Hours came from the Nova Scotia Museum's own pages for the Old Meeting House and Dory Shop only; the Woolen Mill's rest on a search result quoting its site (page would not read); the others are `hours='?'` because sources disagreed or were dated 2018/2025. Not checked: interiors, parking, service times, who owns the Wallace River bridge and St. Peter's Canal land (both set to `view`). Pins: eleven are the Register/Wikipedia point left as it was after looking at the aerial; Sainte-Marie, Prescott House, Orangedale and St. Peter's Canal were moved (see pin notes); Trinity Digby is the street corner the Register names (`prec='site'`). Holy Trinity Yarmouth is `brick='yes'` from the Commons photograph. Pictures chosen for 17; Yarmouth County Museum only had interiors.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pictou Railway Station (Intercolonial) | Front Street, Pictou (Register id 7470) | 1904 brick Class One station, national historic site, ground floor a museum (Register) | The Register/Wikipedia point (45.6833, -62.7167) is inland in houses; the building was not found on the aerial |
| Grassy Island Fort | Canso Islands (Register id 11666) | 1720s–1735 British fort earthworks, national historic site | Boat access and a pin on the footprint |
| Inverness Railway Station / Miners Museum | Inverness (Register id 11859) | 1901 wooden station, now the Miners Museum | Not written up |
| Christ Church, Windsor | Windsor (Register id 12032) | 1882–1884 Gothic Revival by Stephen Earle | Not written up |
| Ottawa House | Partridge Island, Parrsboro (Register id 13852) | Georgian house begun about 1774, museum | Not written up |

## Tips
- historicplaces.ca place pages read fast one at a time with `page.py --all -n 60000` (23 pages at 3 s pauses, no resets); the "Architect / Designer" and "Builder" fields near the end give names for `arch=`/`builder=`.
- The Wikipedia HPC list coordinates are often wrong in towns (Pictou station inland, Prescott House in a field); `geo.py` on the Register's street address landed on the house.
- Nova Scotia Museum sites have their own hosts (`meetinghouse.novascotia.ca/visit`, `doryshop.novascotia.ca/visit`) that `page.py` reads; `woolenmill`, `rossthomson` and `prescotthouse` visit pages gave nothing to `page.py`.
- `resync.sh` reported `data_b.py` as changed on both sides though this session never edited it; the workspace's main copy was right.
