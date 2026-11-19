# November 18, 2026: Beaufort County, South Carolina (Beaufort, Port Royal, St. Helena Island, Sheldon, Hilton Head
# Island and Bluffton). Region sc drawn at random by choose.py; the first batch for South Carolina beyond the one
# worked example.
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py, including the
# Register list rows for the county), National Register nomination forms read as text from NPGallery, the county's
# Fort Fremont news page, SCDNR's Fort Frederick interpretive panels (PDF), The Island News, South Carolina State Parks,
# the Hilton Head Island Land Trust, the Heritage Library venue listing, the Dataw Historic Foundation, Palmetto Dunes
# and the Rear Range Lighthouse's own site, the National Park Service (Reconstruction Era NHP), Penn Center, the
# Beaufort History Museum, the Church of the Cross, and two local magazines (South Carolina Lowcountry,
# hiltonhead-sc.com). Where a manager's page could not be read the access note says so.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'sc_vxwi','label':'Beaufort County, South Carolina: tabby ruins, forts and old churches','added':'2026-11-18 13:34'}

NR='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'
def F(n,t): return L('National Register nomination: '+t,NR%n)
BC_NR=W('National Register of Historic Places listings in Beaufort County, South Carolina')
REER=L('NPS: Reconstruction Era NHP, places to go','https://home.nps.gov/reer/planyourvisit/placestogo.htm')

