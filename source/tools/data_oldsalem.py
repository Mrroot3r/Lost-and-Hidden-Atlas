# November 17, 2026: Old Salem and the country round Winston-Salem, Forsyth County, North Carolina. A first real pass at
# North Carolina, which had one place (Brunswick Town). Old Salem itself is a restored, standing town, so this batch takes
# what is not standing there: the cellar holes, foundations and outlines that Old Salem's archaeologists have left open or
# marked, the hidden graveyards at St. Philips, and the line of the 1820 mill race. Round the city: the stabilized cellars,
# fort, God's Acre and mill site of Bethabara (the first Moravian town, 1753), Lake Katharine at Reynolda (a lake that is
# now a wetland), Idols Dam on the Yadkin (the 1898 hydroelectric station) and the flooded Piedmont Quarry.
# Facts come from the linked sources only. The Old Salem entries rest mostly on Old Salem Museums & Gardens' own marker
# texts as transcribed on HMdb (read through a small script, one page a marker); Bethabara on the National Historic
# Landmark nomination (NPS PDF, text layer read with tools/page.py) and the park's own pages (historicbethabara.org refuses
# scripts; read with the web fetch tool); the rest on the managing bodies' pages (Reynolda, City of Winston-Salem, Yadkin
# Riverkeeper) and the state's marker and blog pages. Where sources disagree the text gives both; where a source is silent
# it says "not checked". Pins: an HMdb marker position, an OpenStreetMap feature or a spot read off the aerial or LiDAR,
# as each pin note says; every pin was looked at on the pin check (research/pincheck_oldsalem_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'oldsalem','label':'Old Salem and Winston-Salem: cellar holes, Bethabara, Reynolda, Idols Dam','added':'2026-11-17 14:11'}
def HM(n,t): return L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
OSFAQ=L('Old Salem Museums & Gardens: FAQs and policies (hours, pets on the streets)','https://www.oldsalem.org/faqs/')
OSTIX=L('Old Salem Museums & Gardens: ticket information','https://www.oldsalem.org/ticket-information/')
OSACC=('Old Salem Museums & Gardens. The historic district\'s streets and sidewalks are open to walk; Old Salem\'s FAQ welcomes '
       'leashed pets on them and sells tickets only for the interpreted buildings, which it gives as open Wednesday to Saturday, '
       '10 am to 4 pm, closed in January. Old Salem\'s visitor center, where tickets are sold, is at 900 Old Salem Road, with a '
       'timber footbridge (the Heritage Bridge) over Old Salem Road into the district; parking there was not checked on an Old '
       'Salem page that opened. ')
BBNHL=L('NPS: Bethabara National Historic Landmark nomination (1998, PDF)','https://npgallery.nps.gov/NRHP/GetAsset/NHLS/78001948_text')
BBHRS=L('Historic Bethabara Park: park hours and information','https://historicbethabara.org/park-hours-info/')
BBMAP=L('Historic Bethabara Park: park maps (site list)','https://historicbethabara.org/trail-maps/')
BBACC=('Historic Bethabara Park, run by the City of Winston-Salem Recreation and Parks Department with the nonprofit Historic '
       'Bethabara Park Inc. By the park\'s hours page the grounds and trails are free and open every day, dawn to dusk; the '
       'visitor center (2147 Bethabara Road) is open Tuesday to Saturday 10:30 am to 4:30 pm and Sunday 1:30 to 4:30 pm, on '
       'weekend hours only from January to March, and closed at Easter, Thanksgiving and from mid-December to the end of the '
       'year; guided tours cost $5 for adults and $1 for students and children over 3 (the older park map says $4). Dogs: not '
       'checked. ')
