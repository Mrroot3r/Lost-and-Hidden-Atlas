# November 23, 2026: Weston, Platte City and Camden Point, Platte County, Missouri, north-west of Kansas City.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had no place within 15 km of Weston.
# Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py), Legends of America's Weston pages,
# the Advisory Council on Historic Preservation, the National Trust, the Platte County Landmark and Platte County Citizen
# newspapers, Northeast News, KCUR, KSHB, Missouri Wines, Missouri State Parks and the distillery's own page.
# The National Register forms for these places could not be read: NPGallery holds only a placeholder for each, and the
# Missouri State Historic Preservation Office copies have moved (HTTP 404 at the old addresses).
from data_b import N
from data_ma import W

LOA = ['Legends of America: Weston, Missouri', 'https://www.legendsofamerica.com/mo-weston/2/']
ACHP = ['Advisory Council on Historic Preservation: Weston', 'https://www.achp.gov/node/9159']

PLACES = [
N('weston-historic-district-mo', 'Weston Historic District and Main Street', 'Weston', 'kcmo', 'town', 'standing',
  39.41160, -94.90125, 'site', 'public', 'walk', '', 'about 1840–1920',
  'Weston was laid out in 1837 by two soldiers from Fort Leavenworth at a natural steamboat landing, and was the first town in the Platte Purchase. '
  'In the early 1850s it was one of the busiest ports on the Missouri, shipping tobacco and hemp and supplying the fort and the trails west. '
  'A fire in 1855, the Civil War, a flood in 1858 and the flood of 1881, which moved the river about two miles away, ended the boom, and a second downtown fire came in December 1890. '
  'Because the town stopped growing, its old buildings survived; 16 blocks and parts of eight more were listed on the National Register in 1972.',
  look='Main Street and the streets round it are lined with brick commercial blocks, most of them rebuilt between 1855 and 1860 after the first fire, with houses from the 1840s to about 1920 behind them. '
  'Buildings the Register listing names include the John Maitland home (about 1860), the Humphrey house, the Railey Brothers banking building, the Hull mill, the Methodist church (1868), the old Presbyterian church, the German Evangelical Lutheran church (1867) and the former Baptist church of 1902, now the historical museum. '
  'Many buildings carry their own small history plaques. The shops are open their own hours; the houses are private.',
  hook='The river walked away from Weston in 1881, and that is why the old town is still here.',
  accn='Public streets in the town of Weston. Park on Main Street or the side streets. Most downtown buildings are shops, restaurants and private houses: look from the street unless a shop is open.',
  links=[W('Weston Historic District'), W('Weston, Missouri'), LOA, ACHP],
  brick='yes'),

N('st-george-hotel-weston-mo', 'St. George Hotel', 'Weston', 'kcmo', 'hotel', 'standing',
  39.41122, -94.90133, 'exact', 'open', 'drive', 'hotels,burned', '1845–1847; rebuilt 1891',
  'The St. George was one of three hotels in Weston in its river-port days and is the only one left. It catered to working men, with 47 rooms on the top two floors and a saloon, sample rooms for travelling salesmen, a tobacco shop and a restaurant below. '
  'The December 1890 fire left only its two street walls standing; it was rebuilt inside them with a new brick front, about ten feet lower than before. '
  'It stood empty from 1984 and reopened as a hotel in 2004 after a full restoration. The sources disagree on when it was first built: 1845 (the Advisory Council on Historic Preservation) or 1846 (Legends of America).',
  look='The largest building downtown, on the corner of Main Street. The two street-side walls are older than the rest of the building. A photograph on Wikimedia Commons shows a three-storey red brick front with a mansard roof and dormers. It is a working hotel; what of the old interior survives was not checked.',
  hook='A hotel that burned down to two walls and was built back inside them.',
  accn='A working hotel at 500 Main Street, run by the Weston Brewing Company group (its website takes bookings). Street parking on Main Street. No opening hours were found on its page; the lobby is a hotel lobby.',
  links=[['Weston Brewing Company (the hotel\'s owners)', 'https://westonirish.com/'], LOA, ACHP],
  conf='mixed', brick='yes', hours='?'),

N('weston-brewing-cellars-mo', 'Weston Brewing Company and its lagering cellars', 'Weston', 'kcmo', 'industry', 'standing',
  39.41137, -94.89990, 'exact', 'open', 'drive', '', '1842',
  'John Georgian, a German immigrant, founded the brewery in 1842, one of the first lager breweries in the United States. '
  'To keep lager below 60 degrees he dug five arched limestone cellars about 55 to 60 feet underground. After his death in 1857 the brewery changed hands many times (it was the Royal Brewing Company after 1901) and it closed with Prohibition in 1919. '
  'The O\'Malley family opened a restaurant here in the late 1970s and a pub in the largest cellar in the 1980s; the present owners bought the 3.2-acre complex in 2005 and brew again next door.',
  look='O\'Malley\'s Pub is in one of the old cellars: you go down through a narrow stone tunnel into a vaulted limestone room. The brewery\'s brick buildings stand above at Welt and Short streets. '
  'The owners\' own page calls the pub "O\'Malley\'s 1832" in one place and "1842" in another; every other source gives 1842.',
  hook='A bar 55 feet underground in a cellar dug for lager in the 1840s.',
  accn='A working brewery, restaurant and pub at 500 Welt Street, run by Weston Brewing Company. A National Trust article of 2016 gave the pub\'s hours as evenings Monday to Thursday and from late morning Friday to Sunday; the owners\' page read gives only its music calendar, so check before going.',
  links=[['Weston Brewing Company', 'https://westonirish.com/'], ['National Trust for Historic Preservation, 2016', 'https://savingplaces.org/stories/omalleys-pub-historic-bar'],
         ['Northeast News, 2022', 'https://northeastnews.net/pages/oldest-brewery-west-of-the-hudson-river/'], W('Weston, Missouri')],
  brick='?', hours='?'),

N('holladay-distillery-weston-mo', 'Holladay Distillery (McCormick Distilling)', 'Weston', 'kcmo', 'industry', 'standing',
  39.39818, -94.87898, 'site', 'open', 'drive', '', '1856',
  'Ben Holladay, later famous as the "Stagecoach King" of the overland mail, opened a distillery here in 1856 at a limestone spring that Lewis and Clark had noted in 1804. '
  'His brother David ran it until 1894; it was the Shawhan Distillery from 1900, kept going in Prohibition by making whiskey for medicine, became the Old Weston Distillery in 1936 and took the McCormick name in 1942. '
  'It is on the National Register and is the oldest distillery west of the Mississippi still working on its original site.',
  look='A working distillery on a 160-acre hillside south-east of town, with the original spring shown on the tour. Tours start at the house at the top of the hill.',
  hook='Bourbon from the same limestone spring since before the Civil War.',
  accn='Private company grounds at 1 McCormick Lane, open to visitors at the hours on the distillery\'s own page (read November 2026), which also sells tours. Park at the visitor house.',
  links=[W('McCormick Distilling Company'), ['Holladay Distillery', 'https://www.mccormickdistilling.com/'],
         ['Platte County Landmark, 2019', 'https://plattecountylandmark.com/2019/05/31/limestone-spring-water-sets-this-place-apart/'],
         ['KSHB 41', 'https://www.kshb.com/news/local-news/missouri/platte-county/oldest-distillery-west-of-the-mississippi-keeps-bourbon-making-traditions-alive-in-weston']],
  brick='?', hours='Wednesday and Thursday 11 a.m. to 4 p.m., Friday 11 to 5, Saturday 10:30 to 5, Sunday 11 to 4; closed Monday and Tuesday'),

N('pirtle-winery-church-weston-mo', 'German Evangelical Lutheran church (Pirtle Winery)', 'Weston', 'kcmo', 'worship', 'standing',
  39.41159, -94.89875, 'exact', 'open', 'drive', '', '1867',
  'German immigrants built this two-storey brick church in 1867. It later served as a bottling works for a brewery and then as the Second Baptist Church, and it was falling apart and about to be pulled down for a parking lot when Elbert and Patricia Pirtle bought it. '
  'They opened a winery in it in 1978, and their sons run it now.',
  look='The old church on Spring Street. Wine is made on the ground floor and the tasting room and shop are upstairs, in the old church room. What survives of the church fittings was not checked.',
  hook='A German church saved from becoming a parking lot by a math professor who made cherry wine.',
  accn='A working winery and tasting room at 502 Spring Street, family-owned. Street parking. The winery\'s own page gives no opening hours in the text that could be read.',
  links=[['Missouri Wines, 2019', 'https://missouriwine.org/node/26831'], ['Pirtle Winery', 'https://www.pirtlewinery.com/'], LOA],
  brick='?', hours='?'),

N('weston-historical-museum-mo', 'Weston Historical Museum (former Weston Baptist Church)', 'Weston', 'kcmo', 'worship', 'standing',
  39.41259, -94.90078, 'exact', 'open', 'drive', '', '1902',
  'The town\'s museum, founded in 1960 when Weston began to restore its old houses, is in the Weston Baptist Church building of 1902. '
  'It keeps displays and a library, gives town tours, and puts on cemetery walks in which actors play people from Weston\'s past.',
  look='The former church on Main Street at the north end of downtown. Interior not checked beyond its use as a museum.',
  accn='Run by the Weston Historical Museum at 601 Main Street; admission free. Its own pages answered 403 when this was written; the hours given here are as web search results quoted the museum\'s site (closed in winter, reopening about mid-March). Street parking.',
  links=[W('Weston Historic District'), ACHP, ['Weston Historical Museum', 'https://westonhistoricalmuseum.org/']],
  brick='?', hours='Mid-March to December: Wednesday to Saturday 11 a.m. to 4 p.m., Sunday 1 to 4 p.m.; closed in winter (as quoted from the museum\'s site, 2026)'),

N('weston-burley-house-1-mo', 'Missouri District Warehouse (Weston Burley House No. 1)', 'Weston', 'kcmo', 'industry', 'standing',
  39.41016, -94.90283, 'site', 'view', 'drive', '', '1937',
  'A loose-leaf tobacco auction warehouse and curing barn built in 1937, when burley tobacco was still the main crop round Weston. '
  'It is a sprawling two-storey steel-frame building sheathed in corrugated metal, 125 by 300 feet, and was listed on the National Register in 2010.',
  look='A long corrugated-metal shed at the foot of the old town, near where the steamboat landing was. Whether it is still used for tobacco was not checked.',
  hook='The last big tobacco auction house of a town that grew rich on tobacco.',
  accn='Private building; see it from the public street. Owner not checked.',
  links=[W('Missouri District Warehouse'), LOA],
  brick='no'),

N('weston-bend-tobacco-barn-mo', 'Tobacco barns, Weston Bend State Park', 'Weston', 'kcmo', 'industry', 'standing',
  39.39219, -94.87264, 'site', 'public', 'walk', '', '',
  'Platte County once grew a great deal of tobacco, and there were five tobacco barns on the land that became Weston Bend State Park in 1980. '
  'The park keeps one barn as a display of how tobacco was hung and cured after it left the field, with guided tours at its harvest day, and has turned another into the enclosed Bee Creek Shelter. '
  'The sources disagree on how many barns remain: Wikipedia says one, Legends of America says four.',
  look='Big wooden-sided barns built to air-cure hanging tobacco, on the wooded bluffs above the Missouri. The park\'s Barn Trail passes the barn the pin marks.',
  accn='Missouri State Parks, 16600 Highway 45 North. Day-use areas open 7 a.m. to sunset every day; the gates open 7 a.m. and close at 9 p.m. from April 15 to October 31 and at 6 p.m. the rest of the year (park hours page, read November 2026). The Bee Creek Shelter is a rental: reserve through the park office.',
  links=[W('Weston Bend State Park'), ['Missouri State Parks: hours', 'https://mostateparks.com/hours/691/park/weston-bend-state-park'],
         ['Missouri State Parks: picnicking', 'https://mostateparks.com/park/weston-bend-state-park/picnicking'],
         ['Missouri Department of Natural Resources, 2022', 'https://dnr.mo.gov/communications/news/weston-bend-state-park-holds-historic-harvest'], LOA],
  conf='mixed', th=[39.39210, -94.87349], thn='Barn Trail parking, Weston Bend State Park', brick='?', hours='Day-use areas 7 a.m. to sunset daily; gates close 9 p.m. April 15 to October 31, 6 p.m. otherwise'),

N('pleasant-ridge-baptist-church-weston-mo', 'Pleasant Ridge United Baptist Church', 'Weston', 'kcmo', 'worship', 'standing',
  39.43101, -94.85483, 'site', 'view', 'drive', 'cemeteries', '1844',
  'A country Baptist church built in 1844, a one-storey brick building about 35 by 51 feet under a front gable. '
  'The Pleasant Ridge Cemetery beside it has graves from 1848. Church and cemetery were listed on the National Register in 2002.',
  look='A plain brick meeting house of the 1840s with its burying ground, in farm country north-east of Weston. Interior not checked.',
  accn='At the corner of Route P and Woodruff Road. Whether it still holds services and who owns it were not found; see it from the road.',
  links=[W('Pleasant Ridge United Baptist Church')],
  brick='?'),

N('holy-trinity-church-weston-mo', 'Holy Trinity Catholic Church', 'Weston', 'kcmo', 'worship', 'standing',
  39.40961, -94.89914, 'exact', 'view', 'drive', '', '1844 or 1912; parish 1842',
  'The Catholic parish in Weston goes back to 1842, one of the oldest round Kansas City. The sources disagree about the building: Legends of America says Holy Trinity Church was built in 1844 on the hill on Cherry Street, '
  'while a 2009 church-history blog describes the present building as a neo-Gothic limestone church of 1912, with an altar that looks older than the church.',
  look='A limestone Gothic church high on Cherry Street, with a historical marker in front that tells the parish story. Interior not checked.',
  accn='An active parish church at 407 Cherry Street, Diocese of Kansas City-St. Joseph. The parish\'s own site answered 403 when this was written, so no service times are given here.',
  links=[LOA, ['The Steeplechase blog, 2009', 'https://thesteeplechase.blogspot.com/2009/12/holy-trinity-catholic-church-weston-mo.html']],
  conf='mixed', brick='no', hours='?'),

N('old-presbyterian-church-weston-mo', 'Old Presbyterian Church (Christian Assembly Church)', 'Weston', 'kcmo', 'worship', 'standing',
  39.41255, -94.90408, 'exact', 'view', 'drive', '', '1840s',
  'Built for Weston\'s Presbyterians in the 1840s, when the town was a river port; its bell was rung to tell dockworkers a steamboat was coming. '
  'The Register listing of the town calls it the old Presbyterian church and dates it to 1846. It is now the Christian Assembly Church and still in use.',
  look='The church at Washington and Thomas streets, on the slope above the old landing. Interior not checked.',
  accn='An active church at 501 Washington Street; see it from the street. Service times not checked.',
  links=[LOA, W('Weston Historic District')],
  brick='?'),

N('weston-methodist-church-mo', 'Weston United Methodist Church', 'Weston', 'kcmo', 'worship', 'standing',
  39.41201, -94.90130, 'exact', 'view', 'drive', '', '1868',
  'The Methodist church of 1868 on Main Street is one of the buildings the National Register listing of the Weston Historic District names. '
  'It was built in the years after the Civil War, when the town had lost its river trade but kept its churches.',
  look='A red brick church with a tall gabled front and a tower, in the middle of the Main Street blocks (photograph on Wikimedia Commons). What original fabric survives inside was not checked.',
  accn='An active church at 533 Main Street; see it from the street. Service times not checked.',
  links=[W('Weston Historic District')],
  brick='yes'),

N('laurel-hill-cemetery-weston-mo', 'Laurel Hill Cemetery', 'Weston', 'kcmo', 'burial', 'standing',
  39.41551, -94.89748, 'site', 'view', 'walk', 'cemeteries', 'about 1840',
  'Weston\'s old hillside cemetery, started about 1840. Members of many early Weston families lie here. '
  'Nearly 400 Black people are buried here in unmarked graves; in 2019 the town put up a monument to them.',
  look='Old stones on a steep hill above Welt Street, with wide views. Look for the 2019 monument to the unmarked graves.',
  accn='On Welt Street at the east side of town. The sources read do not say who owns or runs it or when it is open; it can be seen from the street.',
  links=[['KCUR, 2020: pocket cemeteries', 'https://www.kcur.org/arts-life/2020-10-19/lost-settlements-crimes-and-communities-kansas-citys-pocket-cemeteries-hold-buried-history'],
         ['Laurel Hill Cemetery (family history page)', 'https://jrm.phys.ksu.edu/Genealogy/Cemeteries/LaurelHill/LaurelHill.html']],
  brick='no'),

N('platte-county-courthouse-mo', 'Platte County Courthouse', 'Platte City', 'kcmo', 'civic', 'standing',
  39.37091, -94.78014, 'exact', 'view', 'drive', 'burned', '1866–1867',
  'The county\'s first courthouse, built in 1841, burned on a December night in 1861 when Union soldiers under Colonel W. James Morgan set fire to much of Platte City. '
  'After the war Peter McDuff of Weston drew this one, and it was finished in May 1867: a two-storey red brick building in a rough cross plan on a limestone foundation, with walls of locally fired brick 15 to 16 inches thick. '
  'Blanche Barrow of the Bonnie and Clyde gang was tried here in 1933. It was listed on the National Register in 1979.',
  look='The cross-plan brick courthouse with its three arched front doors. A 2025 renovation uncovered the original unplastered brick inside, plank floors and the old transom glass; a shoeshine chair with railings made from the first stair banisters stands in the lobby. Whether the work is finished was not checked.',
  hook='Burned by Union troops, rebuilt in brick, and the place Blanche Barrow was tried.',
  accn='Platte County government, at Third and Main streets in Platte City. It was closed inside for renovation in summer 2025; whether it has reopened was not checked. Street parking.',
  links=[W('Platte County Courthouse (Missouri)'), W('Platte City, Missouri'),
         ['Platte County Landmark, 2025', 'https://plattecountylandmark.com/2025/08/21/a-walk-back-through-time-at-the-platte-county-courthouse/']],
  brick='yes'),

N('krause-mansion-platte-city-mo', 'Frederick Krause Mansion (Ben Ferrel Platte County Museum)', 'Platte City', 'kcmo', 'landmark', 'standing',
  39.36941, -94.78119, 'exact', 'open', 'drive', '', '1882–1883',
  'Frederick Krause, an immigrant from Prussia who settled in Platte City in the early 1860s as a builder, butcher and stock farmer, built this house in 1882–1883 from bricks fired in his own brickworks. '
  'It is called the mini-mansion because it copies features of the Missouri Governor\'s Mansion: red brick, limestone corner quoins, a mansard roof of slate, cast-iron cresting and a bronze fireplace surround. '
  'The Platte County Historical Society and the Daughters of the American Revolution bought it in 1977 with a bequest from Ben Ferrel, and it opened as a museum in 1985.',
  look='A two-storey Second Empire house of red brick with a mansard roof of grey-blue and rose hexagonal slate, ironwork along the roof and porches. Inside: furnishings from local families, mostly 1840 to 1920, and the society\'s research room.',
  accn='Platte County Historical Society, Third and Ferrel streets. Its own site could not be opened when this was written. A 2022 newspaper report gave Thursdays and Fridays 1 to 4 p.m., with group tours by appointment and $5 for adults; check before going.',
  links=[W('Frederick Krause Mansion'), ['Ben Ferrel Museum newsletter archive', 'https://benferrelmuseum.blog/'],
         ['Platte County Landmark, 2022', 'https://plattecountylandmark.com/2022/10/07/the-man-who-built-local-museum/']],
  brick='yes', hours='?'),

]

