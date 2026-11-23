# Fort Worth, Texas: buildings named in a video about the city's old buildings, each checked against the National
# Register list and forms, Wikipedia, Texas Historical Commission marker texts, SAH Archipedia and the owners' own pages.
from data_b import N
from data_ma import W

def THC(n, label): return [label + ' (Texas Historical Commission marker)', 'https://atlas.thc.texas.gov/Details/%d' % n]
def NR(ref, label): return [label + ' (National Register form)', 'https://atlas.thc.state.tx.us/NR/pdfs/%s/%s.pdf' % (ref, ref)]
def SAH(code, label): return [label + ' (SAH Archipedia)', 'https://sah-archipedia.org/buildings/' + code]
DT = 'Downtown Fort Worth: metered street parking and pay garages.'

BATCH={'key':'fortworth_zbhn','label':'Fort Worth, Texas: courthouse, stations, Art Deco towers, stockyards and banks','added':'2026-11-23 19:40'}

PLACES=[
N('tarrant-county-courthouse-fort-worth','Tarrant County Courthouse','Fort Worth','tx','civic','standing',32.75769,-97.33333,'exact','view','drive','','1893–1895',
  'The county courthouse on the bluff above the Trinity River, designed by Frederick C. Gunn and Louis Curtiss and built by the Probst Construction Company of Chicago from 1893 to 1895, in Renaissance Revival style. It cost $408,840, and voters thought it so extravagant that they elected a new county commissioners\' court in 1894. Its clock tower was renovated in 2012. It still holds the county clerk\'s office, probate and county courts and a law library.',
  'A pink Texas granite building that looks much like the State Capitol in Austin except for its clock tower. Interior not checked.',
  'The pink granite courthouse that cost its commissioners their jobs.',
  'Owned and used by Tarrant County, 100 East Weatherford Street, at the north end of Main Street. Seen from the street on every side; a working courthouse, whose public hours were not checked. '+DT,
  [W('Tarrant County Courthouse')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('tp-station-fort-worth','Texas and Pacific Passenger Station (T&P Station)','Fort Worth','tx','rail','standing',32.74727,-97.32839,'site','public','drive','stations','1931–',
  'The Texas and Pacific Railway\'s passenger station, opened on October 25, 1931, in place of an earlier station, in the Zigzag Moderne style of Art Deco. Passenger trains left it in 1967; railway offices stayed upstairs until 1981, and a federal agency then used the building into the late 1990s. The passenger area, nearly untouched since 1967, was restored in 1999, and commuter trains have used the station again since then.',
  'The waiting room: marble floors, metal-inlaid panel ceilings, and nickel and brass fittings with zigzags and chevrons. The larger T&P Warehouse, built in the same style, stands one block west.',
  'An Art Deco station lobby you can still walk through to catch a train.',
  'A working station for the Trinity Railway Express and TEXRail commuter trains, 1600 Throckmorton Street. The waiting room is open to train riders. Free parking off West Vickery Boulevard (Wikipedia).',
  [W('T&P Station'), NR('78002983','Texas and Pacific Terminal Complex')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('livestock-exchange-building-fort-worth','Livestock Exchange Building (Stockyards Museum)','Fort Worth','tx','civic','standing',32.78924,-97.34655,'site','open','drive','','1902–1903',
  'The headquarters of the Fort Worth cattle market, built in 1902–1903 for the Stockyards Company, the livestock commission men and the buyers, and once surrounded by lawns. The United Stockyards Corporation bought it in 1944. It is a Recorded Texas Historic Landmark inside the Stockyards historic district.',
  'The Stockyards Museum, run by the North Fort Worth Historical Society, is on the first floor, with objects from the history of the yards. Building fabric not checked.',
  'The office block where Fort Worth\'s cattle were bought and sold.',
  '131 East Exchange Avenue, in the Stockyards. Museum hours and the $3 admission (children 12 and under free) from the Stockyards\' own page, read November 2026. Pay lots along East Exchange Avenue.',
  [THC(5439002029,'Fort Worth Livestock Exchange'), ['Fort Worth Stockyards: Stockyards Museum','https://fortworthstockyards.com/attractions/livestock-exchange/'], W('Fort Worth Stockyards')],
  conf='', th=[32.78976,-97.34523], thn='Lot on East Exchange Avenue', brick='?', hours='Monday and Wednesday to Saturday 10 a.m. to 5 p.m.; closed Tuesday and Sunday'),

N('fort-worth-stockyards-historic-district','Fort Worth Stockyards Historic District','Fort Worth','tx','town','standing',32.79028,-97.34611,'area','public','walk','','1890–',
  'The livestock market north of downtown. Railroads reached the area in 1876, the Fort Worth Union Stockyards opened in January 1890, and Boston investors formed the Fort Worth Stock Yards Company in 1893 and brought in the Swift and Armour packing houses. By 1907 the yards sold a million cattle a year; trade fell away after the 1950s as auctions moved closer to the ranches. A 98-acre part was listed on the National Register in 1976.',
  'Recorded landmarks in the district include the entrance sign, the Livestock Exchange Building and the Thannisch Block (the Stockyards Hotel); the Armour and Swift plaza and the Cowtown Coliseum are State Antiquities Landmarks. Today the streets are mostly shops, restaurants and entertainment, with weekend rodeos at the Coliseum and cattle drives through the streets.',
  'Cowtown\'s old cattle market, still with a cattle drive down the street.',
  'Public streets round East Exchange Avenue and North Main Street, open any day; the buildings are privately owned shops and venues. Pay lots throughout the district.',
  [W('Fort Worth Stockyards'), NR('76002067','Fort Worth Stockyards Historic District')],
  conf='', th=[32.78748,-97.34628], thn='Lot by Mule Alley', brick='?', hours=''),

N('blackstone-hotel-fort-worth','Blackstone Hotel','Fort Worth','tx','hotel','standing',32.75386,-97.33051,'exact','open','drive','','1929–',
  'A 23-storey, 284-room hotel at Fifth and Main streets, built by the cattleman C. A. "Gus" O\'Keefe to designs by Mauran, Russell & Crowell of St. Louis, and opened on October 10, 1929. It was the first skyscraper in Fort Worth to use Art Deco ornament. Five presidents stayed there. It ran for over fifty years, stood empty for nearly twenty, and was restored in the late 1990s; it is a Courtyard by Marriott hotel today.',
  'Terra cotta ornament and setbacks on the top floors; at 268 feet it is the tallest hotel downtown. Interior not checked.',
  'The 1929 Art Deco hotel that hosted five presidents.',
  'A working hotel, 601 Main Street. Hours not checked. '+DT,
  [W('Blackstone Hotel (Fort Worth, Texas)')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('flatiron-building-fort-worth','Flatiron Building (Saunders Triangle Building)','Fort Worth','tx','civic','standing',32.75060,-97.32987,'exact','view','drive','','1907–',
  'A seven-storey wedge-shaped office block on the corner of Houston and West Ninth streets, built in 1907 for the physician Bacon Saunders, who kept the top floor for his offices. Designed by Sanguinet & Staats after New York\'s Flatiron Building, it was one of the city\'s first steel-frame buildings and for a time the tallest in north Texas. Ten storeys were planned, cut to seven after the Panic of 1907. It was renovated after 1989.',
  'Reinforced concrete over a steel frame, a two-storey base, arches across the top floor, carved panther heads above the second storey, brick lozenges and a heavy cast-iron cornice. Inside, a lobby with tile floor, marble wainscot and an ornate iron elevator (Wikipedia); as of 2021 offices above and an event space on the ground floor. Interior not checked.',
  'Fort Worth\'s own seven-storey flatiron, with panther heads.',
  'Privately owned, 1000 Houston Street. Look from the street. '+DT,
  [W('Flatiron Building (Fort Worth, Texas)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('sinclair-building-fort-worth','Sinclair Building','Fort Worth','tx','civic','standing',32.75393,-97.33097,'exact','open','drive','','1929–1930',
  'A Zigzag Moderne office tower at Fifth and Main streets, built in 1929–1930 for the oilman Richard Otto Dulaney to designs by Wiley G. Clarkson, and leased mostly by the Sinclair Oil Company. Offices filled it until 2013, when new owners began turning it into a hotel; it opened as a Marriott Autograph Collection hotel in 2019, its zigzag work restored from archive drawings and original fixtures found behind later walls.',
  'Limestone and cast stone over reinforced concrete, with granite and marble, zigzag ornament with Maya-style touches, and setbacks at the top. An arcade runs in from the Main Street door. Interior otherwise not checked.',
  'An oil-boom Art Deco tower turned hotel.',
  'A working hotel, 512 Main Street. Hours not checked. '+DT,
  [W('Sinclair Building (Fort Worth)'), NR('91001913','Sinclair Building')],
  conf='', th=None, thn=None, brick='no', hours='?'),

N('petroleum-building-fort-worth','Petroleum Building','Fort Worth','tx','civic','standing',32.75283,-97.33179,'site','view','drive','','1927–',
  'A fourteen-storey office building at the northeast corner of Throckmorton and Sixth streets, built in 1927 to designs by Wyatt C. Hedrick, shortly after he took over the practice of Sanguinet & Staats. It was put up for the oil companies that made Fort Worth their regional base. It has also been called the Life of America, Schick, Finevest and Executive Plaza building.',
  'Commercial Gothic fronts on Throckmorton and Sixth streets of brick and stone, with narrow pilaster strips and carved stone owls, wings spread, at their feet. Ground-floor changes made in the late 1960s have been reversed. Interior not checked.',
  'Look for the stone owls on the oil men\'s office tower.',
  'Privately owned, 210 West Sixth Street. Look from the street. '+DT,
  [NR('09000982','Petroleum Building')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('fort-worth-main-post-office','Fort Worth Main Post Office','Fort Worth','tx','civic','standing',32.74652,-97.32909,'exact','open','drive','','1931–1933',
  'The city\'s main post office, designed by the Wyatt C. Hedrick firm and opened in 1933, between the Texas and Pacific station and warehouse. In 2014 the Postal Service thought of selling it and moving its work north, and the building went on a list of endangered places, but it was kept as a post office.',
  'Texas fossil limestone, sixteen Corinthian columns along Lancaster Avenue with shorthorn heads in place of scrolls, longhorn and Hereford heads on the capitals and lions\' heads on the cornice. Inside, a coffered lobby the length of the building, with marble, bronze and gold leaf, and murals of 1934 by the Fort Worth artists Dwight Clay Holmes and William Henry Baker.',
  'A post office with cattle heads on its columns.',
  'United States Postal Service, 251 West Lancaster Avenue. Lobby hours not checked. '+DT,
  [W('United States Post Office (Fort Worth, Texas)'), THC(5439002030,'Fort Worth Main Post Office Building'), SAH('TX-02-FW18','U.S. Post Office')],
  conf='', th=None, thn=None, brick='no', hours='?'),

N('farmers-and-mechanics-national-bank-fort-worth','Farmers and Mechanics National Bank (The Harper)','Fort Worth','tx','civic','standing',32.75267,-97.33023,'exact','open','drive','','1921–',
  'A bank tower at Main and Seventh streets, built in 1921 to designs by Sanguinet & Staats in the Chicago style, when oil and cattle money were making Fort Worth grow. It was the tallest building in the city until 1957. It has also been called Fort Worth National Bank, Continental Life, Transport Life and 714 Main. It stood empty from 1997 until 2007, when XTO Energy bought and renovated it.',
  'A three-part tower: base, plain shaft and decorated top. It is now the Kimpton Harper Hotel (Wikipedia). Interior not checked.',
  'The 1921 bank that was Fort Worth\'s tallest for 36 years.',
  'A hotel, 714 Main Street. Hours not checked. '+DT,
  [W('Farmers and Mechanics National Bank (Fort Worth)')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('first-national-bank-building-fort-worth','First National Bank Building (Fort Worth)','Fort Worth','tx','civic','standing',32.75259,-97.33057,'exact','view','drive','','1910–',
  'An eleven-storey bank and office tower at 711 Houston Street, at Seventh Street, built in 1910 to designs by Sanguinet & Staats and widened along Houston Street in 1926 to designs by Wyatt C. Hedrick. It has also been called the Baker Building and the Bob R. Simpson Building.',
  'A three-part skyscraper with Beaux-Arts ornament. Interior not checked.',
  '',
  'Privately owned, 711 Houston Street. Look from the street. '+DT,
  [W('First National Bank Building (Fort Worth, Texas)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('will-rogers-memorial-center-fort-worth','Will Rogers Memorial Center','Fort Worth','tx','amuse','standing',32.74602,-97.36686,'site','public','drive','','1936–',
  'A 120-acre show and livestock grounds named for the humorist Will Rogers, built in 1936 to designs by Wyatt C. Hedrick in the Moderne (Art Deco) style. Its coliseum was the home of the Fort Worth Stock Show and Rodeo for many years, until the new Ariat Arena next door took the show in 2020. The statue Riding into the Sunset, of Rogers on his horse Soapsuds, was unveiled in 1947. The complex was listed on the National Register in 2016.',
  'The coliseum, the Pioneer Memorial Tower and the auditorium in Art Deco dress, with horse and cattle show barns round them. Interiors seen by going to an event.',
  'The 1936 Art Deco rodeo grounds still full of horses.',
  'Owned by the City of Fort Worth, 3401 West Lancaster Avenue. The grounds are open round events; event times on the center\'s pages. Large lots round the complex.',
  [W('Will Rogers Memorial Center')],
  conf='', th=[32.74634,-97.36376], thn='Lot on Van Cliburn Way', brick='?', hours=''),

N('north-fort-worth-high-school','North Fort Worth High School','Fort Worth','tx','civic','standing',32.78119,-97.35688,'exact','view','drive','','1918–1919',
  'A three-storey school on a bluff above Circle Park, designed by Marshall Sanguinet and Carl Staats and opened on September 11, 1919, for the growing North Side; it was also called North Side High School and Fort Worth Technical High School. It is built on an H plan, with the auditorium in the south opening and the gymnasium in the north. Stone retaining walls and a fountain with three cast-stone lions were added below it in 1934 under the Civil Works Administration. It was later an annex of J. P. Elder Middle School.',
  'Prairie School brick with cast stone and orange terra cotta trim in strong horizontal and vertical lines, grand stairs up to the second floor, and the lion fountain at street level on Park Street. The outside is almost as it was built in 1918–1919 (the Register form). Interior not checked.',
  '',
  'Fort Worth school district property, 600 Park Street. Look from Park Street and Circle Park Boulevard; a school building, not open to visitors. Street parking.',
  [NR('94001627','North Fort Worth High School')],
  conf='', th=None, thn=None, brick='yes', hours=''),

N('fire-station-no-1-fort-worth','Fire Station No. 1','Fort Worth','tx','civic','standing',32.75647,-97.33110,'exact','view','drive','','1907–',
  'A small fire station at Commerce and Second streets, designed by Sanguinet & Staats and built in 1907. It served the business district for almost seventy-five years, until 1980, and was restored in 1983 with the building of the City Center towers beside it.',
  'A corbelled brick cornice and rusticated second storey. SAH Archipedia says it holds an exhibition of Fort Worth history; later reports say a café and restaurant use it, so what is inside now is not checked.',
  'A 1907 fire house kept among the downtown towers.',
  'Privately owned, 215 Commerce Street, by Sundance Square. Look from the street; whether it opens to visitors was not checked. '+DT,
  [SAH('TX-02-FW8','Fire Station No. 1')],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('fort-worth-union-depot-ashton','Fort Worth Union Depot (Santa Fe Depot, Ashton Depot)','Fort Worth','tx','rail','standing',32.74914,-97.32417,'exact','view','drive','stations','1899–',
  'The passenger station the Gulf, Colorado and Santa Fe Railroad built for Fort Worth; SAH Archipedia dates it 1899, the Wikipedia text 1900. It was renovated in 1938, losing its entrance portico. Rock Island, Frisco and Southern Pacific trains used it too, and it was Fort Worth\'s Amtrak station from 1971 until 2002. In private hands since, it is an 800-seat event hall called the Ashton Depot.',
  'Beaux-Arts: red brick walls with red and white stone quoins, banding and stone-trimmed round windows. The 1938 Santa Fe freight station, with fine brickwork, stands one block north at 1401 Jones Street. Interior not checked.',
  'Fort Worth\'s old union station, now a party hall.',
  'Privately owned event hall, 1501 Jones Street. Look from Jones Street; inside only for events. '+DT,
  [W('Fort Worth Union Depot (1900–2002)'), SAH('TX-02-FW15','Ashton Depot')],
  conf='mixed', th=None, thn=None, brick='yes', hours=''),

N('first-united-methodist-church-fort-worth','First United Methodist Church (Fort Worth)','Fort Worth','tx','worship','standing',32.75202,-97.33641,'exact','open','drive','','1929–1931',
  'A Gothic Revival church on West Fifth Street, designed by Wiley G. Clarkson after Notre Dame in Paris and built by Harry B. Friedman. Ground was broken on October 29, 1929; the congregation moved in on October 30, 1930, and the church was dedicated on June 14, 1931.',
  'Two unequal bell towers with terra cotta tracery, a blind marbled arcade, tall lancet windows and a triple doorway, round a courtyard garden. Interior not checked.',
  'A Methodist church modelled on Notre Dame.',
  'An active church, 800 West Fifth Street; Sunday service times from the church\'s own page, read November 2026. '+DT,
  [['Historic Fort Worth: First United Methodist Church','https://historicfortworth.org/property/first-united-methodist-church-fifth'], ['First United Methodist Church of Fort Worth: worship','https://www.fumcfw.org/worship']],
  conf='', th=None, thn=None, brick='?', hours='Sundays 9:30 a.m. and 11 a.m., in the sanctuary'),
]

PIN_NOTES={
'tarrant-county-courthouse-fort-worth':'OpenStreetMap\'s outline of the courthouse; the Register point is about 40 m east of it.',
'tp-station-fort-worth':'Address lookup on 1600 Throckmorton Street. On the aerial it falls on the plaza beside a long building that is probably the station, so the pin marks the site.',
'livestock-exchange-building-fort-worth':'OpenStreetMap\'s building at 131 East Exchange Avenue; the address lookup put the number on West Exchange Avenue, about 200 m off.',
'fort-worth-stockyards-historic-district':'Wikipedia\'s point for the district, by East Exchange Avenue; the district covers many blocks round it.',
'blackstone-hotel-fort-worth':'Address lookup on 601 Main Street.',
'flatiron-building-fort-worth':'Address lookup on 1000 Houston Street.',
'sinclair-building-fort-worth':'Address lookup on 512 Main Street.',
'petroleum-building-fort-worth':'The National Register point, at Throckmorton and Sixth streets; the address lookup went to East Sixth Street, the wrong side of town.',
'fort-worth-main-post-office':'OpenStreetMap\'s outline of the post office at 251 West Lancaster Avenue.',
'farmers-and-mechanics-national-bank-fort-worth':'Address lookup on 714 Main Street.',
'first-national-bank-building-fort-worth':'Address lookup on 711 Houston Street.',
'will-rogers-memorial-center-fort-worth':'Address lookup on 3401 West Lancaster Avenue, in the middle of the complex.',
'north-fort-worth-high-school':'Address lookup on 600 Park Street.',
'fire-station-no-1-fort-worth':'Address lookup on 215 Commerce Street; on the aerial the small building is in the shadow of the towers beside it.',
'fort-worth-union-depot-ashton':'Address lookup on 1501 Jones Street.',
'first-united-methodist-church-fort-worth':'OpenStreetMap\'s outline of the church at 800 West Fifth Street.',
}
