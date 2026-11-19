# pane_wipu: Carbon County and the Lehigh Gorge, Pennsylvania
state: Pennsylvania
region: pane
date: 2026-11-19
places: 16
file: data_pane_wipu.py

## What this batch is
The first close pass in region `pane` (drawn at random with `choose.py`): Carbon County round Jim Thorpe (old Mauch Chunk), the Lehigh Gorge, Weissport and Lehighton, Nesquehoning and Lansford, with Eckley Miners' Village just over the line in Luzerne County. 16 places. Standing: the Old Jail Museum (Molly Maguires), the Asa Packer and Harry Packer mansions, the CNJ station, St. Mark's Episcopal Church (Upjohn, Tiffany glass), the Mauch Chunk Opera House, Little Gap Covered Bridge, the No. 9 Mine and Museum, the Nesquehoning grotto (a miner's WWII shrine) and Eckley. Ruins and traces: the Switchback gravity railroad (now a trail), Lehigh Canal Lock No. 1 under the PA 903 bridge, Lock 22 at Mud Run in the gorge, the Lehigh Tannery ruins, and the Fort Allen well. Marker only: the Gnaden Huetten massacre site (1755). Wikipedia read with `wiki_raw.py`; HMdb marker pages, DCNR, PHMC, Carbon County, museum and church pages, the Switchback Gravity Railroad Foundation trail notes, Times News and the grotto's Register form read with `page.py`. Not checked: anything on the ground; fees at the jail, Asa Packer Mansion and Eckley; the No. 9 Mine season (its own site answered 403; hours from the Lehigh Valley Passport to History page and a 2019 Visit PA copy); the Harry Packer Mansion's tour times; the Opera House interior; what can be seen of the Lehigh Tannery ruins (pin is the marker on the trail) and of Lock No. 1 (pin is the bridge end, area); the Switchback pin is the Wikipedia coordinate (area) and its "what to look for" rests on the foundation's trail notes, which call themselves local knowledge. The Fort Allen well's mapped point falls in Weissport Borough Park on the federal map, though the PHMC marker says it is "behind houses opposite"; access made public on that basis. Red brick: Harry Packer Mansion and the CNJ station from Wikipedia's words; Asa Packer Mansion and Little Gap bridge from Wikipedia pictures opened with `brick.py look` (no red brick); the rest from sources naming stone, or left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hotel Wahnetah and Glen Onoko resort | Glen Onoko, Jim Thorpe, PA | DCNR history page: 47-room hotel, closed by a fire in 1911; a 1917 fire ended the resort era | Whether any ruin is left and where; the Glen Onoko Falls trail's present status |
| Mud Run disaster (1888) | Lehigh Gorge near Lock 22, PA (40.9877, -75.7135) | HMdb marker "Disaster at Mud Run" stands next to the Lock 22 panels | Marker text not read |
| Indian Stairway (122 stone steps) | Back Track trail east of the Mauch Chunk Lake dam, PA | Switchback trail notes: built by the Gehring brothers after the 1888 blizzard | A coordinate, and whether the ground is county park or private |
| Mauch Chunk Lake Park entrance / Switchback trailhead | Jim Thorpe, PA | County page: trail joined near the park's main entrance | A coordinate for the lot; park hours (county hours page shows only rental rates) |
| Parryville Historic District | Parryville, PA (40.81717, -75.67297) | HMdb marker 124045, "largely illegible" | Any source on what stands |
| Old Wash Shanty (OSM mapped ruin) | Nesquehoning, PA (40.85738, -75.8166) | OpenStreetMap lead only | Any source |
| Lansford and Summit Hill historic districts | Panther Valley, PA | National Register listings (12000605 Lansford) | Forms not read |

## Tips
- The Pennsylvania leaf-off server took 60 s to several minutes a tile and often timed out to Esri: `pincheck.py --batch` on 16 places with 7 trailheads managed six tiles in 25 minutes. Copying the workspace to six folders (`cp -r atlas atlas_pN`, 67 MB each) and running `pincheck.py <ids> --lidar` on two or three ids in each at once finished all of them in about eight minutes. The LiDAR half takes about 4 s a tile; the aerial is the slow part.
- HMdb nearby lists round Weissport and Jim Thorpe (5 miles) found most of this batch: Fort Allen, Gnaden Huetten, Lock No. 1 and the Mansion House bridge dam panel. The D&L heritage-corridor panels on the Lehigh Gorge Trail give exact positions for the lock ruins.
- no9mine.com answers 403 to `page.py` and its archived copy is empty. allentowndiocese.org news pages answer 404 with no archive.
- The grotto's National Register text (`NRHP/GetAsset/NRHP/11000923_text`) is a 153-page PDF with a good text layer under OCR noise; grep the cached copy in `research/pages/` with a short Python search rather than `page.py -g`.
