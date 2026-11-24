# de_kmpt: Delaware: Milton to Wilmington
state: Delaware
region: de
date: 2026-11-24
places: 11
file: data_de_kmpt.py

## What this batch is
Fourth pass over Delaware, taken with `choose.py --thinnest` (51 places before, 62 after). Eleven places spread over all three counties: New Castle (Amstel House, St. Georges Presbyterian Church, the Wilmington Friends Meetinghouse), Kent (the Clayton railroad station, Cow Marsh Old School Baptist Church, the Mahon River light) and Sussex (the Milton Historic District and Cannon Museum, the Indian Mission Church near Harbeson, the Hearn and Rawlins Mill at Seaford, the Brick Hotel in Georgetown). Sources: the Register lists and Wikipedia articles read with `wiki_raw.py`; the Delaware Public Archives marker and house-of-worship pages; the New Castle Historical Society and Wilmington Friends Meeting pages read with `page.py`. Hours: only Amstel House and the Friends meeting have a page read this session. Not checked: any interior, owners of the Clayton station, Cow Marsh church and Hearn mill, whether the Cannon Museum and St. Georges church open, Mahon River tower viewpoint. Two Register points were in water (Mahon River light, Hearn's Pond) and were moved; the Mahon pin is the shore by the pier, not the tower. Dropped after reading: Blackwater Presbyterian Church (demolished 2018), Chipman Potato House (removed 2017-18), Bancroft Mills (demolished after the 2016 fire).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fourteen Foot Bank Light | Delaware Bay off Bowers (39.0482, -75.1836) | Wikipedia: 1885-86, first lighthouse built with a pneumatic caisson, 11 miles offshore | Whether it can be seen from any public point or boat tour |
| Mermaid Tavern | Newark (39.7428, -75.6945) | Wikipedia: stone house of about 1725 with later frame additions, once tavern and post office | Who owns it and whether it is visible from a street |
| Rockwood | Wilmington (39.7725, -75.5208) | Mansion and park; search results say the galleries are closed for construction in autumn 2026 | Hours from a page of New Castle County (rockwood.org answered 403) |
| Milton Historical Society hours | Milton (38.7792, -75.3117) | Search snippet of an older page said Thursday to Saturday 11 to 4 (2024) | The society's page (historicmilton.org/about/location.html is a 404) |

## Tips
- `history.delaware.gov` is not needed for Milton: the Public Archives' marker pages (`archives.delaware.gov/delaware-historical-markers/<name>`) read cleanly with `page.py --all -n 3000`; the plain `-g` filter printed nearly nothing for them.
- `newcastlehistory.org/plan-your-visit` lists hours for several sites on one page; Amstel House's lines are those under "Amstel House tours start on even hours".
- Wikipedia has no article for the Cannon Museum; the Commons search by name returned John Milton prints.
