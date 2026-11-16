# November 16, 2026: a fourth round of LiDAR finds, from the same sweep of 26 units as data_lidar3.py.
# The next 36 candidates on the ranked list (tools/lidar_sweep.py rank) were looked at on LiDAR alone; the nine with a
# clear shape were then looked at with the leaf-off aerial and two old maps; the six below held up.
# Set aside this time: pits on pond and lake shores, pits beside paved roads, clusters of pits on rough ground at
# Thacher Park, pits under conifer plantations where the ground model is coarse, and faint hollows.
# Nothing here has been seen on the ground. Every entry is conf='lead'. Sources as in data_lidar3.py:
#   old    - USGS 15-minute sheets (1:62,500): Gilboa 1901, Schoharie 1898, Hoosick 1897, Fonda 1896
#   1940s  - USGS Livingstonville 1945, Middleburgh 1944 and Esperance 1943 (1:24,000); Grafton 1946 (1:31,680)
#   parcel - NYS tax parcel record at the pin (tools/parcel.py). The four Schoharie County entries have none, because
#            that county is not in the state's public parcel file; they rest on the federal protected-areas
#            database (tools/pad.py), as GUIDE.md section 13 allows, and say so.
from data_b import N
from data_lidar3 import SRC,HUNT,NOPARCEL
BATCH={'key':'lidar4','label':'LiDAR finds: six more from the sweep','added':'2026-11-16 21:30'}
PLACES=[
N('lidar-kautz-hollow-ringed-pit','Ringed pit above Kautz Hollow','Pittstown','renss','lidar','traces',42.821766,-73.464638,'exact','public','hike','','before 1897–before 1946',
  'The 1897 USGS survey draws a building about 55 m from here, beside a road that climbs the hill. The 1946 survey draws no building here.',
  'On LiDAR: a pit about 7 by 6 m and 1 m deep inside a strong raised ring, at a spot where two old tracks meet. The ring is heavier than most cellar holes have, so this may be something other than a house: only a visit will tell. The leaf-off aerial shows evergreens and hardwoods and nothing standing. Not checked on the ground.',
  'A pit in a heavy ring where two old tracks meet.',
  'State land: the tax parcel under the pin is a 79-acre lot owned by the state on Kautz Hollow Road, and the protected-areas database names it Pittstown State Forest. OpenStreetMap maps a way it calls Zig Zag near the spot. No parking place for this spot was found, so check the state forest map for the legal way in.'+HUNT,SRC,conf='lead'),
N('lidar-charleston-forest-pits','Cluster of pits in Charleston State Forest','Charleston','mohw','lidar','traces',42.841664,-74.316524,'site','public','hike','','before 1896–before 1943',
  'The 1896 USGS survey draws a building about 60 m from here on a road. The 1943 survey draws a track along that line and no building.',
  'On LiDAR: two or three sharp pits close together, the largest about 12 by 9 m and 1.1 m deep. The ground model is coarse under the trees here, so the shapes are less certain than at the other finds, and the pin could be 60 m from where the house stood. The leaf-off aerial shows brushy woods and nothing standing. Not checked on the ground.',
  'The least certain of this round: deep pits, a rough ground model.',
  'Public land: the tax parcel under the pin is a 201-acre lot classed as state forest on Gillen Road, and the protected-areas database names it Charleston State Forest. OpenStreetMap maps a ski trail near the spot.'+HUNT,SRC,conf='lead'),
N('lidar-juried-road-cellar','Cellar pit in Keyserkill State Forest','Gilboa','scho','lidar','traces',42.484247,-74.371255,'exact','public','hike','','before 1901–before 1945',
  'The 1901 USGS survey draws a building beside a road here. On the 1945 survey the road is a dashed trail, the nearest building is about 200 m to the north, and nothing is drawn here.',
  'On LiDAR: a sharp pit about 6 by 7 m and 0.8 m deep with a raised rim, a few metres from a straight bank or wall line that runs north to south. The leaf-off aerial shows mixed woods and nothing standing. Not checked on the ground.',
  'A rimmed cellar beside a road that shrank to a trail.',
  NOPARCEL%('Keyserkill State Forest','Juried Road')+HUNT,SRC,conf='lead'),
N('lidar-hubbard-hill-cellar','Cellar pit north of Hubbard Hill','Gilboa','scho','lidar','traces',42.451886,-74.339247,'exact','public','hike','','before 1901–before 1945',
  'The 1901 USGS survey draws a building here, north of the hill it labels Hubbard Hill. The 1945 survey draws an open field at this spot and a building about 170 m to the north-east, and nothing here.',
  'On LiDAR: a squarish pit about 7 m across and 0.8 m deep with a raised rim, beside a long straight line, a wall or an old road, that runs from north-west to south-east. The leaf-off aerial shows open hardwoods with fallen trees, a conifer plantation to the north-east, and nothing standing. Not checked on the ground.',
  'A square pit on a wall line, about a kilometre south-east of the Leonard Hill farmstead.',
  NOPARCEL%('Leonard Hill State Forest','Leonard Mountain Road')+HUNT,SRC,conf='lead'),
N('lidar-nickerson-hill-house-site','House site on Nickerson Hill Road, High Knob','Broome','scho','lidar','traces',42.439728,-74.306258,'exact','public','hike','','before 1901–before 1945',
  'The 1901 USGS survey draws a building here on a road beside a stream. On the 1945 survey the spot is woods, and the nearest building it draws is about 350 m to the south-west.',
  'On LiDAR: a pit at the upper end of a larger rectangular hollow about 13 by 10 m and 0.6 m deep, with a woods road about 40 m to the south. The leaf-off aerial shows open hardwoods, a pale patch of bare ground at the pit, and nothing standing. Not checked on the ground.',
  'A wide, shallow hollow 13 m from the house the 1901 map draws.',
  NOPARCEL%('High Knob State Forest','Nickerson Hill Road')+HUNT,SRC,conf='lead'),
N('lidar-gates-hill-pits','Two pits on an old road line, Gates Hill','Fulton','scho','lidar','traces',42.522320,-74.368477,'exact','public','hike','','before 1898–before 1944',
  'The 1898 USGS survey draws a building here on a road. The 1944 survey draws only a trail along the same line.',
  'On LiDAR: two pits a few metres from a long straight line that crosses the frame, which the leaf-off aerial shows as a row of evergreens: an old wall or the edge of the old road. The larger pit is about 12 by 11 m and 0.7 m deep, the smaller about 5 by 6 m and 0.8 m deep. Nothing is standing. Not checked on the ground.',
  'A house on the 1898 map; two pits beside a hedgerow now.',
  NOPARCEL%('Gates Hill State Forest','Evieann Road')+HUNT,SRC,conf='lead'),
]
PIN_NOTES={
 'lidar-kautz-hollow-ringed-pit':'The pin is the LiDAR pit. The building symbol on the 1897 sheet is about 55 m away; sheets of that scale can be 50 to 100 m off. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-charleston-forest-pits':'The pin is the largest LiDAR pit. The building symbol on the 1896 sheet is about 60 m away, so the pin is rated "on site", not exact. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-juried-road-cellar':'The pin is the LiDAR pit. The building symbol on the 1901 sheet is about 40 m away. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-hubbard-hill-cellar':'The pin is the LiDAR pit. The building symbol on the 1901 sheet is about 25 m away. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-nickerson-hill-house-site':'The pin is the LiDAR hollow. The building symbol on the 1901 sheet is 13 m away. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-gates-hill-pits':'The pin is the larger LiDAR pit; the smaller is about 17 m to the north. The building symbol on the 1898 sheet is about 40 m away. Looked at on LiDAR and the leaf-off aerial.',
}
