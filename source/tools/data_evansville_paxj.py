# November 22, 2026: downtown Evansville, Indiana, and the old Evansville College campus. The names came from one
# video (a stranger's tip, never a source); every fact here is from a source opened while this batch was written:
# Wikipedia articles, National Register forms and state inventory sheets on NPGallery, the Old Courthouse's own history
# page, Willard Library's own page, the Coliseum's own page, Clio and Discover Indiana entries.
from data_b import N
from data_ma import W

BATCH={'key':'evansville_paxj','label':'Evansville, Indiana: courthouse square and old downtown','added':'2026-11-22 17:35'}

def NR(ref,label):
    return ['National Register form: '+label,'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]

DT='Downtown Evansville has metered street parking and several lots; OpenStreetMap maps one on Court Street a block west of the courthouse. Who may use each lot was not checked.'

PLACES=[
N('old-vanderburgh-courthouse-evansville','Old Vanderburgh County Courthouse','Evansville','in','civic','standing',37.97394,-87.57226,'exact','view','walk','','1887–1890',
  'Vanderburgh County\'s courthouse from 1891 until the county moved to its new Civic Center in 1969. Henry Wolters of Louisville designed it in the Beaux-Arts style and it fills a whole city block, built on the filled-in turning basin of the Wabash and Erie Canal. The dates and cost differ by source: Wikipedia says work began in spring 1888 and cost $379,450, the Old Courthouse Foundation says November 9, 1887 and about $500,000; both say it was finished in 1890. Plans to pull it down after 1969 came to nothing, partly because demolition would have cost so much, and citizens\' groups leased and restored it; the county has run it again since 2000.',
  'Indiana limestone carved all round: fourteen main statues of allegorical figures by Franz Engelsmann, and fruit, vegetables and flowers of the region on the capitals of the 48 pairs of pilasters. The bell tower is 216 feet tall. Inside, by the Foundation\'s page, are marble floors, pink Etowah marble wainscots, slate stairs and iron and brass rails; the restored courtroom and ballroom are hired for events. A tunnel under Vine Street joins it to the old jail.',
  'A whole block of carved limestone built on top of a canal basin.',
  'Owned and managed by Vanderburgh County with the Old Courthouse Foundation. The county engineer and veterans\' service offices are in the building and the rest is leased to private offices and hired out for weddings and events (the Foundation\'s page); no visiting hours were found, so the entry treats it as seen from the street and the lawn (Bicentennial Park). The Foundation\'s page says it gives tours; ask it about one. '+DT,
  [['Old Courthouse Foundation: history','https://www.oldvanderburghcourthouse.com/history'],W('Old Vanderburgh County Courthouse'),
   ['Clio: Old Vanderburgh County Courthouse','https://theclio.com/entry/77032']],
  conf='mixed',brick='no'),

N('old-vanderburgh-jail-evansville','Old Vanderburgh County Jail and Sheriff\'s Residence','Evansville','in','civic','standing',37.9735,-87.57305,'site','view','walk','','1890–1967',
  'A jail and sheriff\'s house built together in 1890 by Henry Wolters, the courthouse\'s architect, across Vine Street from it. It was modelled on Lichtenstein Castle in Germany. It held prisoners until 1967 and the sheriff lived in the front house until 1969; it then stood empty and decaying until it was renovated in the 1990s. In 1903 it was the scene of a race riot after a Black man shot a white police officer. Listed on the National Register in 1970.',
  'A stone castle in miniature: rusticated Indiana limestone, a round central keep, step gables, turrets, battlements and a mock portcullis over the pointed-arched entrance (Register form and Wikipedia). The jail block stands behind the house. Interior not checked.',
  'A county jail built to look like a German castle.',
  'Private: Wikipedia names a law firm as the building\'s user and owner of its offices. Look from Vine and Fifth streets; no public opening was found. '+DT,
  [W('Old Vanderburgh County Jail'),NR('70000009','Former Vanderburgh County Sheriff\'s Residence')],brick='no'),

N('willard-library-evansville','Willard Library','Evansville','in','civic','standing',37.97836,-87.57404,'exact','open','walk','','1877–1885',
  'Willard Carpenter gave the land and money for it in 1876, after his plan for a Willard College proved too costly. The stone foundation was laid in 1877, then work stopped for years while the property that was to pay for it lost value; the library opened on March 28, 1885. The library says it is the oldest library building in Indiana. It is still a free public library, with a large genealogy and local-history collection on the second floor.',
  'A Victorian Gothic library by James W. Reid, with steep roofs, turrets and rows of Gothic-arched windows, set in its own small park on First Avenue. Wikipedia\'s photograph shows red brick banded and trimmed in lighter stone. It is open to all; the library is also known for its "Grey Lady" ghost story and the webcams it keeps for her.',
  'Indiana\'s oldest library building, still lending books.',
  'Run by the Willard Library trustees; free and open to the public. Hours from the library\'s own page. Parking not checked: OpenStreetMap shows lots on Ingle Street to the south.',
  [['Willard Library: about us and hours','https://willard.lib.in.us/about-us/'],W('Willard Library')],
  brick='yes',hours='Monday and Tuesday 9 a.m. to 8 p.m.; Wednesday to Friday 9 a.m. to 5:30 p.m.; Saturday 9 a.m. to 5 p.m.; Sunday 1 to 5 p.m.'),

N('old-post-office-evansville','Evansville Post Office and Customs House','Evansville','in','civic','standing',37.9716,-87.57464,'exact','view','walk','','1876–1879',
  'Evansville\'s federal building, begun in 1876 and finished in 1879, designed in the Supervising Architect\'s office: Alfred B. Mullett drew a Second Empire design and William Appleton Potter changed it to Ruskinian Gothic. It held the post office, the federal court, the customs service and the weather bureau. Matching wings were added in 1918. After a new federal building opened in 1968 it was sold, and it is now offices and event space called Old Post Office Plaza.',
  'Three storeys of limestone with contrasting brownstone details, a front arcade, an oriel window and a slate roof (Wikipedia). Interior not checked; it is hired out for events.',
  'A Gothic federal building that held the post office, the court and the customs house at once.',
  'Privately owned offices and event space. Look from Second Street and Sycamore; no public opening hours were found. '+DT,
  [W('United States Post Office (Evansville, Indiana)')],brick='no'),

N('soldiers-sailors-coliseum-evansville','Soldiers and Sailors Memorial Coliseum','Evansville','in','civic','standing',37.97436,-87.5734,'exact','view','walk','','1916–1917',
  'A memorial hall to Vanderburgh County\'s soldiers of the Civil War and the Spanish–American War, set on the axis of Fourth Street; the cornerstone was laid on May 9, 1916 and it was dedicated on April 18, 1917. It was the city\'s first modern hall for conventions and big gatherings, designed by Shopbell & Company. It is still run by the veterans and hired out for events, sports and shows.',
  'A neoclassical front with six columns and two large bronze groups by George H. Honig flanking the steps: the Spirit of 1865 and the Spirit of 1916. Inside, by the hall\'s own page, are a lobby with a built-in ticket booth and the Grand Army of the Republic and Spanish–American War rooms off it. Interior seen only at events.',
  'A 1917 memorial hall with two bronze groups of old soldiers at the door.',
  'Run by the local Veterans Council and hired for events; it opens for whatever is booked. No regular visiting hours were found: look from Fourth and Court streets. '+DT,
  [W('Soldiers and Sailors Memorial Coliseum'),['Soldiers and Sailors Memorial Coliseum: the hall\'s page','https://vmcoliseumevvgm.wixsite.com/veteransmemorial']],
  brick='?'),

N('citizens-national-bank-evansville','Citizens National Bank Building','Evansville','in','civic','standing',37.97139,-87.57139,'exact','view','walk','','1916',
  'A ten-storey bank tower at Fourth and Main, the region\'s first skyscraper, designed by William Lee Stoddart and opened on Washington\'s Birthday in 1916. It has also been called the Hilliard-Lyons Building and Kunkel Square. In 2011 it was turned into 46 apartments. Listed on the National Register in 1982.',
  'The stone and terracotta front on Main Street (Wikipedia). Interior not checked; it is now apartments.',
  'Evansville\'s first skyscraper.',
  'Private apartments: look from Main and Fourth streets. '+DT,
  [W('Citizens National Bank (Evansville, Indiana)')],brick='no'),

N('eagles-home-evansville','Eagles Home','Evansville','in','civic','standing',37.97468,-87.57159,'exact','view','walk','','1912',
  'The lodge of the Fraternal Order of Eagles\' Evansville aerie, designed by local architect Harry E. Boyle and built in 1912; a rear wing was added in 1940. The Eagles moved out after 1968 and Lockyear Business College used it until the college closed in 1991; the college\'s own building beside it was pulled down in 1993 for a parking court. Since 1994 it has been offices, latterly a law firm\'s.',
  'A red-brick lodge with stone trim on Northwest Fifth Street, with a plainer white-painted wing beside it (Wikipedia\'s photograph). Interior not checked.',
  'A 1912 fraternal lodge that became a business college.',
  'Private offices: look from Fifth Street. '+DT,
  [W('Eagles Home (Evansville, Indiana)'),NR('82000090','Eagles Home')],brick='yes'),

N('mccurdy-hotel-evansville','McCurdy Hotel','Evansville','in','hotel','standing',37.96854,-87.57401,'exact','view','walk','','1916–1969',
  'A Colonial Revival hotel by St. Louis architect H. Ziegler Dietz, built in 1916–1917 on the site of the St. George Hotel, which was razed in 1915. It opened on June 17, 1917, the same year as the Coliseum, as the city\'s convention headquarters, and was one of three big downtown hotels of its day; it closed in bankruptcy on March 16, 1969. Harry Truman stayed there on his 1948 campaign. It reopened as apartments in spring 2017.',
  'A tall red-brick hotel block with a light stone base and a deep cornice, on First Street at the riverfront (Wikipedia\'s photograph). Interior not checked; it is now apartments.',
  'The convention hotel where Truman stayed in 1948.',
  'Private apartments: look from First Street and Riverside Drive. OpenStreetMap maps a lot just south on Riverside Drive; who may use it was not checked.',
  [W('McCurdy Hotel'),NR('82000109','McCurdy Hotel')],brick='yes'),

N('indiana-bell-building-evansville','Indiana Bell Building','Evansville','in','civic','standing',37.97357,-87.57107,'exact','view','walk','','1929',
  'A telephone company building of 1929 by the Indianapolis firm Vonnegut, Bohn and Mueller, which the 1982 state inventory called one of Evansville\'s finest Art Deco buildings. It was built smaller than it is now; later additions in the same manner enlarged it. Listed on the National Register in 1982.',
  'Seven storeys clad in limestone, in the Art Deco manner (Wikipedia). Interior not checked.',
  'Art Deco built for the telephone company.',
  'Private: look from Fifth Street. Whether it still houses the telephone company was not checked. '+DT,
  [W('Indiana Bell Building'),NR('82000103','Indiana Bell Building')],brick='no'),

N('evansville-brewing-company-building','Evansville Brewing Company','Evansville','in','industry','standing',37.97572,-87.57337,'exact','view','walk','','1891–1918',
  'The main block of the Evansville Brewery, begun in 1891 at Fourth and Ingle streets under Henry Wimberg. In 1893 it joined two other breweries as the Evansville Brewing Association. Brewing here stopped in April 1918 with Prohibition; the building was then cold storage for eggs and butter, a Dodge dealership until the late 1960s, and by 1981 a restaurant supply company. It is not the later Evansville Brewing Company of 1988, which was in the old Fulton Avenue brewery on Pennsylvania Avenue.',
  'A four-storey Romanesque Revival brick building at the corner of Northwest Fourth and Ingle streets (Wikipedia); its photograph shows red brick walls with tall round-arched panels. Interior not checked.',
  'A Romanesque brewery block that made beer until Prohibition.',
  'Private: look from Fourth and Ingle streets. Its use today was not checked. '+DT,
  [W('Evansville Brewing Company'),NR('82000091','Evansville Brewing Company')],brick='yes'),

N('olmsted-hall-university-evansville','Olmsted Administration Hall, University of Evansville','Evansville','in','inst','standing',37.97165,-87.53156,'exact','view','walk','','1921–1922',
  'The first building of Evansville College, dedicated in June 1922, after the city\'s Chamber of Commerce and the Methodist Church moved the struggling Moores Hill College here in 1917. It was meant as the head of a 22-building Collegiate Gothic campus round a green called the Circle, most of which was never built to that plan. The hall, the Circle and the President\'s House were listed on the National Register together in 1983. Renamed Olmsted Hall in 1980; the college became the University of Evansville in 1967.',
  'Three storeys of clay tile faced with Indiana limestone ashlar, with Tudor Gothic mouldings, carved stone and a 78-foot tower on the front, by the architects Miller, Fullenwider and Dowling (Register form). It faces south over the Circle from Lincoln Avenue. Interior not checked.',
  'A Gothic college hall that was to be the first of 22.',
  'Owned by the University of Evansville; a working campus. The grounds can be walked from Lincoln Avenue; the buildings are for the university\'s use. Campus parking rules not checked.',
  [W('University of Evansville'),NR('83000106','Evansville College'),['Discover Indiana: Evansville College','https://discoverindianahistory.org/items/show/319']],
  brick='no'),
]

PIN_NOTES={
 'old-vanderburgh-courthouse-evansville':'Address point for 201 Northwest Fourth Street; checked on the aerial.',
 'old-vanderburgh-jail-evansville':'Moved onto the block across the street west of the courthouse, between Wikipedia\'s coordinate (which fell in a parking lot) and the National Register list\'s; the castle front could not be picked out from above, so the pin marks the site.',
 'willard-library-evansville':'OpenStreetMap\'s point for the library on First Avenue; checked on the aerial.',
 'old-post-office-evansville':'OpenStreetMap\'s building "Old Post Office"; checked on the aerial.',
 'soldiers-sailors-coliseum-evansville':'OpenStreetMap\'s point for the Coliseum, 300 Court Street; checked on the aerial.',
 'citizens-national-bank-evansville':'Wikipedia\'s coordinate at Fourth and Main; checked on the aerial.',
 'eagles-home-evansville':'Address point for 221 Northwest Fifth Street, the address on the state inventory sheet; checked on the aerial.',
 'mccurdy-hotel-evansville':'Address point for 101 Southeast First Street, the address on the state inventory sheet; checked on the aerial.',
 'indiana-bell-building-evansville':'OpenStreetMap\'s building at 133 Northwest Fifth Street, within the 129–133 address on the state inventory sheet; the street address point fell at the building\'s edge.',
 'evansville-brewing-company-building':'Address point for 401 Northwest Fourth Street, the address on the state inventory sheet; checked on the aerial.',
 'olmsted-hall-university-evansville':'OpenStreetMap\'s building "Olmsted Administration Hall"; checked on the aerial.',
}
