# November 28, 2026: Lincoln, Nebraska, from the names in one Old World Exploration video about Lincoln
# (record: source/videos/20230507_AuBI-u1hbCU.md). The video was a list of names only; every fact below comes from the
# sources linked on each place: National Register records and nomination forms read as text from NPGallery, SAH Archipedia
# entries, the University of Nebraska-Lincoln archives' historic-buildings pages, Wikipedia, the City of Lincoln's
# Pioneers Park page and First-Plymouth's own site. Pins are Register-list points, ArcGIS address points and one
# OpenStreetMap point, each looked at on the aerial.
# Red brick: Architecture Hall ('yes', SAH Archipedia: red brick) and the Coliseum ('some', red pressed brick with
# limestone, UNL archives); Old City Hall ('no', faced with rough limestone) and the Pioneers Park columns ('no',
# sandstone); the VA hospital ('yes', its main building is plain red brick in a Commons photograph); the rest are '?'.
from data_b import N
from data_ma import W

BATCH={'key':'lincoln_vuxe','label':'Lincoln, Nebraska (from a video)','added':'2026-11-28 04:45'}

NR='https://npgallery.nps.gov/NRHP/GetAsset/NRHP/'
REC='https://npgallery.nps.gov/AssetDetail/NRIS/'
SAH='https://sah-archipedia.org/buildings/'
UNL='https://archives-spec.unl.edu/unl-historic-buildings/'

