# November 25, 2026: Jefferson County and rural Leavenworth County, Kansas (about 30 to 50 miles west and north-west of Kansas City).
# Eight places the earlier Kansas City batches did not reach: two Delaware River truss bridges, two country schools,
# four Register-listed farmsteads .
# Facts from the linked sources only: National Register forms read as text from NPGallery and the Kansas Historical
# Society's register search. Nothing was seen on the ground.
from data_b import N
from data_ma import W
NR='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'
JF1='https://www.kansashistory.gov/natreg/natreg_listings/search/page:1/county:JF/records:all/submit:SEARCH'
JF2='https://www.kansashistory.gov/natreg/natreg_listings/search/page:2/county:JF/records:all/submit:SEARCH'
LV2='https://www.kansashistory.gov/natreg/natreg_listings/search/page:2/county:LV/records:all/submit:SEARCH'
LV3='https://www.kansashistory.gov/natreg/natreg_listings/search/page:3/county:LV/records:all/submit:SEARCH'
BATCH={'key':'ks_jflv_rkvm','label':'Kansas: Jefferson and rural Leavenworth counties','added':'2026-11-25 15:52'}
PLACES=[
N('buck-creek-school-perry-ks','Buck Creek School','Perry, Kansas','ks','civic','standing',39.06616,-95.29703,'site','view','drive','','1878–1952',
  'Jefferson County School District 43 was organized in January 1869 and first met in a small frame school. This limestone schoolhouse replaced it in about 1878 and served the district until consolidation closed it in 1952. In 1954 it was sold to the Valley Ridge Extension Homemakers Unit, which used it as a meeting hall. The 1988 form says it was one of two one-room schools still standing in Rural Township, out of seven.',
  'A one-storey limestone schoolhouse about 25 by 40 feet with a gable front facing south and a two-storey wooden entry tower with a bell stage. The front and sides are random-coursed, rock-faced limestone blocks with quoins; the back wall is limestone rubble. Arched front windows have limestone arches with keystones, and a narrow brick chimney rises from the back. A dirt-floor cellar lies under the north half. The form calls the tower later than the school, perhaps of the 1890s or 1900s. Interior not checked.',
  'A stone one-room school beside US-24, built in a county where most country schools were frame.',
  'About two miles east of Williamstown, north of US-24, on a tract of about 45 by 60 feet. The 1988 form says a homemakers\' club owned it; who owns it now, and whether it is ever open, were not checked. Look from the roadside and stay off the grounds unless invited.',
  [['National Register form, Buck Creek School (88002830)',NR%'88002830'],['Kansas Historical Society: Jefferson County register listings',JF1],W('Buck Creek School')],brick='?'),
N('delaware-river-parker-truss-bridge-perry-ks','Delaware River Parker Truss Bridge, Perry','Perry, Kansas','ks','landmark','standing',39.075,-95.402778,'site','public','drive','','1926',
  'Built in 1926 to carry Bridge Street (the old US-24) over the Delaware River at the west edge of Perry, this is a single-span riveted Parker through truss 222 feet long and 20 feet wide. The 2003 form credits the Midland Bridge Company and Kansas City Structural Steel Company, both of Kansas City, Missouri, and Yancy Brothers Construction. It calls the design an uncommon answer to a long span, with concrete abutments and deck.',
  'The arched top chord has eleven sloping sections and the web is built of channels and angle stock, riveted together. A double-span Baltimore truss railroad bridge of the Union Pacific stands about 100 yards to the south. A 2019 photograph on Wikimedia Commons shows a bare deck with brush at both ends, so it may no longer carry traffic; this was not checked.',
  '',
  'On Bridge Street about 0.3 mile west of its junction with Main Street in Perry, a public street. Look from the roadside and the approaches; the form is dated 2003 and current road status was not checked.',
  [['National Register form, Delaware River Parker Truss Bridge (03000372)',NR%'03000372'],['Kansas Historical Society: Jefferson County register listings',JF1]],brick='no'),
N('delaware-river-composite-truss-bridge-valley-falls-ks','Delaware River Composite Truss Bridge, Valley Falls','Valley Falls, Kansas','ks','landmark','standing',39.350833,-95.454722,'site','public','drive','','1936',
  'A 1936 bridge on Coal Creek Road at the north-east edge of Valley Falls that combines three trusses in one crossing: a riveted Parker through truss 152 feet long, with a 103-foot Warren pony truss at each end. The 2003 form calls this an uncommon compound answer for a long span. The deck is 25 feet wide.',
  'Two poured-concrete piers with tapered columns joined by a central arched spandrel hold the inner ends of the trusses, and the original guardrails of channel stock and pipe rail are intact. Remnant abutments of two demolished railroad bridges stand beside it on the east. Whether the bridge still carries traffic was not checked.',
  '',
  'On Coal Creek Road, 0.1 mile south of 170th Road at the north-east city limit of Valley Falls; a public road. Look from the roadside. The form is dated 2003 and current road status was not checked.',
  [['National Register form, Delaware River Composite Truss Bridge (03000371)',NR%'03000371'],['Kansas Historical Society: Jefferson County register listings',JF1]],brick='no'),
N('sunnyside-school-jefferson-county-ks','Sunnyside School','Sarcoxie Township, Jefferson County, Kansas','ks','civic','standing',39.06265,-95.2525,'exact','view','drive','','1879',
  'A log schoolhouse built by John Large was the first Sunnyside School; it burned in 1875. The frame school that replaced it, built about 1879, follows a pattern-book design by the Topeka architects John Haskell and Louis M. H. Wood, published by the state education department. In 1894 the property was deeded to School District 51. Later the building served as a clubhouse and meeting hall.',
  'A wood-frame, front-gabled schoolhouse with a rather ornate front: two entrances flanking a group of round-arched windows. The back wall is plain clapboard. The cupola was lost to decay in the 1970s but the original bell is kept in the attic. Repairs to the foundation (2002) and front windows (2005) are listed in the form. Interior not checked.',
  '',
  'At 1121 Republic Road in the south of Jefferson County; a rural lot of about an acre. Who owns it now and whether it is open were not checked. Look from the road.',
  [['National Register form, Sunnyside School (10001139)',NR%'10001139'],['Kansas Historical Society: Jefferson County register listings',JF2]],brick='no'),
N('morris-harris-farmstead-perry-ks','Morris Harris Farmstead','Perry, Kansas','ks','landmark','standing',39.06161,-95.28275,'site','view','drive','','1909',
  'Morris Harris built this farmstead in 1909. The Kansas Historical Society lists six contributing buildings, all of that year: a large house with a recessed west wing and a projecting rear bay, a tenant house, a smokehouse, a barn, a granary and a poultry house. All are of rusticated irregular stone masonry, a distinctive style. It was listed in 2023.',
  'The Society calls the farmstead well preserved, with good integrity. The nomination form itself could not be read, so what is seen from the road, and the condition of each building, were not checked.',
  '',
  'At 16010 US-24 near Perry. A private working property: look from US-24 and do not enter. Who owns it now was not checked.',
  [['Kansas Historical Society: Jefferson County register listings',JF1]],conf='mixed',brick='no'),
N('maplecroft-farmstead-grantville-ks','Maplecroft Farmstead','Grantville, Kansas','ks','landmark','standing',39.0997,-95.55887,'site','view','drive','','1862–1967',
  'The west part of the house dates from about 1862 and is credited to James Townsend, son-in-law of John Kuykendall, who held the first land patent here. A stone house and limestone barn were begun in the 1870s by M. R. Dutton; Hanson Z. Frisbie bought the land in 1873 and moved in in 1874. The farm stayed in the Frisbie family for over a century, growing potatoes and apples and raising livestock. It was listed in 2017.',
  'The 2017 form calls the house one of the largest vernacular stone residences with Italianate details in the county. The farmstead sits on about five acres in the Kansas River valley, with cultivated fields all round. Interior and outbuildings not checked.',
  '',
  'At 2957 KOA Road, a private farm. Look from the road and do not enter; who owns it now was not checked.',
  [['National Register form, Maplecroft Farmstead (100001702)',NR%'100001702'],['Kansas Historical Society: Jefferson County register listings',JF1]],brick='no'),
N('lyman-christy-farmstead-meriden-ks','Lyman Christy Farmstead','Meriden, Kansas','ks','landmark','standing',39.20924,-95.58181,'site','view','drive','','1892–1951',
  'Lyman Christy bought 160 acres in two lots, in 1879 and 1880. Six historic buildings now stand on a 22-acre piece of the farm: the notable one is a bank barn built in 1892, near which are a loafing shed, a chicken coop, an oil house and a tool shed. A hay shed, garage, three grain bins and a ranch house are newer. The period of significance ends in 1951, when it stopped being a subsistence farm.',
  'The Kansas Historical Society says the farmstead keeps a high level of integrity. The nomination form could not be read, so the barn\'s look and condition were not checked.',
  '',
  'At 9001 Christy Road north-west of Meriden, listed on the state register in 2018. A private farm: look from the road and do not enter. Who owns it now was not checked.',
  [['Kansas Historical Society: Jefferson County register listings',JF1]],conf='mixed',brick='?'),
N('lamborn-farmstead-leavenworth-county-ks','Horace and Rosemond Lamborn Farmstead','Leavenworth County, Kansas','ks','landmark','standing',39.24416,-94.93631,'site','view','drive','','1877–',
  'Horace Greeley Lamborn bought this farm in 1877 and ran it as a subsistence farm that also boarded horses. In the early 1900s it took up dairying. It lies in Delaware Township, where settlers from Platte City, Missouri, laid out the town of Delaware City in 1854 as a rival to Leavenworth; the prison town of Lansing is less than two miles away. It was listed in 2011.',
  'The 2011 form describes a barn, a residence and other farm buildings, with some later metal outbuildings that do not count as historic. Interior and present condition not checked.',
  '',
  'At 25952 155th Street, a private farm. Look from the road and do not enter. Who owns it now was not checked.',
  [['National Register form, Lamborn Farmstead (11000725)',NR%'11000725'],['Kansas Historical Society: Leavenworth County register listings',LV2]],brick='?'),
N('holman-farmstead-leavenworth-county-ks','Alice and Edwin Holman Farmstead','Leavenworth County, Kansas','ks','landmark','standing',39.25135,-94.95576,'site','view','drive','','',
  'In Delaware Township, this farmstead was begun by Alice and Edwin Holman, who raised fruit, vegetables and nursery trees until they sold it in 1914. Della Knabb bought it that year and kept milk cows. The Kansas Historical Society lists it as a vernacular agricultural district, listed in 2023.',
  'The nomination form could not be read, so the buildings and their condition were not checked.',
  '',
  'At 26352 New Lawrence Drive, a private farm. Look from the road and do not enter. Who owns it now was not checked.',
  [['Kansas Historical Society: Leavenworth County register listings',LV2]],conf='mixed',brick='?'),
]
PIN_NOTES={
'buck-creek-school-perry-ks':'Started from the OpenStreetMap point, which falls on a road crossing; moved about 40 m north onto the small gabled building with a gravel yard. The aerial does not show the stone walls or tower clearly, so the pin marks the site.',
'delaware-river-parker-truss-bridge-perry-ks':'Coordinate from Wikipedia\'s list of Register listings; checked on the aerial.',
'delaware-river-composite-truss-bridge-valley-falls-ks':'Coordinate from Wikipedia\'s list of Register listings; checked on the aerial.',
'sunnyside-school-jefferson-county-ks':'Address lookup for 1121 Republic Road fell on the road; moved about 50 m west onto the gabled building beside it, seen on the aerial.',
'morris-harris-farmstead-perry-ks':'Address lookup for 16010 US-24; Wikipedia\'s list point is about a kilometre away. Checked on the aerial.',
'maplecroft-farmstead-grantville-ks':'Address lookup for 2957 KOA Road, matching the Register list point; checked on the aerial.',
'lyman-christy-farmstead-meriden-ks':'Address lookup for 9001 Christy Road; checked on the aerial.',
'lamborn-farmstead-leavenworth-county-ks':'Address lookup for 25952 155th Street; checked on the aerial.',
'holman-farmstead-leavenworth-county-ks':'Address lookup for 26352 New Lawrence Drive; checked on the aerial.',
}
