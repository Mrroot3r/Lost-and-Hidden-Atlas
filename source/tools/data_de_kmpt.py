# November 24, 2026: Delaware, fourth pass, taken with tools/choose.py --thinnest. One scatter over all three counties:
# Sussex (Milton, Harbeson, Seaford), Kent (Clayton, Sandtown, Little Creek) and New Castle (New Castle, St. Georges,
# Wilmington). Facts only from pages read in this session: Wikipedia articles read as raw text, the Delaware Public
# Archives' marker and historic-houses-of-worship pages, the New Castle Historical Society and Wilmington Friends Meeting
# pages, and the Register lists for each county.
from data_b import N
from data_ma import W

DPA='https://archives.delaware.gov'

BATCH={'key':'de_kmpt','label':'Delaware: Milton to Wilmington','added':'2026-11-24 11:30'}

PLACES=[
# ---------------- New Castle County ----------------
N('amstel-house-new-castle','Amstel House','New Castle','de','landmark','standing',39.66065,-75.56488,'exact','open','walk','','1730s',
  'Built in the 1730s and also called the Dr. Finney House, this was the first building the New Castle Historical Society saved. In 1931 citizens raised money to buy it when new building was replacing old houses in the town, which began the preservation of New Castle as a whole.',
  'A preserved house of the 1730s in the New Castle Historic District, now a museum shown by guided tour. What original fabric survives inside is not checked.',
  'The first house New Castle saved from the wrecker, in 1931.',
  'Run by the New Castle Historical Society as a museum at 2 East 4th Street. The Society\'s page lists weekend tours until December 27, 2026 (the Amstel House starts its tours on even hours, the neighbouring Dutch House on odd hours) and group tours on other days by appointment. Street parking in the town; lots not checked.',
  [['New Castle Historical Society: plan your visit','https://newcastlehistory.org/plan-your-visit'],W('Amstel House')],
  brick='?',hours='Weekends to Dec 27, 2026: Sat 10 a.m. to 4 p.m., Sun noon to 4 p.m.; tours on even hours, last at 3 p.m.'),

N('st-georges-presbyterian-church','St. Georges Presbyterian Church','St. Georges','de','worship','standing',39.55576,-75.65181,'exact','view','walk','','1845',
  'The congregation was founded in 1698 and met first in a log building a mile west of the village. The present brick church in the village was begun in 1840 and dedicated on July 27, 1845, and it was rebuilt inside and reopened in 1904 with ten memorial windows. The St. Georges Historical Society restored the building in 1988.',
  'A one-storey brick church in the Greek Revival style, built like a temple, with a wooden steeple, on a fieldstone foundation; its roof is carried on a Town lattice truss. Inside there are a rear gallery, ten memorial windows of 1904 and two marble tablets to former ministers. The state archives say it is now a community centre.',
  'A temple-fronted brick church of 1845 on the old road through St. Georges.',
  'On Main Street in St. Georges, in the North Saint Georges Historic District. The state archives and a marker say the Historical Society restored the building and runs it as a community centre; no visiting hours were found, so look from the street unless the Society says otherwise. Street parking.',
  [['Delaware Public Archives: St. Georges Presbyterian Church',DPA+'/historic-houses-of-worship/st-georges-presbyterian-church/'],W('St. Georges Presbyterian Church')],
  brick='yes',hours='?'),

N('wilmington-friends-meetinghouse','Wilmington Friends Meetinghouse','Wilmington','de','worship','standing',39.74216,-75.55434,'exact','view','walk','cemeteries','1815-1817',
  'Quakers in Wilmington met from 1738; the first meetinghouse stood across the street, a second was built here in 1748, and the present house opened on September 25, 1817. Friends School began in the meetinghouse in 1748. The abolitionist Thomas Garrett, a member, was buried from here in 1871, and the yard is said to hold about 3,000 graves, among them John Dickinson\'s.',
  'A large meetinghouse said to hold 700 people, with a burying ground beside it, in the Quaker Hill neighbourhood. Interior not checked.',
  'The meeting where Underground Railroad conductor Thomas Garrett worshipped.',
  'An active Quaker meeting at Fourth and West Streets (401 North West Street). Its own page says all are welcome to Sunday worship at 10 a.m., and that worship is sometimes held online in bad weather, so check its page the same day. Street parking in Quaker Hill.',
  [['Wilmington Friends Meeting','https://wilmingtondefriendsmeeting.org/'],['Delaware Public Archives: Meeting House 1816',DPA+'/delaware-historical-markers/meeting-house-1816-religious-society-of-friends/'],W('Friends Meetinghouse (Wilmington, Delaware)')],
  brick='?',hours='Sunday worship 10 a.m.'),

# ---------------- Kent County ----------------
N('clayton-railroad-station','Clayton Railroad Station','Clayton','de','rail','standing',39.29121,-75.63295,'exact','view','drive','stations','about 1855',
  'The Delaware Railroad built this station about 1855 at a settlement then called Jimtown, and the town took the name Clayton. It served passengers into the 1950s and later housed an antique shop. In 1885 the railroad moved its division offices and shops to Clayton, which became one of the Delmarva peninsula\'s largest railroad centres.',
  'A one-storey, five-bay brick station in the Italianate style, with a low hipped roof that overhangs about three feet and arched windows and doors with moulded hoods; many of the fanlights remain. Inside are six rooms, one of them the ticket office. The chimneys and the passenger shed have been removed. Interior not checked.',
  'An 1850s Italianate depot of the Delaware Railroad, still standing.',
  'Beside the railroad on South Bassett Street in Clayton. Who owns it and whether it opens were not found; look from the street.',
  [W('Clayton station (Delaware)')],
  brick='yes',hours=''),

N('cow-marsh-old-school-baptist-church','Cow Marsh Old School Baptist Church','Sandtown','de','worship','standing',39.04194,-75.695,'site','view','drive','','1872',
  'Also known as Mount Moriah Baptist Church, this church near Sandtown was built in 1872 and was listed on the National Register of Historic Places in 1976.',
  'A plain one-storey rectangular frame church covered in clapboard, with a low gable roof and corner pilasters. Interior not checked.',
  'A country Baptist church of 1872 with hardly a change since.',
  'Who owns it, whether services are held and where to stop were not checked; look from the road. The pin is the Register\'s point and has been checked against the aerial photograph only.',
  [W('Cow Marsh Old School Baptist Church')],
  brick='no',hours='',conf='mixed'),

N('mahon-river-light','Mahon River Light and the Port Mahon tower','Little Creek','de','light','standing',39.1845,-75.40161,'area','view','drive','burned','1903-1955 (keeper\'s house burned 1984)',
  'The first Mahon River lighthouse, built in 1903, was a two-storey wooden keeper\'s house with an eight-sided lantern on the roof. It was discontinued in 1955, the year the present steel skeleton tower was lit, and the old house burned by accident in 1984. A replica of it serves as the clubhouse of the Jonathan\'s Landing golf course at Magnolia.',
  'The steel skeleton tower still carries a navigation light and is not open to the public. The 1903 house is gone.',
  'A steel tower that took over from a burned wooden lighthouse.',
  'Where the tower can be seen from, and who manages the land round it, were not checked; the pin is on the shore beside the pier and marks the general area, not the tower. The tower is not open to the public.',
  [W('Mahon River Light')],
  brick='no',hours='',conf='mixed'),

# ---------------- Sussex County ----------------
N('milton-historic-district','Milton Historic District','Milton','de','town','standing',38.77639,-75.30972,'area','view','walk','','late 1700s to early 1900s',
  'Milton\'s old centre is a national historic district of 188 buildings along Union, Federal, Broad, Chestnut and Mill Streets, ranging from the late 1700s to the early 1900s. Listed separately inside it are the Draper-Adkins House, the Hazzard House and the Gov. James Ponder House. The district was listed in 1982 and its boundary enlarged in 2022.',
  'Gothic Revival and vernacular houses along Union, Broad and Chestnut Streets, and larger Federal, Second Empire and Queen Anne houses along Federal Street. On Union Street are the former Grace Church of 1859 (now the Cannon Museum), two storefronts of 1910 and the Milton Theater of 1939; on Federal Street are the former Sussex Trust, Title and Safe Deposit building of 1901 and the Episcopal Church of St. John Baptist of 1877.',
  'A whole small town of 1800s buildings, walkable in an hour.',
  'The streets are open to walk, but most buildings are private homes and shops, so look from the sidewalk. Street parking in the town centre; no lot checked.',
  [W('Milton Historic District (Milton, Delaware)')],
  brick='?',hours=''),

N('cannon-museum-milton','Lydia B. Cannon Museum (Milton Museum)','Milton','de','landmark','standing',38.7792,-75.31171,'exact','open','walk','','1857, rebuilt 1906',
  'Land here was conveyed to the Methodist Protestant Church in 1857 and a church was built soon after. It was enlarged and rebuilt in 1906, when the present stained glass windows were added, and was called Grace Methodist Church from 1940. Services stopped in 1962; the Milton Historical Society bought the property in 1971 and named it for Lydia Black Cannon, who helped arrange the purchase. After a fund drive to save the failing building it reopened in 2006 with new space added.',
  'The old church sanctuary, with its 1906 stained glass windows, now holds the Milton Historical Society\'s museum. What is on show inside is not checked.',
  'A Methodist church of 1857 turned into the town\'s history museum.',
  'Run by the Milton Historical Society at 210 Union Street. The Society\'s own page could not be opened when this was written, so no hours are given; check with the Society before a visit. Street parking.',
  [['Delaware Public Archives: Milton Museum',DPA+'/delaware-historical-markers/milton-museum']],
  brick='?',hours='?'),

N('indian-mission-church-harbeson','Indian Mission Church','Harbeson','de','worship','standing',38.67351,-75.23451,'exact','view','drive','','1881, present building 1921',
  'The Nanticoke people built the first church here in 1881 and called it Johnson\'s Chapel; it belonged to the Methodist Protestant church. The congregation was formally incorporated in 1915 and the present building went up in 1921. The state marker says the Nanticoke people still hold their services here and that the church helps them keep their heritage and culture. The oldest marked grave is of 1885.',
  'A one-storey clapboard church in a late Gothic Revival style, with a two-storey tower under a hipped roof and pointed windows, and a burying ground beside it. Interior not checked.',
  'The Nanticoke community\'s own church, still in use.',
  'An active church at 22701 Indian Mission Road, on the junction of Route 5 and Road 48. No service times were found on a page of the church or its association; the Nanticoke Indian Association lists the church among its places and gives a telephone number on its page. Show respect to the congregation and its graves. Look from the road unless a service is open to visitors.',
  [['Delaware Public Archives: Indian Mission Methodist Church',DPA+'/delaware-historical-markers/indian-mission-methodist-church'],W('Indian Mission Church')],
  brick='no',hours='?'),

N('hearn-and-rawlins-mill-seaford','Hearn and Rawlins Mill','Seaford','de','industry','standing',38.67927,-75.59374,'site','view','drive','','1816, rebuilt after 1879 and about 1880',
  'Nathaniel Ross set up a grist mill on Clear Brook Branch in 1816, which created the pond. It was known by the names of two early owners, William Cannon and William Ross, and burned in 1879. Marcellus Hearn bought the site in 1885 and installed rollers for flour; his son George Hearn and daughter Mary Rawlins ran it after 1916 and the family kept it until 1999, when the United Nation of Islam bought it. The state owns the pond.',
  'A water-powered mill complex of frame buildings sheathed in metal, standing on brick footings on an earthen dam, with two overshot wheels installed in 1912. The Corn Stone saved from the 1879 fire was reinstalled in the new mill. Interior not checked.',
  'A flour mill on a dam, with two overshot wheels.',
  'The mill buildings are private or owned by an organisation; the pond is state land. The state marker stands on the Bridgeville Highway just before the bridge over the pond, which is the place to look from. Whether the mill can be entered was not checked.',
  [['Delaware Public Archives: Hearns Pond',DPA+'/delaware-historical-markers/hearns-pond'],W('Hearn and Rawlins Mill')],
  brick='some',hours=''),

N('brick-hotel-georgetown','Brick Hotel','Georgetown','de','hotel','standing',38.68953,-75.38622,'exact','view','drive','hotels','1836',
  'Built in 1836 as a hotel on The Circle in Georgetown. In 1955 it was altered and became a bank, in 2008 it became a hotel again, and on August 28, 2021 the hotel closed for good and the building was leased for office space.',
  'A seven-bay brick building of two and a half storeys in a Federal and Greek Revival style, with a slate roof, double end chimneys and a Greek Revival porch, and a one-storey kitchen wing at the back. Interior not checked.',
  'An 1836 hotel on the Georgetown Circle.',
  'On The Circle, the town square beside the Old Sussex County Courthouse. Now offices, not open to visitors as far as found; look from the square. Street parking round the Circle.',
  [W('Brick Hotel')],
  brick='yes',hours=''),
]

