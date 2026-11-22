# November 22, 2026: West Virginia, a second scatter across the state (it had 33 places, most in Jefferson County and
# along the New River Gorge). Ground claimed with tools/choose.py --thinnest (wv). Places in Marshall, Berkeley, Mineral,
# Hampshire, Mason, Nicholas, Pocahontas, Mercer, Mingo, Randolph, Preston, Lewis, Hardy, Fayette, Pendleton, Wayne and
# McDowell counties.
# Sources read: Wikipedia articles (tools/wiki_raw.py); with tools/page.py the pages of the WV Department of Arts, Culture
# and History (Grave Creek Mound), WV State Parks, WV Tourism (the state's tourism office: Carnifex Ferry, Droop
# Mountain), the Friends of Ashby's Fort, the WV Daughters of the American Revolution, SAH Archipedia, NPS (Martinsburg
# shops), Arthurdale Heritage, the US Forest Service (Seneca Rocks), WVU Jackson's Mill, Davis & Elkins College, the West
# Virginia Mine Wars Museum, West Virginia Public Broadcasting and the Glen Ferris Inn. Interiors were not visited by any
# source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'wv_fszp','label':'West Virginia: a second scatter across the state','added':'2026-11-22 14:26'}

WVSP='West Virginia State Parks (WV Division of Natural Resources). '
WVCH=['WV Culture: notice of operating hours','https://wvculture.org/west-virginia-division-of-culture-and-history-announces-new-operating-hoursfor-the-culture-center-grave-creek-mound-independence-hall-museum-in-the-park-and-the-state-museum/']