PLACES=[
# ---- Old Salem: what the archaeologists left open ----
N('reich-hege-cellar-old-salem','Reich-Hege House cellar hole','Winston-Salem (Old Salem)','nc','town','ruins',36.08363,-80.24077,'exact','public','walk','','1830–1922',
  'Shoemaker Emanuel Reich built a frame house on a stone foundation here on Lot 101 in 1830, its rooms round a central chimney, with one wing for his shoe shop and one for his aunt. Mill owner George Hege bought it in 1851, added a second storey and a two-storey Greek Revival porch; the lot also held a barn, a building census takers called a slave house, and other outbuildings. Lewis Hege (1840–1918), enslaved here, became a leader of the African church next door. The house was taken down in 1922 for the Central School; Old Salem cleared the lot in the 1970s and its archaeologists dug it in 2005–2006, then left it open to be seen.',
  'By the two Old Salem markers: the original cellar hole, stone foundation walls and the central chimney footing of the 1830 house, with the outlines of the 1830 house (tan) and the 1850 enlargement (dark red boards) laid on the ground, and an exhibit of part of the house front. Not checked on the ground.',
  'A cellar hole in a museum town, kept open on purpose.',
  OSACC+'The site is on Race Street at South Church Street, beside St. Philips Church; whether the lot is fenced was not checked.',
  [HM(172073,'Reich-Hege Lot (1830)'),HM(172102,'Reich-Hege House Site (1830-1922)'),OSFAQ,OSTIX],conf='',th=None,thn=None),
N('salem-tavern-smokehouse','Salem Tavern smokehouse foundation','Winston-Salem (Old Salem)','nc','town','ruins',36.08545,-80.24220,'exact','public','walk','','',
  'The smokehouse that cured meat for the guests of the Salem Tavern stood here. Old Salem\'s marker describes the process: meat packed in salt for up to six weeks, then hung over a slow fire of green wood for one or two weeks, and kept in the smokehouse afterwards. Its stone foundation was found by archaeologists. When it was built and when it went are not on the marker.',
  'A stone foundation that marks the smokehouse, by the marker reached from South Main Street at Blum Street. Whether it lies in a ticketed yard was not checked.',
  '',
  OSACC,
  [HM(172068,'Tavern Smokehouse'),OSFAQ],conf='',th=None,thn=None),
N('second-house-site-salem','Second House site (the "Two-Story House")','Winston-Salem (Old Salem)','nc','town','traces',36.08907,-80.24245,'exact','public','walk','','1767–before 1861',
  'Salem\'s second house, finished in 1767, was half-timbered with a clay tile roof and was called the Two-Story House because it was the first of that height. It served as the first congregation house for church services until 1771, then as the community store until 1775, briefly as a Continental hospital in the Revolutionary War, and for about 75 years as the home of the Meinung family of surveyors. It was gone before 1861, when Francis Fries had a store on the lot; Old Salem says there is not enough evidence to rebuild it.',
  'An outline on the ground showing where the house stood, by the marker on South Main Street near West Bank Street. Not checked on the ground.',
  '',
  OSACC,
  [HM(172144,'Second House Site (1767)'),OSFAQ],conf='',th=None,thn=None),
N('builders-house-site-salem','Builders\' House and Shaffner pottery site','Winston-Salem (Old Salem)','nc','industry','marker',36.09098,-80.24395,'site','public','walk','','1766–1907',
  'On January 6, 1766 a dozen men came from Bethabara and Bethania to the chosen spot for Salem and that afternoon began a one-storey log shelter, the Builders\' House, the first building of the new town. A farmer used it after 1772. In 1834 Heinrich Shaffner set up a pottery on this lot (Lot 81), using the house as his shop and adding a kiln, dry house, pug mill and warehouse; the pottery ran until about 1900 and the buildings stood until 1907. Old Salem\'s archaeologists dug the lot from 2000 to 2008.',
  'Two markers on Brookstown Avenue just west of Old Salem Road and a lighting work made for Salem\'s 250th anniversary with the UNC School of the Arts, on the house site. Whether any foundation is shown: not checked.',
  'Where Salem began: one log hut, later a pottery.',
  OSACC,
  [HM(172153,"Builders' House"),HM(172154,"Builders' House Lighting Project"),OSFAQ],conf='',th=None,thn=None),
N('st-philips-graveyards-salem','Strangers\' and African American graveyards at St. Philips','Winston-Salem (Old Salem)','nc','burial','traces',36.08413,-80.24025,'site','public','walk','cemeteries','1816–1859',
  'The old Parish Graveyard for non-Moravians was extended to the street and set aside in 1816 for every African American, Moravian or not, who died in and around Salem; 108 people, enslaved and free, were buried there until it closed in 1859. Archaeology suggests Christians were buried north of an east-west walk, divided by age and church, and at least 92 others south of it. In 1913 the few gravestones were pulled up and the ground landscaped, leaving no trace; in 1994 archaeologists found 31 stones under the steps and hall of St. Philips Church. Salem\'s African congregation, formed in 1822, first built a log church; the church of 1861 that replaced it is the oldest surviving African American church building in North Carolina.',
  'Modern stones on the 90 graves archaeologists have located, marked adult or child, with replica stones on the few identified graves, and a plaque on the church naming everyone known to be buried in both graveyards (marker text). The last burials in the old Parish Graveyard, before the graveyards were segregated in 1816, have also been located. The restored church is one of Old Salem\'s interpreted buildings.',
  'A graveyard erased in 1913, found again under a church floor.',
  OSACC+'The graveyard is on South Church Street just north of Race Street.',
  [HM(172103,'The African American Graveyard'),HM(172104,'Last Burials in the Parish Graveyard'),W('St. Philips Moravian Church'),OSFAQ],conf='',th=None,thn=None),
N('salem-flour-mill-race','Salem Flour Mill race','Winston-Salem (Old Salem)','nc','industry','traces',36.08415,-80.24008,'area','public','walk','','1820–1923',
  'In 1820 a mill race, 4,521 feet long and 10 feet wide, was dug to carry water to the new Salem Flour Mill southwest of town, looping round St. Philips Church on the way. Its running water eased fears of fever from stagnant ponds, and boys swam in it, to the worry of church leaders. The mill burned in December 1902, and the race was lost when Salem Avenue was built in 1923.',
  'Nothing of the race itself is described as surviving: the marker says its line is kept by the name of Race Street and by the bends of Salem Avenue. The marker stands by a split-locust rail fence south of St. Philips, with the race having run just beyond the fence.',
  'A street named for a ditch nobody can see.',
  OSACC+'Race Street and Salem Avenue are city streets.',
  [HM(172118,'The Landscape South of St. Philips'),HM(172073,'Reich-Hege Lot (1830)')],conf='',th=None,thn=None),
# ---- Bethabara, the first Moravian town (1753) ----
N('bethabara-ruins-fort','Bethabara: stabilized cellars and palisade fort','Winston-Salem (Bethabara)','nc','fort','ruins',36.15552,-80.29763,'site','public','walk','forts','1753–',
  'Bethabara was the first Moravian settlement in the Wachovia tract, begun in 1753 and a trades town by 1766. In July 1756, during the French and Indian War, the Moravians built a five-sided palisade round the middle of the town in 18 days, and refugees built cabins inside it; the stockade was pulled down in 1762. When the people moved on to Salem some buildings were taken apart for materials, leaving open cellars, which later farmers filled in to plough. Stanley South dug the site in the 1960s; the park says more than 40 ruins are now stabilized, and the palisade was rebuilt on the line of its original ditch, beginning on the northeast side in 1966.',
  'Stone-lined dry cellars of the 18th-century houses and shops, opened and stabilized for visitors, the stabilized cellar of the 1756 first church north of the 1788 Gemeinhaus, the site of Gottfried Aust\'s 1755 pottery shop, and the rebuilt palisade, which a park marker calls the only French and Indian War fort in the Southeast rebuilt on its own site. The 1788 Gemeinhaus, the 1782 Potter\'s House and the 1803 Brewer\'s House stand.',
  'A frontier fort and forty cellar holes, rebuilt where they stood.',
  BBACC+'Parking at the visitor center; a second mapped lot on Old Town Drive is on park land.',
  [BBNHL,BBHRS,HM(234122,'The Foundations'),HM(53517,'Bethabara Fort 1756-63'),HM(162107,'Palisade Fort'),L('Historic Bethabara Park: historic buildings and grounds','https://historicbethabara.org/?p=160'),W('Bethabara Historic District')],conf='',th=[36.15606,-80.30188],thn='Historic Bethabara Park lot, Old Town Drive'),
N('bethabara-gods-acre','Bethabara God\'s Acre','Winston-Salem (Bethabara)','nc','burial','standing',36.15391,-80.29815,'area','public','hike','cemeteries','1757–',
  'The first Moravian graveyard in Wachovia, in use since the town\'s early years (the landmark nomination lists it as 1757). It is laid out in four quarters by the Moravian choir system: married men in the southwest, married women in the northwest, single men in the southeast and single women in the northeast, the last two split again into youths and adults and infants. Later 19th-century monuments of the popular kinds of the day stand along the south edge, from when it served the scattered country Moravians.',
  'The graveyard on the wooded hill west of the village, reached by a footpath (mapped as God\'s Acre Cemetery Trail; "To God\'s Acre Trail" on the park map). Not checked on the ground; the exact spot of the graveyard was not found on the aerial.',
  '',
  BBACC,
  [BBNHL,BBMAP,BBHRS],conf='',th=[36.15606,-80.30188],thn='Historic Bethabara Park lot, Old Town Drive'),
N('bethabara-mill-site','Bethabara mill site and Dobbs Parish graveyard','Winston-Salem (Bethabara)','nc','industry','traces',36.15640,-80.30800,'area','public','hike','','',
  'About half a kilometre from the town the Moravians spent two years building a mill complex of grist and saw mills with a mill house, dam and race. In 1758, as the Cherokee War came closer, they put a second stockade round the mill and built refugee cabins there. In 1759 they laid out a Strangers\' Graveyard near the mill for the non-Moravians who died while sheltering at Bethabara; it was renamed Dobbs Parish Graveyard in 1769 and used until about 1825, with later graves outside its bounds. Digs in 1985 found rock foundations of the mill along the creek.',
  'Sources differ on what a visitor can reach: the 1998 landmark nomination says the mill site was not open to visitors and the graveyard overgrown and not interpreted, and that both are reached by a sunken road; the park\'s current map lists an "Old Mill Site", and its children\'s sheet asks visitors to find where grain was ground and draw the big stone. The Mill Creek and Millrace trails run here. Not checked on the ground.',
  '',
  BBACC,
  [BBNHL,BBMAP,L('Historic Bethabara Park: park map and scavenger hunt (PDF)','https://historicbethabara.org/wp-content/uploads/2020/03/BBP20001_ScavengerHunt_English_d1.pdf')],conf='mixed',th=[36.15606,-80.30188],thn='Historic Bethabara Park lot, Old Town Drive'),
# ---- Round the city ----
N('lake-katharine-reynolda','Lake Katharine (now a wetland) and boathouse, Reynolda','Winston-Salem (Reynolda)','nc','water','traces',36.12800,-80.28320,'area','public','walk','','',
  'One of Katharine Reynolds\' first works at the Reynolda estate was to dig out about 16 acres of the Silas Creek bed and dam it into Lake Katharine, the main feature of the grounds when the family moved in in 1917; thousands of fieldstones from the dig went into the dam, chimneys and foundations. The lake was for fishing and boating, and a pump house lifted its water to a cistern for watering the gardens. The lake is now a wetland. When and why it went to wetland was not checked.',
  'The wetland where the lake was, the boathouse designed by Charles Barton Keen and built before January 1913 (still standing, used for children\'s programmes), and the cement cistern at the corner of Reynolda Road and Coliseum Drive.',
  'A rich family\'s lake, gone back to marsh.',
  'Reynolda Gardens of Wake Forest University: by its pages the gardens and grounds are open year-round from dawn to dusk, free, with more than two miles of trails; park in the free lots outside the main gardens entrance at 100 Reynolda Village. Leashed dogs are welcome everywhere but the Formal Gardens.',
  [L('Reynolda: The Waters of Reynolda','https://reynolda.org/feature-stories/the-waters-of-reynolda/'),L('Reynolda: trails and outdoor spaces','https://reynolda.org/gardens/trails-outdoor-spaces/'),L('Reynolda: hours, directions and admission','https://reynolda.org/visit/'),L('Reynolda: gardens and grounds','https://reynolda.org/gardens/')],conf='',th=[36.12413,-80.28538],thn='Reynolda Village parking lot'),
N('idols-dam-yadkin','Idols Dam and hydroelectric station','Clemmons','nc','industry','ruins',35.97428,-80.39938,'site','boat','boat','','1898–',
  'Henry E. Fries\'s Fries Manufacturing and Power Company built a low run-of-the-river dam and power plant at the old Idol\'s ferry on the Yadkin, starting in 1897; investors included Thomas Edison and Frank Sprague. It began sending power to the Fries family\'s Arista mill in Salem about 13 miles away in April 1898, the first long-distance transmission of electricity in North Carolina (the state gives April 20, ASME April 18). Duke took it over in 1914 and replaced the machinery, and ran the station until 1996. In 1998 a fire destroyed the generator shed built out over the river and ruined the inside of the brick transformer building. The dam, built in 1898 and never much repaired since, is owned by Winston-Salem/Forsyth County Utilities and holds the pool for the Idols pump station, which supplies about 70 percent of the utility\'s water.',
  'From the river: the low masonry dam across the Yadkin and what is left of the station. The state gives the dam as 482 feet long; the federal dam list (as copied by a dam-safety site) gives 665 feet. In December 2006 a demolition of the station building was postponed (ASME); NC Anchor says a generator set and bricks from the old buildings were kept for a planned restoration. Whether the building still stands was not checked.',
  'Where North Carolina first sent power down a wire: a burned plant on a working dam.',
  'Utility land, closed to visitors (ASME). Seen by paddlers on the Yadkin River State Trail: put in at the Tanglewood access, 4061 Clemmons Road, Clemmons (Forsyth County; gate open 9 am to 5 pm, a small gravel lot of about 10 spaces), and carry round Idol\'s Dam about four miles downstream at mile 72, leaving the river on the right just before the railroad trestle; the next take-out is US 64, 16.7 miles from Tanglewood (Yadkin Riverkeeper). WARNING: a low-head dam. In 2009 paddlers reported the warning signs at the spillway hidden; know the portage before you set out.',
  [L('NC Dept. of Natural and Cultural Resources: Hydroelectric power introduced, 1898','https://www.dncr.nc.gov/blog/2016/04/20/hydroelectric-power-introduced-1898'),L('NCDNCR: Fries Manufacturing and Power Co. marker J-70','https://www.dncr.nc.gov/blog/2024/01/08/fries-manufacturing-and-power-co-j-70'),L('ASME landmark 99: Idols Station','https://www.asme.org/about-asme/engineering-history/landmarks/99-idols-station-fries-manufacturing-power-co'),L('NC Anchor: Idol\'s Dam and Power Plant','https://www.ncanchor.org/anchor/idol%25e2%2580%2599s-dam-and-power-plant'),L('Yadkin Riverkeeper: Yadkin River State Trail accesses','https://www.yadkinriverkeeper.org/yadkin-river-access'),L('Salisbury Post (2009): signs at Idols Dam obscured','https://www.salisburypost.com/?p=106327'),L('Dam record: Idols Reservoir Dam','https://recallcheck.net/dam-safety/47646'),L('ConstructConnect: Idols Dam structural assessment (city project listing)','https://projects.constructconnect.com/details/5950451-rfq-idols-dam-structural-assessment&find_loc=NC-27101')],conf='mixed',th=[36.013597,-80.416689],thn='Tanglewood river access (paddle put-in, 4 miles upstream)'),
N('piedmont-quarry-winston-salem','Piedmont Quarry (The Quarry at Grant Park)','Winston-Salem','nc','industry','traces',36.08038,-80.20186,'site','public','walk','','1920s–1970s',
  'Piedmont Quarry supplied crushed rock for the homes, schools and roads of Winston-Salem from the 1920s (the city says the mid-1920s). Vulcan Materials owned it by 1960; it last produced stone in the early 1970s, though stockpiled stone was sold there as late as 1982, and after the late 1980s the pit filled with water. Vulcan gave the land to the city (1997 by the city\'s page, 1998 by the Winston-Salem Chronicle), and it opened as a park after the city\'s 2014 bonds.',
  'The flooded pit ringed by high rock cliffs, seen from an overlook pier over its eastern side and several other overlooks.',
  '',
  'City of Winston-Salem park, open sunrise to sunset; 1790 Quarry Road, entered off Reynolds Park Road next to the tennis courts; also reached on foot or bike by the Waughtown Connector greenway. No boats, kayaks or other craft on the water, and the Chronicle says there is no public access to the water at all; clean up after dogs.',
  [L('City of Winston-Salem: The Quarry at Grant Park','https://www.cityofws.org/quarrypark'),L('Winston-Salem Chronicle: Quarry Park opens to public','https://wschronicle.com/quarry-park-opens-public/')],conf='mixed',th=[36.08025,-80.20142],thn='Quarry Park lot, Quarry Road'),
]
PIN_NOTES={
 'reich-hege-cellar-old-salem':'HMdb position of the Old Salem marker "Reich-Hege Lot (1830)", which stands at the cellar hole on Race Street. The aerial shows a small cleared lot with a low structure; the LiDAR shows a small rectangular hollow and walls at the pin.',
 'salem-tavern-smokehouse':'HMdb position of the Old Salem marker "Tavern Smokehouse", which stands at the foundation.',
 'second-house-site-salem':'HMdb position of the Old Salem marker "Second House Site (1767)" on South Main Street, beside the outline.',
 'builders-house-site-salem':'HMdb position of the Old Salem marker "Builders\' House" on Brookstown Avenue; the house site is on the same lot.',
 'st-philips-graveyards-salem':'HMdb position of the Old Salem marker "The African American Graveyard" on South Church Street, beside the graveyard.',
 'salem-flour-mill-race':'HMdb position of the Old Salem marker "The Landscape South of St. Philips"; the race ran just beyond the fence there. Its line is not mapped, so area only.',
 'bethabara-ruins-fort':'HMdb position of the park markers "The Foundations" and "The Palisade"; the aerial shows the rebuilt palisade fence round the open ground at the pin, with the Gemeinhaus to the northeast.',
 'bethabara-gods-acre':'The God\'s Acre Cemetery Trail as mapped in OpenStreetMap, so area only. The aerial shows a cleared graveyard with rows of stones about 200 m southwest of the pin, on a flat bench in the LiDAR; it may be God\'s Acre or a later churchyard, and was not confirmed.',
 'bethabara-mill-site':'The Millrace Trail as mapped in OpenStreetMap, beside Mill Creek, so area only. The LiDAR shows a straight raised bank running east and west through the pin, which may be the race or a later sewer line; not identified.',
 'lake-katharine-reynolda':'Silas Creek below Reynolda as mapped in OpenStreetMap, so area only. The LiDAR shows a broad flat bottom with a wandering creek here, which fits a filled lake bed; the boathouse and dam were not placed.',
 'idols-dam-yadkin':'The dam as mapped in OpenStreetMap; the aerial and LiDAR show the dam crossing the Yadkin under the pin, with gates and a building at its north (Forsyth) end and the railroad trestle just to the west.',
 'piedmont-quarry-winston-salem':'Moved with tools/pix.py onto the overlook pier at the east edge of the flooded pit, as seen on the aerial; the first pin (the OpenStreetMap park feature) was on a building in a field.',
}
