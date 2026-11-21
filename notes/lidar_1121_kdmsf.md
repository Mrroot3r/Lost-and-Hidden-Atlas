# lidar_1121_kdmsf: LiDAR finds: Beaver Meadow and Exeter State Forests, New York; Monroe and Savoy, Massachusetts
state: Massachusetts, New York
region: berk, cny, pv, scho
date: 2026-11-21
places: 22
file: data_lidar_1121_kdmsf.py

## What this batch is
A judging-only LiDAR session (LIDAR.md; nothing was swept). 22 unverified leads, each a pit on the LiDAR ground model beside a building on the oldest USGS sheet with nothing standing on the state leaf-off aerial: 17 in Beaver Meadow State Forest (Smyrna and Otselic, Chenango County), 1 in Exeter State Forest (Otsego County), 3 in Monroe State Forest and 1 in the Savoy part of Kenneth Dubuque Memorial State Forest. Every chip of Exeter (11) and Beaver Meadow (39) was looked at, and the eight "maybe" candidates left by earlier sessions (Catamount, Dubuque, Monroe) were settled on full sheets. Read with `tools/lidar.py` (next, sheet, check, draft) and `tools/pincheck.py`; the map panels were also enlarged to read the building marks. NOT checked: anything on the ground; the owner of any Beaver Meadow spot (Chenango County is not in the state parcel file, so those 17 rest on the federal public-land record alone); whether any forest road named can be driven ("walk" was given only where the aerial shows a gravel or dirt road within about 100 m); parking and trails in New York (none looked up); hours and rules for the Dubuque forest (the DCR page would not open; Monroe's did). brick is '?' for all: nothing shows above ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Walled farm site at the sheet edge (candidate msf4) | Monroe State Forest, MA (42.699552, -72.999870) | LiDAR: sharp round pit where three straight banks meet, small rectangular banked enclosures 30 to 50 m west. Set aside as "nomap" because the spot is on the west margin of the Hawley 1890 and Rowe 1944 sheets, so the "building" the search found is the sheet border | Read the Greylock sheet (the next one west) for a building here; then the ownership check |
| Roadside pit (candidate esf3) | Exeter State Forest, NY (42.836624, -75.093865) | 1907 Winfield sheet draws a building on the north side of the road here; LiDAR pit is cut into the bank within about 10 m of a wide gravel road, so it could be road works | A look on the ground |
| Small sharp pit about 55 m east-north-east of candidate bemsf31 | Beaver Meadow State Forest, NY (near 42.69596, -75.65027, read off the sheet, not measured) | Both the 1903 and 1944 sheets draw a building about there; the scanner did not list this pit, and bemsf31 itself is a soft hollow | A full sheet centred on it, the ownership check, a look on the ground |
| Pit at an old road corner (candidate bemsf33) | Beaver Meadow State Forest, NY (42.703807, -75.674246) | 1903 sheet draws a building at the road corner; the LiDAR pit is small and shallow with no sharp edge | A look on the ground |
| Small pit east of the paved road (candidate bemsf20) | Beaver Meadow State Forest, NY (42.672344, -75.685091) | 1903 sheet draws a building about 30 m south; pit is small, on plantation furrows, could be a tip-up; a house and lawn stand about 110 m south-west across the road | A look on the ground; who owns the road frontage |

## Tips
- `publish.sh` refuses a LiDAR draft with no `brick=`; `lidar.py draft` does not write one. This session added `brick='?'` by hand to every entry.
- The 1,800 m map panel on a sheet is about 4.5 m to the pixel: a building mark is 3 pixels. Enlarging the middle of the panel made lettering, town-line dashes and real building squares easy to tell apart.
- The building finder took a town-line dash for a building twice in Exeter (esf2, esf7) and the sheet margin once in Monroe (msf4).
- Two Beaver Meadow candidates were set aside as the second pit of a farm already written up (bemsf12 with bemsf13, bemsf21 with bemsf14); the place texts mention both pits.
