# November 20, 2026: the South Fork of Long Island: the Town of East Hampton (East Hampton village, Amagansett, Springs,
# Northwest Harbor, Montauk), Sag Harbor and Bridgehampton. Region drawn at random by tools/choose.py --state ny (nyc);
# tools/start.py showed no Atlas place within 25 km of East Hampton or Sag Harbor.
# Sources read in this session: Wikipedia articles and the Register lists for the towns of East Hampton and Southampton
# (tools/wiki_raw.py), and the pages of the bodies that run the places (NYS Parks, Suffolk County Parks, the Village of
# East Hampton, the East Hampton Historical Society, the Sag Harbor Whaling and Historical Museum, Preservation Long
# Island, Old Whalers' Church, Stony Brook University's Pollock-Krasner House, the Amagansett Historical Association,
# southamptontrails.org), and local news (The East Hampton Star, Patch, aaqeastend.com), all read with tools/page.py.
# montauklighthouse.com would not open to any tool, and montaukhistoricalsociety.org was read once by the web fetch tool.
from data_b import N
from data_ma import W
BATCH={'key':'nyc_xrml','label':'Long Island: East Hampton, Montauk and Sag Harbor','added':'2026-11-20 13:41'}

VILLAGE='Street parking in East Hampton village; parking was not checked on the ground.'
SAG='Street parking and the village lots in Sag Harbor; parking was not checked on the ground.'
EHHS=['East Hampton Historical Society: visit us (events calendar)','https://easthamptonhistory.org/visit-us/']