PLACES=[
N('old-city-hall-lincoln-ne','Old City Hall (first U.S. Post Office and Court House)','Lincoln','ne','civic','standing',40.81392,-96.70777,'exact','view','walk','','1874–1879',
  "Lincoln's first federal building, begun in 1874 and finished in 1879 as the U.S. Post Office and Court House, only a few years after statehood. It held a U.S. Land Office that handled Homestead Act claims for more than five million acres of southern Nebraska. When the second federal building went up on the north half of the same block in 1906, the city took this one over, and it was Lincoln's City Hall until 1969; civic groups have used it since.",
  look="Four storeys over a basement, brick faced with rough quarry-faced limestone, under a mansard roof with gabled dormers; the pointed and trefoil-headed window arches are the High Victorian Gothic touch of William A. Potter, who followed Alfred B. Mullett as the Treasury's architect. SAH Archipedia says the cast-iron stairways and much of the original woodwork survive inside, and the pressed-metal ceiling of the old courtroom is a restoration. Whether the public may go in was not checked.",
  accn="At 920 O Street, at the south end of Government Square in the Haymarket. Used by civic groups: see it from O Street and the square. Downtown street and pay parking nearby (not checked).",
  links=[W('City Hall (Lincoln, Nebraska)'),['SAH Archipedia: Old City Hall',SAH+'NE-01-109-0029'],['National Register record',REC+'69000132']],
  brick='no',bcol='none'),
N('grand-manse-lincoln-ne','Grand Manse (second U.S. Post Office and Court House)','Lincoln','ne','civic','standing',40.81441,-96.70739,'exact','view','walk','','1904–1941',
  "The second federal post office and court house, built on the north half of Government Square in three stages between 1904 and 1941. James Knox Taylor, the Treasury's supervising architect, designed the first, east part in a restrained Beaux-Arts classical manner, and later architects carried his design north and west. In 2004 it was renovated as Grand Manse, with offices, homes, a restaurant and event space.",
  look="A block-long classical stone building facing Old City Hall across Government Square. Interior not checked.",
  accn="At 129 North 10th Street. Privately run offices, homes and businesses: see it from the street and the square. Downtown street and pay parking nearby (not checked).",
  links=[['SAH Archipedia: Grand Manse',SAH+'NE-01-109-0029-01'],['SAH Archipedia: Old City Hall and Government Square',SAH+'NE-01-109-0029']],
  apart='old-city-hall-lincoln-ne: the first and second federal buildings, two buildings on one square',
  brick='?'),
N('architecture-hall-unl-lincoln','Architecture Hall (Old University Library)','Lincoln','ne','civic','standing',40.81731,-96.70611,'exact','view','walk','','1891–1895',
  "The University of Nebraska's first library, built in two stages between 1891 and 1895 to designs by Mendelssohn, Fisher and Lawrie, and the oldest building on the Lincoln city campus. It later became Architecture Hall, and in 1985 to 1987 it was restored and joined by a glass link to the 1912 Old Law College next door.",
  look="Red brick over a raised basement with stone stringcourses and sills: a two-storey north wing with a hipped roof and clerestory, and a taller south wing with steep gabled dormers and an octagonal-roofed projection flanked by two copper owls about three feet tall. The east entrance has a round arch between brick pilasters topped with octagonal turrets, and a grand wooden stair inside (SAH Archipedia).",
  accn="At 11th and R streets on the University of Nebraska-Lincoln city campus. A working college building: see it from the campus walks. Campus and downtown pay parking nearby (not checked).",
  links=[['SAH Archipedia: Architecture Hall',SAH+'NE-01-109-0031'],['National Register nomination (1975)',NR+'75001098_text']],
  brick='yes',bcol='red'),
N('temple-building-unl-lincoln','Temple Building, University of Nebraska','Lincoln','ne','civic','standing',40.81658,-96.70355,'exact','view','walk','','1906',
  "A university building of 1906 at the corner of 12th and R streets, designed by John Latenser and Sons, built by W. L. Campbell and costing $95,000. The university's archives list John D. Rockefeller and Chancellor E. Benjamin Andrews among the people tied to it, and date it from 1906 to the present. The university's news pages show shows still staged in it.",
  look="Seen from 12th and R streets. Its materials and interior were not checked.",
  accn="On the University of Nebraska-Lincoln city campus at 12th and R streets. A working university building: see it from the street; performances inside were not checked. Campus and downtown pay parking nearby (not checked).",
  links=[['UNL Archives: The Temple',UNL+'temple'],['Nebraska Today: Temple Building','https://news.unl.edu/tag/temple-building']],
  brick='?'),
N('nebraska-coliseum-lincoln','Nebraska Coliseum','Lincoln','ne','civic','standing',40.82139,-96.7025,'exact','view','walk','','1925–1926',
  "The University of Nebraska's arena, paid for out of future football gate receipts, designed by Davis and Wilson and built from 1925 in time for commencement in spring 1926. It held basketball, commencement and dances (Glenn Miller and Tommy Dorsey played there) and was home to the volleyball team until 2013. It was renovated in 1989 and is now part of the campus recreation centre.",
  look="Red pressed brick and Bedford limestone, with ten large columns across the entrance, in the same manner as Morrill Hall and Memorial Stadium nearby (UNL archives).",
  accn="On the University of Nebraska-Lincoln city campus, north of the downtown. Used for student recreation: see it from the campus walks. Campus pay parking nearby (not checked).",
  links=[W('Nebraska Coliseum'),['UNL Archives: Coliseum',UNL+'coliseum']],
  brick='some',bcol='red'),
N('old-main-nebraska-wesleyan-lincoln','Old Main, Nebraska Wesleyan University','Lincoln','ne','civic','standing',40.8389,-96.64972,'exact','view','walk','','1887–1889',
  "The first building of Nebraska Wesleyan University, opened in October 1888 in the then separate town of University Place; for a time it was the whole university. It was designed by Gibbs and Parker and is listed on the National Register.",
  look="Three storeys of Richardsonian Romanesque, about 150 by 71 feet, in pressed brick trimmed with red stone on a limestone foundation, with heavy round arches over many of the windows (Register form, 1975). Interior not checked.",
  accn="On the Nebraska Wesleyan University campus near 50th Street and St. Paul Avenue. A working college building: see it from the campus walks. Parking not checked.",
  links=[W('Nebraska Wesleyan University'),['National Register nomination (1975)',NR+'75001097_text']],
  brick='?'),
N('burr-block-lincoln','Burr Block','Lincoln','ne','civic','standing',40.81389,-96.70381,'exact','view','walk','','1887, 1916',
  "An office block at 12th and O streets, built in 1887 to James Tyler's design as a six-storey Victorian building with turrets and an onion dome on its rounded corner. In 1916 four storeys were added and the front made over into a ten-storey skyscraper, probably by Berlinghof and Davis. For more than forty years it was the home office of an insurance company; it has also been called the Security Mutual, Veterans Administration and Anderson Building.",
  look="A ten-storey block on the corner, stone being its main material (Register form, 1979). Present use not checked.",
  accn="At 1206 O Street, downtown. Privately owned: see it from O and 12th streets. Downtown street and pay parking nearby (not checked).",
  links=[W('Burr Block'),['National Register nomination (1979)',NR+'79001448_text']],
  brick='?'),
N('federal-trust-building-lincoln','Federal Trust Building','Lincoln','ne','civic','standing',40.81275,-96.70227,'exact','view','walk','','1926–1927',
  "A twelve-storey Gothic Revival office building of 1926 to 1927, built by the Olson Construction Company for the Federal Trust Company and designed by Meginnis and Schaumberg. It has been on the National Register since 2002.",
  look="A tall Gothic-detailed office tower at 13th Street just south of O Street. Interior not checked.",
  accn="At 134 South 13th Street, downtown. Privately owned offices: see it from the street. Downtown street and pay parking nearby (not checked).",
  links=[W('Federal Trust Building'),['National Register record',REC+'02000409']],
  brick='?'),
N('pioneers-park-treasury-columns-lincoln','Treasury Building columns, Pioneers Park','Lincoln','ne','curio','standing',40.77917,-96.75712,'site','public','walk','','',
  "Four Ionic sandstone columns taken down from the U.S. Treasury Building in Washington and given to Lincoln: the park's Register form says they came off the Treasury in 1908 and were given in 1916 by a friend of William Jennings Bryan, while the city's park page says they were given in 1907. They stood at the O Street entrance of Antelope Park for decades, were put in store when that land was sold, and were set up in Pioneers Park in 1976 as a bicentennial project, as a picturesque 'ruin' beside the pond.",
  look="Four free-standing columns with benches, paths and plaques, near the middle of an allee just west of a pond in the formal east part of the park, which was laid out by Ernst Herminghaus about 1930.",
  accn="Pioneers Park, 3201 South Coddington Avenue, is a City of Lincoln park, open daily 5 a.m. to 11 p.m. (city page). No alcohol in the park. Parking along the park roads (not checked). The pin is the columns as mapped in OpenStreetMap, on a small rise beside the pond.",
  links=[['City of Lincoln: Pioneers Park','https://www.lincoln.ne.gov/City/Departments/Parks-and-Recreation/Parks-Facilities/Parks-A-to-Z/Pioneers-Park'],['National Register nomination: Pioneers Park (1993)',NR+'93000538_text']],
  conf='mixed',
  brick='no',bcol='none',hours='Park open daily 5 a.m. to 11 p.m.'),
N('first-plymouth-church-lincoln','First-Plymouth Congregational Church','Lincoln','ne','worship','standing',40.8031,-96.692,'exact','open','walk','','1929–1931',
  "The church of the congregation formed when First and Plymouth Congregational churches joined in 1923. The building was designed by H. Van Buren Magonigle of New York, a finalist in the State Capitol competition, and dedicated in April 1931. SAH Archipedia calls it one of Lincoln's finest religious and architectural landmarks; its plan was loosely modelled on a farmstead, with the worship hall as the barn and the tower as the silo.",
  look="Walls of brick in old rose and tawny gold, an arcaded forecourt and a 171-foot, sixteen-sided carillon tower with the four evangelists on its corner buttresses. Set in the tower base are a stone from Martin Luther's birthplace in Eisleben and one from Plymouth, England. Inside, a barrel-vaulted nave with large round-arched windows, a carved Lord's Prayer over the altar and an organ of about 6,000 pipes (SAH Archipedia). A chapel was added in 1966 to 1968 and a wing in 1989 to 1994.",
  accn="At 2000 D Street (20th and D). An active church: visitors are welcome at its services (times from the church's own site). Street parking nearby (not checked).",
  links=[['SAH Archipedia: First-Plymouth Congregational Church','https://sah-archipedia.org/node/16190'],['First-Plymouth Church','https://firstplymouth.org/']],
  brick='?',hours='Services Saturday 5:30 p.m.; Sunday 8:15, 9, 10:30 and 11:57 a.m.; Wednesday 5:30 p.m.'),
N('lincoln-va-hospital-historic-district','Lincoln Veterans Administration Hospital','Lincoln','ne','inst','standing',40.80788,-96.62163,'site','view','drive','','1930',
  "A veterans' hospital campus of 1930 on South 70th Street, built by the Veterans Bureau's construction service in the Colonial and Classical Revival manner. Its Register form counts nineteen historic buildings, among them the monumental main building, the general medical building, the kitchen and boiler plant, a recreation hall of about 1934 and staff quarters. A 1983 clinic addition joined three of them into one. A 2015 city plan and preservation agreement opened the old campus to redevelopment, with the old hospital building to be kept; how far that has gone was not checked.",
  look="Brick buildings with slate roofs and terra-cotta trim round a lawn, the main building facing west to 70th Street (Register form, 2012). The present use of each building was not checked.",
  accn="At 600 South 70th Street, about 500 feet south of O Street. Federal and redeveloped land: see it from 70th Street; do not go into buildings or closed areas. Parking not checked.",
  links=[['National Register nomination (2012)',NR+'12000785_text'],['City of Lincoln: VA campus redevelopment plan (2015)','https://www.lincoln.ne.gov/files/sharedassets/public/urban-development/redevelopment/va-campus-redev-plan.pdf']],
  conf='mixed',brick='yes',bcol='red'),
]