PLACES=[
# ---- northern Beaufort County ----
N('old-sheldon-church-ruins','Old Sheldon Church ruins (Prince William\'s Parish Church)','Sheldon','sc','worship','ruins',32.61854,-80.78046,'exact','view','walk','','1745–1753',
  'Built between 1745 and 1753 as the church of Prince William\'s Parish, in the English Georgian style with a row of Tuscan columns. The usual account is that the British burned it in 1779, that it was rebuilt in 1826 and burned again by Sherman\'s army in 1865; but a letter of February 1866 says the church was not burned, only gutted inside, and it is now thought local people stripped it for materials to rebuild their own burned houses. Governor William Bull is buried inside the ruin. A tablet on the grounds gives the building years as 1745–1755, and a local magazine says the first services were held in 1757.',
  'The outer walls, three and a half feet thick, laid in Flemish bond brick, stand roofless among live oaks and old graves, with the four brick columns of the west portico (the nomination). Since 2019 a locked black fence surrounds the ruin itself: visitors may walk the grounds and look, but may not go in among the columns and arches.',
  'Two fires, or one fire and a gutting: the sources argue about how this church became a ruin.',
  'Owned and kept by the Parish Church of St. Helena, Beaufort (South Carolina Lowcountry magazine). The ruin is behind a locked fence; the grounds round it are open to look at. Weddings stopped being held here in 2015 (beaufort.com). The parish\'s own page on visiting was not found, so hours not checked. A mapped parking area on Old Sheldon Church Road is 130 m south-west.',
  [W('Old Sheldon Church Ruins'),F('70000562','Sheldon Church'),L('South Carolina Lowcountry: Old Sheldon Church ruins are protected','https://southcarolinalowcountry.com/?p=12787'),
   L('South Carolina Lowcountry: Old Sheldon Church, then and now','https://southcarolinalowcountry.com/?p=49429'),L('beaufort.com: the Old Sheldon Church ruins','https://www.beaufort.com/the-old-sheldon-church-ruins'),BC_NR],
  conf='mixed',th=[32.61754,-80.78122],thn='Old Sheldon Church Road parking area',brick='?'),

# ---- Beaufort ----
N('parish-church-st-helena-beaufort','Parish Church of St. Helena','Beaufort','sc','worship','standing',32.43406,-80.67467,'exact','view','walk','','1724',
  'The parish was set up by act of the colonial assembly in 1712, two years after Beaufort was founded, and its church was finished about 1724 after the Yamasee War held up the work. It was enlarged in 1769 and again in 1842, when galleries were added inside; in the Civil War it served as a hospital. It is still a working church and one of the oldest church buildings in continuous use in the country.',
  'A large church in a walled churchyard of live oaks and palmettos, with old graves including that of Colonel John "Tuscarora Jack" Barnwell, buried in 1724. A local guide describes white columns inside. Interior fabric beyond that not checked.',
  '',
  'An active Episcopal parish; a visitors\' guide says the church and graveyard are open to visitors (hiltonhead-sc.com), but the parish\'s own site gave no visiting hours, so hours not checked. Street parking in downtown Beaufort.',
  [W('Parish Church of St. Helena'),L('hiltonhead-sc.com: St. Helena\'s','https://hiltonhead-sc.com/st-helenas.html'),L('Parish Church of St. Helena','https://www.sthelenas1712.org/')],
  brick='?'),
N('john-mark-verdier-house','John Mark Verdier House','Beaufort','sc','town','standing',32.43064,-80.671,'exact','public','walk','','1804',
  'Built in 1804 by John Mark Verdier, a Huguenot merchant who made his money trading indigo and growing sea island cotton. Also known as the Lafayette Building. It stands in the Beaufort Historic District, a National Historic Landmark, and is the town\'s house museum, owned and run by the Historic Beaufort Foundation.',
  'A two-storey merchant\'s house of painted weatherboard over a raised basement, with a two-tier columned portico on Bay Street (Wikimedia Commons photograph); shown on guided tours. Original interior fabric not checked.',
  '',
  'Historic Beaufort Foundation house museum. Wikipedia gives tours Monday to Saturday 10 to 4 at $10 a person, children and military free; the foundation\'s own site refused to open (HTTP 403), so hours not checked. Street parking downtown.',
  [W('John Mark Verdier House'),L('Historic Beaufort Foundation','https://historicbeaufort.org/'),BC_NR],brick='no'),
N('beaufort-arsenal','Beaufort Arsenal (Beaufort History Museum)','Beaufort','sc','fort','standing',32.43276,-80.67069,'exact','public','walk','','1798, rebuilt 1852',
  'Built in 1798 on the original town square as the headquarters and armoury of the Beaufort Volunteer Artillery, a militia of the town\'s leading families. Secessionists enlarged it and rebuilt the first tabby building in brick; the National Park Service gives 1852 as the year the present Arsenal was built. After the Civil War the Reconstruction government disbanded the company and took over the building. It now holds the Beaufort History Museum.',
  'A yellowish walled building on Craven Street, across the street from the Reconstruction Era National Historical Park visitor center, which shares the site. Interior fabric not checked.',
  'An armoury for gentlemen soldiers who also policed the enslaved.',
  'Beaufort History Museum, 713 Craven Street (NPS). The museum\'s page names "visiting hours and admission" but the hours did not come through, so hours not checked. Street parking downtown.',
  [L('Beaufort History Museum: the Arsenal','https://beauforthistorymuseum.wildapricot.org/the-arsenal'),REER],conf='mixed',brick='no'),

# ---- Port Royal ----
N('fort-frederick-port-royal','Fort Frederick (Fort Prince Frederick)','Port Royal','sc','fort','ruins',32.38444,-80.67833,'site','public','walk','','1730s–1757',
  'A small British tabby fort on the Beaufort River, built to guard Beaufort against Spanish ships from St. Augustine. Wikipedia gives 1730 to 1734 and SCDNR\'s panels 1733 to 1735. Its guns were only ever fired in salute, and each salute shook loose some of the tabby. It was given up in 1757 for Fort Lyttelton. It is held to be the oldest tabby fort surviving in South Carolina.',
  'The low tabby walls of a fort about 125 by 75 feet, with a bastion on the south-west side, at the river\'s edge; the shells in the tabby were dug from old Native American middens, and bits of pottery show in the walls (SCDNR panels). Interpretive panels and a picnic pavilion.',
  'A fort whose guns fired only salutes, and crumbled their own walls doing it.',
  'Fort Frederick Heritage Preserve: SCDNR land, with the public entrance, parking and pavilion on land owned by Beaufort County and kept by the Town of Port Royal. Open dawn to dusk every day since its opening in 2021 (The Island News); SCDNR\'s own preserve page was not opened. It is next to the grounds of the Naval Hospital Beaufort.',
  [W('Fort Frederick Heritage Preserve'),L('SCDNR: Fort Frederick interpretive panels (PDF)','https://content.govdelivery.com/attachments/SCDNR/2021/02/22/file_attachments/1700786/2021%20FFHP%20Interpretive%20Panels%20Reduced%20Size.pdf'),
   L('The Island News: Fort Frederick Heritage Preserve now open','https://archive.yourislandnews.com/?p=48342'),BC_NR],conf='mixed',brick='no'),

# ---- St. Helena Island ----
N('st-helena-chapel-of-ease-ruins','St. Helena Parish Chapel of Ease ruins','St. Helena Island','sc','worship','ruins',32.37555,-80.57656,'exact','view','drive','','c.1740–1886',
  'A tabby chapel built about 1740, by enslaved people, for planters on St. Helena Island who lived too far from the parish church in Beaufort. In 1812 it became a parish church in its own right. The planters fled in 1861; in the Union occupation the Northern teachers held meetings here, and the freedmen, who worshipped at the Brick Church, called it the "White Church". Methodist freedmen used it from 1868 until a forest fire burned it in February 1886, and it was never repaired.',
  'Roofless tabby walls with much of their plaster still on them, beside a small cemetery whose gravestones the Register counts as exceptional; the Edgar Fripp mausoleum in the churchyard is listed separately.',
  'Built by enslaved hands, burned by a forest fire.',
  'Beside Lands End Road. Ownership not checked; the ruin and graves are seen from the grounds. The Register form gives no visiting rules, so hours not checked. No mapped parking: pull off at the site.',
  [W('St. Helena Parish Chapel of Ease Ruins'),F('88001777','St. Helena Parish Chapel of Ease ruins'),BC_NR],brick='no'),
N('brick-baptist-church-st-helena','Brick Baptist Church','St. Helena Island','sc','worship','standing',32.38967,-80.576,'exact','view','drive','','1855',
  'Built in 1855 by enslaved people as a church for the island\'s white planters, several of whom lie in the small cemetery beside it. After the Union army took the sea islands it became a refuge for the freed people, and in 1862 Laura Towne and Ellen Murray opened what became the Penn School inside it. It is part of the Reconstruction Era National Historical Park.',
  'The fingerprints of the enslaved people who made the bricks can still be seen in some of the walls (NPS). The National Park Service keeps the outside; the inside belongs to a working congregation and is not usually open to visitors.',
  'Fingerprints in the brick.',
  'Outside preserved by the National Park Service; the interior is an active church and not normally open (NPS). Be respectful of services. Free parking at Penn Center across the road (Penn Center).',
  [L('NPS: Brick Baptist Church','https://home.nps.gov/reer/planyourvisit/brick-baptist-church.htm'),REER,W('Penn Center (Saint Helena Island, South Carolina)')],
  th=[32.38791,-80.57718],thn='Penn Center parking',brick='?'),
N('penn-center-st-helena','Penn Center (Penn School Historic District)','St. Helena Island','sc','inst','standing',32.38845,-80.57747,'site','public','walk','','1862',
  'Founded in 1862 by Quaker and Unitarian missionaries from Pennsylvania as the first school in the South set up for the education of African Americans, for the freed Gullah people of the sea islands. The campus became a National Historic Landmark district in 1974, and Darrah Hall is part of the Reconstruction Era National Historical Park.',
  'A 50-acre district of 25 historic buildings and structures. The York W. Bailey Museum is in the old Cope Industrial Shop, built for trade classes and dedicated on the school\'s 50th anniversary. A self-guided walking-tour map and a nature trail shared with the National Park Service.',
  '',
  'Penn Center, 16 Penn Center Circle West. Museum Tuesday to Saturday 10 to 4, welcome center Tuesday to Saturday 9 to 4; self-guided tour $10, docent tour with film $15, under 5 free; parking free (Penn Center visit page, read November 18, 2026). Heritage Days are each November.',
  [L('Penn Center: visit','https://penncenter.com/visit'),W('Penn Center (Saint Helena Island, South Carolina)'),REER],
  th=[32.38791,-80.57718],thn='Penn Center parking',brick='?'),
N('fort-fremont-batteries','Fort Fremont batteries','St. Helena Island','sc','fort','ruins',32.30616,-80.64285,'exact','public','walk','','1899–1911',
  'A coast-artillery fort begun in 1899 for the Spanish-American War, to guard the naval station on Parris Island across Port Royal Sound. It had three 10-inch disappearing guns and two 4.7-inch rapid-fire guns. The War Department gave it up after nineteen years and sold it at auction in June 1930. The Register calls it one of two coastal forts in the country surviving intact from the Spanish-American War era.',
  'The poured-concrete 10-inch battery and rapid-fire battery, in woods facing the sound; no guns remain. The brick post hospital is listed separately and whether it is inside the preserve was not checked. A history center with scale models of the fort.',
  'The guns that hid behind their own walls.',
  'Fort Fremont Preserve, 1124 Land\'s End Road: owned by Beaufort County (bought in 2004 and 2010), open daily dawn to dusk, free, with parking, a picnic pavilion, paths and restrooms. The history center is open Fridays 10 to 2, Saturdays 10 to 4 and Sundays 1 to 4 (county news, April 2023).',
  [W('Fort Fremont'),F('88001821','Fort Fremont Battery'),L('Beaufort County: Fort Fremont History Center hours','https://beaufortcountysc.gov/news/2023/04/sundays-in-the-park-beaufort-county-announces--new-hours-for-the-fort-fremont-history-center-.html'),L('Friends of Fort Fremont','https://fortfremont.org/')],
  brick='no'),
N('hunting-island-lighthouse','Hunting Island Lighthouse','Hunting Island','sc','light','standing',32.37556,-80.4375,'exact','public','walk','','1859; 1875',
  'The first tower was begun in 1859 and destroyed in the Civil War. It was rebuilt in 1875 as a segmented cast-iron tower, a design that could be taken apart, and in 1889 beach erosion forced its move 1.3 miles inland. It was put out in 1933. A restoration closed it from 2022, and it reopened for climbing in 2026.',
  'A brick tower inside a cast-iron shell, black on the top third and white below; 167 steps to the gallery. The original lens is gone; the first-order lens from the Morris Island lighthouse stands at the base, and an LED now flashes the 1859 pattern at night. Climbs are sold at the oil house across from the tower.',
  'A lighthouse built to be taken apart, and then moved.',
  'Hunting Island State Park (South Carolina State Parks). Park admission or a Park Passport is required ($8 adult, $5 South Carolina seniors, $4 ages 6 to 15, under 6 free, as the lighthouse page lists them); the park closes at 6 p.m., 9 p.m. in Daylight Saving Time. Climbs first come first served, groups of 12, 30 minutes; climbers at least 44 inches tall and able to climb alone; climb fee not checked.',
  [L('SC State Parks: Hunting Island Lighthouse','https://southcarolinaparks.com/hunting-island/lighthouse'),L('SC State Parks: Hunting Island','https://southcarolinaparks.com/hunting-island'),W('Hunting Island Lighthouse')],
  th=[32.3761,-80.43835],thn='Lighthouse parking, North Beach Road',brick='no'),

# ---- Hilton Head Island ----
N('fort-howell-hilton-head','Fort Howell','Hilton Head Island','sc','fort','traces',32.23273,-80.6949,'exact','public','walk','','1864',
  'An earthwork fort built from late summer to November 1864 by the 32nd United States Colored Infantry and the 144th New York Infantry, to guard Mitchelville, the town of freed people on Hilton Head. It measured about 525 by 400 feet with parapets 23 feet high (as designed) and could take up to 27 guns; which guns were ever mounted is not known.',
  'The earth walls and bastions of the fort in woods, circled by a gravel path with interpretive signs.',
  'A fort built by Black soldiers to protect a free Black town.',
  'Owned by the Hilton Head Island Land Trust, a nonprofit. Free, open dawn to dusk, with parking on Beach City Road (land trust page).',
  [L('Hilton Head Island Land Trust: Fort Howell','https://www.hhilandtrust.org/fort-howell'),F('11000371','Fort Howell'),REER],
  th=[32.23215,-80.69422],thn='Fort Howell, 160 Beach City Road',brick='no'),
N('zion-cemetery-baynard-mausoleum','Zion Chapel of Ease cemetery and Baynard Mausoleum','Hilton Head Island','sc','burial','standing',32.20167,-80.69979,'site','public','walk','','18th century; mausoleum 1846',
  'The burying ground of St. Luke\'s Parish\'s Zion Chapel of Ease, begun in the 18th century; the chapel itself was destroyed in the 1860s and its remains lie somewhere on the ground. The Baynard Mausoleum of 1846 is believed to be the oldest surviving building on the island.',
  'A Classical Revival mausoleum of 20 chambers, built of brick faced with red sandstone dressed to look like ashlar, with an inscription in its pediment and a cast-iron fence; gravestones from 1798 on, among them family plots of the Irvine, Flinn, Webb, Kirk and Baldwin families. A paved path and outdoor learning center from 2016.',
  '',
  'Run by the Heritage Library Foundation, which holds tours and events here, at 574 William Hilton Parkway (hiltonheadisland.com venue listing). Opening hours not checked: the library\'s own page for the site answered 404.',
  [W("St. Luke's Parish Zion Chapel of Ease Cemetery"),F('100000727','St. Luke\'s Parish Zion Chapel of Ease cemetery'),L('hiltonheadisland.com: Zion Cemetery & Baynard Mausoleum','https://www.hiltonheadisland.com/events/venues/zion-cemetery-baynard-mausoleum-historic-site')],brick='no'),
N('hilton-head-rear-range-light','Hilton Head Rear Range Lighthouse (Leamington Light)','Hilton Head Island','sc','light','standing',32.16417,-80.74,'exact','view','drive','','1879–1932',
  'Built in 1879–80 by the Lighthouse Board as the rear light of a range that guided ships into Port Royal Sound; the front light stood on a keeper\'s house that could be moved as the channel shifted. Put out of use in 1932. One keeper\'s house was cut in two and moved to Harbour Town.',
  'A cast-iron skeleton tower on six concrete piers, with a central stair cylinder and a wooden watch room and lantern, beside a small brick oil house of 1892, in pines by the 15th hole of the Arthur Hills golf course. The tower is closed: no going inside or up.',
  '',
  'Inside the Palmetto Dunes resort. Free to visit: ask at the resort gate for a lighthouse pass (none given after 5 p.m.), then go to the Leamington Gate and park along the roadside on Leamington Lane (Palmetto Dunes; the lighthouse\'s own site).',
  [W('Hilton Head Range Rear Light'),F('85003349','Rear Lighthouse of Hilton Head Range Light Station'),L('Hilton Head Rear Range Lighthouse: plan your visit','https://www.hiltonheadlighthouse.com/plan-your-visit'),
   L('Palmetto Dunes: lighthouse lore','https://www.palmettodunes.com/blog/lighthouse-lore-in-the-lowcountry')],brick='?'),
N('stoney-baynard-ruins','Stoney-Baynard plantation ruins','Hilton Head Island','sc','town','ruins',32.12884,-80.81424,'site','ask','walk','','1793 or c.1800–1865',
  'A plantation house of tabby and timber on the highest ground at the south end of Hilton Head, overlooking Calibogue Sound. Wikipedia says Captain Jack Stoney built it in 1793; the Register form dates the house, overseer\'s house and slave house to the first decade of the 1800s. William Baynard had it by 1837 and lived there in the 1840s; Union troops camped here in the Civil War, and the house burned soon after the war.',
  'Two-storey fragments of the tabby main house, the chimney footing of what may be the overseer\'s house, a slave house ruin and the footings of a Union tent, on about six acres of preserved green space.',
  'A house said to have been lost in a card game.',
  'On green space owned by the Sea Pines property owners\' association, between Baynard Park Road and Plantation Drive, inside the private gated community of Sea Pines. How outside visitors get in (gate pass, fee) was not checked from Sea Pines\' own page. A mapped parking area on Plantation Drive is 80 m east.',
  [W('Stoney-Baynard Plantation'),F('94000038','Stoney/Baynard Plantation')],conf='mixed',th=[32.12891,-80.81346],thn='Plantation Drive pull-off',brick='no'),

# ---- Bluffton ----
N('church-of-the-cross-bluffton','Church of the Cross','Bluffton','sc','worship','standing',32.23159,-80.86372,'exact','public','walk','','1857',
  'A cruciform Gothic church on the bluff over the May River, designed by E. B. White and consecrated in July 1857. When Federal troops burned most of Bluffton in 1863 the church was spared, though its people fled; services began again in 1870. A new roof of 1892 was damaged with the rest of the building in the 1898 hurricane.',
  'A wooden church of vertical board and batten under a grey metal roof (Wikimedia Commons photograph). Mullioned windows topped by fanned arches like palmetto fronds, with lattice shutters; the rose-coloured glass came from England. Inside, scored pink plaster and exposed pine timbers.',
  '',
  'An active parish. Docents give tours of the historic campus Monday to Thursday 11 to 2; call ahead (843-757-2661), as funerals and services change this (Church of the Cross, historic campus page).',
  [W('Church of the Cross'),L('Church of the Cross: historic campus','https://thechurchofthecross.net/?p=2868'),BC_NR],brick='no'),
]