BATCH = {'key': 'kcmo_weston_afuv', 'label': 'Weston and Platte City, Missouri', 'added': '2026-11-23 05:07'}

PIN_NOTES = {
 'weston-historic-district-mo': 'Moved onto Main Street in the middle of the downtown blocks, seen on Esri satellite; the Wikipedia coordinate for the district falls about 165 m north-west, among houses.',
 'st-george-hotel-weston-mo': 'Pin is the street address 500 Main Street (map address lookup).',
 'weston-brewing-cellars-mo': 'Pin is the street address 500 Welt Street (map address lookup).',
 'holladay-distillery-weston-mo': 'Pin is the street address 1 McCormick Lane (map address lookup), on the distillery grounds.',
 'pirtle-winery-church-weston-mo': 'Pin is the street address 502 Spring Street (map address lookup).',
 'weston-historical-museum-mo': 'Pin is the street address 601 Main Street (map address lookup).',
 'weston-burley-house-1-mo': 'Pin is the Wikipedia coordinate for the warehouse; on Esri satellite it is on the roof of the large white-roofed shed.',
 'weston-bend-tobacco-barn-mo': 'OpenStreetMap maps two buildings named Tobacco Barn in the park; the pin is on the one by the Barn Trail parking, a barn seen on Esri satellite. Which barn is the one shown to visitors was not found.',
 'pleasant-ridge-baptist-church-weston-mo': 'Moved onto the cemetery, which shows plainly on Esri satellite about 100 m east of the Wikipedia coordinate (that falls in a field); a map listing for Pleasant Ridge Cemetery agrees. Which of the buildings near the road corner is the church was not settled, so the pin marks the churchyard.',
 'holy-trinity-church-weston-mo': 'Pin is the street address 407 Cherry Street (map address lookup).',
 'old-presbyterian-church-weston-mo': 'Pin is the OpenStreetMap point for the Christian Assembly Church, 501 Washington Street.',
 'weston-methodist-church-mo': 'Pin is the OpenStreetMap point for the church, 533 Main Street.',
 'laurel-hill-cemetery-weston-mo': 'Pin is the OpenStreetMap outline of the cemetery.',
 'platte-county-courthouse-mo': 'Moved onto the cross-shaped courthouse seen on Esri satellite; the address lookup for 328 Main Street fell on the street corner, and the new point matches the National Register point.',
 'krause-mansion-platte-city-mo': 'Pin is the street address 220 Ferrel Street (map address lookup).',
}
