# Eastern Washington County, New York: Dresden, Granville, Hebron, Easton, Fort Ann, Kingsbury, Hartford and Whitehall.
# From Wikipedia, National Register forms (NPGallery), HMdb marker texts, the DEC's Lake George Wild Forest page and fire
# tower study, and the Pember Library's own pages.
from data_b import N
from data_ma import W

def HM(n, label): return [label + ' (HMdb marker %d)' % n, 'https://www.hmdb.org/m.asp?m=%d' % n]

BATCH={'key':'wash_ngoz','label':'Eastern Washington County: Black Mountain tower, the Pember, Burton Hall and village markers','added':'2026-11-22 20:50'}

PLACES=[
N('black-mountain-fire-tower-dresden','Black Mountain fire tower','Dresden','wash','landmark','standing',43.60645,-73.53095,'site','public','hike','','1911–',
  'Black Mountain is the highest peak round Lake George and the highest point in Washington County. The state Conservation Commission put a wooden fire lookout on the summit in May 1911 and replaced it in 1918 with a 35-foot Aermotor steel tower; in 1938 an aircraft beacon was mounted on it to warn pilots flying between Glens Falls and Montreal. Observers kept watch until the end of the 1988 fire season. The tower then went over to police radio: the Wikipedia article says the DEC closed it in early 1989, the DEC\'s own fire tower study says it has been shut to the public since the State Police fitted it for communications in 1990.',
  'The steel tower stands on the bare summit beside a radio relay building and a wind turbine, fenced off: the summit is open, the tower is not. The DEC study notes the old observer\'s cabin was removed in the 1990s. Just north of the tower is a rock cut with "R. Rogers 1763", which the Wikipedia article (citing the state chapter of the Forest Fire Lookout Association) says was carved by Robert Rogers of Rogers\' Rangers and authenticated by the State Education Department; not checked on the ground.',
  'A 1918 fire tower on the top of Washington County, with a Rogers\' Rangers carving below it.',
  'State land, Lake George Wild Forest (DEC). From the Pike Brook Road Parking Area the Black Mountain Trail climbs 1,239 feet in 2.5 miles to the summit (DEC page, read November 2026). A loop by Black Mountain Pond is longer. Open all year; the tower itself is closed.',
  [W('Black Mountain (Washington County, New York)'),['Lake George Wild Forest (NYS DEC)','https://dec.ny.gov/places/lake-george-wild-forest'],['Fire Tower Study for the Adirondack Park (NYS DEC, 2010)','https://extapps.dec.ny.gov/docs/lands_forests_pdf/ftowerstudy.pdf']],
  conf='mixed', th=[43.61157,-73.49324], thn='Pike Brook Road Parking Area (DEC)', brick='no', hours=''),

N('pember-library-museum-granville','Pember Library and Museum','Granville','wash','civic','standing',43.40622,-73.26305,'exact','open','drive','','1909–',
  'Franklin Tanner Pember and his wife Ellen Wood Pember founded the library and a natural history museum together in 1909, in a building put up for the purpose. After Pember died in 1924 the museum\'s money ran out and it was shut to the public for almost forty years, until the Friends of the Museum reopened the building and its collections in 1973.',
  'A two-storey granite building at 33 West Main Street with a large slate sign on its lawn giving the opening hours (the Pember\'s own directions page). Inside, the library and Pember\'s natural history collections; the museum\'s exhibitions are listed on its page. Which original fittings survive was not checked.',
  'A 1909 village library and natural history museum in the slate country.',
  'Run by the Pember Library and Museum, 33 West Main Street, Granville. The hours given are the library\'s, from its own page read November 2026; the museum\'s posts mention special openings and closures, so check before a trip. Street and village parking nearby.',
  [W('Pember Library and Museum'),['The Pember: directions','https://thepember.org/index.php/directions/'],['Pember Library (hours)','https://gralib.sals.edu/']],
  conf='', th=[43.40571,-73.26144], thn='Water Street lot', brick='no', hours='Tuesday 10 a.m. to 5 p.m., Wednesday and Thursday 1 to 5, Friday 10 to 5, Saturday 10 to 1'),

N('hebron-district-school-16','Hebron District School No. 16 (Munson Hollow School)','East Hebron','wash','civic','standing',43.26222,-73.28722,'site','view','drive','','c. 1847–1944',
  'A one-room school of about 1847, also known as the Munson Hollow School and in its time as District School No. 12 and No. 2. It is a plain building with a few Greek Revival touches, of stacked plank construction on a slate foundation. It held school until 1944 and was then a community centre. It was listed on the National Register in 2012, and a Pomeroy Foundation marker on Route 22 says so.',
  'A small gable-roofed schoolhouse by New York Route 22, with its 2014 roadside marker. Interior not checked. The Wikipedia article on Hebron says the Hebron Historical Society keeps a museum in two old buildings on the east side of Route 22 in East Hebron, one of them an 1845 one-room school; whether that is this building was not confirmed, and no page of the society\'s own was found.',
  '',
  'Looked at from New York Route 22; owner and any opening times not checked. Pull off only where the shoulder is wide.',
  [W('Hebron District School No. 16'),HM(132226,'Hebron School District No. 16'),W('Hebron, New York')],
  conf='mixed', th=None, thn=None, brick='no', hours=''),

N('burton-hall-north-easton','Burton Hall (Easton Town Hall)','North Easton','wash','civic','standing',43.01095,-73.55054,'exact','view','drive','','1901–',
  'A one-storey frame hall finished in 1901, paid for through the local benefactor Isaac A. Burton, as a meeting place for the people of the Town of Easton and a seat for its government. For a long stretch it also held the town\'s circulating library. It is still Easton\'s municipal centre, and was listed on the National Register in 2015.',
  'White clapboard over a board-and-batten skirt, a slate hip roof and original six-over-six windows with green shutters. Inside, the Register form describes a large auditorium with a stage on the west side that still has its big hand-painted stage curtain. The form also notes the birthplace of the engineer George Henry Corliss, of the Corliss steam engine, as the next house south, and a tavern of about 1790 nearby; both private.',
  'A 1901 town hall that still keeps its painted stage curtain.',
  'Town of Easton building, 1071 State Route 40. Look from the road; the town offices inside open on weekdays, but no hours were found on a town page. Parking area beside the hall (Register form). The Wikipedia coordinate is about 10 km off; the pin is on the address.',
  [W('Burton Hall (Greenwich, New York)'),['National Register nomination (NPGallery)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/15000610_text']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('adamsville-baptist-church-kingsbury','Adamsville Baptist Church','Adamsville','wash','worship','standing',43.31959,-73.47319,'exact','view','drive','','',
  'Adamsville was named for President John Quincy Adams, who allowed a post office here about 1825. The hamlet once had a hotel, a store and several trade shops; the Town of Kingsbury\'s 1999 marker says the Baptist church is all that remains of them. No source found gives the year the church was built.',
  'A white church on County Route 43 just south of its crossing with New York Route 196, with the town\'s marker at the crossing. Interior and building date not checked.',
  '',
  'An active congregation (Adamsville Community Baptist Church); service times not found on a page of its own. Look from the road.',
  [HM(181681,'Adamsville')],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('fort-anne-baptist-bell-fragment','First Baptist Church site and bell fragment, Fort Ann','Fort Ann','wash','curio','marker',43.41292,-73.48813,'site','public','walk','','1874–1955',
  'The First Baptist Church of Fort Anne village was built in 1874 and burned in 1955. Its bell also rang as the town clock. A state marker of 1964 stands on the site with a fragment of the bell, which carries the date it was bought.',
  'A marker on George Street (U.S. 4) between Ann and Elizabeth streets, with the piece of the bell set beside it (HMdb). The Old Stone House Library is a few doors away.',
  '',
  'On the public street. Park in the village along George Street.',
  [HM(19854,'Fort Anne First Baptist Church')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('oldest-house-fort-ann','Oldest house in Fort Ann (98 George Street)','Fort Ann','wash','landmark','standing',43.41607,-73.48710,'exact','view','drive','','before 1800–',
  'A village marker calls this the oldest house in Fort Ann: built before 1800 and owned in turn by the Moore, Pike and Shipman families. Nothing else was found about it.',
  'A private house at George Street (U.S. 4) and Charles Street, with its marker. Look from the street; interior not checked.',
  '',
  'Private home. Look from the public street only.',
  [HM(155124,'Oldest House')],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('mount-carmel-bell-granville','Our Lady of Mount Carmel bell, Granville','Granville','wash','curio','marker',43.40369,-73.26268,'site','view','walk','','1879',
  'Our Lady of Mount Carmel was a Roman Catholic church in Granville from 1867 to 2009. Its 1,020-pound bell, cast in 1879 by the Meneely foundry of West Troy, now stands with a marker in front of St. Mary\'s Roman Catholic Church on Bulkley Avenue.',
  'The bell and its marker on the lawn of St. Mary\'s, 23 Bulkley Avenue (HMdb).',
  '',
  'On the lawn of St. Mary\'s church (parish property); look from the Bulkley Avenue sidewalk.',
  [HM(229650,'Our Lady of Mt Carmel Roman Catholic Church')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('skenes-mills-site-whitehall','Skene\'s Mills site, Wood Creek falls','Whitehall','wash','industry','marker',43.559286,-73.399306,'area','view','walk','','1776',
  'Near the falls of Wood Creek stood the Skenesborough mills, which sawed planks for Benedict Arnold\'s fleet of 1776, the one that fought at Valcour Island. A state marker of 1993 marks the spot.',
  'The marker off North Williams Street, by the falls. Nothing of the mills is described as surviving. The Skenesborough Museum and the old canal walls are a short walk south.',
  'Where the planks for the 1776 Lake Champlain fleet were sawn.',
  'HMdb gives the marker as reached from North Williams Street in the village of Whitehall; who owns the ground at the falls was not checked, so look from the street.',
  [HM(89669,'Skene\'s Mills'),W('Whitehall (village), New York')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('smiths-basin-kingsbury','Smith\'s Basin','Smith\'s Basin','wash','canal','marker',43.35823,-73.4951,'area','view','drive','canal','c. 1825',
  'A canal hamlet named for Ezekiel Smith, who with his brother Israel kept a store and tavern here about 1825. It once had several hotels and stores, a school, a post office, a church and a railroad station, and a canal boat basin where lime was loaded for New York City (Town of Kingsbury marker, 1999).',
  'The town marker at New York Route 149 and County Route 41, near Lock 9 of the present Champlain Canal. What, if anything, is left of the basin was not checked.',
  '',
  'Roadside marker at a highway corner; the land round it was not checked and may be private, so read it from the roadside.',
  [HM(61659,'Smith\'s Basin')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('hartford-old-mills-site','Site of the old mills, Hartford','Hartford','wash','industry','marker',43.36316,-73.39010,'area','view','drive','','1814–',
  'A marker of the Hartford Historical Group lists the works that stood here: a dam built by I. Norton in 1814, the Downs clothing works, the Woodell starch mill of 1866, the Daicy cabinet works of 1870 and, below, the Higby tannery of 1818.',
  'The marker on New York Route 40 just south of the Hartford fire house. On the aerial a small pond lies on the stream east of the road; whether it is the old mill pond, and whether any dam stone is left, was not checked.',
  '',
  'Roadside marker on a state highway; the land round the stream was not checked and may be private.',
  [HM(61515,'Site of Old Mills')],
  conf='mixed', th=None, thn=None, brick='no', hours=''),

]

PIN_NOTES={
 'black-mountain-fire-tower-dresden':'The summit point from the Wikipedia article; OpenStreetMap maps the radio relay building 40 m north. Parking point is the Pike Brook Road lot mapped in OpenStreetMap on the Lake George Wild Forest.',
 'pember-library-museum-granville':'On the building at 33 West Main Street (ArcGIS geocoder, address point); the Wikipedia point agrees within 20 m.',
 'hebron-district-school-16':'The Wikipedia point; the HMdb marker is 50 m east on Route 22.',
 'burton-hall-north-easton':'On the address from the Register form, 1071 State Route 40 (ArcGIS geocoder, address point). The Wikipedia coordinate is about 10 km away.',
 'adamsville-baptist-church-kingsbury':'Moved 58 m onto the church building seen on the aerial, beside the ArcGIS geocoder\'s point for Adamsville Community Baptist Church; the HMdb marker is at the crossroads 130 m north.',
 'fort-anne-baptist-bell-fragment':'The HMdb marker position.',
 'oldest-house-fort-ann':'On 98 George Street (ArcGIS geocoder, address point), the address HMdb gives for the marker.',
 'mount-carmel-bell-granville':'On 23 Bulkley Avenue (ArcGIS geocoder, address point); the HMdb marker position is 20 m west.',
 'skenes-mills-site-whitehall':'The HMdb marker position; the mills stood somewhere near the falls.',
 'smiths-basin-kingsbury':'The HMdb marker position; the basin itself was not located.',
 'hartford-old-mills-site':'The HMdb marker position; the mill sites were along the stream nearby.',
}
