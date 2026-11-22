# November 22, 2026: Cleveland, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Cleveland buildings (the record is source/videos/20221203_hvRfITuDjbs.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links) and the National Register list for Cleveland;
# the pages of whoever runs each place for hours (Lake View Cemetery, the Cleveland Museum of Art, Cleveland Public
# Library, West Side Market, the Shrine Church of St. Stanislaus, Trinity Cathedral, the Soldiers' and Sailors'
# Monument Commission, the Arcade); the Encyclopedia of Cleveland History for the monument. Pins are ArcGIS address
# points (or, on Public Square and in Lake View Cemetery, the Wikipedia point), each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'cleveland_lnbb','label':'Ohio: old Cleveland, from Public Square to University Circle','added':'2026-11-22 11:32'}

DT=' Downtown street meters and public garages are close by; their hours and fees were not checked.'
UC=' University Circle has paid lots and garages; the Cleveland Museum of Art garage is off Jeptha Drive; fees not checked.'

PLACES=[
N('soldiers-sailors-monument-cleveland','Soldiers\' and Sailors\' Monument','Cleveland','oh','landmark','standing',41.49956,-81.69301,'exact','open','walk','','1894',
  'Cuyahoga County\'s Civil War monument, honouring more than 9,000 people from the county who served the Union. Levi Scofield, an architect and Civil War veteran, designed it and its sculptures without fee, and it was dedicated on July 4, 1894, on the southeast quarter of Public Square. An acid cleaning in the 20th century stripped the paint from the inside walls; a restoration put the colours back, and the monument reopened in December 2009 and was rededicated in 2010.',
  'A granite shaft 125 feet high topped by a 15-foot figure of Liberty, rising from a memorial room on a terrace of red Medina sandstone with four bronze groups for the infantry, cavalry, artillery and navy. Inside, the names of the county\'s veterans are cut on tablets round the walls, with four large bronze panels round the base of the shaft and 14 stained glass windows above the tablets, re-leaded in 2008. Its small details are military: cannons under the window sills, ramrods for column edges. Wikipedia says it is regularly open to the public, free.',
  'A Civil War memorial room with the names of every county veteran on its walls, in the middle of Public Square.',
  'Run by the Cuyahoga County Soldiers\' and Sailors\' Monument Commission, on Public Square, which is open ground. Entry is free. The commission\'s own page, as read in November 2026, listed events but no daily opening hours.'+DT,
  [W('Soldiers\' and Sailors\' Monument (Cleveland)'),['Soldiers\' and Sailors\' Monument Commission','https://www.soldiersandsailors.com/'],['Encyclopedia of Cleveland History: Soldiers and Sailors Monument','https://case.edu/ech/articles/s/soldiers-and-sailors-monument']],
  brick='no',hours='?'),

N('cleveland-arcade','The Arcade','Cleveland','oh','civic','standing',41.49997,-81.69028,'exact','open','walk','','1890',
  'One of the earliest indoor shopping arcades in the United States, opened on May 30, 1890, at a cost of $867,000. John Eisenmann and George H. Smith designed it after the Galleria Vittorio Emanuele II in Milan, and John D. Rockefeller, Stephen V. Harkness, Marcus Hanna and Charles F. Brush were among those who paid for it. It became a National Historic Landmark in 1975, and in 2001 it was made into a Hyatt Regency hotel.',
  'Two nine-storey office buildings, one on Euclid Avenue and one on Superior Avenue, joined by a five-storey arcade of iron and glass with four tiers of balconies under a skylight of 1,800 panes, 100 feet up and over 300 feet long. The arched Superior Avenue entrance of Hummelstown brownstone is original; the Euclid Avenue front was remodelled in 1939. Because the two avenues are not parallel, the Euclid entrance turns at an angle into a rotunda. The hotel has the towers and the upper floors of the atrium; the two lower floors stay open to the public with shops and a food court.',
  'Cleveland\'s glass-roofed 1890 arcade, built with Rockefeller money.',
  'Privately owned; the hotel and shops are at 401 Euclid Avenue and 420 Superior Avenue. The lower two floors are open to the public; the Arcade\'s page gives no opening hours.'+DT,
  [W('Cleveland Arcade'),['The Arcade Cleveland','https://www.theclevelandarcade.com/']],
  brick='?',hours='?'),

N('cuyahoga-county-courthouse-cleveland','Cuyahoga County Courthouse','Cleveland','oh','civic','standing',41.5034,-81.697,'exact','view','walk','','1912',
  'The county\'s fifth courthouse, finished in 1912 by the firm of Lehman and Schmitt as part of the Cleveland Group Plan of 1903. It stands on Lakeside Avenue at the north end of the Mall and was listed on the National Register with the Mall district in 1975. The first courthouse, of 1813, was a small stone building; the later ones stood on Public Square.',
  'A Beaux-Arts building of pink Milford granite from Massachusetts, with a rusticated ground floor of deeply set arched windows and doors, three tall arched windows between Ionic columns over the main doors, and stone statues of lawgivers above the cornice. Inside are murals by Frank Brangwyn, Violet Oakley, Charles Yardley Turner, Max Bohm and Frederick Wilson. Whether visitors may see them outside court business was not checked.',
  '',
  'A working county courthouse, 1 West Lakeside Avenue. Seen from Lakeside Avenue and the Mall, which are open ground.'+DT,
  [W('Cuyahoga County Courthouse')],
  brick='no'),

N('garfield-memorial-cleveland','James A. Garfield Memorial','Cleveland','oh','burial','standing',41.51,-81.59139,'exact','open','drive','','1885–1890',
  'The tomb of President James A. Garfield, who was shot in Washington on July 2, 1881, and died on September 19, 1881. He had wished to be buried at Lake View Cemetery, and the highest point in the cemetery was chosen for him in 1883. Building began in October 1885 and the memorial was dedicated on May 30, 1890. Garfield, his wife Lucretia and two other members of the family lie in the crypt. It was listed on the National Register in 1973.',
  'A round tower 50 feet across and 180 feet high of Ohio sandstone on a broad stone terrace, in a mix of Byzantine, Gothic and Romanesque styles. Inside are stained glass windows for the 13 original states and Ohio, panels showing War and Peace, mosaics, deep red granite columns, and a white Carrara marble statue of Garfield 12 feet high by Alexander Doyle; the caskets are in the crypt below.',
  'A president\'s tomb built like a castle tower on the highest point of a Cleveland cemetery.',
  'Owned by Lake View Cemetery, 12316 Euclid Avenue; drive in through the cemetery gates and up to the memorial. The cemetery gates open every day, 7:30 a.m. to 5:30 p.m. from November to March and 7:30 a.m. to 7:30 p.m. from April to October; security may close them early at dusk or in bad weather. Groups of 12 or more book tours with the cemetery. Wikipedia says the memorial reopens each April.',
  [W('James A. Garfield Memorial'),['Lake View Cemetery: the Garfield Memorial','https://www.lakeviewcemetery.com/visit/james-a-garfield-memorial'],['Lake View Cemetery: hours','https://www.lakeviewcemetery.com/our-events-tours/hours-amp-map']],
  brick='no',hours='Memorial: daily 10 a.m. to 4 p.m. in season; closed for the winter from November 20, 2026; cemetery gates daily from 7:30 a.m.'),

N('rose-building-cleveland','Rose Building','Cleveland','oh','civic','standing',41.49926,-81.68651,'exact','view','walk','','1902',
  'A ten-storey office building of 1902 at Prospect Avenue and East Ninth Street, 165 feet tall and named for the Cleveland businessman and charity founder Benjamin Rose. When it was built it was the largest office building in Ohio, and it was thought too far from the business district to find tenants. Medical Mutual of Ohio had its home there from 1947 to 2023. It is a City of Cleveland landmark.',
  'Ornamental iron on the lower floors and richly decorated panels on the upper ones; the building follows the street lines on both fronts. Its floors are taller than ten floors would be now. Interior not checked.',
  '',
  'Privately owned, 2060 East Ninth Street, in the Gateway District; seen from the street.'+DT,
  [W('Rose Building (Cleveland)')],
  brick='no'),

N('severance-hall-cleveland','Severance Hall (Severance Music Center)','Cleveland','oh','civic','standing',41.50625,-81.60948,'exact','open','walk','','1931',
  'The concert hall of the Cleveland Orchestra, opened on February 5, 1931, and named for its patrons John L. Severance and his wife Elisabeth. Before it the orchestra played at Grays Armory and then the Masonic Auditorium, and twice had to move out for a poultry show. A two-year restoration and enlargement costing $36 million reopened it in January 2000 and won a National Preservation Honor Award. It is part of the Wade Park District on the National Register.',
  'A domed rotunda at the front opens into a fan-shaped auditorium behind. Inside, Art Deco mixes with Egyptian Revival: the Grand Foyer has marble columns and papyrus and lotus patterns, and the hall holds a restored Skinner organ of 6,025 pipes. Reinberger Chamber Hall, seating 402, is on the ground floor. The orchestra lists public tours of the building on its events pages.',
  '',
  'Owned by the Cleveland Orchestra, 11001 Euclid Avenue, University Circle. Doors open two hours before most performances, by the orchestra\'s guest-services page; free talks are held in Reinberger Chamber Hall an hour before most concerts.'+UC,
  [W('Severance Hall'),['Cleveland Orchestra: guest services','https://clevelandorchestra.com/help/guest-services']],
  brick='?',hours='Concerts on their own dates, doors two hours before; public tours on dates the orchestra lists'),

N('st-stanislaus-cleveland','Shrine Church of St. Stanislaus','Cleveland','oh','worship','standing',41.45907,-81.6445,'exact','open','drive','','1886–1891',
  'Often called the mother church of Cleveland\'s Polish Catholics, in the old Warszawa neighbourhood, now Slavic Village. The parish was organised in the 1870s; the present church was begun in August 1886, closed in the next year and dedicated on November 15, 1891. A tornado on April 21, 1909, brought down its twin spires; they were rebuilt within the year, lower than before (232 feet first, 122 feet now). After an interior renovation of $1.4 million it was rededicated as a shrine church. It is on the National Register, and the neighbourhood is a Register district.',
  'A large Gothic church, 85 by 200 feet, of locally made warm red brick and dressed stone, with twin towers at the front. The interior was renovated and has a pipe organ (not described further by the sources read). Mass is open to anyone.',
  'A Polish church whose spires were blown down by a tornado in 1909.',
  'An active parish of the Catholic Diocese of Cleveland, 3649 East 65th Street at Forman Avenue. Mass times are from the parish\'s own page as read in November 2026. Small parking lots are mapped on Baxter Avenue and Osmond Court nearby; whose they are was not checked.',
  [W('Shrine Church of St. Stanislaus'),['St. Stanislaus parish','https://www.ststanislaus.org/']],
  brick='yes',hours='Sunday Mass 8:30 a.m., 10 a.m. (Polish), 11:30 a.m.; Saturday vigil 5 p.m.; weekday Masses from 6:45 a.m.'),

N('trinity-cathedral-cleveland','Trinity Cathedral','Cleveland','oh','worship','standing',41.50149,-81.6742,'exact','open','walk','','1901–1907',
  'The cathedral of the Episcopal Diocese of Ohio, on Euclid Avenue at East 22nd Street. Trinity parish was founded in 1816 and built the first church inside the village of Cleveland in 1829, then a stone Gothic church on Superior Avenue in 1855. Charles F. Schweinfurth designed the present cathedral; the congregation turned down his first, Romanesque plan for a Gothic one. Building began in 1901 and it was consecrated on September 24, 1907. It was listed on the National Register in 1973.',
  'A Gothic cathedral. Trinity Commons, finished in 2002, adds a piazza that is now the entry, with a gallery, coffee shop and restaurant. The cathedral\'s page speaks of its choirs and pipe organs; the rest of the interior was not checked.',
  '',
  'An active cathedral, 2230 Euclid Avenue. Service times are from the cathedral\'s calendar as read in November 2026.'+DT,
  [W('Trinity Cathedral (Cleveland)'),['Trinity Cathedral: services calendar','https://trinitycleveland.org/events/category/worship/services/']],
  brick='no',hours='Sundays: early Eucharist in the chapel, Holy Eucharist 9 a.m. (fall to spring), choral service; Thursday Healing Eucharist; Evensong 1st, 3rd and 5th Wednesdays'),

N('west-side-market-cleveland','West Side Market','Cleveland','oh','civic','standing',41.48465,-81.70304,'exact','open','walk','','1912',
  'Cleveland\'s oldest working public market. An open-air market began on land given by Josiah Barber and Richard Lord in 1840, across the street from the present one, and a wooden market house, the Pearl Street Market, followed in 1868. Hubbell and Benes designed the present building, finished in 1912 for nearly $680,000. It was listed on the National Register in 1973. The city still owns it and in April 2024 handed its running to the non-profit Cleveland Public Market Corporation.',
  'A Neoclassical and Byzantine brick hall with a large clock tower, at West 25th Street and Lorain Avenue in Ohio City. Inside, a big concourse holds nearly 100 stalls; an outdoor produce arcade of 85 stalls wraps round the side and back, enclosed and heated since 2004.',
  'A 1912 market hall with a clock tower, still full of stalls.',
  'Owned by the City of Cleveland, 1979 West 25th Street. Hours from the market\'s own page as read in November 2026. Several parking lots are mapped nearby; their fees were not checked.',
  [W('West Side Market'),['West Side Market: hours','https://westsidemarket.org/hours/']],
  brick='some',hours='Monday, Wednesday, Friday, Saturday 8 a.m. to 5 p.m.; Sunday 10 a.m. to 4 p.m.; closed Tuesday and Thursday'),

N('cleveland-city-hall','Cleveland City Hall','Cleveland','oh','civic','standing',41.50504,-81.69364,'exact','view','walk','','1912–1916',
  'The seat of Cleveland\'s government, the mayor\'s office and the city council, opened in 1916 at 601 Lakeside Avenue. J. Milton Dyer designed it to carry on Daniel Burnham\'s Group Plan of 1903; the design was ready by 1907, building began in 1912, and it cost $3 million. It stands on the bluff above North Coast Harbor and is a city landmark.',
  'A Neoclassical front, little changed outside since 1916. Its rotunda has held weddings, rallies and galas, and Representative Louis Stokes lay in state there in 2015. Visiting hours not checked.',
  '',
  'Owned by the City of Cleveland; seen from Lakeside Avenue, Willard Park and the Mall.'+DT,
  [W('Cleveland City Hall')],
  brick='?'),

N('cleveland-masonic-temple','Cleveland Masonic Temple (Masonic Auditorium)','Cleveland','oh','civic','standing',41.50365,-81.66245,'exact','view','walk','','1921',
  'An auditorium and banquet hall opened in 1921, designed by Hubbell and Benes. The Cleveland Orchestra played here through the 1920s before Severance Hall was built. It was listed on the National Register in 2001 and still holds concerts and wrestling shows.',
  'The main auditorium seats 2,200, and the building has two large organs, an Austin and a Wurlitzer, as well as a banquet hall and lounge. Inside only for events.',
  '',
  'Privately owned, 3615 Euclid Avenue; seen from the street, and open inside only to ticket holders on event dates.',
  [W('Cleveland Masonic Temple')],
  brick='?'),

N('cleveland-public-library-main','Cleveland Public Library, Main Library','Cleveland','oh','civic','standing',41.5011,-81.6917,'exact','open','walk','','1923–1925',
  'The main building of a library founded in 1869. Walker and Weeks won the competition for it in 1916; building, held up by the First World War, began in 1923, and it opened on May 6, 1925, for just under $5 million. It was renovated from 1997 to 1999, when a new wing of glass and Georgia marble opened beside it, joined by a tunnel under the Eastman Reading Garden.',
  'A classical building of five storeys, each as tall as two in most buildings. Inside are a pearl-grey art glass globe of 1925 hanging in the entrance hall, and in Brett Hall murals from 1934 (among them Ora Coltman\'s Dominance of the City, restored) with later ones. The Eastman Reading Garden between the two buildings has sculptures by Maya Lin and Tom Otterness. Free tours.',
  '',
  'Run by Cleveland Public Library, 325 Superior Avenue. Hours and tours from the library\'s page as read in November 2026. On-street meters on East Sixth Street between St. Clair and Superior, and paid garages nearby.',
  [W('Cleveland Public Library'),['Cleveland Public Library: Main Library','https://cpl.org/locations/main-library/']],
  brick='no',hours='Monday to Saturday 10 a.m. to 6 p.m.; free tours Monday to Friday 10 a.m. to 5:30 p.m., subject to staff'),

N('cleveland-museum-of-art','Cleveland Museum of Art','Cleveland','oh','civic','standing',41.5086,-81.61161,'exact','open','walk','','1913–1916',
  'An art museum founded as a trust in 1913 with money from the industrialists Hinman Hurlbut, John Huntington and Horace Kelley, and opened on June 6, 1916. Hubbell and Benes designed the building as the centrepiece of Wade Park, land that Jeptha H. Wade gave the city in 1881; the park, with the museum in it, is on the National Register. It holds more than 61,000 works.',
  'A Beaux-Arts building of white Georgian marble on the south edge of Wade Park, facing the lagoon. General admission to the permanent collection is free; some exhibitions are ticketed.',
  '',
  'Run by the museum, 11150 East Boulevard. Hours from its own page as read in November 2026; it has its own parking garage off Jeptha Drive.',
  [W('Cleveland Museum of Art'),['Cleveland Museum of Art: visit','https://www.clevelandart.org/visit']],
  brick='no',hours='Tuesday, Thursday, Saturday, Sunday 10 a.m. to 5 p.m.; Wednesday and Friday 10 a.m. to 9 p.m.; closed Monday',
  th=[41.50979,-81.61289],thn='Cleveland Museum of Art garage, Jeptha Drive'),

N('tiffany-glass-building-cleveland','Tiffany Glass Building (Citizens Building)','Cleveland','oh','civic','standing',41.50002,-81.68699,'exact','view','walk','','1903',
  'Built in 1903 by the Citizens Savings and Trust bank on the site of Cleveland\'s first high school building, and designed by Hubbell and Benes. It opened to the public on September 28, 1903. Its granite portico was taken off in 1924 and a two-storey addition built in its place. The City Club of Cleveland has been there since 1982; the building was renamed the City Club Building in 1999 and the Tiffany Glass Building in 2024.',
  'An office tower whose first two floors are faced with Barre granite and whose upper floors are brick with ivory glazed terra cotta round the windows. The bank\'s lobby was lit by a barrel vault of leaded glass and lined with Italian marble, with work by the muralists Edwin Blashfield and Kenyon Cox and by Tiffany and Co.; how much of that survives was not checked.',
  '',
  'Privately owned, 850 Euclid Avenue; seen from the street.'+DT,
  [W('Tiffany Glass Building')],
  brick='?'),

N('hotel-cleveland','Hotel Cleveland','Cleveland','oh','hotel','standing',41.49879,-81.69481,'exact','open','walk','','1918',
  'A 1,000-room hotel on Public Square that opened on December 16, 1918, on a site used for lodging since Mowrey\'s Tavern of 1815; the Forest City House before it was pulled down in 1916. The Van Sweringen brothers bought it in the 1920s and built the Cleveland Union Terminal round it. It was later a Sheraton, a Stouffer\'s and from 1996 the Renaissance Cleveland, and took back its first name in spring 2024 after a $90 million renovation, reopening that June. It is on the National Register as part of the Terminal group.',
  'A large hotel on the west side of Public Square, joined to Tower City Center. Its rear courtyard was roofed in glass as an atrium in the late 1970s. The famous Bronze Room restaurant has closed and is offices.',
  '',
  'A working hotel, 24 Public Square; its lobby is for guests and visitors.'+DT,
  [W('Hotel Cleveland')],
  brick='?',hours='?'),
]

