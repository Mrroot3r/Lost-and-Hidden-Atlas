# November 23, 2026: Duluth, Minnesota, the buildings named in one walk-through video of old Duluth photographs, each
# checked in sources opened for this batch. The video is only the tip: no fact below comes from it.
# Facts come from Wikipedia read as raw text, the Register list for St. Louis County, National Register nomination forms
# read as text (Duluth Civic Center Historic District, 86003097; Fitger Brewing Company, 84001690; Duluth Masonic Temple,
# 15000215), and the owners' own pages read in a headless browser on November 23, 2026: the Fitger's complex
# (fitgers.com), the City of Duluth (duluthmn.gov), St. Louis County's office list, and the College of St. Scholastica's
# visit page. The Minnesota court system's Duluth pages could not be opened (a bot check).
# Brick values: from what the sources say each building is built of. Old Central is Lake Superior brownstone; the civic
# center buildings are grey granite; the Masonic Temple is brown pressed brick on red sandstone (not red brick: 'no').
# Fitger's street fronts are basalt and sandstone with some brick buildings; the picture
# 'Fitger's Brewery.jpg' shows dark stone with red sandstone trim and a red brick block at the west end: some. From pictures on
# Wikimedia Commons: 'College of St Scholastica.JPG' (grey stone, no red brick: no); 'Duluth Downtown 1.jpg' (red brick
# fronts among others on Superior Street: some).
from data_b import N
from data_ma import W

BATCH={'key':'duluth_vkqe','label':'Duluth, Minnesota','added':'2026-11-23 07:34'}

