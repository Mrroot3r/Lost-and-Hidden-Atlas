# November 23, 2026: Providence, Rhode Island, the standing buildings named in one walk-through video of old Providence
# photographs, each checked in sources opened for this batch. The video is only the tip: no fact below comes from it.
# Facts come from Wikipedia read as raw text (the articles linked on each place) and the National Register list for
# Providence. Hours and service times come from the owners' own pages read on November 23, 2026: the Providence Athenaeum,
# First Baptist Church in America, Beneficent Church, Central Congregational Church (centralchurch.us), the Cathedral's
# parish page (providencecathedral.org) and the City of Providence. The Providence Public Library, Trinity Rep and the
# Providence Performing Arts Center pages could not be opened (HTTP 403 or 404); their hours are left unrecorded.
# Pins: street addresses through the ArcGIS geocoder (PointAddress matches), or the Wikipedia point where no address was
# sourced; every pin was looked at on the aerial.
# Brick values only where a source names the material: the Arcade (granite, brick and cast iron: some), Beneficent
# (a brick church: yes), the Market House (brick: yes), the County Courthouse (red brick with granite and limestone trim:
# yes), the John Hay Library (white marble with a 1939 red brick wing: some), Union Station (yellow brick: no), the
# Old Stone Bank (granite: no), the Joseph Brown House (brick on a brownstone base: yes), City Hall (granite-faced: no),
# the Federal Building (granite: no). From a picture on Wikimedia Commons, 'Trinity Reperatory Company theatre, Providence,
# Rhode Island.jpg': a white front, no red brick: no. The rest are '?'.
from data_b import N
from data_ma import W

BATCH={'key':'prov_qfjt','label':'Providence, Rhode Island','added':'2026-11-23 10:32'}

DT='Downtown Providence: street parking and public garages nearby; no lot for this building was checked.'
CH='College Hill, Providence: street parking on the hill; no lot for this building was checked.'

