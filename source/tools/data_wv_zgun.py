# November 20, 2026: West Virginia, a first scatter across the state (the state had 16 places, all but one in Jefferson
# County). Ground claimed with tools/choose.py --thinnest (wv). Places in Monongalia, Lewis, Marshall, Ohio, Barbour,
# Tucker, Pocahontas, Greenbrier, Monroe, Fayette, Raleigh, Summers, Morgan and Wood counties.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py); with tools/page.py the pages of WV State Parks
# (Coopers Rock trails, Cass), the Trans-Allegheny Lunatic Asylum, WV Penitentiary Tours, the WV Division of Culture and
# History (Independence Hall), Old Stone Presbyterian Church, the Museum of the Berkeley Springs, NPS New River Gorge
# (Visiting Kaymoor, hours and seasons, Thurmond), WV Rails to Trails (Blackwater Canyon Trail), e-WV (Exhibition Coal
# Mine) and the City of Parkersburg and Mountwood Park (Fort Boreman). Interiors were not visited by any source opened
# unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'wv_zgun','label':'West Virginia: a first scatter across the state','added':'2026-11-20 10:22'}

NERI=('New River Gorge National Park and Preserve (National Park Service). The park is open year-round; NPS hours page read November 20, 2026.')
NERIH=['NPS: New River Gorge hours and seasons','https://www.nps.gov/neri/planyourvisit/hours.htm']
WVCH=['WV Culture: West Virginia Independence Hall','https://wvculture.org/explore/wv-independence-hall/']

