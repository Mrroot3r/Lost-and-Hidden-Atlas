# November 19, 2026: Jefferson County, West Virginia: Harpers Ferry and Bolivar, Charles Town, Halltown, Duffields,
# Shepherdstown and Shannondale. Region drawn at random by tools/choose.py (wv); the county chosen inside it.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), National Park Service pages for Harpers Ferry
# (hours, fees, trails, places), the Jefferson County Historic Landmarks Commission's cement-mill page and brochure, the
# Shannondale Springs National Register form (wvculture.org PDF, text layer), the WVDNR map of the wildlife management
# area, the Friends of Happy Retreat site, St. James parish's St. Peter tour page, Zion Episcopal's history page, Clio
# entries, historicshepherdstown.com, SAH Archipedia, ObserverWV, West Virginia Explorer and the Harpers Ferry-Bolivar
# Historic Town Foundation's blog. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'wv_gkkh','label':'West Virginia: Harpers Ferry, Charles Town and Shepherdstown','added':'2026-11-19 08:01'}

HAFE=('Harpers Ferry National Historical Park (National Park Service). The park is open every day of the year except Thanksgiving, December 25 and January 1; '
      'trails and parking lots are open from 30 minutes before sunrise to 30 minutes after sunset, and Lower Town museums from 9 a.m. An entrance pass is required in all park areas, '
      'bought at the entrance station by the visitor center (171 Shoreline Drive) or online. Parking in Lower Town is limited: the park sends visitors to the visitor center lot and its shuttle bus (NPS hours and fees pages, read November 19, 2026).')
NPSH=['NPS: Harpers Ferry hours and seasons','https://www.nps.gov/hafe/planyourvisit/hours.htm']
NPSF=['NPS: Harpers Ferry fees and passes','https://www.nps.gov/hafe/planyourvisit/fees.htm']
TOWN='Street parking and public lots in town; parking was not checked on the ground.'

