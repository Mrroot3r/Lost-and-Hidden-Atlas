# November 24, 2026: Richmond and Ray County, Missouri, with Plattsburg in Clinton County, north-east of Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had no place in Richmond or Plattsburg.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), the Ray County Historical Society's
# own visitor page (the museum's tour of the county), the 2013 National Register form for the Stoutimore House (read in full
# from NPGallery), Clio, and web-search result text for the Bob Ford and Pioneer Cemetery pages.
# The National Register forms for the Ray County listings could not be read: NPGallery holds only a placeholder for each,
# and the Missouri State Historic Preservation Office copies answer HTTP 404.
from data_b import N
from data_ma import W

RCM = ['Ray County Museum: Visit (hours, county tour)', 'https://raycountymuseum.org/home/visit/']

PLACES = [
N('ray-county-courthouse-richmond-mo', 'Ray County Courthouse', 'Richmond', 'kcmo', 'civic', 'standing',
  39.27875, -93.97721, 'site', 'view', 'drive', '', '1914',
  'The Ray County Courthouse in Richmond was built in 1914 as a three-storey Classical Revival building of Bedford limestone. Paired Ionic columns carry a pediment on each of its four fronts. '
  'Wikipedia says its design resembles the Livingston County Courthouse in Chillicothe and that the same architect drew both. It was listed on the National Register of Historic Places in 1979.',
  look='A grey limestone block with a column-and-pediment front on all four sides. On the lawn stand a statue of Alexander Doniphan, unveiled in 1918, a World War I doughboy by the walk, and World War II, Korean War and Vietnam War memorials, all listed on the museum\'s county tour. '
  'Inside not checked.',
  accn='A working county courthouse on the square in Richmond, owned by Ray County. Look from the street. Court and office hours were not checked. OpenStreetMap maps a public lot on West Royle Street, a few blocks south; parking beside the square was not checked.',
  links=[W('Ray County Courthouse'), RCM], brick='no'),

N('ray-county-poor-farm-museum-richmond-mo', 'Ray County Poor Farm (Ray County Museum)', 'Richmond', 'kcmo', 'inst', 'standing',
  39.27278, -93.98889, 'exact', 'open', 'drive', '', '1909–1910',
  'The county built this Y-shaped brick building as its poor farm in 1909 and 1910 to house and care for the poor and indigent. The Ray County Historical Society\'s page says it cost $19,491 with wiring, plumbing and heating, and that it served over the years as a nursing home, a hospital, a jail for juveniles and a shelter. '
  'It is now the Ray County Museum. It was listed on the National Register of Historic Places in 1979.',
  look='A big three-floor building with three wings, 54 rooms and 14-inch masonry walls with fire doors at the wing entrances, about 14,400 square feet in all, according to the Historical Society. Wikipedia and the Society both describe it as brick; the colour of the brick was not checked. '
  'The museum inside holds Civil War, World War I and II, Mormon history and homestead displays, according to its web page; the original rooms were not described.',
  accn='Ray County Museum, 901 West Royle Street, Richmond, run by the Ray County Historical Society. Hours from the museum\'s own page (read November 2026). Parking not checked.',
  links=[W('Ray County Poor Farm'), RCM], brick='?',
  hours='April to November, Wednesday to Saturday, 12 to 4 p.m. Closed December to March.'),

N('dougherty-auditorium-farris-theatre-richmond-mo', 'Dougherty Auditorium (Farris Theatre)', 'Richmond', 'kcmo', 'civic', 'standing',
  39.27833, -93.97917, 'site', 'view', 'drive', '', '1900–1901',
  'Richmond\'s opera house was built in 1900 and 1901 and named for Sam Dougherty, who moved to town in the late 1800s after striking it rich in the Colorado gold fields. It later took the name Farris Theatre. '
  'It is a two-storey brick building 60 by 100 feet, with a Palladian window of sheet metal over the central entrance and a round window on each side. It was listed on the National Register of Historic Places in 1979.',
  look='A plain brick hall with a pressed-metal Palladian window above the door. Wikipedia says it houses a local history museum; the Ray County Museum\'s own page lists it only as a stop on its driving tour, and the museum sits at the poor farm, so whether anything is open inside was not confirmed. Brick colour not checked.',
  accn='Private or not known to open; look from the street. Ownership and any hours were not found.',
  links=[W('Dougherty Auditorium'), RCM], conf='mixed', brick='?'),

N('watkins-house-richmond-mo', 'Watkins House', 'Richmond', 'kcmo', 'landmark', 'standing',
  39.27638, -93.97936, 'site', 'view', 'drive', '', 'about 1890',
  'This Queen Anne house at 302 South Camden Street was designed by the architect George F. Barber and built about 1890. It was listed on the National Register of Historic Places in 1983.',
  look='A frame house covered in five different kinds of shingle, with a porch that wraps round to a six-sided corner tower with a turret roof, a gable with a recessed porch, carved wood panels and a chimney with ornate terra cotta panels. '
  'Barber sold house plans by mail, and this is one of his designs. Interior not checked.',
  accn='A private house on a town street. Look from the sidewalk.',
  links=[W('Watkins House (Richmond, Missouri)')], brick='no'),

N('richmond-pioneer-cemetery-mormon-mo', 'Richmond Pioneer Cemetery (the Mormon cemetery)', 'Richmond', 'kcmo', 'burial', 'standing',
  39.2853, -93.97654, 'area', 'view', 'drive', '', 'about 1830s–1875',
  'The old burying ground at North Thornton and Crispin Streets, north of the courthouse square, holds early settlers of Ray County. The Ray County Museum\'s tour page says it holds several early Latter-day Saints, among them Oliver Cowdery, one of the Three Witnesses to the Book of Mormon, and that Martin Harris and David Whitmer are buried there too. '
  'Other sources are less sure: Clio says Cowdery\'s burial site was found in 1911 and that Jacob Whitmer\'s stone lies flat in concrete, and web-search results list David Whitmer in the city cemetery on West Main instead. '
  'The same museum page gives William "Bloody Bill" Anderson, the guerrilla leader killed near Albany in October 1864, as buried here; a stone was put up for him later. A larger city cemetery was opened about 1875 on West Main Street.',
  look='A small old cemetery with a monument to the Three Witnesses and low stones for the Whitmer family. Who lies under which stone is disputed in places, as above. Pin is at the street corner given by the museum and Clio; the exact lot was not checked on the aerial.',
  accn='A cemetery at the corner of North Thornton and Crispin Streets, Richmond; the owner was not checked (likely the city). The owner was not found and no opening times were found; treat it as look-from-the-street.',
  links=[['The Richmond Pioneer Cemetery (Clio)', 'https://www.theclio.com/entry/38929'], RCM], conf='mixed', brick='?'),

N('bob-ford-grave-richmond-cemetery-mo', 'Bob Ford\'s grave, Richmond Cemetery', 'Richmond', 'kcmo', 'burial', 'marker',
  39.27980, -93.98507, 'area', 'view', 'drive', '', '1892',
  'Bob Ford, the gang member who shot Jesse James in 1882, was killed in Creede, Colorado, in 1892 and was later reburied at Richmond, his family\'s home town. '
  'The museum\'s tour page places the grave in Richmond Cemetery on West Main Street, between Sunny Slope Cemetery and the Shotwell and Woodland Cemeteries. '
  'Sources disagree: a 2009 local newspaper story named Sunny Slope, which the paper later corrected, and a WPA guide excerpt reproduced on Waymarking says an unmarked grave in the old Pioneer Cemetery.',
  look='A grave in the cemetery on the hill. A visitor\'s write-up in a search result says to take the right-hand entrance to the top of the hill and look down the slope to the left, a couple of rows behind the Chenault stone. The pin is a coordinate from a Waymarking entry and was not checked against the ground.',
  accn='A cemetery on West Main Street, Richmond. The owner and opening times were not found, so it is listed as look-from-the-road. A visitor\'s write-up in a search result describes driving in by the right-hand entrance.',
  links=[RCM, ['Waymarking: Grave of Bob Ford', 'https://www.waymarking.com/waymarks/WMK5JT_Grave_of_Bob_Ford_He_Shot_Jesse_James_Richmond_Mo'], W('Robert Ford (outlaw)')], conf='mixed', brick='no'),

N('richmond-bank-206-w-main-mo', 'McCalley, Gorham and Bowman Building (old Hughes-Wasson Bank), 206 West Main', 'Richmond', 'kcmo', 'civic', 'standing',
  39.27862, -93.97824, 'site', 'view', 'drive', '', '1860s',
  'The Ray County Museum\'s tour lists this building at 206 West Main as the old Hughes-Wasson Bank, robbed six times in 1866 and 1867 and reportedly robbed by the James gang on May 23, 1867. A plaque on the building notes the robbery. '
  'It is now a private office. The museum\'s page gives no date for the building and calls the James-gang robbery "reportedly", so treat the story as local tradition.',
  look='A plaque hangs on the front. The building\'s age and what it looks like inside were not checked.',
  accn='A private office on West Main Street, Richmond. Look from the sidewalk.',
  links=[RCM], conf='mixed', brick='?'),

N('new-hope-primitive-baptist-church-richmond-mo', 'New Hope Primitive Baptist Church', 'Richmond', 'kcmo', 'worship', 'standing',
  39.24972, -94.04333, 'site', 'view', 'drive', '', '1897',
  'The congregation was founded about 1820 as North Bluffton and is one of the oldest in Ray County. The church standing now was built in 1897: a one-storey frame Greek Revival meeting house, 30 by 40 feet, with a high gable roof. '
  'A cemetery beside it, with 166 graves from 1856 to 1973, is part of the National Register listing of 1980.',
  look='A plain white-style frame church with a steep gable roof and its churchyard beside it. Interior, services and whether it is open to visitors were not found.',
  accn='A country church on Old Orrick Road off Highway EE, south-west of Richmond. Owned by the congregation. Look from the road; services and visiting times were not found.',
  links=[W('New Hope Primitive Baptist Church'), ['Ray County Genealogy: New Hope Church', 'https://ray.mogenweb.org/histsites/newhope/newhope.htm']], brick='no'),

N('mansur-farmstead-rock-hall-richmond-mo', 'Isiah Mansur Farmstead (Rock Hall)', 'Richmond', 'kcmo', 'landmark', 'standing',
  39.41278, -93.88639, 'area', 'view', 'drive', '', '1842–1945',
  'Rock Hall is a farm near Richmond that grew from the middle of the 1800s into the 1900s. The Wikipedia summary of its 1998 National Register listing names a two-storey, five-bay frame I-house (1842, with an addition of 1858), a buggy house (about 1905), a large barn (about 1909), an engine house (about 1900), and smaller farm buildings, wells and a smokehouse from about 1840 to 1945.',
  look='A working-farm group: the I-house, a big barn and a string of small outbuildings. The pin is the Register\'s point for the farm and was not checked on the aerial. Interior and condition not checked.',
  accn='Private farm. It is not a visitor site; look only from a public road if the buildings can be seen, and do not enter the farm.',
  links=[W('Isiah Mansur Farmstead Historic District')], brick='no'),

N('stoutimore-house-plattsburg-mo', 'David L. and Sallie Ann Stoutimore House (Jenkins House)', 'Plattsburg', 'kcmo', 'landmark', 'standing',
  39.56088, -94.45161, 'site', 'view', 'drive', '', '1892',
  'The Stoutimore House at 501 South Birch Avenue was designed and built in 1892 by a local architect named in the nomination as Joseph H. (the surname is garbled in the scanned form). It is a one-and-a-half-storey Second Empire house with a wood-shingled mansard roof, a finished brick basement and a frame first storey. '
  'The 2013 National Register form says it keeps its original design, materials and workmanship apart from two minor additions, a sunroom and a staircase of the mid-1900s, and that it is one of the houses that show Plattsburg\'s prosperity in the late 1800s.',
  look='A mansard-roofed Victorian house on a street of homes mostly dating from about 1880 to 1920. Interior not checked.',
  accn='A private house in Plattsburg. Look from the sidewalk; the form lists the ownership as private.',
  links=[['National Register nomination form, 2013 (NPGallery)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/13000536_text']], brick='?'),
]