PIN_NOTES={
 'old-city-hall-lincoln-ne':'Wikipedia Register-list point; on the building at the south end of Government Square on the aerial.',
 'grand-manse-lincoln-ne':'ArcGIS PointAddress for 129 N 10th St; on the long building on the north half of Government Square on the aerial.',
 'architecture-hall-unl-lincoln':'Wikipedia Register-list point for the Old University Library; on the building at 11th and R on the aerial.',
 'temple-building-unl-lincoln':'ArcGIS PointAddress for 1209 R St (12th and R); checked on the aerial.',
 'nebraska-coliseum-lincoln':'Coordinate from the Wikipedia article; checked on the aerial.',
 'old-main-nebraska-wesleyan-lincoln':'ArcGIS PointAddress for 5000 St Paul Ave, beside the Register point; checked on the aerial.',
 'burr-block-lincoln':'Wikipedia Register-list point at 12th and O; checked on the aerial.',
 'federal-trust-building-lincoln':'ArcGIS PointAddress for 134 S 13th St, inside the OpenStreetMap outline named Federal Trust; checked on the aerial.',
 'pioneers-park-treasury-columns-lincoln':'OpenStreetMap point named Columns in Pioneers Park; checked on the aerial.',
 'first-plymouth-church-lincoln':'ArcGIS PointAddress for 2000 D St; checked on the aerial.',
 'lincoln-va-hospital-historic-district':'ArcGIS PointAddress for 600 S 70th St; checked on the aerial.',
}