PLACES=[
N('virginius-island-ruins-harpers-ferry','Virginius Island mill ruins','Harpers Ferry','wv','industry','ruins',39.32149,-77.73916,'area','public','walk','','1806–1936',
  'A twelve-acre island in the Shenandoah made by the Shenandoah Canal, dug by the Patowmack Company in 1806–1807 to carry boats past the rapids and drive machinery. Through the first half of the 1800s it held most of Harpers Ferry\'s industry outside the Armory: at different times a cotton mill, a flour mill (the longest lived), a sawmill, an iron foundry, a tannery, a rifle factory and a machine shop, with row houses for about 180 people at the 1850 peak. Floods wore it down, and after the 1936 flood the last islanders left; no building stands.',
  'Ruins of the cotton and flour mills, turbine and waterworks remains, old waterways and house foundations along the Virginius Island and Hall\'s Island trails (up to 2 miles, easy, compacted earth and gravel), with the site of John Hall\'s Rifle Works on the neighbouring island. Dogs must be on a leash.',
  'An island of factories that the river took back.',
  HAFE+' The island trails can be reached from Lower Town (Shenandoah Street) or from the River Access parking area and the Lower Town Trail from the visitor center. Open during daylight hours.',
  [W('Virginius Island, West Virginia'),['NPS: Virginius Island and Hall\'s Island Trail','https://www.nps.gov/hafe/planyourvisit/virginius-island-trail.htm'],['NPS: Virginius and Hall\'s Islands','https://www.nps.gov/places/000/virginius-and-halls-islands.htm'],NPSH,NPSF],
  th=[39.32163,-77.74321],thn='River Access parking, Harpers Ferry NHP',brick='?'),

N('john-browns-fort-harpers-ferry','John Brown\'s Fort (Armory engine house)','Harpers Ferry','wv','fort','standing',39.32304,-77.72956,'exact','public','walk','','1848',
  'The fire-engine and guard house of the federal Harpers Ferry Armory, built in 1848 and described then as one storey of brick under a slate roof. John Brown and some of his men barricaded themselves in it at the end of the raid of October 1859 until Marines broke in. It is the only Armory building left. It was sold in 1891 and taken to Chicago for the World\'s Columbian Exposition, rebuilt on the Murphy Farm outside town in 1895, moved to the Storer College campus in 1909, and brought back by the Park Service in 1968 to Lower Town, near its first site, which an obelisk marks.',
  'A small one-storey red brick building with three arched doors under fanlights, brick chimneys at the gable ends and a white cupola (Wikipedia\'s photograph). Wikipedia says the words "John Brown\'s Fort" were painted over the doors in the 1800s for visitors. Whether the inside can be entered was not checked.',
  'Moved four times, and now about where it began.',
  HAFE,
  [W('John Brown\'s Fort'),['NPS: John Brown\'s Fort','https://www.nps.gov/places/john-brown-s-fort.htm'],NPSH,NPSF],
  th=[39.32444,-77.73119],thn='Potomac Street lot, Lower Town (limited)',brick='yes'),

N('st-peters-church-harpers-ferry','St. Peter\'s Roman Catholic Church','Harpers Ferry','wv','worship','standing',39.32273,-77.7313,'exact','public','walk','','1831–1833, remodelled 1896',
  'A church on the heights above Lower Town, built in 1831 and dedicated in 1833 in an early Gothic style, and the only church in Harpers Ferry to come through the Civil War undestroyed. In 1896 the architects Thomas J. Collins and Son remodelled it completely into the stone-clad Victorian Gothic church seen now. Its congregation was largely the Irish who came to build the canal and the railroad. It is now a mission church of St. James in Charles Town.',
  'A stone-faced Gothic church with a spire, reached by the stone steps from Lower Town; the street beside it is part of the Appalachian Trail, and a short path goes on to Jefferson Rock. The NPS page praises its stained glass. Inside: St. James parish says docents usually open it to visitors on Saturdays, Sundays and federal holidays, 11 a.m. to 2 p.m., and Mass is said there on Sundays at 9:30 a.m.',
  '',
  'Owned by the Catholic parish (the NPS calls it a private location inside the park); the walk up from Lower Town is in Harpers Ferry National Historical Park. '+HAFE,
  [W('St. Peter\'s Roman Catholic Church (Harpers Ferry, West Virginia)'),['NPS: St. Peter\'s Catholic Church','https://www.nps.gov/places/000/st-peters-catholic-church.htm'],['St. James parish: St. Peter tours','https://www.stjameswv.org/st-peter---tours'],NPSH],
  th=[39.32444,-77.73119],thn='Potomac Street lot, Lower Town (limited)',brick='no'),

N('storer-college-harpers-ferry','Storer College campus, Camp Hill','Harpers Ferry','wv','civic','standing',39.32379,-77.73541,'site','public','walk','','1867–1955',
  'A historically Black college that grew from a one-room school opened in 1865 by the Rev. Nathan Brackett for freed people, chartered with money from John Storer in 1867 and closed in 1955. The government gave it four empty Armory houses on Camp Hill (Lockwood House, Brackett House, Morrell House and the first Anthony Hall) as its first campus, and it added buildings into the 1930s. The Niagara Movement, forerunner of the NAACP, held its first American meeting here in 1906. Much of the campus is now part of the national park and, as of 2021, one of the Park Service\'s training centres.',
  'Nineteenth-century houses and halls along Fillmore Street on Camp Hill, among them Lockwood House, the college\'s first building, two storeys of red brick on a stone basement with a two-level porch (Wikipedia\'s photograph), and Cook Hall, a grey stone building of 1939–1940. Which buildings can be entered was not checked; much of the campus is offices.',
  '',
  HAFE+' The campus is on Camp Hill above Lower Town, near the Hartzog Road lot.',
  [W('Storer College'),['NPS: Storer College','https://www.nps.gov/places/storer-college.htm'],NPSH],
  th=[39.32401,-77.7415],thn='Hartzog Road lot, Harpers Ferry NHP',brick='some'),

N('bo-bridge-ruins-harpers-ferry','B&O bridge piers at the Potomac crossing','Harpers Ferry','wv','rail','ruins',39.32355,-77.7273,'site','public','walk','','1836–1936',
  'The Baltimore and Ohio crossed the Potomac here from 1836–1837 on an 830-foot covered wooden bridge designed by Benjamin Latrobe II, the only railroad bridge over the river until after the Civil War; John Brown came over it at the start of his raid. It was destroyed in the war and replaced several times. Stone piers from the 1851 Bollman truss bridge stand beside the 1894 bridge; the old crossing was finally lost to the 1936 flood. Two CSX bridges, of 1894 and 1931, still carry trains.',
  'Stone piers in the river next to the working railroad bridge. The footbridge beside the railroad (the Appalachian Trail\'s crossing to Maryland) passes them.',
  '',
  HAFE+' The railroad bridges are an active CSX line: stay on the footbridge.',
  [W('B & O Railroad Potomac River Crossing'),['NPS: Baltimore & Ohio Bridge Ruins','https://www.nps.gov/places/harpers-ferry-baltimore-ohio-bridge-ruins.htm'],NPSH],
  th=[39.32444,-77.73119],thn='Potomac Street lot, Lower Town (limited)',brick='no'),

N('bolivar-heights-earthworks','Bolivar Heights earthworks','Harpers Ferry','wv','fort','traces',39.32389,-77.76113,'area','public','walk','','1862',
  'The ridge west of Harpers Ferry, which Union troops fortified with earthworks along its length. In September 1862 Stonewall Jackson\'s army took the heights and forced the surrender of the Harpers Ferry garrison, at the time the last sizable Union force south of the Potomac.',
  'A preserved trench line, cannon and signs on a 0.3-mile loop on the crest, with a 1.3-mile upper loop and a lower loop through fields toward Schoolhouse Ridge (NPS trail page).',
  '',
  HAFE+' The trail starts at the Bolivar Heights parking area at the end of Whitman Avenue, Bolivar; portable toilets there, no drinking water. Open during daylight hours.',
  [W('Bolivar Heights Battlefield'),['NPS: Bolivar Heights Trail','https://www.nps.gov/hafe/planyourvisit/bolivar-heights-trail.htm'],['NPS: Bolivar Heights','https://home.nps.gov/places/000/bolivar-heights.htm'],NPSH],
  th=[39.32389,-77.76113],thn='Bolivar Heights parking area (Prospect Avenue)',brick='no'),

N('shannondale-springs-ruins','Shannondale Springs resort ruins','Shannondale','wv','hotel','ruins',39.23053,-77.83787,'area','public','hike','','1820–1909',
  'A mineral-springs resort on the Shenandoah, begun in 1820 with ten to twelve wooden cottages and a two-storey hotel the next year. The hotel and some cottages burned in 1858; after the war brick cottages were built and a new hotel went up on the old site in 1890. That hotel burned in 1909 and was not rebuilt, and the cottages were unusable some thirty years later. The land went to The Nature Conservancy and in 1986 to the West Virginia Division of Natural Resources.',
  'The hotel foundation midway up the hill, with a ring of cottage and stable foundations and brick rubble round it; a one-storey mortared stone bath or spring house of about 1820, with stone benches inside under a vault, 50 feet northeast of the hotel ruin; and a cement fountain 50 feet south of it (1997 Register form). The springs are between the hotel and the river. The Jefferson County Historic Landmarks Commission has leased the two structures since 1996 and stabilised them.',
  'A burned spa hotel in a hunting ground.',
  'Shannondale Springs Wildlife Management Area (West Virginia DNR), reached from Charles Town by WV 9 and Mission Road. The DNR map marks hunter-access parking lots and gates; the one labelled for the WMA is on the river at the north end of this tract, but which lot is nearest the ruins was not settled. It is a public hunting area: wear orange in hunting seasons. No camping. Hours not checked.',
  [W('Shannondale Springs'),W('Shannondale Springs Wildlife Management Area'),['National Register nomination (1997)','https://wvculture.org/wp-content/uploads/2021/03/Shannondale-springs.pdf'],['WVDNR: WMA map','https://wvdnr.gov/wp-content/uploads/2022/11/ShannondaleSpringsWMA_11x17.pdf'],['West Virginia Explorer: Shannondale Springs WMA','https://wvexplorer.com/attractions/wildlife-management-areas/shannondale-springs-wildlife-management-area/']],
  conf='mixed',brick='?'),

N('potomac-mills-cement-mill-shepherdstown','Potomac Mills (Shepherdstown cement mill) ruins','Shepherdstown','wv','industry','ruins',39.42833,-77.78,'site','view','drive','','1826–1901',
  'A grist mill built in 1826 by Henry Boteler and George Reynolds about half a mile below Shepherdstown, which from 1829 burned limestone into cement for the Chesapeake and Ohio Canal, eventually in a battery of six kilns that could make enough for a lock every four days. Union troops burned it in 1861, and the fighting of September 1862 after Antietam, the Battle of Shepherdstown, was around it. Floods and droughts cut its work in the 1880s and it closed for good in 1901. The landmarks commission calls it the best preserved of ten known 19th-century cement mills on the Potomac.',
  'Stone foundations of the mill with segmental arches that carried the water, a battery of lime kilns, the outer walls of the warehouse, an office building, and the river wall of the headrace, mostly intact. The stone footing of the mill dam still makes a rapid across the river. The commission asks visitors not to climb on the ruins.',
  'The mill that made the canal\'s cement.',
  'Owned since 2011 by the Jefferson County Historic Landmarks Commission, under a conservation easement held by the Land Trust for the Eastern Panhandle; the commission plans to pass it to the National Park Service. It is about a mile east of Shepherdstown on River Road. The commission\'s brochure speaks of future visitor services; whether the grounds are open to walk was not checked, so this is marked view only from River Road.',
  [W('Potomac Mills (Shepherdstown, West Virginia)'),['JCHLC: The Shepherdstown Cement Mill','https://www.jeffersoncountyhlc.org/?p=483'],['JCHLC: Cement Mill brochure','https://www.jeffersoncountyhlc.org//wp-content/uploads/2017/10/JCHLC_CementMill_Brochure_DIGITAL.pdf'],['Clio: Potomac Mills','https://www.theclio.com/entry/121811']],
  brick='?'),

N('shepherds-mill-shepherdstown','Thomas Shepherd\'s Mill and its 40-foot wheel','Shepherdstown','wv','industry','standing',39.43333,-77.80139,'site','view','walk','','by 1739',
  'A grist mill on Town Run where it drops to the Potomac, built by the town\'s founder Thomas Shepherd and at work by April 1739, when a Frederick County court journal mentions it. It began as a two-storey stone mill with a wooden wheel; a third storey came in the late 1800s and the wooden wheel gave way to a 40-foot iron overshot wheel from the Fitz Water Wheel Company (1891 to SAH Archipedia, 1894 to Wikipedia). The wheel stood about 200 feet downstream at first and was moved beside the mill about 1900 (1905 on one local page). It ground until 1939.',
  'The huge iron overshot wheel beside a gable-roofed mill on tall stone foundations, near East High Street. One millstone is still in the building (Clio). Interior not open.',
  'One of the largest overshot wheels anywhere, in a town backyard.',
  'Privately owned and closed to the public (historicshepherdstown.com; Clio says it was sold to a private owner in 2015). See it from the street only. '+TOWN,
  [W('Shepherd\'s Mill'),['Historic Shepherdstown: Thomas Shepherd Gristmill','https://historicshepherdstown.com/2015/10/52-thomas-shepherd-gristmill/'],['SAH Archipedia: Thomas Shepherd Grist Mill','https://sah-archipedia.org/buildings/WV-01-JE31'],['Clio: Thomas Shepherd Gristmill','https://www.theclio.com/entry/41656']],
  conf='mixed',brick='?'),

N('fountain-rock-morgans-grove-park','Fountain Rock ruins and springhouse, Morgan\'s Grove Park','Shepherdstown','wv','landmark','traces',39.421,-77.82182,'area','public','walk','','1831–1864',
  'Henry Boteler built the house Fountain Rock in 1831 beside Fountain Spring, on land of the old Morgan family grant where riflemen gathered in July 1775 for the Bee-Line March to join Washington at Boston. His son Alexander Boteler, an aide to Stonewall Jackson, lost it when Union cavalry under General Hunter\'s orders burned it in 1864. The ground became a fairground from 1889 to 1931, and in 1961 the Shepherdstown Men\'s Club bought twenty acres for the park.',
  'The stone springhouse at Fountain Spring, the only structure of Fountain Rock left, and parts of the stone foundation under the 1982 pavilion on the house site, with the original stairs (Clio). A Civil War Trails marker shows how the house looked.',
  '',
  'Morgan\'s Grove Park, owned by the Shepherdstown Community Club (ObserverWV, 2019), with fields, a pavilion and a three-quarter-mile walking trail. Hours not checked.',
  [W('Morgan Grove Park'),W('Morgan\'s Grove'),['Clio: Fountain Rock/Morgan\'s Grove Park','https://theclio.com/entry/117480'],['ObserverWV: Community Club takes over Morgan\'s Grove','https://observerwv.com/shepherdstown-community-club-takes-over-morgans-grove/']],
  brick='?'),

N('duffields-depot','Duffields Depot','Duffields','wv','rail','standing',39.3627,-77.8256,'site','view','drive','','1839–1843',
  'A privately owned station that Richard Duffield built on his land for the Baltimore and Ohio between 1839 and 1843, believed to be the second-oldest surviving B&O depot. Mosby\'s rangers seized it in June 1864, and their "Greenback Raid" derailed a train just west of here that October. The B&O built its own station nearby in 1883–1884 (gone about 1942). The old depot had a stone half, the stationmaster\'s house and passenger room, and a wooden freight half.',
  'The stone half, of rough local limestone with 18-inch walls, built into the slope like a bank barn with the main floor at Melvin Road and the basement at track level, re-roofed by its preservation group in 2008. The wooden half collapsed in 2018.',
  '',
  'Owned by the non-profit Duffields Station Inc. (Wikipedia), on the north side of the tracks east of Flowing Springs Road; see it from the road. Trains still use the line: keep off the tracks. The MARC commuter lot on Flowing Springs Road is owned by the West Virginia State Rail Authority. Hours not checked.',
  [W('Duffields station')],
  th=[39.36174,-77.82762],thn='MARC Duffields station lot, Flowing Springs Road',brick='no'),

N('halltown-memorial-chapel','Halltown Memorial Chapel (Union Colored Sunday School)','Halltown','wv','worship','standing',39.3095,-77.803,'site','view','drive','','1901',
  'A Gothic Revival stone chapel built in 1901 by and for Halltown\'s African American community, many of whom built it after work, on a small lot given by Daniel B. Lucas from his Rion Hall estate, beside the Halltown Colored Free School. The non-denominational Sunday school ran until 1967 and the chapel was used for weddings and funerals afterwards. A committee restored it in 1983.',
  'Pointed-arch windows and doors, open-beam ceilings, stained glass in the sanctuary and the original pulpit (West Virginia Explorer). In 2024 it was being restored again and got pews from Harpers Ferry\'s First Zion church. The Halltown Colored Free School stands next door. Interior not open on a set schedule as far as was checked.',
  '',
  'Owned by the Halltown Memorial Chapel Association (Clio), off US 340 in Halltown. View from the road; no public hours were found. Parking not checked.',
  [W('Halltown Union Colored Sunday School'),W('Halltown Colored Free School'),['West Virginia Explorer: Halltown Union Sunday School','https://wvexplorer.com/travel/attractions/historic-sites/halltown-union-sunday-school/'],['Harpers Ferry-Bolivar Historic Town Foundation: pews for the chapel','https://historicharpersferry.org/blog/pews-from-first-zion-donated-to-halltown-memorial-chapel/'],['Clio: Halltown Colored Free School','https://theclio.com/tour/2232/45']],
  brick='no'),

N('jefferson-county-courthouse-charles-town','Jefferson County Courthouse','Charles Town','wv','civic','standing',39.28911,-77.85981,'site','view','drive','','1836–1837',
  'The court where John Brown was tried in 1859 for treason against Virginia, and where in 1922 the miners of the Battle of Blair Mountain were tried for treason against West Virginia, the reason it was made a National Historic Landmark in 2023. The first courthouse on Charles Washington\'s lot (1808) burned; the core of this one dates from 1836–1837. Shelled and stripped for metal in the Civil War, it stood empty from 1865 to 1872, then was repaired, with a rear extension designed by Mullett and a later Georgian Revival addition holding a jail and sheriff\'s offices.',
  'A red brick Georgian courthouse on a high stone base, with a pedimented Doric portico, an iron balcony and an odd square-domed clock tower, behind an iron fence (Wikipedia). Interior not checked.',
  'Two treason trials, sixty-three years apart.',
  'County building in downtown Charles Town; public hours were not checked. '+TOWN,
  [W('Jefferson County Courthouse (West Virginia)')],
  th=[39.28947,-77.86074],thn='West Liberty Street lot',brick='yes'),

N('zion-episcopal-church-charles-town','Zion Episcopal Church and churchyard','Charles Town','wv','worship','standing',39.28892,-77.85572,'exact','view','walk','','1851',
  'The town\'s Episcopal church on its highest ground, built on the site of churches of 1815 and 1847–1848 and opened on December 6, 1851. The churchyard holds over 1,500 graves, including about 70 members of the Washington family, more than anywhere but Mount Vernon (Wikipedia; the parish counts twenty born at Mount Vernon), two Revolutionary officers, some 85 to 90 Confederate soldiers, and John Yates Beall, hanged as a Confederate spy in New York.',
  'A brick Gothic Revival church with a square bell tower, decorative corbelling and pointed multi-pane windows. A Francis Scott Key poem is cut on the stone of his friend Mary Ann Morsel. Interior not checked.',
  '',
  'An active parish church at 301 East Congress Street. Whether the churchyard is open to walk at set times was not checked. '+TOWN,
  [W('Zion Episcopal Church (Charles Town, West Virginia)'),['Zion Episcopal Church: More history','https://www.zionepiscopal.net/more-history']],
  conf='mixed',brick='?'),

N('happy-retreat-charles-town','Happy Retreat (Charles Washington House)','Charles Town','wv','landmark','standing',39.28222,-77.85972,'exact','view','drive','','c. 1780',
  'The home of Charles Washington, George Washington\'s youngest brother, who moved here from Fredericksburg in 1780 and laid out Charles Town on 80 acres of his land in 1786. The two one-storey wings came first; the central block was added later and much altered. A cornerstone of the old kitchen is dated 1768, which has never been proved. Since 2006 the Friends of Happy Retreat have been restoring it as a heritage and cultural centre.',
  'A two-and-a-half-storey white-painted brick house with wings on short hyphens and stepped gables, a Doric pediment with a fanlight, an old brick smokehouse, and an octagonal wooden powder house like the one at Mount Vernon. The Friends show the exposed foundation of the quarters of the people enslaved here.',
  '',
  'Run by the Friends of Happy Retreat, in Charles Town park land round it (ownership not checked). Inside only at events: the Friends list open houses and ticketed concerts (a Christmas open house on December 6, 2026, 2 to 4 p.m.). Otherwise view from outside. Parking not checked.',
  [W('Happy Retreat'),['Friends of Happy Retreat','https://www.happyretreat.org'],['Friends of Happy Retreat: about','https://happyretreat.org/about/']],
  brick='no'),
]

