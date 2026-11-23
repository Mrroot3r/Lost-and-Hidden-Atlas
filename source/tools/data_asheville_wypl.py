# Asheville, North Carolina: buildings named in a video about the city's old buildings, each checked against the
# National Register list for Buncombe County, Wikipedia and the owners' own pages.
from data_b import N
from data_ma import W

def NR(ref, label): return [label + ' (National Register record)', 'https://npgallery.nps.gov/AssetDetail/NRIS/%s' % ref]

BATCH={'key':'asheville_wypl','label':'Asheville, North Carolina: Biltmore, the Grove Park Inn, Art Deco downtown and a castle on Sunset Mountain','added':'2026-11-23 02:59'}

PLACES=[
N('biltmore-house-asheville','Biltmore House (Biltmore Estate)','Asheville','nc','inst','standing',35.54078,-82.55316,'exact','open','drive','','1889–1895',
  'A French château-style mansion built from 1889 to 1895 for George Washington Vanderbilt II, who came to the Asheville area with his mother in the 1880s and bought about 125,000 acres, nearly 700 parcels, including more than 50 farms and the community of Shiloh. Richard Morris Hunt designed the house and Frederick Law Olmsted the grounds. With about 179,000 square feet of floor space it is the largest privately owned house in the United States, and it is still owned by Vanderbilt\'s descendants. The estate closed for a time after Hurricane Helene in September 2024.',
  'The house, its gardens and the estate grounds, shown by ticket. Entry to the house is by a timed reservation. Interior not checked here beyond what the estate advertises.',
  'The Vanderbilts\' 250-room château in the North Carolina mountains.',
  'Owned and run by the Vanderbilt family\'s estate company, 1 Lodge Street (the estate entrance by Biltmore Village). Tickets required, and a reserved entry time for Biltmore House; the estate\'s page says it is open every day with hours that vary by day and season (read November 2026). The pin is the house; visitor lots are near it on the estate roads.',
  [W('Biltmore Estate'),NR('66000586','Biltmore Estate'),['Biltmore: hours of operation','https://biltmore.com/visit/visitor-information/hours-of-operation']],
  conf='', th=[35.54272,-82.54916], thn='Walking Lot B, Shiloh Road (estate visitor parking)', brick='?', hours='Open every day; hours vary by day and season. House entry by reserved time'),

N('asheville-city-hall','Asheville City Hall','Asheville','nc','civic','standing',35.59547,-82.54843,'exact','view','walk','','1926–1928',
  'An Art Deco city hall of brick and stone built from 1926 to 1928 to plans by Douglas Ellington, who also designed Asheville High School and the First Baptist Church. It was meant as a twin to the new Buncombe County Courthouse beside it, but the county built in a taller, more conservative style, and the wing planned to join them was never built. Its outline is on the city\'s seal, and it still houses the city government. Listed on the National Register in 1976.',
  'The stepped, colourful roof and Art Deco ornament, best seen from Pack Square Park. The council chamber has five murals by Clifford Addams. Interior not checked.',
  'The Art Deco city hall whose silhouette is the city\'s seal.',
  'Owned by the City of Asheville, on Court Plaza at the east end of Pack Square Park. Seen from the park and the street at any time; whether the public may walk in outside meetings was not checked. Paid garages and street parking downtown.',
  [W('Asheville City Hall'),NR('76001307','Asheville City Hall')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('first-baptist-church-asheville','First Baptist Church of Asheville','Asheville','nc','worship','standing',35.5989,-82.5474,'exact','open','walk','','1925–1927',
  'The congregation formed about 1829 and outgrew three earlier buildings before hiring the architect Douglas Ellington, who lived near Asheville, to design this one, built from 1925 to 1927. It seats 2,000, with rooms for 3,000 more. It is a four-storey polygonal brick church in a Beaux-Arts form with Art Deco details, under a dome 90 feet across inspired by the cathedral of Florence. Listed on the National Register in 1976.',
  'The great dome of Ludowici tiles shading from dark red at the base to bright green at the top, the six-column portico and the pressed-brick walls. The congregation welcomes visitors to Sunday worship. Interior not checked.',
  'A tiled dome modelled on Florence, by the architect of City Hall.',
  'An active Baptist church at 5 Oak Street. Sunday worship at 11 a.m. and the office hours are from the church\'s own page, read November 2026. Street and lot parking nearby on Oak and Woodfin streets.',
  [W('First Baptist Church (Asheville, North Carolina)'),NR('76001308','First Baptist Church'),['First Baptist Church of Asheville','https://www.fbca.net/']],
  conf='', th=None, thn=None, brick='?', hours='Sunday worship 11 a.m. (Bible study 10 a.m.); office Monday to Thursday 8 a.m. to 4 p.m., Friday 8 a.m. to noon'),

N('grove-park-inn-asheville','Grove Park Inn','Asheville','nc','hotel','standing',35.62017,-82.54195,'exact','open','drive','hotels','1912–1913',
  'A resort hotel on the west slope of Sunset Mountain, begun after Edwin Wiley Grove and his son-in-law Fred Seely bought about 400 acres in 1909. Seely, who had no training as an architect, sketched it himself, and workers living in tents on the site built it in under a year; it opened on July 12, 1913. It was built of rough granite and furnished by the Roycrofters of East Aurora, New York. It has been enlarged several times and still runs as a resort; it closed for about six weeks after flooding from Hurricane Helene in 2024.',
  'The original block of rough granite boulders in the Arts and Crafts style, with views west over the Blue Ridge. Inside, the hotel kept its Roycroft furnishings when it opened. Interior not checked.',
  'Granite boulders and Arts and Crafts, built in under a year.',
  'A working hotel at 290 Macon Avenue, run by Omni Hotels. A hotel is open to guests at all hours; the hotel\'s own page could not be read when this was written, so rules for visitors who are not staying were not checked.',
  [W('The Omni Grove Park Inn'),NR('73001295','Grove Park Inn')],
  conf='', th=None, thn=None, brick='no', hours='?'),

N('overlook-castle-asheville','Overlook (Seely\'s Castle)','Asheville','nc','landmark','standing',35.61111,-82.53444,'exact','view','drive','','1912–1914',
  'A stone house on top of Sunset Mountain, built from 1912 to 1914 for Fred Loring Seely, the son-in-law of Edwin Wiley Grove, on ten acres Grove gave him. The Seelys lived there until Fred Seely died in 1942. Asheville-Biltmore College used it from 1949 to 1961; it then passed through two more owners before a family bought and restored it in 1984. Listed on the National Register in 1980.',
  'A castle-like house with two large windows looking out over the city, Jacobean ceilings inside and English gardens round it. It is a private home; interior not open.',
  'Fred Seely\'s castle above the Grove Park Inn.',
  'A private home, not open to the public. Whether it can be seen from a public road was not checked. Do not go up private drives.',
  [W('Overlook Castle'),NR('80002804','Overlook')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('basilica-of-st-lawrence-asheville','Basilica of St. Lawrence','Asheville','nc','worship','standing',35.59733,-82.55629,'exact','open','walk','','1905–',
  'A Catholic church designed and built in 1905 by the Spanish architect Rafael Guastavino, who is buried in it, with the architect Richard Sharp Smith. Its dome is said to be the largest free-standing elliptical dome in North America; Guastavino took as his model a 17th-century basilica in his native Valencia. Floors, ceilings and stairs are all of his tile vaulting. Pope John Paul II made it a minor basilica in 1993.',
  'The elliptical dome, the bright tiles on the tops of the towers, stained-glass windows many of them made in Munich, statues of saints made in Italy, and a high altar of Tennessee marble with a Spanish wood carving of the crucifixion above it. A gift shop opens after weekend Masses.',
  'Guastavino\'s tile dome, and his grave inside.',
  'An active parish of the Diocese of Charlotte, 97 Haywood Street. Sunday Mass times are from the diocese\'s page for the parish, read November 2026; the parish\'s own site could not be read. Downtown garages and street parking.',
  [W('Basilica of St. Lawrence (Asheville, North Carolina)'),NR('78001933','Church of St. Lawrence'),['Diocese of Charlotte: Basilica of St. Lawrence','https://charlottediocese.org/parishes/basilica-of-st-lawrence/']],
  conf='', th=None, thn=None, brick='?', hours='Sunday Mass 9 a.m. and noon (English), 4 p.m. (Spanish)'),

N('grove-arcade-asheville','Grove Arcade','Asheville','nc','civic','standing',35.59554,-82.55661,'exact','open','walk','','1926–1929',
  'A building filling a whole city block, put up from 1926 to 1929 in a Tudor and Gothic Revival style as the base for a skyscraper that was never built; it housed one of the first indoor shopping malls in America. The federal government bought it in 1943, and the National Climatic Data Center was there until 1995. The city took it over in 1997 and leased it to a foundation that restored it and reopened it in 2002 with shops, offices and flats.',
  'Moulded terra cotta pilasters, rounded corners, a set-back top storey with a bronze balcony, and the arcade inside, now lined with shops and restaurants.',
  'A shopping arcade built to carry a skyscraper that never came.',
  'Owned by the City of Asheville and run by the Grove Arcade Public Market Foundation, 1 Page Avenue. Building hours are from the arcade\'s own page, read November 2026; the shops keep their own hours. Downtown garages and street parking.',
  [W('Grove Arcade'),NR('76001306','Arcade Building'),['Grove Arcade: about','https://grovearcade.com/?p=3119']],
  conf='', th=None, thn=None, brick='?', hours='Monday to Saturday 9 a.m. to 7 p.m., Sunday 10 a.m. to 5 p.m.'),

N('asheville-high-school','Asheville High School (Lee H. Edwards High School)','Asheville','nc','civic','standing',35.57218,-82.55187,'exact','view','drive','','1927–1929',
  'The city\'s high school, designed by Douglas Ellington and opened on February 5, 1929, at a cost of $1.3 million. In 1935 it was renamed Lee H. Edwards High School after its principal, who died that year. Additions came in 1949, 1970 and 2006, and it is still a public high school. Listed on the National Register in 1996.',
  'The original 1929 building by the architect of City Hall and the First Baptist Church, seen from McDowell Street. A working school; interior not open.',
  'Ellington\'s Art Deco high school.',
  'Owned by Asheville City Schools, 419 McDowell Street. A working school: look from the street, not during school arrivals or departures.',
  [W('Asheville High School'),NR('96000481','Asheville High School')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('asheville-masonic-temple','Asheville Masonic Temple','Asheville','nc','civic','standing',35.59811,-82.55244,'exact','view','walk','','1913–1915',
  'A lodge building at 80 Broadway, planned in 1912 by Mount Hermon Lodge No. 118 and the Scottish Rite of Asheville and designed by Richard Sharp Smith, an English-born Freemason who had supervised building Biltmore House for Richard Morris Hunt. The contractor handed it over on April 29, 1915. The Scottish Rite took the third and fourth floors. It counts toward the Downtown Asheville Historic District.',
  'Four storeys of pressed brick with limestone and grey brick trim on a granite base, a red tile hipped roof over the front, and a two-storey portico of paired Ionic columns on Broadway. Interior not checked.',
  'Biltmore\'s supervising architect designed the Masons\' temple.',
  'Owned by the Masonic lodges, 80 Broadway. Seen from the street; whether it opens to visitors was not checked. Downtown street parking.',
  [W('Asheville Masonic Temple'),W('Downtown Asheville Historic District')],
  conf='', th=None, thn=None, brick='?', hours=''),
]

PIN_NOTES={
 'biltmore-house-asheville':'OpenStreetMap outline of Biltmore House; the Wikipedia coordinate is a rough point for the whole estate. Parking point from OpenStreetMap.',
 'asheville-city-hall':'OpenStreetMap point for Asheville City Hall on Court Plaza.',
 'first-baptist-church-asheville':'OpenStreetMap point for the church at 5 Oak Street.',
 'grove-park-inn-asheville':'OpenStreetMap point for the hotel at 290 Macon Avenue.',
 'overlook-castle-asheville':'OpenStreetMap point for Overlook Castle, the same as the National Register point; on the house on the aerial.',
 'basilica-of-st-lawrence-asheville':'OpenStreetMap point for the basilica at 97 Haywood Street.',
 'grove-arcade-asheville':'OpenStreetMap outline of the Grove Arcade at 1 Page Avenue.',
 'asheville-high-school':'OpenStreetMap outline of the school building on McDowell Street.',
 'asheville-masonic-temple':'Wikipedia coordinate for the temple at 80 Broadway.',
}