PLACES=[
N('old-central-high-school-duluth','Historic Old Central High School','Duluth','mn','civic','standing',46.78936,-92.10046,'exact','view','walk','','1891–1893',
  'Duluth\'s high school from 1893 to 1971: a three-storey Richardsonian Romanesque building of Lake Superior brownstone with a central clock tower, designed by the Duluth firm of Palmer & Hall, with most of the design by William Hunt. The cornerstone was laid in 1891 before about 7,000 people. After the school moved out in 1971 the building held offices and a small school; the district sold it in 2022 and a developer turned it into 122 apartments, finished in 2024.',
  'The clock tower with its ten-foot faces, made by E. Howard & Co. of Boston and installed in 1893, flanked by two small turrets, and the great entrance arch at its foot. Wikipedia says the conversion kept the auditorium (now a common room), the hallways and the lockers. It is now homes: look from the street. Interior not open to the public.',
  'A brownstone castle of a high school, clock and all, now flats.',
  accn='Privately owned apartments since 2024, downtown on the hill above Superior Street. View from the public sidewalks. Street parking downtown; parking not checked.',
  links=[W('Central High School (Duluth, Minnesota)'),['National Register nomination (1972)','https://npgallery.nps.gov/GetAsset/7a4a73b8-c6b2-4e27-ac59-dac3ed1e60d0/']],
  brick='no'),
N('duluth-masonic-temple','Duluth Masonic Temple (Masonic Center)','Duluth','mn','civic','standing',46.78795,-92.10022,'exact','view','walk','','1905',
  'A three-storey Beaux-Arts Masonic Temple at Lake Avenue and West Second Street, designed by John J. Wangenstein and finished in 1905. It is still the home of Duluth\'s Freemasons. It was listed on the National Register in 2015, as the long-standing centre of Duluth\'s most influential fraternal order and for its Scottish Rite auditorium, with an Egyptian-style frieze and 80 hand-painted stage backdrops, the largest working set left in Minnesota.',
  'The Register form describes brown pressed brick over a base of rock-faced red sandstone, with heavy stone trim, columns and pediments, and round-arched windows that keep their stained glass with Masonic symbols. The auditorium and its backdrops are inside; no public tour times were found: interior not checked.',
  'A working 1905 lodge whose theatre still has 80 painted backdrops.',
  accn='Privately owned, still the Freemasons\' home, 4 West Second Street. No visiting hours were found on any page read: look from the street. Street parking downtown; parking not checked.',
  links=[W('Duluth Masonic Center'),['National Register nomination (2015)','https://npgallery.nps.gov/GetAsset/328fd60a-fc09-4555-9689-648177105f9d']],
  brick='no'),
N('fitger-brewing-company-duluth','Fitger\'s Brewery complex','Duluth','mn','industry','standing',46.79221,-92.09088,'site','open','walk','','1886–1911',
  'The brewery grew out of one founded in 1859, the first commercial brewery at the head of Lake Superior, and brewed as Fitger\'s from 1881 until 1972. Most of the ten-building complex, which runs about 720 feet along East Superior Street above the lake, went up between 1886 and 1911. Business owners bought it after it closed and reopened it in December 1984 as shops, restaurants, a hotel and a museum of the brewery.',
  'The Register form singles out the Superior Street fronts of randomly laid native basalt with sandstone quoins and window trim, among the finest stonework of its kind in north-eastern Minnesota, and a stone retaining wall about 30 feet high and over 580 feet long along the railway on the lake side. Wikipedia says there is a brewery museum and a self-guided tour of parts of the complex.',
  'A lakeside stone brewery that stayed open through Prohibition by making soda and candy bars.',
  accn='Privately owned shops, restaurants and the Fitger\'s Inn, 600 East Superior Street. The hours are the complex\'s own, from its page read November 23, 2026; holiday hours may differ, and single businesses keep their own. Its page has a location and parking section that could not be read; parking not checked.',
  links=[W("Fitger's Brewing Company"),['Fitger\'s complex: hours and location','https://fitgers.com/'],['National Register nomination (1984)','https://npgallery.nps.gov/GetAsset/NRHP/84001690_text']],
  hours='Complex: Monday to Saturday 10 a.m. to 9 p.m., Sunday 11 a.m. to 5 p.m.',brick='some'),
N('st-louis-county-courthouse-duluth','St. Louis County Courthouse, Duluth Civic Center','Duluth','mn','civic','standing',46.78353,-92.10669,'exact','open','walk','','1909',
  'The focal building of the Duluth Civic Center, the government square Daniel Burnham planned in 1909 as a City Beautiful scheme and that was built over the next twenty years. Burnham\'s firm designed the courthouse, finished in 1909 and built of grey granite at a cost of nearly $1,000,000. The district, listed on the National Register in 1986, also holds City Hall (1928), the Federal Building (1929), the old county jail (1923) and the Soldiers and Sailors Monument by Cass Gilbert.',
  'A ground floor of round-arched windows and rusticated stone after early Renaissance Italian palaces, with a lion\'s-head stone above the front door. The Register form notes marble and granite floors and oak woodwork inside. In front, on the square, stands Cass Gilbert\'s monument of about 1921, with a 1960s fountain spilling down the slope before it.',
  'Daniel Burnham\'s plan for Duluth, built in granite round a square.',
  accn='St. Louis County, 100 North Fifth Avenue West. A working courthouse. Weekday hours are those the county gives for its offices in the building, read November 23, 2026; the courts\' own page could not be opened. The square and the monument are open ground. Street parking downtown; parking not checked.',
  links=[W('Duluth Civic Center Historic District'),['St. Louis County: offices in the Duluth Courthouse','https://www.stlouiscountymn.gov/departments-a-z/attorney/about-the-county-attorney/our-locations'],['National Register nomination (1986)','https://npgallery.nps.gov/GetAsset/NRHP/86003097_text']],
  hours='Monday to Friday 8 a.m. to 4:30 p.m.',brick='no'),
N('duluth-city-hall','Duluth City Hall','Duluth','mn','civic','standing',46.78392,-92.10535,'exact','open','walk','','1928',
  'The east side of the Duluth Civic Center, built in 1928 to designs by the Duluth firm of Shefchik & Olsen. The Register form says it follows Burnham\'s plan closely, and its likeness to the courthouse beside it is deliberate.',
  'Round-arched windows on the ground floor, paired windows above, then Doric columns rising four storeys to a plain frieze and a flat roof, all in rusticated stone. It faces the Federal Building across the square, the courthouse between them. Interior not checked.',
  accn='City of Duluth, 411 West First Street. Hours from the city\'s own page, read November 23, 2026. Street parking downtown; parking not checked.',
  links=[W('Duluth Civic Center Historic District'),['City of Duluth','https://duluthmn.gov/'],['National Register nomination (1986)','https://npgallery.nps.gov/GetAsset/NRHP/86003097_text']],
  hours='Monday to Friday 8:30 a.m. to 4 p.m.',brick='no'),
N('heaney-federal-building-duluth','Federal Building and U.S. Courthouse (Gerald W. Heaney Federal Building)','Duluth','mn','civic','standing',46.78253,-92.10653,'exact','view','walk','','1929',
  'The west side of the Duluth Civic Center, designed by federal government architects in 1929 to match City Hall across the square, at a cost of $1,200,000. It was built as the federal courthouse and custom house with a post office on the ground floor. An act of Congress named it for the federal judge Gerald Heaney in 2007.',
  'Round-arched windows on the ground floor and columns rising to a plain frieze and classical cornice, as on City Hall; the Register form gives it as 163 by 177 feet. Interior not checked.',
  accn='Federal government building, 515 West First Street. No visiting hours were looked for: look from the square. Street parking downtown; parking not checked.',
  links=[W('Duluth Civic Center Historic District'),['National Register nomination (1986)','https://npgallery.nps.gov/GetAsset/NRHP/86003097_text']],
  brick='?'),
N('tower-hall-st-scholastica-duluth','Tower Hall, College of St. Scholastica','Duluth','mn','inst','standing',46.8162,-92.10614,'exact','view','walk','','1909–1928',
  'The first building of the College of St. Scholastica, the Benedictine sisters\' school on the hill above Duluth. The sisters had come from St. Joseph, Minnesota, in 1892 and ran their academy elsewhere in the city before moving here in 1909. Franklin Ellerbe took over the design in 1908 after the first architects were let go; the first part was finished in 1909 and the hall, with two towers, Tudor towers flanking the front and turrets at each end of a 375-foot range, in 1928.',
  'The long stone front with its towers and turrets. Interior not checked.',
  'A castle-like convent school on the hill, begun in 1909.',
  accn='Private college campus, 1200 Kenwood Avenue. The college\'s visit page offers campus tours booked through admissions, and group visits on Tuesdays, Wednesdays and Thursdays; otherwise look from the campus roads. Campus parking rules not checked.',
  links=[W('College of St. Scholastica'),['College of St. Scholastica: visit','https://www.css.edu/visit/']],
  brick='no'),
N('duluth-commercial-historic-district','Duluth Commercial Historic District (Superior Street)','Duluth','mn','town','standing',46.787264,-92.098764,'area','public','walk','','1872–1929',
  'Duluth\'s old business district: five blocks of Superior Street and seven of West First Street, with 87 contributing buildings put up between 1872 and 1929. It was listed on the National Register in 2006 for its state-level significance in architecture and commerce, as a record of the city\'s growth at the turn of the twentieth century.',
  'A walk along Superior Street and First Street downtown. The Old Central High School, the Masonic Temple and the Civic Center are a few blocks up the hill.',
  accn='Public city streets, owned by the City of Duluth; the buildings along them are private. Any time. Street parking and public ramps downtown; parking not checked.',
  links=[W('Downtown Duluth')],
  brick='some'),
]

PIN_NOTES={
 'old-central-high-school-duluth':'OpenStreetMap building named for the apartments in the old school; checked on the aerial.',
 'duluth-masonic-temple':'Wikipedia point, about 10 m from the OpenStreetMap building at Lake Avenue and Second Street; checked on the aerial.',
 'fitger-brewing-company-duluth':'OpenStreetMap building for the Fitger\'s complex at 600 East Superior Street; checked on the aerial.',
 'st-louis-county-courthouse-duluth':'Moved about 40 m from the OpenStreetMap point onto the courthouse roof seen on the aerial.',
 'duluth-city-hall':'Moved about 40 m from the OpenStreetMap point onto the City Hall roof seen on the aerial.',
 'heaney-federal-building-duluth':'OpenStreetMap building for the Federal Building, 515 West First Street; checked on the aerial.',
 'tower-hall-st-scholastica-duluth':'OpenStreetMap building named Tower Hall; checked on the aerial.',
 'duluth-commercial-historic-district':'Register list point for the district, downtown; the pin marks the area only.',
}
