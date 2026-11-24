# November 24, 2026: Fall River, Bristol County, Massachusetts. The Atlas had nothing in the city.
# The names came from a walk-through video of the city's old buildings, taken only as a list of names to look up.
# Facts from the linked sources only: Wikipedia read as raw text (the articles and the city's National Register list and list of
# mills), the Diocese of Fall River's page for the cathedral, and the Fall River Public Library's own hours page.
# Church service times were not found on any page of the parishes' own, so those churches carry no hours.
from data_b import N
from data_ma import W

NRHP = ['Wikipedia: National Register listings in Fall River', 'https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Fall_River,_Massachusetts']
MILLS = ['Wikipedia: list of mills in Fall River', 'https://en.wikipedia.org/wiki/List_of_mills_in_Fall_River,_Massachusetts']
CITY = W('Fall River, Massachusetts')
STREET = 'Downtown Fall River: metered street parking and public lots; nothing to arrange to look from the sidewalk.'

BATCH = {'key': 'fallriver_clou', 'label': 'Fall River, Massachusetts', 'added': '2026-11-24 13:32'}

PLACES = [
N('academy-building-fall-river', 'Academy Building (Borden Block)', 'Fall River', 'south', 'civic', 'standing',
  41.70049, -71.15567, 'exact', 'view', 'drive', '', '1875–1876',
  'Built in 1875 as a memorial to Nathaniel Briggs Borden by his widow and children, and opened on January 6, 1876, with a theatre, the Academy of Music, inside. '
  'It held the city\'s first telephone exchange from 1879 to 1890. It decayed in the 1960s and 1970s, the city\'s redevelopment authority bought it in 1973 meaning to pull it down, and it was restored in the 1980s instead, losing the theatre.',
  look='A four-story Ruskinian Gothic block by the Boston architects Hartwell and Swasey, with polychrome brick and carved stone, on South Main Street. '
       'Senior apartments above and shops at street level; the inside is not open to visitors. Photographed for the Historic American Buildings Survey in 1979.',
  accn='Privately owned apartments with street-level shops, on South Main Street across from City Hall. ' + STREET,
  links=[W('Academy Building (Fall River, Massachusetts)'), NRHP], brick='yes'),

N('central-congregational-church-fall-river', 'Central Congregational Church (The Historic Abbey)', 'Fall River', 'south', 'worship', 'standing',
  41.70288, -71.15366, 'exact', 'view', 'drive', '', '1875',
  'A church built in 1875 to designs by Hartwell and Swasey, at 100 Rock Street. It was the church of Lizzie Borden and her family; she taught Sunday school here. '
  'In the 1990s and 2000s the church and its abbey became a culinary school with a restaurant, which closed in March 2009. Since 2019 it has been an events hall, The Historic Abbey.',
  look='A red brick church with pale stone trim, a rose window and a tall pointed spire banded in brick and stone (as photographed for Wikipedia), on Rock Street in the Highlands. A Hook and Hastings pipe organ is in the main hall, according to Wikipedia. Inside only for events held there; interior otherwise not checked.',
  accn='A private events venue. Look from Rock Street and Bank Street; on-street parking.',
  links=[W('Central Congregational Church (Fall River, Massachusetts)'), NRHP], brick='yes'),

N('church-of-the-ascension-fall-river', 'Church of the Ascension (Church of the Holy Spirit)', 'Fall River', 'south', 'worship', 'standing',
  41.70398, -71.15302, 'site', 'view', 'drive', '', '1875',
  'Fall River\'s first Episcopal parish, formed in 1836, worshipped in borrowed halls and an old Baptist church until this church on Rock Street was dedicated on November 29, 1875. '
  'A Tudor Revival parish house by Angell and Swift was added in 1910. Since 2008 the parish has been called the Church of the Holy Spirit.',
  look='A Victorian Gothic church of Fall River granite with red brick and Scotch stone trim, with a buttressed square tower, a crenellated cap and stone corner pinnacles, an attached chapel and a side garden. Interior not checked.',
  accn='An active Episcopal church at 160 Rock Street. Look from the street; on-street parking. No service times were found on a page of the parish\'s own.',
  links=[W('Church of the Ascension (Fall River, Massachusetts)'), NRHP], brick='some', hours='?'),

N('bmc-durfee-high-school-1886-fall-river', 'B.M.C. Durfee High School (1886 building)', 'Fall River', 'south', 'civic', 'standing',
  41.70555, -71.15168, 'exact', 'view', 'drive', '', '1883–1887',
  'Mary B. Young gave the school to the city in memory of her son, Bradford Matthew Chaloner Durfee, who died young in 1872. The Boston architect George A. Clough designed it; ground was broken in August 1883 and it was dedicated on June 15, 1887. '
  'A new high school replaced it in 1978. It stood empty until the early 1990s, when the Commonwealth restored it as a probate and family court.',
  look='A big stone school on a hilltop at 289 Rock Street, seen from much of the city: the first story is Fall River granite and the stone above it came from Mason, New Hampshire. Now a working courthouse.',
  accn='A state courthouse (Bristol Probate and Family Court). Look from Rock Street; going in is for court business. On-street parking.',
  links=[W('B.M.C. Durfee High School (1886 building)'), NRHP], brick='no'),

N('st-anne-shrine-fall-river', "St. Anne's Church and Shrine", 'Fall River', 'south', 'worship', 'standing',
  41.69389, -71.16389, 'exact', 'view', 'drive', '', '1891–1906',
  'A French-Canadian parish church and pilgrimage shrine run by the Dominicans from 1891 to 1978. Napoleon Bourassa of Canada designed it in the Romanesque Revival style; work began in 1891, the upper church was started in 1902 and dedicated on July 4, 1906. '
  'The upper church was shut in May 2015 when plaster fell during Mass, and the parish closed in 2018. The lower crypt shrine reopened on July 4, 2019; the upper church stays closed for repair.',
  look='A church of blue marble from Proctor, Vermont, 277 feet long with two 160-foot steeples, at South Main and Middle streets. The complex also holds the former Dominican monastery and the 1894 Dominican Academy. '
       'The lower church is open for worship; the upper church is closed. Father Vincent Marchildon and two other Dominican founders are buried in the crypt.',
  accn='A shrine of the Diocese of Fall River, 818 Middle Street. Look from South Main Street, Middle Street and Kennedy Park across the road. Service times were not found on the shrine\'s own pages.',
  links=[W('St. Anne Shrine of Fall River'), NRHP], brick='no', hours='?'),

N('st-marys-cathedral-fall-river', 'Cathedral of St. Mary of the Assumption', 'Fall River', 'south', 'worship', 'standing',
  41.69861, -71.15778, 'exact', 'view', 'drive', '', '1852–1856',
  'The oldest church building left in Fall River. Its cornerstone was laid on August 8, 1852, on the site of the small frame church of St. John the Baptist, which stayed in use inside the new walls until the roof went on. '
  'It became a cathedral when the Diocese of Fall River was created in 1904. The Lady Chapel was finished in 1869; the rectory, joined to the church by a colonnade, dates from 1927.',
  look='Granite throughout, the 190-foot steeple included, with a rose window in the main gable. Inside, three naves divided by granite columns, intricate woodwork and some gilding above the sanctuary (Wikipedia). Daily Mass is said in the Lady Chapel, according to the diocese.',
  accn='The cathedral of the Diocese of Fall River, 327 Second Street. Look from Second and Spring streets; on-street parking. Service times were not given on the diocese\'s page for it.',
  links=[W('Cathedral of St. Mary of the Assumption (Fall River, Massachusetts)'), ['Diocese of Fall River: the cathedral', 'https://www.fallriverdiocese.org/parish/cathedral-of-saint-mary-of-the-assumption/'], NRHP],
  brick='no', hours='?'),

N('st-patricks-church-fall-river', "St. Patrick's Church", 'Fall River', 'south', 'worship', 'standing',
  41.68539, -71.17327, 'exact', 'view', 'drive', '', '1881',
  'A granite church of 1881 at 1598 South Main Street. The parish was split from the Irish parish of St. Mary\'s in 1873. '
  'In 2002 it merged with two neighbours as the Parish of the Good Shepherd, and in 2018 it joined the Catholic Community of Central Fall River.',
  look='A church of local Fall River granite; Wikipedia files it among the buildings of Patrick Keely. Interior not checked.',
  accn='An active Catholic church (Good Shepherd Parish), 1598 South Main Street. Look from the street; on-street parking. Service times were not found on a page of the parish\'s own.',
  links=[W("St. Patrick's Church (Fall River, Massachusetts)"), NRHP], brick='no', hours='?'),

N('oak-grove-cemetery-fall-river', 'Oak Grove Cemetery', 'Fall River', 'south', 'burial', 'standing',
  41.70528, -71.13722, 'site', 'public', 'drive', 'cemeteries', '1855',
  'The city\'s chief cemetery, set out from 1855 by the local architect Josiah Brown, who also designed early mills such as the Union and Border City, in the garden style of Mount Auburn in Cambridge. '
  'It began with 47 acres and now has over 120. Mill owners and merchants are buried here, and it holds the city\'s Civil War monument, given by Richard Borden.',
  look='A Gothic Revival entrance arch of Fall River granite on Prospect Street, winding lanes, the Civil War monument and the monuments of the city\'s mill families.',
  accn='Owned and run by the City of Fall River (Cemeteries Division, under the park commissioners), 765 Prospect Street. Drive in through the gate; park along the lanes. Opening hours were not given on the city\'s page.',
  links=[W('Oak Grove Cemetery (Fall River, Massachusetts)'), ['City of Fall River: cemeteries', 'https://www.fallriverma.gov/departments/public_works/cemeteries___trees/'], NRHP],
  brick='?'),

N('fall-river-waterworks', 'Fall River Waterworks', 'Fall River', 'south', 'water', 'standing',
  41.69643, -71.12661, 'exact', 'view', 'drive', '', '1872–1875',
  'Built from 1872 to 1875 on the shore of North Watuppa Pond, after the city\'s fast growth made a water board necessary in 1871; the high-service system began work in 1875. '
  'It still supplies the city and some of its neighbours, about 11 million gallons a day.',
  look='The original granite buildings, mostly Ruskinian Gothic: the engine house, boiler house and coal house, the intake house, and a 121-foot standpipe tower. The Register listing also takes in the 1908 Narrows gate house at the south end of the pond. Modern plant stands beside them.',
  accn='A working city water plant at the east end of Bedford Street, not open to visitors. Look from Bedford Street.',
  links=[W('Fall River Waterworks'), NRHP], brick='no'),

N('durfee-mills-fall-river', 'Durfee Mills', 'Fall River', 'south', 'industry', 'standing',
  41.69833, -71.14972, 'site', 'view', 'drive', '', '1866–1904',
  'A cotton mill company founded in 1866 with B.M.C. Durfee as its chief stockholder and named for his father, Bradford Durfee. Mill No. 1 was built in 1866, No. 2 in 1871 and No. 3 in 1881; the company was wound up in 1935. '
  'It was the city\'s largest and finest mill complex, and the most complete of its 19th-century mills left.',
  look='Two facing five-and-a-half-story granite mills with seven-story Italianate towers, a third mill at Pleasant Street and Plymouth Avenue, and many low granite outbuildings, the main office among them. With the Union Mills next door it holds shops and a restaurant (Durfee-Union Mills).',
  accn='Privately owned; the buildings hold shops, whose parking lots are off Pleasant Street. Look from Pleasant Street and Plymouth Avenue.',
  links=[W('Durfee Mills'), NRHP], brick='no'),

N('metacomet-mill-fall-river', 'Metacomet Mill', 'Fall River', 'south', 'industry', 'standing',
  41.702778, -71.161667, 'area', 'view', 'drive', '', '1847',
  'Built by Richard Borden in 1847 on Anawan Street. Wikipedia\'s article on the city calls it the oldest textile mill left in Fall River, and its list of mills the oldest cloth-making mill left; the city\'s National Register list gives "oldest remaining mill" to Oliver Chace\'s Thread Mill instead. '
  'It is on the Register with the American Printing Company buildings round it.',
  look='A granite mill of 1847 on Anawan Street, near the brick American Printing Company Mill No. 7 of 1906 built over the falls of the Quequechan River. Which building on Anawan Street is the 1847 mill was not settled from a source here.',
  accn='Privately owned. Look from Anawan Street, near Battleship Cove and the Marine Museum. ' + STREET,
  links=[CITY, MILLS, NRHP], brick='no', conf='mixed'),

N('truesdale-hospital-fall-river', 'Truesdale Hospital', 'Fall River', 'south', 'inst', 'standing',
  41.72853, -71.13501, 'exact', 'view', 'drive', '', '1912–1927',
  'Dr. Philemon E. Truesdale founded the hospital in 1905 in a parsonage downtown. The building on Highland Avenue was built in 1912 (the Register list gives 1920), with a south wing in 1923 and a surgical wing in 1927. '
  'It ran a nursing school from 1912 to 1972 and merged with Union Hospital in 1980 as Charlton Memorial Hospital. The building is now apartments, The Highlands.',
  look='The former hospital at 1820 Highland Avenue, now apartments: a long building of pale yellow brick with a columned entrance porch, on a lawn (as photographed for Wikipedia).',
  accn='Private apartments. Look from Highland Avenue only.',
  links=[W('Truesdale Hospital'), NRHP], brick='no', conf='mixed'),

N('jesus-marie-convent-fall-river', 'Jesus Marie Convent', 'Fall River', 'south', 'inst', 'standing',
  41.69083, -71.13222, 'site', 'view', 'drive', '', '1887',
  'A convent of 1887 for the French-Canadian parish of Notre Dame de Lourdes, designed by the parish member Louis G. Destremps, who also drew its orphanage, school and church. '
  'It housed Jesus Marie Academy, a girls\' high school, until 1971, then a home for retired religious, and after its listing in 1983 became apartments, Lafayette Place.',
  look='A four-story Second Empire brick convent with a west-facing central tower, Italianate window heads and dentils at the cornice, at 138 St. Joseph Street. An auditorium of 1939 stands to the north and newer buildings to the west.',
  accn='Private apartments. Look from St. Joseph Street.',
  links=[W('Jesus Marie Convent (Fall River, Massachusetts)'), NRHP], brick='?'),

N('st-josephs-orphanage-fall-river', "St. Joseph's Orphanage", 'Fall River', 'south', 'inst', 'standing',
  41.69167, -71.13294, 'exact', 'view', 'drive', '', '1892',
  'An orphanage built in 1892 for Notre Dame de Lourdes, the French-Canadian parish of Flint Village; two wings were added about 1917. It later held an elementary school, Mount Saint Joseph. '
  'From 1982 to 1986 its chapel served as Notre Dame\'s church after the parish\'s granite church of 1895 burned on May 11, 1982. It became apartments in 1989.',
  look='The former orphanage at 56 St. Joseph Street, now apartments with a large addition on the north side. The statue of St. Joseph that stood in the alcove at the top of the front now stands on the grounds of Notre Dame Church nearby.',
  accn='Private apartments. Look from St. Joseph Street.',
  links=[W("St. Joseph's Orphanage (Fall River, Massachusetts)"), W('Notre Dame de Lourdes Church (Fall River, Massachusetts)'), NRHP], brick='?'),

N('fall-river-public-library', 'Fall River Public Library', 'Fall River', 'south', 'civic', 'standing',
  41.70344, -71.15538, 'exact', 'open', 'drive', '', '1899',
  'The library was founded in 1861 and has been at 104 North Main Street since 1899. It stands in the Downtown Fall River Historic District.',
  look='The 1899 library building on North Main Street, open to anyone during library hours; it also houses the Fall River Room of local history. Original interior fabric not checked.',
  accn='Run by the City of Fall River, 104 North Main Street. Hours from the library\'s own page, read November 2026. ' + STREET,
  links=[['Fall River Public Library: hours and contact', 'https://fallriverlibrary.org/hours-and-contact/'], CITY],
  brick='no', hours='Monday to Thursday 8 a.m. to 8 p.m.; Friday and Saturday 9 a.m. to 4:30 p.m. (hours may vary)'),
]

