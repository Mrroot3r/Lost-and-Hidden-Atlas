# November 21, 2026: Yates County, New York (Penn Yan, the Keuka Lake Outlet, Dresden, Bluff Point, Dundee, Middlesex),
# with the Sampson Military Museum just over the line in Seneca County. Drawn at random by tools/choose.py --state ny
# (region wny, which offered Penn Yan); the Atlas had nothing within 20 km of Penn Yan.
# Sources opened in this session: Wikipedia as raw text (tools/wiki_raw.py, including the Yates County Register list),
# Frances Dumas's series on the Outlet mills in the Crooked Lake Review (1989-1990, and the Friends of the Outlet's
# reprint of its first part), uncoveringnewyork.com (a first-hand visit), TrailLink, the Finger Lakes Land Trust's
# gofingerlakes.org page for the trail, HMdb marker pages, parks.ny.gov (Sampson State Park), garrettchapel.org,
# thebirkettmills.com, the Freethought Trail's Ingersoll museum page and the Yates County Chamber's listing for the
# Penn Yan Theatre Company. The Register forms for the Outlet, Courthouse Park and Penn Yan districts are NPGallery
# placeholders, and yatescountyhistory.org would not connect.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def HM(m,t): return ['HMdb: '+t,'https://www.hmdb.org/m.asp?m='+m]
D1=L('Crooked Lake Review, Frances Dumas: A History of the Crooked Lake Outlet (1989)','https://crookedlakereview.com/articles/1_33/12mar1989/12dumas.html')
D2=L('Crooked Lake Review, Frances Dumas: Seneca Millsite (1989)','https://crookedlakereview.com/articles/1_33/13apr1989/13dumas.html')
D3=L('Crooked Lake Review, Frances Dumas: Cascade Millsite (1990)','https://crookedlakereview.com/articles/1_33/23feb1990/23dumas.html')
D4=L('Crooked Lake Review, Frances Dumas: The Crooked Lake Canal, part two (1990)','https://crookedlakereview.com/articles/1_33/25apr1990/25dumas.html')
UNY=L('Uncovering New York: the waterfalls on the Keuka Lake Outlet Trail','https://uncoveringnewyork.com/?p=1783')
TL=L('TrailLink: Keuka Outlet Trail','https://www.traillink.com/trail/keuka-outlet-trail')
FLLT=L('Finger Lakes Land Trust (Go Finger Lakes): Keuka Outlet Trail','https://www.gofingerlakes.org/locations/keuka-outlet-trail/')
OUT=('The Keuka Outlet Trail, a 6.7-mile rail-trail from Penn Yan to Dresden kept up by the Friends of the Outlet '
     '(keukaoutlettrail.org, whose pages are drawn by script and could not be read here; the Land Trust page names them and '
     'lists restrooms, picnic tables and dogs as allowed). Open to walkers, bikes and horses, skis and snowmobiles in winter. ')

BATCH={'key':'wny_vtcb','label':'Yates County, NY: the Keuka Outlet mills, Penn Yan, Dresden and Bluff Point','added':'2026-11-21 11:42'}