PIN_NOTES={
 'amstel-house-new-castle':'The ArcGIS address result for 2 East 4th Street and the OpenStreetMap point agree with the Register\'s point.',
 'st-georges-presbyterian-church':'The Register point, the map\'s own point for the church and OpenStreetMap agree.',
 'wilmington-friends-meetinghouse':'The ArcGIS result for 401 North West Street, a few metres from the Register point.',
 'clayton-railroad-station':'OpenStreetMap\'s point for the station; the Wikipedia article gives no coordinates.',
 'cow-marsh-old-school-baptist-church':'The Register point; the address search found only the village of Sandtown.',
 'mahon-river-light':'The Register\'s point lies in the water of the bay; the pin is moved about 50 m to the shore beside the pier, and marks the general area, not the tower.',
 'milton-historic-district':'The Register point for the district, in the middle of the old town.',
 'cannon-museum-milton':'The ArcGIS result for 210 Union Street.',
 'indian-mission-church-harbeson':'The ArcGIS address result for 22701 Indian Mission Road and OpenStreetMap agree.',
 'hearn-and-rawlins-mill-seaford':'The Register\'s point is in the pond; the pin is moved about 55 m to the buildings at the dam, where the map\'s search also puts the mill.',
 'brick-hotel-georgetown':'OpenStreetMap\'s point for The Brick Hotel, 18 The Circle.',
}
