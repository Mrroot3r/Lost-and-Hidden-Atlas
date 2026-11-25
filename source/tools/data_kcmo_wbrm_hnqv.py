# November 25, 2026: the West Bottoms, the River Market and the West Side, Kansas City, Missouri.
# Part of filling in the Kansas City area on purpose for a local researcher. The Atlas had none of these buildings.
# Facts are from the linked sources only: Clio's West Bottoms Walking Tour pages (read with tools/page.py), the Clio page for
# Richards and Conover, Wikipedia (read as raw text) for the Cold Storage building and St. Mary's, and a 2018 Flatland KC
# article for the Peppard House. The National Register forms could not be read (the Park Service holds only a placeholder
# and the Missouri copies no longer open), so nothing here comes from a Register form. Pins are street addresses looked
# up on the Esri geocoder and then looked at on the aerial.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_wbrm_hnqv', 'label': 'Kansas City: West Bottoms, River Market and West Side', 'added': '2026-11-25 13:52'}

CLIO = 'West Bottoms Walking Tour (Clio)'
BOT = 'In the West Bottoms, the flat ground beside the Kansas and Missouri rivers where Kansas City\'s railroads, stockyards and wholesale houses stood.'
STREET = 'Private building; look at it from the public street. Parking is on the street or in the small lots between the old warehouses. '

