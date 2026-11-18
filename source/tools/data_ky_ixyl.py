# November 18, 2026: Kentucky, Mercer and Boyle counties (Harrodsburg, Pleasant Hill, Danville, Perryville), first pass
# (region drawn at random by tools/choose.py). Facts from the linked sources only, read in this session: Wikipedia through
# tools/wiki_raw.py, National Register forms through tools/page.py (npgallery text layers), Kentucky Historical Society
# marker pages, HMdb marker pages, and the managing bodies' own pages named in each access note. Kentucky State Parks pages
# (parks.ky.gov) are drawn by script and could not be read; hours for the two state parks come from the sources named.
from data_b import N
from data_ma import W

BATCH={'key':'ky_ixyl','label':'Kentucky: Harrodsburg, Pleasant Hill, Danville and Perryville','added':'2026-11-18 06:59'}

SVP='https://shakervillageky.org'

PLACES=[
N('old-fort-harrod-state-park','Old Fort Harrod State Park','Harrodsburg','ky','fort','standing',37.76194,-84.84889,'site','public','walk','forts','1774–',
  'James Harrod and about thirty men built a fort here in June 1774, the first permanent American settlement in Kentucky. The park opened in November 1934 as Pioneer Memorial State Park, with a full-size replica of the fort. Wikipedia says the site of the real fort lies under the present parking lot.',
  'The replica fort with its blockhouses and cabins, the Mansion Museum (a Greek Revival house of the 1830s holding Civil War, Lincoln and Native American collections), the George Rogers Clark monument, a pioneer cemetery that Wikipedia calls the oldest west of the Alleghenies, and the brick Lincoln Marriage Temple. The temple shelters the log cabin where Thomas Lincoln and Nancy Hanks married: Wikipedia calls the cabin reconstructed, a state-parks guide calls it the original; not settled.',
  'Where Kentucky began, rebuilt in logs in the middle of town.',
  'Kentucky State Parks, 100 South College Street, Harrodsburg. The park\'s own page (parks.ky.gov) is drawn by script and could not be read. The Harrodsburg Herald (2026) gives the park as open Wednesday to Saturday from 9 a.m. and admission $8 adults, $6 seniors 55 and over, $5 children 6 to 12; closing time and winter hours not checked. Two lots on park land, off West Lexington Street and Fort Harrod Street.',
  [W('Old Fort Harrod State Park'),['Harrodsburg Herald: Step back in time at Old Fort Harrod State Park','https://www.harrodsburgherald.com/?p=259579'],
   ['Kentucky State Parks: Old Fort Harrod','https://parks.ky.gov/harrodsburg/parks/historic/old-fort-harrod-state-park'],
   ["America's State Parks: Old Fort Harrod",'https://www.americasstateparks.org/state-park/old-fort-harrod-state-park/']],
  conf='mixed',th=[37.76191,-84.84694],thn='Park lot off Fort Harrod Street (state park land)',brick='?'),

N('shaker-village-pleasant-hill','Shaker Village of Pleasant Hill','Harrodsburg','ky','town','standing',37.81849,-84.73781,'site','public','walk','','1805–1910',
  'A Shaker community lived here from 1805 to 1910, at its peak nearly 500 people farming more than 4,000 acres. By 1825 it had large stone and brick dwellings, shops and stone sidewalks. Restoration began in 1961, and the whole village is a National Historic Landmark district.',
  'Original Shaker buildings, dated by the village\'s own guide: the Meeting House (1820), the Centre Family Dwelling (1824–1834), a 21,000-square-foot house with 14 bedrooms and a meeting room, restored and reopened for guided tours, the Trustees\' Office (1839) with Micajah Burnett\'s twin spiral staircases rising three floors, the East Family Dwelling (1817), the brick Tanyard (1824) and the West Lot timber-frame stable (1830), the only surviving Shaker-built barn. Stone fences run round the fields. Exhibits and tours Tuesday to Sunday, 10 a.m. to 5 p.m.',
  'A whole Shaker town, stone and brick, still standing above the Kentucky River.',
  'Shaker Village of Pleasant Hill (a nonprofit), 3501 Lexington Road, Harrodsburg. Its own page: exhibits and tours Tuesday to Sunday 10 a.m. to 5 p.m., admission $20 adults (ages 13 to 61), $15 seniors 62 and over, $10 ages 6 to 12; hiking and walking daily 6 a.m. to 8:30 p.m. or dusk, $10 per car suggested donation. Lots on the village grounds.',
  [['Shaker Village: Plan your visit (hours and rates)',SVP+'/plan/'],['Shaker Village: building guide (PDF)',SVP+'/wp-content/uploads/2015/12/Shaker-Village-of-Pleasant-Hill.pdf'],
   W('Shaker Village of Pleasant Hill'),['Advocate-Messenger: Centre Family Dwelling open again for tours','https://www.amnews.com/?p=43649']],
  th=[37.81797,-84.73865],thn='East Lot, Shaker Village grounds',brick='?'),

N('shaker-landing-kentucky-river','Shaker Landing and the 1866 stable','Harrodsburg','ky','water','standing',37.82119,-84.72480,'area','public','drive','','1826–',
  'The Pleasant Hill Shakers traded down the Kentucky River as far as New Orleans from this landing below the palisades. They cut a road down to it in 1826, and kept a timber-frame stable here to change horses for stagecoaches.',
  'The village\'s guide calls the 1866 timber-frame stable the last structure left at the once busy landing. The Shaker roadbed of 1826 is now the 1.5-mile River Road Trail down from the village; the 1-mile Palisades Trail runs along the river bottom past a waterfall, and High Bridge is in sight upriver. Where the stable stands was not found on the aerial: the pin is the landing\'s parking lot.',
  'The Shakers\' river port, at the foot of a 400-foot descent.',
  'Shaker Village of Pleasant Hill land. Its river page: trails open daily sunrise to sunset; drive down Shaker Ferry Road or walk the River Road Trail. Non-motorized boats only, $10 launch fee paid at the Welcome Center, and only when pool 7 is at 12 feet or lower.',
  [['Shaker Village: The River',SVP+'/the-river/'],['Shaker Village: building guide (PDF)',SVP+'/wp-content/uploads/2015/12/Shaker-Village-of-Pleasant-Hill.pdf']],
  brick='?'),

N('old-mud-meeting-house','Old Mud Meeting House','Harrodsburg','ky','civic','standing',37.72403,-84.86308,'site','view','drive','','1800',
  'Low Dutch settlers who came from Pennsylvania in 1781 built this as the first Dutch Reformed church west of the Alleghenies, finished in 1800. The walls are wattle and daub, mud and straw packed into a hewn oak frame. Weatherboards went over them in 1849, and the Harrodsburg Historical Society has owned it since the late 1920s (the Society\'s trust says 1927, the state marker history says deeded August 27, 1928).',
  'A small weatherboarded meeting house with the early Dutch settlers\' graveyard beside it, which the Society also keeps. The original mud walls are under the 1849 siding; the ceiling was lowered and plastered. Interior not checked.',
  'A church with walls of mud and straw, built on the frontier in 1800.',
  'Harrodsburg Historical Society, 730 Dry Branch Road, south of Harrodsburg. No opening hours found; see it from the road and contact the Society (Morgan Row, Harrodsburg) to go in. Parking not mapped; the road shoulder was not checked.',
  [W('Dutch Reformed Church (Harrodsburg, Kentucky)'),['ExploreKYHistory: Marker 141, Old Mud Meeting House','https://explorekyhistory.ky.gov/items/show/988'],
   ['James Harrod Trust: Old Mud Meeting House','https://www.jamesharrodtrust.org/84-old-mud-meeting-house/']],
  conf='mixed',brick='?'),

N('morgan-row-harrodsburg','Morgan Row','Harrodsburg','ky','civic','standing',37.76054,-84.84488,'exact','view','walk','','1807–1830s',
  'Squire Joseph Morgan built this row of four brick units facing the Mercer County courthouse, the oldest row house west of the Alleghenies. A contract suggests the first part was to be done by 1816 and the state marker dates it from 1807; all four units were finished by the 1830s. It served as a tavern, inn, gambling house and stagecoach stop.',
  'Federal-style row in Flemish bond brick, 220 to 232 South Chiles Street. Inside, the connecting passages and the big central bar survive, with woodwork by the joiner Matthew P. Lowery. It now houses the Harrodsburg Historical Society and its research library among other businesses; opening hours not checked.',
  'Kentucky\'s oldest row house, once a stagecoach tavern.',
  'Street frontage in downtown Harrodsburg. The Harrodsburg Historical Society\'s museum and library are inside; hours not checked. Parking not checked.',
  [['ExploreKYHistory: Marker 185, Morgan Row','https://explorekyhistory.ky.gov/items/show/974'],
   ['James Harrod Trust: Morgan Row','https://www.jamesharrodtrust.org/tours/downtown-walking-tour/morgan-row/'],
   ['Kentucky Historical Society marker: Morgan Row 1807','https://history.ky.gov/markers/morgan-row-1807']],
  brick='?'),

N('beaumont-inn-harrodsburg','Beaumont Inn (Daughters\' College)','Harrodsburg','ky','hotel','standing',37.75261,-84.84274,'site','public','drive','hotels','1845–',
  'A three-story brick Federal-style building of about 1845, built to house some 100 girls. It was the campus of the Greenville Institute, Daughters\' College and Beaumont College. Two former students bought it in 1917 and Annie Bell Goddard made it an inn in 1918; her descendants still run it.',
  'The 1845 main building, an inn with 31 rooms and a restaurant known for country ham and fried chicken since Duncan Hines praised it in 1949. Interior fabric not checked.',
  'A girls\' college of 1845 that has been an inn since 1918.',
  'Privately owned inn and restaurant, open to guests and diners. Its own site lists the Main Dining Room, the Old Owl Tavern and the Owl\'s Nest Lounge; hours not checked.',
  [W('Beaumont Inn'),['Beaumont Inn','https://www.beaumontinn.com/']],brick='yes'),

N('high-bridge-kentucky-river','High Bridge over the Kentucky River','High Bridge','ky','rail','standing',37.81756,-84.71641,'site','view','drive','','1851–',
  'The Lexington & Danville Railroad hired John A. Roebling to build a suspension bridge here, but money ran out with only the stone towers built (Wikipedia gives 1851 and 1855, the overlook marker 1854 and 1858). The Cincinnati Southern built a cantilever bridge in 1876–77, the first in North America and the highest railroad bridge in the world. It was rebuilt in 1911 and double-tracked in 1929, when Roebling\'s towers were taken down.',
  'The steel bridge, about 275 feet above the river, still carries Norfolk Southern freight trains. Sources disagree whether the 1877 bridge used Roebling\'s towers as anchors (Wikipedia) or not (the marker). The overlook marker says 271 steps once led from the park down to the river; whether any remain was not checked.',
  'The first cantilever bridge in North America, from the park its builders made.',
  'High Bridge Park, Park Road, High Bridge (Jessamine County side); the marker stands on the park overlook, reached from Old Park Road east of Lock 7 Road. The park is public land on the federal map; who runs it and its hours not checked. The railroad is active: stay off the tracks and the bridge.',
  [W('High Bridge of Kentucky'),W('High Bridge, Kentucky'),['HMdb: An Engineering Landmark (overlook marker)','https://www.hmdb.org/m.asp?m=218252']],
  conf='mixed',th=[37.81767,-84.71573],thn='High Bridge Park lot, Park Road',brick='?'),

N('constitution-square-danville','Constitution Square','Danville','ky','civic','standing',37.6453,-84.7708,'site','public','walk','','1785–',
  'Ten conventions met in a log courthouse on this square between 1785 and 1792 and led Kentucky to statehood apart from Virginia. The square was a state park from 1937 to 2012 and is now run for Boyle County.',
  'Replicas of three buildings that stood on the square, including the courthouse, and the original building of the first U.S. post office west of the Alleghenies, with other early 1800s buildings moved or kept on the grounds. Cabins open 10 a.m. to 4 p.m., Monday to Saturday, April to October.',
  'Where Kentucky talked itself into statehood.',
  'Constitution Square Historic Site, a free open-air museum, South Second and Walnut streets, Danville. McDowell House\'s page (it runs the tours): park open daylight hours all year; cabins and restrooms 10 to 4, Monday to Saturday, April to October. Parking not checked.',
  [W('Constitution Square Historic Site'),['McDowell House: Constitution Square','https://mcdowellhouse.com/constitution-square']],
  brick='?'),

N('mcdowell-house-danville','McDowell House','Danville','ky','civic','standing',37.6451,-84.77101,'exact','public','walk','','1792–',
  'Dr. Ephraim McDowell lived and worked here. On Christmas morning 1809 he removed an ovarian tumor from Jane Todd Crawford without anaesthetic, the first successful operation of its kind; she lived another 32 years. Doctors bought the house in 1935 and opened it as a museum.',
  'A brick ell of 1792–1795, the clapboard front of 1803–1804 and a small brick office of 1820, with an apothecary and two gardens. Guided tours of the house, apothecary and gardens Tuesday to Saturday at set times; book ahead.',
  'The house where abdominal surgery began.',
  'McDowell House Museum, 125 South Second Street, Danville, across the street from Constitution Square. Its own page: tours Tuesday to Saturday at select times, office Tuesday to Friday 10 to 4; adults $8, seniors $7, students $4, children 5 to 12 $3. Small visitor lot on the north side of the property.',
  [W('Ephraim McDowell House'),['McDowell House Museum','https://mcdowellhouse.com/']],brick='?'),

N('old-centre-danville','Old Centre, Centre College','Danville','ky','inst','standing',37.645556,-84.781667,'site','view','walk','','1819–',
  'The first building of Centre College, chartered in 1819; classes began in it in 1820. It is the oldest college administration building west of the Alleghenies. Confederate and then Union troops occupied it in 1862.',
  'The 1819 core is a plain two-story Georgian block of red brick in Flemish bond; the Register form (1972) says it was restored in 1929 and given one-story wings in 1930, with a brick-walled courtyard on the north. It holds college offices. Interior not checked.',
  'The oldest college building west of the mountains.',
  'Centre College campus, Danville. Seen from the campus walks; whether visitors may go in was not checked. Parking not checked.',
  [W('Centre College'),['National Register nomination (1972)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/72000529_text']],brick='yes'),

N('jacobs-hall-danville','Jacobs Hall, Kentucky School for the Deaf','Danville','ky','inst','standing',37.6414,-84.7717,'site','view','walk','','1855–1857',
  'The Kentucky School for the Deaf, founded in 1823, was the first state-supported school for the deaf in the country and the first west of the Alleghenies. Jacobs Hall, built in 1855–57 to designs by Thomas Lewinski, held all of its main functions until 1882 and is a National Historic Landmark.',
  'A four-story brick Italianate block nine bays wide, with a two-story octagonal wooden cupola. The Register form singles out the main hall, whose curving staircase rises open to the skylight in the cupola. Interior not checked.',
  'A school for the deaf from 1857, crowned by a lantern.',
  'On the campus of a working state school, Danville; the building faces South Third Street (Wikimedia photo caption). Look from the street; ask the school before going on the grounds. Parking not checked.',
  [W('Kentucky School for the Deaf'),['National Register nomination','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/66000354_text']],brick='?'),

N('perryville-battlefield','Perryville Battlefield','Perryville','ky','fort','traces',37.67446,-84.97003,'site','public','walk','','1862',
  'Kentucky\'s largest and bloodiest Civil War battle was fought here on October 8, 1862, between Buell\'s Army of the Ohio and Bragg\'s Army of Mississippi. Bragg withdrew from Kentucky afterwards. The ground became a state park in 1936 and has grown by land bought by the state and the American Battlefield Trust.',
  'Open battlefield with monuments, cannon and signs, a museum near where many Confederate dead were buried, and nearly 12 miles of walking trails. On Squire Henry P. Bottom\'s farm, where much of the fighting was, artillery fire burned his hay barn.',
  'The field of Kentucky\'s biggest Civil War battle.',
  'Perryville Battlefield State Historic Site, 1825 Battlefield Road, Perryville. The park\'s own site: grounds open daily 7 a.m. to 7 p.m. April 1 to October 31 and 7 a.m. to 4 p.m. November 1 to March 31; museum April to October Monday to Saturday 9 to 5, Sunday 11 to 5, and in winter Wednesday to Saturday 10 to 3. No hunting. Fees not checked.',
  [W('Perryville Battlefield State Historic Site'),['Perryville Battlefield: directions and hours','https://perryvillebattlefield.org/html/directions_and_hours.html'],
   ['Friends of Perryville Battlefield: visiting','https://friendsofperryville.org/visiting.html']],brick='?'),

N('merchants-row-perryville','Merchants\' Row','Perryville','ky','town','standing',37.64987,-84.95196,'site','view','walk','','1830–1840',
  'The old Main Street of Perryville, renamed Buell Street after the Union general. Most of its buildings went up in 1830–40. They were damaged in the battle of October 8, 1862 and used as field hospitals, and several between Second and Third streets burned in the street fighting. Carrie Nation lived here as a child.',
  'A row of original 1800s commercial buildings along South Buell Street that now hold restaurants, shops and museums (the county visitors\' page). Interiors not checked.',
  'A whole 1830s main street that became a field hospital.',
  'Public street, South Buell Street (US 68) at West Second Street, Perryville; the state marker stands there. The Friends of Perryville say the downtown visitor center opens Saturdays 10 to 3 from April 1. Small lots on Buell and Second streets.',
  [['Kentucky Historical Society: marker 2223, Merchants\' Row','https://history.ky.gov/markers/merchants-row'],['HMdb: Merchants\' Row / Street Fighting','https://www.hmdb.org/m.asp?m=46399'],
   ['Visit Danville: Historic Merchants\' Row','https://danvillekentucky.com/listing/historic-merchants-row/']],
  th=[37.65015,-84.95200],thn='Lot on South Buell Street',brick='?'),

N('penns-store-gravel-switch','Penn\'s Store','Gravel Switch','ky','town','standing',37.549722,-85.028056,'area','view','drive','','1845–',
  'A country store at Gravel Switch, on the Boyle–Casey county line, first opened in 1845. Garden & Gun calls it the oldest country store in America owned and run by one family; the sixth generation runs it. After Hack Penn died in the early 1990s his niece Jeanne Penn Lane revived it, starting the Great Outhouse Blowout in 1992.',
  'The store is on the National Register (1998). What survives inside was not checked.',
  'A crossroads store run by one family since 1845.',
  'Privately owned store. Opening hours not checked. Pin is the Register list point, not checked against the building; parking not mapped.',
  [['Garden & Gun: My Old Kentucky Store','https://gardenandgun.com/old-kentucky-store'],['National Register listings in Boyle County',
   'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Boyle_County,_Kentucky']],conf='mixed',brick='?'),
]

