# November 24, 2026: Superior, Wisconsin. Twelve standing buildings in the city, taken as leads from the names in one
# walk-through video and the boom-period business blocks round them, each then checked in sources opened for this
# batch: the National Register forms read as text from NPGallery (the 1983 New Jersey Building form, the 1985 survey
# forms for the "Speculative Commercial Blocks of Superior's Boom Period", the 1979 Trade and Commerce form and the 1981
# Martin Pattison House form), the Wisconsin Historical Society's Architecture and History Inventory records (later
# surveys, demolitions), the Douglas County Historical Society's school pages, Wikipedia read as raw text, the Library
# History Buff page that quotes a 1999 state survey of the Carnegie library, WPR and B105 news. Nothing in an entry
# comes from the video.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]

BATCH={'key':'superior_pnqa','label':'Superior, Wisconsin: boom-era blocks, library and mansion','added':'2026-11-24 18:33'}

DC_NR=W('National Register of Historic Places listings in Douglas County, Wisconsin')
def AHI(n,label): return L('Wisconsin Historical Society property record: '+label,'https://www.wisconsinhistory.org/Records/Property/HI'+n)
def NRF(n,label): return L('National Register form: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'+n+'_text')
MPS=NRF('64500723',"Speculative Commercial Blocks of Superior's Boom Period")
DOWNTOWN="On Tower Avenue in downtown Superior, a public street; street parking along Tower Avenue and the side streets."