PLACES=[
N('henry-clay-furnace-coopers-rock','Henry Clay Iron Furnace','Cheat Neck (Coopers Rock State Forest)','wv','industry','ruins',39.64889,-79.81861,'site','public','hike','','1834–1868',
  'A stone blast furnace built between 1834 and 1836 by Leonard Lamb, the first steam-powered blast furnace in western Virginia, able to make about four tons of pig iron a day. It may have run until 1868, when all the Cheat River iron works stopped. Nothing else of the works survives; it is one of ten or more abandoned furnaces left in northern West Virginia.',
  'A dry-laid stone stack about 30 feet square and 30 feet high, shaped like a truncated pyramid, in the woods at the end of the Clay Furnace Trail (Wikipedia). Look for the arched openings at its base. No buildings remain around it.',
  'The first steam blast furnace west of the mountains, alone in the woods.',
  'Coopers Rock State Forest (West Virginia state forest). The Clay Furnace Trail (0.8 mile, mostly level with a few steep sections) runs from the furnace parking area to the furnace; the Rhododendron Trail (1 mile) reaches it from the lower picnic area near Shelter 3, and the Mont Chateau Trail goes on from it to Cheat Lake (WV State Parks trails page, read November 20, 2026). Forest hours not checked.',
  [W('Henry Clay Furnace'),['WV State Parks: Coopers Rock trails','https://wvstateparks.com/parks/coopers-rock-state-forest/trails/']],
  th=[39.65345,-79.82301],thn='Clay Furnace Trail parking, Coopers Rock State Forest',brick='no'),

N('trans-allegheny-lunatic-asylum-weston','Trans-Allegheny Lunatic Asylum (Weston State Hospital)','Weston','wv','inst','standing',39.03861,-80.47139,'site','open','drive','','1858–1994',
  'A state mental hospital begun in late 1858, at first with prison labour, and not finished until 1881; its 200-foot central clock tower was done in 1871. It took patients from 1864 until May 1994. Built for 250, it held about 2,400 in the 1950s. Empty for years after it closed, it was sold at auction in 2007 for $1.5 million and has been shown on tours since 2008 to raise money for its restoration. The main building is a National Historic Landmark (1990).',
  'A vast Gothic Revival Kirkbride building of hand-cut blue sandstone from a quarry at Mount Clare, said to be one of the largest hand-cut stone buildings in the United States, with its clock tower at the centre (Wikipedia). Inside: the short historic tour covers the first floor of the Kirkbride, where several rooms serve as a museum; the longer one all four floors, staff flats, the morgue and the operating room. Historic tours leave every hour on the hour in season (asylum\'s tour page).',
  'Built for 250 patients, it held 2,400.',
  'Privately owned; shown by tour only. The asylum\'s own site said in November 2026 that it is closed until spring 2027; tour times and prices are on its historic-tours page. Paranormal and photography tours cost more and are booked ahead.',
  [W('Trans-Allegheny Lunatic Asylum'),['Trans-Allegheny Lunatic Asylum','https://trans-alleghenylunaticasylum.com/'],['TALA: historic tours','https://trans-alleghenylunaticasylum.com/historic-tours/']],
  brick='no',hours='Closed until spring 2027 (site, November 2026); in season, historic tours leave every hour on the hour'),

N('west-virginia-penitentiary-moundsville','West Virginia Penitentiary','Moundsville','wv','inst','standing',39.91649,-80.74237,'site','open','drive','','1866–1995',
  'The state prison, begun after an 1866 act of the legislature and completed in 1876, a half-size copy of the 1858 Joliet prison in Illinois. It held more than 2,000 men by the 1920s; a new wing begun in 1929 was finished in 1959. Ninety-four men were executed here between 1899 and 1959. After the 1986 New Year\'s Day riot the state supreme court ruled its 35-square-foot cells cruel and unusual punishment, and it closed on March 27, 1995. Since 1997 it has been leased out and is shown as a museum and tour site.',
  'A castellated Gothic stone prison with turrets and battlements (Wikipedia). The day tour shows the inside, including the original "Old Sparky" electric chair, built by an inmate (Wikipedia). Regular day tours are wheelchair accessible; Monday summer tours, paranormal events and Halloween events are not (WV Pen Tours FAQ).',
  'Ninety-four executions, and a chair built by a prisoner.',
  'Run as a tour site under a lease from the state. Two small lots next to the tour entrance and across the street; street parking in front of the prison north of the lot, and lots at the south end; the operators ask visitors not to park on the residential side of Jefferson Avenue (WV Pen Tours FAQ, read November 20, 2026). Tour times not checked.',
  [W('West Virginia Penitentiary'),['WV Penitentiary Tours','https://wvpentours.com'],['WV Pen Tours: FAQ','https://wvpentours.com/faq/']],
  brick='no',hours='Day tours Tuesday to Sunday; Monday tours June to August only (times not checked)'),

N('wheeling-suspension-bridge','Wheeling Suspension Bridge','Wheeling','wv','landmark','standing',40.07028,-80.72722,'site','public','walk','','1847–1849',
  'Designed by Charles Ellet Jr. and begun in 1847, it carried the National Road across the main channel of the Ohio River to Wheeling Island and was the largest suspension bridge in the world from 1849 until 1851, with a 1,010-foot span. A windstorm wrecked its deck in May 1854 and it was rebuilt; the deck was rebuilt again in 1956. It fought two rounds of Supreme Court cases with Pennsylvania over river traffic. Called the oldest vehicular suspension bridge in the US still in use, it has been closed to cars since September 2019.',
  'Two masonry towers, the east one on the Wheeling shore and the west one on Wheeling Island, carrying the cables over a steel-grated roadway (Wikipedia). It is a National Historic Landmark.',
  'The world\'s longest span in 1849, now walkers only.',
  'In the care of the West Virginia Division of Highways, which closed it to cars and is planning its rehabilitation (Wikipedia). Closed to motor vehicles since 2019; Wikipedia says it remains open to pedestrians and cyclists while a rehabilitation plan is worked out. Street parking in downtown Wheeling, not checked.',
  [W('Wheeling Suspension Bridge')],
  brick='?'),

N('west-virginia-independence-hall-wheeling','West Virginia Independence Hall','Wheeling','wv','civic','standing',40.06417,-80.72167,'exact','open','drive','','1859–1860',
  'Built as the Wheeling Custom House, post office and federal court, opened in 1859 (the state\'s page) or built in 1860 (Wikipedia), to designs supervised by Ammi B. Young. From 1861 to 1863 it was the seat of the Restored Government of Virginia, the Union government that led to the new state; Governor Francis Pierpont had his office here. Lincoln signed the proclamation making West Virginia the 35th state on June 20, 1863. It is now a state museum.',
  'A three-storey Renaissance Revival building of load-bearing ashlar sandstone with round-arched windows and an arcaded entrance; inside, round-arched doorways and a wrought-iron frame of rolled I-beams from the Trenton Iron Works (Wikipedia). The museum holds exhibits on the state\'s history; admission is free (state\'s page).',
  'Where a state was made in the middle of a war.',
  'West Virginia Department of Arts, Culture and History. Open Tuesday to Saturday, free (state\'s page, read November 20, 2026). The 9 a.m. to 5 p.m. hours come from a Division of Culture and History notice whose year was not checked. Parking not checked.',
  [W('West Virginia Independence Hall'),WVCH,['WV Culture: notice of operating hours','https://wvculture.org/west-virginia-division-of-culture-and-history-announces-new-operating-hoursfor-the-culture-center-grave-creek-mound-independence-hall-museum-in-the-park-and-the-state-museum/']],
  brick='no',hours='Tuesday to Saturday 9 a.m. to 5 p.m.; closed Sunday and Monday; free'),

N('philippi-covered-bridge','Philippi Covered Bridge','Philippi','wv','landmark','standing',39.15306,-80.04361,'exact','public','drive','','1852',
  'Built in 1852 by Lemuel Chenoweth for the Beverly–Fairmont Turnpike over the Tygart Valley River, the oldest and longest covered bridge in West Virginia. Union and Confederate troops both used it at the Battle of Philippi on June 3, 1861. Concrete piers and deck were added in 1934. A flood in 1985 damaged it and a fire on February 2, 1989 nearly destroyed it; it was rebuilt for $1.4 million and reopened on September 16, 1991.',
  'A Burr arch truss covered bridge 285½ feet long (312 feet first) on sandstone piers built for it plus two concrete piers of 1934, with an outside walkway for people on foot (Wikipedia). It still carries a road.',
  'A covered bridge that still carries traffic, and saw the first land battle of the war.',
  'A public road bridge in Philippi (Wikipedia says it still carries traffic and was rebuilt after the 1989 fire; owner not checked). Walk across on the outside walkway. Parking not checked.',
  [W('Philippi Covered Bridge')],
  brick='no'),

N('coketon-coke-ovens-thomas','Coke ovens on the Blackwater Canyon Trail','Thomas (Coketon)','wv','industry','ruins',39.13204,-79.5161,'area','public','hike','','1887–1919',
  'The Davis Coal & Coke Company of Henry G. Davis built its company town of Coketon in the 1880s and tried two beehive coke ovens in 1887; by 1900 there were more than 600. Coke making at the mines ended when steel-making changed, and by 1919 Tucker County made no coke at all, leaving long banks of ovens idle (Wikipedia). The railroad grade through the canyon, used from 1888 to haul coal and lumber, is now the Blackwater Canyon Trail.',
  'Banks of old coke ovens along the mountainside beside the trail just outside Thomas (WV Rails to Trails). How many survive and in what state was not checked.',
  'Six hundred ovens, cold since 1919.',
  'The Blackwater Canyon Trail is in the Monongahela National Forest (WV Rails to Trails); the federal land map puts this stretch in the Blackwater Wildlife Management Area. From Thomas take WV 32 (Spruce Street) south, turn right on Douglas Road, then left onto the trail, which can be driven about a mile to the trailhead. The trail is not maintained and has washouts, rough surfaces and large sinkholes; stay on the trail (WV Rails to Trails, read November 20, 2026). Hours not checked.',
  [W('Coketon, West Virginia'),['WV Rails to Trails: Blackwater Canyon Trail','https://wvrailtrails.org/rail_trail/blackwater-canyon-trail/']],
  conf='mixed',th=[39.14451,-79.50221],thn='Blackwater Canyon rail-trail head, Thomas (OSM)',brick='?'),

N('cass-company-town','Cass company town','Cass','wv','town','standing',38.39716,-79.91489,'site','open','drive','stations','1901',
  'A lumber company town founded in 1901 by the West Virginia Pulp and Paper Company for the men who cut spruce and hemlock for its West Virginia Spruce Lumber Company. Its logging railroad climbed Back Allegheny Mountain to Whittaker Station and on to Spruce. The first tourist train left the Cass depot in 1963, and the town and railroad are now a state park running geared Shay, Heisler and Climax locomotives on 11 miles of track laid in 1901.',
  'The company town with its company store and houses, and the railroad shops where the geared locomotives are kept (Wikipedia). Town and shop tours run daily, and the park has a diorama of the town in its logging days (Wikipedia; WV State Parks). A recreated logging camp is shown at Whittaker. Interior of the company store not checked.',
  'A whole lumber town kept as it was, steam still in the shed.',
  'Cass Scenic Railroad State Park (West Virginia state parks). Guided tours of the town are offered; the northern end of the Greenbrier River Trail is at Cass (WV State Parks, read November 20, 2026). Train times and seasons not checked.',
  [W('Cass Scenic Railroad State Park'),['WV State Parks: Cass additional information','https://wvstateparks.com/parks/cass-scenic-railroad-state-park/additional-information/']],
  brick='?',hours='?'),

N('old-stone-church-lewisburg','Old Stone Presbyterian Church','Lewisburg','wv','worship','standing',37.80177,-80.44798,'exact','open','drive','','1796',
  'A Presbyterian church built in 1796 under the Rev. Benjamin Grigsby, on land given by a man who also carved the stone set over the front door. In the Civil War its pews were taken out to make room for soldiers\' cots, and after the Battle of Lewisburg a trench beside it was used to bury Confederate dead. Its congregation still worships here.',
  'Walls of native limestone gathered nearby and laid in their natural shapes, with an open cupola belfry; tradition says women and boys carried the mortar sand from the Greenbrier River four miles away (Wikipedia). Interior fabric not checked.',
  'Built in 1796 and still used every Sunday.',
  'The church (Old Stone Presbyterian Church). The sanctuary is open to the public Monday to Friday 9 a.m. to 4 p.m. from late spring to early fall, and for worship on Sundays at 11 a.m. (church\'s site, read November 20, 2026). Parking not checked.',
  [W('Old Stone Church (Lewisburg, West Virginia)'),['Old Stone Presbyterian Church','https://oldstonechurchwv.com/']],
  brick='no',hours='Sunday worship 11 a.m.; sanctuary open Monday to Friday 9 a.m. to 4 p.m., late spring to early fall'),

N('sweet-springs-resort','Sweet Springs Resort (Old Sweet Springs)','Sweet Springs','wv','hotel','standing',37.62871,-80.24157,'site','view','drive','','1792; hotel 1830–1833',
  'A mineral-spring resort developed by William Lewis after the Revolution; Washington, Madison, Lafayette and Robert E. Lee are among its recorded guests. In 1830 the first buildings were taken down and a large brick hotel in a Jeffersonian classical style was built, finished by 1833; cottages followed in 1857. With no railroad it lost out to White Sulphur Springs and Hot Springs and went bankrupt in 1930. The state bought it in 1945 for the Andrew S. Rowan Memorial Home for the aged, which closed in 1991; a nonprofit, the Sweet Springs Resort Park Foundation, is now restoring it.',
  'The long classical brick hotel and outbuildings on 8.5 acres, listed on the National Register in 1970 (Wikipedia). Interior and present condition not checked.',
  'Five presidents\' spa, then an old people\'s home, now being saved.',
  'Owned by the Sweet Springs Resort Park Foundation (Wikipedia), at 19540 Sweet Springs Valley Road. The foundation\'s site would not open from here, so whether and when visitors are shown round was not checked: look from the road unless the foundation says otherwise.',
  [W('Sweet Springs Resort'),['Sweet Springs Resort Park (foundation, not read)','https://www.sweetspringsresortpark.org/']],
  brick='?'),

N('kaymoor-mine-ruins','Kaymoor mine and coke works','Fayetteville (Kaymoor)','wv','industry','ruins',38.04778,-81.06472,'area','public','hike','','1899–1962',
  'A coal mine, processing plant and company town on the side of the New River Gorge, opened in 1899 to supply coal and coke to its owners\' blast furnaces. Houses were built from 1901; the coke works grew from 120 to 202 beehive ovens in the First World War and closed in the 1930s. Kaymoor Bottom by the river was empty by 1952 and mostly burned in 1960; Kaymoor One mine closed for good in 1962. The whole site is in the national park, and the NPS calls it one of the most intact mine complexes left in the gorge.',
  'At Kaymoor One mine, only the entrance and an old mine car (NPS). From there 821 wooden steps go down to the coal processing plant, the coke ovens and the Kaymoor Bottom town site near river level; the site is heavily overgrown (NPS; Wikipedia).',
  'Eight hundred and twenty-one steps down to a coal town.',
  NERI+' Two ways in (NPS "Visiting Kaymoor"): the Kaymoor Miners Trail from the Kaymoor Top trailhead, or the Kaymoor Trail, 2 miles one way with about 350 feet of climb, from the Wolf Creek trailhead on Fayette Station Road (1.2 miles past the Tunney Hunsaker Bridge; small parallel parking, obey the no-parking signs, not for large vehicles or trailers). Both meet at the mine entrance.',
  [W('Kay Moor, West Virginia'),['NPS: Visiting Kaymoor','https://www.nps.gov/neri/learn/historyculture/visiting-kaymoor.htm'],NERIH],
  th=[38.04602,-81.06828],thn='Lot on Kaymoor Road (OSM; taken to be Kaymoor Top)',brick='?'),

N('thurmond-coal-town','Thurmond','Thurmond','wv','town','standing',37.95712,-81.07881,'site','public','drive','stations','1888',
  'A railroad town on the C&O main line through the New River Gorge. It grew after 1892 when a crossing of Dunloup Creek was agreed with the railroad, and had banks, the 100-room Dun Glen Hotel (opened 1901, nationally known) and the Lafayette. The banks closed or left in the 1930s; in the late 1980s the National Park Service began buying property with the aim of a living-history town. The 1888 passenger depot was renovated in 1995 as a visitor centre.',
  'A strip of commercial buildings facing straight onto the tracks with no street between, and houses of three or four standard types climbing the hill behind, graded by railroad rank (Wikipedia). The NPS says the town is surprisingly untouched by modern development. The depot is a visitor centre in summer.',
  'A main street that is a railroad.',
  NERI+' Thurmond Depot Visitor Center: open Memorial Day to Labor Day 10 a.m. to 5 p.m., usually weekends in September and October, closed November to May (NPS hours page). The tracks are an active railroad: stay off them. Parking in town not checked.',
  [W('Thurmond, West Virginia'),['NPS: Thurmond','https://home.nps.gov/neri/planyourvisit/thurmond.htm'],NERIH],
  brick='?',hours='Depot visitor center Memorial Day to Labor Day 10 a.m. to 5 p.m.; usually weekends Sept.–Oct.; closed November to May'),

N('roman-bath-house-berkeley-springs','Old Roman Bath House, Berkeley Springs State Park','Berkeley Springs','wv','hotel','standing',39.62667,-78.22778,'site','open','walk','','1815',
  'The oldest public building in Berkeley Springs, built in the Federal style in 1815 on the site of a 1784 bathhouse attributed to James Rumsey, which had five bathing chambers. The warm springs, flowing at a steady 74.3 degrees from the Oriskany sandstone of Warm Springs Ridge, were famed for cures; an annual event recalls George Washington\'s visit, though the tub where he is said to have bathed was rebuilt in the 1930s. The bath house was renovated in 2019.',
  'The 1815 bath house, still in use: its baths are open to the public daily all year (Wikipedia). The Museum of the Berkeley Springs is on its second floor. Interior fabric not checked.',
  'Taking the waters where Washington did.',
  'Berkeley Springs State Park (West Virginia state parks), in the middle of town. Museum of the Berkeley Springs, upstairs: June to August daily 11 a.m. to 4 p.m. except Wednesday; May and September to November Friday to Monday 11 to 4; December to April Saturday and Sunday 11 to 4; open holiday Mondays; admission free (museum\'s page, read November 20, 2026; Wikipedia). Bath and spa hours not checked.',
  [W('Berkeley Springs State Park'),['Museum of the Berkeley Springs: hours','https://museumoftheberkeleysprings.com/directions/']],
  brick='?',hours='Museum: Jun–Aug daily 11–4 exc. Wed; May, Sep–Nov Fri–Mon 11–4; Dec–Apr Sat–Sun 11–4'),

N('beckley-exhibition-coal-mine','Beckley Exhibition Coal Mine (Phillips-Sprague Mine)','Beckley','wv','industry','standing',37.78417,-81.19361,'site','open','drive','','about 1889–1953',
  'A coal mine opened about 1889 on an older family drift mine; the Sprague Mine of Cranberry Fuel opened in 1906. The New River Company closed it in 1953 and sold the land to the City of Beckley for a park. Its passages were restored and it opened to the public on July 23, 1962, as the first historic site given over wholly to coal mining; more passages were opened in the 1970s.',
  'A ride into 1,500 feet of restored passages with 3,000 feet of vintage track, led by retired miners (Wikipedia; e-WV).',
  'Underground with a retired miner as guide.',
  'City of Beckley, in New River Park, 409 South Kanawha Street. e-WV says it is open daily April 1 to November 1 with an admission charge; the operator\'s own page was not found, so hours are not checked.',
  [W('Phillips-Sprague Mine'),['e-WV: Exhibition Coal Mine','https://wvencyclopedia.org/entries/2517']],
  brick='?',hours='?'),

N('hinton-historic-district','Hinton Historic District','Hinton','wv','town','standing',37.67481,-80.89227,'site','public','walk','stations','1870s–1926',
  'The downtown of a C&O railroad town, listed on the National Register in 1984 and enlarged in 2005. Its buildings include the C&O passenger station, the Summers County jail of the 1870s, the Wagon Wheel Restaurant building of 1876, the Hotel McCreery (about 1907), the YMCA (about 1911), the First Baptist Church (1913), a Carnegie library, several commercial blocks of 1905–1919 and the 1926 post office.',
  'Commercial buildings with stone trim, some with cast-iron shopfronts (Wikipedia), and the passenger station by the tracks. Which buildings open to visitors was not checked.',
  '',
  'Public streets of the town (City of Hinton); the buildings are privately owned and seen from the street. Parking not checked.',
  [W('Hinton Historic District')],
  brick='?'),

N('fort-boreman-parkersburg','Fort Boreman','Parkersburg','wv','fort','traces',39.26139,-81.56833,'site','public','walk','','1863',
  'A Civil War fort built in 1863 by Company A of the 11th West Virginia Volunteer Infantry on a hill above Parkersburg, to protect the B&O Railroad terminal and the river landings. It was named for Arthur I. Boreman, the state\'s first governor, a Parkersburg man.',
  'Paired trenches about four feet deep circling the hilltop in a zigzag (Wikipedia). Condition on the ground not checked.',
  '',
  'Fort Boreman Historical Park, City of Parkersburg: open year-round if weather permits (city\'s page, read November 20, 2026). A lot on Fort Boreman Drive in the park (OpenStreetMap).',
  [W('Fort Boreman'),['City of Parkersburg: Fort Boreman','https://parkersburgwv.gov/departments/parks___recreation/area_parks/fort_boreman.php'],['Mountwood Park: Fort Boreman Park','https://mountwoodpark.org/fortboremanpark/']],
  th=[39.26239,-81.56944],thn='Fort Boreman Drive lot (OSM)',brick='no',hours='Year-round, weather permitting'),
]

