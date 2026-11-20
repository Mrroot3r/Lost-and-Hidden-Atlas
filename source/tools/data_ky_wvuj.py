# November 20, 2026: Kentucky, a first statewide scatter (claimed as the thinnest state by tools/choose.py --thinnest; the
# Atlas then had 15 places there, all round Harrodsburg and Danville). Facts from the linked sources only, read in this
# session: Wikipedia through tools/wiki_raw.py, National Register forms through tools/page.py (npgallery text layers),
# Kentucky Historical Society and HMdb marker pages, and the managing bodies' own pages named in each access note.
# Kentucky State Parks pages (parks.ky.gov) are drawn by script and could not be read.
from data_b import N
from data_ma import W

BATCH={'key':'ky_wvuj','label':'Kentucky: a first statewide scatter','added':'2026-11-20 06:22'}

NPG='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'
HM='https://www.hmdb.org/m.asp?m='

PLACES=[
N('old-state-capitol-frankfort','Old State Capitol','Frankfort','ky','civic','standing',38.20030,-84.87655,'exact','open','walk','','1827–',
  'Kentucky\'s capitol from 1830 to 1910, voted by the legislature in 1827 and designed in the Greek Revival style by Gideon Shryock, then 25; it was his first building. William Goebel, claimant to the governorship after the bitter 1899 election, was shot here on his way to be inaugurated. The Kentucky Historical Society has kept it as a museum since 1920, and it is a National Historic Landmark.',
  'A temple front with no windows, copied from the Temple of Minerva Polias at Priene, a self-supporting stone stairway inside and a domed lantern above it. Wikipedia says it has been restored to its Civil War appearance. Open to visitors with the Kentucky Historical Society ticket (see hours).',
  'The windowless Greek temple that ran Kentucky for eighty years.',
  'Kentucky Historical Society, Old State Capitol at 300 West Broadway, Frankfort; the same ticket covers the Kentucky History Center (100 West Broadway) and the Kentucky Military History Museum. Hours from the Society\'s own page, which also warns that some areas may have limited access. Parking not checked.',
  [W('Old State Capitol (Kentucky)'),['Kentucky Historical Society: Old State Capitol Experience','https://history.ky.gov/visit/tour-old-state-capitol/']],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 5 p.m.'),

N('liberty-hall-frankfort','Liberty Hall','Frankfort','ky','landmark','standing',38.19979,-84.88118,'exact','open','walk','','1796–1800',
  'Senator John Brown built this house between 1796 and 1800 on four acres he bought in 1796, on a corner of the town James Wilkinson had laid out. It was one of the first brick houses in Frankfort, of bricks fired from local clay. It is a National Historic Landmark (1971) for Brown and for its Federal-style architecture.',
  'A two-story, five-bay brick house with a two-story rear ell, above the Kentucky River at Wilkinson and West Main streets, with the Orlando Brown House on the same grounds. Guided tours show first-floor rooms restored to the early 1800s and tell of the enslaved people who worked there; upstairs are an art gallery, the Brown library and an exhibit. Garden open after the tour. The house is not wheelchair accessible (five steps up).',
  'A senator\'s Federal house of 1796 above the Kentucky River.',
  'Owned and run by the National Society of the Colonial Dames of America in Kentucky, 218 Wilkinson Street. Its own page: two guided tours a day, Monday to Saturday, starting in front of Liberty Hall; call to reserve or walk in at tour times. Wikipedia says tours run mid-March to mid-November; the season is not on the page read. Parking not checked.',
  [W('Liberty Hall (Frankfort, Kentucky)'),['Liberty Hall Historic Site: Tour','https://www.libertyhall.org/visit']],
  conf='mixed',brick='yes',hours='Guided tours Monday to Saturday 11:30 a.m. and 1:30 p.m. (season not given on the page; Wikipedia says mid-March to mid-November)'),

N('switzer-covered-bridge','Switzer Covered Bridge','Switzer','ky','landmark','standing',38.25389,-84.75222,'exact','view','drive','','c.1855–',
  'Franklin County\'s only covered bridge, built by George Hockensmith about 1855 over North Elkhorn Creek. The Kentucky Historical Society marker says it was restored in 1906 by Louis Bower and closed to traffic in 1954; Wikipedia says it was nearly destroyed in 1953 but saved, and that high water knocked it off its foundations in March 1997, after which it was rebuilt that year.',
  'A timber lattice truss pinned with treenails, with a sawtooth edge at each portal. Length: 120 ft by the marker, 126 ft by Wikipedia; 11 ft wide. Kentucky Historical Society marker 1571 stands on KY 1262.',
  'A lattice bridge that a flood knocked off its piers and Kentucky put back.',
  'Off KY 1262 / Rocky Branch Road at Switzer. Who owns the bridge now, whether you may walk through it and where to park were not checked: look from the road.',
  [W('Switzer Covered Bridge'),['Kentucky Historical Society marker 1571: Switzer Covered Bridge','https://history.ky.gov/markers/switzer-covered-bridge'],['HMdb: Switzer Covered Bridge',HM+'11614']],
  conf='mixed',brick='no'),

N('old-washington-maysville','Old Washington','Maysville','ky','town','standing',38.61634,-83.80848,'site','public','walk','','1786–',
  'Founded in 1786 by Arthur Fox and William Wood on land bought from Simon Kenton, with Daniel Boone among the first trustees; by the 1790 census it was the second largest town in what became Kentucky. Harriet Beecher saw a slave auction in front of the old courthouse here in 1833, and Thornton Blackburn, whose case made Canada a safe end of the Underground Railroad, was held here as a slave from 1815 to 1824. Maysville took the county seat in 1848, the town hardly grew after the 1840s, and it is now a neighbourhood of Maysville.',
  'Still standing, by Wikipedia: the Marshall home on Green Street where Captain Thomas Marshall\'s family lived and died; the large house the postmaster William Murphy built on Old Main Street (the Murphy-Lashbrooke-Wood-Moose House), where Blackburn lived; the Key House on Main Street, where Harriet Beecher stayed, now the Harriet Beecher Stowe Slavery to Freedom Museum; and the Washington Presbyterian Church (the article gives both 1870 and 1871 for the present building). Its photographs also show the Paxton Inn and a log cabin of flatboat lumber. Interiors not checked.',
  'Kentucky\'s second town of 1790, left behind when the river town took over.',
  'Public streets in a neighbourhood of private houses and museums: look from the street. The pin is 2028 Old Main Street, the address a Lewis and Clark Trail listing gives for the district and its visitor centre. That listing (not the operator\'s own page) gives visitor-centre hours Wednesday to Friday 10:30 a.m. to 4:30 p.m., Saturday 9:30 a.m. to 4:30 p.m., Sunday 11:30 a.m. to 4:30 p.m., and calls it seasonal: hours not checked. Parking not checked.',
  [W('Washington, Kentucky'),['Lewis and Clark Trail: Old Washington Historic District','https://lewisandclark.travel/listing/old-washington-historic-district']],
  conf='mixed',brick='?'),

N('federal-hill-bardstown','Federal Hill (My Old Kentucky Home)','Bardstown','ky','landmark','standing',37.80676,-85.45666,'exact','open','walk','','1795–1818',
  'Judge John Rowan and his wife Ann Lytle built Federal Hill in two phases, by slave labour: the rear ell in 1795 and the three-story, five-bay main block by 1818. It is tied to Stephen Foster\'s song "My Old Kentucky Home", though Wikipedia says the song more likely came from Uncle Tom\'s Cabin than from a visit. Kentucky bought it and dedicated it on July 4, 1923; it passed to the state parks in 1936.',
  'Brick fired on the site and laid in Flemish bond on a limestone foundation; every room has mantels and window sills carved by a free Black craftsman, and the original springhouse survives. Wikipedia says 85 percent of the furniture shown belonged to the Rowans. Guided mansion tours, with the song sung by the guide.',
  'The house on the Kentucky quarter, with its carved mantels.',
  'Kentucky State Parks, My Old Kentucky Home State Park, 501 East Stephen Foster Avenue, Bardstown. From the park\'s own tour page: tours every hour, first come first served, last tour 4 p.m., up to 25 to a tour; closed Thanksgiving, Christmas Eve, Christmas Day and New Year\'s Day. Days of the week not given there. Park lots on state land.',
  [W('My Old Kentucky Home State Park'),['My Old Kentucky Home: Admission and tours','https://www.visitmyoldkyhome.com/admission']],
  brick='yes',hours='Mansion tours every hour, last tour 4 p.m.; closed Thanksgiving, Christmas Eve, Christmas Day and New Year\'s Day'),

N('st-joseph-proto-cathedral-bardstown','Basilica of St. Joseph Proto-Cathedral','Bardstown','ky','worship','standing',37.81071,-85.47104,'exact','open','walk','','1816–1823',
  'The first cathedral of the Catholic diocese that became the Archdiocese of Louisville, begun with a cornerstone laid on July 16, 1816 and built by John Rogers of Baltimore from local materials; Mass was said in it by 1819 and the interior was done by 1823. Benedict Joseph Flaget, the first bishop of Bardstown, was its pastor. It is now a parish church.',
  'Paintings and furnishings given by Pope Leo XII, King Louis-Philippe of France and King Francis I of the Two Sicilies. Nine paintings were cut from their frames by thieves in November 1952 and recovered by the FBI in 1953; one of the gifts was later restored at the Getty. The parish holds Mass every day and adoration in the afternoons (see hours).',
  'Kentucky\'s first cathedral, with paintings sent by a pope and a king.',
  'Parish church, 310 West Stephen Foster Avenue. Service times from the parish\'s own page. Parking not checked.',
  [W('Basilica of St. Joseph Proto-Cathedral'),['Basilica of St. Joseph Proto-Cathedral (parish site)','https://stjosephbasilica.org/']],
  brick='yes',hours='Mass Monday to Friday 8:45 a.m., Wednesday also 6 p.m.; Saturday 4 p.m.; Sunday 7, 9 and 11 a.m.; adoration Monday to Thursday noon to 4 p.m.'),

N('historic-locust-grove-louisville','Historic Locust Grove','Louisville','ky','landmark','standing',38.28769,-85.66267,'exact','open','walk','','c.1790–',
  'William Croghan and Lucy Clark Croghan founded the farm in 1790; their Georgian house was a gathering place for George Rogers Clark (Lucy\'s brother), Lewis and Clark and presidents. Enslaved African Americans built the house and outbuildings, and more than 40 were held here at the peak in 1820. Louisville Metro owns the 55-acre site, a National Historic Landmark, and Historic Locust Grove, Inc. runs it.',
  'The house of about 1790 and the visitors\' center with a museum. Guided house tours four times a day; grounds open on the same days. Interior details not checked.',
  'The house where George Rogers Clark spent his last years with his sister.',
  'Historic Locust Grove, 561 Blankenbaker Lane. Its own page: Tuesday to Saturday 10 a.m. to 5 p.m., tours at 10:30, 12, 1:30 and 3; $12 adults, $10 seniors, $6 ages 6 to 18; closed all of January, Thanksgiving, Christmas Eve and Day, New Year\'s Eve and Derby Day. Free parking in two lots in front of the visitors\' center. Leashed dogs on the grounds.',
  [W('Historic Locust Grove'),['Locust Grove: Plan your visit','https://www.locustgrove.org/plan-your-visit/']],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 5 p.m., house tours 10:30, 12, 1:30 and 3; closed January'),

N('riverview-hobson-grove','Riverview at Hobson Grove','Bowling Green','ky','landmark','standing',37.01197,-86.45969,'exact','open','walk','','1850s–1872',
  'Atwood and Juliet Hobson began this Italianate house above the Barren River in the 1850s; the Civil War stopped the work. Confederate General Simon Bolivar Buckner spared it, and his troops roofed the basement over and used it as a magazine. It was finished in 1872. The city bought the land meaning to pull it down for a golf course, but it was restored and opened for tours in 1972.',
  'Arched windows, deep bracketed eaves and a cupola whose eight windows draw hot air up through the house. Restored to the Victorian period, with gardens. Open for tours (see hours).',
  'A house a Confederate general spared and used as a powder store.',
  'City of Bowling Green, in Hobson Grove Park, 1100 West Main Avenue. The city\'s page: $12 adults, $10 seniors, veterans and active military; allow an hour. Parking not checked.',
  [W('Riverview at Hobson Grove'),['City of Bowling Green: Riverview, plan your visit','https://bgky.org/riverview/visit']],
  brick='yes',hours='Tuesday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.; closed Monday'),

N('south-union-shaker-village','South Union Shaker Village','Auburn','ky','town','standing',36.88472,-86.64444,'site','open','walk','','1807–1922',
  'Shakers founded South Union in 1807 and kept it until 1922, building some 200 buildings and farming 6,000 acres. After the Civil War they hired freedmen for their mills; in 1868 a white mob burned freedmen\'s cabins and then the Shakers\' uninsured mills. The property was sold to the Benedictines in 1949.',
  'The 1824 Centre House, a 40-room dwelling, now holds the Shaker Museum with original Shaker furniture and craft. The village is on the National Register as the South Union Shakertown Historic District. Other buildings not checked.',
  'Kentucky\'s other Shaker village, quieter than Pleasant Hill.',
  'South Union Shaker Village (a nonprofit), off US 68 at South Union. Its own page: open Tuesday to Saturday 10 a.m. to 4 p.m. Central time; children 6 to 12 $5, seniors $12, military $10 (adult price not on the lines read). Parking not checked.',
  [W('Shaker Museum at South Union'),W('South Union Shaker Center House and Preservatory'),W('South Union, Kentucky'),
   ['South Union Shaker Village: Admission','https://www.southunionshakervillage.com/visit-south-union-shaker-village/']],
  brick='?',hours='Tuesday to Saturday 10 a.m. to 4 p.m. (Central time)'),

N('old-mulkey-meetinghouse','Old Mulkey Meetinghouse','Tompkinsville','ky','worship','standing',36.67778,-85.70750,'exact','public','walk','','1804–',
  'The Mill Creek Baptist Church, led by Philip Mulkey, voted in May 1804 for a meeting house 50 by 30 feet with five windows and three doors, and Jiles Thompson built it that year. It is the oldest log meeting house in Kentucky. The congregation stopped using it about 1885, and it became a state shrine in 1931.',
  'Half-hewn log walls chinked with rocks and mud, laid out as a cross with twelve corners and three doors; inside, the Register form saw huge cross beams, peg-leg benches and a rough handmade pulpit (the shingle roof and puncheon floor are replacements). There was never any heating. In the churchyard lie Hannah Boone, Daniel Boone\'s sister, and fifteen Revolutionary War soldiers.',
  'Kentucky\'s oldest log meeting house, shaped like a cross.',
  'Kentucky State Parks, Old Mulkey Meetinghouse State Historic Site, off Old Mulkey Park Road south of Tompkinsville. Hours from the Office of Kentucky Nature Preserves\' page (the parks\' own page could not be read). Parking not checked.',
  [W('Old Mulkey Meetinghouse State Historic Site'),['National Register form (1973)',NPG+'73000821_text'],
   ['Office of Kentucky Nature Preserves: Old Mulkey Meeting House','https://eec.ky.gov/Nature-Preserves/Locations/Pages/Old-Mulkey-Meeting-House.aspx']],
  brick='no',hours='Daily 8 a.m. to 5 p.m. April to October; Tuesday to Saturday in November, December and March; by appointment January and February'),

N('columbus-belmont-state-park','Columbus-Belmont State Park','Columbus','ky','fort','traces',36.76624,-89.11091,'site','public','walk','forts','1861–',
  'Confederate General Leonidas Polk fortified the bluff here from September 3, 1861, naming it Fort De Russey; he called it the "Gibraltar of the West". It had 143 cannons and a chain across the Mississippi to Belmont, Missouri, to stop Union boats. Floods in the 1920s washed much of the earthworks, buildings and guns off the bluff.',
  'The giant chain, exposed when the 1925 flood went down, and its anchor of four to six tons, on a stone monument the Civilian Conservation Corps built in 1934; the remains of the "Lady Polk" experimental cannon; earthworks on the bluff; and a restored building used as a museum.',
  'The chain that was meant to close the Mississippi.',
  'Kentucky State Parks, Columbus (the federal public-land map shows the park lot on park land). The park\'s own page could not be read; Wikipedia says the museum is open daily May to September and at weekends in April and October: hours not checked.',
  [W('Columbus-Belmont State Park'),['American Battlefield Trust: Columbus-Belmont State Park','https://www.battlefields.org/visit/heritage-sites/columbus-belmont-state-park']],
  th=[36.76558,-89.11085],thn='Park lot off Roggers Street (OpenStreetMap)',brick='?'),

N('center-furnace-lbl','Center Furnace','Golden Pond','ky','industry','ruins',36.89969,-88.03865,'site','public','walk','','1852–1912',
  'Daniel Hillman built this charcoal iron furnace by 1852, the Kentucky Historical Society marker says; it was also called Hematite. It ran, not always, until 1912, and in 46 weeks of 1856 made 2,139 tons of pig iron, mostly shipped by steamboat. It was one of eight furnaces in what is now Land Between the Lakes.',
  'Little of the stack stands: a guide to the furnaces calls it much more decayed than the Great Western Furnace. A 0.3-mile interpretive trail, with stairs, leads past signs and traces of the iron works.',
  'An ironworks of the Between the Rivers country, now a short woodland trail.',
  'Land Between the Lakes National Recreation Area (USDA Forest Service), off Silver Trail Road near Hematite Lake and the Woodland Nature Station. Trails open year-round by the recreation area\'s trail page. Use the furnace trail parking on the Nature Station trail map, not the Hematite Lake picnic area. The roadside marker is 2.5 miles away on KY 274.',
  [['Kentucky Historical Society marker (HMdb): Center Furnace',HM+'136776'],['Explore Kentucky Lake: Iron furnaces in Land Between the Lakes','https://www.explorekentuckylake.com/lbl/iron-furnaces'],
   ['LBL Guide: Center Furnace Trail','https://lblguide.com/?p=699'],['Land Between the Lakes: Trails','https://www.landbetweenthelakes.us/?p=2122']],
  th=[36.90045,-88.03979],thn='Center Furnace Trailhead, Forest Service Road 133 (OpenStreetMap)',brick='?'),

N('cottage-furnace-estill','Cottage Furnace','Irvine','ky','industry','ruins',37.75752,-83.91429,'exact','public','hike','','1854–1879',
  'A charcoal iron furnace of rough-hewn sandstone, built in 1854 and worked until 1879 in the Red River Iron District. Some iron was cast into household wares for the Bluegrass; most went as pig iron to the forge and rolling mill at Clay City to be made into bars and nails.',
  'The stone stack, which the 1973 Register form found in good condition with few stones missing, most of them off the top, and cracks starting; the inside is filled. Interpretive signs.',
  'A sandstone furnace stack a mile up a gated forest road.',
  'Daniel Boone National Forest (USDA Forest Service), off Marbleyard Road. The Forest Service page: on Cottage Furnace Ruins Road (Forest Road 231), about a mile past the gate, with limited parking; open year-round, 24 hours, no fee, no toilets or water. Directions there: from Irvine, KY 89 north, Rice Street to Sweet Lick Road, then Henry Mountain Road (FS 227) to the ridge top; the gate is on the right.',
  [['USDA Forest Service: Cottage Furnace Interpretive Site','https://www.fs.usda.gov/r08/danielboone/recreation/cottage-furnace-interpretive-site'],['National Register form (1973)',NPG+'73000794_text']],
  brick='no',hours='Open all year, 24 hours'),

N('white-hall-richmond','White Hall','Richmond','ky','landmark','standing',37.83318,-84.35269,'exact','open','walk','','1798–',
  'General Green Clay built an eight-room Georgian house here in 1798–1799 and called it Clermont. His son Cassius Marcellus Clay, the anti-slavery publisher and Lincoln\'s minister to Russia, and Mary Jane Warfield Clay enlarged it into the 44-room Italianate White Hall, designed by Thomas Lewinski. Restored, it opened to the public in 1971.',
  'The 44-room house, a kitchen of 1790 from Green Clay\'s time, and furnishings that include part of Clay\'s 104-piece china service from Russia. Interior otherwise not checked.',
  'Cassius Clay\'s house, wrapped round his father\'s.',
  'Kentucky State Parks, White Hall State Historic Site, off White Hall Shrine Road north of Richmond. The parks\' own page could not be read: hours not checked. Parking not checked.',
  [W('White Hall State Historic Site')],
  brick='yes',hours='?'),

N('camp-nelson-national-monument','Camp Nelson','Nicholasville','ky','fort','traces',37.79766,-84.60142,'area','public','walk','forts','1863–1866',
  'A Union supply depot set up in 1863 by Hickman Bridge, the only Kentucky River bridge above Frankfort, and named for the murdered General William Nelson. It became a recruiting ground for East Tennesseans and for enslaved men, who enlisted here, and a refuge for their families; about 300 refugees who died here are remembered at the refugee cemetery. It became a national monument on October 26, 2018.',
  'Five miles of trails along the northern edge, where remnants of the forts and fortifications are marked by signs; Fort Putnam rebuilt to its original plan; reconstructed barracks and a museum. The Oliver Perry House of about 1846, called the "White House" in camp letters and the only building left from the camp, is closed for renovation.',
  'Where thousands of enslaved Kentuckians walked in to join the Union army.',
  'National Park Service, Camp Nelson National Monument (the lot by the visitor centre is on monument land on the federal map), on the old Danville Pike beside US 27, about 6 miles south of Nicholasville; the visitor centre is just inside the gate. No fees. The NPS page gives the visitor centre, museum and barracks 9 a.m. to 5 p.m. daily from Memorial Day to Labor Day 2026 and does not say for the rest of the year; grounds open daily, sunrise to sunset.',
  [W('Camp Nelson National Monument'),['National Park Service: Camp Nelson basic information','https://www.nps.gov/cane/planyourvisit/basicinfo.htm']],
  th=[37.79718,-84.60128],thn='Monument lot by the visitor centre (OpenStreetMap)',brick='?',hours='Grounds daily sunrise to sunset; visitor centre and barracks 9 a.m. to 5 p.m. daily Memorial Day to Labor Day (other months not given)'),

N('ashland-henry-clay-estate','Ashland, the Henry Clay Estate','Lexington','ky','landmark','standing',38.02936,-84.47976,'exact','open','walk','','1857–',
  'Henry Clay\'s farm and home, where at its largest he held more than 600 acres and 60 enslaved people. Poor brick made his house unstable, and his son James Brown Clay had it razed in 1854 and rebuilt by 1857 to Thomas Lewinski\'s design on the old footprint, foundation and floor plan. Clay\'s great-granddaughter\'s family lived here from 1883; the house opened as a museum in 1950.',
  'The 1857 mansion on the plan of Clay\'s own house, shown by guided tour, with grounds exhibits and gardens. Interior details not checked.',
  'Henry Clay\'s house, rebuilt by his son on the same footings.',
  'Henry Clay Memorial Foundation, 120 Sycamore Road at Richmond Road. Its own page: tours $25 adults, $15 students, free under 5; mansion Tuesday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m. (closed Sundays in March and December); grounds and gardens 8 a.m. to 5 p.m. daily; closed Mondays, major holidays and all of January and February. Paved lot entered from Fincastle Road (a GPS sends you to the front of the house).',
  [W('Ashland (Henry Clay estate)'),['Henry Clay Estate: Tours','https://henryclay.org/visit/tours/']],
  brick='yes',hours='Tuesday to Saturday 10 a.m. to 4 p.m., Sunday 1 to 4 p.m.; grounds 8 a.m. to 5 p.m.; closed Mondays and January to February'),
]

PIN_NOTES={
 'old-state-capitol-frankfort':'Wikipedia coordinate; the ArcGIS geocoder\'s point for 300 West Broadway is 30 m away.',
 'liberty-hall-frankfort':'ArcGIS geocoder PointAddress for 218 Wilkinson Street (Wikipedia\'s point is 5 m away).',
 'switzer-covered-bridge':'Wikipedia coordinate; the OpenStreetMap way for the bridge is 7 m away.',
 'old-washington-maysville':'ArcGIS geocoder PointAddress for 2028 Old Main Street, the address given for the district; Wikipedia\'s point for the town is 50 m away.',
 'federal-hill-bardstown':'Moved with pix.py from the Wikipedia point (in trees, 48 m away) onto the brick house with the red roof the aerial shows; not confirmed against a plan of the park.',
 'st-joseph-proto-cathedral-bardstown':'ArcGIS geocoder PointAddress for 310 West Stephen Foster Avenue.',
 'historic-locust-grove-louisville':'ArcGIS geocoder PointAddress for 561 Blankenbaker Lane.',
 'riverview-hobson-grove':'ArcGIS geocoder PointAddress for 1100 West Main Avenue.',
 'south-union-shaker-village':'Wikipedia coordinate for the Shaker Museum (Centre House).',
 'old-mulkey-meetinghouse':'National Register list coordinate.',
 'columbus-belmont-state-park':'ArcGIS geocoder point for the park, beside the park lot; the Wikipedia point lands in woods 360 m east. Where the chain and anchor stand in the park was not found.',
 'center-furnace-lbl':'OpenStreetMap point for the Center Iron Furnace ruins, off Forest Service Road 134; the Register list point is 10 m away.',
 'cottage-furnace-estill':'OpenStreetMap point for the furnace ruins; the Forest Service page gives 37.75739, -83.91432, 15 m away.',
 'white-hall-richmond':'Moved with pix.py from the Wikipedia point (on a lawn) onto the large dark-roofed house 61 m northwest on the aerial.',
 'camp-nelson-national-monument':'OpenStreetMap building for the Oliver Perry "White House", by the visitor centre; the forts and trails spread over the 525-acre monument, so area only. The Wikipedia point was on a field 1.1 km south.',
 'ashland-henry-clay-estate':'OpenStreetMap building tagged historic=manor, Ashland; the geocoder point for 120 Sycamore Road was in trees 140 m southwest.',
}