PLACES=[
N('new-jersey-building-superior','New Jersey Building','Superior','wi','civic','standing',46.72093,-92.10354,'exact','view','walk','','1889',
  "A two-storey shop and apartment block at the corner of Tower Avenue and Belknap Street, finished in 1889 by the Land and River Improvement Company, the New York firm that paid for much of Superior's boom; it was named for the company's New Jersey charter. Its 1983 Register form calls it the best surviving Victorian Romanesque brownstone commercial block in the city. The Grand Opera House and the West Superior Hotel once stood beside it and are gone.",
  look="Smooth red brick upper storey over a ground floor of rough-cut brownstone, with brownstone string courses, arches over the upstairs windows filled with herringbone brickwork, a corbel table under the coping and a square corner projection. The arched brownstone doorway in the middle of the Belknap side, with carved leaf capitals, survives; most shop fronts were altered (the 1983 form; a 2012 state survey found they had not been restored). The upstairs are apartments. Interior not checked.",
  accn=DOWNTOWN+" Shops on the ground floor and private apartments above: look from the street.",
  links=[NRF('83003373','New Jersey Building'),AHI('17857','New Jersey Block'),DC_NR],brick='yes',hours=''),
N('new-york-block-superior','New York Block','Superior','wi','civic','standing',46.72188,-92.10374,'exact','view','walk','','1889–1890',
  "A three-storey shop and flat block on the southeast corner of Tower Avenue and 14th Street, built in 1889 and 1890 by the Land and River Improvement Company and named for its New York backers; it held ten stores and twenty flats, and for a time the company's own offices. A fire in 1956 badly damaged the south end, and about 100 feet of the building were taken down.",
  look="Red pressed brick front in a long arcade of tall brick arches over the second and third storeys, with red sandstone capitals and basket-weave brickwork over the middle; the 14th Street side keeps more of the original redstone base. A 2009 state survey said the surviving part had been restored, with apartments upstairs and the shop fronts redone. Interior not checked.",
  accn=DOWNTOWN+" Shops below and private apartments above: look from the street.",
  links=[NRF('85001472','New York Block'),AHI('17853','New York Block'),MPS,DC_NR],brick='yes',hours=''),
N('empire-block-superior','Empire Block','Superior','wi','civic','standing',46.72408,-92.10355,'exact','view','walk','','1892',
  "A three-storey business block at Tower Avenue and 12th Street, built in 1892 for about $50,000 by the Empire Building Company, a land and investment firm formed by Franklin Billings, a former governor of Vermont, with New York and Superior partners. Carl Wirth of Superior designed it. Early tenants included a grocery, a drug store and the Pease hardware business; Wikipedia says a furniture store was there for about seventy years.",
  look="Pairs of upper windows under massive rough-cut sandstone lintels, set in two-storey bays between brick pilasters with carved stone capitals, and paired brick Romanesque columns between the windows. The 12th Street side has brick-arched doorways. A 2009 state survey found the arched stone entrances partly or wholly hidden by later alterations. Interior not checked.",
  accn=DOWNTOWN+" Shops and upper floors are private: look from the street.",
  links=[W('Empire Block (Superior, Wisconsin)'),NRF('85001467','Empire Block'),AHI('17826','Empire Block'),DC_NR],brick='?',hours=''),
N('minnesota-block-board-of-trade-superior','Minnesota Block (Board of Trade Building)','Superior','wi','civic','standing',46.72034,-92.10443,'exact','view','walk','','1891–1892',
  "The largest of the Land and River Improvement Company's blocks: four storeys at Tower Avenue and Belknap Street, designed by C. C. Haight and built in 1891 and 1892 for about $225,000, with a fireproof steel and tile frame. A dry goods store filled the lower floors. From 1894 it was called the Board of Trade Building, and the corner became the transfer point of the city's streetcar lines.",
  look="Salmon pressed brick with sandstone trim, five bays between brick pilasters, a carved stone panel reading \"Board of Trade\" over the entrance and a copper cornice. On the Belknap side cast-iron shop-front columns stamped by the West Superior Iron and Steel Company survive (the 1985 form). Inside, the form saw an open iron elevator shaft in a cast-iron stair, oak and marble trim in the upper halls. Interior not checked now.",
  accn=DOWNTOWN+" Offices and shops: look from the street.",
  links=[NRF('85001470','Minnesota Block'),AHI('17859','Minnesota Block'),MPS,DC_NR],brick='?',hours=''),
N('washington-block-superior','Washington Block','Superior','wi','civic','standing',46.71984,-92.10437,'exact','view','walk','','1891',
  "A three-storey office and apartment block on Tower Avenue, begun in 1891 by William Folsom of New York and finished by the Land and River Improvement Company. It held the Northwest Hanna Coal Company, a furniture store and the state highway department, and became the Burlington Northern railroad's Superior office in 1980.",
  look="A front of light-coloured brick with cream terra cotta window surrounds carved with swags and flowers, a Greek key band over the ground floor and a terra cotta cornice in the manner of Louis Sullivan, with the original terra cotta entrance and its round window. The ground floor arcade was remodelled (the 1985 form). Interior not checked.",
  accn=DOWNTOWN+" Offices: look from the street.",
  links=[NRF('85001473','Washington Block'),AHI('17860','Washington Block'),MPS,DC_NR],brick='no',hours=''),
N('berkshire-block-superior','Berkshire Block','Superior','wi','civic','standing',46.72702,-92.10427,'exact','view','walk','','1892',
  "A two-storey Richardsonian Romanesque block at Tower Avenue and Broadway, built in 1892 by the New York financier Francis H. Weeks, an early president of the Land and River Improvement Company. It was built to carry six more floors that never came. The Register list says it first housed the State Bank; the 1985 form knew it as the Amsoil Building.",
  look="A front of rock-faced Kasota limestone with a ground-floor arcade of heavy round arches on rusticated columns wrapping two sides, polygonal bays at the corners, paired upper windows under heavy lintels and a dentilled cornice. The windows were replaced with tinted glass in the late 1970s and the interior was modernised (the 1985 form). Interior not checked.",
  accn=DOWNTOWN+" Offices: look from the street.",
  links=[NRF('85001466','Berkshire Block'),MPS,DC_NR],brick='no',hours=''),
N('trade-and-commerce-building-superior','Trade and Commerce Building (Old Superior City Hall)','Superior','wi','civic','standing',46.72682,-92.09751,'exact','view','walk','','1890',
  "A five-storey Richardsonian Romanesque office building of native sandstone at 916 Hammond Avenue, built in 1890 for Henry D. Minot and designed by Clarence H. Johnston Sr. of St. Paul, later Minnesota's state architect. It was the core of a grain exchange and later served as Superior's city hall.",
  look="Rusticated sandstone walls about three feet thick at the base, rounded corners, a big round-arched entrance with a fanlight and round-arched windows; the cornice was replaced with a metal fascia in the 1950s (the 1979 form). A 1918 brick police headquarters with a Doric porch is joined to its back (state record). Interior not checked.",
  accn="On Hammond Avenue at Broadway; street parking. Present use not checked: look from the street.",
  links=[NRF('79000076','Trade and Commerce Building'),AHI('17617','Trade and Commerce Building'),AHI('17618','Police Headquarters'),DC_NR],brick='no',hours=''),
N('superior-federal-building-1401-tower','Old Federal Building (Post Office, Custom House and Courthouse)','Superior','wi','civic','standing',46.72157,-92.10418,'site','view','walk','','1908',
  "The United States courthouse, custom house and post office at 1401 Tower Avenue, designed by Barber and Barber and first occupied in June 1908. It stayed a post office until 1982; a 2010 note in the state record says it had been made into apartments.",
  look="Cut stone: a rusticated ground floor with recessed segmental-arched windows and keystones, giant fluted Ionic columns across the second and third storeys, Ionic pilasters on the sides and a modillioned cornice over an inscribed frieze (state record). Interior not checked.",
  accn=DOWNTOWN+" Present use not checked beyond the 2010 note: look from the street.",
  links=[AHI('17852','United States Courthouse, Custom House and Post Office')],brick='no',hours=''),
N('superior-carnegie-library-hammond','Superior Carnegie Library (1204 Hammond Avenue)','Superior','wi','civic','standing',46.72389,-92.09750,'exact','view','walk','','1901',
  "Superior's first public library building, at 1204 Hammond Avenue, designed by Carl Wirth of Superior and built in 1901 (a 1999 state survey quoted by the Library History Buff), the oldest of Wisconsin's Carnegie library buildings; WPR also says it was the first built in the state, in 1901. It was the library until the end of 1991 and has stood empty since. The city council voted to condemn it in 2006, a friends' group raised money to save it, and in November 2022 the council paid $275,000 for a temporary roof membrane to keep it dry.",
  look="One storey of red brick on a raised rusticated red stone basement, with brick quoins, a stone balustrade on the parapet and a stone entrance pavilion: fluted Ionic columns carrying a pediment, round-arched windows either side and the word CARNEGIE over the door. The 1999 survey found the reading rooms, the Ionic columns into the stack room and the classical woodwork intact; some windows are boarded. Interior not open.",
  accn="Empty building on Hammond Avenue at 12th Street; street parking. Not open: look from the street. Owner not checked.",
  links=[L('Library History Buff: Carnegie libraries in Superior','https://libraryhistorybuff.com/carnegie-libraries-superior.htm'),L('Wisconsin Library Heritage Center','https://heritage.wisconsinlibraries.org/entry/superiors-carnegie-library-buildings/'),L('WPR: architectural firm seeks to buy the library','https://wpr.org/economy/north-carolina-architectural-firm-seeks-breathe-new-life-superior-carnegie-library'),L('B105: roof repair vote, November 4, 2022','https://b105country.com/superior-votes-to-spend-275k-on-carnegie-library-roof-repairs/')],brick='yes',hours=''),
N('old-main-uw-superior','Old Main, University of Wisconsin-Superior','Superior','wi','inst','standing',46.71759,-92.09104,'exact','view','walk','','1914–1916',
  "The main hall of the Superior State Normal School, now the University of Wisconsin-Superior; the state set the school up in 1893 and it took its first students in 1896 (the university's history page). This Late Gothic Revival hall by Van Ryn and DeGelleke was begun in 1914 and finished in 1916, and the Curran library wing was added in 1931 (state record).",
  look="Brick, with a slightly projecting entrance pavilion between two four-storey towers, a big round-arched doorway in a carved limestone surround and a classical porch on a side entrance (state record). Interior not checked.",
  accn="On the university campus at 1710 Weeks Avenue; look from the campus walks and the street. Campus parking rules not checked.",
  links=[AHI('17604','Main Hall, Superior State Normal School'),L('UW-Superior: history','https://uwsuper.edu/about/history/')],brick='?',hours=''),
N('franklin-school-superior','Franklin School (Allouez)','Superior','wi','civic','standing',46.69116,-92.02837,'site','view','drive','','1905',
  "A public school in the Allouez neighbourhood, built in 1905 and enlarged in 1917 with a junior high wing by E. R. Radcliffe that added a gymnasium, an auditorium and workshops. It closed as a school after the 1984 to 1985 year and has been apartments since 1992 (Douglas County Historical Society).",
  look="The historical society places it on the block between 36th and 37th avenues East and East 2nd and 3rd streets; OpenStreetMap maps a three-storey apartment building there named Franklin Courts. What survives of the 1905 front was not checked.",
  accn="Private apartments: look from the street only.",
  links=[L('Douglas County Historical Society: Franklin','https://douglashistory.org/franklin/')],conf='mixed',brick='?',hours=''),
N('fairlawn-mansion-superior','Fairlawn (Martin Pattison House)','Superior','wi','landmark','standing',46.71791,-92.06294,'exact','open','drive','','1889–1891',
  "The 42-room Queen Anne house of Martin Pattison, lumber and mining baron and three times mayor of Superior, begun in 1889 and finished in 1891, looking over the bay. The family lived there until 1918; it was a children's home from 1920 to 1962 and is now a museum; the 1981 Register form gives the city as owner. The 1981 Register form calls it the last surviving mansion of the city's boom.",
  look="A two-and-a-half storey house on a rock-faced Lake Superior brownstone foundation, with a wraparound brownstone-trimmed porch, a corner tower (its cupola was lost in a windstorm in the late 1920s), a porte-cochere and copper work dated 1890 in the front gable. Inside, the main floor keeps oak, cherry and mahogany woodwork, a central hall and stair and an Egyptian marble fireplace; Wikipedia says the main floor was restored in 1996.",
  accn="Museum at 906 East 2nd Street, on its own block; a lot on East 3rd Street by the grounds. The museum's own pages could not be opened when this was written; a search result quoting them says tours leave on the hour from the gift shop. Hours not checked.",
  links=[W('Fairlawn Mansion'),NRF('81000042','Martin Pattison House'),L('Superior Public Museums','https://superiorpublicmuseums.org/fairlawn-mansion'),DC_NR],brick='no',hours='?',
  th=[46.71788,-92.06345],thn='Fairlawn lot, East 3rd Street'),
]

