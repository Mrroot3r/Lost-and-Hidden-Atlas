# November 16, 2026: the first LiDAR finds inside the Adirondack Park, from a sweep of three units:
# Terry Mountain State Forest (Clinton County), Taylor Pond Wild Forest (Clinton, Essex and Franklin counties) and
# Shaker Mountain Wild Forest (Fulton County). The old sheets draw 1,484 buildings inside them and 253 separate LiDAR
# pits lie within 90 m of one. The best-ranked 94 were looked at on LiDAR, 15 of those on full comparison sheets,
# and the five below held up.
# It went less well than round Albany, for three reasons the texts below do not hide:
#   - the state's ground model is coarser over much of this country, so a cellar hole is a soft dimple, not a sharp pit;
#   - on these sheets the building finder also picks up lettering, county lines and survey marks, and most of the
#     "buildings" beside the best pits turned out to be those;
#   - none of the four counties is in the state's public parcel file, so no find has a tax-parcel check. Each rests on
#     the federal protected-areas database (tools/pad.py) alone, as GUIDE.md section 13 allows, and says so. Forest
#     Preserve is a patchwork with private lots inside it: confirm on the ground.
# Only one old map was looked at for each (no 1940s sheet), so the texts do not say when the buildings went.
# Nothing here has been seen on the ground. Every entry is conf='lead'.
from data_b import N
from data_lidar3 import SRC,HUNT
BATCH={'key':'lidar5','label':'LiDAR finds: first sweep inside the Adirondack Park','added':'2026-11-17 00:30'}
OWN='No tax-parcel record could be checked: %s County is not in the state\'s public parcel file. The federal protected-areas database puts the spot inside %s, open to the public%s. Forest Preserve is a patchwork with private lots inside it, so confirm with the Owner? button or the state boundary signs before you leave the road.'
PLACES=[
N('lidar-rock-street-house-site','House site on Rock Street','Franklin','adk','lidar','traces',44.503483,-73.952426,'exact','public','walk','','before 1911',
  'The 1911 USGS survey (Lyon Mountain sheet) draws a row of three buildings along this road. The nearest is about 50 m from here.',
  'On LiDAR: a sharp pit about 5 by 7 m and 1.3 m deep with a mound of spoil beside it, about 12 m west of a dirt road. It is the deepest and sharpest of this round. The leaf-off aerial shows the road, woods and nothing standing. No later map was looked at, so when the house went is not known. Not checked on the ground.',
  'One of a row of houses on the 1911 map; a deep pit beside a dirt road now.',
  OWN%('Franklin','Taylor Pond Wild Forest',', and OpenStreetMap names the road Rock Street')+HUNT,SRC,conf='lead'),
N('lidar-alder-brook-road-pit','Pit and ditch on the old road north of Alder Brook','Franklin','adk','lidar','traces',44.519276,-73.937065,'exact','public','hike','','before 1911',
  'The 1911 USGS survey (Lyon Mountain sheet) draws a poor road running north from the hamlet it labels Alder Brook, with buildings along it. One is about 50 m from here.',
  'On LiDAR: a pit about 9 by 7 m and 1.2 m deep with a mound beside it, at the head of a narrow, sharply cut ditch that runs south for about 60 m. A pit with a ditch leading from it may be a cellar with a drain, or a dug spring or well. The leaf-off aerial shows evergreens and mixed woods and nothing standing. No later map was looked at. Not checked on the ground.',
  'A pit with its own drain, on a road the woods took back.',
  OWN%('Franklin','Taylor Pond Wild Forest',', and the nearest road OpenStreetMap names is Alder Brook Road')+HUNT,SRC,conf='lead'),
N('lidar-saranac-river-farmstead','Farmstead traces above the Saranac River','Black Brook','adk','lidar','traces',44.567506,-73.846844,'site','public','hike','','before 1911',
  'The 1911 USGS survey (Lyon Mountain sheet) draws two buildings on a poor road that runs east from the Saranac River. They are about 80 m north of here.',
  'On LiDAR: a straight bank or ditch running north to south for more than 100 m, a pit about 12 by 11 m and 0.8 m deep against it, level rectangular platforms just to the north, and the edge of an old field to the west. It reads as a farmyard, with the pit perhaps not the house itself. The leaf-off aerial shows mixed woods with a brushy opening to the north and nothing standing. No later map was looked at. Not checked on the ground.',
  'A wall line, platforms and a pit where the 1911 map has a farm.',
  OWN%('Clinton','Taylor Pond Wild Forest','. No named road is near; the old road on the 1911 map is the way in, if it can still be followed')+HUNT,SRC,conf='lead'),
N('lidar-terry-mountain-walls','Field walls and a farm site on Terry Mountain','Peru','adk','lidar','traces',44.576119,-73.635953,'site','public','hike','','before 1913',
  'The 1913 USGS survey (Dannemora sheet) draws a poor road climbing from the east and ending at two buildings. They are about 70 m south-east of here.',
  'On LiDAR: straight lines, walls or ditches, that meet at right angles like the corners of fields, with a small pit about 6 by 4 m and 0.7 m deep at the junction. The ground model is coarse here, so the pit is less sure than the lines. The leaf-off aerial shows hardwoods with patches of evergreens and nothing standing. No later map was looked at. Not checked on the ground.',
  'The corners of somebody\'s fields, at the end of a road on the 1913 map.',
  OWN%('Clinton','Terry Mountain State Forest',', and the nearest road OpenStreetMap names is McGarr Road')+HUNT,SRC,conf='lead'),
N('lidar-mussey-road-crossroads','House site at an old crossroads off Mussey Road','Caroga','adk','lidar','traces',43.099594,-74.500581,'exact','public','walk','','before 1901',
  'The 1901 USGS survey (Lassellsville sheet) draws a crossroads here, marked 1,368 feet, with buildings along each road. One is 16 m from the pin.',
  'On LiDAR: a rectangular hollow about 12 by 9 m and 1 m deep with a short bank beside it, a long straight wall line running north to south about 40 m to the east, and a deeper oval pit about 60 m to the west. A present-day road passes about 60 m to the south. The leaf-off aerial shows woods and nothing standing. No later map was looked at. Not checked on the ground.',
  'A crossroads hamlet on the 1901 map; hollows and a wall in the woods.',
  OWN%('Fulton','Shaker Mountain Wild Forest',', and OpenStreetMap names the road to the south Mussey Road')+HUNT,SRC,conf='lead'),
]
PIN_NOTES={
 'lidar-rock-street-house-site':'The pin is the LiDAR pit. The nearest building symbol on the 1911 sheet is about 50 m away; sheets of that scale can be 50 to 100 m off. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-alder-brook-road-pit':'The pin is the LiDAR pit. The nearest building symbol on the 1911 sheet is about 50 m to the north. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-saranac-river-farmstead':'The pin is the LiDAR pit beside the wall line. The building symbols on the 1911 sheet are about 80 m to the north, so the pin is rated "on site", not exact. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-terry-mountain-walls':'The pin is the junction of the wall lines on LiDAR. The building symbols on the 1913 sheet are about 70 m to the south-east, so the pin is rated "on site". Looked at on LiDAR and the leaf-off aerial.',
 'lidar-mussey-road-crossroads':'The pin is the rectangular hollow on LiDAR. The building symbol on the 1901 sheet is 16 m away. Looked at on LiDAR and the leaf-off aerial.',
}
