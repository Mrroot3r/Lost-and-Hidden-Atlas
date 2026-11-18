# paw_egal: Beaver County, Pennsylvania
state: Pennsylvania
region: paw
date: 2026-11-18
places: 13
file: data_paw_egal.py

## What this batch is
The first close pass in region `paw` (drawn at random with `choose.py`): Beaver County, where the Beaver River meets the Ohio. 13 places. Standing: Old Economy Village (the Harmonists' last town), the Merrill Lock No. 6 lock station on the Ohio (closed restaurant, look from PA 68), Greersburg Academy (about 1806), the Vicary House (1826–29 sandstone), the Aliquippa and Beaver P&LE stations, and the Carnegie Free Library of Beaver Falls. Ruins, traces and sites: the Fort McIntosh dig (stone hearths and wall footer in a roadside park), Legionville (markers only), the 1881 Beginning Point monument, the Girard Locks of the Beaver Division Canal, the Watts Mill truss footbridge and mill site on State Game Land 285, and the Frankfort Mineral Springs resort remnants in Raccoon Creek State Park. Wikipedia was read as raw text with `wiki_raw.py`; HMdb marker pages and its nearby lists, SAH Archipedia (Buildings of Pennsylvania), PHMC, oldeconomyvillage.org, DCNR, the Beaver County Library System, the Beaver Area Heritage Foundation, the Little Beaver Historical Society, Atlas Obscura and one Register form (88000868) with `page.py`. Not checked: anything on the ground; who owns the Merrill Lock buildings, the Fort McIntosh park, the Legionville park and the Girard lock remains; hours at the Vicary House, the Beaver Area Heritage Museum and this year's Greersburg Academy open days; what the Frankfort resort remnants and the Watts mill remains are; whether the lock remains under the Bridgewater–Rochester Bridge can be seen from public ground. Old Economy's two official pages give different weekday hours (both given). Pins that mark only a general area or a marker, not the thing: Girard Locks (the marker corner; remains are under the bridge about 150 m west), Legionville (the DAR monument), Beginning Point (Wikipedia point; the monument was not seen on the aerial). The Watts Mill parking point is an OpenStreetMap lot that the aerial does not clearly show. Red brick from sources: yes for Old Economy (SAH: "red brick and frame") and Merrill Lock (brick on Wikipedia, orange-colored on SAH); no for the stone academy, the Vicary House, Fort McIntosh, the Watts truss and the yellow-brick library; the rest '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Homewood Iron Furnace | Homewood, PA (marker 40.81367, -80.32962) | Charcoal furnace built 1857 by James Wood on the Beaver River near Rock Point, out of blast 1867/68 (HMdb 167530) | Whether anything of the stack survives, and where |
| Hungerford Cabin | Raccoon Creek State Park, PA | DCNR hiking page names the "historic Hungerford Cabin" on a trail by Raccoon Creek | Date, what it is, coordinate |
| Traverse Creek mill and spring house sites | Raccoon Creek State Park, PA | DCNR: an 1800s gristmill, stone spring house and homesteads along Traverse Creek and its trail | Which trail, what remains, coordinate |
| Beaver Division Canal locks at New Brighton and Eastvale | New Brighton, PA | HMdb nearby list: five locks at New Brighton and two at Eastvale; "few remains are visible today" | Marker number and any source saying what can be seen |
| First reservoir (1845), Beaver Falls / New Brighton area | Beaver County, PA | HMdb nearby list (5 miles round Beaver Falls): "First reservoir, built 1845 from native stone, still stands" | Which marker, where, owner |
| Old stone church (1800), Shenango Road | North of Beaver Falls, PA | HMdb nearby list: "Old stone church built 1800 north of here on Shenango Road" | Marker, name, whether it stands |
| Logstown / Legionville redoubt No. 4 | Harmony Township, PA (near 40.62, -80.23) | HMdb nearby list: a redoubt and blockhouse of the Legion Ville cantonment stood in the SE corner of a property | Which marker, and whether anything shows |

## Tips
- The Pennsylvania leaf-off server took about 90 seconds a tile with `--lidar`: `pincheck.py --batch` on 13 places with 3 trailheads was killed by a 20-minute timeout two tiles short. Run it in two halves of named ids, in the background, with no timeout (the named-id run always writes `pincheck_picked_*`, so move the first half's sheets aside before the second).
- `publish.sh` stopped once because two data files had been merged to `main` while the pin check ran; `resync.sh` fixed it in a minute. Take the batch time again after resyncing.
- SAH Archipedia (`sah-archipedia.org/node/<n>`) reads cleanly with `page.py --all`: its "Materials:" line and the "Print Source" paragraph settle red brick and give current use. Search results find the node numbers.
- HMdb nearby lists with a 5-mile radius round several points in the county found most of the leads above; marker numbers come from the cached page in `research/pages/` (search for `m.asp?m=`).
- oldeconomyvillage.org and the PHMC page give different weekday hours for Old Economy Village.
