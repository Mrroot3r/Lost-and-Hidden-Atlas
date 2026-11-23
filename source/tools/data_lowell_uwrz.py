# November 23, 2026: Lowell, Massachusetts. A "videos" session (PROMPTS.md job 9): the names came from one video's
# tour of old Lowell buildings (the record is source/videos/20241213_DUZf0QKiyOw.md); the video is a tip and nothing
# here rests on it. Sources read: Wikipedia (each article named in the links); the City of Lowell's Historic Board pages
# (City Hall district, St. Patrick's, the two old post offices); Doors Open Lowell building sheets and its 2024 guide
# (St. Anne's, St. Patrick, First United Baptist, the Boston & Maine depot, Coburn Hall); the National Park Service
# (St. Anne's); Lost New England (the county jail); the parishes' own pages (Immaculate Conception, St. Michael); the
# Lowell Cemetery's pages; the Pollard Memorial Library's and the City of Lowell's pages for hours.
# Pins are OpenStreetMap points, Wikipedia points or address points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'lowell_uwrz','label':'Massachusetts: old Lowell, City Hall, churches and the buildings round them','added':'2026-11-23 05:44'}

DT=' Downtown street meters and city garages are close by; their hours and fees were not checked.'
DOL=['Doors Open Lowell 2024: building guide','https://www.doorsopenlowell.org/s/Doors-Open-Lowell-2024-Program-Guide-Web.pdf']
LHB_PAT=['City of Lowell Historic Board: St. Patrick\'s Church','https://lowellma.gov/1057/St-Patricks-Church']
VC=[42.64369,-71.31386]
VCN='Lowell National Historical Park visitor center parking, Dutton Street'
LLG=[42.64301,-71.30565]
LLGN='Lower Locks Garage, Warren Street'

