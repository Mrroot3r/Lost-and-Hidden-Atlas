# November 20, 2026: Virginia, a second scatter across the state (it had sixteen places, from the first scatter, va_wulp,
# and Belle Isle). Region claimed with tools/choose.py --thinnest (va). Fourteen places from the Northern Neck and Cape
# Henry to Winchester, the Blue Ridge, Lynchburg, Blacksburg and Abingdon: two burned or broken colonial mansions, a
# canal of George Washington's, an iron furnace, colonial churches, house museums and a theatre in a church of 1833.
# Sources read in this session: Wikipedia articles (tools/wiki_raw.py), the Virginia Department of Historic Resources'
# register page (Catherine Furnace), and the pages of the bodies that run each place (tools/page.py): the Fairfield
# Foundation (Rosewell), the Menokin Foundation, the National Park Service (Great Falls Park, Chatham), Preservation
# Virginia (Cape Henry Lighthouse), the St. John's Church Foundation, the Foundation for Historic Christ Church, Virginia
# Wildlife Resources' birding-trail page (Catherine Furnace parking and day-use hours), Virginia Tech's Shenandoah Valley
# research station (McCormick Farm), Historic Smithfield, the Lynchburg Museum System (Point of Honor), Pohick Church,
# the Winchester-Frederick County Historical Society (Abram's Delight) and Barter Theatre. Interiors were not visited by
# any source opened unless the entry says so. Nothing was checked on the ground. Red brick: from what the sources say the
# place is built of, or from the Wikipedia photograph opened with tools/brick.py look.
from data_b import N
from data_ma import W
BATCH={'key':'va_gfto','label':'Virginia: a second scatter across the state','added':'2026-11-20 13:12'}

