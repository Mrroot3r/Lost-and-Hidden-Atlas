# sar_tesm: Saratoga County: old Champlain Canal at Schuylerville, Stillwater, Spruce Mountain and Lake Luzerne
state: New York
region: adk, sar
date: 2026-11-21
places: 9
file: data_sar_tesm.py

## What this batch is
Nine places in region `sar` (drawn at random by `choose.py --claim --state ny`), mostly in the northern and eastern towns of Saratoga County that the Atlas had little in, with three across the Hudson from Hadley in Lake Luzerne filed under `adk`. Old Champlain Canal: the towpath and Fish Creek aqueduct in Schuylerville, and Lock 10 with the replica lock tender's shanty and the Northumberland Dam at Hudson Crossing Park. Standing: the Marshall House (1770–73, private, Riedesel's cellar), the Dirck Swart House in Stillwater village (about 1757, private), the Spruce Mountain fire tower in Corinth (tower closed for structural concerns per Saratoga PLAN), the Pulp Mill Museum in Lake Luzerne's Mill Park, and the stone Church of Rockwell Falls. Also the Yellow Meeting House cemetery in the Town of Stillwater and the Garnar tannery smokestack in Lake Luzerne. Sources: the American Canal Society's Champlain index PDF and the Glens Falls Feeder sheet via `page.py`; Hudson Crossing Park's wayside pages; the villages of Schuylerville and Stillwater and the Town of Stillwater pages; Saratoga PLAN, DEC and Protect the Adirondacks for Spruce Mountain; Warren County's Lake Luzerne marker PDF; Wikipedia via `wiki_raw.py`; HMdb marker pages. Not checked: anything on the ground; the Pulp Mill Museum's opening days (no page of its own found; `hours='?'`); whether the 1764 Yellow Meeting House building still stands; where the Garnar smokestack stands (pin is the marker); the Lock 10 wall and the Fish Creek aqueduct masonry were not picked out on the aerial (the LiDAR shows the canal prism crossing Fish Creek). Red brick is `'?'` for all but the steel fire tower.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Becker's Lock (old Champlain Lock 9) | Town of Stillwater, NY, just north of Mitchell Road (canal index: 42.92366, -73.67328) | American Canal Society index: lift 9.17 ft, "just north of Mitchell Rd." | Condition, owner and whether it can be seen from a road; no second source found |
| Victory Mills | Victory, NY (Register 09001271, 43.08908, -73.59188) | Wikipedia: 1918 cotton mill, burned May 31, 2025 and demolished | Nothing known to be left; add only as `gone` if a series wants it |
| Hadley D&H depot | Hadley, NY, Rockwell Street at the tracks (HMdb 97390) | Marker (1999): depot closed 1958 and demolished | Gone; listed so nobody looks again |
| Kinnear Museum (Hadley-Lake Luzerne Historical Society) | Lake Luzerne, NY | Stories from Open Space: 1880s house given to the society in 1982 | The society's own page with hours, and a position |
| Joseph Henry's boyhood home | Galway, NY, NY 29 / Galway Road (HMdb 140627: 43.01932, -74.01942) | State marker: Henry lived here 1806–1813 | Whether the house stands, and which building |

## Tips
- Saratoga County's Register list rows put villages in the town column: grepping for "Schuylerville" or "Stillwater" with a pipe before it found the Marshall House and Victory Mills that a town-name grep missed.
- HMdb's 1999 Town of Hadley markers say plainly which buildings were demolished (depot, paper mill, Arlington Hotel); read them before hunting.
- `page.py` cannot read nashuacitystation.org (drawn by script) or brooksidemuseum.org's 2014 posts (drawn by script; one later post 404).
- Saratoga PLAN's Spruce Mountain page (read November 2026) says the tower is closed; the 2015 DEC bulletin and Wikipedia still describe it as open.
