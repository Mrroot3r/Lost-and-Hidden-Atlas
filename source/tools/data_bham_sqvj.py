# November 22, 2026: downtown Birmingham, Alabama, and the Highlands just south of it.
# The names came from a video walk-through of the city's old buildings (a tip only, never a source); every fact here is
# from a page read for this batch: SAH Archipedia (Alabama Power, First United Methodist, the Cathedral of St. Paul, the
# Empire Building), the National Register nomination forms on NPGallery (First Presbyterian, Empire, Woodward, Ridgely),
# Wikipedia, the Encyclopedia of Alabama (Lyric Theatre, Southside Baptist), Bham Now (Tutwiler Hotel), and the
# churches' own pages for service times.
from data_b import N
from data_ma import W
BATCH={'key':'bham_sqvj','label':'Birmingham, Alabama: the old downtown and the Highlands','added':'2026-11-22 14:45'}

def SAH(n,label):
    return ['SAH Archipedia: '+label,'https://sah-archipedia.org/node/'+n]
def NR(ref,label):
    return ['National Register nomination: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'+ref+'_text']
DOWNTOWN=' Downtown Birmingham has metered street parking and paid lots; parking was not checked on the ground.'
HEAVY=['Wikipedia: Heaviest Corner on Earth','https://en.wikipedia.org/wiki/Heaviest_Corner_on_Earth']

