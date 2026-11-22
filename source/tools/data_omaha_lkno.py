# November 22, 2026: downtown and South Omaha, Nebraska, from the names in one Old World Exploration video about Omaha
# (record: source/videos/20221211_KW1k7K10hiA.md). The video was a list of names only; every fact below comes from the
# sources linked on each place: Wikipedia articles, National Register nomination forms read as text from NPGallery,
# National Park Service "Travel Omaha" place pages, the HMdb marker and SAH Archipedia entry for the Anheuser-Busch office,
# and a Lodging Magazine report on the Blackstone's reopening. Pins are ArcGIS address points looked at on the aerial.
# Red brick: the Hill Hotel (dark red brick, Register form) and the Anheuser-Busch office (red brick, Register form) are
# 'yes'; the courthouse and Central High (Bedford limestone) and the First National Bank (light-coloured brick) are 'no';
# the rest are '?'.
from data_b import N
from data_ma import W

BATCH={'key':'omaha_lkno','label':'Omaha, Nebraska (from a video)','added':'2026-11-22 19:29'}

NPS='https://www.nps.gov/places/'
NR='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'

PLACES=[
N('douglas-county-courthouse-omaha','Douglas County Courthouse','Omaha','ne','civic','standing',41.25702,-95.93918,'exact','open','walk','','1909–1912',
  "Douglas County's third courthouse, designed by John Latenser Sr. in the French Renaissance Revival style and finished in 1912 on the block between 17th, 18th, Farnam and Harney streets. It replaced the 1885 courthouse on the same block, which was then torn down. In 1919 a mob set the building on fire and lynched Will Brown, a Black man falsely accused; the National Park Service says bullet holes from the riot can still be seen inside. The Omaha-Douglas Civic Center was built against it in the early 1970s.",
  look="Limestone on a granite base, with engaged Corinthian columns across the nine-bay north front on Farnam Street. Inside, the halls have mosaic floors and marble wainscoting. The National Park Service calls it a working county building partly open to the public.",
  accn="Owned and run by Douglas County as a working courthouse; the public may go into the parts that are open, through security. Downtown street and pay parking nearby (not checked). Hours not checked.",
  links=[W('Douglas County Courthouse (Nebraska)'),['National Park Service: Douglas County Courthouse',NPS+'douglas-county-courthouse.htm']],
  brick='no',hours='?'),
N('first-national-bank-building-omaha','First National Bank Building','Omaha','ne','civic','standing',41.25745,-95.9374,'exact','view','walk','','1917',
  "A fourteen-storey steel-frame bank and office tower at 16th and Farnam streets, built in 1917 for the First National Bank and designed by the Chicago firm Graham, Burnham & Co. Wikipedia calls it the first high-rise built in Omaha. It was turned into condominiums, offices and shops in 2000.",
  look="Light-coloured brick and stone above a ground floor of shops. The 1982 Register form describes a two-storey classical lobby with a coffered ceiling, ornamental plaster and Tennessee and Colorado marble; whether the lobby is open to visitors was not checked.",
  accn="Privately owned condominiums and offices: see it from 16th and Farnam streets. Downtown street and pay parking nearby (not checked).",
  links=[W('First National Bank Building (Omaha, Nebraska)'),['National Register nomination (1982)',NR+'82003187_text']],
  brick='no'),
N('blackstone-hotel-omaha','Blackstone Hotel (Kimpton Cottonwood Hotel)','Omaha','ne','hotel','standing',41.25742,-95.96645,'exact','open','walk','','1915',
  "Built in 1915 at 302 South 36th Street as a residential hotel of large suites, then run as a regular hotel from the 1920s; it was known on the Lincoln Highway for its restaurants, and Wikipedia says the Reuben sandwich was likely invented there. It became offices in 1984. After a $75 million restoration it reopened as the Kimpton Cottonwood Hotel, with 205 rooms (Lodging Magazine; the year of reopening was not checked).",
  look="Brick with terra cotta detailing on a steel frame. Lodging Magazine reports that the carved terra cotta columns, a marble staircase, original tile and wood floors and more than 800 windows were restored. It is a working hotel with restaurants, so the public rooms can be seen as a guest or diner.",
  accn="A privately owned working hotel in the Blackstone district on Farnam Street. Street parking and lots nearby (not checked). Hours not checked.",
  links=[W('Blackstone Hotel (Omaha, Nebraska)'),['Lodging Magazine: Kimpton Cottonwood Hotel opens','https://lodgingmagazine.com/kimpton-opens-first-hotel-in-nebraska-kimpton-cottonwood-hotel/']],
  brick='?',hours='?'),
N('omaha-central-high-school','Omaha Central High School','Omaha','ne','civic','standing',41.26069,-95.94329,'exact','view','walk','','1900–1912',
  "Omaha High School began in 1859 in the territorial capitol building, which stood on this hill until 1870. The present building, designed by John Latenser Sr., was built in four stages between 1900 and 1912 around the 1872 school, which was taken down from inside it once the new one was done. Wikipedia calls it the oldest high school building still in use in the city.",
  look="A French Renaissance Revival block of Bedford limestone, three storeys on a full basement, built round a central courtyard and approached by tiered walks from the east. The Register form notes a 200-foot round brick chimney stack at the west edge, and that Dodge Street was cut down in 1920, leaving the school higher above it.",
  accn="A working public school (Omaha Public Schools): see it from 20th and Dodge streets, not during school hours inside. Downtown street parking nearby (not checked).",
  links=[W('Omaha Central High School'),['National Register nomination (1979)',NR+'79003684_text']],
  brick='?'),
N('hill-hotel-omaha','Hill Hotel (Kensington Tower)','Omaha','ne','hotel','standing',41.25535,-95.93686,'site','view','walk','','1919',
  "A 13-storey hotel built in 1919 at 16th and Howard streets, at the south edge of downtown, and one of the last Colonial Revival buildings in Omaha (Wikipedia). It now holds apartments, with a bookshop on the ground floor.",
  look="Dark red brick above a stone base, with the top two storeys and attic in varied shades of red brick and terra cotta ornament at the roofline (Register form, which notes the shopfronts have been altered).",
  accn="Private apartments: see it from 16th Street. Downtown street and pay parking nearby (not checked).",
  links=[W('Hill Hotel (Omaha, Nebraska)'),['National Register nomination (1988)',NR+'88000377_text']],
  brick='yes'),
N('rose-blumkin-performing-arts-center','Riviera Theatre (The Rose)','Omaha','ne','civic','standing',41.25732,-95.94277,'exact','open','walk','','1926',
  "An atmospheric movie palace designed by John Eberson and opened in 1927 as the Riviera, with 2,776 seats; later the Paramount and the Astro. Threatened in the 1980s, it was bought and restored by Rose Blumkin, founder of Nebraska Furniture Mart, and is now The Rose, a children's and family theatre. A second restoration began in 2012.",
  look="A copper-domed tower on Farnam Street with two smaller towers, walls of diamond-patterned glazed brick, glazed terra cotta coping, and free-standing columns carrying griffins on the north and east sides. Inside can be seen by going to a show.",
  accn="Privately owned and run as The Rose theatre, 2001 Farnam Street: inside by ticket on show dates (rosetheater.org). Downtown street parking nearby (not checked).",
  links=[W('Rose Blumkin Performing Arts Center'),['National Park Service: Astro Theater',NPS+'astro-theater.htm'],['The Rose: box office','https://rosetheater.org/box-office']],
  brick='?',hours='?'),
N('livestock-exchange-building-omaha','Livestock Exchange Building','Omaha','ne','industry','standing',41.20989,-95.95577,'exact','view','walk','','1926',
  "The eleven-storey centrepiece of the Union Stockyards in South Omaha, designed by George Prinz and finished in May 1926. It held the Stockyards National Bank, offices, a cafeteria, shops, sleeping rooms and a convention hall among 260 acres of pens. In 1955 Omaha's yards passed Chicago's as the largest in the country; the last big packing house closed in 1976 and the yards in 1999. The building was turned into more than 100 apartments with community and commercial space by 2005.",
  look="An H-shaped tower in Romanesque and Northern Italian Renaissance Revival styles, standing over what were the yards; Metropolitan Community College has built a campus on part of the old stockyards site. Interior not checked.",
  accn="Mixed-use building run in a public-private partnership with the City of Omaha (National Park Service), at 4920 South 30th Street: see it from the street. Parking not checked.",
  links=[W('Livestock Exchange Building (Omaha, Nebraska)'),['National Park Service: Livestock Exchange Building',NPS+'livestock-exchange-building.htm']],
  brick='?'),
N('brandeis-store-building-omaha','J. L. Brandeis and Sons Store Building','Omaha','ne','civic','standing',41.25833,-95.93783,'site','view','walk','','1906',
  "The flagship of the Brandeis department store chain, at 16th and Douglas streets, designed by John Latenser Sr. and opened in 1906 as the largest store in downtown Omaha. It offered a restaurant, a post office, meeting rooms and free telephones. Two storeys were added in 1921, making ten. It now holds apartments, condominiums and shops.",
  look="A Second Renaissance Revival block with its front divided into bands of stone, brick and terra cotta. The top-floor ballroom has been made into apartments (Wikipedia).",
  accn="Privately owned apartments with shops at street level, 200 South 16th Street: see it from the street. Downtown street and pay parking nearby (not checked).",
  links=[W('J. L. Brandeis and Sons Store Building'),['National Park Service: J.L. Brandeis & Sons Store',NPS+'j-l-brandeis-sons-store-building.htm']],
  brick='?'),
N('anheuser-busch-beer-depot-omaha','Anheuser-Busch Beer Depot office','Omaha','ne','industry','standing',41.25324,-95.93261,'exact','view','walk','','1887',
  "Henry Voss designed this beer depot in 1887 for the Anheuser-Busch Brewing Association of St. Louis: beer came in by rail to a siding behind the vault and went out by wagon from a cobbled alley. The 1979 Register form described an office, a stable and a three-storey beer vault and icehouse; the HMdb marker and SAH Archipedia say only the office building is left. Wikipedia calls it the last structure of the Krug brewery, which Anheuser-Busch bought; the Register form names only Anheuser-Busch. In the 1960s and 1970s the office was a private house.",
  look="A small red brick office in Victorian Romanesque style, with round and flat-arched openings and corbelled brickwork (Register form), at 1213 Jones Street near the Old Market. Interior not checked.",
  accn="Private building: see it from Jones Street. Old Market street and pay parking nearby (not checked).",
  links=[W('Anheuser-Busch Beer Depot'),['National Register nomination (1979)',NR+'79001440_text'],['HMdb marker','https://www.hmdb.org/m.asp?m=35267'],['SAH Archipedia','https://sah-archipedia.org/node/16140']],
  conf='mixed',brick='yes'),
]

