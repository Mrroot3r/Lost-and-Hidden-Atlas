# Dallas, Texas: standing buildings named in a video about the city's old buildings, each checked against the
# National Register list for Dallas County, Wikipedia and the owners' own pages. The video was a tip only.
from data_b import N
from data_ma import W

DT = 'Parking: downtown street meters and pay garages; no one lot was checked.'

BATCH={'key':'dallas_ggtn','label':'Dallas, Texas: hotels, towers, courthouse, station and cathedral downtown','added':'2026-11-26 14:37'}

PLACES=[
N('adolphus-hotel-dallas','The Adolphus Hotel','Dallas','tx','hotel','standing',32.77976,-96.80053,'site','open','drive','hotels','1910–1912',
  'A luxury hotel built by the brewer Adolphus Busch on the site of the old Dallas City Hall, which he bought in June 1910 and pulled down. Designed by Thomas P. Barnett of St. Louis in the Beaux-Arts style, it opened on October 5, 1912; at 22 stories it was the tallest building in Texas until the Magnolia Building next door passed it ten years later. It was enlarged in 1916, 1926 and 1950, renovated in 1980 and again in 2017, and is still a working hotel.',
  'A tall Beaux-Arts tower with a heavily ornamented top, across the street from where Busch\'s earlier Oriental Hotel stood. The hotel\'s own page offers guided history tours of the building and has a public lobby, restaurants and bars. Interior detail not checked.',
  'The brewer\'s hotel that was the tallest building in Texas.',
  'A working hotel (part of Marriott\'s Autograph Collection), 1321 Commerce Street. The lobby, restaurants and bars are open to the public, and the hotel\'s page offers guided history tours; tour times not found. '+DT,
  [W('Adolphus Hotel'), ['The Adolphus (hotel\'s own page)','https://www.adolphus.com/']],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('magnolia-building-dallas','Magnolia Building (Magnolia Hotel)','Dallas','tx','civic','standing',32.78020,-96.79912,'site','open','drive','','1921–1922',
  'A 29-story Beaux-Arts tower that opened next to the Adolphus Hotel in August 1922, at a cost of $4 million, as the headquarters of the Magnolia Petroleum Company; for years it was the tallest building in Texas. In 1934 the company put its red neon Pegasus on the roof, and the winged horse became a symbol of the city. The city bought the building in 1977, and it became the Magnolia Hotel after 1997. The old sign was beyond repair, and a new Pegasus was lit on the roof at midnight on January 1, 2000.',
  'The red Pegasus on the roof, best seen in the skyline from the south. Inside, Wikipedia\'s photographs show an elevator lobby with Pegasus medallions. A copy of the original sign is shown at the Old Red Courthouse building (not checked since the museum there moved out).',
  'The oil company tower that put a flying red horse over Dallas.',
  'A working hotel, 1401 Commerce Street; what visitors who are not guests may see inside was not checked. '+DT,
  [W('Magnolia Hotel (Dallas, Texas)')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('kirby-building-dallas','Kirby Building (Busch Building)','Dallas','tx','civic','standing',32.78075,-96.79936,'site','view','drive','','1913',
  'A 17-story Gothic Revival office tower finished in 1913 for Adolphus Busch, to go with his Adolphus Hotel nearby; it was first called the Busch Building. Like many downtown towers it stood empty in the 1980s, and it then became the first Dallas high-rise turned from offices into apartments.',
  'Gothic tracery and pointed ornament on the street front. Now apartments; interior not checked.',
  '',
  'Privately owned apartments, 1509 Main Street. Seen from the street. '+DT,
  [W('Kirby Building')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('santa-fe-terminal-dallas','Santa Fe Terminal Buildings','Dallas','tx','rail','standing',32.77887,-96.80208,'site','view','drive','','1924–',
  'Four warehouse and office buildings put up from 1924 for the Gulf, Colorado and Santa Fe Railway, in a line from Commerce Street to Young Street, on the site of the railway\'s 1896 passenger depot. Freight cars ran into the buildings through tunnels under the streets, pulled by fireless steam locomotives charged from a boiler under the office building, until about 1950. Building No. 3 was pulled down in 1988; No. 1 still holds federal offices, No. 2 is lofts, and No. 4 became a hotel in 2009. Buildings No. 1 and No. 2 are on the National Register.',
  'The pin is Building No. 1, 1114 Commerce Street. Building No. 4 stands at the south end of the line, on Young Street. Wikipedia says remnants of the freight tunnels are still inside the buildings; they are not open to visitors.',
  'Warehouses that took freight trains in through tunnels under downtown.',
  'Building No. 1 is federal offices, No. 2 private lofts and No. 4 a hotel. Seen from the street. '+DT,
  [W('Santa Fe Terminal Complex')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('old-red-courthouse-dallas','Dallas County Courthouse (Old Red)','Dallas','tx','civic','standing',32.77853,-96.80729,'site','view','drive','','1892',
  'The county courthouse of 1892, built of red sandstone with marble trim in the Richardsonian Romanesque style to a design by Max A. Orlopp Jr. of Little Rock; four of the five courthouses before it had burned. Its 123-foot clock tower was taken off in 1919 as unsafe and rebuilt during a renovation finished in 2007. A newer courthouse replaced it in 1966; it was the Old Red Museum of local history from 2007, and the Texas Fifth District Court of Appeals moved in in 2024.',
  'Red sandstone walls and turrets, with the rebuilt clock tower. Dealey Plaza is next to it. Interior not checked.',
  'The red sandstone courthouse that got its clock tower back after 88 years.',
  'Owned by Dallas County and used by the Texas Fifth District Court of Appeals, 100 South Houston Street. Seen from the street on every side; public hours for the court were not checked. '+DT,
  [W('Dallas County Courthouse (Texas)')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('dallas-municipal-building','Dallas Municipal Building (old City Hall)','Dallas','tx','civic','standing',32.78139,-96.79382,'site','view','drive','','1913–1914',
  'The city\'s fourth city hall, a Beaux-Arts building designed by C. D. Hill & Company and opened on October 17, 1914, after the first builder went bankrupt. The police department used it and its 1956 annex. Lee Harvey Oswald was held here after President Kennedy\'s assassination, and was shot in its basement garage on November 24, 1963. City hall left in 1978 and the police in 2003; after years half empty it was renovated, and the University of North Texas at Dallas College of Law moved in in 2020.',
  'A classical front on Harwood Street, across from Main Street Garden Park. Interior not checked.',
  'The old city hall where Oswald was shot.',
  'Owned by the City of Dallas and used by the University of North Texas at Dallas College of Law, 106 South Harwood Street. Seen from the street. '+DT,
  [W('Dallas Municipal Building')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('davis-building-dallas','Davis Building (1926 Republic National Bank)','Dallas','tx','civic','standing',32.78060,-96.80060,'site','view','drive','','1925–1926',
  'A 20-story bank tower designed by Charles D. Hill, who died in January 1926, just before Republic National Bank held its first open house here on February 15, 1926. The bank moved out in 1954 and the building was renamed for its new owners, the Davis family among them. After a foreclosure in 1986 it was turned into 183 loft apartments from 2002; the domed cupola on top was lit in 2003 for the first time since 1954. It is now called the Drakestone.',
  'The domed cupola on the top. Interior not checked.',
  '',
  'Privately owned apartments, 1309 Main Street. Seen from the street. '+DT,
  [W('Davis Building (Dallas, Texas)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('neiman-marcus-building-dallas','Neiman Marcus Building','Dallas','tx','civic','standing',32.78077,-96.79748,'site','view','drive','','1914–',
  'The first Neiman Marcus store on Elm Street burned in 1913, and this one opened on September 15, 1914, four floors of red brick and white stone at Main and Ervay. A matching addition of 1927 by George Dahl doubled it and replaced the brick face with white terra cotta; floors were added in the 1950s and in 1983, to nine stories. It survived a fire in 1964 that destroyed millions of dollars of goods. The flagship store closed for good on September 30, 2026, after 112 years.',
  'A white terra-cotta store front in the Renaissance Revival manner; the Wilson Building is across Main Street. The store is closed; interior not open.',
  'The flagship store that closed after 112 years in 2026.',
  'Privately owned; the store closed on September 30, 2026, and what becomes of the building was not checked. 1618 Main Street. Seen from the street. '+DT,
  [W('Neiman Marcus Building')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('dallas-scottish-rite-temple','Dallas Scottish Rite Temple','Dallas','tx','civic','standing',32.77925,-96.79189,'site','view','drive','','1913',
  'Built in 1913 as the headquarters of the Scottish Rite Masons and other Masonic lodges of Dallas, in the Beaux-Arts classical style. It is a Dallas Landmark and a Recorded Texas Historic Landmark, and is on the National Register as part of the Harwood Street Historic District. The Scottish Rite still uses it, and calls it the Cathedral.',
  'A columned temple front at Harwood and Young streets. The Scottish Rite\'s page mentions a library and museum but gives no visiting hours; interior not checked.',
  '',
  'Owned and used by the Dallas Scottish Rite, 500 South Harwood Street. Seen from the street; its page invites visitors but gives no hours, so ask first. '+DT,
  [W('Dallas Scottish Rite Temple'), ['Dallas Scottish Rite (own page)','https://www.dallasscottishrite.org/']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('dallas-hall-smu','Dallas Hall, Southern Methodist University','University Park','tx','inst','standing',32.84530,-96.78490,'site','view','drive','','1912–1915',
  'The first building of Southern Methodist University, designed by the Chicago office of Shepley, Rutan and Coolidge after the Roman Pantheon and Jefferson\'s University of Virginia. Its cornerstone was laid on November 28, 1912 and it was dedicated in 1915, alone on a flat prairie on one of the highest points in the county, which gave the university its nickname, "the Hilltop". For a decade it held every classroom; the campus has since been built round it.',
  'A three-story brick building under a great dome, with a columned portico, at the head of the campus lawn. Interior not checked.',
  'The domed hall that stood alone on the prairie and gave SMU its nickname.',
  'Owned and used by Southern Methodist University, a private university, 3225 University Boulevard, University Park. The hall faces the long campus lawn; whether visitors may walk the grounds or go in, and where they may park, was not checked.',
  [W('Dallas Hall')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('dallas-union-station','Dallas Union Station','Dallas','tx','rail','standing',32.77606,-96.80754,'site','open','drive','stations','1914–1916',
  'One station for the railroads of Dallas, built by the Union Terminal Company that seven railroads chartered in 1912, to a design by Jarvis Hunt, who also designed Kansas City\'s Union Station. It opened in October 1916 and took the place of five stations; at its busiest about 80 trains a day stopped here. The last train before Amtrak left in 1969; Amtrak came back in 1974 and light rail in 1996. It was renamed for Representative Eddie Bernice Johnson in 2016.',
  'The restored Grand Hall on the second floor is meeting space now; the ground-floor waiting room and ticket window are used by Amtrak riders. Interior detail not checked.',
  'Still a working station after more than a century.',
  'A working station for Amtrak, DART light rail, the Trinity Railway Express and the Dallas Streetcar, 400 South Houston Street. The waiting room is open to travellers; station hours were not checked. '+DT,
  [W('Dallas Union Station')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('wilson-building-dallas','Wilson Building','Dallas','tx','civic','standing',32.78138,-96.79756,'site','view','drive','','1904',
  'An eight-story office and department-store building finished in 1904 for the cattleman John B. Wilson, designed by Sanguinet & Staats of Fort Worth after the Paris Opera house. It was the tallest building in Dallas until 1909 and drew the city\'s shopping east to Main and Ervay; a 12-story addition on Elm Street followed in 1911. The H. L. Green store here, whose lunch counter was the first in the city to be integrated in the 1960s, closed in 1997, and the building became loft apartments.',
  'Rounded corners and carved stone and brick work on three street fronts. Now apartments; interior not checked.',
  'The 1904 store and office block modelled on the Paris Opera.',
  'Privately owned apartments, 1623 Main Street. Seen from the street. '+DT,
  [W('Wilson Building (Dallas)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('mercantile-national-bank-building-dallas','Mercantile National Bank Building','Dallas','tx','civic','standing',32.78110,-96.79642,'site','view','drive','','1943',
  'A 31-story Art Deco bank tower designed by Walter W. Ahlschlager and finished in 1943, which Wikipedia calls the only major skyscraper built during the Second World War; its steel had been made before the halt on private building. It stands where the 1889 post office with its clock tower stood until 1936. The clock and spire on top date from 1958. The bank complex was empty from 1993 and the tower has since been made into apartments.',
  'Setbacks rising to the four-faced clock and weather spire. The stone base was covered with a modern curtain wall in the 1960s. Interior not checked.',
  '',
  'Privately owned apartments, 1800 Main Street. Seen from the street. '+DT,
  [W('Mercantile National Bank Building')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('cathedral-guadalupe-dallas','Cathedral Shrine of Our Lady of Guadalupe','Dallas','tx','worship','standing',32.78855,-96.79759,'site','open','drive','','1898–1902',
  'Built as Sacred Heart Cathedral after Dallas became a diocese in 1890: the cornerstone was laid on June 17, 1898 and it was dedicated on October 26, 1902, to a design by Nicholas J. Clayton. In 1975 the Spanish-speaking parish of Our Lady of Guadalupe joined it, and in 1977 it was renamed for her. The bell tower Clayton planned was never built until a recent renovation added it, with a 49-bell carillon. It was made a National Shrine in 2023.',
  'The new bell tower beside the old church. Interior not checked.',
  'A cathedral that waited a century for its bell tower.',
  'The cathedral of the Catholic Diocese of Dallas, 2215 Ross Avenue, in the Arts District. Open for Mass; the cathedral\'s page has announced its underground garage on Crockett Street as open for some services. '+DT,
  [W('Cathedral Santuario de Guadalupe (Dallas, Texas)'), ['Cathedral (own page)','https://www.cathedralguadalupe.org/']],
  conf='', th=None, thn=None, brick='?', hours='Weekdays: Mass in English at noon, in Spanish at 7 p.m.; Sunday times not checked'),
]

PIN_NOTES={
 'adolphus-hotel-dallas':'Address point for 1321 Commerce Street from an address lookup; on the building on the aerial.',
 'magnolia-building-dallas':'Address point for 1401 Commerce Street from an address lookup; on the building on the aerial.',
 'kirby-building-dallas':'Address point for 1509 Main Street from an address lookup; on the building on the aerial.',
 'santa-fe-terminal-dallas':'Address point for Building No. 1, 1114 Commerce Street, from an address lookup; on the building on the aerial.',
 'old-red-courthouse-dallas':'Address point for 100 South Houston Street from an address lookup; on the building on the aerial.',
 'dallas-municipal-building':'Address point for 106 South Harwood Street from an address lookup; on the building on the aerial.',
 'davis-building-dallas':'Address point for 1309 Main Street from an address lookup; on the building on the aerial.',
 'neiman-marcus-building-dallas':'Address point for 1618 Main Street from an address lookup; on the building on the aerial.',
 'dallas-scottish-rite-temple':'Address point for 500 South Harwood Street from an address lookup; on the building on the aerial.',
 'dallas-hall-smu':'Address point for 3225 University Boulevard from an address lookup; on the building on the aerial.',
 'dallas-union-station':'Address point for 400 South Houston Street from an address lookup; on the building on the aerial.',
 'wilson-building-dallas':'Address point for 1623 Main Street from an address lookup; on the building on the aerial.',
 'mercantile-national-bank-building-dallas':'Address point for 1800 Main Street from an address lookup; on the building on the aerial.',
 'cathedral-guadalupe-dallas':'Address point for 2215 Ross Avenue from an address lookup; on the aerial it falls in the shadow of the towers beside the church, next to its red roof.',
}
