# November 26, 2026: three places round the Kansas City edge that earlier batches left out: a relocated one-room school in Independence,
# an 1835 log cabin in Harrisonville, and a lake-side club community at Bonner Springs. Each fact comes from a page opened in this
# session: the Jackson County Historical Society, the Cass County Public Library's "Early Cass County" panel, Clio, and the
# National Register form for the Lake of the Forest (the National Park Service's full text).
from data_b import N
from data_ma import W

PLACES = [
N('howard-schoolhouse-independence-mo', 'William Bullitt Howard Schoolhouse, Independence', 'Independence', 'kcmo', 'civic', 'standing',
  39.09340, -94.41520, 'site', 'open', 'drive', '', '1870s',
  'William and Mary Howard built this one-room frame school behind their home in Lee\'s Summit, in the early 1870s, for their own children. Their grandson gave it to the Jackson County Historical Society, and volunteers moved it to the courtyard of the 1859 jail in Independence in 1959; it was opened to visitors in June 1960. The building is small, 12 by 16 feet. Concern about its foundation closed it for a time, and it was lifted off the foundation and set back down on a new one before it reopened to school groups and visitors.',
  look='A tiny frame schoolroom in the jail courtyard, set out as an elementary school of the 1870s. The society says it is restored. The 1870 date used in some places is an estimate: its own page says the early 1870s, and a society article says it was finished in or around 1870. Inside the room was not checked.',
  accn='Owned by the Jackson County Historical Society, which also owns the 1859 jail beside it. It is on the jail museum grounds at 217 N. Main Street. The society says there is free parking across the street and parking along the street. Admission is paid at the door of the museum; the museum says its site is a historic building and is not ADA compliant. The hours given are the museum\'s, from its visit page; the schoolhouse has no separate times on that page.',
  hours='April to October: Tuesday to Saturday 10 a.m. to 4 p.m.; also weekends in December (museum hours; closed Sunday and Monday)',
  links=[['Jackson County Historical Society: Howard Schoolhouse', 'https://www.jchs.org/howardschoolhouse'], ['Jackson County Historical Society: plan your visit', 'https://www.jchs.org/plan-your-visit'], ['Jackson County Historical Society: Saving the Howard Schoolhouse', 'https://www.jchs.org/jchs-e-journal/2025/2/14/saving-the-howard-schoolhouse']],
  conf='mixed', brick='no', th=[39.09343, -94.41457], thn='Parking lot on North Lynn Street (the society names a free lot across the street, not which one)',apart='jackson-county-1859-jail-independence-mo: a one-room school moved onto the jail museum grounds; the jail is its own building'),

N('sharp-hopper-log-cabin-harrisonville-mo', 'Sharp-Hopper Log Cabin (1835), Harrisonville', 'Harrisonville', 'kcmo', 'landmark', 'standing',
  38.65329, -94.34605, 'area', 'ask', 'drive', '', '1835',
  'Samuel Sharp\'s family, who came from Patrick County, Virginia, built this two-room log house in 1835, on a farm north of what is now Harrisonville. Only two families owned the farm until 1974, when a rock quarry was about to take the site. The owners then gave the cabin to the Cass County Historical Society, which moved it to Harrisonville and rebuilt it; the panel says it cannot be on the National Register because it was moved.',
  look='A large cabin for its day, 34 feet by 18 feet 3 inches, one storey, with a room at each end and a fireplace in each. The library\'s panel names the logs (walnut, oak, elm and maple cut on the farm), notched and dovetailed corners, clay-and-wattle filling between the logs, four-inch oak tongue-and-groove floor boards, hand-split lath under lime plaster, and square hand-forged nails. The door casings are the one part of milled lumber, and the doors are replicas.',
  accn='Run by the Cass County Historical Society at 400 E. Mechanic Street. The Cass County Public Library\'s panel says the cabin is open for tours by calling the society (816-380-4396), and Clio says it is also opened for special events. Tour by arrangement only; no open hours were read from a page of the society, so hours are not checked. The pin is the street address from the ArcGIS geocoder, not the cabin: the cabin\'s spot on the lot was not checked.',
  links=[['Cass County Public Library: Early Cass County, the Sharp-Hopper Log Cabin', 'https://www.casscolibrary.org/casscountyhistory/panel2/'], ['Clio: Sharp-Hopper Log Cabin', 'https://www.theclio.com/web/entry?id=38874'], ['Cass County Historical Society (Western Missouri history)', 'https://www.westmohistory.org/html/cass_hist.html']],
  conf='mixed', brick='?'),

N('lake-of-the-forest-district-bonner-springs-ks', 'Lake of the Forest Historic District, Bonner Springs', 'Bonner Springs', 'ks', 'town', 'standing',
  39.06873, -94.84182, 'area', 'view', 'drive', '', '1888–1934',
  'Mission Creek was dammed about 1888 to make a lake for cutting ice, and ice cutting went on until about 1909. In December 1910 a group bought 810 acres and formed the Lake of the Forest Club, a private summer colony of cottages round a spring-fed lake of about 30 acres. It was listed on the National Register in 1996. The form counts ten resources, among them a limestone clubhouse of 1917, a limestone caretaker\'s house of about 1911, stone retaining walls, a stone staircase, the entrance structure and a brick pump house of about 1918.',
  look='A lake with stone walls and old cottages built up the hillsides, a two-storey Shingle and Craftsman clubhouse with a ballroom, stage and stone fireplace, and stonework laid out under the club member C. A. Chandler, who is named in the form as landscape gardener of Swope Park. Union Pacific stone walls run south of the lake near the old depot. Most of this is inside a private community, and what can be seen from the road was not checked.',
  accn='A private community on K-32, about 9/10 of a mile west of Edwardsville. The form says the entrance buildings provide security and monitoring of people coming into it, so treat it as view from the public road only, and ask the club before going in. It is not on mapped public land. There is no public parking: park nowhere on private roads. The pin is the lake as OpenStreetMap shows it, not a building.',
  links=[['National Register form, Lake of the Forest Historic District (National Park Service)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/95001553_text'], ['Kansas Historical Society: Wyandotte County register listings', 'https://www.kansashistory.gov/natreg/natreg_listings/search/page:2/county:WY/records:all']],
  conf='mixed', brick='some'),
]
BATCH={'key':'kcmo_cass_hxjn','label':'Kansas City, Missouri','added':'2026-11-26 03:52'}
PIN_NOTES={
'howard-schoolhouse-independence-mo':'Placed beside the 1859 jail pin (the schoolhouse is in the jail courtyard); on the aerial the ring falls on the small buildings of the jail block; the schoolhouse itself is too small to pick out.',
'sharp-hopper-log-cabin-harrisonville-mo':'The ArcGIS geocoder\'s point for 400 E. Mechanic Street, Harrisonville, the address the library gives for the cabin. On the aerial the point falls on a large white building; the cabin is too small to pick out, so the pin marks the address only.',
'lake-of-the-forest-district-bonner-springs-ks':'OpenStreetMap\'s point for the lake, which falls in open water on the 2024 aerial; the district\'s buildings lie round the lake and the pin marks the area only.',
}