PIN_NOTES={
 'douglas-county-courthouse-omaha':'ArcGIS address point for 1701 Farnam Street, on the courthouse on the aerial.',
 'first-national-bank-building-omaha':'ArcGIS address point for 300 South 16th Street, on the tower at 16th and Farnam on the aerial.',
 'blackstone-hotel-omaha':'ArcGIS address point for 302 South 36th Street, on the hotel on the aerial.',
 'omaha-central-high-school':'ArcGIS address point for 124 North 20th Street, on the school on the aerial.',
 'hill-hotel-omaha':'The address point fell in 16th Street; moved about 20 m onto the building at the Register and Wikipedia coordinate. Which corner building it is was judged from the aerial only.',
 'rose-blumkin-performing-arts-center':'ArcGIS gave the corner of 20th and Farnam; moved about 30 m onto the theatre roof seen on the aerial, beside the Wikipedia coordinate.',
 'livestock-exchange-building-omaha':'ArcGIS address point for 4920 South 30th Street, on the tower on the aerial.',
 'brandeis-store-building-omaha':'The address point fell in the street; moved about 50 m onto the building at the Register coordinate, at the corner of 16th and Douglas.',
 'anheuser-busch-beer-depot-omaha':'ArcGIS address point for 1213 Jones Street.',
}