PLACES = [
N('kc-bolt-nut-screw-west-bottoms-kc', 'Kansas City Bolt, Nut and Screw Company building (Bella Patina)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.1009, -94.6013, 'area', 'open', 'drive', '', '1891',
  'Two old industrial buildings face West 12th Street in the West Bottoms. Their earliest known tenants, in 1891, were the Whitman and Barnes Manufacturing Company, which sold farm implements, and the Crane Bros. Machine Supply Company. The Kansas City Bolt, Nut and Screw Company, founded in 1888 with a factory in the East Bottoms, held the site from about 1950. '
  'Since 2011 the building has housed Bella Patina Vintage Revival, an antiques market.',
  look='Plain multi-storey warehouse fronts on West 12th Street. The market fills three floors inside, and its goods have been used in film work (Clio). Original interior fabric was not checked.',
  accn='Private building, 1324 West 12th Street. Clio says the market opens one weekend a month; the days were not confirmed on a page read. Street parking in the West Bottoms.',
  links=[[CLIO + ': Kansas City Bolt, Nut and Screw Company', 'https://theclio.com/tour/3025/3']],
  hours='?', brick='yes'),

N('studebaker-stowe-hardware-building-kc', 'Studebaker Brothers building (Stowe Hardware Building)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.09991, -94.6007, 'site', 'open', 'drive', '', '1903',
  'Finished in 1903 as the Kansas City distribution centre of the Studebaker Brothers Company, which then made buggies and carriages and soon began making automobiles. Clio calls the nine-storey brick building, 120 by 127 feet, the largest in the West Bottoms. Its tower held a wooden water tank for the sprinklers. '
  'Stowe Supply (later Stowe Hardware) bought it in 1918 and stayed until the company closed in 1991. It was storage for years, and antique shops and an event space moved in from the early 2000s.',
  look='A tall brick warehouse with a water tower on its roof, the most prominent building on its block. Antique shops, including Serendipity and the Ugly Glass Company, and an event space use it now (Clio). Interior beyond the shops was not checked.',
  accn='Private building, 1300 West 13th Street. The shops keep their own hours, which no page read gives. Street parking.',
  links=[['Clio: The Studebaker Brothers Building (1903-1918), Stowe Hardware Building (1918-1991)', 'https://theclio.com/tour/3025/5']],
  hours='?', brick='?'),

N('john-deere-distribution-center-beast-kc', 'John Deere Plow Company distribution centre (The Beast)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.09943, -94.60193, 'site', 'open', 'drive', '', '1890',
  'John Deere built a five-storey brick warehouse here in 1890 for $60,000, at 13th and Hickory, to receive and ship farm implements across the Great Plains. A second building went up beside it to the south in 1893. The Great Flood of 1951 damaged the lower floors, and in 1953 the company moved to higher ground at 3210 East 85th Street. '
  'The buildings were then leased out as warehouses. Since 1991 the main building has been a seasonal haunted house, the Beast.',
  look='A big brick warehouse of the 1890s on West 13th Street; the haunted house is open in season and is the way inside. Its sister houses, the Edge of Hell and Macabre Cinema, are nearby. Original interior fabric was not checked.',
  accn='Private building, 1401 West 13th Street, run as a haunted-house attraction. Its season and hours were not found on a page read. Street parking.',
  links=[['Clio: The John Deere Company Distribution Center (1890-1953), The Beast (1991- )', 'https://theclio.com/tour/3025/6']],
  hours='?', brick='?'),

N('parlin-orendorff-oliver-plow-building-kc', 'Parlin and Orendorff plow building (Oliver Chilled Plow, Central Bag)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.0994, -94.60118, 'site', 'open', 'drive', '', '1898',
  'The Parlin and Orendorff Plow Company, one of the country\'s big makers of plows and farm implements, put up this six-storey factory, warehouse and office in 1898 at 1323 West 13th Street. The Oliver Chilled Plow Company bought it in 1920. In 1946 the Central Bag Company, which had made cloth and burlap bags in the West Bottoms since 1929, bought it and stayed until 2010. '
  'Investors then bought it; the upper floors have been stripped back to the original brick and wood framing and let as office and event space.',
  look='A six-storey industrial building from 1898. Inside, the upper floors show the original brick walls and wood framing (Clio). A coffee shop and antique stores are on the ground floor.',
  accn='Private building, 1323 West 13th Street, with shops on the ground floor that keep their own hours (none found on a page read). Street parking.',
  links=[['Clio: Central Bag Company; Parlin-Orrendorf Company, Oliver Chilled Plow Company', 'https://theclio.com/tour/3025/7']],
  hours='?', brick='some'),

N('keystone-implement-building-kc', 'Keystone Implement Company building (West Bottoms Whiskey)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.0994, -94.60085, 'site', 'open', 'drive', '', '1895',
  'The Keystone Implement Company, a maker of plows, threshers, wagons and buggies, built this building in 1895 to replace a frame one of 1879 that burned. The Parlin-Orendorff Company bought it in 1900 and added a fifth floor, and the Oliver Chilled Plow Company took over the complex in 1920. '
  'It was leased as warehouse space and stood empty from the early 1980s. Today it is an event space for weddings and the home of the West Bottoms Whiskey Company.',
  look='A five-storey industrial building of 1895 beside the Parlin-Orendorff plant, with a whiskey distillery and event rooms inside. Whether the distillery takes visitors was not checked.',
  accn='Private building, 1321 West 13th Street; the distillery and event space set their own hours, not found on a page read. Street parking.',
  links=[['Clio: Keystone Implement Company (1879-1898), Parlin-Orendorff (1898-1919), Oliver Chilled Plow Company (1920-1946); West Bottoms Whiskey', 'https://theclio.com/tour/3025/8']],
  hours='?', brick='?'),

N('adams-building-west-bottoms-kc', 'Charles Francis Adams Jr. Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.0993, -94.6006, 'site', 'view', 'drive', '', '1883',
  'Charles Francis Adams Jr., great-grandson of John Quincy Adams, had this building put up in 1883 on prime ground between Union Depot and the stockyards. Its first tenant was the Buford and George Company, a farm-implement firm. A fire in 1894 destroyed the original building, and it was rebuilt; Buford and George stayed until 1903. '
  'John Deere later used it for saddlery and harness until 1913. It is now loft apartments with a barbershop and salon on the ground floor.',
  look='A late nineteenth-century commercial building at 1311 West 13th Street, now apartments, with a barbershop and salon on the street level. The West Bottoms Whiskey Company is next door (Clio).',
  accn='Private apartment building; look from the street. Street parking in the West Bottoms.',
  links=[['Clio: Charles Francis Adams Jr. Building', 'https://theclio.com/tour/3025/9']],
  brick='?'),

N('lowe-brothers-paint-edge-of-hell-kc', 'Lowe Brothers Paint and Varnish warehouse (The Edge of Hell)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10098, -94.60007, 'site', 'open', 'drive', '', '1915',
  'Built in 1915 as the Kansas City warehouse of the Lowe Brothers Paint and Varnish Company, which Sherwin-Williams owned until it dropped the brand in 1972. The building was left empty and decayed until 1988, when Full Moon Productions bought it for the Edge of Hell, a haunted house that Clio calls the oldest continuously operating commercial one in the United States (founded 1975). '
  'It sits at the end of a row of brick warehouses built after the 12th Street bridge was rebuilt in 1915 and the houses on this side of the street came down.',
  look='A brick warehouse at 1300 and 1302 West 12th Street, the last in a row of 1915 warehouses. The haunted house runs through its floors and ends in a five-storey slide.',
  accn='Private building run as a seasonal haunted-house attraction. Its season and hours were not found on a page read. Street parking.',
  links=[['Clio: Lowe Brothers Paint and Varnish Building (1915-1972), The Edge of Hell (1988- )', 'https://theclio.com/tour/3025/10']],
  hours='?', brick='yes'),

N('advance-rumely-thresher-building-kc', 'Advance-Rumely Thresher Company building (Macabre Cinema)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.1009, -94.599, 'area', 'open', 'drive', '', '1915',
  'Built in 1915 at 1222 West 12th Street for the Advance-Rumely Thresher Company, one of over a dozen farm-implement makers with a distribution house in the West Bottoms. Allis-Chalmers bought the company in 1931 and used the building for tractors until the 1951 flood. It then became leased warehouse space and stood empty from 1997. '
  'A haunted house, Macabre Cinema, took part of it in 2003, and the Rumely Tractor Historic Event Space has used the west half since 2012.',
  look='A 1915 industrial building on the north side of West 12th Street, with two floors renovated as an event space. Original interior fabric beyond that was not checked.',
  accn='Private building; the haunted house and event space keep their own hours, none found on a page read. Street parking.',
  links=[['Clio: The Advance-Rumely Thresher Company Building', 'https://theclio.com/tour/3025/11']],
  hours='?', brick='?'),

N('avery-holsum-studios-building-kc', 'B. F. Avery and Sons plow building (Holsum Studios)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.1009, -94.59855, 'site', 'open', 'drive', '', '1915',
  'Built about 1915 at 1200 West 12th Street for the B. F. Avery and Sons Plow Company, a distribution centre for plows, tractors and farm implements until 1931. In 1935 it became a factory for the Holsum Food Products Company, which made bread, peanut butter, jelly and pickles. '
  'Haunted houses used it in the 1990s and early 2000s. In 2019 the owners fitted it out as studios, and over 30 artists work there.',
  look='One of the row of brick industrial buildings that replaced houses on West 12th Street in 1915. It holds working artists\' studios; whether they open to visitors was not checked.',
  accn='Private building. Studio hours were not found on a page read. Street parking.',
  links=[['Clio: B.F. Avery & Sons (1915-1931), Holsum Food Products (1935-1980), Holsum Studios (2019- )', 'https://theclio.com/tour/3025/12']],
  hours='?', brick='?'),

N('english-morse-the-ship-kc', 'English, Morse and Company warehouse (The Ship)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.1022, -94.59921, 'exact', 'open', 'drive', '', '1888',
  'Built in 1888 at 1217 to 1221 Union Avenue as a warehouse and office for English, Morse and Company, makers of engines, boilers and pumps, on the site of a boarding house. The Great Western Manufacturing Company, a Leavenworth firm still in business, used it from 1898, and the Liberty Storage Company kept it as a warehouse for many years. '
  'It sat empty for decades until a local developer bought it in 2000. It is now the Ship, a restaurant, bar and live-music venue, with fixtures from a Pendergast-era bar that stood at 411 East 10th Street.',
  look='An 1888 warehouse with a very large replica cap gun mounted on its front, the building\'s trademark. Inside, the Ship has fixtures salvaged from the old 10th Street bar.',
  accn='A working restaurant and venue; ask at the door or check its page for hours (none found on a page read). Street parking.',
  links=[['Clio: The Ship (2014- ), English Morse & Co. (1888-1896), Great Western Manufacturing Co. (1898-1919)', 'https://theclio.com/tour/3025/14']],
  hours='?', brick='?'),

N('ridenour-baker-grocery-building-kc', 'Ridenour-Baker Grocery Company Building', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10307, -94.599, 'site', 'view', 'drive', '', '1910',
  'A grocery wholesaler in the West Bottoms since 1878, Ridenour-Baker lost its first building in the 1903 flood. It built this four-block complex between 1910 and 1919; a fire hit it part-way through and some of the unfinished work had to be rebuilt. '
  'Clio says it was built of reinforced concrete with no basement and a plain flat-roofed front, to resist flood and fire. The company dissolved in 1936. A series of smaller carriers leased it until the last owner left in 2003, and it has been vacant and deteriorating.',
  look='A large plain warehouse with a long loading dock beside the railroad tracks. Its unadorned style was what city officials encouraged after the floods. It stands vacant, so the outside is all there is to see.',
  accn='Private and vacant building, near 933 Mulberry Street. Look from the public street and do not enter. Street parking.',
  links=[['Clio: Ridenour-Baker Grocery Company Building', 'https://theclio.com/tour/3025/19']],
  conf='mixed', brick='?'),

N('seavey-flarsheim-building-kc', 'Seavey and Flarsheim Building (Tobin Seed)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10316, -94.60047, 'exact', 'view', 'drive', '', '1902',
  'A warehouse built about 1902 at 1317 St. Louis Avenue for the Seavey and Flarsheim Brokerage Company, wholesale brokers of tea, coffee and fresh produce who were formed in 1890. They moved out in 1933, and the Tobin Seed Company, later Tobin Lawn and Garden Supply, was there from 1938 to 2003. '
  'Robert Flarsheim left his $8.9 million fortune to the University of Missouri-Kansas City. As of 2025 the building was vacant, with no announced plans.',
  look='A brick warehouse whose wall still carries a painted advertisement for the Tobin Seed Company, a ghost sign repainted over the bricks (Clio). It is vacant, so the outside is what you see.',
  accn='Private and vacant building; look from the street and do not enter. Street parking.',
  links=[['Clio: The Seavey and Flarsheim Building', 'https://theclio.com/tour/3025/20']],
  brick='yes'),

N('peppard-seed-company-building-kc', 'J. G. Peppard Seed Company building (Doc\'s Caboose)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10279, -94.60154, 'exact', 'open', 'drive', '', '1892',
  'Built in 1892 at 1400 to 1402 Union Avenue for the J. G. Peppard Seed Company. Joseph Grear Peppard, born in New Orleans in 1858, came to Kansas City at 16 and began his own seed business in 1882, one of the dealers who brought Kentucky bluegrass to Missouri and the West. The company moved to a larger building on 8th Street in 1903. '
  'Later tenants included a wholesale grocer and Pearson and Ferguson Chemical (1938 to 1983), and from 1984 to 1988 the furniture reuse charity Surplus Exchange. Artist Laurence "Doc" Snyder bought it and opened Doc\'s Caboose model train store, a print shop and a gallery.',
  look='A brick warehouse of 1892 on Union Avenue with small shops, studios and a design firm inside. Peppard also built a house on the West Side that still stands (see the Peppard House entry).',
  accn='Private building with small businesses; their hours were not found on a page read. Street parking.',
  links=[['Clio: J.G. Peppard Seed Company (1892-1903), Pearson-Ferguson Chemicals (1938-1983), Doc\'s Caboose Building (2002- )', 'https://theclio.com/tour/3025/22']],
  hours='?', brick='?'),

N('hogue-mercantile-peanut-factory-kc', 'Hogue Mercantile Company peanut factory', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10279, -94.60459, 'exact', 'view', 'drive', '', '1930',
  'The Hogue Mercantile Company, started in 1916 by George Hogue and Albert Lustig in a small space at 1208 East Ninth Street, built this two-storey factory at 1600 St. Louis Avenue in 1930 so that peanuts could come straight off the railroad. It could process over 30,000 pounds of peanuts a day for tins, peanut butter and cooking oil sold as Ideal and Missouri Valley. '
  'The 1951 flood crippled it; Red Dot Foods bought it in 1957 and Frito-Lay in 1961, which ran it until 1985. Jural Manufacturing, makers of canvas and leather tool bags, has owned it since.',
  look='A two-storey industrial building of 1930 beside the tracks, with a basement that once stored raw peanuts. Whatever remains of the factory fittings was not checked.',
  accn='Private building, in use by a manufacturer and its tenants; look from the street. Street parking.',
  links=[['Clio: Hogue Mercantile Company', 'https://theclio.com/tour/3025/23']],
  brick='?'),

N('abernathy-furniture-west-bottoms-flats-kc', 'Abernathy Furniture Company building (West Bottoms Flats)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.1042, -94.60369, 'exact', 'view', 'drive', '', '1880',
  'The Abernathy brothers began making furniture in Leavenworth, Kansas, in 1856 and opened a second plant in the West Bottoms about 1880. The building grew to 300,000 square feet, reaching Ninth and Liberty streets, and Abernathy became one of the area\'s largest employers. One extension was torn down in the 1970s. '
  'The firm was bought by other companies in the 1950s and the buildings stood vacant. In 2016 MCM bought them, and a $68 million restoration made them the West Bottoms Flats apartments.',
  look='A large red-brick factory with the Abernathy Furniture Co. lettering preserved on the walls; the restorers cleaned the brick and left the ground-floor graffiti in place. Abernathy\'s Leavenworth plants are separate entries.',
  accn='Private apartment building at 1500 West 9th Street; look from the street. Street parking.',
  links=[['Clio: Abernathy Furniture Company Building', 'https://theclio.com/tour/3025/26']],
  brick='yes'),

N('kansas-city-cold-storage-building-kc', 'Kansas City Cold Storage Company Building (Cold Storage Lofts)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.11128, -94.57904, 'exact', 'view', 'drive', '', '1922',
  'The United States Cold Storage Company of Chicago built the first phase in 1922 for $1.5 million, to a design by S. Scott Joy, beside the Kansas City Southern tracks in the River Market. Ice was made and stored in two basement levels, with rooms for fruit, vegetables and other goods above. A second $1.5 million block was added from 1928 to plans revised by Chicago engineer Abraham Epstein. '
  'It held 38 million cubic feet of refrigerated space for about 80 years, then stood empty until a $37 million conversion made it the 226-unit Cold Storage Lofts, finished in 2007. It is on the National Register of Historic Places (listed June 1, 2005; Wikipedia also gives 2006).',
  look='A six-storey industrial block with a Tudor Revival look (Wikipedia\'s listing) at the corner of East 3rd Street. It is apartments now, so the outside is what you see.',
  accn='Private apartment building at 500 East 3rd Street; look from the street. Parking in the River Market.',
  links=[W('Kansas City Cold Storage Company Building')],
  conf='mixed', brick='?'),

N('richards-conover-hardware-building-kc', 'Richards and Conover Hardware Company Building (Richards and Conover Lofts)', 'Kansas City', 'kcmo', 'industry', 'standing',
  39.10796, -94.58564, 'exact', 'view', 'drive', '', '1902',
  'The Kansas City firm of Shepard and Farrar designed this six-storey, L-shaped building for the Richards and Conover Hardware Company, and William Davis built it in 1902 to 1903 at 200 West 5th Street. It has a limestone foundation, brick and stone walls and 95,000 square feet. The company had started in Leavenworth in 1857 and moved to Kansas City between 1881 and 1884. '
  'It closed in 1999, and the building was turned into loft apartments. Sources differ on the firm\'s start (1857 in Kansas, 1875 in Kansas City).',
  look='A heavy six-storey Commercial-style warehouse of brick and stone near the River Market. A one-storey 1928 office addition to the west and south is gone; its site is a park.',
  accn='Private apartment building; look from the street or the park beside it. Parking in the River Market.',
  links=[['Clio: Richards and Conover Hardware Company Building', 'https://theclio.com/entry/211404']],
  conf='mixed', brick='yes'),

N('st-marys-episcopal-church-kansas-city-mo', 'St. Mary\'s Episcopal Church, Kansas City', 'Kansas City', 'kcmo', 'worship', 'standing',
  39.09804, -94.5747, 'exact', 'view', 'drive', '', '1887',
  'The first Episcopal church in Kansas City, founded in 1857 as St. Luke\'s and renamed in the 1870s, sponsored by Trinity Church in Independence. Before the building at 13th and Holmes it met in several places, including one at 8th and Walnut. '
  'The Gothic Revival church on Holmes Street was built in 1887 to a design by William Halsey Wood and was accepted onto the National Register of Historic Places in 1978. It is Anglo-Catholic in tradition.',
  look='A Gothic Revival church in the downtown loop. Wikipedia\'s photographs show a high altar, a reredos behind it and a side chapel, which suggests a rich interior, but the pictures were not seen in person and its hours for visitors were not found.',
  accn='An active parish at 1307 Holmes Street. Service times were not found on a page read; the parish\'s own page (stmaryskcmo.org) would give them. Street and garage parking downtown.',
  links=[W('St. Mary\'s Episcopal Church (Kansas City, Missouri)')],
  hours='?', brick='yes'),

N('peppard-house-west-side-kc', 'Joseph Grear Peppard House', 'Kansas City', 'kcmo', 'landmark', 'standing',
  39.09275, -94.59255, 'exact', 'open', 'drive', '', '1887',
  'The seed merchant Joseph Peppard built this large red-brick Queen Anne house in 1887 on Jefferson Street and lived in it with his family until they sold it in 1909. Like many of its neighbours it became a boarding house. By 2017 it had no plumbing to speak of and little heat. '
  'A restoration took over a year, and in 2018 it reopened as a short-term rental with eight bedrooms in three flats. It is on the National Register of Historic Places (listed 1985). Peppard\'s middle name is spelled both Grear and Greer in sources.',
  look='A big red-brick Queen Anne mansion with a turret and tall leaded windows, among the few survivors of the 1880s mansions on Jefferson Street. It can be rented by the night, so staying there is the way inside.',
  accn='A private house let as a short-term rental, at 1704 Jefferson Street. Visitors may look from the street; the interior is for booked guests. Street parking. Hours: not applicable.',
  links=[['Flatland KC (2018): Restored 1887 mansion offers unique Airbnb stay', 'https://flatlandkc.org/news-issues/restored-1887-mansion-offers-unique-airbnb-stay-on-downtowns-west-side/']],
  hours='?', brick='yes'),
]

