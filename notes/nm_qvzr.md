# nm_qvzr: New Mexico: mining camps, Route 66 and adobe churches across the state
state: New Mexico
region: nm
date: 2026-11-22
places: 21
file: data_nm_qvzr.py

## What this batch is
Twenty-one places scattered across New Mexico, which had 34, none of them in the north-west, the far east, Albuquerque, Taos town or the south-west corner: Elizabethtown, the St. James Hotel (Cimarron), the Shuler Theater (Raton), Hotel Eklund (Clayton), the Cleveland Roller Mill (Mora County), the Kit Carson House (Taos), the Santuario de Chimayó, the Chama rail yard and depot, the El Rancho Hotel (Gallup), San Felipe de Neri and the KiMo Theatre (Albuquerque), Golden, Cuervo, the Blue Swallow Motel (Tucumcari), Glenrio, Hotel Clovis, Kelly, the Pioneer Store (Chloride), Kingston, Shakespeare and the Basilica of San Albino (Mesilla). Sources read with `wiki_raw.py` and `page.py`: Wikipedia, nps.gov/places pages, HMdb markers (Chama yard, coal tipple, depot; Kelly), the City of Albuquerque's KiMo pages, shulertheater.com, clevelandrollermillmuseum.org, hoteleklund.com, sanalbino.org, shakespeareghostown.com, holychimayo.us, Sierra County Recreation & Tourism, newmexico.org, New Mexico Magazine, the Albuquerque Journal, Atlas Obscura and newmexicoghosttowns.net. Pins checked on Esri satellite; Cuervo moved 75 m off the I-40 embankment. Not checked: nothing seen on the ground; hours for the Kit Carson House, St. James, El Rancho, Blue Swallow, Eklund, Shuler, San Felipe de Neri and Chimayó (their pages would not open or gave none); the Pioneer Store and Kingston museum hours come from the county tourism board, not the museums' own pages; who owns the ruins at Kelly, Golden, Elizabethtown and Cuervo (all view-only); where Elizabethtown's boarding-house wall stands (area pin). Sources disagree on El Rancho's opening year (1936/1937), the Blue Swallow's opening (1941/1942) and unit count (12/14), San Albino's date (1906/1908) and Kelly's road (all conf='mixed'). `check.py` warns that Glenrio's pin is just outside the coarse state outline; it is on the OpenStreetMap State Line Bar, which Wikipedia puts on the New Mexico side. Brick from sources: San Albino yes (fired brick, plaster removed), El Rancho and the Chama roundhouse some, adobe and stucco buildings no, the rest '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Dorsey Mansion | Colfax County, NM, 12 miles north of US 56 north-east of Springer (Wikipedia 36.48667, -104.19111) | Wikipedia: log and stone mansion 1878–1886 of Senator Stephen Dorsey; privately owned since 1987 and not open for tours | Whether any of it can be seen from a public road |
| Steins | Hidalgo County, NM, I-10 at Steins Pass (Wikipedia 32.22917, -108.98944) | Wikipedia: railroad town abandoned 1944, tours ended 2011 | Current owner and whether anything can be seen from the road |
| Kelly Mine headframe | Kelly, south of Magdalena, NM | 121-foot headframe of 1906 (newmexico.org) up the hill from the church | Exact position and who owns the mine ground |
| Luna Theater | Clayton, NM, across from Hotel Eklund | Wikipedia (Eklund Hotel): also on the Register | Article or form not read |

## Tips
- Web searches returned titles and links only; every fact came from pages read with `page.py`.
- taos.org, kitcarsonmuseum.org, sanfelipedeneri.org and blueswallowmotel.com refused `page.py` (403 or no connection); holychimayo.us/schedule is drawn by script and empty.
- The federal land line labels the Kit Carson House in central Taos "Taos Pueblo".
- `photo_find.py look` on five places runs longer than two minutes; start it in the background.
