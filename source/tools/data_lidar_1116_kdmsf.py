# November 16, 2026: the first LiDAR finds in Massachusetts: Kenneth Dubuque Memorial State Forest, Hawley, drafted by
# tools/lidar.py (method: LIDAR.md) and finished by hand from the evidence sheets.
# Every entry is an unverified lead (conf='lead'): a pit on the LiDAR ground model beside a building on an old
# USGS sheet, nothing standing on the leaf-off aerial, on land the records show as public. Nothing was seen on the ground.
#   LiDAR  - USGS 3DEP ground model (1 m), read through tools/lidar_dem.py
#   old    - USGS Hawley 15-minute sheet (1:62,500), the 1890 printing. The 1886 printing of the same sheet is a pale
#            scan on which the building finder sees nothing, so the sweep used the 1890 one.
#   1940s  - USGS Plainfield sheet, 1947 (1:31,680)
#   aerial - MassGIS 2023 leaf-off imagery (flown 21 February to 28 April 2023)
#   parcel - MassGIS standardized assessors' parcels at the pin (tools/parcel.py): one 5,103.5-acre lot of the
#            Commonwealth, use class 910 (state parks and forests), for all four
# The sweep found 26 pits beside a map building in this forest. All were looked at; these four are the ones where the
# LiDAR shape, the old map and the aerial agree. Set aside: a walled complex beside Route 8A and a present house at West
# Hawley, three on pond shores, the summit of Parker Hill (the map "building" is the name), and faint or rocky ones.
# Two are left as "maybe" in the ledger (a field-corner pit in the west of the forest; and, in Catamount State Forest,
# two small pits on the old Catamount Hill road).
from data_b import N
from data_lidar3 import SRC,HUNT
BATCH={'key':'lidar_1116_kdmsf','label':'LiDAR finds: South Hawley, Massachusetts','added':'2026-11-17 02:15'}
SRCM=SRC+[['Mass. DCR: Kenneth Dubuque Memorial State Forest','https://www.mass.gov/locations/kenneth-dubuque-memorial-state-forest'],
          ['Mass. DCR: suggested hikes (the two parking places)','https://www.mass.gov/doc/kenneth-dubuque-memorial-state-forest/download']]
DCR=' Massachusetts DCR lists "cellar holes from the abandoned village of South Hawley" among the things to look for in this forest. Whether this pit is one that DCR or anyone else has already recorded was not checked.'
def ACC(west,east,where):
    return ('State land: the tax parcel under the pin is a 5,103.5-acre lot owned by the Commonwealth (use class 910, state parks and forests), in Kenneth Dubuque Memorial State Forest, which Massachusetts DCR runs. DCR gives the hours as sunrise to sunset. '
            'It names two parking places: the lot by Hallockville Pond off Route 8A (West Hawley Road), about %s km west of here in a straight line, and a gravel lot beside the Hawley fire station on Plainfield Road, about %s km to the %s; it says parking fees may apply. '
            'South Road and Middle Road are named on DCR\'s trail map, but whether either can be driven was not checked and no marked trail to this spot was found. DCR\'s rules say to stay on designated trails and roads: %s'%(west,east[0],east[1],where))+HUNT