PIN_NOTES = {
  'academy-building-fall-river': 'OpenStreetMap\'s building outline for the Academy Building on South Main Street.',
  'central-congregational-church-fall-river': 'OpenStreetMap\'s point for the church.',
  'church-of-the-ascension-fall-river': 'The address point for 160 Rock Street from the ArcGIS geocoder. The Wikipedia and National Register coordinate lies about 320 m further south, below the number 100 Rock Street of Central Congregational, so it was not used; the aerial does not settle which roof is the church.',
  'bmc-durfee-high-school-1886-fall-river': 'The address point for 289 Rock Street from the ArcGIS geocoder, on the large building east of Rock Street; the Wikipedia coordinate was in the street.',
  'st-anne-shrine-fall-river': 'The Wikipedia coordinate for the church.',
  'st-marys-cathedral-fall-river': 'The Wikipedia coordinate for the cathedral.',
  'st-patricks-church-fall-river': 'The address point for 1598 South Main Street from the ArcGIS geocoder; the Register list coordinate was in the street.',
  'oak-grove-cemetery-fall-river': 'The Wikipedia coordinate, inside the cemetery.',
  'fall-river-waterworks': 'OpenStreetMap\'s outline of the 1875 water tower (121 feet) beside Bedford Street; the National Register list coordinate was out in North Watuppa Pond.',
  'durfee-mills-fall-river': 'The Wikipedia coordinate for the mill complex.',
  'metacomet-mill-fall-river': 'The National Register list coordinate for the American Printing Company and Metacomet Mill listing; it marks the group on Anawan Street, not one building.',
  'truesdale-hospital-fall-river': 'OpenStreetMap\'s outline for The Highlands apartments, the former hospital.',
  'jesus-marie-convent-fall-river': 'The Wikipedia coordinate for the convent.',
  'st-josephs-orphanage-fall-river': 'OpenStreetMap\'s outline for St. Joseph\'s Orphanage at 56 St. Joseph Street.',
  'fall-river-public-library': 'OpenStreetMap\'s point for the library at 104 North Main Street.',
}
