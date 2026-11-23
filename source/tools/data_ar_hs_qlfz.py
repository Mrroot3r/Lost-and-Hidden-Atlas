# November 23, 2026: Hot Springs, Arkansas. The buildings named in a video walk through the town's old postcards were
# taken as leads; every fact below comes from a source opened in this session (Wikipedia, the National Park Service's
# Hot Springs pages, the Encyclopedia of Arkansas), never from the video. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'ar_hs_qlfz','label':'Arkansas: old Hot Springs, from the bathhouses to the churches','added':'2026-11-23 22:31'}

NPS='https://www.nps.gov/hosp/'
DT='Downtown Hot Springs: metered street parking and public lots along Central Avenue (not checked in detail).'

PLACES=[
N('hale-bathhouse-hot-springs','Hale Bathhouse (Hotel Hale)','Hot Springs','ar','hotel','standing',34.51470,-93.05323,'exact','open','walk','hotels','1892',
  'The oldest building you can see on Bathhouse Row, and at least the fourth bathhouse to carry the name of John Hale, who opened the first one in 1841. Most of it was finished in 1892 to a design by George and Fremont Orff; a 1914 remodel enlarged the red-brick building in the Classical Revival style, and in 1939 it was redone in the Mission Revival style with its brick covered in stucco (National Park Service). It closed as a bathhouse on October 31, 1978, and reopened in May 2019 as Hotel Hale, a nine-room hotel with a restaurant (Wikipedia).',
  'A stuccoed Mission-style front with a curved gable over the door and a red tile roof. A hot spring was boxed in tile in the basement in 1917 and is still there; a thermal cave cut into the hill behind, once used as a sweat room, is now a protected archaeological site and not open (National Park Service). The lobby and restaurant are open to the public as a working hotel.',
  '',
  'Leased from Hot Springs National Park and run as a private hotel and restaurant, 341 Central Avenue. The park\'s hours page says the restaurant\'s hours are on the hotel\'s own site, which did not give them when read. '+DT,
  [W('Bathhouse Row'),['National Park Service: Hale Bathhouse',NPS+'learn/historyculture/hale-bathhouse.htm'],['National Park Service: hours on Bathhouse Row',NPS+'planyourvisit/hours.htm']],
  brick='no',hours='?'),

N('maurice-bathhouse-hot-springs','Maurice Bathhouse','Hot Springs','ar','hotel','standing',34.51396,-93.05330,'exact','view','walk','hotels','1912',
  'Opened on January 1, 1912 in place of an older Victorian bathhouse called the Independent, renamed after its owner Charles Maurice. It had a gymnasium, a roof garden and twin elevators, and in the 1930s a therapeutic pool for arthritis and polio, the only pool on the Row; it closed in November 1974 (National Park Service). The sources differ on where its architect, George Gleim Jr., came from: Chicago (Wikipedia) or New York City (National Park Service).',
  'A stuccoed front in a mix of Italian Renaissance and Mediterranean styles, with an arched sun porch added in a 1915 remodel. Inside, out of reach, are stained glass skylights and the Roycroft Den, an Arts and Crafts room with a stone hearth (National Park Service). The Maurice Spring fountain and wall just north of it date from 1903 (Wikipedia).',
  '',
  'Hot Springs National Park, 359 Central Avenue. The building is empty: the park\'s hours page (May 2026) says it is closed for renovation, and its history page that it is to be leased. Seen from the Central Avenue sidewalk and the Grand Promenade behind the Row. '+DT,
  [W('Bathhouse Row'),['National Park Service: Maurice Bathhouse',NPS+'learn/historyculture/maurice-bathhouse.htm']],
  brick='no',conf='mixed'),

N('ozark-bathhouse-hot-springs','Ozark Bathhouse','Hot Springs','ar','hotel','standing',34.51262,-93.05378,'exact','open','walk','hotels','1922',
  'Built in the summer of 1922 for $93,000 in the Spanish Colonial Revival style, to a design by Mann and Stern of Little Rock, after the owners turned down three grander designs. It had 27 tubs and catered to middle-class bathers, and closed in 1977 (National Park Service). It housed the park\'s cultural center until the fall of 2024; since the summer of 2025 it holds the Mystic Ozark, an exhibit about the waters and legends of Hot Springs.',
  'Twin low towers either side of the front, with stepped-back windows, plaster window boxes found on no other bathhouse, and scroll-and-shield cartouches. The painted wooden porch enclosure was taken off in the late 1990s to bring back the open front (National Park Service).',
  '',
  'Hot Springs National Park, 425 Central Avenue; the exhibit inside is run privately. The park\'s hours page sends visitors to the Mystic Ozark\'s own site for daily hours; that site refused to open. '+DT,
  [W('Bathhouse Row'),['National Park Service: Ozark Bathhouse',NPS+'learn/historyculture/ozark-bathhouse.htm'],['National Park Service: hours on Bathhouse Row',NPS+'planyourvisit/hours.htm']],
  brick='?',hours='?'),

N('arlington-hotel-hot-springs','Arlington Hotel','Hot Springs','ar','hotel','standing',34.51733,-93.05297,'site','open','walk','hotels','1924',
  'The third hotel of the name. The first Arlington opened in 1875 and was pulled down for the second, a red-brick hotel of 300 rooms built in 1892–93, which burned on April 5, 1923, killing a fireman. The present hotel, designed by Mann and Stern in 1924 in the Spanish Colonial Revival style, stands at the fork of Central Avenue and Fountain Street; the old site became a park at the north end of Bathhouse Row. Al Capone is said to have taken a whole floor in the 1930s (Wikipedia).',
  'A huge twin-towered hotel closing the view up Central Avenue. Arlington Lawn, where the 1893 hotel stood, is across the street at the north end of the Row. Which rooms of the hotel a non-guest may walk into was not checked.',
  '',
  'A private hotel, 239 Central Avenue; its own site was taking bookings when read (November 2026). Newspapers from 2017 on report the city pressing the owners over the condition of the building. '+DT,
  [W('Arlington Hotel (Hot Springs National Park)'),['The hotel\'s own site','https://www.arlingtonhotel.com']],
  brick='no',hours='?'),

N('ohio-club-hot-springs','Ohio Club','Hot Springs','ar','hotel','standing',34.51481,-93.05391,'exact','open','walk','','1905',
  'Counted as the oldest bar in Arkansas that has never closed. It opened in 1905 as a bar and casino; after gambling was banned in 1913 and drink in 1919 it carried on as the "Ohio Cigar Store", with the bar behind a false wall and the tables upstairs. Al Capone, Lucky Luciano and Babe Ruth are among the patrons the Encyclopedia of Arkansas names. It is part of the Hot Springs Central Avenue Historic District.',
  'A small front with a rounded, dome-shaped bay of five arched windows painted blue and gold, and a bench outside with a life-size statue of Capone. Inside is the 1880s mahogany back bar brought from Cincinnati, carved with horse heads (Encyclopedia of Arkansas). Live music upstairs several times a week.',
  '',
  'A working bar and restaurant, 336 Central Avenue, across the street from Bathhouse Row. Its own site gives the kitchen\'s closing times only. '+DT,
  [['Encyclopedia of Arkansas: Ohio Club','https://encyclopediaofarkansas.net/entries/ohio-club-9408/'],['The club\'s own site','https://www.theohioclub.com']],
  brick='?',hours='Kitchen open until 10 p.m. Sunday to Thursday, until 11 p.m. Friday and Saturday'),

N('medical-arts-building-hot-springs','Medical Arts Building','Hot Springs','ar','civic','standing',34.51608,-93.05382,'exact','view','walk','','1929',
  'A 16-storey Art Deco tower of 1929 by Almand & Stuck, 180 feet tall, the first skyscraper in Arkansas and the tallest building in the state until 1960. All but its ground floor was shut to the public from 1991; in 2012 it was named endangered. The upper floors were bought in May 2021 to be made into a hotel (Wikipedia).',
  'The main door is framed by fluted pilasters under floral panels and a stone frieze with the building\'s name (Wikipedia). Whether the hotel conversion is finished was not checked.',
  '',
  'Private, 236 Central Avenue, at the north end of downtown near the Arlington. Seen from the street. '+DT,
  [W('Medical Arts Building (Hot Springs, Arkansas)')],brick='?'),

N('army-navy-hospital-hot-springs','Army and Navy Hospital','Hot Springs','ar','inst','standing',34.51236,-93.05269,'site','view','walk','','1933',
  'The War Department ran a hospital here for soldiers, sailors and veterans who came for the hot water. The present building, the second Army and Navy hospital, was built in 1933. The state then used it for more than 60 years as the Hot Springs Rehabilitation Center and later a career training school, until it emptied in May 2019; the Wikipedia article says it is unclear who owns it now. It is listed as the Army and Navy General Hospital Historic District.',
  'A great tiered building on the slope of Hot Springs Mountain behind the south end of Bathhouse Row, seen above the town from Central Avenue and Reserve Street. Empty and closed.',
  '',
  'Closed and empty since 2019, owner unclear (Wikipedia). Look from Reserve Street or from downtown; do not enter the grounds. '+DT,
  [W('Hot Springs National Park'),['Arkansas Historic Preservation Program: Register form','https://www.arkansasheritage.com/docs/default-source/national-registry/ga0218-pdf.pdf']],
  brick='no'),

N('garland-county-courthouse-hot-springs','Garland County Courthouse','Hot Springs','ar','civic','standing',34.50476,-93.05867,'site','open','drive','','1905',
  'A four-storey brick courthouse in the Classical Revival style, built in 1905 and gutted by the great fire of 1913, after which the inside was rebuilt; later additions to the south and west follow its style. A 1979 statewide survey judged it one of the most important courthouse buildings in Arkansas (Wikipedia).',
  'Projecting entrance fronts on the north and south sides. The interior was not checked.',
  '',
  'Garland County, at Ouachita Avenue and Hawthorne Street. A working courthouse; office hours not checked.',
  [W('Garland County Courthouse')],brick='?',hours='?'),

N('first-presbyterian-hot-springs','First Presbyterian Church','Hot Springs','ar','worship','standing',34.51759,-93.05748,'exact','view','walk','','1907',
  'A large stone church of 1907 in the Late Gothic Revival style, designed by Charles L. Thompson, on Whittington Avenue a short walk west of the Arlington (Wikipedia).',
  'A square, heavily buttressed tower on the right of the front and a lower one on the left, with the door in a broad pointed arch under a three-part stained glass window; a large stained glass window fills the end of the sanctuary (Wikipedia).',
  '',
  'An active church, 213 Whittington Avenue. Its own site gives only office hours; service times not read on a church page. Street parking.',
  [W('First Presbyterian Church (Hot Springs, Arkansas)'),['The church\'s own site','https://www.firstpreshotsprings.org']],brick='no'),

N('st-lukes-episcopal-hot-springs','St. Luke\'s Episcopal Church','Hot Springs','ar','worship','standing',34.51043,-93.05219,'exact','open','walk','','1925',
  'A stone Gothic Revival church at Spring and Cottage streets, designed by Thompson and Harding and finished in 1926 after a tornado wrecked the one before it; the parish dates from 1866 (Wikipedia, which also puts the building under 1925).',
  'A massive buttressed stone tower at the front with a tall parapet and a stained glass window above the entrance porch (Wikipedia).',
  '',
  'An active parish, 228 Spring Street, a block east of Central Avenue. Service times come from a web search result quoting the church\'s own page, which would not open directly. Street parking.',
  [W('St. Luke\'s Episcopal Church (Hot Springs, Arkansas)'),['The parish\'s own site','https://stlukeshs.org/what-to-expect']],
  brick='no',conf='mixed',hours='Sunday Holy Eucharist 8 a.m. and 10:45 a.m.'),

N('central-methodist-hot-springs','Central Methodist Episcopal Church, South','Hot Springs','ar','worship','standing',34.50513,-93.05556,'exact','view','drive','','1914–1915',
  'Now the First United Methodist Church. Built in 1914–15 to a design by John Gaisford of Memphis for a congregation founded in 1852; Gothic Revival outside, with Carpenter Gothic touches inside (Wikipedia). It stands at the south end of downtown.',
  'A one-storey masonry church with restrained Gothic detail. The interior was not checked.',
  '',
  'An active church, 1100 Central Avenue. Service times not read on a church page. Parking not checked.',
  [W('Central Methodist Episcopal Church South')],brick='?'),

N('visitors-chapel-ame-hot-springs','Visitors Chapel AME Church','Hot Springs','ar','worship','standing',34.50889,-93.05012,'exact','view','walk','','1913',
  'Built in 1913 to a design by J. H. Northington, the fourth known home of an African Methodist Episcopal congregation in Hot Springs since the 1870s. It is named for the many outsiders who came to worship (Wikipedia). It stands in the Pleasant Street Historic District, once the heart of Black Hot Springs.',
  'A brick church on a Greek cross plan with a dome at the centre, a classical gable front and towers with Gothic windows either side (Wikipedia).',
  '',
  'An active church, 319 Church Street. Service times not read on a church page. Street parking.',
  [W('Visitors Chapel AME'),W('Pleasant Street Historic District (Hot Springs, Arkansas)')],brick='?'),

N('hot-springs-high-school-1914','Hot Springs High School (1914)','Hot Springs','ar','civic','standing',34.50560,-93.05349,'site','view','drive','','1914',
  'A Late Gothic Revival school by Sanguinet & Staats, built in 1914 on Oak Street after the great fire of September 1913 burned the earlier high school on the same site. Bill Clinton graduated from it in 1964. The high school moved out in 1968; the building was a junior high until 1992 and was made into 32 homes, the Hot Springs High School Lofts, in 2006 (Wikipedia).',
  'A large Gothic Revival front. Private homes inside.',
  '',
  'Private apartments, Oak Street. Seen from the street.',
  [W('Hot Springs High School (Arkansas)')],brick='yes'),

N('mopac-depot-hot-springs','Missouri Pacific Depot','Hot Springs','ar','rail','standing',34.50752,-93.05270,'exact','view','drive','stations','1917',
  'Built about 1917 by the Missouri Pacific at the end of the branch from Malvern, where visitors changed off the St. Louis to Texas main line. For decades it was the main way into the resort (Wikipedia). It is now the city bus hub and a Greyhound station.',
  'A one-storey depot bent into a V to fit a triangular lot, under a tile hip roof on deep bracketed eaves, with a Tuscan tower and bays of round-arched windows (Wikipedia).',
  '',
  'City of Hot Springs transit centre, Broadway and Market Street. A working bus station; its hours not checked.',
  [W('Hot Springs station')],brick='yes'),

N('old-post-office-hot-springs','Old Post Office','Hot Springs','ar','civic','standing',34.50750,-93.04917,'area','view','drive','','1901',
  'A two-storey Renaissance Revival post office of 1901, steel and masonry faced in brick and stone, counted among the best buildings of its style in the city (Wikipedia).',
  'A five-bay front with the door in a round arch under a heavy keystone. Inside, the lobby keeps its red marble and quartersawn oak (Wikipedia); whether it can be entered was not checked.',
  '',
  'Convention Boulevard. Present use and owner not checked; seen from the street.',
  [W('Old Post Office (Hot Springs, Arkansas)')],brick='?'),
]