PLACES=[
N('alabama-power-building-birmingham','Alabama Power Building','Birmingham','al','civic','standing',33.51799,-86.81296,'exact','view','drive','','1924–1925',
  'Alabama Power Company\'s headquarters, a sixteen-storey Art Deco tower of 1924 to 1925 by the Birmingham firm Warren, Knight and Davis, at 600 18th Street North. Later wings were added in 1950–51, 1957–58 and 1981–87, and the old building was renovated in 1987–88. The company said at the time that most of its main materials came from within 60 miles of the city.',
  'A brick shaft on a limestone base, with patterns in red and buff brick and buff tile near the top under a peaked red-tile roof. Over the entrance are three eight-foot limestone figures for power, light and heat by Edward Field Sanford Jr., and on the roof the gilded bronze statue called Electra, about 23 feet tall, holding lightning bolts. The street loggia has a painted terra-cotta ceiling and coffers each holding a bare light bulb. Inside is a marble-lined lobby with gilded column capitals; whether the public may go in was not found, so look from the street.',
  'A power company\'s Art Deco tower with a gilded goddess of electricity on its roof.',
  'A working office building of Alabama Power Company: look from 18th Street North and 6th Avenue North.'+DOWNTOWN,
  [SAH('7773','Alabama Power Company Corporate Headquarters'),['Alabama Power: the exhibit in the 1925 building','https://www.alabamapower.com/news/community/alabama-power-opens-exhibit-celebrating-states-development.html']],
  brick='some', hours=''),

N('first-united-methodist-birmingham','First United Methodist Church, Birmingham','Birmingham','al','worship','standing',33.51816,-86.81057,'exact','view','drive','','1890–1891',
  'The congregation began in 1872 as the First Methodist Episcopal Church, South, two months after Birmingham was incorporated; this is its third building, after a frame church and a brick one. Weary and Kramer designed it and Gilreath-Decker built it in 1890–91, in the Richardsonian Romanesque style, at 518 19th Street North. An addition came in 1950–51 and a restoration in 2014. It was listed on the National Register in 1982, and by the 2010s the congregation often called itself First Church Birmingham.',
  'Rough-faced brownstone walls, deep round arches and a tall square bell tower with a pyramid roof on the street corner. Inside is a semicircular auditorium on the Akron plan, with curving pews, two large rose windows and the choir in a great arch before the organ pipes. Service times were not checked: look from the street, or go in at a service.',
  'Birmingham\'s finest Romanesque church, in brownstone, from the city\'s first iron boom.',
  'An active church at 19th Street North and 6th Avenue North.'+DOWNTOWN,
  [W('First United Methodist Church (Birmingham, Alabama)'),SAH('7774','First United Methodist Church')],
  brick='no', hours='?'),

N('cathedral-st-paul-birmingham','Cathedral of St. Paul, Birmingham','Birmingham','al','worship','standing',33.51775,-86.80456,'exact','open','drive','','1890–1893',
  'Birmingham\'s Irish Catholics built a small frame church on this block in 1872. The present church, by the Chicago architect Adolphus Druiding with the contractor Lawrence Scully, was begun in 1890 and dedicated on November 30, 1893, at a cost of about $90,000; labour disputes slowed the work. Its pastor James Coyle was shot dead by a Klansman in 1921. It became the cathedral of the new Diocese of Birmingham in 1969, and a $6.5 million exterior repair was finished in 2015.',
  'High Victorian Gothic in pressed brick with stone trim, with two slender octagonal spires 185 feet high clad in patterned slate, and stone statues at the door that came from the high altar of 1905. Inside: a 67-foot nave on slender piers, ribbed vaults, clerestory windows and many stained-glass windows, among them St. Patrick and the Holy Family. The great west window was remade in 1972 in faceted glass set in concrete. The parish says the church is usually open for prayer on weekdays.',
  'A twin-spired Gothic church built for the city\'s Irish ironworkers.',
  'The Cathedral parish runs it (2120 3rd Avenue North). Hours from the parish\'s schedule and "Location, Parking and Hours" pages, read November 2026.'+DOWNTOWN,
  [W('Cathedral of Saint Paul (Alabama)'),SAH('7771','Cathedral of Saint Paul'),['Cathedral of St. Paul: Mass schedule','https://stpaulsbhm.org/sacred-liturgy/schedules'],['Cathedral of St. Paul: location, parking and hours','https://stpaulsbhm.org/about/location-parking-hours/']],
  brick='?', hours='Church usually open Mon–Fri about 8 a.m.–2:30 p.m.; Mass Sat 5 p.m., Sun 7:15, 8:30 and 11 a.m., Mon–Fri 6:30 a.m. and 12:10 p.m.'),

N('first-presbyterian-birmingham','First Presbyterian Church, Birmingham','Birmingham','al','worship','standing',33.51824,-86.80611,'exact','open','drive','','1888',
  'A Victorian Gothic church of 1888 at 2100 4th Avenue North, one of the oldest church buildings left downtown. It was listed on the National Register in 1982.',
  'Red pressed brick with stone tracery, pointed and Tudor arches, coloured decoration and ornamental terra-cotta tiles. The big bell tower with pinnacles, tall open tracery windows and a pointed spire is the thing to see; narrow towers flank the entrance. The stained glass is by D\'Ascenzo Studios of Philadelphia, from the 1940s and 1950s. Go in at the Sunday service.',
  'Red brick Gothic of 1888 with a pinnacled tower.',
  'An active church; the service time is from the church\'s own visiting page, read November 2026.'+DOWNTOWN,
  [W('First Presbyterian Church (Birmingham, Alabama)'),NR('82001604','First Presbyterian Church'),['First Presbyterian Church: visiting','https://endive-prism-l34h.squarespace.com/visiting-1']],
  brick='yes', hours='Sunday worship 11 a.m.; Sunday school 9:45 a.m.'),

N('empire-building-birmingham','Empire Building (Elyton Hotel)','Birmingham','al','civic','standing',33.51459,-86.80605,'exact','open','drive','','1908–1909',
  'A sixteen-storey steel-frame skyscraper of 1908–09 by Carpenter and Blair of New York with Warren and Welton, built for Robert Jemison Jr.\'s Empire Improvement Company at 1928 1st Avenue North. It is one of the four towers on the "Heaviest Corner on Earth" at 20th Street and 1st Avenue North, a booster\'s name for four of the tallest buildings in the South going up there between 1902 and 1912. A bank used it from 1964 until 2009; after standing empty it reopened in July 2017 as the Elyton Hotel.',
  'White and coloured terra cotta on both street fronts: two pinkish granite Doric columns at the entrance, twisted columns, busts and foliage on the lower floors, and at the top round-arched windows on a diamond-patterned coloured wall, with a big "E" in shields along the cornice. A marker of 1985 on the sidewalk outside tells the story of the corner. The ground floor and rooftop bar belong to the hotel.',
  'The white terra-cotta tower on the "Heaviest Corner on Earth".',
  'A working hotel; hours were not looked up.'+DOWNTOWN,
  [SAH('23912','Elyton Hotel (Empire Building)'),NR('82002040','Empire Building'),HEAVY],
  brick='no', hours='?'),

N('john-hand-building-birmingham','John Hand Building (American Trust and Savings Bank)','Birmingham','al','civic','standing',33.51443,-86.80522,'exact','view','drive','','1912',
  'Finished in 1912 as the American Trust and Savings Bank Building, at 20 storeys and 287 feet it was the tallest in the city until 1913, and the last of the four towers on the "Heaviest Corner on Earth". AmSouth and the banks before it owned it until the mid-1990s; it was renovated for $20 million in 2000 and now holds offices below and homes above. It was listed on the National Register in 1983.',
  'Glazed white terra cotta in the Classical Revival style, on the corner of 20th Street and 1st Avenue North, across from the Empire and Woodward buildings. Interior not checked.',
  'The tallest of the four towers on the "Heaviest Corner".',
  'Offices and private homes: look from the street.'+DOWNTOWN,
  [W('John Hand Building'),SAH('23912','the Heaviest Corner, in the Empire Building entry'),HEAVY],
  brick='no', hours=''),

N('woodward-building-birmingham','Woodward Building','Birmingham','al','civic','standing',33.51408,-86.8058,'exact','view','drive','','1902',
  'The first of the four towers on the "Heaviest Corner on Earth": ten storeys, built in 1902 to designs by Stone Brothers of New Orleans with William C. Weston, at 20th Street and 1st Avenue North. It is listed on the National Register.',
  'A Chicago-style steel-frame tower faced in brown brick, with terra-cotta mouldings dividing a two-storey base, seven middle floors and a top floor under a classical cornice; the windows come in threes between tall piers. The base was refaced in black granite and green glazed terra cotta in the early 1930s. The Register form says the interior was remodelled many times and was never notable.',
  'The oldest skyscraper on the "Heaviest Corner".',
  'A private building: look from the street.'+DOWNTOWN,
  [NR('83002977','Woodward Building'),HEAVY],
  brick='no', hours=''),

N('boutwell-auditorium-birmingham','Boutwell Auditorium (Municipal Auditorium)','Birmingham','al','civic','standing',33.5218,-86.81119,'site','view','drive','','1924',
  'Built in 1924 as Birmingham\'s Municipal Auditorium, facing Capitol Park (now Linn Park), to a design by the theatre architect Thomas W. Lamb with a committee of local architects. It holds about 4,300 people and was renamed for Mayor Albert Boutwell. A later renovation put a modern lobby of marble, aluminium and glass in front of the brick facade. The city still owns it.',
  'Inside, horseshoe seating with a stage at one end and a balcony at the other; it still holds concerts, sports and other events (it was a venue of the 2022 World Games). From outside the modern front hides most of the old brick one. Go in only with a ticket for an event.',
  '',
  'Owned by the City of Birmingham, on 8th Avenue North beside the Birmingham Museum of Art; open for events only.'+DOWNTOWN,
  [W('Boutwell Memorial Auditorium')],
  brick='?', hours=''),

N('lyric-theatre-birmingham','Lyric Theatre','Birmingham','al','civic','standing',33.51533,-86.80967,'exact','open','drive','','1912–1914',
  'A vaudeville house built in 1912–14 by Gen. Louis V. Clark at the back of a six-storey commercial building on 3rd Avenue North, opposite the Alabama Theatre. It opened in January 1914 and booked acts such as the Marx Brothers, Mae West and Will Rogers; it was one of the first theatres where Black and white patrons could see the same show for the same price, though seated apart, with Black patrons sent round to an 18th Street door and the upper balcony. It became a cinema in 1933, closed in 1958, was later an art-film house and then an adult cinema, and stood empty until Birmingham Landmarks bought it in 1993. After a $7.4 million campaign it reopened for live shows on January 14, 2016.',
  'The two box offices under the decorated entrance arch are original; the two marquees are copies of those of 1914, and the white cornice is gone. Inside: about 750 seats on the floor and mezzanine, 23 opera boxes, blue and gold plasterwork and a painted proscenium and curtain with scenes from Greek mythology. Go in for a show.',
  'A 1914 vaudeville theatre, shut for decades and brought back to life in 2016.',
  'Run by Birmingham Landmarks, the nonprofit that also runs the Alabama Theatre; show times were not looked up.'+DOWNTOWN,
  [['Encyclopedia of Alabama: Lyric Theatre','https://encyclopediaofalabama.org/article/lyric-theatre/']],
  brick='yes', hours='?'),

N('thomas-jefferson-tower-birmingham','Thomas Jefferson Tower (Thomas Jefferson Hotel)','Birmingham','al','hotel','standing',33.51299,-86.81062,'exact','view','drive','','1926–1929',
  'A 350-room hotel at 1623 2nd Avenue North designed by David O. Whilldin. Work began in May 1926, stopped in April 1927 when a backer failed, resumed in July 1928, and the hotel opened on September 7, 1929, having cost $2.5 million. It declined in the 1970s, was renamed the Cabana Hotel in 1972, and was shut by city health officials on May 31, 1983. It later became apartments, the Thomas Jefferson Tower.',
  'The tower on the roof was meant as a mooring mast for airships; its top was replaced in August 2016, returning it to its first look. The hotel had a marble lobby and a large ballroom. Now private apartments: look from the street.',
  'A 1929 hotel with an airship mooring mast on its roof.',
  'Private apartments: look from 2nd Avenue North.'+DOWNTOWN,
  [W('Thomas Jefferson Hotel')],
  brick='?', hours=''),

N('tutwiler-hotel-ridgely-birmingham','Tutwiler Hotel (Ridgely Apartments)','Birmingham','al','hotel','standing',33.52014,-86.80802,'exact','open','drive','','1913–1914',
  'Built as the Ridgely, Birmingham\'s first luxury apartment hotel downtown, financed by Maj. Edward Magruder Tutwiler for the developer Robert Jemison Jr., with a roof garden and playground, a cafe and shops. The Register form dates it 1914 and a 2026 news article 1913. In the mid-1980s it was made over as the "new" Tutwiler Hotel, named after the original Tutwiler (1914), which was pulled down in 1974. It reopened in 2007 as a Hampton Inn, and after a renovation begun under owners who bought it in 2023 it was to reopen as a DoubleTree by Hilton.',
  'Eight or nine storeys (the sources differ) of deep red brick with cream terra-cotta trim and a two-storey arch motif, a brick drive curving through the front courtyard, and a marble entrance porch with Corinthian pilasters. The Register form says the lobby kept its marble wainscot and balusters. Balconies under the arched windows were removed.',
  'Birmingham\'s first luxury apartment hotel, now a hotel itself.',
  'A working hotel at 2021 Park Place; hours were not looked up.'+DOWNTOWN,
  [NR('84000634','Ridgely Apartments'),['Bham Now: Tutwiler Hotel reopening, July 2026','https://bhamnow.com/2026/07/14/tutwiler-hotel-teases-grand-reopening-as-new-doubletree-by-hilton/']],
  brick='yes', hours='?', conf='mixed'),

N('temple-emanu-el-birmingham','Temple Emanu-El, Birmingham','Birmingham','al','worship','standing',33.50021,-86.79379,'exact','view','drive','','1912',
  'A Reform congregation whose first holy-day services were held in 1881, with Samuel Ullman as founding president. Its first temple, of 1886–89 at 5th Avenue North and 17th Street, had a corner tower and onion-domed turrets; in 1912 it moved to this neoclassical sanctuary at 2100 Highland Avenue South, designed by William C. Weston. The sanctuary was restored and the other buildings rebuilt in 2004 for $17 million.',
  'A neoclassical temple on Highland Avenue. Interior not checked; service times were not looked up, so look from the street.',
  '',
  'An active synagogue in the Highland Avenue Historic District.'+' Street parking nearby; parking was not checked on the ground.',
  [W('Temple Emanu-El (Birmingham, Alabama)')],
  brick='?', hours=''),

N('st-marys-on-the-highlands-birmingham','St. Mary\'s-on-the-Highlands Episcopal Church','Birmingham','al','worship','standing',33.49926,-86.79688,'exact','open','drive','','',
  'The parish was founded on February 11, 1887, by members who left the Church of the Advent, as a neighbourhood church for the Highlands, the city\'s first streetcar suburb. The parish says its original buildings are gone; when the present church at 1910 12th Avenue South was built was not checked.',
  'A photograph of 2012 on Wikimedia Commons shows a rough-stone Gothic church with a square corner tower, a large traceried window in the gable and a slate roof. Interior not checked. Go in at a Sunday service.',
  '',
  'An active Episcopal parish; service times are from its own home page, read November 2026. Street parking nearby; parking was not checked on the ground.',
  [['St. Mary\'s-on-the-Highlands: history','https://www.stmarysoth.org/history'],['St. Mary\'s-on-the-Highlands: home page and services','https://www.stmarysoth.org']],
  brick='no', hours='Sunday worship 8 a.m., 10:30 a.m. and 5 p.m.', conf='mixed'),
]