PLACES=[
N('westminster-arcade-providence','The Arcade (Westminster Arcade)','Providence','riprov','civic','standing',41.82416,-71.41073,'exact','open','walk','','1828',
  'Built in 1828 for Cyrus Butler to designs by Russell Warren and Tallman & Bucklin, the Arcade is counted as the first enclosed shopping mall in the United States: three levels of shops along a skylit lane running through the block from Westminster Street to Weybosset Street. It declined in the late 20th century and was closed for rebuilding more than once; it reopened in October 2013 with small apartments upstairs and shops and food on the ground floor. It was made a National Historic Landmark in 1976.',
  'Greek Revival columned fronts on both streets, and inside the long skylit lane with cast-iron railings capped in mahogany along the upper floors. Granite, brick and cast iron were used throughout to resist fire.',
  'America\'s first shopping mall, 1828, still selling things under its skylights.',
  accn='Privately owned, with shops and restaurants on the ground floor and apartments above. Entrances on Westminster Street and Weybosset Street. Its own website no longer answers; opening hours not checked, and each shop keeps its own. '+DT,
  links=[W('Westminster Arcade')],brick='some',hours='?'),

N('providence-athenaeum','Providence Athenaeum','Providence','riprov','civic','standing',41.82580,-71.40631,'exact','open','walk','','1838',
  'A member-supported subscription library whose roots go back to the Providence Library Company of 1753; the present name dates from a merger in 1836. Its Greek Revival building on Benefit Street was finished in 1838 to designs by the Philadelphia architect William Strickland. The building is open to the public, though only members may borrow.',
  'The temple front on Benefit Street and the old reading rooms inside. Its rare book room holds books from the colonial library.',
  'A 1838 library temple that still lends books to its members.',
  accn='Run by the Providence Athenaeum, 251 Benefit Street. Open to the public; borrowing is for members. Hours from the Athenaeum\'s visit page, November 2026; it closes on some holidays and for private events. '+CH,
  links=[W('Providence Athenaeum'),['Providence Athenaeum: visit','https://www.providenceathenaeum.org/visit/']],brick='?',hours='Tuesday to Saturday 10 a.m. to 6 p.m., Sunday 11 a.m. to 5 p.m.; closed Monday'),

N('old-stone-bank-providence','Old Stone Bank (Providence Institution for Savings)','Providence','riprov','civic','standing',41.82465,-71.40677,'exact','view','walk','','1854',
  'The granite bank with the gilded dome on South Main Street was designed by C. J. and R. J. Hall in 1854 for the Providence Institution for Savings, the savings bank founded in 1819 that later called itself the Old Stone Bank. The bank failed and was seized in 1993. Brown University bought the building in 1995 for its anthropology museum but gave that up, sold it in 2009, and it was turned into a single-family house between 2015 and 2017.',
  'The granite front and the gold-leafed dome, seen from South Main Street. It is a private house: interior not open.',
  'A domed granite bank that became somebody\'s house.',
  accn='Private residence on South Main Street. View from the public sidewalk only. '+CH,
  links=[W('Old Stone Bank')],brick='no'),

N('joseph-brown-house-providence','Joseph Brown House (Old Providence Bank)','Providence','riprov','landmark','standing',41.82480,-71.40694,'exact','view','walk','','1774',
  'The house Joseph Brown designed for himself at 50 South Main Street, finished about 1774, is said to be the oldest surviving house built by an American architect for his own use. In 1801 the Providence Bank, founded by his brothers John and Moses, bought it for its office and stayed until 1929. Its curved, scroll-ended front gable is rare even among English houses of the period.',
  'The ogee-curved gable with its white balustrade, the five-bay brick front on a brownstone base, and the entrance now at street level where once it stood up a double stair. It stands right beside the Old Stone Bank.',
  'Providence\'s first bank worked out of an architect\'s own house for 128 years.',
  accn='Privately owned (an office building). View from South Main Street. '+CH,
  links=[W('Joseph Brown House (Providence, Rhode Island)')],brick='yes'),

N('market-house-providence','Market House','Providence','riprov','civic','standing',41.82581,-71.40833,'exact','view','walk','','1773–1775',
  'A brick market house built 1773 to 1775 to designs by Joseph Brown with Stephen Hopkins: a market on the ground floor and a meeting room above. A third floor added in 1797 held the first Masonic lodge in Rhode Island, and the city council met here before City Hall was built. On March 2, 1775, townspeople burned British tea in the square outside. It was later given to the Rhode Island School of Design, on condition that the outside be kept.',
  'The three-storey brick front on Market Square, with a bull\'s-eye window in the east gable and a clock in the west. It belongs to the Rhode Island School of Design: interior not checked.',
  'Where Providence burned its tea in 1775.',
  accn='Owned by the Rhode Island School of Design. View from Market Square and South Main Street. '+CH,
  links=[W('Market House (Providence, Rhode Island)')],brick='yes'),

N('first-baptist-meeting-house-providence','First Baptist Meeting House','Providence','riprov','worship','standing',41.82745,-71.40832,'exact','open','walk','','1774–1775',
  'The church Roger Williams gathered in 1638 is the oldest Baptist church in the Americas. Its present meeting house, designed by Joseph Brown after plates in James Gibbs\'s 1728 book, was put up in 1774 and 1775; the steeple, after one of Gibbs\'s unbuilt designs for St Martin-in-the-Fields, went up in three and a half days in June 1775. Brown University still holds its commencement here. A restoration paid for by John D. Rockefeller Jr. took out Victorian additions. It became a National Historic Landmark in 1960.',
  'The tall white steeple over North Main Street and the light, galleried meeting room inside. The church\'s page offers tours and a gift shop but gives no tour times.',
  'Roger Williams\'s church, under a steeple built in three and a half days.',
  accn='An active American Baptist church at 75 North Main Street. Sunday worship from the church\'s own page, November 2026; for tours ask the church office by telephone. '+CH,
  links=[W('First Baptist Church in America'),['First Baptist Church in America','https://www.firstbaptistchurchinamerica.org/']],brick='?',hours='Sunday worship 11 a.m. (Christian education 10 a.m.)'),

N('beneficent-congregational-church-providence','Beneficent Congregational Church ("Round Top")','Providence','riprov','worship','standing',41.82025,-71.41375,'exact','open','walk','','1809',
  'The congregation began in 1743 in the Great Awakening and built its first meeting house on this Weybosset Street site. The present brick church went up in 1809 to plans by Barnard Eddy and John Newman and was remodelled in the Greek Revival style in 1836 by James C. Bucklin, who added the Doric columns. The textile man Henry J. Steere paid for the work and gave a chandelier of 5,673 pieces of Austrian crystal. Until about 2007 its dome was gilded.',
  'The dome over Weybosset Street and the Doric portico. Wikipedia names the crystal chandelier inside; interior not otherwise checked.',
  'An 1809 domed meeting house downtown, crystal chandelier and all.',
  accn='An active United Church of Christ congregation, 300 Weybosset Street. Worship time from the church\'s own page, November 2026. '+DT,
  links=[W('Beneficent Congregational Church'),['Beneficent Church','https://www.beneficentchurch.org/']],brick='yes',hours='Sunday worship 10 a.m.'),

N('central-congregational-church-providence','Central Congregational Church','Providence','riprov','worship','standing',41.82887,-71.39601,'exact','open','walk','','1891–1893',
  'The congregation formed in 1852 and first worshipped in a brownstone church on Benefit Street. Its present church at 296 Angell Street was designed by Carrère and Hastings of New York; the cornerstone went down in July 1891 and the church was dedicated in November 1893. It stands in the Stimson Avenue Historic District.',
  'The church on Angell Street; inside, oak woodwork, with the decoration gathered round the pulpit and chancel.',
  'Carrère and Hastings, the Fifth Avenue library architects, built this East Side church.',
  accn='An active United Church of Christ congregation, 296 Angell Street. Worship time from the church\'s own page, November 2026. Street parking on the East Side; no lot was checked.',
  links=[W('Central Congregational Church (Providence, Rhode Island)'),['Central Congregational Church','https://centralchurch.us/']],brick='?',hours='Sunday worship 10:30 a.m.'),

N('cathedral-saints-peter-paul-providence','Cathedral of Saints Peter and Paul','Providence','riprov','worship','standing',41.81890,-71.41637,'exact','open','walk','','1878–1889',
  'The mother church of the Catholic Diocese of Providence, a Romanesque Revival cathedral designed by Patrick Keely in 1873 to replace an older, smaller cathedral on the site. Its cornerstone was laid in 1878 and it was consecrated on June 30, 1889. It was listed on the National Register in 1975. A later restoration repaired the sandstone facing and lengthened the sanctuary.',
  'Inside, Munich-style stained glass with two rose windows and a great circular window, green marble columns along the nave, a carved and painted vaulted ceiling, oak pews, and Bishop Hendricken\'s granite sarcophagus in the west transept.',
  'Munich glass and green Alpine marble in a Keely cathedral.',
  accn='An active Catholic cathedral at 30 Fenner Street, Cathedral Square. Mass times from the cathedral\'s own page, November 2026; visiting hours outside Mass not given there. '+DT,
  links=[W('Cathedral of Saints Peter and Paul (Providence, Rhode Island)'),['Cathedral: Mass times','https://www.providencecathedral.org/mass-times']],brick='?',hours='Mass Monday to Friday 12 noon; Saturday 5 p.m.; Sunday 10 a.m., 1 p.m. and 6 p.m.'),

N('providence-city-hall','Providence City Hall','Providence','riprov','civic','standing',41.82414,-71.41291,'exact','open','walk','','1875–1878',
  'After some thirty years of argument over whether it should stand east or west of the river, the city built its hall at the end of what is now Kennedy Plaza between 1875 and 1878, to a Second Empire design by Samuel J. F. Thayer. Before then the city government met in the Market House. Talk of demolition in the 1970s led to a full restoration, finished in the 1990s.',
  'An iron and brick building faced in Westerly and New Hampshire granite, with a mansard roof; inside, a tall central atrium and the council chamber. Open on weekdays as the seat of city government.',
  'A Second Empire city hall that was nearly pulled down in the 1970s.',
  accn='City of Providence, 25 Dorrance Street. Office hours from the city\'s own website, November 2026; some departments stay open later on set evenings. '+DT,
  links=[W('Providence City Hall'),['City of Providence: contact','https://providenceri.gov/contact/']],brick='no',hours='Monday to Friday 8:30 a.m. to 4:30 p.m. (to 4 p.m. in July and August)'),

N('providence-county-courthouse','Providence County Courthouse (Licht Judicial Complex)','Providence','riprov','civic','standing',41.82566,-71.40683,'site','view','walk','','1924–1933',
  'This lot has served government since the 18th century: a 1723 meeting house used as the town house, then a High Victorian Gothic courthouse of 1875 to 1877. That was replaced between 1924 and 1933 by the present Georgian Revival courthouse by Jackson, Robertson & Adams, which holds the Rhode Island Supreme Court and the county Superior Court. At 216 feet it is one of the tallest buildings in the city.',
  'A red brick building with granite and limestone trim climbing the hill from South Main Street to Benefit Street, with a tall spire. A working courthouse: interior not checked.',
  'A brick Georgian courthouse with a steeple, on a lot used for government since the 1700s.',
  accn='State of Rhode Island courts, between South Main and Benefit Streets. A working courthouse with security screening; view from the street. '+CH,
  links=[W('Providence County Courthouse')],brick='yes'),

N('john-hay-library-providence','John Hay Library, Brown University','Providence','riprov','civic','standing',41.82639,-71.40491,'exact','open','walk','','1910',
  'Brown University\'s main library from 1910, paid for in part by Andrew Carnegie and named at his request for John Hay, class of 1858. Shepley, Rutan and Coolidge designed it in the Beaux-Arts style, in white Vermont marble from Dorset; a Georgian red brick wing followed in 1939. It now holds the university\'s rare books, manuscripts and archives.',
  'The white marble front on Prospect Street, opposite the Van Wickle Gates, and the brick 1939 wing behind. The library says its first floor and exhibits are open to the public; the special collections reading room is by appointment.',
  'Carnegie\'s marble library for Brown, now its rare book house.',
  accn='Brown University, 20 Prospect Street. Open to the public for exhibits; an exterior renovation from June 2026 has limited reading room hours. Current hours not read: see the library\'s page. '+CH,
  links=[W('John Hay Library'),['Brown University Library: John Hay Library','https://library.brown.edu/hay/']],brick='some',hours='?'),

N('providence-public-library-washington-street','Providence Public Library (central library)','Providence','riprov','civic','standing',41.82203,-71.41688,'site','open','walk','','1896–1900',
  'The library founded in 1875 first opened in 1878 on the second floor of the Butler Exchange. Its central building on Washington Street went up from 1896 and opened in March 1900 in a Renaissance style, paid for largely by John Nicholas Brown I, who died six weeks after it opened. A large addition on Empire Street came in 1954 and was renovated from 2019. It is governed by a board of trustees and privately funded, but serves the public.',
  'The 1900 front on Washington Street; the way in is now through the 1954 building on Empire Street.',
  'A Renaissance palace of books given by a Brown.',
  accn='Providence Public Library, entrance at 150 Empire Street. Its own hours page could not be opened when this was written (HTTP 403). '+DT,
  links=[W('Providence Public Library'),['Providence Public Library','https://provlib.org/']],brick='?',hours='?'),

N('masonic-temple-providence','Masonic Temple (Renaissance Providence Hotel)','Providence','riprov','hotel','standing',41.83006,-71.41664,'exact','open','walk','','1927–1929',
  'Begun in 1927 as a meeting hall for the Freemasons on Francis Street, opposite the State House, the Greek Revival building was halted by the crash of 1929 and given up for good with the Second World War. It stood unfinished and empty for decades. It was listed on the National Register in 1993 with the Veterans Memorial Auditorium next door, which was part of the same complex, and opened as a hotel in June 2007.',
  'The columned front on Francis Street facing the State House. It is a working hotel: interior not checked.',
  'A Masonic temple left unfinished for over 70 years, then made a hotel.',
  accn='Privately owned hotel on Francis Street. Hotel guests and diners go in; others view from the street. '+DT,
  links=[W('Renaissance Providence Hotel')],brick='?',hours='?'),

N('providence-biltmore','Providence Biltmore (Graduate Providence)','Providence','riprov','hotel','standing',41.82435,-71.41330,'exact','open','walk','','1922',
  'The hotel at 11 Dorrance Street, on the southern corner of Kennedy Plaza, opened on June 6, 1922 as the Providence Biltmore of the Bowman-Biltmore chain, designed by Warren and Wetmore, the Grand Central Terminal architects, and paid for by a public campaign of 1,800 citizens. It passed through Sheraton, Dunfey and Omni ownership, stood empty for four years, and was sold in 2017; it now runs as the Graduate by Hilton.',
  'The tall neo-Federal hotel beside City Hall. A working hotel: interior not checked.',
  'A 1922 hotel built with 1,800 citizens\' money.',
  accn='Privately owned hotel, 11 Dorrance Street. Guests and diners go in. '+DT,
  links=[W('Providence Biltmore')],brick='?',hours='?'),

N('federal-building-providence','Federal Building (post office and courthouse)','Providence','riprov','civic','standing',41.82589,-71.41046,'exact','view','walk','','1903–1908',
  'Congress gave $1 million in 1902 for a post office, courthouse and custom house; the city gave the site at the east end of Exchange Place, and the local firm of Clarke & Howe won the design competition in 1903. The building was finished in 1908: five storeys of New Hampshire granite over a steel frame around a central courtyard. It still houses the federal District Court for Rhode Island.',
  'The granite front on Kennedy Plaza with its twice life-size marble statue groups. Wikipedia describes an oak-panelled courtroom under a stained-glass skylight. A working federal courthouse with security: interior not checked.',
  'A 1908 granite post office and courthouse on Kennedy Plaza.',
  accn='United States courts, Kennedy Plaza. View from the plaza. '+DT,
  links=[W('Federal Building (Providence, Rhode Island)')],brick='no'),

N('loews-state-theatre-providence','Loew\'s State Theatre (Providence Performing Arts Center)','Providence','riprov','civic','standing',41.82126,-71.41202,'exact','open','walk','','1928',
  'Built in 1928 as a Loew\'s movie palace by Rapp & Rapp, the leading designers of such theatres. Over 14,000 people came on opening day to see the chandeliers, marble columns and mouldings. From 1950 it put on live concerts, and from 1972 to 1975 it was the Palace Concert Theater for rock shows. It was nearly torn down in 1977, reopened in October 1978, and is now the Providence Performing Arts Center, with 3,100 seats for touring shows and concerts.',
  'The marquee on Weybosset Street; inside, chandeliers, marble columns and moulded plaster, seen on a show night.',
  'A 1928 movie palace where 14,000 came on opening day just to look.',
  accn='Providence Performing Arts Center, a not-for-profit, 220 Weybosset Street. Open for performances; box office hours could not be read when this was written. '+DT,
  links=[W('Providence Performing Arts Center')],brick='?',hours='?'),

N('majestic-theatre-trinity-rep-providence','Majestic Theatre (Trinity Rep, Lederer Theater Center)','Providence','riprov','civic','standing',41.82221,-71.41635,'exact','open','walk','','1917',
  'Built in 1917 as the Emery Majestic Theatre, a vaudeville house, the building has been the home of Trinity Repertory Company since 1973. Inside are now two stages, the 500-seat Chace Theater and the 300-seat Dowling Theater, with offices, shops and rehearsal halls.',
  'The old theatre front at 201 Washington Street; inside on a show night. Interior not otherwise checked.',
  'A 1917 vaudeville house reborn as a repertory theatre.',
  accn='Trinity Repertory Company, a non-profit, 201 Washington Street. Open for performances; the company\'s own page could not be opened when this was written. '+DT,
  links=[W('Trinity Repertory Company')],brick='no',hours='?'),

N('turks-head-building-providence','Turk\'s Head Building','Providence','riprov','civic','standing',41.82456,-71.40986,'exact','view','walk','','1913',
  'A 16-storey, 215-foot office tower finished in 1913, the tallest in downtown Providence until the Biltmore of 1922. It is wedge-shaped on its corner, after the Flatiron Building in New York. The name goes back to a ship\'s figurehead of a Turk\'s head that a shopkeeper, Jacob Whitman, set over his store here in the early 19th century; the figurehead was lost in a storm.',
  'The narrow curved prow of the building, and a stone copy of the Turk\'s head on the third-floor front.',
  'Look for the stone Turk on the third floor.',
  accn='Privately owned office building at the corner of Westminster and Weybosset Streets. View from the street. '+DT,
  links=[W('Turk\'s Head Building')],brick='?'),

N('union-station-providence-1898','Union Station (1898)','Providence','riprov','rail','standing',41.82560,-71.41404,'site','open','walk','stations','1898–1986',
  'The second Union Station opened in 1898, a row of yellow brick buildings by Stone, Carpenter & Willson along Exchange Terrace, replacing the 1848 station that a fire gutted in 1896. Trains left it in 1986 for the new Providence station half a mile north, and a fire in April 1987, during renovation, changed the plans for it. Parts now hold offices, restaurants and the Rhode Island Foundation; a food hall, Track 15, opened in March 2025.',
  'The long yellow brick front facing Kennedy Plaza, where the tracks once ran behind. The food hall inside is open to the public.',
  'Providence\'s old station, now a food hall named for the track that never was.',
  accn='Privately owned; Track 15 food hall and restaurants inside. Exchange Terrace, beside Kennedy Plaza. Hours not checked. '+DT,
  links=[W('Union Station (Providence)')],brick='no',hours='?'),
]

