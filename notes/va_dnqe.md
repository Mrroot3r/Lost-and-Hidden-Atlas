# va_dnqe: Virginia: a fourth scatter, Hampton Roads to the Shenandoah
state: Virginia
region: va
date: 2026-11-24
places: 12
file: data_va_dnqe.py

## What this batch is
Twelve places across Virginia (47 before, 59 after; the fewest of any state not held by another session): the Woodrow Wilson Birthplace (Staunton), the Stonewall Jackson House (Lexington), Waterford village (Loudoun), the Booker T. Washington birthplace (Franklin County), the Strasburg Museum in the 1891 pottery and depot, Sully (Chantilly), Michie Tavern (moved 1927), Lee Hall Mansion (Newport News), Dayton Historic District, Christiansburg Institute, Fort Boykin's earthworks (Isle of Wight) and Hanover Tavern. Facts come from Wikipedia (`wiki_raw.py`) and the managers' own pages (`page.py`). Not checked: anything on the ground, interiors, parking for most places, ownership of Dayton's buildings. Hours not found: Lee Hall (`hours='?'`; the city page gave none), Christiansburg Institute (its own site would not load; a web search said tours by appointment, not read from the operator, so not used). Stonewall Jackson House hours come from a holiday-hours notice and may differ from the regular schedule; Sully's page also carried a 2022 notice. Brick was settled from pictures for Wilson (yes), Jackson (yes), Sully (no), Michie and Hanover (some); the rest are `?`. Pins moved: Sully (was on a highway), Hanover (parking lot), Michie (woods), Strasburg (40 m), Fort Boykin (to the middle of the earthworks on LiDAR). Pictures chosen for four places in `pics_qarq.py`.

## Leads
Places you read about and could not finish.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Shirley Plantation | Charles City County (37.34194, -77.26083) | Wikipedia: oldest active plantation in Virginia, settled 1613 | Its own page gave no hours to `page.py`; not written up |
| Appomattox Manor (City Point) | Hopewell (37.31667, -77.27722) | Wikipedia: Union headquarters 1864-65, run by the National Park Service | NPS hours page 404; not written up |
| Carlyle House | Alexandria (38.80528, -77.04222) | Wikipedia: 1751-52 stone Georgian house | Not read beyond the lead |
| Haller-Gibboney Rock House | Wytheville | Wikipedia article exists | Not read |
| Dismal Swamp Canal (Deep Creek lock) | Chesapeake (36.55667, -76.38056) | Opened 1805, oldest operating canal in the U.S. | No lock pin chosen |

## Tips
- `tools/smoke.js` needs the address as its first argument (`http://localhost:8766/web/ <place id>`) with `dist/` served; `app_smoke.js` tests the Android copy and fails if nothing serves it.
- `page.py --all` prints one long line; a `grep -oiE '.{0,110}(a\.m|p\.m).{0,140}'` on it finds hours quickly.
- Wikipedia coordinates fell on a highway, a lot and woods for three of twelve places; the ArcGIS geocoder on a street address fixed two of them.
