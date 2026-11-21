# November 21, 2026: a first scatter across Georgia outside the northeast Piedmont, which held all 20 earlier places:
# the coast from Savannah to Cumberland Island, the Ebenezer Salzburger church, Augusta, Macon, Andersonville,
# Dahlonega, Chatsworth and Cartersville (ground claimed with tools/choose.py --thinnest).
# Facts from the linked sources only, read in this session: Wikipedia through tools/wiki_raw.py; National Park Service,
# Georgia State Parks, Jekyll Island Authority, Midway Museum, Jerusalem Lutheran Church, Hay House and HMdb pages through
# tools/page.py. exploregeorgia.org answered 403; nothing was taken from it.
from data_b import N
from data_ma import W

BATCH={'key':'ga_mhty','label':'Georgia: the coast, Ebenezer, Augusta, Macon, Andersonville and the north','added':'2026-11-21 18:21'}

HM='https://www.hmdb.org/m.asp?m='
GSP='https://gastateparks.org/'

PLACES=[
N('fort-pulaski','Fort Pulaski','Savannah (Cockspur Island)','ga','fort','standing',32.02722,-80.89028,'exact','open','walk','forts','1829–1847',
  'A Third System brick fort on Cockspur Island at the mouth of the Savannah River, begun in 1829 (Robert E. Lee worked on it as a young lieutenant) and finished in 1847; wooden pilings driven up to 70 feet into the mud carry an estimated 25 million bricks. In April 1862 Union rifled cannon on Tybee Island breached it from long range, the test that showed brick forts were obsolete. It was later a prisoner-of-war camp, and is now Fort Pulaski National Monument.',
  'The whole brick fort, with its casemates and exhibit rooms, which the Park Service says have ramps. A museum opened in the 1980s.',
  'The brick fort that rifled cannon made obsolete in a day and a half.',
  'Fort Pulaski National Monument (National Park Service), 41 Cockspur Island Road off US 80 between Savannah and Tybee Island. Every visitor needs an entrance pass (America the Beautiful passes accepted; the fee itself was not read). Hours from the Park Service\'s "Explore Fort Pulaski" and visitor center pages; the park\'s own hours page is drawn by script and was not read.',
  [W('Fort Pulaski National Monument'),['NPS: Explore Fort Pulaski','https://www.nps.gov/thingstodo/explore-fort-pulaski.htm'],
   ['NPS: Fort Pulaski visitor center','https://www.nps.gov/thingstodo/visit-fort-pulaski-s-visitor-center.htm'],['NPS: fees and passes','https://www.nps.gov/fopu/planyourvisit/fees.htm']],
  th=[32.0277,-80.89246],thn='Fort Pulaski lot on Fort Pulaski Road',brick='yes',hours='Fort 9 a.m. to 4:30 p.m. daily; visitor center 9 a.m. to 5 p.m.'),

N('wormsloe-tabby-ruins','Wormsloe tabby ruins','Savannah (Isle of Hope)','ga','landmark','ruins',31.95955,-81.06946,'site','open','walk','','1739–1745',
  'Noble Jones, a carpenter who came to Georgia with Oglethorpe in 1733, built a small fortified house of wood and tabby (oyster shell and lime) on the southeast tip of the Isle of Hope between 1739 and 1745, watching the Skidaway Narrows. His descendants turned Wormsloe into a plantation worked by enslaved people. The state acquired most of the property in 1973; the family still lives in the 1828 house on 50 acres it kept.',
  'A 1.5-mile dirt avenue under live oaks, a museum of finds from the site, and a walking trail through maritime forest to the tabby walls of the 1740s house, which the state calls one of the oldest standing structures in Savannah. Drainage ditches dug by enslaved people remain on the property. The trail goes on to a Colonial Life Area used for demonstrations on program days.',
  'The tabby walls at the end of Savannah\'s most famous oak avenue.',
  'Wormsloe State Historic Site (Georgia Department of Natural Resources), Skidaway Road, Isle of Hope. Admission charged (children under 6 $3.25; adult rate not read). The family house and its 50 acres are private. Hours from the state park page.',
  [W('Wormsloe Historic Site'),['Georgia State Parks: Wormsloe',GSP+'Wormsloe']],
  th=[31.96339,-81.07084],thn='Wormsloe lot by the museum, Live Oak Avenue',brick='no',hours='Daily 9 a.m. to 4:45 p.m.; closed Thanksgiving and Christmas'),

N('fort-mcallister','Fort McAllister earthworks','Richmond Hill','ga','fort','traces',31.89111,-81.19611,'site','open','walk','forts','',
  'Confederate earthworks on the south bank of the Ogeechee River, about ten miles south of Savannah. Union ironclads attacked the fort seven times without taking it; it fell only in December 1864 to Sherman\'s army at the end of the March to the Sea. The state park calls it the best-preserved earthwork fortification of the Confederacy.',
  'Earthen walls with cannon, a hot shot furnace, bombproof barracks and palisades (state park page), and a Civil War museum with a film. Interior of the museum not described further.',
  'The sand fort that ironclads could not crack.',
  'Fort McAllister State Park (Georgia DNR), off Georgia 144 east of Richmond Hill. Parking fee required; museum admission charged (rate not read). Hours from the state park page.',
  [W('Fort McAllister Historic State Park'),['Georgia State Parks: Fort McAllister',GSP+'FortMcAllister']],
  th=[31.88913,-81.20027],thn='Lot on Fort McAllister Road',brick='?',hours='Historic site 8 a.m. to 5 p.m.; park 7 a.m. to 10 p.m.'),

N('midway-congregational-church','Midway Congregational Church','Midway','ga','worship','standing',31.806,-81.4303,'exact','view','drive','','1792',
  'Congregationalists who had come from New England by way of South Carolina founded the Midway Society in a log meeting house in 1754. A second church, built two years later, was destroyed by the British in the Revolution; the present New England-style meeting house was completed in 1792. Enslaved people entered by a smaller side door to a gallery. The congregation left in 1892, and the Midway Society has kept the building and graveyard since.',
  'The 1792 meeting house with its central door and the smaller side door to the slave gallery (Midway Museum), beside its walled cemetery on US 17. No regular services; the Midway Society holds a service there each April. Whether the inside can be seen at other times was not checked.',
  '',
  'Beside US 17 in Midway, opposite the Midway Museum. Kept by the Midway Society. The museum gives tours Tuesday to Saturday 10 a.m. to 4 p.m. (its own page); whether it holds a key to the church was not checked.',
  [W('Midway Congregational Church'),['Midway Museum: Midway Church','https://www.themidwaymuseum.org/midway-church/'],['Midway Museum: visit','https://www.themidwaymuseum.org/?p=281']],
  brick='?'),

N('jerusalem-lutheran-church-ebenezer','Jerusalem Lutheran Church, Ebenezer','Rincon','ga','worship','standing',32.37667,-81.18085,'site','open','drive','','1767–1769',
  'All that remains of Ebenezer, the town of Protestant refugees from Salzburg and southern Germany who came to Georgia soon after 1733. They built the church between 1767 and 1769 of brick made from clay near the site, with walls 21 inches thick. The British took Ebenezer in January 1779 and the town never recovered. It is called the oldest church building in Georgia, and its congregation the oldest continuing Lutheran one in the country.',
  'The brick church, with fingerprints of the brickmakers still in the bricks, some original window glass, and bells brought from Europe, rung before each service (the Ebenezer visitors\' site). Across the road the Georgia Salzburger Society runs a small museum, and a colonial Salzburger cabin has been moved beside it; remains of a British redoubt are visible near the New Ebenezer Retreat Center (Georgia Trust).',
  'Georgia\'s oldest church, with the brickmakers\' fingerprints in its walls.',
  '2966 Ebenezer Road, Rincon; a working congregation. Service times from the congregation\'s own page; the Ebenezer visitors\' site says the services are held in the old church. Museum hours not checked.',
  [W('Ebenezer, Georgia'),['Jerusalem Lutheran Church: worship','https://www.jerusalemlutheran.org/'],
   ['Go Visit Ebenezer: Jerusalem Lutheran Church','https://govisitebenezer.com/?p=47'],
   ['Georgia Trust: The Salzburger town that Georgia refused to forget','https://www.georgiatrust.org/georgia-250/the-salzburger-town-that-georgia-refused-to-forget-jerusalem-lutheran-church-rincon-ga/']],
  brick='yes',hours='Sundays 8 and 11 a.m.; Memorial Day to Labor Day, Sundays 9:30 a.m. and Thursdays 7 p.m.'),

N('horton-house-jekyll','Horton House tabby ruins','Jekyll Island','ga','landmark','ruins',31.10177,-81.41456,'site','public','drive','','1743',
  'Major William Horton, an aide to Oglethorpe, rebuilt his house in tabby in 1743 after a Spanish attack destroyed his first one; he also brewed Georgia\'s first beer on the plantation. The du Bignon family, who owned Jekyll from 1790 to 1886, lived in the house into the mid-1800s. It is one of the oldest tabby buildings in Georgia.',
  'The roofless two-storey tabby walls of the house; across the road the tabby wall round the du Bignon family cemetery; and the brewery ruins a few hundred yards along the road (Wikipedia).',
  'Georgia\'s oldest brewery, and the tabby house beside it.',
  'On Riverview Drive, Jekyll Island, a state park run by the Jekyll Island Authority. Every vehicle entering the island pays a parking fee ($10 a day as read on the authority\'s page, more on event days). Hours not checked.',
  [W('Horton House'),['Jekyll Island Authority: Horton House','https://www.jekyllisland.com/history/sites/horton-house/'],['Jekyll Island Authority: parking','https://www.jekyllisland.com/plan-your-trip/parking/']],
  th=[31.10216,-81.41449],thn='Small lot at Horton House, Riverview Drive',brick='no'),

N('fort-frederica','Fort Frederica','St. Simons Island','ga','fort','ruins',31.22384,-81.39325,'exact','open','walk','forts','1736–1758',
  'The fort and town James Oglethorpe built on St. Simons Island from 1736 to guard the southern edge of the Georgia colony against Spain; English, Scottish and German colonists settled it. The town survived a fire in 1758 but was abandoned a few years later; William Bartram found it in ruins in 1774. Archaeologists have since uncovered its streets and house sites.',
  'The remains of the fort on the river, its magazine and barracks, and excavated house foundations of the town (Wikipedia photographs). Visitor center with exhibits.',
  '',
  'Fort Frederica National Monument (National Park Service), off Frederica Road on St. Simons Island. Admission free (Wikipedia). The Bloody Marsh unit, a separate battlefield site, keeps 8:30 a.m. to 4 p.m. daily. Hours from the Park Service hours page; closed some holidays.',
  [W('Fort Frederica National Monument'),['NPS: Fort Frederica hours','https://www.nps.gov/fofr/planyourvisit/hours.htm']],
  th=[31.22282,-81.38869],thn='Fort Frederica visitor center lot',brick='?',hours='Grounds and trails 9 a.m. to 5 p.m. daily; visitor center Wednesday to Sunday 9 a.m. to 5 p.m.'),

N('hofwyl-broadfield-plantation','Hofwyl-Broadfield Plantation','Brunswick','ga','landmark','standing',31.30487,-81.45643,'site','open','walk','','1807–1942',
  'A rice plantation carved from the Altamaha River marshes by enslaved West Africans from 1807; when its owner died in 1849 it held 357 people as slaves on 7,300 acres. The present main house was built in the early 1850s. The family grew rice until about 1913–1915 and ran a dairy until 1942. The state has managed it as a historic site since 1976.',
  'A short film, then a walk to the 1850s house; a nature trail returns along the marsh where the rice fields were (state park page). Interior furnishings not checked.',
  '',
  'Hofwyl-Broadfield Plantation State Historic Site (Georgia DNR), on US 17 north of Brunswick. Admission charged (children under 6 $2.25; adult rate not read). Leashed dogs on trails, not in buildings. Hours from the state park page.',
  [W('Hofwyl-Broadfield Plantation'),['Georgia State Parks: Hofwyl-Broadfield',GSP+'HofwylBroadfieldPlantation']],
  conf='mixed',brick='?',hours='Tuesday to Sunday 9 a.m. to 5 p.m.'),

N('dungeness-ruins-cumberland','Dungeness ruins','Cumberland Island','ga','landmark','ruins',30.74844,-81.47087,'exact','boat','boat','burned','1800–1959',
  'Nathanael Greene\'s widow, Catharine, built a four-storey tabby mansion here in 1800 over a Timucuan shell mound; "Light-Horse Harry" Lee died in it in 1818. It burned in 1866. Thomas Carnegie, Andrew\'s brother, bought the land in the 1880s and built a 59-room Queen Anne mansion, finished after his death in 1886; the family moved out in 1925, and the house was destroyed by fire in 1959, said to be arson.',
  'The burned shell of the Carnegie mansion and the ruins of its estate, kept by the Park Service; the Tabby House (Nathanael Greene Cottage) from the Greene years still stands nearby.',
  'A Carnegie mansion burned to its walls on a wild island.',
  'Cumberland Island National Seashore (National Park Service). Reached only by passenger ferry from St. Marys (about 45 minutes; reservations at cumberlandislandferry.com, trips sell out). Entrance fee $15 per person for 7 days. Ferry departs 9 and 11:45 a.m. daily March to November, and not on Tuesdays and Wednesdays December to February. Which dock is closest and how far the walk is was not checked.',
  [W('Dungeness (Cumberland Island, Georgia)'),['NPS: Cumberland Island hours and ferry','https://www.nps.gov/cuis/planyourvisit/hours.htm'],['NPS: Cumberland Island fees','https://www.nps.gov/cuis/planyourvisit/fees.htm']],
  brick='?'),

N('andersonville-prison','Andersonville prison site (Camp Sumter)','Andersonville','ga','inst','traces',32.19472,-84.12889,'site','open','walk','','1864–1865',
  'The Confederate prisoner-of-war camp held about 45,000 Union soldiers between February 1864 and April 1865, and nearly 13,000 of them died. It began as 16.5 acres inside a 15-foot stockade and was enlarged to 26.5 acres in June 1864.',
  'The 26.5-acre prison ground, outlined with double rows of white posts, with two stretches of stockade rebuilt (the north gate and the northeast corner); the national cemetery; and the National Prisoner of War Museum (1998), which is the visitor center.',
  '',
  'Andersonville National Historic Site (National Park Service), on Georgia 49 near Andersonville. Hours from the Park Service hours page; closed only Thanksgiving, Christmas and New Year\'s Day. The national cemetery opens daily from 8 a.m. Fees not checked.',
  [W('Andersonville Prison'),['NPS: Andersonville hours','https://www.nps.gov/ande/planyourvisit/hours.htm']],
  th=[32.19443,-84.13094],thn='Lot on Prison Site Road',brick='no',hours='Grounds 8 a.m. to 5 p.m. daily; museum 9:30 a.m. to 4:30 p.m.'),

N('dahlonega-gold-museum','Old Lumpkin County Courthouse (Dahlonega Gold Museum)','Dahlonega','ga','civic','standing',34.53267,-83.98488,'exact','open','drive','','1836',
  'The Lumpkin County courthouse, built in 1836 in the middle of the town square during America\'s first major gold rush, is called the oldest surviving county courthouse in Georgia. A federal branch mint in Dahlonega coined more than $6 million in gold from 1838 to 1861. The building is now a state historic site telling the gold rush story.',
  'The courthouse itself, with wooden chapel seats from 1889 and the judge\'s chambers (state park page), and exhibits of nuggets, coins and panning tools. Some second-floor exhibits have no lift.',
  '',
  'Dahlonega Gold Museum State Historic Site (Georgia DNR), on the public square. Admission charged (children 6 and under $3.50; adult rate not read). Closed Thanksgiving, Christmas and New Year\'s Day. Hours from the state park page.',
  [W('Dahlonega Gold Museum Historic Site'),['Georgia State Parks: Dahlonega Gold Museum',GSP+'DahlonegaGoldMuseum']],
  brick='?',hours='Monday to Saturday 9 a.m. to 4:45 p.m.'),

N('chief-vann-house','Chief Vann House','Chatsworth (Spring Place)','ga','landmark','standing',34.7631,-84.82189,'site','open','drive','','1803–1804',
  'James Vann, the wealthiest man in the Cherokee Nation, had this two-and-a-half-storey house built in 1803–1804, the first brick house in the nation, of bricks from the red clay of his own plantation. His son Joseph ("Rich Joe") was forced out in 1835 and went west on the Trail of Tears. The state restored it from 1958 over six years.',
  'Solid brick walls about 18 inches thick outside, hand-wrought nails and hinges from Vann\'s own smithy, painted interiors in red, blue, green and yellow, a 12-foot mantel, carvings, and a cantilevered "floating" staircase, one of the oldest in Georgia (Wikipedia; state park page).',
  'The brick "showplace of the Cherokee Nation" and its floating staircase.',
  'Chief Vann House State Historic Site (Georgia DNR), at Spring Place east of Chatsworth. Seen only on guided tours, on the hour, last at 4 p.m. Adults $7 plus tax. Closed Thanksgiving, Christmas and New Year\'s Day. Hours from the state park page.',
  [W('Chief Vann House Historic Site'),['Georgia State Parks: Chief Vann House',GSP+'ChiefVannHouse']],
  th=[34.76359,-84.82101],thn='Chief Vann House lot, Joseph Vann Highway',brick='yes',hours='Thursday to Saturday 9 a.m. to 5 p.m., Sunday 1 to 5 p.m. (no Sundays December to March)'),

N('coopers-furnace','Cooper\'s Furnace (Etowah Iron Works)','Cartersville','ga','industry','ruins',34.16474,-84.73365,'exact','public','walk','burned','before 1847–1864',
  'The stack of an iron furnace built by Moses Stroup, all that is left of Mark Anthony Cooper\'s ironworks at the vanished town of Etowah. Cooper, a congressman, bought into the furnace and in 1847 he and Leroy M. Wiley bought Stroup out, adding a nail factory, rolling mill and flour mill. Cooper sold the works in 1862; Union troops burned the plant on May 22, 1864, but left the furnace stack standing.',
  'The stone stack of the furnace, with its arched opening (Wikimedia Commons photographs), in a Corps of Engineers day-use area on the Etowah River below Allatoona Dam, with the HMdb-listed marker. Trails start from the day-use area.',
  'An iron furnace that outlived its whole town.',
  'Cooper\'s Furnace Day Use Area, Allatoona Lake (U.S. Army Corps of Engineers), on Old River Road southeast of Cartersville: picnic shelters, restroom, trails. Hours and fees not checked (recreation.gov gives none).',
  [['HMdb: Mark Anthony Cooper\'s Iron Works',HM+'56319'],W('Mark A. Cooper'),['Recreation.gov: Cooper\'s Furnace Day Use Area','https://www.recreation.gov/camping/poi/251866']],
  th=[34.16466,-84.73206],thn='Cooper\'s Furnace Day Use Area lot, Old River Road',brick='no'),

N('sibley-mill-augusta','Sibley Mill','Augusta','ga','industry','standing',33.48728,-81.99197,'exact','view','drive','','1880–1882',
  'A cotton mill built on the Augusta Canal in 1880–1882 on the site of the Confederate Powderworks, using half a million bricks bought from the old powder works. Its ornate exterior has been called eclectic and neo-Gothic. Textiles were made here until 2006. The Augusta Canal Authority bought it in 2010 and still runs its hydropower; it was leased in 2016 to a technology company.',
  'Two towers, one for the bell and one for a water tank, at the centre of the front; the tall chimney in front is a relic of the Confederate Powderworks (Wikipedia). A 2005 Wikimedia Commons photograph shows the mill and chimney in red brick. Interior not open; not checked.',
  'A Gothic mill on the ground of the Confederacy\'s powder works.',
  '1717 Goodrich Street on the Augusta Canal; offices of private tenants. View from the street. The Kroc Center stands across the canal.',
  [W('Sibley Mill')],
  brick='yes'),

N('hay-house-macon','Hay House (Johnston–Felton–Hay House)','Macon','ga','landmark','standing',32.84029,-83.6336,'exact','open','drive','','1855–1859',
  'An Italian Renaissance Revival mansion of 24 rooms built from 1855 to 1859 on Coleman Hill by William Butler Johnston and Anne Tracy Johnston after a grand tour of Europe; a reporter called it "the palace of the South" in 1860. It was named a National Historic Landmark and given to the Georgia Trust for Historic Preservation in 1977.',
  'Hour-long guided tours of the first three levels; a two-hour behind-the-scenes tour on the second and fourth Saturdays climbs all seven levels to the widow\'s walk (Hay House page).',
  '',
  '934 Georgia Avenue, Macon; run by the Georgia Trust as a house museum. Tour times and prices were not read: the house\'s hours page did not open.',
  [W('Johnston–Felton–Hay House'),['Hay House','https://www.hayhousemacon.org/']],
  brick='?',hours='Guided tours Wednesday to Sunday (times not read)'),
]

