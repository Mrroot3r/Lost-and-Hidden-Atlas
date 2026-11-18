# ky_ixyl: Kentucky: Harrodsburg, Pleasant Hill, Danville and Perryville
state: Kentucky
region: ky
date: 2026-11-18
places: 14
file: data_ky_ixyl.py

## What this batch is
Fourteen standing places in Mercer and Boyle counties (plus High Bridge Park, Jessamine County): Old Fort Harrod State Park, Shaker Village of Pleasant Hill, Shaker Landing, the Old Mud Meeting House, Morgan Row and the Beaumont Inn in and around Harrodsburg; High Bridge; Constitution Square, McDowell House, Old Centre and Jacobs Hall in Danville; Perryville Battlefield and Merchants' Row in Perryville; Penn's Store at Gravel Switch. Sources read: Wikipedia (`wiki_raw.py`, including the two county Register lists), Register forms for Old Centre and Jacobs Hall (npgallery text layers), ExploreKYHistory and Kentucky Historical Society marker pages, HMdb markers, the James Harrod Trust tour pages, and the managing bodies' own pages for Shaker Village, McDowell House/Constitution Square and Perryville (perryvillebattlefield.org, friendsofperryville.org). Not checked: Kentucky State Parks pages (parks.ky.gov is drawn by script), so Old Fort Harrod's hours come from a 2026 Harrodsburg Herald article and its closing time is not checked; hours for Morgan Row, the Old Mud Meeting House, Beaumont Inn, Penn's Store and High Bridge Park; who runs High Bridge Park; parking at Old Mud, Morgan Row, Constitution Square, Old Centre, Jacobs Hall and Penn's Store. Nothing seen on the ground. Pins that mark only a parking lot or a general area: Shaker Landing (the landing lot; the 1866 stable was not found on the aerial) and Penn's Store (Register list point in trees, no roof visible). Red brick: 'yes' for Old Centre (Register form says red brick) and Beaumont Inn (Wikimedia photo); '?' for the rest (Jacobs Hall's only photo is black and white).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Dix Dam | Mercer/Garrard line, KY (37.78528, -84.70389) | 1923–25 rock-fill dam, the largest of its kind when built, owned by Kentucky Utilities (Wikipedia) | Any public viewpoint and access rules from the owner |
| Shawnee Springs | Harrodsburg, KY | Register listing 76000927; list says destroyed by fire August 1982 | Whether anything is left to see |
| H.P. Bottom House and Crawford House | Perryville, KY (37.664444, -84.970556; 37.6625, -84.94) | Register-listed battlefield houses (Boyle County list) | Whether the park or a private owner holds them and whether they can be seen |
| Stone Quarters on Burgin Road | Harrodsburg, KY | Register listing 83002833 (Mercer County list), address restricted | Location and owner |
| Wilson's Station | Danville, KY (37.620833, -84.813611) | Register-listed station site (Boyle County list) | What is there and whether it is public |

## Tips
- parks.ky.gov (Kentucky State Parks) is drawn by script and `page.py` gets 63 characters; its static mirror `kyp-kyparks-static.azurewebsites.net` answers 403. A local newspaper (Harrodsburg Herald) carried the 2026 hours for Old Fort Harrod.
- For Danville, McDowell House's own site (`mcdowellhouse.com/constitution-square`) carries the hours for Constitution Square too.
- Perryville Battlefield's hours read cleanly from `perryvillebattlefield.org/html/directions_and_hours.html`.
- `brick.py look` hit Wikimedia's HTTP 429 twice in a row for McDowell House even after a 60-second wait; give up after two tries.
