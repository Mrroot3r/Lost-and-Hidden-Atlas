# November 16, 2026: LiDAR finds. Places nobody pointed to: each was found by scanning the state's LiDAR ground model
# for cellar-hole-sized pits and matching them to buildings drawn on old USGS survey sheets (GUIDE.md section 13).
# Nothing here has been seen on the ground. Every entry is conf='lead' and says exactly what the evidence is:
#   LiDAR  - NYS "Latest_DEM" ground model, read through tools/lidar_dem.py
#   1900   - USGS Berne 15-minute sheet, 1900 edition (1:62,500)
#   1946   - USGS Rensselaerville 7.5-minute sheet, 1946 (1:24,000)
#   aerial - NYS leaf-off orthoimagery
#   parcel - NYS tax parcel record at the pin (tools/parcel.py); private owners are not named here
# The owner of the Atlas adds finds of their own to this category from the app.
from data_b import N
BATCH={'key':'lidar','label':'LiDAR finds','added':'2026-11-16'}
SRC=[['USGS historical topographic maps (topoView)','https://ngmdb.usgs.gov/topoview/viewer/'],['Helderberg Hilltowns: Partridge Run','https://albanyhilltowns.com/Partridge_Run']]
HIST='Most of the hill farms on West Mountain were bought up by the federal Resettlement Administration in the 1930s, and many had been abandoned before that.'
PLACES=[
N('lidar-bradt-hollow-cellar','Cellar pit off Bradt Hollow Road','Berne','albco','lidar','traces',42.560654,-74.172735,'exact','ask','hike','','before 1900–before 1946',
  'A house stood here on a road in 1900, according to the USGS survey of that year. On the 1946 survey the road has become a dashed track and the house is gone. '+HIST,
  'On LiDAR: one sharp pit about 8 by 9 m and about 0.9 m deep beside an old road trace, with a smaller pit about 55 m to the south-east. The leaf-off aerial shows only bare hardwoods. Nobody has checked it on the ground: it may be a stone-lined cellar or just a hollow.',
  'A farmhouse that left the map between 1900 and 1946.',
  'PRIVATE LAND. The tax parcel under the pin is a private 60-acre lot beside Partridge Run Wildlife Management Area, not part of it. Ask the owner first: the app\'s owner lookup shows who that is. The nearest mapped road is Bradt Hollow Road, about 440 m away.',SRC,conf='lead'),
N('lidar-peasley-road-farmstead','Farmstead pits on Peasley Road','Berne','albco','lidar','traces',42.54915,-74.18975,'site','public','walk','','before 1900–before 1946',
  'The 1900 USGS survey draws two buildings here beside the road. Neither is on the 1946 survey. '+HIST,
  'On LiDAR: two pits within about 25 m of the south side of Peasley Road, with more broken ground just to the north-west. The leaf-off aerial shows hardwoods and nothing standing. Not checked on the ground.',
  '','The tax parcel under the pin belongs to the state Department of Environmental Conservation: Partridge Run Wildlife Management Area. An occupied house on its own private lot is about 115 m to the west along the road; stay east of it. The area is hunted: wear orange in season.',SRC,conf='lead'),
N('lidar-beaver-road-farmstead','Farmstead site off Beaver Road','Berne','albco','lidar','traces',42.56905,-74.18213,'site','public','walk','','before 1900–before 1946',
  'Two buildings stand here beside the road on the 1900 USGS survey, near a stream crossing. They are gone on the 1946 survey, which shows a dammed pond just downstream. '+HIST,
  'On LiDAR: several pits and mounds, the largest about 12 m across, in what the aerial shows as a scrubby clearing among conifers. Some of the digging could be from the pond dam and not from the farm. Not checked on the ground.',
  '','The tax parcel under the pin belongs to the state Department of Environmental Conservation: Partridge Run Wildlife Management Area. The nearest mapped road is Beaver Road, about 45 m away. The area is hunted: wear orange in season.',SRC,conf='lead'),
N('lidar-partridge-run-lost-road','House site on a vanished road, Partridge Run','Berne','albco','lidar','traces',42.55527,-74.16689,'area','public','hike','','before 1900–before 1946',
  'The 1900 USGS survey shows a house here on a north-south road. On the 1946 survey both the house and the road are gone. '+HIST,
  'On LiDAR: pits and an oval bank about 25 m across to the north-east, on rough ground where the LiDAR is noisy. This is the weakest of the four finds: the pits may be natural. Not checked on the ground.',
  '','The tax parcel under the pin belongs to the state Department of Environmental Conservation: Partridge Run Wildlife Management Area. The area is hunted: wear orange in season.',SRC,conf='lead'),
]
PIN_NOTES={
'lidar-bradt-hollow-cellar':'Pin is the centre of the pit as measured on the state LiDAR ground model; the 1900 map\'s building symbol is 7 m away. The leaf-off aerial shows bare woods at the ring.',
'lidar-peasley-road-farmstead':'Pin is between the two pits seen on LiDAR, 30 m east of the 1900 map\'s building symbols. The leaf-off aerial shows woods beside the road.',
'lidar-beaver-road-farmstead':'Pin is the 1900 map\'s building symbol; the pits on LiDAR are spread over about 60 m around it. The leaf-off aerial shows a scrubby clearing.',
'lidar-partridge-run-lost-road':'Pin is the 1900 map\'s building symbol, which can be 50 to 100 m off; no single pit was chosen. The leaf-off aerial shows woods and small clearings.',
}
