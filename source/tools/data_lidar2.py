# November 16, 2026: a second round of LiDAR finds, from three more state forests in the Helderberg hill towns:
# Cole Hill, Partridge Run State Forest (beside the wildlife area scanned first) and Rensselaerville State Forest.
# Method as in GUIDE.md section 13: buildings drawn on the 1900 survey sheet inside each forest, then the state's LiDAR
# ground model, the leaf-off aerial and a 1940s sheet at each one, then the tax parcel.
# Nothing here has been seen on the ground. Every entry is conf='lead' and says exactly what the evidence is:
#   LiDAR  - NYS "Latest_DEM" ground model, read through tools/lidar_dem.py
#   1900   - USGS Berne 15-minute sheet, 1900 edition (1:62,500)
#   1940s  - USGS Westerlo 7.5-minute sheet, 1943, and Rensselaerville 7.5-minute sheet, 1946 (1:24,000)
#   aerial - NYS leaf-off orthoimagery
#   parcel - NYS tax parcel record at the pin (tools/parcel.py); forest names from PAD-US (tools/pad.py)
# Of 33 buildings the 1900 sheet draws inside the three forests, 9 had a LiDAR pit within 90 m; the six below are the
# ones where the pit, the old map and the aerial agree. The rest showed smooth ground, or a pit beside a modern road.
from data_b import N
BATCH={'key':'lidar2','label':'LiDAR finds: three more forests','added':'2026-11-16 15:00'}
SRC=[['USGS historical topographic maps (topoView)','https://ngmdb.usgs.gov/topoview/viewer/']]
HUNT=' The forest is hunted: wear orange in season.'
PLACES=[
N('lidar-cole-hill-farmstead','Farmstead site in Cole Hill State Forest','Berne','albco','lidar','traces',42.598313,-74.112144,'site','public','hike','','before 1900–before 1943',
  'The 1900 USGS survey draws a building here, just west of a north–south road, near a road junction. On the 1943 survey the building is gone and the ground is shown as open land.',
  'On LiDAR: a pit about 9 by 8 m and 0.7 m deep in broken ground, with straight raised lines like old walls to its west. A second pit of the same size lies about 130 m to the south-west beside an old track. The leaf-off aerial shows a brushy opening and nothing standing. Nobody has checked it on the ground.',
  'A farmhouse that left the map between 1900 and 1943.',
  'State land: the tax parcel under the pin is a 370-acre state lot on Irish Hill Road, in Cole Hill State Forest. OpenStreetMap maps a ski trail beside the spot.'+HUNT,SRC,conf='lead'),
N('lidar-bradt-hollow-walled-yard','Walled farmyard on Bradt Hollow Road','Berne','albco','lidar','traces',42.565868,-74.203233,'site','public','walk','','before 1900–before 1946',
  'The 1900 USGS survey draws two buildings here on the west side of the road. Neither is on the 1946 survey, which shows open land with patches of woods.',
  'On LiDAR: straight raised lines forming a rectangle about 40 by 50 m on the west side of the road, with rough ground and a small pit inside it. This is the clearest pattern of the six: it reads as a walled yard or foundation lines, not a single hole. The leaf-off aerial shows a brushy old field with scattered evergreens and nothing standing. Not checked on the ground.',
  'A farmyard you can still see in outline from the air.',
  'State land: the tax parcel under the pin is a 94-acre state lot, in Partridge Run State Forest. The spot is beside Bradt Hollow Road.'+HUNT,SRC,conf='lead'),
N('lidar-cook-hill-crossroads-cellar','Cellar pit at the Cook Hill Road crossroads','Berne','albco','lidar','traces',42.561664,-74.202447,'exact','public','walk','','before 1900–before 1946',
  'The 1900 USGS survey shows buildings round this crossroads, which it marks at 1,837 feet. On the 1946 survey the nearest building is about 100 m to the north and nothing is drawn here.',
  'On LiDAR: a sharp, square-cornered pit about 9 by 8 m and 0.7 m deep with a raised rim, a few metres south of a woods road, and two more hollows about 20 m to the north-west across the road. The leaf-off aerial shows the woods road, hardwoods and young conifers, and nothing standing. Not checked on the ground.',
  'A square pit at a crossroads that once had houses.',
  'State land: the tax parcel under the pin is a 129-acre state lot on Cook Hill Road, in Partridge Run State Forest.'+HUNT,SRC,conf='lead'),
N('lidar-gulf-road-house-site','House site on Gulf Road Extension','Rensselaerville','albco','lidar','traces',42.527621,-74.221234,'exact','public','walk','','before 1900–after 1946',
  'A building is drawn here beside the road on both the 1900 and the 1946 USGS surveys, so it stood into the 1940s at least.',
  'On LiDAR: a sharp pit about 10 m across and 0.75 m deep with a mound beside it, and a small second pit about 45 m to the north. On the leaf-off aerial the pit shows as a brown ring at the edge of a mown clearing beside a woods road, and nothing is standing. The clearing looks kept, perhaps a forest landing, so the pit may have been dug or disturbed in recent years. Not checked on the ground.',
  'A house that was still on the map in 1946 and is a pit today.',
  'State land: the tax parcel under the pin is a 228-acre state lot on Gulf Road Extension, in Rensselaerville State Forest.'+HUNT,SRC,conf='lead'),
N('lidar-scutt-road-house-site','House site off Scutt Road','Rensselaerville','albco','lidar','traces',42.501781,-74.217006,'site','public','walk','','before 1900–before 1946',
  'The 1900 USGS survey draws a building here on a road at the south edge of its sheet. On the 1946 survey the road is a dashed track through a clearing and there is no building.',
  'On LiDAR: a pit about 10 by 9 m and 0.7 m deep, with another about 95 m to the south-east. The leaf-off aerial shows fresh logging right at the spot: a landing, skid roads and slash. The pit may be from the logging and not from the farm. This is the weakest of the six. Not checked on the ground.',
  '',
  'State land: the tax parcel under the pin is a 246-acre state lot on Scutt Road, in Rensselaerville State Forest. Logging was under way when the aerial was flown: keep clear of any work.'+HUNT,SRC,conf='lead'),
N('lidar-gordon-road-pit','Deep pit on Gordon Road','Broome','scho','lidar','traces',42.50104,-74.230153,'exact','ask','walk','','before 1900–before 1946',
  'The 1900 USGS survey draws a building here at the end of a short road spur, at the south edge of its sheet. The 1946 survey shows the road as an unimproved track through a clearing and no building.',
  'On LiDAR: the sharpest pit of the six, about 6 m square and 1.2 m deep with a mound beside it, about 40 m east of the road, and a shallower hollow about 50 m to the north-north-west. The leaf-off aerial shows conifers and brush and nothing standing. A pit this small and deep could be a well or a root cellar and not a house. Not checked on the ground.',
  'Six metres square and over a metre deep, where a house stood in 1900.',
  'OWNERSHIP NOT CONFIRMED. No tax parcel record came back for this spot, which is just over the line in the Town of Broome, Schoharie County. The national public-land database puts it inside Rensselaerville State Forest, but those outlines are rough and take in private lots. Find out whose land it is before walking in: look for state forest boundary signs on Gordon Road.',SRC,conf='lead'),
]
PIN_NOTES={
 'lidar-cole-hill-farmstead':'The pin is the larger LiDAR pit. The building symbol on the 1900 sheet is about 57 m to the south-west of it, within that sheet\'s error.',
 'lidar-bradt-hollow-walled-yard':'The pin is the LiDAR pit inside the walled rectangle. The nearer building symbol on the 1900 sheet is about 37 m away.',
 'lidar-cook-hill-crossroads-cellar':'The pin is the LiDAR pit itself. The nearest building symbol on the 1900 sheet is about 38 m away.',
 'lidar-gulf-road-house-site':'The pin is the LiDAR pit itself. The building symbol on the 1900 sheet is about 66 m away; the 1946 sheet draws the building at the pin.',
 'lidar-scutt-road-house-site':'The pin is the LiDAR pit. The building symbol on the 1900 sheet is about 42 m away.',
 'lidar-gordon-road-pit':'The pin is the LiDAR pit itself. The building symbol on the 1900 sheet is about 13 m away.',
}