PIN_NOTES={
 'new-jersey-building-superior':'OpenStreetMap building point (1432 Tower Avenue), on the corner block on the aerial.',
 'new-york-block-superior':'OpenStreetMap building named New York Apartments, at the southeast corner of Tower Avenue and 14th Street.',
 'empire-block-superior':'OpenStreetMap building point (1202 Tower Avenue), on the building on the aerial.',
 'minnesota-block-board-of-trade-superior':'OpenStreetMap building point for the Minnesota Block (1501 Tower Avenue).',
 'washington-block-superior':'OpenStreetMap building point (1517 Tower Avenue).',
 'berkshire-block-superior':'OpenStreetMap building point at Tower Avenue and Broadway.',
 'trade-and-commerce-building-superior':'OpenStreetMap building point (916 Hammond Avenue).',
 'superior-federal-building-1401-tower':'The address point for 1401 Tower Avenue fell in the street; moved to the three-storey building OpenStreetMap maps on the west side of Tower Avenue at 14th Street, opposite the New York Block. Not matched to the building by name.',
 'superior-carnegie-library-hammond':'Address lookup for 1204 Hammond Avenue, checked on the aerial.',
 'old-main-uw-superior':'OpenStreetMap building point for Old Main (1710 Weeks Avenue).',
 'franklin-school-superior':'OpenStreetMap building named Franklin Courts on the block the historical society gives; the pin marks that building.',
 'fairlawn-mansion-superior':'OpenStreetMap museum point (906 East 2nd Street); the parking point is the mapped lot on East 3rd Street.',
}
