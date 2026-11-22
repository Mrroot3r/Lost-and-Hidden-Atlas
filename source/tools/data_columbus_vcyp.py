# November 22, 2026: downtown Columbus and the Ohio State campus, from the names in one Old World Exploration video
# (job 9, "videos"; the record is source/videos/20230709_ja43hoeHWtI.md). The video was a tip only: every fact here is
# from a source opened in this session. Sources: Wikipedia articles (tools/wiki_raw.py) and the Register list for
# Columbus; the pages of the Orton Geological Museum, Columbus Recreation and Parks (Cultural Arts Center, McFerson
# Commons), Green Lawn Cemetery, the Columbus Metropolitan Library hours sheet, First Congregational Church and Broad
# Street United Methodist Church (tools/page.py). Pins from the ArcGIS geocoder's address points, checked on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'columbus_vcyp','label':'Columbus, Ohio: downtown and the Ohio State campus','added':'2026-11-22 01:32'}

DT='Downtown street parking and paid garages and lots; none checked.'

PLACES=[
N('leveque-tower-columbus','LeVeque Tower','Columbus','oh','civic','standing',39.96226,-83.00225,'exact','view','drive','','1924–1927',
  "A 47-storey Art Deco skyscraper by C. Howard Crane, opened in 1927 as the American Insurance Union Citadel. At 555 feet it was the city's tallest building until 1974 and was then the fifth tallest in the world; it was built with 600 hotel rooms in two wings and an attached vaudeville and movie house, the Palace Theatre. After the insurance union failed in the Depression it became the Lincoln-LeVeque Tower in 1946 and the LeVeque Tower in 1977. Owners who bought it in 2011 made it a mix of hotel, apartments, condominiums, offices and a restaurant, opened in 2017.",
  "The terracotta-faced tower, with its carved figures near the top; some of the upper ornament was taken down over fears of falling pieces and for penthouse views. The tower is lit for events several times a year. The Palace Theatre, attached, still runs as a 2,827-seat venue. Interior not checked.",
  "Columbus's Art Deco skyline tower, once fifth tallest in the world.",
  "A private building at 50 West Broad Street; the hotel, restaurant and Palace Theatre take the public, the offices and homes do not. "+DT,
  [W('LeVeque Tower')],brick='no'),

N('ohio-state-arsenal-columbus','Ohio State Arsenal (Cultural Arts Center)','Columbus','oh','fort','standing',39.95537,-83.00322,'exact','open','drive','','1861–',
  "A castle-like brick arsenal built in 1861 by prisoner labour, on a site the state penitentiary had used since 1814. It held weapons and horses during the Civil War and was listed on the National Register in 1974. The city leased it from the state for 99 years at a dollar a year and opened it in 1978 as the Cultural Arts Center, a gallery and teaching space for visual artists, renamed for Priscilla R. Tyson.",
  "The Italianate arsenal of 1861 with its battlemented towers. Inside are galleries and studios (ceramics in the basement, painting and weaving upstairs), an eagle and shield from the battleship USS Ohio and a bell from the cruiser USS Columbus.",
  "A Civil War arsenal built by prisoners, now an art school.",
  "Owned by the state and run by Columbus Recreation and Parks at 139 West Main Street. Hours from the department's page for the center, which also lists classes and gallery openings. "+DT,
  [W('Cultural Arts Center'),['Columbus Recreation and Parks: Priscilla R. Tyson Cultural Arts Center','https://columbusrecparks.com/facilities/priscilla-r-tyson-cultural-arts-center/']],
  brick='?',hours='Tuesday to Saturday 9 a.m. to 4 p.m.'),

N('green-lawn-cemetery-columbus','Green Lawn Cemetery','Columbus','oh','burial','standing',39.9395,-83.02544,'area','public','walk','cemeteries','1848–',
  "Organized in 1848 and opened in 1849 by a group of Columbus business and civic leaders when the town's older burying grounds were full; families moved graves here from the Franklinton Cemetery and the North Graveyard. A Civil War soldiers' and sailors' memorial went up in 1891 and the domed Mortuary (Huntington) Chapel, designed by Frank Packard, was dedicated in 1902. At 360 acres it is Ohio's second-largest cemetery, with more than 160,000 burials; an 1898 iron bridge crosses a ravine between two sections.",
  "Old monuments, tombs and big trees across rolling ground (the oldest tree, a white oak, is thought to be over 315 years old). The Renaissance Revival chapel has a rotunda capped in red vitrified tile, two murals, mosaics and leaded and stained glass; its glass dome was restored in 2025–2026. Chapel interior opening not checked.",
  "Columbus's 1849 garden cemetery and its domed chapel.",
  "A private, active cemetery at 1000 Greenlawn Avenue; the cemetery has its own police. Grounds hours from its maps and resources page; office Monday to Friday 9 a.m. to 4:30 p.m. The pin is the office address; the chapel's place in the grounds was not checked. Parking along the cemetery drives.",
  [W('Green Lawn Cemetery (Columbus, Ohio)'),['Green Lawn Cemetery: maps and resources (hours)','https://www.greenlawncemetery.org/maps-and-resources']],
  brick='?',hours='March 15 to October 19 daily 7 a.m. to 7 p.m.; from October 20 daily 7 a.m. to 5 p.m.'),

N('hoster-brewing-columbus','L. Hoster Brewing Company buildings','Columbus','oh','industry','standing',39.95212,-83.00085,'site','view','drive','','about 1887–1967',
  "Louis Hoster founded his brewery in 1836 in what is now the Brewery District, and by 1892 it was the city's leading brewery and a household name in Ohio. Prohibition closed it after soda and imitation beer failed, and part of the building facing Front Street was demolished in 1965. In 2019 the site held eight buildings built from about 1887 to 1967, listed on the National Register; they were being redeveloped as Front & Fulton, with apartments, restaurants and offices, with completion put back to summer 2023.",
  "The surviving brick brewery buildings at Front and Fulton streets. Whether the Front & Fulton conversion is finished, and what is open inside, was not checked; the Hoster beer name is now brewed elsewhere in the city.",
  "The Brewery District's namesake brewery, turned into a new block.",
  "Private property at 477 South Front Street; look from the street. "+DT,
  [W('L. Hoster Brewing Company'),['Breakfast With Nick: After More Than 20 Years, Hoster Brewing Has a Home Again (2024)','https://breakfastwithnick.com/2024/04/12/hoster-brewing-columbus-ohio/']],
  conf='mixed',brick='?'),

N('broad-street-umc-columbus','Broad Street United Methodist Church','Columbus','oh','worship','standing',39.96353,-82.98719,'exact','open','drive','','1885–',
  "A Gothic Revival Methodist church built in 1885 to designs by Yost & Packard, one of five churches built on East Broad Street around the turn of the century, and an Akron Plan church. It was faced in green serpentine stone; the architects Rogers Krajnak later replaced the stone with a synthetic stone that keeps the green colour. It was listed on the National Register in 1980.",
  "The green-faced Gothic church and its corner. The traditional service is held in the historic sanctuary; the other two services meet in Triplett Hall. Interior details not checked.",
  "An 1885 church faced in green stone.",
  "An active congregation at 501 East Broad Street; service times from the church's own page. "+DT,
  [W('Broad Street United Methodist Church (Columbus, Ohio)'),['Broad Street United Methodist Church: worship','https://www.bsumc.org/worship-2']],
  brick='no',hours='Sunday 10:45 a.m. traditional service in the sanctuary; 8:30 and 10:45 a.m. services in Triplett Hall'),

N('first-congregational-columbus','First Congregational Church','Columbus','oh','worship','standing',39.96389,-82.98889,'exact','open','drive','','1931–',
  "The congregation was formed in 1852 by 42 abolitionists who left the Second Presbyterian Church; first called the Third Presbyterian Church, it took its present name in 1856, and Washington Gladden was its minister for 36 years. After a frame chapel and an 1857 church on East Broad Street it dedicated the present Gothic Revival church, designed by John Russell Pope, on December 6, 1931. It was listed on the Columbus Register in 1982 and the National Register in 2021.",
  "The stone Gothic church and its tower on East Broad Street. Interior not checked.",
  "John Russell Pope's Gothic church for an abolitionist congregation.",
  "An active congregation at 444 East Broad Street. Its plan-your-visit page gives the service times, free parking in the church's North and West lots, and an accessible entrance by the elevator; church office Monday to Friday 9 a.m. to 3 p.m.",
  [W('First Congregational Church (Columbus, Ohio)'),['First Congregational Church: plan your visit','https://www.first-church.org/plan-your-visit/']],
  brick='?',hours='Sunday worship 9 and 11 a.m.'),

N('great-southern-hotel-theatre-columbus','Great Southern Hotel and Southern Theatre','Columbus','oh','hotel','standing',39.95585,-82.99896,'exact','open','drive','','1894–1896',
  "After fires destroyed five downtown theatres between 1889 and 1893, local businessmen built \"The Great Southern Fireproof Hotel and Opera House\" on the southern edge of downtown, of tile, brick, iron, steel and concrete, to designs by Dauben, Krumm and Riebel. Begun in 1894, it opened on September 21, 1896, and made its own electricity. It is the oldest surviving theatre in central Ohio. It was listed on the National Register in 1982.",
  "The hotel, which operates as the Westin Great Southern Columbus, and the Southern Theatre behind it, a venue for concerts, plays and opera run by CAPA (the Columbus Association for the Performing Arts). Interior details not checked.",
  "The fireproof hotel and opera house of 1896, still both.",
  "A working hotel at 310 South High Street; the theatre is open for its performances. No opening or box-office hours were read in this session. "+DT,
  [W('Great Southern Hotel & Theatre')],brick='?',hours='?'),

N('us-post-office-courthouse-columbus','Old U.S. Post Office and Courthouse','Columbus','oh','civic','standing',39.96029,-82.99714,'exact','view','drive','','1884–1887',
  "Built from 1884 to 1887 as the city's main post office, in Romanesque Revival style by John T. Harris; it also held the federal district court until 1934. From 1907 to 1912 it was tripled in size and made over in High Victorian Gothic under James Knox Taylor. It was listed on the National Register in 1973 and rehabilitated in 1986 as the Bricker & Eckler law offices, which it still houses.",
  "Tan rock-faced Berea sandstone with smooth sandstone trim, round-arched windows under heavy hood moulds, the later Gothic arches and buttresses on the south part, and a red tile roof that replaced the slate. Not open to visitors.",
  "The 1887 post office that grew Gothic in 1912.",
  "Private law offices at 121 East State Street, across from the Statehouse; look from the street. "+DT,
  [W('United States Post Office and Courthouse (Columbus, Ohio)')],brick='no'),

N('main-library-columbus','Main Library, Columbus Metropolitan Library','Columbus','oh','civic','standing',39.96119,-82.98998,'exact','open','drive','','1903–1907',
  "Andrew Carnegie largely paid for the city's main library, designed by Albert Randolph Ross in Beaux-Arts style in white Vermont marble and opened in 1907, after years in a reading room in City Hall. It was enlarged in 1953 and 1961; a 1991 addition replaced those wings and tripled its size, and a 2015–2016 renovation opened it onto Topiary Park.",
  "The white marble Carnegie building at the front of the much larger modern library, which holds about 300,000 volumes, a reading room, a gallery and the Franklin County Genealogical and Historical Society on the third floor.",
  "A Carnegie library in white Vermont marble.",
  "A public library at 96 South Grant Avenue. Hours from the library's own hours sheet dated January 2024; check its site before going. "+DT,
  [W('Main Library (Columbus, Ohio)'),['Columbus Metropolitan Library: locations and hours (January 2024)','https://columbuslibrary.org/branch-address-location-hours-of-operations-2024-01']],
  brick='no',hours='Monday to Thursday 9 a.m. to 9 p.m.; Friday and Saturday 9 a.m. to 6 p.m.; Sunday 1 to 5 p.m. (as of January 2024)'),

N('orton-hall-osu','Orton Hall, Ohio State University','Columbus','oh','inst','standing',39.99838,-83.01192,'exact','open','walk','','1891–1893',
  "Authorized by the legislature in 1891 and opened in August 1893, the same year as Hayes Hall across the Oval, to house the Orton Geological Museum, the university library, classrooms and offices. It was built only of Ohio building stone, laid in the order of the rock layers, from Silurian at the base to Carboniferous near the top of the bell tower. With Hayes Hall it is on the National Register; the third building of that listing, the original University Hall, was torn down in 1971.",
  "The stone hall and bell tower on the Oval, with geological carvings inside and out; grotesques high on the tower show animals of the Mesozoic and Cenozoic. The tower chimes. The Orton Geological Museum inside is free and open to all.",
  "A building made of Ohio's rocks in the order they lie.",
  "Ohio State University, 155 South Oval Mall. Museum hours from its own visit page, which warns that hours on other websites are wrong and that summer weekday hours are irregular (ask first). Weekday parking: the Ohio Union South Garage, 1780 College Road South, a short way east.",
  [W('University, Hayes and Orton Halls'),['Orton Geological Museum: Orton Hall, a landmark building','https://ortonmuseum.osu.edu/about-museum/orton-hall-landmark-building'],['Orton Geological Museum: visit the museum','https://ortonmuseum.osu.edu/visit-its-free/visit-museum']],
  brick='no',hours='Late August to early May, Monday to Friday 10 a.m. to 4 p.m.; summer irregular; closed weekends'),

N('atlas-building-columbus','Atlas Building (Columbus Savings and Trust Building)','Columbus','oh','civic','standing',39.96528,-83.00083,'exact','view','drive','','1904–1905',
  "A thirteen-storey office tower designed by Frank Packard for the Columbus Savings & Trust Company; ground was broken in May 1904 and the Chicago firm John Griffiths and Son finished it in 1905. After the bank failed, Depositors Realty bought it in 1913, the year the new Athletic Club of Columbus made its first home there. It was listed on the National Register in 1977 and renovated in 1979–1982 and again in 2014.",
  "A skyscraper of its day in three distinct parts, topped by an elaborate terracotta cornice, facing Long Street with its west side on High Street. Interior not checked.",
  "A 1905 bank tower with a terracotta crown.",
  "A private building at 8 East Long Street; look from the street. "+DT,
  [W('Atlas Building')],brick='?'),

N('union-station-arch-columbus','Union Station arch','Columbus','oh','rail','standing',39.96814,-83.00741,'exact','public','walk','stations','1890s; moved 1980 and 1999',
  "The one piece left of the arcade Daniel Burnham designed for the entrance to Columbus's Union Station of the 1890s. The arcade was listed on the National Register in 1974, but Battelle, which owned it, had it demolished in October 1976 until a court order stopped the wreckers; the Ohio Historical Society was given 120 days to remove the single arch left standing. It went into storage in 1977, stood in Arch Park from 1980, and was moved again in 1999 to McFerson Commons, on what had been the edge of the Ohio Penitentiary. The station itself was demolished in 1979.",
  "A 35-foot Beaux-Arts arch with four fluted Corinthian columns, angels carved in the spandrels and eagle medallions in the frieze, standing alone as the centrepiece of the park. Some of its statuary is in storage.",
  "All that is left of Burnham's Union Station.",
  "McFerson Commons, a city park run by Columbus Recreation and Parks, in the Arena District. Park hours not given on its page. Parking: the McConnell Garage on John H. McConnell Boulevard, mapped 140 m northwest (paid; not checked).",
  [W('Union Station arch'),W('Union Station (Columbus, Ohio)'),['Columbus Recreation and Parks: McFerson Commons','https://columbusrecparks.com/parks/mcferson-commons/']],
  th=[39.96931,-83.00809],thn='McConnell Garage, John H. McConnell Boulevard',brick='?'),

N('downtown-ymca-columbus','Downtown YMCA (Central YMCA building)','Columbus','oh','civic','standing',39.96493,-83.00249,'exact','view','drive','','1921–1924',
  "A seven-storey YMCA in Jacobethan and Late Gothic Revival style by the Chicago YMCA architects Shattuck & Layer. Ground was broken in November 1921 and it was dedicated in January 1924, at a cost of $850,000; it was claimed as the largest YMCA in the world and was the largest YMCA residence in the United States. Its evening high school grew into Franklin University. Listed on the National Register in 1993, it was sold to the Columbus Downtown Development Corporation in March 2023, and the Columbus Landmarks Foundation put it on its most endangered list that June.",
  "Dark red Flemish-bond brick with light limestone trim, three-part windows, pointed arches, buttresses and battlements on the roofline. What it is used for now was not checked; not open to visitors.",
  "The world's biggest YMCA of 1924, now waiting on its future.",
  "Private property at 40 West Long Street; look from the street. "+DT,
  [W('Downtown YMCA')],conf='mixed',brick='yes'),

N('ohio-deaf-institution-columbus','Ohio Institution for the Deaf building (Cristo Rey Columbus High School)','Columbus','oh','civic','standing',39.96048,-82.98898,'site','view','drive','','1899–',
  "Built in 1899 as part of the Ohio Institution for the Deaf and Dumb (now the Ohio School for the Deaf), and listed on the National Register and the Columbus Register in 1984. The property stood empty for years; in 2013 the library bought it and resold the building to Cristo Rey Columbus High School, a Catholic work-study school, which restored it for $18 million.",
  "The restored 1899 school building beside Topiary Park, working again as a high school. Not open to visitors; interior not checked.",
  "The 1899 school for the deaf, a school again.",
  "A private school at 400 East Town Street; look from the street or from Topiary Park next door. "+DT,
  [W('Cristo Rey Columbus High School'),W('Main Library (Columbus, Ohio)')],brick='no'),
]

