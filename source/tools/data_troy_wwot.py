# November 22, 2026: Troy (region troy, drawn at random by tools/choose.py --state ny). Earlier Troy batches had taken
# downtown, RPI, Oakwood and central Lansingburgh, and left the Register's River Street factories as leads with "a
# source opened that says what stands". This batch takes them: the collar-and-cuff factories, the paint works and the
# brewery bottling works along River Street north of downtown, the Neemes Foundry and the International Shirt and
# Collar building south of downtown, the old Catholic Central High School (built as Cluett, Peabody's research
# laboratory) and the Jacob H. Patten House with its blacksmith's carriage house in Lansingburgh. Sources opened in
# this session: the National Register nomination forms on NPGallery (read as text with tools/page.py), the Hudson
# Mohawk Industrial Gateway's article on the textile factories (updated June 2020) and its foundry and manhole-cover
# page, the Governor's office releases on the 2023 and 2024 Register nominations and on Flanigan Square (June 2024),
# historypointer.com for Register addresses, a 2021 citybiz news item on 701 River Street, a 2023 radio-station item
# on Catholic Central, another on the Fitzgerald plant, and Wikipedia as raw text (tools/wiki_raw.py).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'troy_wwot','label':'Troy: the River Street collar factories and other works','added':'2026-11-22 02:40'}
def NR(r,t): return L('National Register nomination: '+t+' (NPGallery, PDF)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'+r+'_text')
def HP(r): return L('historypointer: National Register record '+r,'https://historypointer.com/nris/resource/'+r)
HMIG=L('Hudson Mohawk Industrial Gateway: Four textile factories in Troy listed on the National Register (2016, updated 2020)','https://hudsonmohawkgateway.org/troy-textile-factories')
GOV24=L('Governor\'s office: 15 nominations to the State and National Registers (March 14, 2024)','https://www.governor.ny.gov/news/governor-hochul-announces-15-nominations-state-and-national-registers-historic-places')
GOV24B=L('Governor\'s office: nominations to the State and National Registers (June 14, 2024)','https://www.governor.ny.gov/news/governor-hochul-announces-nominations-state-and-national-historic-places')
GOV23=L('Governor\'s office: 37 nominations to the State and National Registers (December 29, 2023)','https://www.governor.ny.gov/news/governor-hochul-announces-37-nominations-state-and-national-registers-historic-places')
RIVER='A private building; look from River Street. No public lot was found nearby (the lots OpenStreetMap maps here are not on public land); park on the street where signs allow, rules not checked.'
PLACES=[
N('international-shirt-collar-troy','International Shirt and Collar Company building (Conkey malt house)','Troy','troy','industry','standing',42.72391,-73.69548,'exact','view','drive','','1876–1904',
  'A U-shaped brick factory at River and Adams Streets, south of downtown. Its first part was built in 1876 as a malt house for Charles F. Conkey; the International Shirt and Collar Company, founded in 1893, bought it about 1899, joined a new south block to it in mill construction, and had the present outline by 1904. The firm was caught in a run of mergers and closed in 1906. Listed on the National Register in 2017.',
  'Four- and five-storey brick blocks over a raised basement, with cut granite trim (the Commons photograph shows red brick), a six-storey tower on River Street with narrow round-arched openings at the top, and a tapered brick chimney. The 15 northern bays on River Street are the 1876 malt house. When the form was written (about 2016) it was the Old Brick Furniture Company, with a showroom on the ground floor; present use not checked. Interior not checked.',
  'A malt house that became a collar factory, in the city that made nine collars in ten.',
  RIVER,
  [NR('100000648','International Shirt and Collar Company'),HP('100000648')],
  brick='yes'),
N('neemes-foundry-troy','Neemes Foundry','Troy','troy','industry','standing',42.72289,-73.69451,'exact','view','drive','','1886',
  'A foundry building on First Street in South Troy, built in 1886 for Neemes Brothers. The Governor\'s office gives the firm\'s founding as 1873; the Hudson Mohawk Industrial Gateway says the father, C. S. Neemes, started the business in 1874 and his sons formed the firm in 1883, so the first year is not settled. It made its own automatic stoker for locomotive boilers, iron grates sold for sugar mills, railways and bakeries, castings for local mills, and manhole covers. Listed on the National Register in 2024.',
  'From the street, a foundry building of its period; inside, the Register summary describes one open workshop under a massive timber truss roof with no posts. Look down at the streets around Troy too: covers lettered "Neemes Bros\' Troy NY" are the commonest old manhole covers still in the city. Present use not checked; interior not checked.',
  'The foundry whose name is still under your feet all over Troy.',
  'A private building at 206 First Street; look from the street. Park on nearby streets where signs allow; rules not checked.',
  [GOV24B,L('Hudson Mohawk Industrial Gateway: Troy\'s foundry industry, manhole covers','https://hudsonmohawkgateway.org/troys-foundry-industry-manholes'),HP('100010631')],
  conf='mixed',brick='?'),
N('cluett-peabody-hedley-park-place-troy','Cluett, Peabody & Co. factory (Hedley Park Place)','Troy','troy','industry','standing',42.73747,-73.68724,'exact','view','drive','','1917–1980s',
  'The largest building in the River Street factory corridor and the only one of reinforced concrete, finished in 1917 to designs by Westinghouse, Church, Kerr & Co. It was the last textile building put up in Troy and the one in textile use longest: Cluett, Peabody made its Arrow collars and cuffs, and later shirts, here until the 1980s. Troy developer John Hedley turned it into offices, Hedley Park Place, without Register listing; it and its power boiler house were listed in 2025.',
  'A plainer, larger-windowed factory than its brick neighbours. In 2020 the Gateway listed Troy City Hall among its tenants; present tenants not checked. The boiler house named in the 2025 listing was not looked for. Interior not checked.',
  'Where Arrow collars were made, and where Troy City Hall moved in.',
  'An office building at 431-433 River Street; look from River Street. No public lot was found nearby (the lots OpenStreetMap maps here are not on public land); park on the street where signs allow, rules not checked.',
  [HMIG,HP('100012135')],
  brick='?'),
N('fitzgerald-bottling-works-troy','Fitzgerald Brothers Brewing Company bottling works','Troy','troy','industry','standing',42.73894,-73.68602,'exact','view','drive','','1892–1955',
  'The bottling plant of the Fitzgerald Brothers brewery, founded in 1866 and in its day one of the leading breweries in Troy and the region, which sold its beer across the Northeast and brewed until the early 1960s. The building is in three parts: a barn and store house of 1892, the bottling works of 1911, and a new bottling addition of 1955. Listed on the National Register in 2024.',
  'A brick industrial building at 500 River Street; the three building dates should show as three parts. A local radio station\'s page says a storage company planned to turn it into about a thousand storage units; whether that was done was not checked. Interior not checked.',
  '',
  RIVER,
  [GOV24,HP('100010345'),L('Q105.7 / Zoey 103.9: Bottle up your belongings in Troy','https://zoey1039.com/bottle-up-your-belonging-in-troy/')],
  brick='?'),
N('miller-hall-hartwell-collar-factory-troy','Miller, Hall & Hartwell shirt collar factory and box factory (Flanigan Square)','Troy','troy','industry','standing',42.74042,-73.68595,'exact','view','drive','','1880–1915',
  'Justice Miller built the south half of this factory in 1880; it became Miller, Hall & Hartwell in 1884, grew into one of the city\'s biggest makers of collars and cuffs, sold in every state, and at its peak employed nearly 3,000 people, most of them women and teenage girls. An 1891 north half by the Troy architect Edward Loth nearly doubled it, and a box factory was added in 1915, a rare survivor of the trades that served the collar mills. Troy\'s collar workers, mostly women, were early union organisers. Listed on the National Register in 2024.',
  'A long load-bearing brick factory at 547 River Street with Italianate and Romanesque Revival trim, and the box factory, listed with it at 558 River Street. Developer John Hedley made 547 into offices (Flanigan Square, with Rensselaer County as main tenant in 2020); in 2024 the Governor\'s office announced 72 flats for 547 and a grocery opened at 558. Whether the grocery is in the box factory building was not checked. Interior not checked.',
  'Three thousand collar girls under one roof.',
  RIVER,
  [GOV24,HMIG,L('Governor\'s office: Flanigan Square grocery completed (June 7, 2024)','https://www.governor.ny.gov/news/governor-hochul-announces-completion-bargain-grocery-75-million-flanigan-square-mixed-use'),HP('100010268')],
  brick='?'),
N('wilbur-campbell-stephens-collar-factory-troy','Wilbur, Campbell, Stephens Company collar factory (Tapestry on the Hudson)','Troy','troy','industry','standing',42.74216,-73.68571,'exact','view','drive','','1899–1960s',
  'A six-storey collar-and-cuff factory at River and Jay Streets, built for the firm the Wilbur brothers founded about 1880. The Register form gives 1899 for the building; the Hudson Mohawk Industrial Gateway says about 1889, so the year is not settled. The firm made collars here until about 1909 and dissolved about 1911; other textile firms followed until the mid-1960s, then Mooradian\'s furniture from 1973 to 2006. Listed in 2016 and turned into apartments.',
  'The largest and showiest of the listed collar factories: red-orange brick, a two-storey Romanesque arcade across the recessed middle of the River Street front, rusticated lower floors and a pressed-metal cornice, carried round onto the south side. The river side and north side are plain. Now flats (Tapestry on the Hudson); interior not open.',
  '',
  RIVER,
  [NR('15001026','Wilbur, Campbell, Stephens Company Cuff and Collar Factory'),HMIG],
  conf='mixed',brick='yes'),
N('van-zandt-jacobs-collar-factory-troy','Van Zandt, Jacobs and Company collar and cuff factory (Arthaus Hudson)','Troy','troy','industry','standing',42.74285,-73.68531,'exact','view','drive','','1896–1923',
  'A five-storey Romanesque Revival collar and cuff factory at River and Rensselaer Streets, designed by Marcus F. Cummings and Son. The north half was built in 1896 and the south half before 1903. Van Zandt, Jacobs and Company made collars here until 1923, when it reorganised as Van Zandt\'s Inc., which also sold whole shirts under its Triangle brand; by 1930 the city directory called it a vacant factory. Listed in 2014; after years largely empty it was renovated as Arthaus Hudson, flats with studio and gallery space for artists.',
  'Red brick, with brick arcades, a heavy cornice and a narrow six-storey entrance tower just off centre with an arched doorway; the plan is a U open to the river. The form notes old painted wall signs. Flats; interior not open.',
  '',
  RIVER,
  [NR('14000009','Van Zandt, Jacobs and Company Collar and Cuff Factory'),HMIG],
  brick='yes'),
N('connors-paint-works-troy','William Connors Paint Manufacturing Company building','Troy','troy','industry','standing',42.74485,-73.68454,'exact','view','drive','','before 1885–1970s',
  'The one works in the River Street collar corridor that made something else: ready-mixed paint, sold under the "American Seal" name. William Connors moved here in 1889 into a former sash and blind factory beside the Troy Nickel Works; in 1897 he bought the nickel works and part of an old paper mill and built a grinding building for pigments on their south side. Paint was made here until the 1970s. Listed on the National Register in 2016.',
  'A three-storey brick factory at 669 River Street in three parts: the south block of about 1897 and two older blocks to the north built before 1885, told apart by their windows on the 13-bay front. The Gateway says it keeps the last signs of water power in the corridor and likely in the city: water came from the Hudson by a canal, now gone, and left by a tailrace, and some water-driven machinery is still inside. Vacant in 2020 with flats and a restaurant planned; present use and interior not checked.',
  'Troy\'s last water-powered machinery, inside a paint works.',
  RIVER,
  [NR('16000486','William Connors Paint Manufacturing Company Building'),HMIG],
  brick='?'),
N('searle-gardner-collar-factory-troy','Searle, Gardner & Company collar factory (Collar Factory Lofts)','Troy','troy','industry','standing',42.74628,-73.68367,'exact','view','drive','','1898–1950s',
  'A five-storey, 18-bay collar and cuff factory at 701-715 River Street, also called the Marshall Ray Building, with a two-storey block attached. Wikipedia and the Register form date it about 1898 to 1899; the Hudson Mohawk Industrial Gateway says about 1889, so the year is not settled. It made collars, cuffs and later shirts into the mid-1900s, then stood empty for more than 20 years. A fire on July 19, 2019 damaged the whole building when its conversion to flats was 80 percent done; the developers rebuilt it, and the Collar Factory Lofts opened in 2021.',
  'Brick mill construction with segmental-arched windows and restrained Romanesque and Renaissance Revival trim, on the block of River Street, President Street and Ingalls Avenue. Flats; interior not open. Brick colour not checked.',
  'Burned at 80 percent done, and finished anyway.',
  RIVER,
  [W('Searle, Gardner and Company Cuff and Collar Factory'),NR('13001092','Searle, Gardner and Company Cuff and Collar Factory'),HMIG,L('citybiz: Historic factory building in Troy destroyed by fire rises from the ashes (2021)','https://www.citybiz.co/article/29842/a-comeback-nearly-complete-historic-factory-building-in-troy-destroyed-by-fire-rises-from-the-ashes/')],
  conf='mixed',brick='?'),
N('catholic-central-high-school-troy','Old Catholic Central High School (Cluett, Peabody research laboratory)','Lansingburgh, Troy','troy','civic','standing',42.77527,-73.67111,'site','view','drive','','1947–2022',
  'An H-shaped building of about 75,000 square feet in Lansingburgh, built in 1947 as a textile research laboratory for the shirt maker Cluett, Peabody & Company. The Diocese of Albany bought it in 1952, and for almost seventy years it was Catholic Central High School, a main regional Catholic secondary school. The school merged into a new one in Latham in 2022 and the Troy property was put up for sale; it was listed on the National Register in 2024.',
  'The three-storey school with its two-storey gym and cafeteria and more than five acres of playing fields, at 625 Seventh Avenue. In 2023 a developer had a contract to buy it and make 65 flats in the main building; whether that went ahead was not checked. Interior not checked.',
  'The Arrow shirt company\'s laboratory that became a high school.',
  'Private; look from Seventh Avenue and 117th Street. Street parking; rules not checked.',
  [GOV23,W('Catholic Central School (Latham, New York)'),L('WGNA: What will the old Catholic Central High School in Troy become? (April 2023)','https://wgna.com/what-will-the-old-catholic-central-high-school-in-troy-become/')],
  brick='?'),
N('jacob-patten-house-lansingburgh','Jacob H. Patten House and blacksmith shop','Lansingburgh, Troy','troy','landmark','standing',42.76214,-73.68008,'exact','view','drive','','1881–1882',
  'An Italianate brick townhouse built in 1881 and 1882 for Jacob H. Patten, a Troy blacksmith, on a double lot in south Lansingburgh, which was not laid out in lots until 1872. Brick and a double lot were both uncommon in this part of the village. The large brick carriage house behind it held Patten\'s blacksmith shop in the late 1800s and early 1900s. Listed on the National Register in 2015.',
  'At 254 Fourth Avenue near 105th Street: double front doors, tall narrow windows, a bracketed cornice, a second-floor oriel over a later bay window, Eastlake-style carved lintels and a side porch with sawn trim; the brick carriage house stands on the alley behind. A private house; interior not open.',
  '',
  'A private house; look from Fourth Avenue. Street parking; rules not checked.',
  [NR('15000954','Jacob H. Patten House'),HP('15000954')],
  brick='?'),
]
PIN_NOTES={
 'international-shirt-collar-troy':'ArcGIS PointAddress for 2 River Street (historypointer\'s Register address), at River and Adams Streets as the form says.',
 'neemes-foundry-troy':'ArcGIS PointAddress for 206 First Street (historypointer\'s Register address).',
 'cluett-peabody-hedley-park-place-troy':'ArcGIS PointAddress for 433 River Street.',
 'fitzgerald-bottling-works-troy':'ArcGIS PointAddress for 500 River Street (historypointer\'s Register address).',
 'miller-hall-hartwell-collar-factory-troy':'ArcGIS PointAddress for 547 River Street; the box factory at 558 is across the street, 50 m east.',
 'wilbur-campbell-stephens-collar-factory-troy':'ArcGIS PointAddress for 599 River Street, the form\'s address.',
 'van-zandt-jacobs-collar-factory-troy':'ArcGIS PointAddress for 621 River Street, the form\'s address.',
 'connors-paint-works-troy':'ArcGIS PointAddress for 669 River Street, the form\'s address.',
 'searle-gardner-collar-factory-troy':'ArcGIS PointAddress for 701 River Street; the Wikipedia point is 15 m away.',
 'catholic-central-high-school-troy':'OpenStreetMap building "Catholic Central High School", 625 7th Avenue (nom.py).',
 'jacob-patten-house-lansingburgh':'ArcGIS PointAddress for 254 4th Avenue, the form\'s address; the Wikipedia point is 200 m west.',
}