PLACES=[
N('lowell-city-hall','Lowell City Hall','Lowell','nshore','civic','standing',42.6464,-71.314,'exact','open','walk','','1890–1893',
  'Lowell\'s city hall at 375 Merrimack Street, built in 1893 in the Richardsonian Romanesque style to designs by the local firm of Merrill and Cutler. Its cornerstone was laid on October 11, 1890, the same day as the library\'s next door. It is the centrepiece of the City Hall Historic District, listed on the National Register in 1975 and enlarged in 1988, which takes in 73 buildings from as early as 1823, Old City Hall of 1830 among them.',
  'A heavy stone building with round arches and a clock tower given as 180 feet high, beside the matching Pollard Memorial Library. A monument to the Armenian Genocide, "A Mother\'s Hands", stands by it. Inside not checked.',
  'One of three stone Romanesque civic buildings Lowell finished within a few years in the early 1890s.',
  'Owned by the City of Lowell and open on weekdays as the city\'s offices; the hours are from the city\'s own page, and single departments may keep others.'+DT,
  [W('City Hall Historic District (Lowell, Massachusetts)'),['City of Lowell: City Hall hours','https://lowellma.gov/1276/History'],['City of Lowell Historic Board: City Hall Historic District','https://lowellma.gov/1064/City-Hall-Historic-District']],
  th=VC,thn=VCN,brick='no',hours='Monday, Wednesday, Thursday 8 a.m. to 5 p.m.; Tuesday 8 a.m. to 8 p.m.; Friday 8 a.m. to noon'),

N('pollard-memorial-library-lowell','Pollard Memorial Library (Memorial Hall)','Lowell','nshore','civic','standing',42.64657,-71.31471,'exact','open','walk','','1890–1893',
  'Lowell\'s main public library, designed by the Lowell architect Frederick W. Stickney as the City Library and Memorial Hall, in honour of the city\'s men who died in the Civil War. Its cornerstone was laid with City Hall\'s on October 11, 1890, and it opened on June 3, 1893. A fire in 1915 destroyed the second floor; it was rebuilt, and military murals by the French painter Paul Philippoteaux were put up there. It was remodelled in 2000 to 2002.',
  'Richardsonian Romanesque stone, next to City Hall. Upstairs are the Philippoteaux murals in the Civil War memorial hall. The accessible entrance is on the Colburn Street side.',
  '',
  'Owned by the City of Lowell; a working public library open to anyone at the hours on its own page, which also says the library opens at 11 a.m. on the first Thursday of each month. The library has a two-hour lot at the corner of Moody and Colburn streets.'+DT,
  [W('Pollard Memorial Library'),['Pollard Memorial Library: hours and parking','https://lowelllibrary.org/?p=26'],DOL],
  th=VC,thn=VCN,brick='no',hours='Monday to Thursday 9 a.m. to 9 p.m. (first Thursday from 11 a.m.); Friday 9 a.m. to 5 p.m.'),

N('lowell-memorial-auditorium','Lowell Memorial Auditorium','Lowell','nshore','civic','standing',42.64507,-71.30417,'exact','open','walk','','1922',
  'A 2,800-seat hall built in 1922 by the architects Blackall, Clapp and Whittemore and dedicated to the city\'s veterans of war. It is used for concerts, comedy, large plays and boxing, and the smaller Merrimack Repertory Theatre is attached to it. In 2014 a Civil War flag carried by a lieutenant of the 2nd Massachusetts Cavalry, given to the hall in 1929, was found in the basement; it now hangs in the Hall of Flags.',
  'The names of generals and battles are carved round the outside walls, and monuments to later wars stand on the small lawn. Inside only for events; not checked.',
  '',
  'A working hall at 50 East Merrimack Street; it is open for its events, whose dates and times are on its own listings.'+DT,
  [W('Lowell Memorial Auditorium')],
  th=LLG,thn=LLGN,brick='no',hours='?'),

N('st-patricks-church-lowell','St. Patrick\'s Church','Lowell','nshore','worship','standing',42.64529,-71.31864,'site','view','walk','','1853–1874; rebuilt inside 1904–1906',
  'Lowell\'s first Catholic church, for a mostly Irish parish founded in 1831 whose first church was a wooden one of that year. The present granite Gothic Revival church was built from 1853 to 1874 to designs by Patrick C. Keely. A fire in 1904 gutted much of the inside, which was rebuilt by 1906. It was listed on the National Register in 1985, and the parish now also serves Hispanic, Vietnamese and Burmese Catholics.',
  'Granite Gothic church on Suffolk Street at the edge of the Acre. The stained glass and pipe organ have been restored in recent years (Doors Open Lowell). Inside not checked.',
  '',
  'An active Catholic parish at 282 Suffolk Street. Its own page could not be read for Mass times when this was written; look them up before going.'+DT,
  [W('St. Patrick\'s Church (Lowell, Massachusetts)'),LHB_PAT,['Doors Open Lowell: St. Patrick Church','https://doorsopenlowell.org/s/St-Patrick-Church-DOL-2024.pdf']],
  brick='no',hours='?'),

N('immaculate-conception-church-lowell','Immaculate Conception Church','Lowell','nshore','worship','standing',42.64519,-71.3029,'exact','open','walk','','1871–1877',
  'A granite Gothic church of the Oblate Fathers at 144 East Merrimack Street, designed by Patrick Keely. By the parish\'s own history, digging began in April 1871, the lower church was blessed in July 1872, and the upper church opened for services on June 2, 1877, 191 feet long and seating about 2,000; the City of Lowell\'s Historic Board gives its date as 1868. The stained glass was all replaced by 1954, and the church has since been restored.',
  'Cruciform granite church with a carillon installed in 1948 and a marble altar and canopy of 1947. The crypt chapel below seats about 500.',
  '',
  'An active Catholic parish; anyone may come to Mass at the times on the parish\'s own page. Rectory at 3 Fayette Street.'+DT,
  [['Immaculate Conception Church: our church history','https://iclowell.org/?p=1563'],['Immaculate Conception Church: Mass times','https://iclowell.org/'],LHB_PAT],
  conf='mixed',th=LLG,thn=LLGN,brick='no',hours='Saturday 4 p.m.; Sunday 8 a.m., 10 a.m. and noon'),

N('st-annes-church-lowell','St. Anne\'s Episcopal Church','Lowell','nshore','worship','standing',42.64627,-71.31142,'exact','view','walk','','1824–1825',
  'The first church built in Lowell, paid for by the Merrimack Manufacturing Company for its mill workers, with the cost taken from their wages as pew rent. Its Gothic Revival design is given to Kirk Boott, the company\'s agent; the first stone was laid on May 20, 1824 and it was consecrated on March 16, 1825. The church and its rectory are the oldest mill-corporation buildings left in the city. It was lengthened in 1845, and a chapel (1868), choir and sacristy (1873) and the present chancel (1884) were added.',
  'Rubblestone walls of stone dug from the Merrimack Canal or the river bed, and a tower whose four lost pinnacles have been copied back. Stained glass from 1872 on, many windows by Tiffany of New York and C. J. Connick of Boston, restored since the 1980s.',
  '',
  'An active Episcopal church at 8 Kirk Street, by Merrimack Street, within Lowell National Historical Park. Service times were not found on a page of its own. It opens on Doors Open Lowell days.'+DT,
  [['National Park Service: St. Anne\'s Church','https://www.nps.gov/places/st-anne-s-episcopal-church.htm'],['Doors Open Lowell: St. Anne\'s Church','https://doorsopenlowell.org/s/St-Annes-Church-DOL-2024.pdf']],
  th=VC,thn=VCN,brick='no',hours='?'),

N('first-united-baptist-church-lowell','First United Baptist Church','Lowell','nshore','worship','standing',42.64133,-71.30603,'exact','view','walk','','1826',
  'A Greek Revival church at 99 Church Street, built in 1826; Doors Open Lowell calls it the city\'s second oldest church. Several of its members took part in the movement to end slavery, and it welcomed new members from the African Meeting House in Boston.',
  'The Greek Revival front on Church Street, in the Downtown Lowell Historic District. Inside not checked.',
  '',
  'An active American Baptist church; service times were not found on a page of its own. Seen from the street.'+DT,
  [['Doors Open Lowell: First United Baptist Church','https://doorsopenlowell.org/s/First-United-DOL-2024.pdf'],DOL],
  brick='no',hours=''),

N('st-jean-baptiste-church-lowell','St. Jean Baptiste Church (former)','Lowell','nshore','worship','standing',42.64911,-71.31991,'exact','view','walk','','1890',
  'A church built in 1890 at 741 Merrimack Street, important to the French Canadian and French American people who settled in Lowell late in the 19th century. Jack Kerouac served there as an altar boy and his funeral Mass was held there in 1969. Many of its people were pushed out by urban renewal in the 1950s, the church closed by the 1990s, and the archdiocese sold it in 2006. In May 2025 the singer Zach Bryan bought it for $3.4 million, to become the Jack Kerouac Center with a performance space and a museum; in February 2026 that was still being planned.',
  'A large stone church in the Acre, said by those planning the center to look like the churches of Europe. Not open while it waits to be converted; seen from Merrimack Street.',
  '',
  'Privately owned and closed. View from the public sidewalk only.'+DT,
  [['WBUR: Zach Bryan buys the church for a Kerouac center (May 2025)','https://www.wbur.org/news/2025/05/15/zach-bryan-jack-kerouac-center-lowell-newsletter'],['GBH: the latest on the Kerouac center (February 2026)','https://www.wgbh.org/news/local/2026-02-15/heres-the-latest-on-creating-a-a-cultural-hub-dedicated-to-jack-kerouac-in-lowell']],
  brick='no',hours=''),

N('st-michael-church-lowell','St. Michael Church','Lowell','nshore','worship','standing',42.65235,-71.30189,'exact','open','walk','','1884–1900',
  'The church of a parish founded in 1883 for the mostly Irish people of Centralville and Dracut, at 543 Bridge Street. By the parish\'s own history the cornerstone was laid on April 21, 1884, the basement church was finished that June and used for years, and the upper church, begun in 1898, was ready for worship in June 1900. The City of Lowell names Patrick Keely as its architect.',
  'A big Catholic church on Bridge Street in Centralville, with the parish school nearby. Its main altar was a gift of the parish founder. Inside not checked.',
  '',
  'An active Catholic parish; anyone may come to Mass at the times on its own page. Rectory open Monday to Thursday.',
  [['Saint Michael Parish: about our parish','https://www.saint-michael.com/about-our-parish'],['Saint Michael Parish: Mass times','https://www.saint-michael.com'],LHB_PAT],
  brick='?',hours='Saturday 4 p.m.; Sunday 7 and 9:30 a.m.; weekdays 7 a.m. (Wednesday 8:15 a.m.)'),

N('lowell-post-office-1893','Old Lowell Post Office (Juvenile Court)','Lowell','nshore','civic','standing',42.64113,-71.30915,'exact','view','walk','','1893–1895',
  'A two-storey granite post office at 89 Appleton Street, designed by W. J. Edbrooke, with a five-storey clock tower. The City of Lowell gives 1893 as the year it was built; Wikipedia and the National Register give 1895 for its completion. The post office moved to Kearney Square in the 1930s (1933 by the city, 1936 by Wikipedia). It later held the school department\'s offices, and after the city sold it a developer restored it as a juvenile court, opened in May 2001. Listed on the National Register in 2002.',
  'Rough-faced square stonework, wide round arches, deep-set doors and windows, and the square clock tower under a pyramid roof with tripled arches on each face.',
  '',
  'A working court building; seen from Appleton Street. Court visitors go through security; it is not a place to tour.'+DT,
  [W('Lowell Post Office'),['City of Lowell Historic Board: Lowell Post Office','https://lowellma.gov/1053/Lowell-Post-Office']],
  conf='mixed',brick='no',hours=''),

N('morse-federal-building-lowell','F. Bradford Morse Federal Building (former U.S. Post Office)','Lowell','nshore','civic','standing',42.64535,-71.30611,'exact','view','walk','','1930–1932',
  'Lowell\'s Neoclassical post office at 50 Kearney Square, designed by George Augustine Daidy, one of the few architects then born in Lowell. Building began in August 1930 and it opened in January 1932, by the city\'s account. It stayed a post office until the late 1960s and then held federal offices; Middlesex Community College bought it in 1996 and renovated it, and it was named for the congressman F. Bradford Morse in 2006. Listed on the National Register in 1986.',
  'The columned Neoclassical front on Kearney Square. It now holds the college\'s Lowell campus library, its Honors Center, art studios and classrooms. Inside not checked.',
  '',
  'Owned by Middlesex Community College; seen from Kearney Square. Its library hours were not checked.'+DT,
  [W('F. Bradford Morse Federal Building'),['City of Lowell Historic Board: U.S. Post Office','https://lowellma.gov/1556/US-Post-Office']],
  th=LLG,thn=LLGN,brick='?',hours=''),

N('middlesex-county-jail-lowell','Old Middlesex County Jail (Keith Academy)','Lowell','nshore','inst','standing',42.63553,-71.3131,'site','view','walk','','1856',
  'The second Middlesex County jail in Lowell, opened on Thorndike Street in 1856 for just over 100 prisoners, most serving short sentences. It is an early example of Romanesque Revival. It closed as a jail in 1919, and in 1926 the Catholic Church bought it and gutted the inside to make a prep school, Keith Academy, which closed in 1970. It was then turned into 56 condominiums.',
  'From outside it looks much as it did when it opened: the Romanesque towers and walls on Thorndike Street. The inside is private homes.',
  '',
  'Private condominiums. View from Thorndike Street only.',
  [['Lost New England: County Jail, Lowell','https://lostnewengland.com/?p=2938'],['UMass Lowell Library: the old Lowell jail','https://libguides.uml.edu/early_lowell/old_Lowell_Jail']],
  brick='no',hours=''),

N('lowell-cemetery','Lowell Cemetery and Talbot Chapel','Lowell','nshore','burial','standing',42.62680,-71.29624,'site','public','walk','cemeteries','1841',
  'A garden cemetery founded in 1841 on the bank of the Concord River, modelled on Mount Auburn in Cambridge, where many of Lowell\'s mill owners are buried under ornate Victorian stones. Its granite main gate on Lawrence Street, designed by C. W. Painter, was built in 1862. The Talbot Memorial Chapel was put up in 1885 by Harriet Rogers Talbot on the site of an 1848 chapel, to designs by Frederick Stickney, who also drew the Pollard library. 73 of its 84 acres were listed on the National Register in 1998.',
  'The granite Lawrence Street gate and gatehouse, the Romanesque Talbot Chapel with its slate roof and rounded apse, the Gothic Revival Superintendent\'s Office of 1887, and winding roads over rolling ground.',
  'Where the men who built the mills are buried.',
  'A private, non-denominational cemetery whose trustees welcome walkers; the main gate is on Lawrence Street and the office at 77 Knapp Avenue. The cemetery runs walking tours in season from the Lawrence Street gate. Its daily opening hours were not checked.',
  [W('Lowell Cemetery (Lowell, Massachusetts)'),['Lowell Cemetery: Talbot Chapel history','https://www.lowellcemetery.com/wp-content/uploads/2021/02/Talbot-Chapel.pdf'],['Lowell Cemetery: walking tours','https://www.lowellcemetery.com/explore-visit/walking-tours/']],
  brick='?',hours='?'),

N('boston-maine-depot-lowell','Boston & Maine Railroad Depot (Rialto)','Lowell','nshore','rail','standing',42.64202,-71.30833,'exact','open','walk','','1876',
  'A High Victorian Gothic station at 240 Central Street, built in 1876 as Lowell\'s Central Street depot, with a long train shed behind. Trains stopped using it in 1895. It was later a cotton and wool store, the Owl Theater from 1913, the Rialto Theater from 1921 to 1960, and a bowling alley from 1961. Near collapse, it was given to the federal Lowell Historic Preservation Commission for $1 in 1989, restored outside, and passed to Middlesex Community College, which rebuilt the inside from 2015 to 2018.',
  'A two-storey brick headhouse with many-coloured masonry, cast-iron colonnettes and iron roof cresting; the two towers and the cornice were rebuilt. It is now the Richard and Nancy Donahue Family Academic Arts Center, with an egg-shaped theatre inside.',
  '',
  'Owned by Middlesex Community College; open for its plays and concerts and on Doors Open Lowell days. Building hours were not checked.'+DT,
  [['Doors Open Lowell: Boston & Maine Railroad Depot','https://doorsopenlowell.org/s/Boston-and-Maine-Depot-DOL-2024.pdf'],DOL],
  th=LLG,thn=LLGN,brick='yes',hours='?'),

N('coburn-hall-lowell','Coburn Hall (Lowell Normal School)','Lowell','nshore','civic','standing',42.64111,-71.33397,'exact','view','walk','','1897',
  'The Classical Revival building of the Lowell Normal School, a state college for teachers founded in 1894, built in 1897 to designs by Frederick Stickney and William Austin and named for the school\'s first dean, Frank Coburn. The school became Lowell Teachers College in 1932 and Lowell State College by 1960, and is now part of UMass Lowell. A $47 million rehabilitation was finished in 2022.',
  'The Classical Revival front on Broadway Street. During the rehabilitation murals of the 1930s were uncovered and restored inside.',
  '',
  'A UMass Lowell building at 850 Broadway Street; seen from the street, and opened to visitors on Doors Open Lowell days.',
  [['Doors Open Lowell: Coburn Hall','https://doorsopenlowell.org/s/Coburn-Hall-DOL-2024.pdf'],DOL],
  brick='no',hours=''),
]

