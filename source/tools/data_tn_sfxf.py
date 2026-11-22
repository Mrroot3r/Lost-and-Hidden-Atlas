# November 22, 2026: Tennessee, a first statewide scatter (the state had 21 places, all but two on the northern
# Cumberland Plateau): iron furnace, mill and tunnel ruins on the Western Highland Rim, Native earthworks at Pinson
# and Manchester, Civil War sites at Fort Pillow and Dover, and frontier houses and inns from Memphis to the
# Virginia line.
# Facts from the linked sources only, read in this session: National Register nomination forms (NPGallery text
# layers), Wikipedia, HMdb markers and the managing bodies' own pages (Tennessee State Parks, the Tennessee Historical
# Commission, the National Park Service and the museums' own sites). Where sources disagree the text gives both and
# conf='mixed'. West and Middle Tennessee keep Central time, East Tennessee Eastern time.
from data_b import N
from data_ma import W

def NR(ref, label='National Register nomination form'):
    return [label, 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text' % ref]

def TSP(slug, label):
    return [label + ' (Tennessee State Parks)', 'https://tnstateparks.com/parks/' + slug]

def THC(slug, label):
    return [label + ' (Tennessee Historical Commission)', 'https://www.tn.gov/historicalcommission/state-programs/state-historic-sites/' + slug + '.html']

BATCH = {'key': 'tn_sfxf', 'label': 'Tennessee: furnaces, mounds, forts and frontier houses', 'added': '2026-11-22 00:25'}

PLACES = [
# ---- West Tennessee ----
N('fort-pillow-earthworks', 'Fort Pillow', 'Henning', 'tn', 'fort', 'traces', 35.63611, -89.84222, 'area', 'public', 'hike', 'forts', '1861',
  'Confederate troops built extensive earthworks on the Chickasaw Bluffs above the Mississippi in 1861 and named the post for General Gideon Pillow. They left it in June 1862 and the Union Army held it for most of the war. On April 12, 1864 Confederate troops under Nathan Bedford Forrest took the fort, and the battle ended in a massacre of Black Union soldiers and their white officers as they tried to surrender.',
  'The remains of the earthworks, and a restored fortification reached on foot, with an overlook above the river and a museum in the visitor centre (state park page). The park page warns that the bluff edges can be unstable.',
  'The bluff where a Civil War battle ended in a massacre of surrendering Black soldiers.',
  'Fort Pillow State Historic Park, run by Tennessee State Parks: visitor centre and museum at 3122 Park Road, Henning. Hours from the park\'s page, read November 22, 2026. Park at the visitor centre lot; the trail goes on to the earthworks.',
  [TSP('fort-pillow', 'Fort Pillow State Historic Park'), W('Fort Pillow State Historic Park'), W('Battle of Fort Pillow')],
  th=[35.63387, -89.84034], thn='Visitor centre lot on Park Road', brick='no', hours='Visitor centre and museum daily 8 a.m. to 4 p.m. Central; closed Thanksgiving and Christmas Day'),
N('pinson-mounds-sauls-mound', 'Pinson Mounds and Sauls\' Mound', 'Pinson', 'tn', 'burial', 'traces', 35.49535, -88.68255, 'exact', 'public', 'walk', '', 'c. 1–500',
  'A Middle Woodland complex of at least 17 mounds built by Native people, most probably between 100 and 300 AD, with an earthen geometric enclosure and living areas over about 400 acres above the South Fork of the Forked Deer River. It is the largest group of Middle Woodland mounds in the United States. Excavations from 1961 on found burials, a cremation pit and, in the Twin Mounds, tombs with copper-adorned headdresses.',
  'Sauls\' Mound, 72 feet high and the second-highest surviving mound in the country, the Twin Mounds and smaller rises along paved trails, and a museum built to fit the landscape (state park page). A burial and ceremonial ground: keep to the trails.',
  'The largest group of Middle Woodland mounds in the country.',
  'Pinson Mounds State Archaeological Park, run by Tennessee State Parks, 460 Ozier Road. Hours from the park\'s page, read November 22, 2026.',
  [TSP('pinson-mounds', 'Pinson Mounds State Archaeological Park'), W('Pinson Mounds')],
  th=[35.50023, -88.67669], thn='Mapped lot by the museum, Pinson Mound Road', brick='no', hours='Park 7 a.m. to 7 p.m. Mar 16 to Oct 31, 7 a.m. to 5 p.m. Nov 1 to Mar 15; museum Mon to Sat 8 to 4:30, Sun 1 to 4:30 (Central)'),
N('woodruff-fontaine-house', 'Woodruff-Fontaine House', 'Memphis', 'tn', 'landmark', 'standing', 35.14492, -90.03786, 'exact', 'open', 'drive', '', '1871',
  'Built in 1871 on Adams Avenue, the street then known as Millionaire\'s Row, to plans by the firm of Edward C. Jones and Matthias H. Baldwin. It stood empty for many years until the Association for the Preservation of Tennessee Antiquities bought and restored it in 1962. It is listed with the James Lee House next door and is in the Victorian Village district.',
  'A house of hand-made brick. The 1971 Register form describes a long parlour with a restored fresco ceiling and twin marble mantels, an octagonal dining room, carved cornices under 16-foot ceilings, plaster arabesques, parquet floors in some rooms and a fireplace in every room. Shown by tour; the interior today was not checked.',
  '', 'Run as a museum by the Memphis chapter of the Association for the Preservation of Tennessee Antiquities, 680 Adams Avenue. Its page, read November 22, 2026, said it was closed November 11 to 29 to decorate for its Yuletide exhibit and would reopen for tours on Wednesday, December 2 at noon; it gave no regular hours. Parking not checked.',
  [['Woodruff-Fontaine House Museum', 'https://www.woodruff-fontaine.org/'], NR('71000835', 'Lee and Fontaine Houses Register form (1971)'), W('Woodruff-Fontaine House')],
  brick='?', hours='?'),
# ---- Western Highland Rim and the lower Cumberland ----
N('great-western-furnace', 'Great Western Iron Furnace', 'Dover', 'tn', 'industry', 'ruins', 36.64064, -87.97555, 'exact', 'public', 'drive', '', '1854–1856',
  'A charcoal iron furnace built in 1854 near the later village of Model, one of eighteen iron works in Stewart County. It ran for a single 34-week blast in 1855 and 1856 and made 1,350 tons of iron, then closed. The marker blames debt, mismanagement, scarce ore and a national recession; a history of the Land Between the Rivers quoted by TNGenWeb gives lack of ore and an uprising by the enslaved furnace crew. The owners\' sale notice of December 1856 listed eighty enslaved furnace hands.',
  'The stack, of large limestone blocks with a fire-brick core, 43 feet across at the base. The 1975 Register form found it unaltered and well preserved because it ran so briefly, with nothing left of the wooden casting house or the charging bridge. Interpretive markers stand by it.',
  'A furnace stack that made iron for 34 weeks.',
  'In Land Between the Lakes National Recreation Area, beside The Trace (the road through it); the marker\'s page shows it at a pull-off. No hours found for the furnace site; who manages the ground today and the parking were not checked on a managing body\'s page.',
  [['HMdb: Great Western Furnace', 'https://www.hmdb.org/m.asp?m=136753'], NR('75001790', 'Great Western Furnace Register form (1975)'), ['TNGenWeb Stewart County: Great Western Furnace', 'https://tngenweb.org/stewart/GW.htm']],
  conf='mixed', brick='no'),
N('dover-hotel-surrender-house', 'Dover Hotel (Surrender House)', 'Dover', 'tn', 'hotel', 'standing', 36.48896, -87.83651, 'exact', 'open', 'drive', '', '1851–1853',
  'A two-storey riverside tavern built between 1851 and 1853 on Petty Street, the first building riverboat travellers saw at the landing. In February 1862 it was General Simon Buckner\'s headquarters, and on the morning of February 16 he surrendered Fort Donelson there to Ulysses S. Grant. It later served as a hospital and a hotel again; a local association saved it from demolition in 1927, opened it as a museum in 1930 and gave it to the National Park Service in 1959.',
  'The Park Service says only about a fifth of the building is original (floor sleepers, most of the frame, the foundation and one chimney), after a 1970s restoration. A 2005 Commons photograph shows a white weatherboarded two-storey building with double porches and red brick end chimneys. One room is open, with exhibits and a short film; the top floor and basement are not restored or open. Waysides outside.',
  'The tavern where Grant took the surrender of Fort Donelson.',
  'Part of Fort Donelson National Battlefield (National Park Service). Hours from the park\'s hours page, read November 22, 2026; weather and short staffing can delay opening. No public restrooms at the hotel. The Park Service lists parking for cars and buses.',
  [['Fort Donelson: hours', 'https://www.nps.gov/fodo/planyourvisit/hours.htm'], ['NPS: Dover Hotel (Surrender House)', 'https://www.nps.gov/places/dover-hotel-surrender-house-tour-stop-10.htm'], ['NPS Dover Hotel brochure (PDF)', 'https://www.nps.gov/fodo/planyourvisit/upload/Dover-Hotel-Brochure-2008_Accessible.pdf'], ['HMdb: Dover Hotel', 'https://www.hmdb.org/m.asp?m=38766'], W('Fort Donelson National Battlefield')],
  brick='some', hours='Exhibit room daily 8:30 a.m. to 4 p.m. Central'),
N('montgomery-bell-tunnel', 'Montgomery Bell Tunnel (Pattison Forge)', 'Kingston Springs', 'tn', 'industry', 'standing', 36.14681, -87.12205, 'exact', 'public', 'walk', '', '1818–1819',
  'Montgomery Bell bought land at the Narrows of the Harpeth in 1818 and had a 290-foot tunnel cut through the limestone neck of a river bend, to use a 16-foot drop in the river to power an iron works he called Pattison Forge. It is thought to be the first full-size tunnel in the United States. The dam, race, forge and Bell\'s house are gone. Wikipedia gives the tunnel as built in 1819 and, in its park article, created in 1818.',
  'The unlined tunnel, about 8 feet high and 15 wide, with a 35-foot-wide entrance portal (National Historic Landmark description as summed up by Wikipedia). A fire in driftwood in 2011 damaged it and the road above, and both were stabilised. The park forbids swimming and climbing on the rocks at Pattison Forge and the tunnel pool.',
  'The first full-size tunnel in the country, cut for an iron forge.',
  'In Harpeth River State Park (Tennessee State Parks); the park lists its Narrows of the Harpeth access at 1254 Narrows of the Harpeth Road, Kingston Springs. No mapped lot was found within 3 km of the tunnel, and the address point falls in woods, so the parking was not settled from here. Park hours not found on its page.',
  [TSP('harpeth-river', 'Harpeth River State Park'), W('Montgomery Bell Tunnel'), W('Harpeth River State Park')],
  conf='mixed', brick='no'),
# ---- Middle Tennessee ----
N('cragfont-castalian-springs', 'Cragfont', 'Castalian Springs', 'tn', 'landmark', 'standing', 36.40507, -86.34183, 'exact', 'open', 'drive', '', '1798–1802',
  'The house of General James Winchester, Revolutionary War officer, War of 1812 general and a founder of Memphis, begun in 1798 and finished in 1802 by craftsmen from Maryland. The state calls it the finest mansion on the Tennessee frontier. It is named for the rocky bluff it stands on and the spring at its foot.',
  'A grey stone Georgian front with a wide stone chimney at each gable end (1970 Register form). Inside, Federal furniture, some of it the Winchesters\' own, and a weaving room in the basement (Tennessee Historical Commission). Guided tours.',
  '', 'A Tennessee State Historic Site, 200 Cragfont Road. Hours from the Tennessee Historical Commission\'s page, read November 22, 2026; it asks visitors to call first. Parking not checked.',
  [THC('cragfont', 'Cragfont State Historic Site'), NR('70000618', 'Cragfont Register form'), W('Cragfont')],
  brick='no', hours='April to mid-November: Thursday to Sunday 9:30 a.m. to 4:30 p.m., tours at 10, 12 and 2; winter: call (Central)'),
N('great-falls-cotton-mill', 'Great Falls Cotton Mill', 'Rock Island', 'tn', 'industry', 'standing', 35.80346, -85.6273, 'site', 'public', 'drive', '', '1892–1902',
  'Asa Faulkner planned a cotton mill at the Great Falls of the Caney Fork before his death in 1886, and his partners built it in 1892, with a mill village called Falls City. A flood in July 1902 swept away its wheelhouse and the mill was given up soon after. The gorge was later dammed for power (1917), and the mill now stands in Rock Island State Park, which calls it the Falls City Cotton Mill.',
  'A three-storey red brick mill on a stone foundation, five bays by eighteen, with segmental-arched windows. The 1982 Register form found it little changed except for the lost wheelhouse and walkway, the collapsed machine shop (1973) and missing window glass. Seen from the park road beside it; the interior is not open as far as the park page says.',
  'An 1892 brick cotton mill left on the bluff after a flood took its wheel.',
  'Rock Island State Park (Tennessee State Parks), 82 Beach Road. The park warns that the TVA dam and powerhouse can release water without warning and that the gorge below the dam is closed when it spills.',
  [TSP('rock-island', 'Rock Island State Park'), NR('82004063', 'Great Falls Cotton Mill Register form (1982)'), W('Rock Island State Park (Tennessee)')],
  th=[35.80368, -85.62830], thn='Mapped lot on Great Falls Road', brick='yes'),
N('old-stone-fort-manchester', 'Old Stone Fort', 'Manchester', 'tn', 'fort', 'traces', 35.48278, -86.10778, 'area', 'public', 'hike', '', 'c. 80–550',
  'A hilltop enclosure of stone and earth walls built by Native people in the Middle Woodland period, most likely between 80 and 550 AD, on a peninsula where the Duck and Little Duck rivers meet. It encloses about 50 acres and was probably ceremonial rather than a fort. It is the most complex hilltop enclosure known in the South.',
  'Walls 4 to 6 feet high, once stacked stone faces with earth between, now grassed over; an entrance between two pedestal mounds and an L-shaped passage. The trail round the walls passes waterfalls on both rivers. Museum by the entrance (state park page).',
  '', 'Old Stone Fort State Archaeological Park (Tennessee State Parks), 732 Stone Fort Drive. Hours from the park\'s page, read November 22, 2026. The park bans open flames along the trails and rivers.',
  [TSP('old-stone-fort', 'Old Stone Fort State Archaeological Park'), W('Old Stone Fort (Tennessee)')],
  th=[35.48709, -86.10150], thn='Mapped lot on Stone Fort Drive', brick='no', hours='Visitor centre and museum 8 a.m. to 4:30 p.m. daily (Central)'),
N('falls-mill-belvidere', 'Falls Mill', 'Belvidere', 'tn', 'industry', 'standing', 35.09885, -86.26154, 'exact', 'open', 'drive', '', '1873',
  'Built in 1873 on Factory Creek as a cotton and woollen factory, with bricks made on the site. It was later a cotton gin, a woodworking shop and a grist mill. It now holds the Museum of Power and Industry.',
  'The three-storey mill and its overshot wheel, which still drives machinery on four floors. The mill\'s page gives the wheel as 32 feet; the Register form gives 34 feet, a metal wheel that replaced a wooden one in 1907. Wikipedia lists power looms, carding machines, millstones and a dog-powered butter churn among the exhibits.',
  'A water wheel still turning in an 1873 factory.',
  'Privately owned and run as a museum, 134 Falls Mill Road, Belvidere; admission charged, leashed pets allowed on the grounds. Hours from the mill\'s page, read November 22, 2026. Parking not checked.',
  [['Falls Mill', 'https://fallsmill.com/'], NR('72001240', 'Falls Mill Register form'), W('Falls Mill')],
  conf='mixed', brick='?', hours='April to November: Thursday to Saturday 9 a.m. to 4 p.m. Central; closed December to March'),
# ---- East Tennessee ----
N('tellico-blockhouse', 'Tellico Blockhouse', 'Vonore', 'tn', 'fort', 'traces', 35.59988, -84.20291, 'site', 'public', 'walk', 'forts', '1794–1807',
  'A United States army post finished in 1794 on the Little Tennessee River, to keep the peace between the Overhill Cherokee towns and settlers after the Cherokee–American wars. Several treaties by which the Cherokee gave up land were made there. It was garrisoned until 1807.',
  'University of Tennessee archaeologists found its foundations in the 1970s. No rebuilding was tried; the foundations were built up with fill so visitors can see the layout. Some finds are shown in the Fort Loudoun museum across the river.',
  '', 'Looked after by the staff of Fort Loudoun State Historic Park (Tennessee State Parks), whose page says the blockhouse foundations can be seen near the rebuilt fort. Hours are the Fort Loudoun visitor centre\'s, from the park\'s page, read November 22, 2026; the blockhouse ground has no hours given. Mapped lot at the end of the Tellico Blockhouse path.',
  [TSP('fort-loudoun', 'Fort Loudoun State Historic Park'), NR('75001771', 'Tellico Blockhouse Register form'), W('Tellico Blockhouse')],
  th=[35.60028, -84.20608], thn='Lot at the Tellico Blockhouse path', brick='no', hours='Fort Loudoun visitor centre and museum daily 8 a.m. to 4:30 p.m. Eastern'),
N('burra-burra-mine-ducktown', 'Burra Burra Mine and Ducktown Basin Museum', 'Ducktown', 'tn', 'industry', 'standing', 35.03565, -84.37851, 'site', 'open', 'drive', '', '1899–1959',
  'The Tennessee Copper Company opened the Burra Burra Mine in 1899, named for the mine in Australia, and took over 15 million tons of copper ore from it before it closed in 1959. The surface buildings were the company\'s mine headquarters until 1975. The state bought the site in 1988 and the Ducktown Basin Museum, founded in 1978, has been there since 1982.',
  'The mine buildings: hoist house, boiler house, ore bins, machine shops, powder house and others, of brick, wood and steel, little altered (1983 Register form). The museum counts 16 structures and Wikipedia 10. The headframe is gone: the form says dismantled in 1966, the museum\'s page after the mine closed in 1958. A collapsed, flooded part of the mine can be seen from the fence by the parking lot; the museum is in the mine office.',
  'A copper mine headquarters left whole except for its headframe.',
  'Ducktown Basin Museum and Burra Burra Mine State Historic Site, owned by the Tennessee Historical Commission, 212 Burra Burra Street; admission charged; free self-guided walk round the buildings. The museum\'s page gives its season and hours as below; the Commission\'s page gives 10 to 5. The museum\'s page also carries an undated notice of renovations closing the museum for several months: call before going.',
  [['Ducktown Basin Museum', 'https://ducktownbasinmuseum.com/'], THC('burra-burra', 'Ducktown Basin Museum & Burra Burra Mine'), NR('83003059', 'Burra Burra Mine Historic District Register form (1983)'), W('Ducktown Basin Museum and Burra Burra Mine')],
  conf='mixed', brick='?', hours='Early March to late December: daily except Wednesday and Sunday, 10 a.m. to 4:30 p.m. Eastern'),
N('blount-mansion-knoxville', 'Blount Mansion', 'Knoxville', 'tn', 'landmark', 'standing', 35.96111, -83.91519, 'site', 'open', 'walk', '', 'c. 1792',
  'William Blount, governor of the Southwest Territory and a signer of the Constitution, began the house about 1792 when he moved to Knoxville, and much of the 1796 Tennessee Constitution was drafted in his office there. It was a frame house when most in Tennessee were log. Badly run down by 1925, it was bought by the Blount Mansion Association by 1930 and restored to its 18th-century look.',
  'A frame and clapboard house with brick chimneys; the finished woodwork, pine panelling, floors and weatherboards were shipped from North Carolina (1966 Register form). Blount\'s one-room office stands apart, with wide-board panelling and a carved mantel; the kitchen was rebuilt in 1960 on its original foundation. Shown by guided tour.',
  'The frame house where Tennessee\'s first constitution was drafted.',
  'Run by the Blount Mansion Association, 200 West Hill Avenue; admission charged. Hours and parking from its page, read November 22, 2026: visitor parking at its visitors centre.',
  [['Blount Mansion: visit', 'https://www.blountmansion.org/visit'], NR('66000726', 'William Blount Mansion Register form'), W('William Blount Mansion')],
  brick='some', hours='Tuesday to Saturday 10 a.m. to 4 p.m., Sunday noon to 4 p.m., last tour at 3; closed Monday (Eastern)'),
N('rocky-mount-piney-flats', 'Rocky Mount', 'Piney Flats', 'tn', 'landmark', 'standing', 36.40552, -82.33658, 'exact', 'open', 'drive', '', '1770s or late 1820s',
  'William Cobb\'s farm, where Governor William Blount lived and governed the Southwest Territory from 1790 to 1792. The age of the log house is disputed: the 1970 Register form says Cobb built it between 1770 and 1772, while tree-ring dating by the University of Tennessee, cited by Wikipedia and the Tennessee Historical Commission, puts the present house in the late 1820s. The state bought it in 1962.',
  'A large log house, with its kitchen and scullery rebuilt on their old foundations; the 1970 form says the late-1800s weatherboarding was taken off and a shingle roof put back, and mentions a brick chimney and pine mantels. Guides in period dress show the house, farm and outbuildings as in 1791; a separate gallery museum.',
  '', 'A Tennessee State Historic Site run by the Rocky Mount Historical Association, 200 Hyder Hill Road; admission charged. Hours from the museum\'s own page, read November 22, 2026; the Commission\'s page gives March 1 to December 15, 11 to 4. The historic house has no air conditioning and the walking tour has stairs and slopes. Parking not checked.',
  [['Rocky Mount: hours and admission', 'https://rockymountmuseum.com/hours-admission'], THC('rocky-mount', 'Rocky Mount State Historic Site'), NR('70000617', 'Rocky Mount Register form (1970)'), W('Rocky Mount State Historic Site')],
  conf='mixed', brick='some', hours='March 4 to mid-December: Wednesday to Saturday 11 a.m. to 4:30 p.m., tours at 11, 1 and 3 (Eastern)'),
N('chester-inn-jonesborough', 'Chester Inn', 'Jonesborough', 'tn', 'hotel', 'standing', 36.2941, -82.47406, 'exact', 'open', 'walk', '', '1797',
  'Dr. William Chester built the inn in 1797 on the Great Stage Road and kept an apothecary in its cellar. The state calls it the finest inn on the Tennessee frontier; Andrew Jackson, James K. Polk and Andrew Johnson stayed there. It was doubled in size in 1836 and given its front porch in the 1880s.',
  'The oldest wood-frame building in Jonesborough\'s commercial district, restored after the state bought it in the early 1990s to its 1890s look (paint analysis found 97 layers). The upstairs parlour, dining and lodging rooms are open, furnished with reproductions and antiques, and the cellar holds a town museum (since 2011).',
  'Where Andrew Jackson took a featherbed on the frontier.',
  'A Tennessee State Historic Site run by the Heritage Alliance, 116 West Main Street; no admission fee. Hours from the Commission\'s and the Town of Jonesborough\'s pages, read November 22, 2026. Walking tours of the town leave from the inn on Saturdays at 1, March to December. Parking in town lots.',
  [THC('chester-inn', 'Chester Inn State Historic Site'), ['Town of Jonesborough: Heritage Alliance museums', 'https://www.jonesboroughtn.org/residents/heritage-alliance-museums/'], W('Chester Inn')],
  brick='?', hours='May to Oct: Mon, Wed to Sat 11 to 6, Sun 1 to 5; Mar, Apr, Nov, Dec: Mon, Fri, Sat 11 to 6, Sun 1 to 5; Jan and Feb by appointment (Eastern)'),
N('elizabethton-covered-bridge', 'Elizabethton Covered Bridge', 'Elizabethton', 'tn', 'landmark', 'standing', 36.34736, -82.21179, 'exact', 'public', 'walk', '', '1882',
  'Carter County voted $3,000 for a bridge over the Doe River in 1882. With no contractor to be found, a local doctor, E. E. Hunter, took the job and hired Thomas Matson, an engineer of the narrow-gauge East Tennessee and Western North Carolina Railroad, to design it; Hunter called it his five-dollar bridge, for his profit. It was the only major bridge in the area to survive the 1901 flood.',
  'A single-span Howe truss, 137 feet long, roofed and sided, on masonry, stone and concrete piers, with projecting gables at each end. Closed to cars and open to people on foot and bicycles all year; a city park with paths lies on one side and downtown on the other.',
  '', 'A public street crossing between 3rd Street and Hattie Avenue in Elizabethton, part of the Elizabethton Historic District. Built by order of the Carter County Court; who owns and maintains it now was not checked, but Wikipedia says it is open to walkers and cyclists all year. Park downtown.',
  [W('Elizabethton Covered Bridge')],
  brick='no'),
]

PIN_NOTES = {
  'fort-pillow-earthworks': 'Wikipedia infobox point for the park; the earthworks spread along the bluff, so prec area.',
  'pinson-mounds-sauls-mound': 'OpenStreetMap point for Saul\'s Mound (nom.py).',
  'woodruff-fontaine-house': 'OpenStreetMap point for the museum at 680 Adams Avenue (nom.py).',
  'great-western-furnace': 'OpenStreetMap ruins point (nom.py); the HMdb markers give 36.64063, -87.97563. The aerial shows the road shoulder with a small pale object at the pin and trees beside it; the stack itself is not plain under the leaves.',
  'dover-hotel-surrender-house': 'HMdb marker 38766 "Dover Hotel" position.',
  'montgomery-bell-tunnel': 'OpenStreetMap point for the tunnel (nom.py), matching the Wikipedia infobox.',
  'cragfont-castalian-springs': 'ArcGIS PointAddress for 200 Cragfont Road.',
  'great-falls-cotton-mill': 'The Register list point (35.8025, -85.62528) fell on the park road in woods; moved 120 m to a long pale roof beside the road and the river on the aerial, taken to be the mill but not certain, so prec site.',
  'old-stone-fort-manchester': 'Wikipedia infobox point inside the enclosure; the walls ring about 50 acres, so prec area.',
  'falls-mill-belvidere': 'ArcGIS PointAddress for 134 Falls Mill Road.',
  'tellico-blockhouse': 'Wikipedia infobox point; on the aerial it sits inside a fenced square outline on a point in Tellico Lake.',
  'burra-burra-mine-ducktown': 'ArcGIS PointAddress for 212 Burra Burra Street (the museum); the flooded pit is about 80 m west.',
  'blount-mansion-knoxville': 'Wikipedia infobox point; on the aerial it falls on the grounds among trees beside a small building, not plainly on the house, so prec site.',
  'rocky-mount-piney-flats': 'OpenStreetMap point for the historic site at 200 Hyder Hill Road (nom.py).',
  'chester-inn-jonesborough': 'OpenStreetMap point for the inn at 116 West Main Street (nom.py).',
  'elizabethton-covered-bridge': 'OpenStreetMap bridge point (nom.py).',
}