PLACES=[
N('camp-hero-radar-tower-montauk','Camp Hero and the AN/FPS-35 radar tower','Montauk','nyc','fort','standing',41.06231,-71.87408,'exact','public','walk','','1942–1981',
  'The Army opened Camp Hero in 1942 as a coastal defence post disguised as a fishing village, with two batteries of two 16-inch guns (Batteries 112 and 113) and a battery of two 6-inch guns (Battery 216), each a large earth-covered concrete bunker. In the Cold War it became Montauk Air Force Station; its huge AN/FPS-35 long-range radar, with an antenna 126 feet across, is the only survivor of the 12 long-range radar stations Sperry built in the 1960s (Register list). Most of the base passed through the National Park Service to New York State, and Camp Hero State Park opened on September 18, 2002.',
  'The radar tower, a tall windowless block that the state has planned to turn into a World War II and Cold War museum (Wikipedia), seen from outside. Wikipedia says the casemates, gun emplacements and concrete fire control towers can still be seen; trail names on the map follow the batteries (the lot used here is on the Battery 113 Trail). Wikipedia says some parts round the old radar installations were kept closed off: keep to the open trails. The base is also the setting of the "Montauk Project" conspiracy books.',
  'The last of the giant Cold War radars, on the cliff at the end of Long Island.',
  'Camp Hero State Park (NYS Parks, 1898 Montauk Highway, 631-668-3781): open year round for picnicking, hiking, surfing and bird watching, sunrise to sunset; a vehicle fee of $8 is taken 8 a.m. to 4 p.m. on weekends in spring and fall and daily from May 23 to October 12, 2026; no swimming. Trails for hiking, biking and horseback riding; surf fishing with a park permit. The park runs guided history walks booked on Eventbrite (one on November 28, 2026) (NYS Parks page read November 2026).',
  [W('Camp Hero State Park'),W('AN/FPS-35'),['NYS Parks: Camp Hero State Park','https://parks.ny.gov/visit/state-parks/camp-hero-state-park']],
  th=[41.06327,-71.87186],thn='Lot on the Battery 113 Trail',brick='?',hours='Sunrise to sunset, all year; vehicle fee 8 a.m. to 4 p.m. daily May 23 to October 12, 2026, weekends in spring and fall'),

N('montauk-point-light','Montauk Point Lighthouse','Montauk','nyc','light','standing',41.0709,-71.85731,'exact','open','drive','','1796',
  'The first lighthouse built in New York State, authorised by Congress in April 1792 and put up between June 7 and November 5, 1796; keeper Jacob Hand first lit it in April 1797. It is the fourth-oldest active lighthouse in the United States and was made a National Historic Landmark in 2012. The tower was raised from its first 80 feet, given a first-order Fresnel lens and a new keeper\'s house (the 1796 house was pulled down), and got its brown stripe in 1899. The Army took it over in World War II; the Coast Guard thought of pulling it down in 1967, and it passed to the Montauk Historical Society, which opened the museum.',
  'The striped tower on Turtle Hill and the keeper\'s house, now the museum. Built 300 feet from the cliff edge, it now stands about 100 feet from it; the stone revetment and terracing below are the erosion works of 1998 and after, and the Army Corps of Engineers let a $30.7 million contract in 2020 to protect it (Wikipedia). Whether visitors may climb the tower was not checked.',
  'New York\'s first lighthouse, ordered under Washington, losing its race with the cliff.',
  'A private museum run by the Montauk Historical Society at 2000 Montauk Highway, next to but not part of Montauk Point State Park (Wikipedia). Its own site (montauklighthouse.com) would not open to any tool, so its hours and fees were not checked. Park in the Montauk Point State Park lot at the end of the parkway: NYS Parks says the park is open all year, sunrise to sunset, with a fee collected 8 a.m. to 4 p.m. daily from May 23 to October 12, 2026.',
  [W('Montauk Point Light'),['NYS Parks: Montauk Point State Park','https://parks.ny.gov/visit/state-parks/montauk-point-state-park']],
  th=[41.07152,-71.85977],thn='Montauk Point State Park lot',brick='some',hours='?'),

N('shadmoor-bunkers-montauk','World War II bunkers at Shadmoor State Park','Montauk','nyc','fort','standing',41.0385,-71.92786,'site','public','walk','','1940s',
  'Shadmoor is a 99-acre state park of bluffs, heath and wetland a quarter mile east of Montauk village. Two concrete bunkers built during World War II, once armed to guard the coast against invasion, still stand on it (NYS Parks). Wikipedia\'s Montauk Point Light article says concrete fire control towers like Camp Hero\'s are also at Shadmoor.',
  'Two concrete bunkers on the bluff top, reached by the park\'s trails; the park also has viewing platforms and two stairways down to 2,400 feet of ocean beach. The pin is on one of them as the aerial and LiDAR show it (see the pin note); the other was not placed.',
  '',
  'Shadmoor State Park (NYS Parks): open all year, seven days a week; no parking fee. Hiking trails; check the park\'s trail map for the bunkers. Parking was not checked on the ground.',
  [['NYS Parks: Shadmoor State Park','https://parks.ny.gov/visit/state-parks/shadmoor-state-park'],W('Montauk Point Light')],
  brick='?',hours='Open all year, every day'),

N('second-house-museum-montauk','Second House','Montauk','nyc','landmark','standing',41.03145,-71.95274,'site','open','drive','','1746; rebuilt 1797',
  'When Montauk was the town\'s common pasture, Second House was built in 1746 for the keeper who watched sheep to the west and cattle to the east; after a fire it was raised again in 1797, the town putting up "three gallons of rum to raise the house at Fort Pond". It was altered in 1879, 1880 and 1912. The town and the state bought it in 1968 from the Kennedy family, who had used it as a summer house, and it opened as a museum in 1969, but it was shut for more than a decade before a three-phase restoration finished in spring 2025 (East Hampton Star).',
  'A shingled farmhouse looking over Kirk Park and Fort Pond. The Montauk Historical Society says the town restored the outside to how it looked in 1886. Interior not checked; a photography exhibition was to open in it on May 23, 2025.',
  '',
  'Owned by the Town of East Hampton and run as a museum by the Montauk Historical Society, on Montauk Highway at Second House Road. Its 2026 opening days were not found: the society\'s home page still spoke of reopening in 2023. Parking was not checked.',
  [['East Hampton Star: Second House restoration done at last (April 2025)','https://www.easthamptonstar.com/villages/2025417/second-house-restoration-done-last'],['Montauk Historical Society','https://montaukhistoricalsociety.org/']],
  brick='?',hours='?'),

N('hook-windmill-east-hampton','Hook Windmill (Old Hook Mill)','East Hampton','nyc','industry','standing',40.96603,-72.1834,'exact','open','walk','','1806–1908',
  'A smock windmill built in 1806 by the East Hampton craftsman Nathaniel Dominy V, replacing a post mill of about 1740 on the same spot and reusing its 24-inch centre post. It ground grain regularly until 1908 and was sold to the town in 1922; Charles Dominy put it back in working order for the village in 1939. Wikipedia counts it among the most complete of Long Island\'s surviving windmills. After two summers shut it reopened restored in June 2012 (Patch).',
  'The mill on the green at the north end of North Main Street, with its gearing inside: Patch says the 2012 restoration put back the interior floors and parts, and tours were then given inside. Wikipedia says it is open daily to visitors.',
  '',
  'Owned by the Village of East Hampton (the village historian runs its windmills). Patch gave the 2012 hours (weekends in June, every day in July and August, $2 adults) but no current page for the mill was found, so today\'s hours were not checked. '+VILLAGE,
  [W('Hook Windmill'),['Patch: newly restored Hook Mill reopens (2012)','https://patch.com/new-york/easthampton/newly-restored-hook-mill-reopens-friday']],
  brick='?',hours='?'),

N('home-sweet-home-pantigo-windmill-east-hampton','Home Sweet Home and the Pantigo Windmill','East Hampton','nyc','landmark','standing',40.95666,-72.19105,'exact','open','walk','','early 1700s',
  'A saltbox house of the early 1700s on James Lane, the most distinguished lean-to house in East Hampton (Village of East Hampton), lived in by the family of John Howard Payne, who wrote the words of "Home, Sweet Home". Behind it stands the Pantigo Windmill, an octagonal smock mill begun in March 1804 by Samuel Schellinger for Huntting Miller on Mill Hill, the third mill on that spot, with a 1771 weathervane on top; the East Hampton Star calls it thrice moved. The village runs house and mill as a museum.',
  'The shingled saltbox and, behind it, the smock mill with its sails. Interior not checked.',
  '',
  'Owned and run by the Village of East Hampton at 14 James Lane. The village page gives the hours: January to April by appointment, daily May to September 10 a.m. to 4 p.m. and Sundays 1 to 4 p.m., and weekends only in October. '+VILLAGE,
  [['Village of East Hampton: Home Sweet Home','https://easthamptonvillage.gov/home-sweet-home/'],W('Pantigo Windmill'),W('Mulford Farmhouse')],
  brick='?',hours='May to September daily 10 a.m. to 4 p.m. (Sundays 1 to 4 p.m.); October weekends; January to April by appointment'),

N('mulford-farm-east-hampton','Mulford Farm','East Hampton','nyc','landmark','standing',40.95702,-72.19121,'site','open','walk','','1680',
  'An English colonial farmstead on the village green: the farmhouse was built in 1680 by Josiah Hobart, high sheriff under the first royal government of New York, and Samuel "Fish Hook" Mulford bought it in 1712 and built the barn in 1721. The East Hampton Historical Society owns it and shows it as it was in 1790, a living museum with the house, barn, spinning house, privy, smokehouse and garden (Wikipedia). The farmhouse has just been through a full restoration of its interior (the society).',
  'The farmhouse and 1721 barn next door to Home Sweet Home. The society calls the restoration of the farmhouse interior comprehensive; what original fabric it kept was not checked.',
  '',
  'East Hampton Historical Society, 10 James Lane. Wikipedia says it is open from Memorial Day weekend to Columbus Day weekend; the society\'s calendar (read November 2026) listed open days on Sunday, November 1 and Saturday, November 14, 11 a.m. to 4 p.m. '+VILLAGE,
  [W('Mulford Farmhouse'),EHHS],
  brick='?',hours='Memorial Day to Columbus Day weekends (Wikipedia); other open days on the society calendar, 11 a.m. to 4 p.m.'),

N('gardiner-windmill-east-hampton','Gardiner Windmill','East Hampton','nyc','industry','standing',40.95526,-72.19187,'site','view','walk','','1804–1900',
  'Built by Nathaniel Dominy V for John Lyon Gardiner, seventh proprietor of Gardiners Island, and others, from timber cut on Gardiners Island, and finished on September 28, 1804 at a cost of more than 528 pounds. It stands where it was built, on the east side of Town Pond on James Lane, and ground until 1900 (aaqeastend.com, quoting the village). The town bought the mill and its lot in 2014, and the village rebuilt the mill cottage beside it as a museum of Hamptons landscape painting (Wikipedia).',
  'The smock mill on its original site, seen from James Lane and from the South End Burying Ground across the road. The mill cottage beside it is a replica of 2014 and after, not the old house. Interior of the mill not checked.',
  '',
  'Town-owned lot on James Lane; the mill cottage museum beside it is run by the village. No page giving visiting hours for the mill was found, so it is marked view from the road. '+VILLAGE,
  [['aaqeastend.com: Gardiner Mill, 1804','https://aaqeastend.com/contents/landmarks/gardiner-mill-1804-east-hampton/'],['Village of East Hampton: historic services','https://easthamptonvillage.org/departments/historic-services'],W('John Lyon Gardiner Mill Cottage')],
  brick='?'),

N('clinton-academy-town-house-east-hampton','Clinton Academy and the Town House','East Hampton','nyc','civic','standing',40.9585,-72.19066,'exact','open','walk','','1784',
  'Clinton Academy, built in 1784 with money from townspeople, was one of the first academies chartered by the New York Board of Regents; it was named for Governor George Clinton, who gave the bell in its cupola, and it prepared boys for college, the sea or surveying and taught girls separately. It was enlarged in 1886 as Clinton Hall. Beside it is the Town House, where the town trustees met, and the oldest one-room schoolhouse left on Long Island (East Hampton Historical Society).',
  'The academy on Main Street, now the historical society\'s exhibition building, with the Mimi Meehan native plant garden behind it (open in daylight through the gate left of the porch); and the small Town House next door. Interior not checked.',
  '',
  'East Hampton Historical Society, 151 Main Street. Exhibit hours vary and are on the society\'s calendar; the Town House opens on its Main Street walking tours, May to November. '+VILLAGE,
  [['East Hampton Historical Society: Clinton Academy','https://easthamptonhistory.org/clinton-academy/'],EHHS],
  brick='?',hours='Exhibit days on the society calendar; garden in daylight; Town House on walking tours May to November'),

N('thomas-moran-house-east-hampton','Thomas and Mary Nimmo Moran House and Studio','East Hampton','nyc','landmark','standing',40.95396,-72.19437,'exact','open','walk','','1884',
  'Built in 1884 by the painter Thomas Moran, largely of reused materials, as home and studio for himself and his wife, the etcher Mary Nimmo Moran; Moran was the first major painter to bring scenes of the American West to the rest of the country, and it was their home until his death in 1926. It was made a National Historic Landmark in 1965. Left in 2004 to Guild Hall after falling into disrepair, it has been restored and opened by reservation under the East Hampton Historical Society (Wikipedia).',
  'An eclectic two-storey frame house on Main Street; the front is taken up by Moran\'s studio, a large room with 20-foot ceilings, which visitors see on the tours. The Morans are buried in the South End Cemetery by Town Pond.',
  '',
  'East Hampton Historical Society, 229 Main Street, by reservation: guided tours on set dates on the society\'s calendar (November 7 and 22 in 2026). '+VILLAGE,
  [W('Thomas Moran House'),EHHS],
  brick='?',hours='Guided tours by reservation on dates on the society calendar'),

N('east-hampton-station','East Hampton railroad station','East Hampton','nyc','rail','standing',40.96494,-72.19346,'exact','public','walk','','1895',
  'Built in 1895 by the Brooklyn and Montauk Railroad on what became the Long Island Rail Road\'s Montauk Branch. The original station house still stands and is still in use; it was put on the National Register in 2000, and in 2017 the MTA announced it would restore it to its original brick and green roofline; Wikipedia shows it after the work (Wikipedia).',
  'The station house on Railroad Avenue between Newtown Lane and Race Lane, with its canopies, beside one high-level platform.',
  '',
  'A working Long Island Rail Road station: parking along Railroad Avenue (Wikipedia). Keep off the track.',
  [W('East Hampton station')],
  brick='yes'),

N('miss-amelias-cottage-amagansett','Miss Amelia\'s Cottage','Amagansett','nyc','landmark','standing',40.97405,-72.14379,'exact','open','walk','','1725',
  'A small house built in 1725 for Catherine Schellinger about 300 yards west of where it stands, up the hill, and towed down on a plank road by two teams of oxen in 1794 (East Hampton Star, quoting the association). Thirty Schellinger children are thought to have been born in it; the last, Mary Amelia Schellinger, born there in 1841, lived in it until about 1929. The Amagansett Historical Association was founded in 1964 to save it from a planned supermarket and parking lot.',
  'The cottage, a museum of three centuries of family life in Amagansett, and on the same ground the Roy Lester Carriage House and the 1850 Lester Barn. Interior not checked.',
  '',
  'Amagansett Historical Association, 129 Main Street (631-267-3020); its site gives no visiting hours, so they were not checked.',
  [W('Amelia Cottage Museum'),['Amagansett Historical Association','https://amagansetthistory.org/'],['East Hampton Star: the little cottage\'s 300th (2025)','https://www.easthamptonstar.com/villages/2025724/little-cottages-300th']],
  brick='?',hours='?'),

N('pollock-krasner-house-springs','Pollock-Krasner House and Studio','Springs','nyc','landmark','standing',41.02384,-72.1549,'exact','open','drive','','1945–1984',
  'The wood-frame house on Accabonac Creek where the painters Jackson Pollock and Lee Krasner lived from November 1945 until their deaths in 1956 and 1984; they bought it for $5,000. In 1946 Pollock moved the barn to open the view and made it his studio. After Krasner\'s death it went to the Stony Brook Foundation, and conservators lifting the Masonite boards Pollock laid in 1953 found the barn floor beneath covered in his paint (Wikipedia).',
  'The house and the studio barn with its paint-spattered floor. Visitors may tour both on guided or audio-guided visits.',
  'Pollock\'s drips are still on the studio floor.',
  'Run by Stony Brook University at 830 Springs Fireplace Road: guided and self-guided tours Thursday to Sunday, May to October, at 12, 2 and 4 p.m. (its page, read November 2026). Parking was not checked.',
  [W('Pollock-Krasner House and Study Center'),['Stony Brook University: Pollock-Krasner House','https://www.stonybrook.edu/pkhouse/']],
  brick='?',hours='May to October, Thursday to Sunday, tours at 12, 2 and 4 p.m.'),

N('cedar-island-light-east-hampton','Cedar Island (Cedar Point) Lighthouse','Northwest Harbor','nyc','light','standing',41.04081,-72.26097,'exact','public','hike','','1839; tower 1860',
  'A granite lighthouse in the Italianate style that guided whaling ships in and out of Sag Harbor. Suffolk County dates it to 1860 and says it stood on an island 200 yards offshore until the hurricane of 1938 shifted the sand into the strip that now joins it to the mainland; Wikipedia files it among lighthouses completed in 1839: the two dates are not reconciled here. It was decommissioned in 1934 and replaced by an automatic light on a steel skeleton on the breakwater.',
  'The granite tower and keeper\'s house at the tip of Cedar Point, over Gardiners Bay, reached along the sand spit from the park. Interior not checked.',
  '',
  'Cedar Point County Park (Suffolk County Parks, 5 Cedar Point Road, 631-852-7620): camping, trails and beach; the park\'s hours were not on its page. The lighthouse is about 1.8 km in a straight line from the park lot used here (measured on the map), along the shore; vehicles on the outer beach need a county permit.',
  [W('Cedar Island Light'),['Suffolk County Parks: Cedar Point County Park','https://www.suffolkcountyny.gov/Departments/Parks/Our-Parks/Cedar-Point-County-Park']],
  th=[41.03986,-72.23931],thn='Cedar Point County Park lot, Cedar Point Road',conf='mixed',brick='?'),

N('old-whalers-church-sag-harbor','Old Whalers\' Church (First Presbyterian)','Sag Harbor','nyc','worship','standing',40.99734,-72.29369,'exact','open','walk','','1844',
  'Built in 1844 to designs by Minard Lafever, the most important surviving Egyptian Revival building in the United States, by the accounts Wikipedia gathers. Its 185-foot steeple made it the tallest building on Long Island until the hurricane of 1938 blew it down; it has not been put back. A National Historic Landmark since 1994, the only one in Sag Harbor.',
  'The façade rises like the pylons of an Egyptian temple, with a cornice crested with carved blubber spades for the whaling money that built it. Inside, by Wikipedia: an ornate Greek Revival sanctuary, a pulpit framed by Corinthian columns rising over 50 feet to a coffered ceiling hung from a central beam, and box pews with Cuban mahogany rails.',
  'An Egyptian temple paid for by whale oil.',
  'An active Presbyterian church at 44 Union Street; its page says all are welcome at worship on Sundays at 10 a.m., with a ramp and a lift to the sanctuary. '+SAG,
  [W("Old Whaler's Church (Sag Harbor)"),['Old Whalers\' Church','https://oldwhalerschurch.org/']],
  brick='?',hours='Worship Sundays 10 a.m.'),

N('sag-harbor-whaling-museum','Sag Harbor Whaling and Historical Museum (Benjamin Huntting House)','Sag Harbor','nyc','landmark','standing',40.99766,-72.29724,'exact','open','walk','','1845',
  'A Greek Revival mansion built in 1845 for the whaling merchant Benjamin Huntting II to designs by Minard Lafever, which the AIA guide calls Long Island\'s finest high-style Greek Revival building. Margaret Olivia Sage summered in it from 1907 to 1918; it became a Masonic temple in 1920 (the Masons still use the upper floor), and has been the whaling museum since 1945 (Wikipedia).',
  'A temple-front portico with fluted Corinthian columns, the roof edged with carved flensing knives and blubber spades, and a pair of whale jawbones framing the front door; inside, a staircase spirals up to a domed skylight. The museum holds the largest collection of whaling gear in New York.',
  '',
  'Run by the museum at 200 Main Street. Its visit page gives the 2026 season: April 18 to May 3 weekends, May 4 to October 4 Tuesday to Sunday, October 5 to 25 weekends, all 10 a.m. to 4 p.m. '+SAG,
  [W('Sag Harbor Whaling Museum'),['Sag Harbor Whaling Museum: visit','https://www.sagharborwhalingmuseum.org/visit']],
  brick='?',hours='Mid-April to late October: May 4 to October 4 Tuesday to Sunday 10 a.m. to 4 p.m.; weekends only before and after'),

N('custom-house-sag-harbor','Sag Harbor Custom House','Sag Harbor','nyc','landmark','standing',40.99823,-72.29749,'exact','open','walk','','c. 1770',
  'A house of about 1770, home and office of Henry Packer Dering (1763–1822), Sag Harbor\'s first customs collector and postmaster after the port became a federal port of entry in 1789; the south side held his custom room and, in a lean-to, the post office. It stood at Union and Church streets until the Old Sagg-Harbour Committee moved it to Main Street in 1948 to save it from demolition, and Preservation Long Island has owned it since 1966.',
  'A shingled house shown as the Dering family\'s home and office, with the custom room. Interior shown on tours; which fittings are original was not checked.',
  '',
  'Preservation Long Island, 192 Main Street, next to the whaling museum. House tours seasonally (its public tours run June to mid-October); no 2026 dates for this house were on its tours page. Private tours $12 a head, $120 minimum. '+SAG,
  [W('Custom House (Sag Harbor, New York)'),['Preservation Long Island: Custom House','https://preservationlongisland.org/custom-house/'],['Preservation Long Island: tours','https://preservationlongisland.org/tours/']],
  brick='?',hours='Seasonal tours, June to mid-October (dates on Preservation Long Island\'s tours page)'),

N('round-pond-ice-house-sag-harbor-spur','Round Pond ice house site and the Sag Harbor rail spur','Sag Harbor','nyc','industry','traces',40.98159,-72.29336,'site','public','hike','','1870–1939',
  'An ice house worked Round Pond for about 70 years, and a 1,400-foot siding was laid to it from the railroad spur that ran from Bridgehampton station to Sag Harbor\'s Long Wharf between 1870 and 1939, so the ice could go by rail to New York City (southamptontrails.org). The spur\'s bed is now the main trail through the Long Pond Greenbelt.',
  'The wide, sandy old railroad bed through the woods, and near Round Pond the remains that OpenStreetMap maps as the ice house ruins beside the "LIRR Ice House Spur". No source opened describes what is left of the ice house itself: not checked on the ground.',
  '',
  'Long Pond Greenbelt, county and village land with trails. southamptontrails.org gives the way in from Mashashimuet Park on the Bridgehampton–Sag Harbor Turnpike: south past the tennis courts between the athletic field and the railroad bed. The lot used here is on the Old Railroad at the park end.',
  [['Southampton Trails Preservation Society: Long Pond Greenbelt','https://southamptontrails.org/long-pond-greenbelt/'],['Dan\'s Papers: get to know the Long Pond Greenbelt (2017)','https://www.danspapers.com/2017/09/get-long-pond-greenbelt']],
  th=[40.98929,-72.29797],thn='Lot on the old railroad bed by Mashashimuet Park',conf='mixed',brick='?'),

N('beebe-windmill-bridgehampton','Beebe Windmill','Bridgehampton','nyc','industry','standing',40.9343,-72.3006,'site','view','drive','','1820',
  'Built in 1820 on the wharf at Sag Harbor for Lester Beebe, then moved to Sherrill\'s Hill, where it also signalled arriving whaleships; Rose Gelston moved it to Bridgehampton, where it worked for more than 50 years. It was moved twice more by the railroad in the 1880s, repaired by Nathaniel Dominy VII in 1888, ground for the Bridgehampton Milling Company until 1915, and was then taken to John E. Berwind\'s summer estate (Wikipedia).',
  'A smock mill at the southeast corner of Ocean Road and Hildreth Avenue. The Historic American Engineering Record called it one of the first Long Island mills with a fly, regulators and cast-iron gears, and the only one keeping the originals, and the only one with a decorative design. Interior not checked.',
  '',
  'Who owns it now and whether it ever opens was not found in the sources read: look from Ocean Road. Parking was not checked.',
  [W('Beebe Windmill')],
  brick='?'),
]