PIN_NOTES={
 'westminster-arcade-providence':'Address lookup for 130 Westminster Street; on the aerial it falls on the long Arcade roof between Westminster and Weybosset Streets.',
 'providence-athenaeum':'Address lookup for 251 Benefit Street; on the aerial it falls on the Athenaeum building.',
 'old-stone-bank-providence':'Address lookup for 86 South Main Street; on the aerial it falls on the domed bank.',
 'joseph-brown-house-providence':'Address lookup for 50 South Main Street, beside the Old Stone Bank; checked on the aerial.',
 'market-house-providence':'Wikipedia point; on the aerial it falls on the Market House at Market Square.',
 'first-baptist-meeting-house-providence':'Address lookup for 75 North Main Street; on the aerial it falls on the meeting house.',
 'beneficent-congregational-church-providence':'Address lookup for 300 Weybosset Street; on the aerial it falls on the domed church.',
 'central-congregational-church-providence':'Address lookup for 296 Angell Street; on the aerial it falls on the church.',
 'cathedral-saints-peter-paul-providence':'Address lookup for 30 Fenner Street; on the aerial it falls on the cathedral.',
 'providence-city-hall':'Address lookup for 25 Dorrance Street; on the aerial it falls on City Hall.',
 'providence-county-courthouse':'Address lookup for 250 Benefit Street; the pin marks the courthouse site.',
 'john-hay-library-providence':'Address lookup for 20 Prospect Street; on the aerial it falls on the library.',
 'providence-public-library-washington-street':'Wikipedia point for the central library; the pin marks the library block.',
 'masonic-temple-providence':'Address lookup on Avenue of the Arts beside Francis Street, agreeing with the Wikipedia point; checked on the aerial.',
 'providence-biltmore':'Address lookup for 11 Dorrance Street; on the aerial it falls on the hotel tower.',
 'federal-building-providence':'The Wikipedia point fell on Kennedy Plaza beside it; moved about 54 m east onto the courtyard building seen on the aerial, which OpenStreetMap names the United States Federal Building and Courthouse.',
 'loews-state-theatre-providence':'Address lookup for 220 Weybosset Street; on the aerial it falls on the theatre.',
 'majestic-theatre-trinity-rep-providence':'Address lookup for 201 Washington Street; on the aerial it falls on the theatre.',
 'turks-head-building-providence':'Wikipedia point; on the aerial it falls on the wedge-shaped tower.',
 'union-station-providence-1898':'Address lookup on Exchange Terrace, close to the Register point; the pin marks the station row.',
}
