# November 19, 2026: Philadelphia & southeast Pennsylvania (region pae, drawn at random by tools/choose.py), second pass:
# Delaware County (none of it was on the map) and the Brandywine side of southern Chester County. New Sweden on the
# Delaware shore, the oldest Quaker and English buildings of Penn's colony, the Brandywine battlefield, a 1704 grist mill
# still grinding, and Mason and Dixon's stone.
# Facts come from the linked sources only. Wikipedia articles were read as raw text (tools/wiki_raw.py); HMdb, the PHMC
# Brandywine page, the DCNR Ridley Creek pages, Natural Lands' ChesLen page, Visit Delco, Birmingham Friends, Kennett
# Friends and Primitive Hall's own site were read with tools/page.py. No National Register form was read. The Chadds Ford
# Historical Society, Newlin Grist Mill and Thomas Massey House sites refused the tool (403 or reset) and their archived
# copies could not be opened unattended, so their hours are "not checked".
# Where sources disagree the text gives both; where a source is silent it says "not checked".
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
HMDB_PRINTZ=L('HMdb: Governor Printz Park marker (PHMC, 1948)','https://www.hmdb.org/m.asp?m=268428')
PHMC_BW=L('PHMC: Brandywine Battlefield Park (hours and fees)','https://www.pa.gov/agencies/phmc/historic-sites-and-museums/military-history-trail/brandywine')
DELCO_NEWLIN=L('Visit Delco: Newlin Grist Mill','https://visitdelcopa.com/newlin-grist-mill')
DELCO_PUSEY=L('Visit Delco: Caleb Pusey House & Landingford Plantation','https://visitdelcopa.com/things-to-do/history-museums/caleb-pusey-house-landingford-plantation')
CFHS=L('Chadds Ford Historical Society: Our Houses (not read: refused the tool)','https://www.chaddsfordhistory.org/about-us/our-houses/')
BFM=L('Birmingham Friends Meeting','https://www.birminghamfriends.org/')
KFM=L('Kennett Friends Meeting','https://www.kennettfriends.org')
PH=L('Primitive Hall Foundation','https://www.primitivehall.org/')
NL_CHESLEN=L('Natural Lands: ChesLen Preserve (hours, lots, Star Gazers\' Stone)','https://natlands.org/cheslen-preserve')
DCNR_RC=L('DCNR: Ridley Creek State Park (hours)','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/ridley-creek-state-park')
DCNR_RCH=L('DCNR: History of Ridley Creek State Park','https://www.pa.gov/agencies/dcnr/recreation/where-to-go/state-parks/find-a-park/ridley-creek-state-park/history')
PLACES=[
# ---- New Sweden on the Delaware ----
N('printzhof-essington','The Printzhof, Governor Printz Park','Essington','pae','town','traces',39.86106,-75.30315,'site','public','walk','','1643–',
  'In 1643 Johan Printz, governor of New Sweden, moved his capital from Fort Christina (now Wilmington) to Tinicum Island and built his house and headquarters here, with Fort Gothenburg beside it. Fire swept the settlement two years later and the Printzhof was rebuilt as a two-storey log house with timber and window glass sent from Sweden. Printz went home in 1653 and the Dutch took the colony in 1655; his daughter Armegott stayed on and sold the estate in the 1660s and 1670s. The PHMC marker calls it the site of the first permanent settlement in what is now Pennsylvania.',
  'The stone foundations of the Printzhof, the only remains of the settlement, in Governor Printz Park by the Delaware, with the 1948 state marker on Taylor Avenue. A farmstead moved from the closed New Sweden Farmstead Museum in Bridgeton, New Jersey, was rebuilt in the park in 2019 and 2020 and dedicated in 2022.',
  'The capital of New Sweden is a few stones in a riverside park.',
  'Governor Printz Park, at Taylor Avenue and Second Street, Essington (Tinicum Township). Who runs the park and its hours were not checked; a large lot on Taylor Avenue beside it belongs to the marina (check on arrival).',
  [HMDB_PRINTZ,W('The Printzhof')],th=[39.86110,-75.30211],thn='Lot on Taylor Avenue by the marina (check on arrival)',brick='no'),
N('philadelphia-lazaretto','Philadelphia Lazaretto','Essington','pae','inst','standing',39.86075,-75.30018,'exact','view','drive','','1799–',
  'After the yellow fever epidemic of 1793 killed some 4,000 to 5,000 people in Philadelphia, the city\'s new Board of Health built this quarantine hospital in 1799 on ten acres of the Delaware shore. Every ship bound for the port had to stop here for inspection; the sick were kept in the hospital and suspect cargo in a warehouse. The state took over quarantine in 1893, and the place later served as an aviation base. It is counted the oldest surviving quarantine hospital in the United States. Saved from development by preservationists, it was bought by Tinicum Township in 2005 and refurbished as its offices.',
  'The 1799 Georgian main building of red brick, with a cupola and long porches (2009 photograph), now the township offices; the federal building survey also recorded a carriage house, gate, bargemen\'s house, kitchen and bake house and seaplane hangars on the grounds (which still stand was not checked). Interior not checked.',
  'Ellis Island\'s great-grandfather, now the township offices.',
  'Tinicum Township offices, Second Street, Essington. See it from the street; office hours not checked.',
  [W('Philadelphia Lazaretto')],brick='yes'),
N('morton-homestead-prospect-park','Morton Homestead','Prospect Park','pae','landmark','standing',39.87694,-75.30583,'site','public','drive','','1654–',
  'Morton Mortenson, a Finnish settler in New Sweden, took up land here on Darby Creek in 1654. His great-grandson John Morton signed the Declaration of Independence. Parts of the present log house date from 1698, with a large addition built in the 18th century.',
  'The homestead by Darby Creek: two log wings with a stone section between them (2009 photograph). Interior not checked.',
  '',
  'Morton Homestead State Park, 100 Lincoln Avenue, Prospect Park. Who opens the house and when were not checked.',
  [W('Morton Homestead')],conf='mixed',brick='no'),
N('lower-swedish-cabin','Lower Swedish Cabin','Drexel Hill','pae','landmark','standing',39.93827,-75.30132,'site','open','drive','','1640s?–',
  'A Swedish-style log cabin on Darby Creek, perhaps one of the oldest log cabins in the United States. Wikipedia says it was likely built between 1640 and 1650 by settlers of New Sweden, but files it under 1700 by its categories: the date is not settled. The film pioneer Siegmund Lubin shot films here in the early 1900s. It was a house until 1937, passed to Upper Darby Township in 1941, and was restored with an archaeological dig in 1989.',
  'The restored log cabin with two stone chimneys (2009 photograph) on Creek Road. Interior not checked.',
  'A log cabin of the New Sweden kind, still on its creek.',
  'Owned by Upper Darby Township and cared for by the Friends of the Swedish Cabin. Wikipedia gives open Sundays 1 to 4 pm, April to October, free; the Friends\' own page did not give hours when read, so this is not checked. Creek Road, Drexel Hill; no parking is mapped near it.',
  [W('Lower Swedish Cabin'),L('Friends of the Swedish Cabin','https://swedishcabin.info/')],conf='mixed',brick='no'),
# ---- Penn's colony ----
N('caleb-pusey-house','Caleb Pusey House','Upland','pae','landmark','standing',39.85147,-75.38634,'exact','view','drive','','1683',
  'Caleb Pusey, a Quaker last maker and partner of William Penn, sailed with Penn on the Welcome in 1682 bringing prefabricated grist and saw mills, and ran the mills on Chester Creek until 1717. His stone house of 1683 is called the oldest English-built house in Pennsylvania and the only house Penn is known to have visited. The Friends of the Caleb Pusey House have owned it since about 1960 and restored it as a museum.',
  'The 1683 stone house, its chimney and the top of its east gable red brick (2023 photograph), with bricks set here and there in the walls where stones were lost and a line in the brickwork of the east wall that shows the change of roof; the outline of an early cave dwelling is marked with a low stone wall. The Landingford Plantation grounds sit beside the first proprietary mill site. Interior not checked.',
  'The one house William Penn is known to have visited.',
  '15 Race Street, Upland. Run by the Friends of the Caleb Pusey House; opening hours not checked (the borough\'s page refused the tool). See it from the street otherwise.',
  [W('Caleb Pusey House'),DELCO_PUSEY],brick='some'),
N('chester-courthouse-1724','1724 Chester Courthouse','Chester','pae','civic','standing',39.8478,-75.3599,'site','view','drive','','1724',
  'Built in 1724 as the Chester County courthouse, it served Delaware County from 1789 to 1850 and was then Chester\'s city hall; Wikipedia calls it the oldest public building still standing in the United States. A mason of Lower Chichester, William Hewes, laid the stone. The court room was kept in use, with one trial a year, until 1967. The PHMC owns it and leased it to Delaware County in 2021 for 99 years.',
  'A 2½-storey German Colonial courthouse with 2-foot walls, hewn stone on the south and east and rubble on the others, two front doors (one for men, one for women), a 1744 three-sided bay and a cupola whose London-cast bell of 1729 came back in 1920. Inside: the stone-floored court room with its low wooden rail. A Law Day mock trial is held there each May. When it is open otherwise was not checked.',
  'The oldest public building still standing in the country, and it held court until 1967.',
  'Avenue of the States, Chester. Managed by Delaware County Council and the county Historical Commission. See it from the street; opening hours not checked.',
  [W('1724 Chester Courthouse')],brick='no'),
N('thomas-massey-house','Thomas Massey House','Broomall','pae','landmark','standing',39.96528,-75.35139,'site','open','drive','','1696–',
  'Thomas Massey came from Cheshire as an indentured servant in 1683 and built the brick part of this house in 1696, as an addition to an earlier wooden one. His son Mordecai added stone in the 1730s, a stone kitchen came in the early 19th century and a room over it about 1860. The family kept it until 1925; it was saved from demolition in 1964 and given to Marple Township, and the architect John Milner restored it, uncovering a walk-in fireplace and beehive oven.',
  'The 1696 brick section with its later stone additions, furnished with 17th- and 18th-century pieces, some of them the house\'s own (cabinetry, the walk-in fireplace, a beehive oven). A state marker of 1986.',
  '',
  'Owned by Marple Township since 1964 (Wikipedia), on Lawrence Road near Sproul Road, Broomall. Wikipedia gives tours on Sundays 1 to 4 pm, April to October; the house\'s own site refused the tool, so this is not checked.',
  [W('Thomas Massey House')],conf='mixed',brick='some'),
N('chichester-friends-meetinghouse','Chichester Friends Meetinghouse','Boothwyn','pae','worship','standing',39.83639,-75.43139,'site','view','drive','','1688, rebuilt 1769',
  'Quakers met here from 1682 and built a 24-foot square meetinghouse about 1688 on land sold "only for the use of the people of God, called Quakers". It burned in January 1769 and the present 33-by-38-foot building replaced it that year. British foraging parties after the Battle of Brandywine left bullet holes in its doors. The two meetings that used it after the 1827 split were laid down in 1880 and 1914; since then it has been used only on special occasions.',
  'The 1769 meetinghouse, never given heat, plumbing or electricity, with bullet holes in the doors and carved graffiti inside; a caretaker\'s house of 1703 and a barn of 1783 beside it, and a burial ground. Opened only on occasions: when was not checked.',
  'A Quaker meetinghouse never wired, plumbed or heated.',
  '611 Meetinghouse Road, Upper Chichester Township. See it from the road and the grounds\' edge; it is opened only for special occasions.',
  [W('Chichester Friends Meetinghouse')],brick='no'),
# ---- Chester Creek and Ridley Creek ----
N('newlin-grist-mill','Newlin Grist Mill','Glen Mills','pae','industry','standing',39.89028,-75.50611,'exact','open','walk','','1704–1941',
  'Nathaniel and Mary Newlin built this water-powered grist mill on the West Branch of Chester Creek in 1704, with its dam and half-mile race; it ground commercially until 1941. E. Mortimer Newlin bought and restored it in 1958 and gave it to the Nicholas Newlin Foundation as a park. Water still turns the mill, and corn meal ground there is sold on site.',
  'The fieldstone mill, built into the hillside with a datestone "Nathan\'l Mary Newlin 1704" and a hurst frame inside that carries the machinery clear of the walls; the 1739 stone miller\'s house with its nine fireplaces and original floors, woodwork and hardware; the warehouse, a 1710 springhouse moved here and the race, among 150 acres of woods. Mill tours carry a fee; the trails and picnic ground are free.',
  'A mill that has been grinding corn on the same creek since 1704.',
  'Newlin Grist Mill park (Nicholas Newlin Foundation), off Baltimore Pike near Concordville. Visit Delco says mill tours run daily for a fee and the trails are free; the park\'s own page refused the tool, so hours are not checked.',
  [W('Newlin Mill Complex'),DELCO_NEWLIN,L('Newlin Grist Mill (not read: refused the tool)','https://www.newlingristmill.org/')],th=[39.89046,-75.50628],thn='Newlin Grist Mill Park lot',brick='no'),
N('sycamore-mills-ridley-creek','Sycamore Mills, Ridley Creek State Park','Upper Providence Township','pae','town','standing',39.94658,-75.42356,'area','view','walk','','1718–1901',
  'A small 18th-century mill village on Ridley Creek. A water mill called Providence Mill began grinding corn here in 1718; a plaster mill was added late in the 18th century and replaced by a rolling and slitting mill by 1812, when the place became Bishop\'s Mills. The mills ran until 1901, when fire damaged them. The village came into Ridley Creek State Park, opened in 1972.',
  'The mill dam on Ridley Creek and the village round it: the miller\'s house, the office, the library and several workers\' cottages, all lived in as private houses. What is left of the mill itself was not checked.',
  '',
  'Ridley Creek State Park (DCNR), open every day sunrise to sunset. Sycamore Mills Road through the village is a trail; the houses are private homes: look from the road. Park lot on Sycamore Mills Road.',
  [W('Ridley Creek State Park'),DCNR_RCH,DCNR_RC],th=[39.94550,-75.42169],thn='Ridley Creek State Park lot, Sycamore Mills Road',brick='?'),
# ---- The Brandywine ----
N('brandywine-battlefield-park','Brandywine Battlefield Park','Chadds Ford','pae','fort','standing',39.87528,-75.57528,'area','public','walk','','1777',
  'On September 11, 1777 the British beat Washington at the Brandywine and opened the road to Philadelphia. The 52-acre state park keeps the ground where the Continentals camped in the two days before. The Gideon Gilpin house, a Quaker farmer\'s, was Lafayette\'s quarters and he was brought back to it wounded; the Benjamin Ring house is believed to have been Washington\'s headquarters. Wikipedia says both houses are restored to their 1777 look and open, and also that the Ring house was destroyed by a fire set off by local youths in the 1930s: whether today\'s is a rebuilding was not checked. The Friends of Brandywine Battlefield have run it with Chadds Ford Township since the state nearly closed it in 2009.',
  'The visitor center, the Gilpin and Ring houses and the encampment ground. Interiors not checked.',
  'Lafayette was wounded here at nineteen and carried back to a Quaker\'s farmhouse.',
  'Brandywine Battlefield Park (PHMC, run with the Friends of Brandywine Battlefield), Baltimore Pike, Chadds Ford. The PHMC page gives self-guided grounds Tuesday to Thursday 10 to 4 and the visitor center Friday and Saturday 10 to 4; fees for the houses (active military free). Lot inside the park off Baltimore Pike.',
  [PHMC_BW,W('Brandywine Battlefield')],conf='mixed',th=[39.87448,-75.57595],thn='Visitor center lot, Brandywine Battlefield Park',brick='?'),
N('john-chads-house','John Chads House','Chadds Ford','pae','landmark','standing',39.87472,-75.59194,'site','view','drive','','about 1713–1727',
  'Built between about 1713 and 1727, probably by John Wyeth Jr., whose initials J.W. Jr. are carved on the front, for John Chads, who ran a ferry over the Brandywine from 1731 and gave Chadds Ford its name. It is a bank house, set into a hillside, and is little changed. In the battle of 1777 his widow Elizabeth stayed in it while the armies fired across the creek, watching from the attic windows. The architect John Milner restored it and the springhouse, which was a school from 1837 to 1844, and they opened as a museum in 1971.',
  'The fieldstone bank house with a red brick chimney (2009 photograph) and the springhouse, owned by the Chadds Ford Historical Society. Interior not checked.',
  '',
  'Chadds Ford Historical Society, on Creek Road (PA 100) just north of Baltimore Pike. House tours: the society\'s pages refused the tool, so hours are not checked. The society\'s barn visitor center is beside it on Creek Road.',
  [W('John Chads House'),CFHS],brick='some'),
N('barns-brinton-house','Barns-Brinton House','Chadds Ford','pae','hotel','standing',39.87375,-75.62569,'site','view','drive','','1714',
  'William Barns built this brick house in 1714 and kept it as a tavern from 1722 until he died in 1731. James Brinton owned it when Knyphausen\'s Hessians marched past to the Battle of Brandywine in 1777, and his family kept it until 1859. The Chadds Ford Historical Society bought and restored it in 1969.',
  'The 1714 brick tavern house on Baltimore Pike. Interior not checked.',
  '',
  'Chadds Ford Historical Society, 630 Baltimore Pike (US 1), Pennsbury Township. Tour hours not checked (the society\'s pages refused the tool). No lot is mapped: park only where the museum allows.',
  [W('Barns-Brinton House'),CFHS],brick='yes'),
N('birmingham-friends-meetinghouse','Birmingham Friends Meetinghouse','Birmingham Township','pae','worship','standing',39.90587,-75.59401,'exact','open','drive','','1763',
  'Quakers met here from about 1690 and built a meetinghouse of red cedar logs in 1718; the present stone one dates from 1763 and was enlarged in 1819, when the octagonal school beside it was built. On the afternoon of September 11, 1777 the fighting at Brandywine swept round it: the Americans held the burying ground\'s stone wall, the house was a hospital first for Americans and then for British officers, and the dead of both armies were buried together in the graveyard.',
  'The 1763 stone meetinghouse, the 1819 octagonal schoolhouse, and the walled burial ground with the common grave of British and American soldiers, a 1915 marker and a 1922 plaque on the line of defence. Interior not checked.',
  'The dead of both armies share one grave inside a Quaker wall.',
  '1245 Birmingham Road, Birmingham Township, owned by Birmingham Friends Meeting. A working meeting: worship Sundays 10 to 11:15 am, open to all. See the burial ground and the wall from the road at other times.',
  [W('Birmingham Friends Meetinghouse'),BFM],brick='no'),
N('old-kennett-meetinghouse','Old Kennett Meetinghouse','Kennett Township','pae','worship','standing',39.87111,-75.64833,'site','view','drive','','1710',
  'Built in 1710 on land deeded from William Penn to Ezekiel Harlan. The first shots of the Battle of the Brandywine were fired in its graveyard on the morning of September 11, 1777, and soldiers killed that afternoon lie in the adjoining Old Kennett Cemetery. In the 19th century it was a Hicksite meeting where Lucretia Mott, William Lloyd Garrison, Sojourner Truth, Susan B. Anthony and Harriet Tubman were among the visitors.',
  'The 1710 meetinghouse, its walls whitewashed (2009 photograph), and its cemetery on Baltimore Pike. Interior not checked.',
  'The battle of the Brandywine began in this graveyard.',
  'Kept by Kennett Friends Meeting (Kennett Square), who meet here on the last Sunday of June, July and August. The hour is given in two ways by Wikipedia (11 am in one paragraph, 9 am in another) and not by the meeting\'s page: not checked. See it from the road at other times. No lot is mapped near it.',
  [W('Old Kennett Meetinghouse'),KFM],conf='mixed',brick='no'),
N('primitive-hall','Primitive Hall','West Marlborough Township','pae','landmark','standing',39.87583,-75.83389,'site','ask','drive','','1738',
  'Joseph Pennock, a Philadelphia merchant and long-serving assemblyman, built this brick house in 1738 on land his grandfather bought from Penn. It is two standard Philadelphia townhouse plans set side by side with a brick-floored centre hall between them. Pennock\'s descendants lived here until 1960 and then gave it to a foundation that restored it. The foundations of a house of about 1710 are nearby.',
  'The 1738 brick house, with much of its own furniture: a settle bench that folds out into a bed and the great table Joseph Pennock bought from the old Chester courthouse, still in the centre hall. Iron bars on a cellar window suggest it held prisoners waiting to go to Chester.',
  '',
  'Primitive Hall Foundation, West Marlborough Township. The house and grounds are toured by appointment and at events (the foundation\'s page): do not call uninvited. No lot is mapped.',
  [W('Primitive Hall'),PH],brick='yes'),
N('star-gazers-stone','Star Gazers\' Stone','Embreeville','pae','landmark','marker',39.93921,-75.73243,'exact','public','walk','','1764',
  'In January 1764 Charles Mason and Jeremiah Dixon set up a temporary observatory here, about 31 miles west of Philadelphia\'s southernmost point, to find its latitude exactly; the Maryland line was then laid 15 miles south of that point. The stone marks their meridian north of the observatory. They worked from the Harlan house, about 700 feet south, through much of the four and a half years of the survey, often spending the winters there. The Chester County Historical Society set the stone in concrete in 1908 with a low wall and a plaque.',
  'The stone in its 1908 walled enclosure with the plaque, in a small plot that is now part of ChesLen Preserve. The c. 1724 Harlan house nearby is private.',
  'Where Mason and Dixon watched the stars to fix the line.',
  'ChesLen Preserve (Natural Lands): free, open Friday to Wednesday dawn to dusk, closed Thursdays. The stone is reached from a parking area at the north end of the preserve, which was built in 2013. Deer management runs in the preserve from mid-September to late January.',
  [W('Star Gazers\' Stone'),NL_CHESLEN],brick='no'),
]
PIN_NOTES={
 'printzhof-essington':'The Wikipedia coordinate, in Governor Printz Park on the leaf-off aerial (lawn and paths by the river); the foundations themselves were not picked out. The trailhead point is the large lot on Taylor Avenue next to the park, which the federal map puts in Riverfront Marina.',
 'philadelphia-lazaretto':'Moved 39 m with pix.py from the Wikipedia coordinate (on the lawn) onto the long main building with its central cupola block, as the leaf-off aerial shows it.',
 'morton-homestead-prospect-park':'The Wikipedia coordinate, inside Morton Homestead State Park on the aerial, 35 m from the OpenStreetMap park point and the ArcGIS point for 100 Lincoln Avenue; a small building is at the ring edge, kept as site.',
 'lower-swedish-cabin':'The Wikipedia coordinate, on a clearing with small buildings by Darby Creek in Addingham Park on the leaf-off aerial; which roof is the cabin was not certain, kept as site.',
 'caleb-pusey-house':'The ArcGIS PointAddress for 15 Race Street, Upland (score 100), on a small building at the north edge of the woods on the aerial; the Wikipedia coordinate was 70 m off in the trees.',
 'chester-courthouse-1724':'The Wikipedia coordinate, among the buildings of the block on Avenue of the States on the aerial; which roof is the courthouse was not settled, kept as site.',
 'thomas-massey-house':'The Wikipedia coordinate, on the loop drive by a house at the end of it on the aerial; kept as site.',
 'chichester-friends-meetinghouse':'The Wikipedia coordinate, on a building in a tree-shaded lot on the aerial. The ArcGIS point for 611 Meetinghouse Road is 115 m north on another building; which is the meetinghouse was not settled, kept as site.',
 'newlin-grist-mill':'The Wikipedia coordinate, on the red-roofed mill building on the aerial; the trailhead point is the park lot OpenStreetMap maps beside it.',
 'sycamore-mills-ridley-creek':'The Sycamore Mills Dam as mapped in OpenStreetMap, on Ridley Creek under trees on the aerial; the village houses are just east. The trailhead point is the park lot OpenStreetMap maps on Sycamore Mills Road, which is under trees on the aerial (check on arrival).',
 'brandywine-battlefield-park':'The Wikipedia coordinate for the park, in woods inside the park on the aerial; area only. The trailhead point was moved with pix.py onto the lot beside the visitor center building that the aerial shows.',
 'john-chads-house':"The Wikipedia coordinate, on the lawn west of Creek Road on the aerial, with small buildings round it; the long building to the northeast is the society's barn visitor center (OpenStreetMap). Kept as site.",
 'barns-brinton-house':'The museum as mapped in OpenStreetMap at 630 Baltimore Pike, on the house beside the road on the aerial.',
 'birmingham-friends-meetinghouse':'The ArcGIS PointAddress for 1245 Birmingham Road (score 100), 3 m from the OpenStreetMap meeting point, on the long building beside the walled burial ground on the aerial; the Wikipedia coordinate was 90 m southwest in trees.',
 'old-kennett-meetinghouse':'The Wikipedia coordinate, at the small building between the drive and Baltimore Pike on the aerial; kept as site.',
 'primitive-hall':'The Wikipedia coordinate, beside the large house at the road on the aerial.',
 'star-gazers-stone':'The monument as mapped in OpenStreetMap, 2 m from the Wikipedia coordinate, at the edge of the woods on the aerial (the stone itself is too small to see).',
}
BATCH={'key':'pae_kqwd','label':'Delaware County and the Brandywine, Pennsylvania','added':'2026-11-19 13:04'}
