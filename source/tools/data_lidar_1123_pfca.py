# November 23, 2026: LiDAR finds in Platte Falls Conservation Area, drafted by tools/lidar.py (method: LIDAR.md).
# Every entry is an unverified lead (conf='lead'): a pit on the LiDAR ground model beside a building on an old
# USGS sheet, nothing standing on the satellite picture, on land the records show as public. Nothing was seen on the ground.
from data_b import N
from data_lidar3 import SRC
SRCP=SRC+[['Missouri Department of Conservation: Platte Falls Conservation Area','https://mdc.mo.gov/discover-nature/places/platte-falls-conservation-area']]
MDC=(' The Missouri Department of Conservation opens the area from 4 am to 10 pm daily; its page names no fee. Vehicles are kept to'
     ' gravel and paved roads and established parking areas, and the area is hunted in season (firearms deer November 14 to 24, 2026,'
     ' and other seasons): wear orange.')
BATCH={'key':'lidar_1123_pfca','label':'LiDAR finds: Platte Falls Conservation Area, Missouri','added':'2026-11-23 18:27'}
PLACES=[
# pfca8  rank 0.65
N('lidar-platte-falls-lane-end-farm-site','Farm site at a lane end, Platte Falls','Fair township','kcmo','lidar','traces',39.393318,-94.754047,'exact','public','hike','','before 1910',
  'The 1910 USGS survey (Leavenworth sheet) draws a building about 48 m from here, at the west end of a short lane that runs east to the north-south road; a railway crosses the hills to the north-west. The 1951 survey (Tracy sheet) draws a cluster of several buildings at this spot, where the lane meets the road.',
  'On LiDAR: two sharp pits about 30 m apart, north and south, on level ground about 45 m west of the gravel road; this one is about 8 by 11 m and 0.7 m deep. The satellite picture (not a leaf-off flight) shows grass and scrub with trees round it, pale scattered debris beside the pits that could be fallen roofing or dumped material, and no roof. A building with a gravel yard stands about 80 m to the south-west. Not checked on the ground.',
  'A farm drawn in 1910 and still drawn in 1951, now two pits and debris in the scrub.',
  'State land: the tax parcel under the pin is a 350.0-acre lot owned by the state, in Platte Falls Conservation Area. The pit is about 45 m west of a gravel road; whether that road is open to cars was not checked. The nearest mapped parking lot is on Settle Station Road, about 630 m south-west.'+MDC,SRCP,conf='lead',brick='?',th=[39.38887,-94.75859],thn='Parking lot on Settle Station Road'),
# pfca5  rank 0.69
N('lidar-settle-station-road-house-site','House site in the woods near Settle Station Road','Fair township','kcmo','lidar','traces',39.397581,-94.75017,'exact','public','hike','','before 1910',
  'The 1910 USGS survey (Leavenworth sheet) draws a building about 59 m from here, at the corner where a road from the west meets a north-south road, right at the east edge of the sheet. The 1951 survey (Tracy sheet) draws a small building about 25 m from the pit.',
  'On LiDAR: a sharp pit about 9 by 6 m and 1.0 m deep on level ground, with low bumps just south of it. The satellite picture (not a leaf-off flight) shows bare woods with a field to the east, a gravel turnaround about 70 m north-west, and nothing standing at the pit. Not checked on the ground.',
  'A sharp pit in the woods where two old maps draw a house.',
  'State land: the tax parcel under the pin is a 355.1-acre lot owned by the state, in Platte Falls Conservation Area. The nearest road OpenStreetMap names is Settle Station Road. A gravel turnaround is about 70 m north-west; whether it is a parking place was not checked. A roofed building stands about 120 m north, past the edge of the woods; whose land that is was not checked, so keep to the conservation area. The nearest mapped parking lot is on Settle Station Road, about 1.2 km south-west.'+MDC,SRCP,conf='lead',brick='?',th=[39.38887,-94.75859],thn='Parking lot on Settle Station Road'),
# pfca11  rank 0.61
N('lidar-platte-falls-river-bend-house-site','House site in a bend of the Platte River','Carroll township','kcmo','lidar','traces',39.380971,-94.769581,'exact','public','walk','','before 1910',
  'The 1910 USGS survey (Leavenworth sheet) draws two buildings here, one on each side of a lane on high ground inside a bend of the Platte River, the nearer about 54 m from the pit. The 1951 survey (Tracy sheet) draws buildings about 75 and 95 m away; whether either is the same farm could not be told.',
  'On LiDAR: a small pit about 13 by 6 m and 0.9 m deep in a levelled patch, inside a curving bank that opens to the south-west, about 90 m east of a gravel road. The satellite picture (not a leaf-off flight) shows woods with a small clearing and patches of bare ground, and nothing standing. Not checked on the ground.',
  'Two buildings on the 1910 map, a levelled yard and a pit in the woods today.',
  'State land: the tax parcel under the pin is a 153.9-acre lot owned by the state, in Platte Falls Conservation Area. The nearest mapped parking lot is on Knighton Lane, about 210 m north; the pit is about 90 m east of the gravel road.'+MDC,SRCP,conf='lead',brick='?',th=[39.38285,-94.76954],thn='Parking lot on Knighton Lane'),
]
PIN_NOTES={
 'lidar-platte-falls-lane-end-farm-site':'The pin is the pit on LiDAR. The building on the 1910 sheet is drawn about 48 m away; sheets of that scale can be 50 to 100 m out. Looked at on LiDAR and a satellite picture; not seen on the ground.',
 'lidar-settle-station-road-house-site':'The pin is the pit on LiDAR. The building on the 1910 sheet is drawn about 59 m away; sheets of that scale can be 50 to 100 m out. Looked at on LiDAR and a satellite picture; not seen on the ground.',
 'lidar-platte-falls-river-bend-house-site':'The pin is the pit on LiDAR. The buildings on the 1910 sheet are drawn about 54 m away; sheets of that scale can be 50 to 100 m out. Looked at on LiDAR and a satellite picture; not seen on the ground.',
}