PIN_NOTES={
 'hale-bathhouse-hot-springs':'OpenStreetMap point for Hotel Hale, 341 Central Avenue; checked on the aerial.',
 'maurice-bathhouse-hot-springs':'OpenStreetMap point for the Maurice Bathhouse building; checked on the aerial.',
 'ozark-bathhouse-hot-springs':'OpenStreetMap point for the Ozark Bathhouse building; checked on the aerial.',
 'arlington-hotel-hot-springs':'OpenStreetMap point for the hotel building; checked on the aerial.',
 'ohio-club-hot-springs':'Street address 336 Central Avenue from an address lookup; checked on the aerial.',
 'medical-arts-building-hot-springs':'The address lookup for 236 Central Avenue fell in the street; moved about 50 m onto the tall tower the aerial shows on the west side.',
 'army-navy-hospital-hot-springs':'The Register list point for the district fell among small buildings to the east; moved onto the large tiered building the aerial shows on the hill behind the south end of Bathhouse Row.',
 'garland-county-courthouse-hot-springs':'Address lookup for 501 Ouachita Avenue, at Hawthorne Street; checked on the aerial.',
 'first-presbyterian-hot-springs':'Street address 213 Whittington Avenue from an address lookup; the Wikipedia coordinate is about 230 m away. Checked on the aerial.',
 'st-lukes-episcopal-hot-springs':'Street address 228 Spring Street from an address lookup; checked on the aerial.',
 'central-methodist-hot-springs':'Street address 1100 Central Avenue from an address lookup; checked on the aerial.',
 'visitors-chapel-ame-hot-springs':'Street address 319 Church Street from an address lookup; checked on the aerial.',
 'hot-springs-high-school-1914':'The Register list point fell in the street; moved about 40 m north onto the large school building on the aerial.',
 'mopac-depot-hot-springs':'Address lookup at Broadway Terrace, beside the Register list point; checked on the aerial.',
 'old-post-office-hot-springs':'Register list coordinate. The aerial shows trees and a parking lot with part of a building under the trees; the building could not be picked out for certain, so the pin is the area only.',
}
