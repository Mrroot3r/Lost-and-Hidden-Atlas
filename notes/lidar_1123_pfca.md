# lidar_1123_pfca: LiDAR finds: Platte Falls Conservation Area, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 3
file: data_lidar_1123_pfca.py

## What this batch is
Three house and farm sites in Platte Falls Conservation Area (Platte County, Missouri), found with `tools/lidar.py` as LIDAR.md says: a pit on the USGS 3DEP ground model beside a building on the 1910 Leavenworth sheet, looked at on full sheets (LiDAR, satellite picture, the 1910 sheet and the 1951 Tracy sheet), and checked as state-owned parcels. Hours, fees, rules and the hunting note come from the Missouri Department of Conservation's own page for the area; parking lots from OpenStreetMap via `parking.py`, looked at on the pin check. Not checked: anything on the ground; whether the gravel roads beside two of the pits are open to cars; what the pale debris beside the lane-end farm pits is; whose the roofed building 120 m north of the Settle Station Road pit is. Missouri has no leaf-off aerial wired in, so "nothing standing" was read off a satellite picture with no leaves visible but not a leaf-off flight. All three are `conf='lead'`.

The same session also finished the backlog of the Kansas City units (Platte Falls 15, Burr Oak Woods 2, Wyandotte County Lake 5 not yet looked at; the four "maybe" bca2, bca3, pfca8, pfca9), and swept two new units: William L Landahl Park Reserve (11 map buildings, 3 pits, all soft or natural) and Bonanza Conservation Area (Caldwell County; 61 map buildings on the 1924 Braymer sheet, 6 pits, none passed: the one "maybe" sat on a spot-height dot, not a building).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pit beside a 1933 building, Burr Oak Woods (`bowca2`) | Sni-A-Bar township, Jackson County, MO (39.061167, -94.292479), near East Strode Road | Sharp small pit in a shrub clump in an old field, a second pit about 40 m north-west; the 1933 and 1945 Blue Springs sheets draw a building about 50 m north-west, east of a lane on the line of today's field track | `lidar.py check` found no state parcel and no federal public-land record at the point, though PAD-US names the unit nearby: a record showing the ground is part of the conservation area |

## Tips
- `setup.sh` did not install `scikit-image`, and every sweep crashed in `lidar_walls.py` (`No module named 'skimage'`) even in Missouri, where walls are not kept. `python3 -m pip install scikit-image` fixed it (plain `pip` installed it for another Python).
- `sweep "Reed (James A.) Memorial Wildlife Area"` and once `sweep "Bonanza Conservation Area"` said NO SUCH UNIT although `find` prints those names; Bonanza worked at once with `--state mo`. Reed was not tried again.
- Bonanza Conservation Area is in Caldwell County, outside `kcmo`; nothing from it was written, so no region was needed.
- `publish.sh` folded the repository's ledger over three verdicts given the same day (bca2, bca3, pfca9 went back from "no" to "maybe"): `merge_from` in `lidar.py` compares only the date, and on a tie the further-along status wins, so a "maybe" turned to "no" on the same day is undone. They were marked again and the two unit files copied from the workspace. Needs a time in `when`, or the later write preferred, in `lidar.py` (not changed here).