PIN_NOTES={
 'henry-clay-furnace-coopers-rock':'Wikipedia infobox coordinate; the aerial shows only tree cover and the LiDAR tile shows a small mound at the pin, which may be the stack; prec is site. Trailhead from tools/parking.py: the aerial shows a trail edge in the woods and the LiDAR a road loop there, not a clear lot.',
 'trans-allegheny-lunatic-asylum-weston':'Wikipedia infobox coordinate.',
 'west-virginia-penitentiary-moundsville':'Wikipedia infobox coordinate.',
 'wheeling-suspension-bridge':'Wikipedia infobox coordinate.',
 'west-virginia-independence-hall-wheeling':'Wikipedia infobox coordinate.',
 'philippi-covered-bridge':'Wikipedia infobox coordinate.',
 'coketon-coke-ovens-thomas':'OpenStreetMap feature "Historic Coke Ovens" (leads layer); it falls on the rail-trail grade on the aerial; the LiDAR tile shows a long straight bank in the hillside beside the grade at the pin, which may be the line of ovens. Trailhead from tools/parking.py, a gravel lot on the aerial.',
 'cass-company-town':'The Cass Company Store as mapped in OpenStreetMap (tools/nom.py); the Wikipedia park coordinate fell on a road junction 55 m south.',
 'old-stone-church-lewisburg':'OpenStreetMap place of worship via tools/nom.py.',
 'sweet-springs-resort':'Wikipedia infobox coordinate fell on the lawn east of the hotel; moved 51 m with tools/pix.py onto the long main building seen on the aerial.',
 'kaymoor-mine-ruins':'Wikipedia coordinate for Kay Moor; lot from tools/parking.py.',
 'thurmond-coal-town':'OpenStreetMap station building (Thurmond depot) via tools/nom.py.',
 'roman-bath-house-berkeley-springs':'Wikipedia infobox coordinate for the state park.',
 'beckley-exhibition-coal-mine':'Wikipedia infobox coordinate.',
 'hinton-historic-district':'The C&O passenger station as mapped in OpenStreetMap (tools/nom.py); the Wikipedia district coordinate fell among houses.',
 'fort-boreman-parkersburg':'Wikipedia infobox coordinate; lot from tools/parking.py.',
}