PLACES=[
N('grave-creek-mound','Grave Creek Mound','Moundsville','wv','burial','standing',39.91684,-80.74466,'exact','public','walk','','250–150 BC',
  'One of the largest conical burial mounds in the United States, raised by people of the Adena culture in stages around 250 to 150 BC; they moved more than 60,000 tons of earth. Amateurs dug three shafts into it in 1838 and found two burial chambers. Women of the Wheeling chapter of the Daughters of the American Revolution saved it from development in 1908, and the state bought it in 1909. It is a National Historic Landmark (1964), and the state\'s Delf Norona Museum beside it opened in 1978.',
  'An earth mound about 62 feet high and 240 feet across, in the middle of town (Wikipedia). A ditch about 40 feet wide and five deep once ringed it, with at least one causeway (state\'s page). The museum next to it covers fossils, West Virginia archaeology and the Adena people; admission is free (state\'s page). This is a burial place: keep to the paths.',
  'Sixty thousand tons of earth, carried by hand two thousand years ago.',
  'West Virginia Department of Arts, Culture and History (Grave Creek Archaeological Complex). The complex is open year-round; the museum is open Tuesday to Saturday and free (state\'s page, read November 22, 2026). The 9 a.m. to 5 p.m. times come from a Division of Culture and History notice whose year was not checked. Parking not checked.',
  [W('Grave Creek Mound'),['WV Culture: Grave Creek Mound','https://wvculture.org/explore/grave-creek-mound/'],WVCH],
  brick='no',hours='Museum Tuesday to Saturday 9 a.m. to 5 p.m.; free'),

N('bo-martinsburg-shops-roundhouse','Baltimore and Ohio Railroad Martinsburg Shops (the Roundhouse)','Martinsburg','wv','rail','standing',39.45926,-77.96009,'site','open','drive','','1866–1988',
  'The B&O built its first shops here in 1848–1850; Confederate troops destroyed them in 1861 and burned the complex again in 1862. The present buildings went up from 1866 to 1872. The Great Railroad Strike of 1877, the first nationwide strike, began here on July 16, 1877. The shops closed in March 1988; a fire in 1990 left only parts of the East Roundhouse walls. Berkeley County bought the site in 1999 and passed it to the Berkeley County Roundhouse Authority. It is a National Historic Landmark (2003).',
  'The West Roundhouse of 1866, sixteen-sided with a domed roof, called the oldest fully covered roundhouse in the United States; its cast-iron roof frame, designed by Albert Fink, makes a spider\'s-web pattern seen only from inside (NPS). Also the Machine and Woodworking Shop and the Car Shop, and what is left of the East Roundhouse walls (NPS, Wikipedia).',
  'Where the 1877 railroad strike began.',
  'Owned by the Berkeley County Roundhouse Authority, a public body. NPS says it is used for public events and private rentals; Wikipedia says the buildings are open for public tours. Tour days and times not checked; the authority\'s own page was not read. Street address 100 Vicky Bullett Street (OpenStreetMap). Parking not checked.',
  [W('Baltimore and Ohio Railroad Martinsburg Shops'),['NPS: The Baltimore and Ohio Railroad Martinsburg Shops','https://www.nps.gov/places/the-baltimore-and-ohio-railroad-martinsburg-shops.htm']],
  brick='?',hours='?'),

N('ashbys-fort-fort-ashby','Fort Ashby (Ashby\'s Fort Museum)','Fort Ashby','wv','fort','standing',39.505278,-78.765833,'site','open','drive','','1755',
  'On October 26, 1755, Colonel George Washington ordered a stockade and fort built on the east side of Patterson Creek; it was finished about six weeks later and held by Captain John Ashby\'s rangers. Its one real fight came in 1756, when Lieutenant Robert Rutherford\'s rangers were beaten by a French and Indian party. It is on the National Register (1970) and is owned by the Friends of Ashby\'s Fort, who run it as a museum and have dug the site.',
  'A museum on the fort site (Wikipedia); a Wikimedia Commons photograph shows it as a log building with a marker in front. The Friends plan to rebuild the southwest bastion and the south wall with its gate to the plan found in their digs (museum\'s page). What survives of the 1755 work was not checked in any source opened; interior not checked.',
  'One of Washington\'s frontier forts, still being dug.',
  'Owned and run by the Friends of Ashby\'s Fort. Wikipedia gives Friday to Sunday, March to November, and special events; the museum\'s own page said in November 2026 that it is closed for the season and reopens March 5, 2027. Admission charged (members free). The pin is the Register list point; the building was not made out on the aerial. Parking not checked.',
  [W('Fort Ashby'),['Ashby\'s Fort Museum','https://www.fortashby.org/']],
  brick='no',hours='Friday to Sunday, March to November (times not checked); reopens March 5, 2027'),

N('indian-mound-cemetery-romney','Indian Mound Cemetery','Romney','wv','burial','standing',39.34259,-78.76585,'site','public','walk','','1860',
  'A cemetery on a bluff above the South Branch of the Potomac, laid out after 1860 on land given by David Gibson, around a small burial mound probably built by Hopewell people between about 500 and 1000 AD. Gibson gave the mound on condition it never be disturbed, and it has never been dug. The cemetery also holds the site of Fort Pearsall, a Confederate memorial, the Parsons Bell Tower and graves moved from Romney\'s Old Presbyterian Cemetery. Its first plan set a lower plot apart for African American burials; that became the separate Mount Pisgah Benevolence Cemetery.',
  'The Romney Indian Mound, about 7 feet high and 15 feet across with pines on it, the largest mound left in the Eastern Panhandle (Wikipedia). Also the Confederate monument, the bell tower and old graves, including two West Virginia governors (Wikipedia). Keep off the mound.',
  'A mound nobody has ever been allowed to dig.',
  'Owned and kept by the Indian Mound Cemetery Association, Inc. (Wikipedia), a private cemetery open as cemeteries usually are. Beside US 50 (the Northwestern Turnpike) on the edge of Romney. Cemetery hours and rules not checked: go in daylight and keep to the drives.',
  [W('Indian Mound Cemetery')],
  brick='?'),

N('mansion-house-point-pleasant','Mansion House, Tu-Endie-Wei State Park','Point Pleasant','wv','hotel','standing',38.83937,-82.14128,'exact','open','walk','','1796',
  'A tavern of squared logs built in 1796 by Walter Newman on part of the ground of the Battle of Point Pleasant, fought on October 10, 1774 between Virginia militia and Shawnee forces under Cornstalk. It is called the oldest known building in the Kanawha valley and the first hewn-log house in the county; it served as an inn, a house and a place of entertainment. It stands in Tu-Endie-Wei State Park, at the point where the Kanawha meets the Ohio, beside the battle monument, and the Colonel Charles Lewis chapter of the DAR runs it as a museum.',
  'A two-and-a-half-storey log house 32 by 24 feet, the logs chinked with mud and grass and dovetailed at the corners, with a stone chimney and a later brick cap (SAH Archipedia). It was one of the first West Virginia buildings recorded by the Historic American Buildings Survey. Interior not checked beyond the DAR page\'s photograph caption.',
  'A tavern raised on a battlefield twenty-two years after the battle.',
  WVSP+'The park is open year-round, at #1 Main Street (park page, read November 22, 2026). The DAR chapter opens the Mansion House seasonally (Wikipedia); its days and times were not on any page read.',
  [W('Tu-Endie-Wei State Park'),['WV State Parks: Tu-Endie-Wei','https://wvstateparks.com/park/tu-endie-wei-state-park/'],['WV DAR: Colonel Charles Lewis chapter','https://wvdar.org/ColonelCharlesLewis'],['SAH Archipedia: Mansion House','https://sah-archipedia.org/node/22624']],
  brick='?',hours='?'),

N('carnifex-ferry-battlefield','Carnifex Ferry Battlefield and the Patterson House','Summersville','wv','fort','standing',38.20666,-80.9397,'area','open','walk','','1861',
  'On September 10, 1861 Union troops attacked the Confederates dug in on the rim of the Gauley River canyon here; the Confederates failed to regain control of the Kanawha Valley, and the way to West Virginia statehood stayed open (WV Tourism). The 156-acre park, one of the oldest state parks in the country, keeps the Patterson House as a museum. It is on the National Register (1974).',
  'The Patterson House Museum (spelled Patteson in some sources), three overlooks of the Gauley River and trails over the battle ground (Wikipedia, WV Tourism). A re-enactment is held on a weekend after Labor Day (Wikipedia). What the house is built of and its interior were not checked.',
  'A farmhouse caught between two armies on a canyon rim.',
  WVSP+'1194 Carnifex Ferry Road, Summersville (park page, read November 22, 2026). The park is seasonal (WV Tourism). The pin is the park as OpenStreetMap maps it; the house itself was not placed.',
  [W('Carnifex Ferry Battlefield State Park'),['WV State Parks: Carnifex Ferry','https://wvstateparks.com/park/carnifex-ferry-battlefield-state-park/'],['WV Tourism: Carnifex Ferry Battlefield State Park','https://wvtourism.com/company/carnifex-ferry-battlefield-state-park']],
  th=[38.20721,-80.93907],thn='Parking off Old Ferry Road, Carnifex Ferry Battlefield State Park',brick='?',hours='Patterson House Museum, in season: Saturday, Sunday and holidays 10 a.m. to 5 p.m.'),

N('droop-mountain-battlefield','Droop Mountain Battlefield','Hillsboro','wv','fort','standing',38.11208,-80.26935,'area','public','walk','','1863',
  'The last major Civil War battle in West Virginia, fought on November 6, 1863, when Union troops under William W. Averell beat John Echols\'s Confederates and ended serious Confederate efforts to hold the state. A Union veteran of the battle, John D. Sutton, pushed for a park as a member of the House of Delegates; dedicated on July 4, 1928, it was West Virginia\'s first state park. The Civilian Conservation Corps made it into a park in the 1930s. On the National Register (1970).',
  'A lookout tower over the Greenbrier valley, the Droop Mountain Museum with battle relics, Confederate graves, a log cabin and trails (Wikipedia). When the tower and cabin were built was not checked.',
  'The state\'s first park, on its last big battlefield.',
  WVSP+'683 Droop Park Road, Hillsboro, on US 219 about 15 miles south of Marlinton (park page and Wikipedia, read November 22, 2026). Park and museum hours not checked. The pin is the park as OpenStreetMap maps it.',
  [W('Droop Mountain Battlefield State Park'),['WV State Parks: Droop Mountain','https://wvstateparks.com/park/droop-mountain-battlefield-state-park/'],['WV Tourism: Droop Mountain Battlefield','https://wvtourism.com/company/droop-mountain-battlefield-state-park']],
  th=[38.11538,-80.26913],thn='Park lot on Droop Mountain State Park Road',brick='?'),

N('bramwell-historic-district','Bramwell Historic District','Bramwell','wv','town','standing',37.32389,-81.30972,'area','view','walk','','1889–1920s',
  'The small coalfield town of Bramwell, whose business centre and houses mostly date from before the 1920s. The district holds 65 contributing buildings, among them the town hall (about 1889), the Bank of Bramwell (about 1893), the Masonic Hall (1893–1894), Bramwell Presbyterian Church (1902), the former Holy Trinity Episcopal Church (about 1895), the Bryant Building with its old soda fountain (about 1910), and big houses such as the Cooper House with its indoor pool (1910). On the National Register (1983).',
  'Walk the streets for the bank, the town hall, the Masonic Hall, the churches and the large houses (Wikipedia). A Wikimedia Commons photograph of Main Street shows a row of red brick commercial buildings; the Bank of Bramwell is stone. Which of them open to visitors was not checked; interiors not checked.',
  'A coal town of big houses and a bank.',
  'Town streets; the houses are private. Look from the street. The pin is the district point from Wikipedia. Parking not checked.',
  [W('Bramwell Historic District')],
  brick='some'),

N('matewan-historic-district','Matewan Historic District','Matewan','wv','town','standing',37.6225,-82.16528,'site','public','walk','','1893–1920',
  'The town centre of Matewan on the Tug Fork, a coal company town where on May 19, 1920 a standoff between police chief Sid Hatfield and Baldwin–Felts detectives sent to evict striking miners ended in a shootout that killed ten men: seven detectives, two miners and the mayor. It drove miners into the union and led on to the Battle of Blair Mountain in 1921. The street plan is little changed since then; the Urias Hotel, the detectives\' headquarters, is gone. A National Historic Landmark (1997).',
  'A row of early 20th-century commercial buildings between Mate Street and Main Street, most standing in 1920, with the railroad beside them (Wikipedia). The West Virginia Mine Wars Museum, 112 Mate Street, tells the story; its first home, an old hardware store across the street, still bears bullet holes from 1920 (Mine Wars Museum; WV Public Broadcasting).',
  'A shootout that started a mine war.',
  'Town streets, public ways open any time. The Mine Wars Museum, privately run, is open Tuesday to Saturday 10 a.m. to 5 p.m., admission $5 (museum\'s visit page, read November 22, 2026). Parking not checked.',
  [W('Matewan Historic District'),['West Virginia Mine Wars Museum: visit','https://www.wvminewars.com/visit'],['WV Public Broadcasting: Mine Wars Museum reopens','https://wvpublic.org/story/wvpb-news/reopening-of-mine-wars-museum-includes-uncovered-history/']],
  brick='?',hours='Mine Wars Museum Tuesday to Saturday 10 a.m. to 5 p.m.; $5'),

N('graceland-elkins','Graceland (Henry Gassaway Davis mansion)','Elkins','wv','hotel','standing',38.93065,-79.84876,'exact','open','drive','','1893',
  'The summer home of Senator Henry Gassaway Davis, coal and railroad magnate, finished in 1893 on a 360-acre estate. The West Virginia Presbyterian Educational Fund bought it in 1941 and gave the house and grounds to Davis & Elkins College in 1945. It is on the National Register and part of the Davis and Elkins Historic District, a National Historic Landmark, and is now an inn, restaurant and conference centre.',
  'A Norman French style house of native sandstone and timber, stone to the top of the second floor and wood-shingled above, with a four-storey octagonal stone tower at the southwest corner rising to an open belvedere under a tall pyramid roof (college page). Interior not checked.',
  'A senator\'s summer castle, now an inn.',
  'Owned by Davis & Elkins College and run as an inn and restaurant (college page and Wikipedia, read November 22, 2026). Restaurant and tour hours not checked.',
  [W('Graceland (Elkins, West Virginia)'),['Davis & Elkins College: Graceland','https://www.dewv.edu/facility/graceland/']],
  brick='no',hours='?'),

N('arthurdale-new-deal-homestead','Arthurdale (New Deal homestead community)','Arthurdale','wv','town','standing',39.49506,-79.81570,'site','open','drive','','1933',
  'A planned community built in 1933 for unemployed miners and farmers by the Subsistence Homesteads Division, with Eleanor Roosevelt closely involved. The aim was self-sufficiency; Wikipedia says the experiment failed through a clash of ideas. The historic district is on the National Register (1989), and Arthurdale Heritage keeps the Administration Building and a homestead house as a museum.',
  'The Administration Building, which once held the government offices and now holds most of the museum, and house E-15, furnished as in the 1930s (Arthurdale Heritage). Many of the homestead houses are private homes.',
  'Eleanor Roosevelt\'s experiment in a mining county.',
  'Arthurdale Heritage, a nonprofit, 18 Q Road. Guided tours of about an hour at 10 a.m., 11:30 a.m., 1 p.m. and 2:30 p.m., starting at the Craft Shop (Arthurdale Heritage visit page, read November 22, 2026). Parking not checked.',
  [W('Arthurdale, West Virginia'),['Arthurdale Heritage: visit','https://arthurdaleheritage.org/visit']],
  brick='?',hours='May to October Tuesday to Saturday, November to April Tuesday to Friday, 10 a.m. to 4 p.m.; tours 10, 11:30, 1 and 2:30'),

N('jacksons-mill-weston','Jackson\'s Mill','Weston','wv','industry','standing',39.0961,-80.4664,'site','public','drive','','1809',
  'Edward Jackson built a sawmill and grist mill on the West Fork River in 1809; his son Cummins Jackson ran it, and the orphaned Thomas Jonathan Jackson, later the Confederate general Stonewall Jackson, grew up here from 1830. The heirs gave the property to the state in 1921, and it is now WVU Jackson\'s Mill, a state 4-H camp and West Virginia University campus. The mill is on the National Register (1972).',
  'A three-storey wood-frame mill with weatherboards and a wood-shingle roof; inside, much original woodwork and machinery, large cog wheels, and an original millstone and feed hopper on the second floor (Wikipedia). Around it in the Historic Area: the McWhorter Cabin of 1793, the oldest building there, moved in 1927; the Mary Conrad Cabin, moved in 1994; Blaker\'s Mill, a barn and a blacksmith shop (WVU page).',
  'A frontier mill where a future general grew up.',
  'West Virginia University (WVU Jackson\'s Mill). When the Historic Area\'s buildings are open was not checked; the WVU page lists walking tours and history programmes. The pin is the Register list point.',
  [W('Jackson\'s Mill'),['WVU Jackson\'s Mill: Historic Area','https://jacksonsmill.wvu.edu/facilities/historic-area']],
  brick='no'),

N('lee-cabin-lost-river','Lighthorse Harry Lee Cabin, Lost River State Park','Mathias','wv','landmark','standing',38.89472,-78.92361,'area','open','drive','','about 1800–1820',
  'A summer house on land granted to Henry "Light Horse Harry" Lee III after the Revolution. Wikipedia\'s park article dates it to about 1800 and says Lee built it; the cabin\'s own article says it was probably built around 1820 by his son Charles Carter Lee. It stayed in the family until 1879, and the state bought it in the 1930s for Lost River State Park, which the Civilian Conservation Corps built. The state runs it as a museum; it is on the National Register (1974), and the park\'s New Deal buildings are listed too.',
  'The cabin museum (Wikipedia); what it is built of and its interior were not checked.',
  'A Lee family summer house in the hills.',
  WVSP+'321 Park Drive, Mathias (park page, read November 22, 2026). Museum days and times were not on any page read. The pin is the Wikipedia point, in woods; the cabin was not made out on the aerial.',
  [W('Lighthorse Harry Lee Cabin'),W('Lost River State Park'),['WV State Parks: Lost River','https://wvstateparks.com/park/lost-river-state-park/']],
  conf='mixed',brick='?',hours='?'),

N('glen-ferris-inn','Glen Ferris Inn','Glen Ferris','wv','hotel','standing',38.15025,-81.21472,'exact','open','drive','','1815–1848',
  'An inn above Kanawha Falls, known also as Stockton\'s Inn or Tavern and the Hawkins Hotel. Wikipedia says it may date from 1815 and its Register listing gives 1848; the inn itself says it has served guests since 1839. It was a stagecoach stop, a Union quartermaster\'s depot in the Civil War, and later housed managers and workers of the local works and hydroelectric plant. On the National Register (1991); it reopened under new owners in 2018.',
  'A T-shaped brick building: a three-storey painted-brick house and a two-storey red brick wing 140 by 40 feet, with a wraparound porch on 13 stuccoed brick columns (Wikipedia). The restaurant looks over the river and the falls (inn\'s page).',
  'A stagecoach inn above a waterfall.',
  'Privately owned inn and restaurant on US 60 (the Midland Trail). Restaurant hours were not on the page read.',
  [W('Glen Ferris Inn'),['The Historic Glen Ferris Inn','https://www.glenferrisinn.com/']],
  conf='mixed',brick='yes',hours='?'),

N('sites-homestead-seneca-rocks','Sites Homestead (Wayside Inn), Seneca Rocks','Seneca Rocks','wv','landmark','standing',38.83592,-79.37337,'exact','open','walk','','1839',
  'A log house built about 1839 by Jacob Sites below Seneca Rocks, enlarged with a frame addition in the 1870s and kept by the family until the Forest Service bought it in 1968. Used for years as a storage shed, it was restored in the 1980s and served as the visitor centre after the old one burned in 1992. On the National Register (1993); it is part of the Seneca Rocks Discovery Center site in the Monongahela National Forest.',
  'A log I-house with a frame addition (Wikipedia). On summer Saturdays the Forest Service holds pioneer days here (Forest Service page). Interior not checked.',
  'A log inn under the most climbed rock in the East.',
  'US Forest Service, Monongahela National Forest (Spruce Knob–Seneca Rocks National Recreation Area). The Discovery Center is at 13 Roy Gap Road, with the main lot off US 33; the picnic area and trails are open 6 a.m. to 10 p.m. (Forest Service page, read November 22, 2026).',
  [W('Sites Homestead'),['USFS: Seneca Rocks Discovery Center','https://www.fs.usda.gov/r09/monongahela/recreation/seneca-rocks-discovery-center'],['USFS: Sites Homestead','https://www.fs.usda.gov/r09/monongahela/recreation/sites-homestead']],
  brick='no',hours='Wayside Inn Saturday and Sunday 11 a.m. to 4 p.m.; Discovery Center Thursday to Monday 9:30 a.m. to 5 p.m.'),

N('camden-park-huntington','Camden Park','Huntington','wv','amuse','standing',38.3975,-82.53056,'site','open','drive','trolleyparks,amusements','1903',
  'Opened in 1903 as a picnic ground by the Camden Interstate Railway, where trolley riders between Huntington, Ceredo, Kenova, Ashland and Coal Grove changed lines, and named for Senator Johnson N. Camden. A carousel came about 1903 and a roller coaster about 1912. Eustace Via bought it in 1916; the Boylin family runs it now. It is called one of only thirteen trolley parks still open in the US, and West Virginia\'s only amusement park.',
  'The Big Dipper, a wooden roller coaster opened in 1958, and old rides such as the carousel, the Whip and a Pretzel dark ride (Wikipedia). In the middle of the park is the Camden Park Mound, an Adena burial mound, third largest in West Virginia, grown over with trees (Wikipedia). Keep off the mound.',
  'A trolley park with a 2,000-year-old mound in the middle.',
  'Privately owned amusement park, admission charged. Wikipedia says it usually opens four days a week from late May to early August, with fewer days in late August and some dates in September and October. The park\'s own site refused the request when this was written, so days and times were not checked.',
  [W('Camden Park (amusement park)'),W('Camden Park Mound')],
  brick='?',hours='?'),

N('kimball-world-war-memorial','World War Memorial, Kimball','Kimball','wv','civic','standing',37.42521,-81.50633,'exact','view','drive','','1928',
  'Dedicated on February 11, 1928, the first memorial in the United States to African American veterans, built for the 1,500 Black men of McDowell County who served in the First World War after veterans petitioned the county commission; the architect was Hassel T. Hicks. It held a meeting room, library and the first African American Legion post, and Cab Calloway played here. A fire gutted it in 1991; listed on the National Register as a ruin in 1993, it was restored for $1.6 million and reopened in 2006.',
  'A Classical Revival memorial building of stone, terra cotta and brick with four columns on a hill above the town; inside, the exhibit "Forgotten Legacy: Soldiers of the Coalfields" (Wikipedia). Interior not checked.',
  'The first memorial to Black veterans in the country.',
  'Owned by McDowell County, which built it (Wikipedia); used for tours, meetings and events. No page giving visiting times was read: look from outside unless it is open.',
  [W('World War Memorial (Kimball, West Virginia)')],
  brick='?'),
]