PLACES=[
# ---- The Keuka Lake Outlet ----
N('seneca-mills-falls-keuka-outlet','Seneca Mills Falls and mill ruins','Seneca Mills','wny','industry','ruins',42.66056,-77.00417,'site','public','walk','canal','1790–1933',
  'The first mill on the Outlet, and by its builders\' account the first in western New York, was finished here on July 4, 1790 by followers of Jemima Wilkinson, the Public Universal Friend, with millstones hauled from Connecticut. Mills on both banks burned and were rebuilt through the 1800s; four locks of the Crooked Lake Canal (1833–1877) lifted boats past the falls. In 1884 a large paper mill was built at the falls on foundations of dressed stone taken from those abandoned locks, and by 1889 it was also making electricity for the streets of Penn Yan; later the Yates Electric Light & Power Corp. generated power here.',
  'A waterfall of 30 to 40 feet in three drops (part natural, part dam) ringed by the crumbling stone walls of the mill. Lock 17 is the one canal lock with its stonework still in place: it carries the old road over the Outlet above the dam, and the groove for a lock-gate pivot can be seen. Here the trail leaves the towpath and runs along the floor of the canal; locks 18, 19 and 20 are said to be easy to find a little upstream where the canal ditch deepens between wetlands (Dumas, 1990). Sheer drops off the old walls: keep back from the edges.',
  'The first mill in western New York, its falls framed by the walls of an 1884 paper mill.',
  OUT+'The ground at the falls belongs to Friends of the Outlet, Inc. (the federal land map files it as closed, but TrailLink and the visit write-up describe the trail and picnic area there as open to all). Park in the Outlet Road lot at Seneca Mills and walk about a third of a mile west (upstream) on the trail; there is a picnic area at the falls. Hours not checked.',
  [D2,D4,D1,UNY,TL,FLLT],brick='?'),
N('cascade-mills-falls-keuka-outlet','Cascade Mills Falls and the Taylor chemical works','Milo','wny','industry','ruins',42.66400,-76.98493,'site','public','walk','','1827–1960s',
  'Meredith Mallory built the twelfth and last dam on the Outlet soon after 1827, with a merchant grist mill at the Cascade that the 1835 state census called the largest on the stream. It became the Croton Mills, then from 1866 the Cascade Paper Manufacturing Co., which made newsprint from straw until it burned in March 1869; paper was made again from 1880. In 1900 the chemist Edward R. Taylor bought it and made carbon bisulfide in an electric furnace of his own invention, and under the J. T. Baker Co. name the plant ran into the 1960s, one of the last working mills on the Outlet.',
  'A waterfall of about 15 feet in several drops, a viewing area and a covered picnic pavilion with interpretive displays. Just before the falls the trail crosses a clearing with several abandoned industrial buildings posted No Trespassing; ruins of a mill stand on the far bank (the blog that describes them calls them the Seneca Paper Mill, a name Dumas gives to the mill at Seneca Mills Falls, so which mill they were is not settled here). Rusty metal lies about. Canal locks 8, 9 and 10 at the falls were destroyed by later building.',
  'A paper mill turned chemical works, rotting beside the last falls on the Outlet.',
  OUT+'The nearest mapped lot is at Mays Mills, on the trail about half a mile upstream (west). The buildings are posted: look from the trail and the viewing area. Hours not checked.',
  [D3,D4,UNY,TL,FLLT],conf='mixed',brick='?'),
N('crooked-lake-canal-lock-3-dresden','Crooked Lake Canal, Lock 3 and canal ditch','Dresden','wny','canal','traces',42.67870,-76.96550,'area','public','walk','canal','1830–1877',
  'The Crooked Lake Canal, built 1830–1833, climbed 270 feet in under eight miles between Seneca Lake at Dresden and Keuka Lake at Penn Yan with 27 or 28 locks (the sources differ), at a time when the whole Erie Canal had 90. It never paid its way, was abandoned by the state in 1873 or 1877 (the sources differ), and its stones were carried off for mills and bridges; the Fall Brook Railroad was laid on its towpath in 1884, and the trail followed the railroad after the floods of 1972 ended it.',
  'About a quarter mile upstream (west) of the Route 14 bridge, Lock 3 lies at the head of what Dumas (1990) called an excellent stretch of the original canal ditch, about 42 feet wide at the waterline, with the towpath beside it carrying the trail. Lock 4, just west of the Hopeton access, keeps only a few stones. Locks 1 and 2, below the Dresden trailhead, are on private land. Not checked on the ground.',
  '',
  OUT+'Park at the Dresden trailhead off Seneca Street and walk west under the Route 14 bridge. Hours not checked.',
  [D4,D1,W('Crooked Lake Canal'),TL],conf='mixed',brick='no'),
# ---- Penn Yan ----
N('birkett-mills-penn-yan','The Birkett Mills','Penn Yan','wny','industry','standing',42.66017,-77.05270,'exact','view','walk','','1824',
  'The Birkett Mills has milled grain at Penn Yan since 1797, and calls itself one of the largest buckwheat millers in the world. The first mill burned in 1823; the mill in use today has been working since 1824. On September 27, 1987, at the Buckwheat Harvest Festival, it cooked what was then the world\'s largest pancake, and the 28-foot griddle hangs on the mill.',
  'The long cream-painted mill (as the Commons photograph chosen for it shows) beside the Main Street bridge over the Outlet, with the giant griddle on its wall (HMdb has a marker for it). The trail passes under Main Street across the stream from the mill. A working, stone-grinding mill; interior not checked.',
  'Stone-ground buckwheat from the same mill since 1824.',
  'A working private mill: look from Main Street and the Outlet Trail. No tours were found on its own page.',
  [L('The Birkett Mills: history','https://www.thebirkettmills.com/our-story/history'),HM('105006','Birkett Mills\' World Record Pancake Griddle'),W('Penn Yan Historic District')],brick='no'),
N('penn-yan-historic-district','Penn Yan Historic District (Main Street)','Penn Yan','wny','town','standing',42.66261,-77.05438,'site','public','walk','','1820s–1929',
  'Sixty-five acres of the village with 281 buildings, 210 of them counted as contributing, from the 1820s to 1929: houses, shops, mills, churches and civic buildings, listed in 1985. It takes in the Birkett Mills, the Chronicle Building, the Knapp Hotel, the Castner House, Struble\'s Arcade, the courthouse square and the 1912–13 post office, a red brick Colonial Revival building on a granite basement designed under James Knox Taylor. The Crooked Lake Canal ended here: its boats unloaded in a basin behind the Main Street stores, and its guard lock lay where the Chronicle Building stands.',
  'Walk Main Street from the Outlet bridge north to the courthouse. HMdb has markers on several Main Street buildings (101, 103, 115, 130, 131 and 158 Main) and one at Seneca and Basin streets where a hotel stood on the canal basin. A carved block from the canal stands at Brown and Lake streets.',
  '',
  'Public village streets and sidewalks; the buildings are private or working offices. Street parking; parking rules not checked.',
  [W('Penn Yan Historic District'),W('United States Post Office (Penn Yan, New York)'),D4,HM('139649','Owl\'s Nest'),HM('223429','Crooked Lake Canal Stone')],brick='some'),
N('yates-county-courthouse-park','Yates County Courthouse Park','Penn Yan','wny','civic','standing',42.66500,-77.05750,'site','public','walk','','',
  'Two acres at the north end of the village holding the Yates County Courthouse, the First Baptist Church, the County Office Building, the old jail and the park, listed on the Register as a district in 1979 and since 1985 part of the Penn Yan Historic District. The Civil War monument honours the 2,109 men of the county who served in that war.',
  'The courthouse and its neighbours round the park, with a bandstand and memorials for each American war from the Revolution on (HMdb lists them). The buildings\' dates were not found in a source read here; interiors not checked.',
  '',
  'The county\'s courthouse grounds and park, on public streets; the courthouse and county offices are working buildings. Parking not checked.',
  [W('Yates County Courthouse Park District'),HM('105005','Civil War Memorial'),HM('104998','The Bandstand')],brick='?'),
N('oliver-house-museum-penn-yan','Oliver House Museum (Yates History Center)','Penn Yan','wny','landmark','standing',42.66353,-77.05560,'site','open','walk','','',
  'The Yates County Genealogical and Historical Society, founded in 1860, was given rooms in the Oliver House by the village in 1946, after the Oliver family left the house and a fund to keep it to Penn Yan, and opened its museum there in July 1948. It now runs three museums together as the Yates History Center: the nineteenth-century period rooms of the Oliver House, the L. Caroline Underwood Museum of decorative arts and local history, and the Scherer Carriage House, with exhibits on the Public Universal Friend.',
  'The red brick house museum at 200 Main Street (red brick from the Commons photograph chosen for it) with its two neighbours. Interior: period rooms, by the society\'s own description as Wikipedia gives it; not checked further.',
  '',
  'A museum. Its own site (yatescountyhistory.org) would not connect from here, so hours were not checked: ask before going. Street parking not checked.',
  [W('Yates County Genealogical and Historical Society')],brick='yes',hours='?'),
N('sampson-theatre-penn-yan','Sampson Theatre','Penn Yan','wny','civic','standing',42.66136,-77.05232,'site','view','walk','','1910',
  'Built in 1910 of poured concrete, three stories high, 60 by 100 feet, with a front auditorium and a rear stage block under gambrel roofs. It showed vaudeville and films, was turned into a miniature golf course in 1929, and later stored tires. It was listed on the Register in 2008.',
  'The concrete theatre with its two gambrel roofs just off Main Street, near the Birkett Mills. The Penn Yan Theatre Company\'s listing with the county chamber says it can be viewed by appointment; how far its restoration has got was not checked.',
  'A vaudeville house that spent decades as a mini-golf course and a tire store.',
  'Owned by the Penn Yan Theatre Company as its chamber listing gives it (not checked on its own page); look from the street, or arrange a visit through the company.',
  [W('Sampson Theatre'),HM('198463','Sampson Theatre'),L('Yates County Chamber: Penn Yan Theatre Company','https://business.yatesny.com/list/member/pytco-penn-yan-theatre-company-817')],brick='no'),
N('lake-view-cemetery-penn-yan','Lake View Cemetery','Penn Yan','wny','burial','standing',42.66229,-77.06645,'site','public','walk','','1855–1906',
  'A fifty-acre cemetery laid out to a landscape plan in two phases between about 1855 and 1906, with wooded and open ground. Its Abraham Wagener Memorial Chapel, a two-story brick Gothic Revival building, dates from 1923–24. It was listed on the Register in 1996.',
  'The south gate, the chapel and the family plots on the slope at the west edge of the village. Interior of the chapel not checked.',
  '',
  'A cemetery, open ground with drives; owner, gate hours and parking not checked: visit in daylight and keep to the drives.',
  [W('Lake View Cemetery (Penn Yan, New York)')],brick='?'),
# ---- Dresden, Bluff Point and the Friend's country ----
N('ingersoll-birthplace-museum-dresden','Robert Green Ingersoll Birthplace Museum','Dresden','wny','landmark','standing',42.68417,-76.95608,'exact','open','walk','','c. 1800',
  'Robert G. Ingersoll, the nineteenth-century orator known as "the Great Agnostic", was born here in 1833 while his father was a minister in Dresden. The main block was built about 1800 as a Congregational parsonage on Charles Street; its wing was built about the same time in Hopeton, a settlement that failed, and the two were moved and joined on Main Street before 1833. It has opened as an Ingersoll museum three times: in 1921, as a museum, community house and library backed by a committee that included Thomas Edison; again from 1954; and since 1993 under the Council for Secular Humanism, which bought it for $7,000.',
  'A small two-story Federal house with a saltbox wing on Main Street, the only one of Ingersoll\'s homes still standing and open to the public; a state highway marker stands in front. Inside, a museum of his life; period fabric not checked.',
  'The birthplace of America\'s best-known 19th-century unbeliever, a museum since 1993.',
  'A museum. The Freethought Trail page says it is open weekends in summer and fall; times not checked. Street parking on Main Street, Dresden, not checked.',
  [W('Robert Ingersoll Birthplace'),L('Freethought Trail: Robert Green Ingersoll Birthplace Museum','https://www.freethought-trail.org/trail-map/location:robert-green-ingersoll-birthplace-museum/'),HM('296494','Birthplace of Robert Ingersoll')],brick='?',hours='Weekends in summer and fall (times not checked)'),
N('esperanza-mansion-bluff-point','Esperanza (John Rose House)','Bluff Point','wny','hotel','standing',42.59587,-77.13451,'exact','view','drive','','1838',
  'A Greek Revival mansion built in 1838 by John Nicholas Rose and his wife Jane Macomb, with a two-story portico of four Ionic columns, high above Keuka Lake. The Roses lived here until 1870, Rose becoming one of the richest men in the area; the house then changed hands several times. It was listed on the Register in 1995.',
  'The columned portico above State Route 54A on the Bluff Point side of Keuka Lake, with a Register marker. Restaurant-booking sites list an inn and restaurant here (as The Mansion at Keuka Lake); that was not checked on its own page. Interior not checked.',
  '',
  'Private. Its use as an inn was not checked on an owner\'s page, so treat it as view only from the road unless you have a booking.',
  [W('Esperanza (Jerusalem, New York)'),HM('283957','Esperanza Mansion')],conf='mixed',brick='?'),
N('garrett-memorial-chapel-bluff-point','Garrett Memorial Chapel','Bluff Point','wny','worship','standing',42.50768,-77.13117,'site','open','drive','','1930–1931',
  'Paul Garrett, a leading figure of the American wine trade, and his wife Evelyn built this small Norman Gothic chapel high on Bluff Point in 1930–31 in memory of their son Charles, who had died of tuberculosis in January 1930. It is of ashlar granite with cast stone trim, with a polygonal apse and a square corner tower topped by a lantern and weathervane, and a crypt below. It is non-denominational under the stewardship of the Episcopal Diocese of Rochester, and the Garrett Chapel Trust cares for it.',
  'The granite chapel known as the Little Chapel on the Mount, looking out over Keuka Lake. Many of its stained glass windows, in the chapel and the crypt, were designed by Frederick Wilson.',
  'A grieving wine baron\'s granite chapel high on Bluff Point.',
  'Reached by a seasonal access road off West Bluff Road; the trust\'s page says the road section once under construction is open. Free.',
  [W('Garrett Memorial Chapel'),L('Garrett Memorial Chapel (the Garrett Chapel Trust)','https://www.garrettchapel.org/'),HM('310667','Garrett Chapel')],brick='no',hours='First week of June to last week of September: Tuesday and Thursday 1 to 4 p.m.'),
N('friends-home-jemima-wilkinson-house','The Friend\'s Home (Jemima Wilkinson House)','Jerusalem','wny','landmark','standing',42.65609,-77.16511,'site','view','drive','','c. 1809–1815',
  'The five-bay Federal house, built about 1809–1815, where the Public Universal Friend (born Jemima Wilkinson, 1752–1819) lived and from which the Society of Universal Friends was led. The Friend\'s followers had settled the country between the lakes from 1788 and built the first mill on the Outlet at Seneca Mills; the Society was gone by the 1860s. A state marker of 1932 gives the house as built about 1790, against the Register\'s 1809–1815.',
  'The house seen from the road, with the 1932 state marker. Interior not checked.',
  'The home of the genderless preacher who founded Jerusalem, New York.',
  'A private residence: view from the road only. Parking not checked; do not stop in the drive.',
  [W('Jemima Wilkinson House'),W('Public Universal Friend'),HM('283009','Friend\'s Home'),D1],conf='mixed',brick='?'),
# ---- Dundee and Middlesex ----
N('dundee-village-historic-district','Dundee Village Historic District','Dundee','wny','town','standing',42.52337,-76.97687,'site','public','walk','','mid-1800s–1901',
  'The historic core of Dundee, a village that grew on salt, petroleum, tin and copper works and farming along Big Stream near Seneca Lake (by the village\'s own street panel). The district, listed in 2007, has 78 contributing buildings: mid- to late-19th-century commercial blocks, the 1887 Baptist church, the 1891 school that houses the Greater Dundee Historical Society, the 1901 Dundee State Bank, and the separately listed Methodist and First Presbyterian churches. Susan B. Anthony spoke at the Yates County Fair held in Dundee in 1858.',
  'Main Street (Route 14A) round Seneca and Spring streets: the commercial blocks, the bank, the churches and the old school. HMdb has a "Then and Now" panel on Main Street.',
  '',
  'Public village streets (Main Street is State Route 14A); the buildings are private. Street parking not checked.',
  [W('Dundee Village Historic District'),HM('284086','Then And Now'),HM('236770','Woman\'s Study Club')],brick='?'),
N('first-presbyterian-church-dundee','First Presbyterian Church of Dundee','Dundee','wny','worship','standing',42.52245,-76.97684,'site','view','walk','','1895',
  'The congregation dates from 1832. Its church, built in 1895, is Romanesque in brick with limestone and terra cotta trim, two towers of several stories, broad cross gables, turret-like pinnacles and finials and carefully corbelled brickwork. It was listed on the Register in 2004.',
  'The two-towered church at Main and Spring streets. Interior not checked.',
  '',
  'An active congregation as far as the 2004 listing goes; services and opening not checked. View from Main Street.',
  [W('First Presbyterian Church (Dundee, New York)'),HM('271443','First Presbyterian Church of Dundee')],brick='?'),
N('overackers-corners-schoolhouse','Overackers Corners Schoolhouse','Middlesex','wny','civic','standing',42.73904,-77.27984,'exact','open','drive','','1874–1938',
  'A one-room Italianate brick school built in 1874 as District 3 of the Town of Middlesex, for grades one to eight, heated by a round stove, with no running water or electricity. It closed in June 1938 when the Middlesex schools were consolidated, then stored grain until 1989, when the Middlesex Heritage Group leased it; after ten years of work it reopened as a museum in 1998. Wikipedia gives its wall bricks as possibly made at a brickworks on the farm next door.',
  'The brick schoolhouse at North Vine Valley Road and State Route 364, with a Pomeroy Foundation plaque (2013 or 2014: the sources differ). Interior restored as a school museum; opening times not found.',
  '',
  'A museum of the Middlesex Heritage Group; no page of its own with hours was found, so ask before going. Parking not checked.',
  [W('Overackers Corners Schoolhouse'),HM('170567','Overackers Corners School')],brick='?',hours='?'),
# ---- Sampson, across Seneca Lake ----
N('sampson-military-museum-romulus','Sampson Military Museum (Sampson Naval Training Station)','Romulus','wny','fort','standing',42.72830,-76.90580,'site','open','drive','','1942–1956',
  'From 1942 to 1946 the Sampson Naval Training Station trained 411,429 sailors and WAVES on the east shore of Seneca Lake, on land taken from more than 100 families. It was Sampson State College from 1946 to 1949 and an Air Force basic-training base during the Korean War (1950–1956); the state bought it in 1960 for a park. Most of the buildings are gone, leaving about 38 miles of once-paved roads in woods, and the surviving brig houses a military museum run by Navy and Air Force veterans.',
  'The museum in the old brig, with aircraft and memorials outside (HMdb lists a T-2C Buckeye and several memorials there), and the old base roads through the woods of the park. Interior: displays of artifacts from the base; not checked further.',
  'Where 411,000 sailors learned their trade in World War II, now woods and a museum in the brig.',
  'Sampson State Park (New York State Parks), open all year dawn to dusk; State Parks says most of its parks charge a vehicle fee (see the park\'s fee list). Hunting is allowed in season with a park permit.',
  [W('Sampson State Park'),L('New York State Parks: Sampson State Park','https://parks.ny.gov/visit/state-parks/sampson-state-park'),HM('66076','U. S. Naval Training Station & Center 1942-1946'),HM('104839','The Sampson State Park Experience')],brick='?',hours='Museum mid-May to mid-October: Wednesday to Sunday 10 a.m. to 3 p.m. (2026)'),
]