PIN_NOTES={
 'leveque-tower-columbus':'ArcGIS geocoder PointAddress for 50 W Broad St; checked on the aerial.',
 'ohio-state-arsenal-columbus':'ArcGIS geocoder PointAddress for 139 W Main St, a few metres from the Register point; checked on the aerial.',
 'green-lawn-cemetery-columbus':'ArcGIS geocoder PointAddress for 1000 Greenlawn Ave; on the aerial it falls on a cross-shaped domed building near the entrance, which may be the chapel (not confirmed); the cemetery spreads far to the west and south, so prec is area.',
 'hoster-brewing-columbus':'ArcGIS geocoder PointAddress for 477 S Front St, 20 m from the Wikipedia point; checked on the aerial.',
 'broad-street-umc-columbus':'ArcGIS geocoder PointAddress for 501 E Broad St; checked on the aerial.',
 'first-congregational-columbus':'ArcGIS geocoder PointAddress for 444 E Broad St, 30 m from the Wikipedia point; checked on the aerial.',
 'great-southern-hotel-theatre-columbus':'ArcGIS geocoder PointAddress for 310 S High St; checked on the aerial.',
 'us-post-office-courthouse-columbus':'The geocoder gave a street point for 121 E State St in the road; moved with pix.py 50 m onto the red-tiled roof of the building at Third and State seen on the aerial (the article names its red tile roof).',
 'main-library-columbus':'ArcGIS geocoder PointAddress for 96 S Grant Ave, 10 m from the Wikipedia point; checked on the aerial.',
 'orton-hall-osu':'ArcGIS geocoder PointAddress for 155 S Oval Mall; checked on the aerial.',
 'atlas-building-columbus':'ArcGIS geocoder PointAddress for 8 E Long St; checked on the aerial.',
 'union-station-arch-columbus':'Wikipedia coordinate for the arch in McFerson Commons; checked on the aerial.',
 'downtown-ymca-columbus':'ArcGIS geocoder PointAddress for 40 W Long St; checked on the aerial.',
 'ohio-deaf-institution-columbus':'ArcGIS geocoder PointAddress for 400 E Town St; the Wikipedia point for the school is 2.9 km west and wrong. Checked on the aerial.',
}