PIN_NOTES={
 'alabama-power-building-birmingham':'Address point for 600 18th Street North from the ArcGIS geocoder.',
 'first-united-methodist-birmingham':'OpenStreetMap point for the church, matching the National Register list position; on the aerial it sits on a round roof, which fits the semicircular auditorium.',
 'cathedral-st-paul-birmingham':'OpenStreetMap point for the cathedral, matching the National Register list position.',
 'first-presbyterian-birmingham':'OpenStreetMap point for the church, matching the National Register list position.',
 'empire-building-birmingham':'OpenStreetMap point for the Elyton Hotel at 1928 1st Avenue North.',
 'john-hand-building-birmingham':'OpenStreetMap outline of the First National-John A. Hand Building.',
 'woodward-building-birmingham':'OpenStreetMap outline of the Woodward Building.',
 'boutwell-auditorium-birmingham':'OpenStreetMap point for Boutwell Auditorium. On the aerial it falls on a flat roof beside a larger hall, and which of the two is the auditorium could not be told, so the pin marks the site.',
 'lyric-theatre-birmingham':'OpenStreetMap point for the Lyric Theatre at 1800 3rd Avenue North.',
 'thomas-jefferson-tower-birmingham':'Address point for 1623 2nd Avenue North from the ArcGIS geocoder.',
 'tutwiler-hotel-ridgely-birmingham':'Address point for 2021 Park Place from the ArcGIS geocoder.',
 'temple-emanu-el-birmingham':'OpenStreetMap point for the synagogue.',
 'st-marys-on-the-highlands-birmingham':'Address point for 1910 12th Avenue South from the ArcGIS geocoder.',
}