PLACES=[
N('rosewell-ruins-gloucester','Rosewell ruins (the Page family mansion)','Gloucester','va','landmark','ruins',37.32778,-76.57639,'site','open','walk','burned','1725–1916',
  'Mann Page I began Rosewell in 1725 above the York River, a three-storey Flemish-bond brick house that the historian Thomas Waterman called the largest and finest American house of the colonial period. It was the Page family seat for more than a hundred years, and Thomas Jefferson was often there in the time of Governor John Page. A fire in 1916 gutted it, and it has been left as a ruin; the Fairfield Foundation, which runs it, is now stabilising the brickwork.',
  'Tall standing walls of brick with their window openings, on foundations three and a half feet thick (Wikipedia). The Fairfield Foundation says much of the 18th-century brickwork still stands, that preservation masonry can be watched in progress, and that a timber-frame Remembrance structure built in 2025 honours the hundreds of enslaved people who lived there. A visitor centre has exhibits and a shop. No roof or interior survives.',
  'The largest house in colonial America, roofless since 1916.',
  'Run by the Fairfield Foundation. Begin at the visitor centre before walking to the ruin. Admission is free for the 2026 season; the grounds are always open for looking at the outside of the ruin and the signs (rosewell.org, read November 20, 2026). Parking was not checked: no lot is mapped near the ruin.',
  [W('Rosewell (plantation)'),['Fairfield Foundation: Rosewell','https://www.rosewell.org/']],
  brick='yes',hours='April 3 to November 1: Friday and Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m.; grounds always open to view the outside'),

N('menokin-warsaw','Menokin (Francis Lightfoot Lee\'s house)','Warsaw','va','landmark','ruins',38.00842,-76.80368,'site','open','walk','','c. 1769',
  'The house of Francis Lightfoot Lee, a signer of the Declaration of Independence, built from about 1769 as a wedding gift from his wife\'s father, John Tayloe II of Mount Airy, on Cat Point Creek. It changed hands many times, stood mostly empty and crumbling from about 1935, and partly collapsed; its panelling and woodwork were taken out for safe keeping in 1968. The Menokin Foundation took it over in 1995 and is filling the missing walls and roof with structural glass instead of rebuilding them (the Glass House Project).',
  'A partly collapsed two-storey stone house, with about 80 percent of its original fabric surviving: stone, brick and mortar, queen posts and dragon beams, and framing assemblies (Wikipedia). The original interior woodwork came back to Menokin in 2005 and is shown in the foundation\'s visitor centre. The 500 acres hold terraced garden remains, woodland trails along the creek, and the 2018 Remembrance Structure honouring the enslaved people of Menokin. The guided tour goes into the ruin; the audio tour does not.',
  'A Founding Father\'s ruin being finished in glass.',
  'Owned and run by the Menokin Foundation, reached from Business Route 3 in Warsaw by Menokin Road (4.5 miles) and a signed gravel road to the visitor centre. Guided tour $15, audio tour $5, children 12 and under free; reservations encouraged, not required. The grounds and trails are open seven days a week (menokin.org, read November 20, 2026). Parking at the visitor centre was not checked on the aerial.',
  [W('Menokin'),['Menokin Foundation: plan your visit','https://www.menokin.org/plan-your-visit']],
  brick='some',hours='Guided tours Tuesday to Friday 10 a.m. to 4 p.m. (last 3 p.m.); June to October Wednesday to Sunday; grounds and trails every day'),

N('patowmack-canal-great-falls','Patowmack Canal and Matildaville ruins, Great Falls','Great Falls','va','canal','ruins',38.98944,-77.24861,'area','public','walk','canal','1785–1828',
  'George Washington presided over the Patowmack Company, formed in 1785 to make the Potomac navigable toward the Ohio country. Its hardest work was the skirting canal round Great Falls, opened in the 1790s: five locks of red sandstone from the Seneca quarry, the last three in a channel blasted through the rock cliffs in one of the earliest uses of black powder in the country. Boats carrying flour, whiskey, tobacco and iron locked through until the company failed and the canal closed in 1828. Matildaville, the canal town named by Light Horse Harry Lee, had a superintendent\'s house, mills, a foundry, an inn and barracks.',
  'The cut canal bed and the walls of the locks in the rock gorge at Great Falls Park; only a few fragile remains of Matildaville can be seen (Wikipedia). Both are protected by the Archaeological Resources Protection Act: look, do not dig or take.',
  'Washington\'s own canal, blasted through the cliffs at Great Falls.',
  'Great Falls Park, a unit of the National Park Service (George Washington Memorial Parkway). Entrance pass required: standard pass $10 to $20, annual and America the Beautiful passes accepted, sold on Recreation.gov or at the park (NPS fees page, read November 20, 2026). Parking is in the park\'s lots off Old Dominion Drive; the Matildaville Trail is named on the park\'s hours page. Stay back from the cliff edges and out of the river.',
  [W('Patowmack Canal'),['NPS: Great Falls Park hours','https://www.nps.gov/grfa/planyourvisit/hours.htm'],['NPS: Great Falls Park fees','https://www.nps.gov/grfa/planyourvisit/fees.htm']],
  th=[38.99350,-77.25432],thn='Great Falls Park lot (Old Carriage Road)',brick='no',hours='Every day 7 a.m. to 30 minutes after sunset'),

N('old-cape-henry-lighthouse','Old Cape Henry Lighthouse','Virginia Beach','va','light','standing',36.9258,-76.00812,'exact','open','walk','','1792',
  'The first lighthouse authorised by the United States government and the first federal construction project under the Constitution, built by John McComb Jr. of Aquia and brown sandstone and finished in November 1792 at the south entrance to the Chesapeake Bay. It was darkened in 1813 against the British blockade and again by Confederate forces in the Civil War. Worries about its stability led to a second tower nearby, built 1879 to 1881; the old tower passed to the Association for the Preservation of Virginia Antiquities (now Preservation Virginia) in 1930.',
  'An octagonal sandstone tower, which Benjamin Latrobe in 1798 described as rising 90 feet to the light, 26 feet across at the base. A brick lining and an iron stairway were added inside; visitors climb at least 79 stairs to the observation platform. Preservation Virginia repaired it in 2025 with Aquia stone. The newer iron tower stands nearby but is not part of the visit (Wikipedia; Preservation Virginia).',
  'The first lighthouse the new nation built.',
  'Inside Joint Expeditionary Base Little Creek-Fort Story, a Navy base; run by Preservation Virginia. Timed tickets bought ahead: $22, seniors, AAA and military $20, students $8. Everyone 18 and over must file the base security form (SECNAV 5512) after buying, and everyone over 16 must show a REAL ID or passport; visitors park and ride a shuttle from the base gate, and the driver needs registration and proof of insurance. Closed Thanksgiving, December 24 and 25, and December 28 to January 1 (Preservation Virginia page, read November 20, 2026).',
  [W('Cape Henry Lighthouses'),['Preservation Virginia: Cape Henry Lighthouse','https://preservationvirginia.org/historic-sites/cape-henry-lighthouse/']],
  brick='no',hours='Tuesday to Sunday 10 a.m. to 5 p.m., by timed ticket; closed some holidays'),

N('st-johns-church-richmond','St. John\'s Church, Church Hill','Richmond','va','worship','standing',37.53139,-77.41972,'exact','open','walk','cemeteries','1741',
  'The oldest church in Richmond, built in 1741 by Colonel Richard Randolph; the Church Hill district is named for it. In March 1775 the Second Virginia Convention met here and Patrick Henry ended his speech with "give me liberty or give me death". Benedict Arnold quartered British troops in it when Richmond was occupied in January 1781. It still has a congregation and is shown to visitors by the St. John\'s Church Foundation.',
  'Guided tours inside the church tell the story of the convention and the speech; the speech is reenacted on select dates. The churchyard holds George Wythe, a signer of the Declaration, and Elizabeth Arnold Poe, Edgar Allan Poe\'s mother (Wikipedia). Graveyard tours are given on some days. What original fabric survives inside was not checked.',
  'Where "liberty or death" was spoken.',
  'Historic St. John\'s Church, 2401 East Broad Street. Tours $15, 12 and under $12; reenactments $12, youth $9; daily tours go on sale 30 days ahead; the gates are open when the site is open. Street parking on all four sides of the block, accessible parking on 24th Street (foundation page, read November 20, 2026; the Friday hours were not on the lines read).',
  [W('St. John\'s Episcopal Church (Richmond, Virginia)'),['Historic St. John\'s Church','https://www.historicstjohnschurch.org/home-1']],
  brick='no',hours='Thursday 11:30 a.m. to 4 p.m., Saturday 9:30 a.m. to 4 p.m., Sunday 12:30 to 4 p.m.'),

N('christ-church-lancaster-va','Historic Christ Church (Robert Carter\'s church)','Weems','va','worship','standing',37.68063,-76.42322,'exact','open','drive','cemeteries','1732–1735',
  'A brick church built in 1732 to 1735 by Robert "King" Carter on about the foundations of a wooden church of 1670 paid for by his father John Carter, who is buried in the yard with four of his five wives. It lost money and members after the Anglican church was disestablished in 1786 and fell into disrepair in the 19th century, when vandals took bricks from its walls. Restoration began in 1927; the Foundation for Historic Christ Church owns it and runs it as a museum.',
  'One of the best-preserved colonial churches in the South: the only colonial Virginia church that keeps its original high-backed box pews, and one of two with its original three-decker wineglass pulpit, in the middle of the building (Wikipedia). The Carter tombs are in the churchyard. A museum and a herb garden are on the site. The church is seen on a guided tour.',
  'A planter\'s church with its box pews and pulpit as built.',
  'Owned by the Foundation for Historic Christ Church, 420 Christ Church Road, Weems. Admission $10 for adults; tours by appointment December to March and outside the set hours; last tour 3:30 p.m. The churchyard and grounds are open every day all year. The visitor lot is on the left on Route 646 just before the church (foundation\'s directions and hours page, read November 20, 2026).',
  [W('Christ Church (Lancaster County, Virginia)'),['Historic Christ Church: directions and hours','https://www.christchurch1735.org/visit/directions-hours']],
  th=[37.6797,-76.42286],thn='Visitor lot on Route 646',brick='yes',hours='April and November: Friday, Saturday 10 a.m. to 4 p.m., Sunday 1 to 4; May to October also Monday, Thursday; grounds daily'),

N('catherine-furnace-page-county','Catherine Furnace','Newport','va','industry','ruins',38.55778,-78.63583,'site','public','walk','','1836',
  'A stone iron furnace in the George Washington National Forest, built in the tapered square shape of its time; it made pig iron used for shells in the Mexican and Civil wars and was abandoned in 1885. The Virginia Department of Historic Resources and Wikipedia give 1836 for its building; the state\'s birding-trail page gives 1840, and says the furnace was bought in 1865 by William Milnes and worked with Big Gem as part of the Shenandoah Iron Works.',
  'A pyramid of stone 32 feet high (Wikipedia; the birding-trail page calls it 20 by 20 feet), at the meeting of Roaring Run and Cub Run, with hiking trails nearby.',
  'An iron furnace by two trout streams in the national forest.',
  'George Washington National Forest (US Forest Service), open daily sunrise to sunset; parking area on Cub Run Road (signed Katherine Furnace Road), about 0.4 mile past the end of Newport Road, State Route 685, from US 340 south of Luray (Virginia Wildlife Resources birding-trail page, read November 20, 2026). The Forest Service\'s own page for the site was not found.',
  [W('Catherine Furnace'),['Virginia DHR: Catherine Furnace','https://www.dhr.virginia.gov/historic-registers/069-0130/'],['Virginia Bird and Wildlife Trail: Catherine Furnace','https://dwr.virginia.gov/vbwt/sites/catherine-furnace-u-s-forest-service/']],
  conf='mixed',th=[38.55746,-78.63555],thn='Forest Service lot on Cub Run Road',brick='no',hours='Every day, sunrise to sunset'),

N('mccormick-farm-raphine','Cyrus McCormick Farm and workshop (Walnut Grove)','Raphine','va','industry','standing',37.931592,-79.214465,'site','open','drive','','1822',
  'The family farm where Cyrus McCormick built and tested his mechanical reaper, the machine that led to the combine harvester. Robert McCormick started the farm in 1822; it once covered 532 acres. Virginia Tech\'s agricultural research station runs it, and five acres round the old buildings are a free museum.',
  'Eight of the nine original buildings stand: the grist mill (built before 1800, which ground wheat for flour), the blacksmith shop where the reaper was made, slave quarters, the carriage house, the brick manor house of 1822, the smoke house, a schoolroom stocked with 1830s books and toys, and the housekeeper\'s quarters; the ice house was pulled down in the 1960s (Wikipedia).',
  'Where the reaper was born, mill and smithy still standing.',
  'Virginia Tech\'s Shenandoah Valley Agricultural Research and Extension Center; admission free (Wikipedia). The museum and historic buildings close on state holidays and in bad weather (research station page, read November 20, 2026). Parking was not checked: the mapped lot on McCormick Farm Circle is over a building on the aerial, so none is given.',
  [W('Cyrus McCormick Farm'),['Virginia Tech: Shenandoah Valley AREC','https://www.arec.vaes.vt.edu/arec/shenandoah-valley.html']],
  brick='some',hours='Monday to Friday 8 a.m. to noon; closed state holidays'),

N('smithfield-blacksburg','Historic Smithfield (William Preston\'s house)','Blacksburg','va','landmark','standing',37.21778,-80.43194,'exact','open','drive','','1772–1774',
  'A frontier plantation house built about 1773 to 1774 by Colonel William Preston on land first granted to his uncle James Patton, who was killed in the Draper\'s Meadow massacre of 1755. Preston, who may have written the Fincastle Resolutions, lived here through the Revolution; two governors of Virginia, James Patton Preston and John B. Floyd, were born here. It stayed a family home until it was given to the APVA in 1959, and opened to the public in 1964.',
  'Rooms furnished with 18th- and 19th-century furniture and portraits; a basement museum shows things found on the site, among them Native American artefacts (Wikipedia). Seen on a guided house tour.',
  'A frontier colonel\'s house on the edge of Virginia Tech.',
  'Run by Historic Smithfield, 1000 Merry Oak Way, Blacksburg (the old address, 1000 Smithfield Plantation Road, still works in some maps). House tour $8, seniors, military and AAA $7, students $5, ages 5 to 12 $3; last tour 2:30 p.m. (Historic Smithfield page, read November 20, 2026). Parking was not checked.',
  [W('Smithfield (Blacksburg, Virginia)'),['Historic Smithfield: directions and hours','https://www.historicsmithfield.org/directions-hours']],
  brick='some',hours='Wednesday to Saturday 10 a.m. to 3 p.m.'),

N('point-of-honor-lynchburg','Point of Honor','Lynchburg','va','landmark','standing',37.42051,-79.14394,'exact','open','walk','','1806–1815',
  'A Federal mansion on Daniel\'s Hill above the James, built from 1806 to 1815 by Dr. George Cabell, Patrick Henry\'s physician and a friend of Jefferson, on ground said to have been used for secret duels, which gave it its name. It passed through the Daniel and Langhorne families. It was restored in 1977 and opened as a city museum in 1978.',
  'A two-storey house of stuccoed brick with a three-bay centre between two octagonal-ended wings (Wikipedia). The museum shows the house, its hearth kitchen and the grounds on guided walking tours; the interior was not described by a source opened.',
  'A house named for the duels fought on its lawn.',
  'Run by the Lynchburg Museum System. Guided walking tours of the house, hearth kitchen and grounds on select Saturdays March to December and at other times by appointment with notice; adults $8, ages 6 to 17 $5. Parking lot at 109 Norwood Street, across from the Carriage House gift shop (Point of Honor page, read November 20, 2026).',
  [W('Point of Honor'),['Point of Honor: hours, admission and directions','https://pointofhonor.org/visit']],
  brick='no',hours='Guided tours on select Saturdays, March to December; other times by appointment'),

N('pohick-church-lorton','Pohick Church','Lorton','va','worship','standing',38.709,-77.19384,'exact','open','drive','cemeteries','1769–1774',
  'The parish church of George Washington and George Mason, who both sat on its vestry; the brick building was finished in 1774 to replace an earlier church at Colchester. In the winter of 1862 to 1863 Union troops stabled horses in it and stripped the inside of everything but the upper cornice, carrying off pieces of the pulpit as relics. Repairs began in 1874 and 1890, and it is again an active Episcopal parish.',
  'A two-storey brick church with a hipped roof, modillioned cornice and quoins; soldiers\' graffiti on the doorposts, quoins and walls and bullet holes in the outside walls can still be seen (Wikipedia). The inside is an early Colonial Revival restoration, not the original fittings. The church keeps the Truro Parish vestry book of 1732 and a 1761 prayer book imported by Washington. Docent tours are given on the first Saturday of the month.',
  'Washington\'s church, with Union graffiti still on the walls.',
  'Pohick Episcopal Church, 9301 Richmond Highway, Lorton. Anyone may attend the Sunday services; first-Saturday docent tours at 1 p.m. (December 5, 2026 listed); office Monday to Thursday 9 a.m. to 3 p.m. (pohick.org, read November 20, 2026). Parking was not checked on the ground; on the aerial a paved lot runs along the road beside the church.',
  [W('Pohick Church'),['Pohick Episcopal Church','https://www.pohick.org/']],
  brick='yes',hours='Sunday services 8 and 10:30 a.m.; docent tours first Saturday of the month at 1 p.m.'),

N('chatham-manor-falmouth','Chatham Manor','Fredericksburg','va','landmark','standing',38.30883,-77.45536,'site','open','walk','','1768–1771',
  'A Georgian mansion that William Fitzhugh finished in 1771 on the Rappahannock opposite Fredericksburg, the only private house said to have been visited by Washington, Jefferson, Lincoln and Eisenhower. In 1805 its enslaved workers rose against their overseer; one was killed in the attack and two died trying to escape. In the Civil War it was a Union headquarters and then a hospital, where Clara Barton and Walt Whitman helped the wounded. It was left to the National Park Service in 1975 and is the headquarters of the Fredericksburg and Spotsylvania battlefield park.',
  'By 1865 over 750 panes were broken, the walls covered in graffiti and much of the panelling burned for firewood; some of the soldiers\' pencil graffiti can still be seen (Wikipedia). The gardens and the graves of Union soldiers at their edge are on the grounds.',
  'A plantation house turned Union hospital, with soldiers\' pencil marks.',
  'National Park Service, 120 Chatham Lane. Park at the gate and walk the grounds. The main building was closed for the season when the park\'s hours page was read (November 20, 2026); restrooms 9 a.m. to 5 p.m.',
  [W('Chatham Manor'),['NPS: Fredericksburg and Spotsylvania hours','https://www.nps.gov/frsp/planyourvisit/hours.htm']],
  brick='yes',hours='Gate and grounds daily 9 a.m. to 5 p.m.; house closed for the season (November 2026)'),

N('abrams-delight-winchester','Abram\'s Delight','Winchester','va','landmark','standing',39.16917,-78.16083,'exact','open','walk','','1754',
  'The oldest house in Winchester, built in 1754 of rubble limestone for the Hollingsworth family, whose forebear Abraham Hollingsworth settled by a spring here in 1728 and called the land "a delight to behold". The family held it for almost 200 years and added a west wing about 1800. The Winchester-Frederick County Historical Society restored it over nine years and opened it as a museum in 1961.',
  'A two-storey stone house with three chimneys; the hand-dug well of Abraham\'s first cabin, a log cabin of 1780 moved here in 1967, a perennial garden and an old gristmill that is now a shop and exhibit space (Wikipedia).',
  'The town founder\'s stone house by the spring.',
  'Run by the Winchester-Frederick County Historical Society. Admission $6, seniors $5, students $3 (society page, read November 20, 2026). Parking was not checked; Jim Barnett Park\'s lot on Maple Drive is the nearest mapped one.',
  [W('Abram\'s Delight'),['Winchester-Frederick County Historical Society: Abram\'s Delight','https://www.winchesterhistory.org/abrams-delight']],
  brick='no',hours='April 1 to October 31: Monday to Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m.'),

N('barter-theatre-abingdon','Barter Theatre (the old Sinking Spring Presbyterian Church)','Abingdon','va','civic','standing',36.71084,-81.97521,'exact','open','walk','','1833',
  'Robert Porterfield opened the Barter in June 1933, in the Depression, letting people pay for a seat with farm produce: 30 cents or the same in goods. It is the longest-running professional Equity theatre in the United States. Its building was put up in 1833 as the Sinking Springs Presbyterian Church and is called the second-oldest theatre building in the country.',
  'The church building on Main Street, renovated inside in 1953 with fittings from New York\'s Empire Theatre and again in 1996, when the stage was deepened from 28 to 60 feet; the main stage seats 505 (Wikipedia). It is seen by going to a play.',
  'A theatre where you once paid in vegetables, in a church of 1833.',
  'A working theatre on Main Street in downtown Abingdon; tickets from the box office. Abingdon\'s visitor centre is open daily 9 a.m. to 5 p.m. (Barter Theatre visit page, read November 20, 2026). Performance times were not read; parking was not checked.',
  [W('Barter Theatre'),['Barter Theatre: visit','https://bartertheatre.com/visit/']],
  brick='yes',hours='?'),
]