PIN_NOTES={
 'camp-hero-radar-tower-montauk':'OpenStreetMap building tagged as the Camp Hero radar tower; the lot is the mapped one on the Battery 113 Trail (tools/parking.py).',
 'montauk-point-light':'OpenStreetMap point for the lighthouse (tools/nom.py), matching Wikipedia within 20 m; lot from tools/parking.py.',
 'shadmoor-bunkers-montauk':'Started at the middle of the park (tools/nom.py); moved 50 m with tools/pix.py onto a small square structure beside the trail that the LiDAR shows as a squared mound, taken to be one of the two bunkers (not confirmed by a source).',
 'second-house-museum-montauk':'ArcGIS geocoder point of interest "Second House Museum" on Montauk Highway.',
 'hook-windmill-east-hampton':'The Register list point fell on North Main Street; moved 60 m with tools/pix.py onto the small tall building with a long shadow on the green, taken to be the mill, on the leaf-off aerial.',
 'home-sweet-home-pantigo-windmill-east-hampton':'OpenStreetMap museum point for Home, Sweet Home Museum, 12 James Lane (tools/nom.py); the windmill is behind the house.',
 'mulford-farm-east-hampton':'ArcGIS street-address match for 10 James Lane (not a rooftop point).',
 'gardiner-windmill-east-hampton':'OpenStreetMap building for the John Lyon Gardiner Mill Cottage; the mill stands on the same lot.',
 'clinton-academy-town-house-east-hampton':'ArcGIS PointAddress for 151 Main Street, East Hampton.',
 'thomas-moran-house-east-hampton':'ArcGIS PointAddress for 229 Main Street, East Hampton.',
 'east-hampton-station':'Wikipedia coordinate for the station.',
 'miss-amelias-cottage-amagansett':'ArcGIS PointAddress for 129 Main Street, Amagansett, the association\'s address.',
 'pollock-krasner-house-springs':'ArcGIS PointAddress for 830 Springs Fireplace Road, the address on Stony Brook\'s page.',
 'cedar-island-light-east-hampton':'Wikipedia coordinate for the lighthouse; lot is the mapped Cedar Point County Park lot (tools/parking.py).',
 'old-whalers-church-sag-harbor':'ArcGIS PointAddress for 44 Union Street, Sag Harbor.',
 'sag-harbor-whaling-museum':'OpenStreetMap museum point at 200 Main Street (tools/nom.py).',
 'custom-house-sag-harbor':'OpenStreetMap museum point for the Custom House (tools/nom.py).',
 'round-pond-ice-house-sag-harbor-spur':'OpenStreetMap mapped ruin "Ice House (ruins)" from the Atlas leads layer; the LiDAR shows a raised bed (the siding) running down to the pond shore and low banks at the pin. The lot is the mapped one on the old railroad bed by Mashashimuet Park.',
 'beebe-windmill-bridgehampton':'Wikipedia coordinate for Beebe Windmill.',
}