PIN_NOTES={
 'lowell-city-hall':'OpenStreetMap point for Lowell City Hall, 375 Merrimack Street.',
 'pollard-memorial-library-lowell':'OpenStreetMap point for the library, 401 Merrimack Street.',
 'lowell-memorial-auditorium':'Wikipedia coordinate for the auditorium at 50 East Merrimack Street.',
 'st-patricks-church-lowell':'Wikipedia coordinate for the church on Suffolk Street.',
 'immaculate-conception-church-lowell':'OpenStreetMap point for the church, 144 East Merrimack Street.',
 'st-annes-church-lowell':'OpenStreetMap point for the church, 8 Kirk Street.',
 'first-united-baptist-church-lowell':'Address point for 99 Church Street, which matches the OpenStreetMap church point.',
 'st-jean-baptiste-church-lowell':'OpenStreetMap point for the church, 741 Merrimack Street.',
 'st-michael-church-lowell':'OpenStreetMap church building on Bridge Street; the address point for 543 Bridge Street fell on a smaller building beside it.',
 'lowell-post-office-1893':'Address point for 89 Appleton Street, which matches the Wikipedia coordinate.',
 'morse-federal-building-lowell':'OpenStreetMap building point, 50 Kearney Square.',
 'middlesex-county-jail-lowell':'Address point for 201 Thorndike Street, one of the addresses the condominiums give, on an OpenStreetMap building of that number beside the YMCA; that it is the old jail itself is not checked on a picture.',
 'lowell-cemetery':'Address point on Lawrence Street, by the main gate on the cemetery side of the road.',
 'boston-maine-depot-lowell':'OpenStreetMap point for the arts center, 240 Central Street.',
 'coburn-hall-lowell':'OpenStreetMap building named Coburn Hall; the address point for 850 Broadway Street fell on the power plant south of it.',
}