PLACES=[
# kdmsf1  rank 1.15  verdict note: crisp square pit about 10 m across just north of South Road, stone walls round the lot; a second rougher pit 80 m north (kdmsf7)
N('lidar-south-hawley-south-road-cellar','Square pit in a walled lot on South Road, South Hawley','Hawley','pv','lidar','traces',42.548012,-72.911146,'exact','public','hike','','before 1947',
  'The 1890 printing of the USGS Hawley sheet names this stretch of road South Hawley and draws buildings along it: one on the road about 230 m to the west and one south of the road about 130 m to the south-east, where a house stands today. It draws nothing exactly at this pit; the search matched the pit to a mark 21 m away that may be part of the lettering. The 1947 survey (Plainfield sheet) draws South Road here and no building in the 600 m around the spot.'+DCR,
  'On LiDAR: a crisp, square pit about 10 m across and 1.1 m deep, about 30 m north of South Road, inside a lot marked off by straight walls: one runs north from the road about 80 m to the west, another runs east to west about 55 m to the north. A second, rougher pit lies about 80 m further north. The leaf-off aerial shows open hardwoods and nothing standing at the pit; across South Road, a house and an outbuilding stand in a clearing about 135 to 150 m to the south-east. Not checked on the ground.',
  'The sharpest pit of the sweep, in a walled lot in the village DCR calls abandoned South Hawley.',
  ACC('2.5',('3.1','east-north-east'),'this pit is about 30 m north of South Road. The parcel records show the north side of South Road here as state land and the south side opposite as a private house lot (the house on the aerial): keep to the north side.'),SRCM,conf='lead'),
# kdmsf10  rank 0.61  verdict note: two-part walled pit at the fork of South Road; the 1890 sheet draws a building at the fork, the 1947 sheet none
N('lidar-south-hawley-road-fork-cellar','Two-part pit at the South Hawley crossroads','Hawley','pv','lidar','traces',42.547706,-72.914091,'exact','public','hike','','before 1890–before 1947',
  'The 1890 printing of the USGS Hawley sheet draws a building at this spot (22 m off by the search\'s measure), on the north side of the road just east of where a north-to-south road crosses it, at the west end of the name South Hawley. The 1947 survey (Plainfield sheet) draws South Road and the junction and no building here.'+DCR,
  'On LiDAR: a pit in two parts with straight, steep sides, about 11 by 16 m over all and 1.2 m deep, about 12 m north of the road just east of a fork, with a low straight bank running north from it for about 40 m. The leaf-off aerial shows woods and nothing standing. Not checked on the ground.',
  'A two-part pit with straight sides, exactly where the 1890 map puts a building at the South Hawley crossroads.',
  ACC('2.3',('3.4','east-north-east'),'this pit is about 12 m north of South Road. The parcel records show state land on both sides of the road here; a private house lot begins on the south side about 100 m to the east.'),SRCM,conf='lead'),
# kdmsf2  rank 1.01  verdict note: rectangular pit beside the old Middle Road where a track forks; the 1890 sheet draws a building here, the 1947 sheet none
N('lidar-hawley-middle-road-fork-cellar','Pit in the fork of two old roads on Middle Road, Hawley','Hawley','pv','lidar','traces',42.558221,-72.90184,'site','public','hike','','before 1890–before 1947',
  'The 1890 printing of the USGS Hawley sheet draws the road that runs north from South Hawley (Middle Road on later maps) with a building on its west side beside a brook, about 65 m from this pit by the search\'s measure, and more buildings further along the road. The 1947 survey (Plainfield sheet) draws Middle Road here with marsh on both sides and no building.',
  'On LiDAR: a rectangular pit about 10 by 11 m and 1.4 m deep, the deepest of the four, in the angle where two old tracks part, a few metres east of the western one. The leaf-off aerial shows conifers and hardwoods and nothing standing. Not checked on the ground.',
  'The deepest pit of the four, in the fork of two abandoned roads.',
  ACC('3.3',('2.0','east'),'this pit is a few metres off the old road.'),SRCM,conf='lead'),
# kdmsf14  rank 0.59  verdict note: pit touching the west side of the old Middle Road; the 1890 sheet draws a building on the road here, the 1947 sheet none
N('lidar-hawley-middle-road-cellar','Roadside pit on old Middle Road, Hawley','Hawley','pv','lidar','traces',42.554762,-72.899608,'exact','public','hike','','before 1890–before 1947',
  'The 1890 printing of the USGS Hawley sheet draws a building on the east side of the road that runs north from South Hawley (Middle Road on later maps), about 56 m from this pit by the search\'s measure, and another at a bend about 270 m to the south-south-west. The 1947 survey (Plainfield sheet) draws only the road here.',
  'On LiDAR: a pit about 6 by 11 m and 0.8 m deep touching the west side of the old road. The leaf-off aerial shows hardwoods with conifers to the west and nothing standing. Not checked on the ground.',
  'A pit right on the edge of an abandoned road, 400 m from the next one.',
  ACC('3.4',('1.9','east'),'this pit touches the west side of the old road.'),SRCM,conf='lead'),
]
PIN_NOTES={
 'lidar-south-hawley-south-road-cellar':'The pin is the pit on LiDAR. The 1890 sheet draws no building exactly here; the nearest clear ones are about 130 m and 230 m away. On the aerial the pin is in woods north of South Road; a house and an outbuilding stand south of the road about 135 to 150 m to the south-east, on a private lot. Looked at on LiDAR and the leaf-off aerial; not seen on the ground.',
 'lidar-south-hawley-road-fork-cellar':'The pin is the pit on LiDAR. The building on the 1890 sheet is drawn about 22 m away. Looked at on LiDAR and the leaf-off aerial; not seen on the ground.',
 'lidar-hawley-middle-road-fork-cellar':'The pin is the pit on LiDAR. The building on the 1890 sheet is drawn about 65 m away; sheets of that scale can be 50 to 100 m out. Looked at on LiDAR and the leaf-off aerial; not seen on the ground.',
 'lidar-hawley-middle-road-cellar':'The pin is the pit on LiDAR. The building on the 1890 sheet is drawn about 56 m away; sheets of that scale can be 50 to 100 m out. Looked at on LiDAR and the leaf-off aerial; not seen on the ground.',
}