PIN_NOTES={
'fort-pulaski':'Wikipedia coordinate.',
'wormsloe-tabby-ruins':'OpenStreetMap building mapped as the tabby ruins (osmnear.py); the Wikipedia coordinate fell in woods near the avenue. Under trees on the aerial; the ruin itself not seen. The parking point is the OpenStreetMap lot by the museum, hidden by trees on the aerial.',
'fort-mcallister':'Wikipedia coordinate, on the earthworks by the river on the aerial. Parking point is an OpenStreetMap lot at the edge of the trees.',
'midway-congregational-church':'Wikipedia coordinate.',
'jerusalem-lutheran-church-ebenezer':'OpenStreetMap church point (nom.py), between two buildings on the aerial; which is the 1769 church was not told apart.',
'horton-house-jekyll':'Wikipedia coordinate, beside Riverview Drive under trees; the walls not seen on the aerial.',
'fort-frederica':'OpenStreetMap fort point (nom.py), same as Wikipedia; on the riverside fort remains on the aerial. Parking point is the OpenStreetMap visitor-center lot, under trees on the aerial.',
'hofwyl-broadfield-plantation':'OpenStreetMap museum point (nom.py).',
'dungeness-ruins-cumberland':'Wikipedia coordinate, on the roofless mansion shell seen on the aerial.',
'andersonville-prison':'Wikipedia coordinate, in the open prison field on the aerial.',
'dahlonega-gold-museum':'Wikipedia coordinate.',
'chief-vann-house':'OpenStreetMap house point; the Wikipedia coordinate fell on the highway about 30 m west.',
'coopers-furnace':'OpenStreetMap ruin point (nom.py).',
'sibley-mill-augusta':'Wikipedia coordinate.',
'hay-house-macon':'OpenStreetMap museum point (nom.py).',
}
