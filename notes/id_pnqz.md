# id_pnqz: Idaho: Coeur d'Alene to the Wood River valley
state: Idaho
region: id
date: 2026-11-24
places: 11
file: data_id_pnqz.py

## What this batch is
Eleven places in Idaho, spread over the north (Fort Sherman buildings and the Inland Empire Electric Railway substation in Coeur d'Alene, St. Stanislaus Kostka Mission in Rathdrum), the Clearwater (the Camas Prairie depot and the 21 Ranch house at Lewiston, the 1909 Presbyterian church at Lapwai), the east (the Church of the Redeemer in Salmon, the Yankee Fork Gold Dredge) and the Wood River valley (Blaine County Courthouse in Hailey, the Gimlet and Cold Springs railroad truss bridges near Ketchum). Sources: Wikipedia articles read with wiki_raw.py, National Register forms read with page.py (NPGallery `_text`), and the Idaho Parks and Recreation page for Land of the Yankee Fork. Pins were looked at on the aerial; the 21 Ranch house and the Cold Springs bridge were moved onto what the aerial showed.
Not checked: every interior; opening hours and service times of every church and the courthouse (hours='?'); who owns the Lewiston depot and the Coeur d'Alene substation now; dredge tour dates and fees (the park page names tours but gives no dates); who manages the two bridge trails; the Rathdrum church and the Hailey courthouse could not be told apart on the aerial (church under trees, courthouse among a cluster), so those pins rest on the Register/OpenStreetMap points. The 2026 Coeur d'Alene Press article on the Fort Sherman Chapel opening for tours was blocked (403) and its archived copy could not be fetched, so the chapel's days and times are unknown.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Sherman Chapel | Coeur d'Alene, ID (about 47.677, -116.797) | A 2026 news report says it is open at set times with volunteer guides | Days, times and address from the city or museum page |
| Hotel Paris | Paris, ID (42.22664, -111.40070) | 1916 brick hotel on the Register; Wikipedia says still in operation | A page of its own showing it operates and its hours |
| Montpelier Historic District | Montpelier, ID (42.31764, -111.30275) | Four 1916 public buildings including the LDS stake tabernacle | Left out: Wikipedia files part of it as Streamline Moderne; a source on the tabernacle alone |
| Mackay Episcopal Church and Mackay Methodist Episcopal Church | Mackay, ID (43.9111, -113.6131; 43.9133, -113.6097) | Both on the Register | Sources on what each is built of and whether open |

## Tips
- Idaho Register forms for these counties all had a text layer; use `page.py --all -n 200000` and cut it with `sed 's/\s\+/ /g'`, then grep "DESCRIBE THE PRESENT" and "STATEMENT OF SIGNIFICANCE".
- `nom.py` found the dredge and the powder magazine but nothing for the Fort Sherman chapel, the Lewiston depot or the substation.
- The `pix.py look` scale is 1.87 px per metre for a 150 m half-width picture: a first guess at 50 m per grid cell is easy to get wrong.
- `resync.sh` reported tools/pics_txwk.py as "needs a decision" though this session never touched it.