PIN_NOTES={
 'seneca-mills-falls-keuka-outlet':'On the white water of the falls as it shows on the New York leaf-off aerial (look.py, pix.py); the Outlet Road lot is the one uncoveringnewyork.com gives (42.66439,-77.00244).',
 'cascade-mills-falls-keuka-outlet':'On the white water of the falls beside the trail buildings west of the Outlet Trail Visitor\'s Center (OpenStreetMap) on the leaf-off aerial (look.py, pix.py). Trailhead: the Mays Mills lot from parking.py.',
 'crooked-lake-canal-lock-3-dresden':'Area only: about 400 m west along the trail from the Route 14 bridge over the trail (OpenStreetMap, 42.67983,-76.96161), from Dumas\'s "a quarter mile upstream"; the lock itself was not seen.',
 'birkett-mills-penn-yan':'Moved onto the mill building on the north bank beside the silos, on the leaf-off aerial (look.py, pix.py); the geocoder\'s point for 1 Main Street was on the block north of it.',
 'penn-yan-historic-district':'Geocoder PointAddress for 159 Main Street, the post office block in the middle of the district.',
 'yates-county-courthouse-park':'OpenStreetMap courthouse point (nom.py), which matches the Register point.',
 'oliver-house-museum-penn-yan':'Geocoder PointAddress for 200 Main Street, Penn Yan.',
 'sampson-theatre-penn-yan':'HMdb marker position, at the street corner beside the theatre; the Wikipedia point is 220 m north.',
 'lake-view-cemetery-penn-yan':'OpenStreetMap cemetery area point (nom.py); the Register point is 150 m south-east.',
 'ingersoll-birthplace-museum-dresden':'Geocoder PointAddress for 61 Main Street, Dresden; the Wikipedia point matches.',
 'esperanza-mansion-bluff-point':'Geocoder PointAddress for 3456 State Route 54A; the HMdb marker is 20 m away.',
 'garrett-memorial-chapel-bluff-point':'HMdb marker position; the Register point is 40 m away.',
 'friends-home-jemima-wilkinson-house':'HMdb marker position; the Register point is 65 m north.',
 'dundee-village-historic-district':'Register list point for the district.',
 'first-presbyterian-church-dundee':'HMdb marker position at Main and Spring streets; the Register point is 220 m north.',
 'overackers-corners-schoolhouse':'HMdb (Pomeroy marker) position; the Register point matches.',
 'sampson-military-museum-romulus':'Among the HMdb memorial markers by the museum (42.7281-42.7286, -76.9052 to -76.9063); the geocoder put the park address, 6096 Route 96A, 700 m west.',
}