PIN_NOTES = {
  'kc-bolt-nut-screw-west-bottoms-kc': 'The address lookup (1324 West 12th Street) landed on a gas station in the rail yard, so the pin was moved by hand to the north side of West 12th Street, west of the Lowe warehouse, where the aerial shows old industrial buildings. It marks the area; the exact building was not confirmed.',
  'studebaker-stowe-hardware-building-kc': 'Street address (1300 West 13th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'john-deere-distribution-center-beast-kc': 'Street address (1401 West 13th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'parlin-orendorff-oliver-plow-building-kc': 'Street address (1323 West 13th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'keystone-implement-building-kc': 'Street address (1321 West 13th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'adams-building-west-bottoms-kc': 'Street address (1311 West 13th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'lowe-brothers-paint-edge-of-hell-kc': 'Street address (1300 West 12th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'advance-rumely-thresher-building-kc': 'The address lookup (1222 West 12th Street) returned the same point as the Studebaker building, so the pin was placed by hand between the 1200 and 1300 blocks on West 12th Street. It marks the area; the exact building was not confirmed.',
  'avery-holsum-studios-building-kc': 'Street address (1200 West 12th Street) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'english-morse-the-ship-kc': 'Street address (1217 Union Avenue) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'ridenour-baker-grocery-building-kc': 'Address near 933 Mulberry Street from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'seavey-flarsheim-building-kc': 'Street address (1317 St. Louis Avenue) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'peppard-seed-company-building-kc': 'Street address (1400 Union Avenue) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'hogue-mercantile-peanut-factory-kc': 'Street address (1600 St. Louis Avenue) from the Esri geocoder. On the aerial it falls on an old industrial building in the block; within the block the exact building was not confirmed.',
  'abernathy-furniture-west-bottoms-flats-kc': 'Street address (1500 West 9th Street) from the Esri geocoder; the pin fell on the street edge, so it was moved a few metres south onto the large building the aerial shows.',
  'kansas-city-cold-storage-building-kc': 'Street address (500 East 3rd Street) from the Esri geocoder; Wikipedia gives 39.11333, -94.57889. On the aerial it falls on the large block building.',
  'richards-conover-hardware-building-kc': 'Street address (200 West 5th Street) from the Esri geocoder. On the aerial it falls on a large corner building.',
  'st-marys-episcopal-church-kansas-city-mo': 'Street address (1307 Holmes Street) from the Esri geocoder. On the aerial it falls on a small church building beside a parking lot.',
  'peppard-house-west-side-kc': 'Street address (1704 Jefferson Street) from the Esri geocoder. On the aerial it falls on a large house with a turret.',
}