PIN_NOTES={
 'rosewell-ruins-gloucester':'Wikipedia coordinate.',
 'menokin-warsaw':'Wikipedia coordinate.',
 'patowmack-canal-great-falls':'Wikipedia coordinate for the canal; the parking point is the mapped Great Falls Park lot (parking.py).',
 'old-cape-henry-lighthouse':'OpenStreetMap lighthouse "Old Cape Henry Lighthouse" (nom.py), 40 m from the Wikipedia coordinate (which is for both towers).',
 'st-johns-church-richmond':'Wikipedia coordinate.',
 'christ-church-lancaster-va':'OpenStreetMap place of worship at 420 Christ Church Road (nom.py); the Wikipedia coordinate fell on Route 646 about 550 m away. The visitor lot was read off the aerial with pix.py.',
 'catherine-furnace-page-county':'Wikipedia coordinate; the birding-trail page gives 38.557502, -78.635560, 40 m away. Parking is the mapped Forest Service lot (parking.py).',
 'mccormick-farm-raphine':'ArcGIS geocoder point of interest "McCormick Farm"; the Wikipedia coordinate was in an empty field about 250 m north-west. The mapped lot on McCormick Farm Circle was over a building on the aerial and is not used.',
 'smithfield-blacksburg':'Wikipedia coordinate.',
 'point-of-honor-lynchburg':'OpenStreetMap feature "Point of Honor", 109 Norwood Street (nom.py), 30 m from the Wikipedia coordinate.',
 'pohick-church-lorton':'OpenStreetMap place of worship "Pohick Episcopal Church" (nom.py); the Wikipedia coordinate was in the woods south of the churchyard. The mapped lot 100 m south-west was a paved square in the woods, not plainly a lot, and is not used.',
 'chatham-manor-falmouth':'Wikipedia coordinate, in the walled garden beside the house; the ArcGIS geocoder put 120 Chatham Lane 65 m east.',
 'abrams-delight-winchester':'Wikipedia coordinate.',
 'barter-theatre-abingdon':'OpenStreetMap theatre "Barter Theater", 127 West Main Street (nom.py); the Wikipedia coordinate was about 370 m east.',
}
