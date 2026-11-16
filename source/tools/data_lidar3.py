# November 16, 2026: a third round of LiDAR finds, from a sweep of 26 state forests, state parks and wildlife areas
# within about 40 miles of Albany (tools/lidar_sweep.py). The oldest USGS 15-minute sheets draw 724 buildings inside
# those units; 264 LiDAR pits lie within 90 m of one. The best-ranked 35 were looked at on LiDAR, the leaf-off aerial
# and two old maps side by side; the seven below are the ones where all of them agree and the ground is public.
# Set aside: pits beside a paved road or a parking area, a pit on a pond shore, a house lot that is private, rough
# LiDAR under conifers in Charleston State Forest, and anything where the pattern was not clear.
# Nothing here has been seen on the ground. Every entry is conf='lead' and says exactly what the evidence is:
#   LiDAR  - NYS "Latest_DEM" ground model, read through tools/lidar_dem.py
#   old    - USGS 15-minute sheets (1:62,500): Hoosick 1897, Berne 1900, Gilboa 1901, Schoharie 1898
#   1940s  - USGS Grafton 1946 and North Pownal 1946 (1:31,680); Altamont 1944, Livingstonville 1945 and
#            Middleburgh 1944 (1:24,000)
#   aerial - NYS leaf-off orthoimagery
#   parcel - NYS tax parcel record at the pin (tools/parcel.py). Schoharie County is not in that file, so the two
#            Schoharie entries rest on the federal protected-areas database (tools/pad.py) and say so.
from data_b import N
from data_albany2 import PARKS
BATCH={'key':'lidar3','label':'LiDAR finds: a sweep of 26 forests and parks','added':'2026-11-16 20:00'}
SRC=[['USGS historical topographic maps (topoView)','https://ngmdb.usgs.gov/topoview/viewer/']]
HUNT=' The forest is hunted: wear orange in season.'
GRAFTON=' The park is open all year from 8 am to sunset and charges $8 a vehicle from Memorial Day weekend to Labor Day. Which parking area is nearest was not worked out.'
NOPARCEL='No tax-parcel record could be checked: Schoharie County is not in the state\'s public parcel file. The federal protected-areas database puts the spot inside %s, open to the public, and the nearest road OpenStreetMap names is %s. State forest edges are a patchwork with private lots between, so confirm with the Owner? button or the yellow state boundary signs before you leave the road.'
PLACES=[
N('lidar-spencer-hollow-walled-yard','Walled yard and pit above Spencer Hollow','Petersburgh','renss','lidar','traces',42.795560,-73.316688,'exact','public','hike','','before 1897–before 1946',
  'The 1897 USGS survey draws a building here on the east side of a north–south road, and a second about 180 m to the east. On the 1946 survey the road is an unimproved track that turns east at this spot and ends at the second building, which is still drawn. Nothing is drawn here.',
  'On LiDAR: a round pit about 9 by 7 m and 0.8 m deep with a raised rim, inside straight raised lines that make a rectangle roughly 70 by 50 m, with the two parallel banks of an old road along its west side. It is the clearest pattern of this round and reads as a walled yard with a cellar or well in it. The leaf-off aerial shows woods and nothing standing. Not checked on the ground.',
  'A farmyard whose walls still show from the air, off the map by 1946.',
  'State land: the tax parcel under the pin is a 1,540-acre lot owned by the state, in Taconic Ridge State Forest. The nearest road OpenStreetMap names is Spencer Hollow Road. No marked trail or parking place for this spot was found, so check the state forest map for the legal way in.'+HUNT,SRC,conf='lead'),
N('lidar-second-pond-road-pit','Ringed pit on the old road east of Second Pond','Grafton','renss','lidar','traces',42.782474,-73.441292,'exact','public','hike','','before 1897–before 1946',
  'The 1897 USGS survey draws a building on the east side of the road here, east of Second Pond. The 1946 survey draws the road and no building.',
  'On LiDAR: a round pit about 5 by 6 m and 1 m deep with a raised rim, a few metres east of the line of the old road. A pit this small and round may be a well or a root cellar and not a house cellar. The leaf-off aerial shows the old road as a path through woods and nothing standing. Not checked on the ground.',
  'A house on the 1897 map, a ringed pit in the woods now.',
  'State land: the tax parcel under the pin is the 1,906-acre Grafton Lakes State Park lot. OpenStreetMap names the old road North Long Pond Road.'+GRAFTON,SRC+[PARKS('Grafton Lakes State Park','grafton-lakes-state-park')],conf='lead'),
N('lidar-long-pond-road-cellar','Cellar pit on the old road east of Long Pond','Grafton','renss','lidar','traces',42.787473,-73.436672,'exact','public','hike','','before 1897–before 1946',
  'The 1897 USGS survey draws a building on the east side of the road here, east of Long Pond. The 1946 survey draws the road with a clearing round this spot and no building; the nearest one it draws is about 130 m to the north-east.',
  'On LiDAR: a sharp-edged rectangular pit about 6 by 9 m and 0.8 m deep, about 15 m east of the line of the old road, which shows as a long straight trench. The leaf-off aerial shows the old road as a path through woods and nothing standing. Not checked on the ground.',
  'A square-cornered cellar beside a road the park has let go back to a path.',
  'State land: the tax parcel under the pin is the 1,906-acre Grafton Lakes State Park lot. OpenStreetMap names the old road North Long Pond Road. It is about 700 m north-east along that road from the ringed pit east of Second Pond.'+GRAFTON,SRC+[PARKS('Grafton Lakes State Park','grafton-lakes-state-park')],conf='lead'),
N('lidar-mill-pond-building-site','Building site at the corner of Mill Pond','Grafton','renss','lidar','traces',42.776447,-73.446089,'site','public','hike','','on the 1946 map',
  'The 1946 USGS survey draws a building here at the end of a short lane that runs down to the north-east corner of Mill Pond, and another about 75 m to the south. On the 1897 survey the spot falls at the corner of the pond, and the sheet is too small in scale to say whether a building is drawn.',
  'On LiDAR: a cluster of square-cornered hollows and mounds over about 30 m beside the pond, with an old lane coming down to it from the north, and three pits between 7 and 12 m across and about 0.9 m deep within 70 m. It reads as the footings of more than one building. The leaf-off aerial shows woods to the water and nothing standing. Not checked on the ground.',
  'Two buildings on the 1946 map beside Mill Pond; footings in the woods now.',
  'State land: the tax parcel under the pin is the 1,906-acre Grafton Lakes State Park lot. OpenStreetMap maps a path it calls Mill Pond Trail beside the spot.'+GRAFTON,SRC+[PARKS('Grafton Lakes State Park','grafton-lakes-state-park')],conf='lead'),
N('lidar-beaver-dam-road-house-site','House site off Beaver Dam Road at Thacher Park','Berne','albco','lidar','traces',42.639781,-74.017859,'exact','public','walk','','before 1900–after 1944',
  'The 1900 USGS survey draws two buildings here beside a road. The 1944 survey still draws buildings at the spot, at a road junction.',
  'On LiDAR: one small sharp pit about 6 m across and 1 m deep on gently sloping ground. About 50 m to the west and north-west the ground drops away sharply, and a wider aerial shows a large patch of bare ground there. The leaf-off aerial shows an opening in the woods ringed by evergreens at the pin and nothing standing. A pit this small and round may be a well, or it may be natural; it needs a look on the ground. Not checked.',
  'Buildings on the maps of 1900 and 1944, a small state lot and a pit today.',
  'State land: the tax parcel under the pin is a 1.1-acre state park lot on Beaver Dam Road, at Thacher State Park. OpenStreetMap maps a path it calls the Purple Trail beside the spot. The park is open all year from sunrise to sunset; its vehicle fee varies by place and season. Hunting is allowed in the park away from roads, buildings and trails: wear orange in season.',SRC+[PARKS('Thacher State Park','thacher-state-park')],conf='lead'),
N('lidar-leonard-hill-farmstead','Farmstead site on Leonard Hill','Gilboa','scho','lidar','traces',42.459189,-74.345549,'exact','public','hike','','before 1901–before 1945',
  'The 1901 USGS survey draws a building at this spot, on a road south-east of the hamlet it labels Broome Center. The 1945 survey draws a road to the north-east and nothing here.',
  'On LiDAR: two hollows about 25 m apart. The eastern one, under the pin, is squarish, about 14 by 11 m and 1.5 m deep, the deepest of this round; the western one is larger and more ragged. That is the pattern of a house cellar with a barn foundation beside it. The leaf-off aerial shows open hardwoods and nothing standing. Not checked on the ground.',
  'A house and barn on the 1901 map, two hollows in open woods now.',
  NOPARCEL%('Leonard Hill State Forest','Leonard Mountain Road')+HUNT,SRC,conf='lead'),
N('lidar-dutton-ridge-ringed-pit','Ringed pit on Dutton Ridge','Broome','scho','lidar','traces',42.526304,-74.272597,'exact','public','hike','','before 1898–before 1944',
  'The 1898 USGS survey draws a building here at a bend in a road. On the 1944 survey the road runs about 200 m to the west with buildings along it, and nothing is drawn here.',
  'On LiDAR: a pit about 8 by 6 m and 1 m deep inside a raised ring about 15 m across, with a second small hollow beside it. A ring like that is the spoil thrown up round a cellar, or the bank of a dug pond or spring: only a visit will tell. The leaf-off aerial shows a line of evergreens and brush through open hardwoods, like an old hedgerow, and nothing standing. Not checked on the ground.',
  'The road moved away; the pit and its ring stayed.',
  NOPARCEL%('Dutton Ridge State Forest','Anderson Road')+HUNT,SRC,conf='lead'),
]
PIN_NOTES={
 'lidar-spencer-hollow-walled-yard':'The pin is the LiDAR pit inside the walled rectangle. The building symbol on the 1897 sheet is about 25 m to the north. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-second-pond-road-pit':'The pin is the LiDAR pit. The building symbol on the 1897 sheet is about 40 m to the north-east; sheets of that scale can be 50 to 100 m off. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-long-pond-road-cellar':'The pin is the LiDAR pit. The building symbol on the 1897 sheet is about 40 m to the north. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-mill-pond-building-site':'The pin is the northern LiDAR pit of the cluster; the building symbol on the 1946 sheet is about 30 m to the north-east and the other pits are within 70 m to the south. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-beaver-dam-road-house-site':'The pin is the LiDAR pit. The two building symbols on the 1900 sheet are 14 and 19 m away. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-leonard-hill-farmstead':'The pin is the eastern LiDAR hollow. The building symbol on the 1901 sheet is 10 m away. Looked at on LiDAR and the leaf-off aerial.',
 'lidar-dutton-ridge-ringed-pit':'The pin is the LiDAR pit. The building symbol on the 1898 sheet is 9 m away. Looked at on LiDAR and the leaf-off aerial.',
}
