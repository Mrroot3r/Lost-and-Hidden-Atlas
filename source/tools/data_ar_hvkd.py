# November 23, 2026: a second scatter across Arkansas, the state with the fewest places on the map when this session began
# (40). Region claimed with tools/choose.py --thinnest (ar). Ten places in the south-west (Washington), the north-west
# (Prairie Grove, Pea Ridge, Fayetteville), the Buffalo River (Rush), the Arkansas River valley (Van Buren), the middle
# (Plum Bayou), the north-east delta (Parkin) and the Texas line (Texarkana).
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), and the pages of whoever runs each place (Arkansas
# State Parks, the National Park Service), read with tools/page.py. Hours for Headquarters House and the Drennen-Scott
# house come from web search results that quote their operators' pages; those pages would not open. Nothing was checked
# on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'ar_hvkd','label':'Arkansas: a second scatter across the state','added':'2026-11-23 17:30'}

ASP='https://www.arkansasstateparks.com/parks/'

PLACES=[
N('historic-washington-state-park','Historic Washington State Park','Washington','ar','town','standing',33.773797,-93.684121,'site','open','drive','','1824–1889',
  'A frontier town on the Southwest Trail, the road from St. Louis to the Red River that took settlers toward Texas. Its post office, begun in 1820, is the oldest in continuous service west of the Mississippi (Wikipedia). It was the county seat of Hempstead County until a courthouse in Hope took over in 1939, and from 1863 to 1865 it was the Confederate capital of Arkansas. The blacksmith James Black is said to have forged the Bowie knife here (state parks page). Today it is a state park of about 54 buildings.',
  'The 1874 courthouse, now the visitor center; a blacksmith shop, a weapons museum, a print museum, an old tavern that serves meals, a church the park calls the oldest Methodist church in Arkansas, and an 1873 brick jail replaced in 1918 by a two-story jail that is now a bed and breakfast. Which buildings can be entered was not checked.',
  '',
  'Arkansas State Parks, 103 Franklin Street. Visitor center open daily, closed New Year\'s Day, Thanksgiving and Christmas Eve and Day; paid guided tours daily; the tavern restaurant serves Tuesday to Sunday (park page). Parking not checked. Admission to the grounds was not stated on the page.',
  [W('Historic Washington State Park'),['Arkansas State Parks: Historic Washington',ASP+'historic-washington-state-park']],brick='?',
  hours='Visitor center daily 8 a.m.–5 p.m.; guided tours daily 9 a.m.–3:30 p.m.; closed New Year\'s Day, Thanksgiving, Dec 24–25'),

N('borden-house-prairie-grove','Borden House, Prairie Grove Battlefield','Prairie Grove','ar','landmark','standing',35.98528,-94.30417,'site','public','drive','','1862',
  'The Borden farm lay in the thick of the Battle of Prairie Grove on December 7, 1862, one of the central points of the Confederate line, and the original house was burned the day after (Wikipedia). Archibald Borden built the present house on the original site. It is on the grounds of Prairie Grove Battlefield State Park, which the state parks page calls one of the most intact Civil War battlefields in America.',
  'A frame house of one and a half stories with a long front porch and three dormers, standing in the battlefield, which has a walking tour and a driving tour. The park museum, Hindman Hall, shows artifacts found after the battle. Whether the house itself can be entered was not checked.',
  '',
  'Arkansas State Parks, 506 East Douglas Street. The museum is free, Wednesday to Saturday 8 a.m. to 5 p.m. and Sunday 1 to 5 p.m. (closed Monday and Tuesday); the grounds are open every day from 8 a.m. to an hour after sunset. Parking not checked.',
  [W('Borden House (Prairie Grove, Arkansas)'),['Arkansas State Parks: Prairie Grove',ASP+'prairie-grove-battlefield-state-park']],brick='?'),

N('plum-bayou-mounds-scott','Plum Bayou Mounds (Toltec Mounds)','Scott','ar','curio','standing',34.64694,-92.06528,'area','open','drive','','AD 650–1050',
  'A ceremonial centre of the Plum Bayou people beside an old channel of the Arkansas River, lived in from about the 7th to the 11th century. It has 18 mounds, the tallest surviving prehistoric mounds in Arkansas, and is a National Historic Landmark. It was long called Toltec Mounds after a 19th-century guess that Toltec people built it; the state renamed it in November 2022 after talking with the Quapaw Nation.',
  'The mounds, with two walking trails (Knapp Trail and Plum Bayou Trail), a visitor center and museum, and archeologists sometimes at work on the site. Guided tours can be booked ahead.',
  '',
  'Arkansas State Parks, 490 Toltec Mounds Road, about four miles from Scott. Parking not checked.',
  [W('Plum Bayou Mounds Archeological State Park'),['Arkansas State Parks: Plum Bayou Mounds',ASP+'plum-bayou-mounds-archeological-state-park']],brick='no',
  hours='Visitor center Wed–Sat 8 a.m.–5 p.m., Sun 1–5 p.m.; closed Mon, Tue, New Year\'s Day, Thanksgiving, Dec 24–25'),

N('elkhorn-tavern-pea-ridge','Elkhorn Tavern, Pea Ridge','Garfield','ar','hotel','standing',36.45356,-94.01577,'site','open','drive','hotels','c. 1833; rebuilt after 1865',
  'A stagecoach inn, post office and meeting place that gave its name to the Battle of Elkhorn Tavern (Pea Ridge) of March 7 and 8, 1862. It was built about 1833 by William Reddick and his son-in-law Samuel Burks. In the battle it was a field hospital and for a short time General Van Dorn\'s headquarters; the Cox family sheltered in its cellar. Confederate guerrillas burned it around January 1863 and Joseph Cox rebuilt it on the old foundations after the war. The Park Service transferred it into its care in 1960 and restored it to about its wartime look. It is the only building left standing in the park of the many that stood on the battlefield (Wikipedia).',
  'A two-story white frame building with an upper porch, set in the battlefield. Its interior and opening times were not checked.',
  '',
  'National Park Service, Pea Ridge National Military Park, near Garfield. The Park Service lists auto parking, restrooms and a trailhead at the site. Hours of the building not checked.',
  [W('Elkhorn Tavern'),['NPS: Elkhorn Tavern','https://www.nps.gov/places/elkhorn-tavern.htm']],conf='mixed',brick='no',hours='?'),

N('headquarters-house-fayetteville','Headquarters House','Fayetteville','ar','landmark','standing',36.066786,-94.156917,'exact','open','walk','','1850s',
  'A Greek Revival house at 118 East Dickson Street, built by Judge Jonas Tebbetts and finished by 1853. Tebbetts was a Union man who was arrested in 1862 and later fled to Missouri; Union troops then used his abandoned house as their headquarters. A Confederate attack on April 18, 1863, aimed at the house, failed; a cannonball hit the front door, and the door and ball are in the museum. The Washington County Historical Society was given it in 1967 and runs it.',
  'Fluted porch columns, dentil eaves and a parlour fireplace in the Greek Revival style, and the door with its cannonball. Tours take about 35 minutes (the society\'s page, as quoted in a web search result).',
  '',
  'Washington County Historical Society. The society\'s page would not open; its tour times were taken from a search result that quotes it, and the older times in a 2017 newspaper guide differ, so call 479-521-2970 first. Street parking not checked.',
  [W('Headquarters House (Fayetteville, Arkansas)'),['Washington County Historical Society: tours','https://washcohistoricalsociety.org/individual_tours']],conf='mixed',brick='?',
  hours='Tours Tue–Thu noon–3 p.m.; Sat by appointment; book by phone 479-521-2970 (not confirmed on the page)'),

N('rush-historic-district-buffalo-river','Rush zinc-mining ghost town, Buffalo National River','Yellville','ar','town','ruins',36.1325,-92.57111,'area','public','walk','','1880–1931',
  'Zinc was found on Rush Mountain in 1880 and the Morning Star mine, the largest in the district, opened in 1885. Ten companies worked fourteen mines here, most busily in the boom of 1911 to 1918; a fall in zinc prices after the First World War closed most of them. The Park Service dates the district\'s importance 1885 to 1931. Wikipedia calls it the only place left in Arkansas\'s zinc country with mines, buildings and ruins together. It is listed on the National Register (1987).',
  'The Park Service lists the Taylor-Medley General Store, the Rush blacksmith shop (1925, stabilized in 1989), the Rush smelter, and several mines, tunnels and houses, many in poor repair and overgrown. A short Morning Star loop and the longer Rush Mine Level Trail go past mine entrances. Mine entrances such as the McIntosh mine are closed: stay out of any mine or tunnel and off unstable walls.',
  '',
  'National Park Service, Buffalo National River (Lower District). A small gravel lot serves the Morning Star trail (search result quoting the Park Service). The pin is the Register coordinate and was checked on the aerial; the buildings are spread along the valley.',
  [W('Rush Historic District'),['NPS: Rush Historic District','https://www.nps.gov/articles/rush-historic-district-500856.htm']],conf='mixed',brick='?'),

N('parkin-archeological-state-park','Parkin Archeological State Park','Parkin','ar','curio','standing',35.27714,-90.55741,'area','open','drive','','AD 1000–1550',
  'A 17-acre palisaded village of the Mississippian period at the meeting of the St. Francis and Tyronza rivers, a National Historic Landmark. Archeologists think it may be the Casqui of Hernando de Soto\'s 1541 march (the state parks page says "may have visited"). The ground later held a 1920s lumber and cooperage works, and a one-room school for Black children, the Northern Ohio School, still stands there.',
  'A museum with finds from the dig, a village trail, the mound ground and the old school. Which parts of the school can be entered was not checked.',
  '',
  'Arkansas State Parks, 60 Highway 184. Admission is free for the museum and self-guided visit. Parking not checked.',
  [W('Parkin Archeological State Park'),['Arkansas State Parks: Parkin',ASP+'parkin-archeological-state-park']],conf='mixed',brick='?',
  hours='Museum Wed–Sat 8 a.m.–5 p.m., Sun 1–5 p.m.; closed Mon, Tue, New Year\'s Day, Thanksgiving, Dec 24–25'),

N('drennen-scott-house-van-buren','Drennen-Scott House','Van Buren','ar','landmark','standing',35.435963,-94.359307,'exact','open','walk','','1836',
  'A one-story log house, covered in clapboards, built in 1836 by John Drennen, one of Van Buren\'s first settlers, who with his brother-in-law David Thompson laid out the town. Drennen served in the territorial and state legislatures. His descendants kept the house until the University of Arkansas at Fort Smith took it and made it a house museum. It was listed on the National Register in 1971.',
  'The log house under its clapboards, with a roof that sweeps out over a front porch across the whole front. Tours start at the visitor center on the property. Interior not checked.',
  '',
  'University of Arkansas at Fort Smith, 221 North 3rd Street. Its page would not open. A search result quoting the university gives tours April to November on Wednesday, Friday and Saturday 10 a.m. to 4 p.m.; one quoting the City of Van Buren gives March to November, 10 to 5, free. Call 479-262-2750 first. Parking not checked.',
  [W('Drennen-Scott House'),['UAFS: Drennen-Scott Historic Site','https://uafs.edu/drennen-scott/']],conf='mixed',brick='?',
  hours='Apr–Nov Wed, Fri, Sat 10 a.m.–4 p.m. (the city lists Mar–Nov, 10–5); not confirmed on its page'),

N('texarkana-union-station','Texarkana Union Station','Texarkana','ar','rail','standing',33.42,-94.0425,'area','view','walk','stations','1928–1930',
  'A railroad station that sits on the Arkansas–Texas line, with the waiting room and ticket office on the Arkansas side. Congress ordered in 1876 that the Texarkana station straddle the line. E. M. Tucker of the Missouri Pacific designed it with an overhead concourse like his rebuilt Little Rock station. Wikipedia says it was built in 1928 and opened April 17, 1930, with a dedication on May 12, 1930. It still serves Amtrak and was listed on the National Register in 1978.',
  'The long station with its concourse over the tracks. The Arkansas-side board agreed in 2023 to put $200,000 toward buying and redeveloping it. Interior and waiting-room hours not checked.',
  '',
  'A working Amtrak station: keep off the tracks. Owner and hours not checked. Parking not checked.',
  [W('Texarkana Union Station')],conf='mixed',brick='?'),

N('old-main-university-of-arkansas','Old Main, University of Arkansas','Fayetteville','ar','civic','standing',36.0687,-94.1717,'site','view','walk','','1873–1875',
  'The oldest building on the University of Arkansas campus, built 1873 to 1875 from plans bought from the University of Illinois for the Chicago architect John Mills Van Osdel; the Illinois building was demolished in 1938. The red bricks were made from clay dug on the campus and fired in kilns just west of the building. It closed in 1981 for safety, was restored in 1989 to 1991 for $10 million and rededicated in the fall of 1991.',
  'A red brick hall with its original 19th-century iron Corinthian columns still along the wings (Wikipedia). Interior and visiting times not checked.',
  '',
  'University of Arkansas campus. Public access to the inside was not checked; look from outside. Parking not checked.',
  [W('Old Main (University of Arkansas)')],brick='yes'),
]

PIN_NOTES={
 'historic-washington-state-park':'Wikipedia coordinate for the park; checked on the aerial.',
 'borden-house-prairie-grove':'Wikipedia article coordinate for the house; checked on the aerial.',
 'plum-bayou-mounds-scott':'Wikipedia coordinate for the site; checked on the aerial.',
 'elkhorn-tavern-pea-ridge':'Wikipedia article coordinate for the tavern; checked on the aerial.',
 'headquarters-house-fayetteville':'Address lookup (118 East Dickson Street); the Wikipedia coordinate lay about 140 m east in trees. Checked on the aerial.',
 'rush-historic-district-buffalo-river':'Wikipedia coordinate for the district; checked on the aerial. The pin marks the district, not one building.',
 'parkin-archeological-state-park':'Wikipedia coordinate for the park; checked on the aerial.',
 'drennen-scott-house-van-buren':'Address lookup (221 North 3rd Street); the Wikipedia coordinate was about 400 m east on a street by the tracks. Checked on the aerial.',
 'texarkana-union-station':'Wikipedia coordinate (a rounded figure); checked on the aerial.',
 'old-main-university-of-arkansas':'Wikipedia article coordinate; checked on the aerial.',
}