PIN_NOTES={
 'old-fort-harrod-state-park':'Wikipedia article coordinate, in the park; checked on the aerial.',
 'shaker-village-pleasant-hill':'ArcGIS geocode of 3501 Lexington Road, at the village centre; checked on the aerial.',
 'shaker-landing-kentucky-river':'Pin is the mapped parking lot on Shaker Ferry Road at the landing, seen on the aerial beside the river; the stable itself was not found on the aerial.',
 'old-mud-meeting-house':'ArcGIS geocode of 730 Dry Branch Road, 30 m from the Wikipedia coordinate; checked on the aerial.',
 'morgan-row-harrodsburg':'ArcGIS geocode of 220 South Chiles Street; checked on the aerial.',
 'beaumont-inn-harrodsburg':'Wikipedia article coordinate; checked on the aerial.',
 'high-bridge-kentucky-river':'Position of the HMdb overlook marker in High Bridge Park; on the aerial it falls on the wooded rim just south of the park road, and the bridge itself is outside the tile.',
 'constitution-square-danville':'Wikipedia article coordinate; checked on the aerial.',
 'mcdowell-house-danville':'ArcGIS geocode of 125 South Second Street; checked on the aerial.',
 'old-centre-danville':'National Register list coordinate; checked on the aerial.',
 'jacobs-hall-danville':'National Register list coordinate; on the aerial it falls on a lawn among the school buildings, within the site.',
 'perryville-battlefield':'ArcGIS geocode of 1825 Battlefield Road, the park address; checked on the aerial.',
 'merchants-row-perryville':'ArcGIS geocode of 207 South Buell Street, behind the buildings on the street; HMdb gives the marker at 37.64997, -84.95192.',
 'penns-store-gravel-switch':'National Register list coordinate; on the aerial it is in trees by a road fork near the river and no store roof is visible, so prec is area.',
}
