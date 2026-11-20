# November 20, 2026: Providence County, Rhode Island (region riprov, drawn at random by tools/choose.py).
# The earlier Rhode Island passes took ruins and a few landmarks; this batch adds the oldest standing buildings of
# the county (three stone-enders, a 1685 farmhouse, a 1704 Quaker meeting house, a 1796 lottery-built meeting house),
# the Slater mills at Pawtucket and Slatersville, a mill-town museum, the fresco church in Woonsocket, a country
# store, a turnpike tavern, and one ruin in the Foster woods (the Ramtail factory, from the leads).
# Facts come from the linked sources only. Wikipedia was read as raw text (tools/wiki_raw.py). Hours and access come
# from the page of whoever runs each place, read with tools/page.py: the National Park Service, the Friends of
# Hearthside, the Rhode Island Historical Society, the St. Ann Arts and Cultural Center, the Pawtucket DAR chapter,
# Providence Friends Meeting, the Smith-Appleby House and the Brown & Hopkins store. Historic New England's own
# property pages answered HTTP 403 with no archived copy, so the two stone-enders it runs have hours='?' and the
# access note says which other page gave the season. The Foster facts come from the Rhode Island Historical
# Preservation Commission's statewide survey report for Foster (a PDF of about 1982, text layer read).
# Pins: the ArcGIS geocoder's point address, an OpenStreetMap feature or an HMdb or Waymarking position, as each
# pin note says; every pin was looked at on the pin check.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
NPS_H=L('National Park Service: Blackstone River Valley NHP, hours','https://www.nps.gov/blrv/planyourvisit/hours.htm')
HH=L('Friends of Hearthside: Hearthside House','https://www.hearthsidehouse.org/')
HHV=L('Friends of Hearthside: Great Road Heritage Campus and nearby sites','https://www.hearthsidehouse.org/visit-folder')
FOSTER=L('RI Historical Preservation Commission: Foster survey report (PDF)','https://preservation.ri.gov/sites/g/files/xkgbur406/files/pdfs_zips_downloads/survey_pdfs/foster.pdf')
STANN=L('St. Ann Arts and Cultural Center: tours','https://www.stannartsandculturalcenter.org/tours.html')
STANNP=L('St. Ann Arts and Cultural Center: directions and parking','https://www.stannartsandculturalcenter.org/directions--parking.html')
STANNH=L('St. Ann Arts and Cultural Center','https://www.stannartsandculturalcenter.org/')
RIM=L('Rhode Island Monthly: Inside St. Ann\'s in Woonsocket','https://www.rimonthly.com/inside-st-anns-in-woonsocket-the-sistine-chapel-of-new-england/')
PLACES=[
# ---- Pawtucket ----
N('old-slater-mill-pawtucket','Old Slater Mill and Wilkinson Mill','Pawtucket','riprov','industry','standing',41.87752,-71.38291,'site','open','drive','','1793–',
  'The first water-powered cotton-spinning mill in America to use Arkwright\'s system, built for Moses Brown by Samuel Slater, who finished the machines, dam, wheel and mill in 1793. It was enlarged from 1801 to 1872, spun cotton until 1895 and was used for other industry until 1923. In 1824 young women workers here led the first factory strike in the country. Restored to its 1835 look from 1923, it opened as a museum in 1955, was the first property put on the National Register in 1966, and was bought by the National Park Service in 2021.',
  'The wooden mill of 1793 with exhibits and an introductory film, the stone Wilkinson Mill of 1810-11 and the Sylvanus Brown House of 1758 (moved here in the 1960s), the dam on the Blackstone and panels round five acres of grounds on both banks. Wikipedia shows a spinning mule inside the mill. The Park Service says the Wilkinson Mill and the Brown House are closed to the public for now; rangers give tours of Old Slater Mill.',
  'Where the American factory began, and where its first strike happened.',
  'Blackstone River Valley National Historical Park (National Park Service), 67 Roosevelt Avenue. The grounds are open dawn to dusk every day; the mill and its visitor station keep the seasons in the hours row, from the Park Service hours page. Tours are cut short or cancelled when the heat index is above 87 degrees. A mapped lot on Leather Avenue, on park land, is about 90 m north-east.',
  [W('Slater Mill'),NPS_H],th=[41.87812,-71.38224],thn='Leather Avenue lot (park land)',brick='no',
  hours='Grounds dawn to dusk daily. Mill: May 17 to Oct 31 Thu to Sun 10 to 4; Apr 24 to May 16 and Nov 1 to 28 Fri and Sat; tours 10:30, 12:30, 2:30'),
N('daggett-house-pawtucket','Daggett House','Pawtucket','riprov','landmark','standing',41.87203,-71.34405,'exact','open','drive','','1685–',
  'The oldest house standing in Pawtucket, built about 1685 for John Daggett Jr. near the site of his father\'s house, which was burned in King Philip\'s War. Eight generations of Daggetts farmed here until 1870; the city bought the run-down farm in 1894 and it became Slater Park. The Daughters of the American Revolution restored the house from 1902 and opened it as a museum in 1905.',
  'A large white clapboard farmhouse with red-brick chimneys (Wikipedia\'s 2009 photograph) in Slater Park. The Pawtucket DAR chapter shows nine furnished rooms with its collection of Revolutionary War, Civil War and 18th- and 19th-century things. From outside any day; inside only at the openings below.',
  '',
  'In Slater Memorial Park (City of Pawtucket); the house is kept by the Pawtucket Chapter, Daughters of the American Revolution. The chapter\'s page says it opens for tours in September during the Arts in the Park festival and in December during the park\'s Winter Wonderland, and by appointment from April to December, by email through its page. Mapped park lots on the Ten Mile River Greenway are about 70 m away.',
  [W('Daggett House'),L('Pawtucket Chapter NSDAR: The Daggett House','https://ridar.org/pawtucket/?p=63')],th=[41.8723,-71.3433],thn='Slater Park lot, Ten Mile River Greenway',brick='some',
  hours='September (Arts in the Park) and December (Winter Wonderland); otherwise by appointment, April to December'),
# ---- Lincoln, the Great Road ----
N('eleazer-arnold-house','Eleazer Arnold House','Lincoln','riprov','landmark','standing',41.90298,-71.41974,'exact','open','drive','','1693–',
  'A large "stone-ender" built for Eleazer Arnold in 1693 (a 2005 tree-ring survey confirmed the date), on the Great Road laid out in 1683. The type came from the west of England and was most used in northern Rhode Island; the work is credited to John Smith "the Mason" of Smithfield and his family. Given to what is now Historic New England in 1919, it was stabilised in 1920 and fully restored in 1950 to its 17th-century look. A National Historic Landmark since 1974.',
  'Two storeys of four rooms each with a lean-to, exposed fieldstone end walls, wooden side walls and a huge pilastered stone chimney end. Wikipedia says the leaded windows and the front door and its surround are 20th-century replacements. Interior not checked.',
  'The house its neighbours called "Eleazer\'s Splendid Mansion".',
  'Owned and run by Historic New England, 487 Great Road. Historic New England\'s own page answered HTTP 403 and could not be read; the Friends of Hearthside page says it is open weekends from June to October, and Wikipedia says weekends, so check before going. A mapped lot on Manchester Print Works Road is about 240 m west (not on mapped public land).',
  [W('Eleazer Arnold House'),HHV,L('Historic New England: Arnold House (page not read)','https://www.historicnewengland.org/property/arnold-house/')],brick='no',hours='?'),
N('hearthside-house-lincoln','Hearthside House','Lincoln','riprov','landmark','standing',41.90676,-71.43015,'exact','open','drive','','1810–',
  'A Federal-style fieldstone mansion with ten fireplaces, built in 1810 by Stephen Hopkins Smith, said to be paid for with lottery winnings and built to win a Providence woman who would not have him. Frederick C. Sayles bought it in 1901. It was a home until 1996, when the Town of Lincoln bought it; the volunteer Friends of Hearthside now run it. The 1908 vote to buy the land for Lincoln Woods, the state\'s first state park, was taken here.',
  'The stone house at Great Road and Breakneck Hill Road, furnished in period style, shown by costumed docents with changing exhibits. The Friends also run the Hannaway Blacksmith Shop, the Pullen\'s Corner Schoolhouse and the Moffett Mill across the road in Chase Farm Park.',
  '',
  'Town of Lincoln, run by the Friends of Hearthside, 677 Great Road. Their page says the sites do not open on a regular schedule but on the dates on their calendars; the next listed were Christmas self-guided tours on December 12, 13, 19 and 20 from 1 to 4, and evening guided tours on December 28 and 29, with tickets. Chase Farm Park has a lot on Great Road about 300 m south-east.',
  [W('Hearthside'),HH,HHV],brick='no',hours='Only on dates on the Friends of Hearthside calendar (December 2026: 12, 13, 19, 20 from 1 to 4 p.m.; 28 and 29 from 4 to 7:30 p.m.)'),
N('moffett-mill-lincoln','Moffett Mill','Lincoln','riprov','industry','standing',41.90497,-71.42522,'site','open','drive','','1812–',
  'A small wooden mill on the Moshassuck River built by George Olney in 1812, which the Friends of Hearthside and the state tourism office call a rare survivor of the first wave of Blackstone Valley industry; the state calls it probably the first machine shop in Rhode Island. Arnold Moffett Jr. bought it in 1850 and built the stone dam that still stands. It made wagons, carriages, boxes, shoelaces and farm tools and parts, closed about 1900, and was given to the Town of Lincoln in the 1980s.',
  'The Friends say the mill was left almost as it was on its last working day, with many of its original contents inside, "like a time capsule"; the stone dam of about 1850 is beside it. From the road only, except on tour days.',
  'A machine shop left as it was on its last day.',
  'Town of Lincoln, shown by the Friends of Hearthside. Their page says the mill is reached only by their shuttle van on days when Hearthside is open for tours, because the road is too busy to walk along safely; in November 2026 it was "closed for the season". Do not stop on Great Road. Start at Hearthside, 677 Great Road.',
  [HH,HHV,L('Visit Rhode Island: Moffett Mill','https://www.visitrhodeisland.com/listing/moffett-mill/7945/')],th=[41.90676,-71.43015],thn='Hearthside House (the shuttle starts here)',brick='no',
  hours='By the Friends of Hearthside shuttle on Hearthside tour days only; closed for the season in November 2026'),
N('saylesville-friends-meetinghouse','Saylesville Friends Meetinghouse','Lincoln','riprov','worship','standing',41.9009,-71.41777,'exact','open','drive','','1703–',
  'A Quaker meeting house built in 1703-04 and more than doubled about 1745, one of the oldest in New England and, its meeting says, in use for worship since 1704, longer than any other Friends meeting house in Rhode Island. Stephen Hopkins, a signer of the Declaration of Independence, married Anna Smith here in 1755. It is now under the care of Providence Friends Meeting.',
  'Plain inside, as Quakers built: benches set roughly in a square, a facing bench and back bench on the north wall, three galleries (later closed in as Sunday-school rooms), irregular hand-cut floorboards in the old west part and panels that swing up on iron hooks to join the men\'s and women\'s meetings. A stone horse-mounting ramp stands on the east edge, and the burial ground behind holds Hearthside\'s builder, Stephen Hopkins Smith.',
  '',
  'Providence Friends Meeting, 374 Great Road. Wikipedia gives worship every Sunday at 10:30 a.m. and a candlelight meeting on December 24 at 4:30; the Friends of Hearthside page says it is also open for viewing on the third Saturday morning of each month. Providence Friends\' own page lists meetings but gave no times.',
  [W('Saylesville Meetinghouse'),L('Providence Friends Meeting: Saylesville','https://providencefriends.org/wordpress/?p=1693'),HHV],brick='no',
  hours='Worship Sundays 10:30 a.m.; open for viewing the third Saturday morning of each month; candlelight meeting December 24, 4:30 p.m.'),
# ---- Johnston and Smithfield ----
N('clemence-irons-house','Clemence–Irons House','Johnston','riprov','landmark','standing',41.84089,-71.48514,'exact','open','drive','','1691–',
  'A stone-ender built by the farmer Richard Clemence in 1691 (a 2003 tree-ring survey gave the date). By 1938 it had grown to 13 rooms; the Sharpe family bought it then and had Norman Isham, who had restored the Arnold House, take it back to its 17th-century form. It went to what is now Historic New England in 1947.',
  'A storey and a half with a steep roof, a stone chimney end and a rear lean-to: a great room and chamber in front, a kitchen and small chamber behind, rebuilt by Isham from old and new materials and furnished with pieces made from old wood. Wikipedia notes it is as much a record of 1930s restoration ideas as of 1691.',
  '',
  'Owned and run by Historic New England, 38 George Waterman Road. Its own page answered HTTP 403 with no archived copy; Wikipedia says it opens on Saturdays from June to mid-October. Hours not checked on the owner\'s page.',
  [W('Clemence–Irons House'),L('Historic New England: Clemence-Irons House (page not read)','https://www.historicnewengland.org/property/clemence-irons-house/')],brick='no',hours='?'),
N('smith-appleby-house','Smith–Appleby House','Smithfield','riprov','landmark','standing',41.90191,-71.51783,'exact','open','drive','','1696–',
  'Begun by Elisha Smith, grandson of John Smith "the Miller", as a small stone-ender: Wikipedia gives 1696 (its infobox says 1697) and the house\'s own site says 1702. It was made a saltbox about 1713, raised about 1750, and about 1800 a second house hauled from Johnston was joined on. When Georgiaville Pond was made, Stillwater Road was moved and the house\'s front and back were swapped. The farm once had mills and a smithy on 700 acres.',
  'The museum\'s site lists early New England cabinetwork, stencilling, painted (faux-finished) floors and period furniture, with exhibits on Smithfield. Home of the Historical Society of Smithfield.',
  '',
  'Historical Society of Smithfield, 220 Stillwater Road. Wikipedia says it is open during scheduled events or by arrangement; the next listed on the society\'s site was an open house on Sunday, December 6, from 1 to 4.',
  [W('Smith–Appleby House'),L('Smith-Appleby House Museum','http://www.smithapplebyhouse.org/')],conf='mixed',brick='?',hours='At scheduled events (open house Sunday December 6, 2026, 1 to 4 p.m.) or by arrangement'),
# ---- Woonsocket and North Smithfield ----
N('museum-of-work-and-culture','Museum of Work and Culture','Woonsocket','riprov','industry','standing',41.99923,-71.51617,'exact','open','drive','','',
  'A museum of the immigrants, many from Quebec, who came to work in the Blackstone Valley mill towns, run by the Rhode Island Historical Society in what it calls a restored mill in Market Square.',
  'A two-storey red-brick mill on Market Square (Wikipedia\'s photograph). Inside, visitors start in a 19th-century Quebec farmhouse and move into the mill-town working day. When the building was built was not checked.',
  '',
  'Rhode Island Historical Society, 42 South Main Street. Closed New Year\'s Day, Easter, July 4, Thanksgiving, Christmas Eve and Day and New Year\'s Eve. Parking in front and in the city lot across the street (the society\'s page).',
  [W('Museum of Work and Culture'),L('Rhode Island Historical Society: Museum of Work & Culture','https://www.rihs.org/locations/museum-of-work-culture/')],brick='yes',
  hours='Tuesday to Friday 9:30 to 4, Saturday 10 to 4; closed Sunday and Monday'),
N('st-ann-arts-cultural-center-woonsocket','St. Ann Arts and Cultural Center (St. Ann\'s Church)','Woonsocket','riprov','worship','standing',42.00761,-71.50145,'exact','open','drive','','1914–',
  'A French-Canadian millworkers\' church built from 1914 to 1917 (first Mass 1918) to replace a brick church and school of 1890, paid for in small gifts. The Italian artist Guido Nincheri covered its walls and vaults in frescoes with about 475 faces modelled on local people. The diocese later closed it, and volunteers formed the arts centre to keep it.',
  'Twin towers, a nave seating 1,500 under a 65-foot ceiling, and what the centre calls North America\'s largest collection of fresco paintings. Phone cameras only inside.',
  'The "Sistine Chapel" of a mill town, painted with its own parishioners.',
  'St. Ann Arts and Cultural Center, a volunteer non-profit, 84 Cumberland Street. Walk-in tours on Sundays (about 45 minutes, $15, under-5s free); group tours on other days by booking, 20 people at least. A separate congregation holds a service there on Sundays at 10. Small lot beside the centre at Cumberland and Locust Streets.',
  [STANN,STANNP,STANNH,RIM],brick='?',hours='Tours Sundays 12 to 4 p.m., no reservation; groups on other days by booking'),
N('slatersville-mill-village','Slatersville mill village','North Smithfield','riprov','town','standing',41.99941,-71.57647,'site','public','walk','','1803–',
  'A planned mill village founded in 1803 by Samuel and John Slater with Almy and Brown. By 1807 it had the largest and most modern mill of its day, worker houses, the owner\'s house and a company store. The first mill burned in 1826 and was replaced by the stone mill there now; a second stone mill followed in 1843. The green was laid out in 1838. The Slaters owned the village until 1900. It is one of the six sites of the Blackstone River Valley National Historical Park.',
  'The Park Service names the Center Mill (Mill No. 1) of 1826 with its five-storey belltower, the Granite Mill (No. 3) of 1843 behind it, a brick weave shed of 1894 and a wooden office, the last piece of the first mill; the mills became flats in 2007 and are not open. Also the green with company houses of 1810-20, the Greek Revival Congregational church, the stone storehouse of the Western Mill (now part of the library), the company store, the dams on the Branch River and a stone arch bridge of 1857.',
  '',
  'A public village: the walk is on town streets and sidewalks, and the green and the river path are stops on the Park Service tour. The Park Service\'s seven-stop self-guided walk keeps to sidewalks and paved paths and starts at 20 Main Street, by the North Smithfield Public Library, where there is a lot. The mill buildings are private flats.',
  [W('Slatersville, Rhode Island'),L('National Park Service: Slatersville self-guided tour','https://www.nps.gov/blrv/planyourvisit/slatersville-self-guided-tour.htm'),L('National Park Service: Slatersville Mill','https://www.nps.gov/places/slatersville-mills.htm')],
  th=[41.99946,-71.58126],thn='Library lot by 20 Main Street, start of the walk',brick='some'),
# ---- Glocester, Foster, Scituate ----
N('brown-hopkins-country-store-chepachet','Brown & Hopkins Country Store','Glocester','riprov','civic','standing',41.91435,-71.67031,'exact','open','drive','','1809–',
  'A general store that says it has traded without a break since 1809, on Putnam Pike in Chepachet village. Chepachet saw the end of the Dorr Rebellion in 1842, and in 1826 Betty the Learned Elephant was shot on the village bridge over the Chepachet River, now marked with a plaque.',
  'Two floors of goods in the old store. When the building itself went up and what original fittings survive were not checked; interior not checked.',
  '',
  'A working shop, 1179 Putnam Pike, Chepachet. Its own page says it is open all year but gives no days or times.',
  [L('Brown & Hopkins Country Store','https://www.brownandhopkins.com/'),W('Chepachet, Rhode Island')],brick='?',hours='?'),
N('foster-town-house','Foster Town House (Elder Hammond\'s Meetinghouse)','Foster','riprov','civic','standing',41.78355,-71.72079,'exact','view','drive','','1796–',
  'Built in 1796-97 as the meeting house of Elder John Hammond\'s Second Baptist Church, with money from a lottery the General Assembly allowed. Town meetings have been held in it since 1801, and the town bought it in 1822. An "Old Home Day" begun in 1904 raised the money to repair it.',
  'A nearly square building in the old Puritan form, pulpit wall facing the door on the long sides. The state survey describes a raised dais where a double pulpit stood, plank pews with galleries on three sides, a corner stair and the heavy framing exposed against plaster. An HMdb marker stands outside.',
  '',
  'Town of Foster, Howard Hill Road in Foster Center. Visiting hours were not found; the town\'s page for it did not answer. Look from the road.',
  [FOSTER,W('Foster Center, Rhode Island'),L('HMdb: Foster Town House','https://www.hmdb.org/m.asp?m=297561')],brick='?'),
N('mount-vernon-tavern-foster','Mount Vernon Tavern','Foster','riprov','hotel','standing',41.73088,-71.71362,'exact','view','drive','','c.1760–',
  'A stagecoach stop on the Plainfield Turnpike between Providence and Connecticut. Wikipedia gives the main block as about 1760; the state survey says Pardon Holden opened the tavern and store about 1815, and that the Mount Vernon Bank, the only bank Foster ever had, opened in a front chamber in 1823. An older part was pulled down in the late 1800s.',
  'A two-and-a-half-storey centre-chimney house with a lower west ell that held the store and post office. Its Federal doorway of about 1814 is one of the best in the town: a semicircular fanlight with a keystone, a double door between Ionic pilasters and a pedimented porch on two slim posts. Across the road the Friends meeting house of 1795, now Mount Vernon Baptist Church, marks the old hamlet.',
  '',
  'A private house at 199 Plainfield Pike (Route 14). Look from the road.',
  [W('Mount Vernon Tavern'),FOSTER],conf='mixed',brick='no'),
N('ramtail-factory-foster','Ramtail factory (Foster Woolen Manufactory) ruins','Foster','riprov','industry','ruins',41.81482,-71.6975,'area','ask','hike','','c.1813–1873',
  'William Potter, Peleg Walker and partners set up the Foster Woolen Factory, called the Ram Tail Mill, half a mile south of Hopkins Mills about 1813, spinning and later weaving wool. The state survey says it stopped before 1850 or about 1840, after a falling-out between Potter and Walker; Walker hanged himself, the mill was said to be haunted, it partly burned in 1873 and the 1885 state census listed it as haunted. Hiker and folklore pages tell the ghost story in more detail.',
  'The state survey of about 1982 lists the remains of a dam and a sluiceway, a mill foundation and the cellar holes of three mill houses on a hillside above the Ponagansett. Waymarking visitors report the foundations under brush along the river. Not checked on the ground.',
  'Rhode Island\'s "officially haunted" mill.',
  'Who owns the ruin was not confirmed: the Foster Land Trust\'s Hopkins Property nearby (gated entrance on Ram Tail Road by Hopkins Mills Cemetery, a trail to the old bridge where Dolly Cole Brook meets the Ponagansett) is documented, but no page read puts the factory on it. The federal public-land map puts the point in a unit called Barden Reservoir with its owner type unknown. Treat it as private and ask the Foster Land Trust or the town before going. Hours not checked.',
  [FOSTER,L('Waymarking: Ram Tail Mill Site','https://www.waymarking.com/waymarks/WM4PJA_Ram_Tail_Mill_Site'),L('Foster Land Trust: Hopkins Property baseline report (PDF)','https://www.landandwaterpartnership.org/documents/Hopkins.pdf')],conf='mixed',brick='?'),
N('old-congregational-church-north-scituate','Old Congregational Church','Scituate','riprov','worship','standing',41.83445,-71.5869,'exact','view','drive','','1831–',
  'A shingled wooden church designed by Clark Sayles, a follower of the church builder Elias Carter, and finished in 1831. Used less and less through the 1800s and only now and then until 1940, when it was given to the town. The Scituate Art Festival has been held on its grounds every autumn since 1967, started to pay for restoring the interior.',
  'The white steepled church on Greenville Road (Route 116) in North Scituate. Interior not checked.',
  '',
  'Town of Scituate. No visiting times were found; look from the road, or come at the autumn art festival.',
  [W('Old Congregational Church (North Scituate, Rhode Island)')],brick='no'),
]
PIN_NOTES={
 'old-slater-mill-pawtucket':'ArcGIS point address for 67 Roosevelt Avenue; Wikipedia\'s point is about 20 m away.',
 'daggett-house-pawtucket':'OpenStreetMap building "Daggett House" in Slater Park; the Wikipedia infobox point is 1.9 km north, off the park.',
 'eleazer-arnold-house':'ArcGIS point address for 487 Great Road.',
 'hearthside-house-lincoln':'ArcGIS point address for 677 Great Road.',
 'moffett-mill-lincoln':'ArcGIS point address for 585 Great Road, the address a Blackstone tourism page gives the mill; a Waymarking marker is about 200 m north-west. On the aerial the point is on Great Road in trees near the river crossing and the mill could not be picked out, so prec is site.',
 'saylesville-friends-meetinghouse':'ArcGIS point address for 374 Great Road.',
 'clemence-irons-house':'ArcGIS point address for 38 George Waterman Road.',
 'smith-appleby-house':'ArcGIS point address for 220 Stillwater Road.',
 'museum-of-work-and-culture':'ArcGIS point address for 42 South Main Street.',
 'st-ann-arts-cultural-center-woonsocket':'ArcGIS point address for 84 Cumberland Street.',
 'slatersville-mill-village':'OpenStreetMap building "Slatersville Mill" (the Center Mill).',
 'brown-hopkins-country-store-chepachet':'ArcGIS point address for 1179 Putnam Pike.',
 'foster-town-house':'HMdb marker position for the Foster Town House, which matches the ArcGIS point for 180 Howard Hill Road.',
 'mount-vernon-tavern-foster':'ArcGIS point address for 199 Plainfield Pike.',
 'ramtail-factory-foster':'The position two Waymarking pages give (N 41 48.889 W 071 41.850). The aerial shows only woods; the LiDAR sheet shows small rectangular hollows and mounds round the pin with an old track running south, which fits foundations and cellar holes. Not confirmed on the ground.',
 'old-congregational-church-north-scituate':'OpenStreetMap place of worship "Old Congregational Church".',
}
BATCH={'key':'riprov_wssn','label':'Providence County, Rhode Island: stone-enders, Slater mills and Woonsocket','added':'2026-11-20 01:57'}