BATCH = {'key': 'kcmo_ray_dqmt', 'label': 'Richmond and Plattsburg, Missouri', 'added': '2026-11-24 06:50'}

PIN_NOTES = {
 'ray-county-courthouse-richmond-mo': 'National Register list coordinate, moved about 28 m south-west onto the courthouse roof seen on the aerial.',
 'ray-county-poor-farm-museum-richmond-mo': 'OpenStreetMap places the Ray County Museum at this spot; it matches the Register point.',
 'dougherty-auditorium-farris-theatre-richmond-mo': 'Coordinate from the National Register list; checked on the aerial.',
 'watkins-house-richmond-mo': 'Address 302 South Camden Street looked up on the ArcGIS geocoder; checked on the aerial.',
 'richmond-pioneer-cemetery-mormon-mo': 'Street corner of North Thornton and Crispin Streets from the ArcGIS geocoder; the cemetery itself is checked on the aerial.',
 'bob-ford-grave-richmond-cemetery-mo': 'Waymarking coordinate for the grave (39 16.788 N, 93 59.104 W); the pin marks the cemetery area, not the stone.',
 'richmond-bank-206-w-main-mo': 'Address 206 West Main Street looked up on the ArcGIS geocoder; checked on the aerial.',
 'new-hope-primitive-baptist-church-richmond-mo': 'Coordinate from the National Register list; checked on the aerial.',
 'mansur-farmstead-rock-hall-richmond-mo': 'National Register list coordinate for the farm. On the aerial it falls in an open field about 150 m from a group of farm buildings east of the road; which group is Rock Hall was not confirmed, so the pin marks only the general area.',
 'stoutimore-house-plattsburg-mo': 'Coordinate in the 2013 National Register form and the address 501 South Birch Avenue; checked on the aerial.',
}