PIN_NOTES={
 'old-sheldon-church-ruins':'OpenStreetMap ruins point (nom.py), within 2 m of the Wikipedia coordinate.',
 'parish-church-st-helena-beaufort':'Wikipedia coordinate; an ArcGIS address point on Church Street falls on it.',
 'john-mark-verdier-house':'Wikipedia coordinate; an ArcGIS address point on Bay Street is 30 m away.',
 'beaufort-arsenal':'OpenStreetMap point for the visitor center and arsenal on Craven Street (nom.py).',
 'fort-frederick-port-royal':'Wikipedia coordinate, in trees at the river edge inside the preserve; neither the aerial nor the LiDAR showed the tabby walls plainly, so site precision.',
 'st-helena-chapel-of-ease-ruins':'OpenStreetMap building mapped as the chapel ruins (osmnear.py), 30 m from the Register list point.',
 'brick-baptist-church-st-helena':'OpenStreetMap building named Brick Church (osmnear.py).',
 'penn-center-st-helena':'ArcGIS address point for 16 Penn Center Circle West, the address Penn Center gives.',
 'fort-fremont-batteries':'Moved 61 m west of the Register list point onto the concrete battery, which shows plainly on the LiDAR sheet (the aerial shows only trees). The preserve\'s parking area was not found on the aerial, so no parking point is given; the ArcGIS point for its address (1124 Land\'s End Road) fell among houses.',
 'hunting-island-lighthouse':'Wikipedia coordinate.',
 'fort-howell-hilton-head':'Moved onto the middle of the earthwork, which shows plainly on the LiDAR sheet 90 m north-west of the address point; the Register list point was 160 m off, by a road junction. The parking point is the ArcGIS address point for 160 Beach City Road (the address NPS gives), on the road beside the fort.',
 'zion-cemetery-baynard-mausoleum':'ArcGIS address point for 574 William Hilton Parkway, within 60 m of the Wikipedia coordinate.',
 'hilton-head-rear-range-light':'Wikipedia coordinate.',
 'stoney-baynard-ruins':'OpenStreetMap park named Baynard Ruins (nom.py), 50 m from the Wikipedia coordinate.',
 'church-of-the-cross-bluffton':'OpenStreetMap point for the church (nom.py); the Wikipedia coordinate fell on the river shore 85 m south-west. The point is on a cross-shaped grey-roofed building on the aerial; its grey metal roof matches the photograph of the 1857 church.',
}