PIN_NOTES={
 'grave-creek-mound':'OpenStreetMap point for the mound.',
 'bo-martinsburg-shops-roundhouse':'OpenStreetMap point for the Roundhouse event centre.',
 'ashbys-fort-fort-ashby':'Register list point (Wikipedia NRHP list for Mineral County).',
 'indian-mound-cemetery-romney':'Wikipedia article point.',
 'mansion-house-point-pleasant':'OpenStreetMap building mapped as the Mansion House.',
 'carnifex-ferry-battlefield':'OpenStreetMap point for the state park, in the picnic grounds on the aerial; the house was not placed.',
 'droop-mountain-battlefield':'OpenStreetMap point for the state park, in woods beside a trail on the aerial; the tower and museum were not placed.',
 'bramwell-historic-district':'Wikipedia point for the district.',
 'matewan-historic-district':'Wikipedia point for the district.',
 'graceland-elkins':'OpenStreetMap building mapped as Graceland Inn.',
 'arthurdale-new-deal-homestead':'Address lookup (ArcGIS) of Arthurdale Heritage, 18 Q Road; the Register list point for the district fell on a house.',
 'jacksons-mill-weston':'Register list point for the mill.',
 'lee-cabin-lost-river':'Wikipedia point for the cabin; on the aerial it is in woods and no building shows. OpenStreetMap maps a building named Lee House about 200 m northwest (38.89571, -78.92544), not confirmed as the cabin.',
 'glen-ferris-inn':'OpenStreetMap point for the inn.',
 'sites-homestead-seneca-rocks':'OpenStreetMap point mapped as Sites Homestead.',
 'camden-park-huntington':'Wikipedia point for the park.',
 'kimball-world-war-memorial':'OpenStreetMap point for the memorial.',
}