PIN_NOTES={
'soldiers-sailors-monument-cleveland':'Moved about 60 m east from the Wikipedia point, which fell on the roadway, onto the monument seen on the aerial in the southeast quarter of Public Square.',
'cleveland-arcade':'Address point for 401 Euclid Avenue, on the Arcade.',
'cuyahoga-county-courthouse-cleveland':'Address point for 1 West Lakeside Avenue, on the courthouse.',
'garfield-memorial-cleveland':'The Wikipedia point, on the memorial in Lake View Cemetery.',
'rose-building-cleveland':'Address point for 2060 East Ninth Street.',
'severance-hall-cleveland':'Address point for 11001 Euclid Avenue, on the hall.',
'st-stanislaus-cleveland':'Address point for 3649 East 65th Street, on the church.',
'trinity-cathedral-cleveland':'Address point for 2230 Euclid Avenue.',
'west-side-market-cleveland':'Address point for 1979 West 25th Street, on the market hall.',
'cleveland-city-hall':'Address point for 601 Lakeside Avenue.',
'cleveland-masonic-temple':'Address point for 3615 Euclid Avenue.',
'cleveland-public-library-main':'Address point for 325 Superior Avenue.',
'cleveland-museum-of-art':'Address point for 11150 East Boulevard, on the museum.',
'tiffany-glass-building-cleveland':'Address point for 850 Euclid Avenue.',
'hotel-cleveland':'Address point for 24 Public Square, on the hotel.',
}