PIN_NOTES={
 'virginius-island-ruins-harpers-ferry':'Wikipedia coordinate for the island; the ruins are spread along the island trails.',
 'john-browns-fort-harpers-ferry':'Wikipedia coordinate.',
 'st-peters-church-harpers-ferry':'Wikipedia coordinate.',
 'storer-college-harpers-ferry':'Wikipedia coordinate for the campus, on a building in a lawn on Camp Hill. The Storer College Place lot that parking.py listed was on a house on the aerial, and the mapped Fillmore Street lot was on a building, so the Hartzog Road lot, which the aerial shows as a long parking lot, is given.',
 'bo-bridge-ruins-harpers-ferry':'OpenStreetMap point "B&O - Harpers Ferry Bollman Bridge" (historic=ruins), found with nom.py; on the aerial it is on a stone pier in the river beside the railroad bridges.',
 'bolivar-heights-earthworks':'The Wikipedia battlefield coordinate fell among houses in Bolivar. Pinned instead on the mapped parking lot on Prospect Avenue (parking.py), inside Harpers Ferry NHP on the federal land map and beside the mapped Bolivar Heights Trail, which the NPS says starts at the end of Whitman Avenue; the trenches are along the crest from there. Pin is the trailhead, not a particular earthwork.',
 'shannondale-springs-ruins':'Wikipedia coordinate for the Register site. On the aerial it is in trees, and on the LiDAR it sits on the north bank of the river bend inside the wildlife management area; the hotel foundation, said by the Register form to be midway up the hill, was not picked out on the LiDAR, so the pin marks the area only.',
 'potomac-mills-cement-mill-shepherdstown':'Wikipedia coordinate. Trees on the aerial; the LiDAR shows walls and a long wall along the river edge beside River Road at the pin.',
 'shepherds-mill-shepherdstown':'Wikipedia coordinate.',
 'fountain-rock-morgans-grove-park':'OpenStreetMap point for Morgan\'s Grove Park (nom.py). It falls on the playing field; the 1982 pavilion on the house site and the springhouse are among the small buildings near the field and were not told apart on the aerial, so the pin marks the park.',
 'duffields-depot':'Register coordinate from the Wikipedia infobox (45 Melvin Road). On the aerial and LiDAR it is at the north edge of the tracks among trees, where a depot built into the bank would be; the building itself was not made out.',
 'halltown-memorial-chapel':'Wikipedia coordinate.',
 'jefferson-county-courthouse-charles-town':'Wikipedia coordinate, at a corner of the downtown crossroads beside a large building.',
 'zion-episcopal-church-charles-town':'Wikipedia coordinate.',
 'happy-retreat-charles-town':'Wikipedia coordinate.',
}
