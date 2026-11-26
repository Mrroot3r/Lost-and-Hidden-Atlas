# November 26, 2026: Springfield, Ohio (Clark County). A "videos" session (PROMPTS.md job 9): the names came from one
# video's tour of old Springfield buildings (the record is source/videos/20240320_HZot3PrV83M.md); the video is a tip and
# nothing here rests on it. Sources read: Wikipedia (each article named in the links) and the National Register list for
# Clark County; the Clark County Historical Society's own pages (the building, the society's history, plan your visit);
# SAH Archipedia for the Bushnell House; the Westcott House audio-tour page for the Bushnell Building; Wittenberg
# University's pages for Recitation Hall; the herr2ck architecture blog for the Odd Fellows' Home's later changes; the
# St. Rose Family of Parishes bulletin of October 18, 2026 for St. Raphael's Mass times. Pins are ArcGIS address points,
# each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'springfield_esac','label':'Ohio: old Springfield, the Champion City','added':'2026-11-26 10:35'}

DT=' OpenStreetMap maps several parking lots within a few hundred metres downtown; their owners, hours and fees were not checked.'

PLACES=[

N('clark-county-courthouse-springfield-oh','Clark County Courthouse','Springfield','oh','civic','standing',39.92602,-83.8085,'exact','view','walk','','1878; rebuilt 1918–1924',
  'The third courthouse for Clark County, built over the foundations of the second. That second courthouse, by Thomas J. Tolan & Son of Fort Wayne, went up after the first (a red brick building finished in 1828) was sold for $50 in 1878 and pulled down. Fire broke out about 1 a.m. on March 12, 1918 and gutted it; the county rebuilt it from 1918 to 1924, saving and reusing parts of the outer walls.',
  'A mix of old and new: the fire took the big front tower, the stairs and the mansard roof, and a low dome now sits in the middle of the roof, partly hidden behind the entablature. Interior and public hours not checked.',
  '',
  'Owned by Clark County, at the northwest corner of North Limestone and East Columbia streets; seen from the street.'+DT,
  [W('Clark County Courthouse (Ohio)')],
  brick='?'),

N('clark-county-heritage-center','City Hall and Market (Clark County Heritage Center)','Springfield','oh','civic','standing',39.92283,-83.81064,'exact','open','walk','','1890',
  'Springfield\'s city hall and market house of 1890, by the Springfield architect Charles A. Cregar: city offices, a council chamber, an opera house and a farmers\' market under one roof, 462 feet long. The city moved to a new city hall in 1979; when the old building faced demolition in 1990, city, county and the Clark County Historical Society saved it, and the society moved in in March 2001. On the National Register as the Municipal Building.',
  'Richardsonian Romanesque, red brick with stone trim, with a stone tower at each end: the east one rises four storeys above the roof and the west one three. Inside are the historical society\'s museum (over 13,000 square feet of exhibits), its library and archives, and a cafe.',
  '',
  'Run by the Clark County Historical Society at 117 South Fountain Avenue. Admission to the museum is free, with a suggested donation; the library and archives (Wednesday to Friday and Saturday) are by appointment only. The society\'s own lot is reached from South Fountain Avenue and South Center Street. The society\'s page said it was closed for Thanksgiving, November 25 to 28, 2026.',
  [W('Clark County Heritage Center'),['Clark County Historical Society: the building','https://heritage.center/the-building/'],['Plan your visit','https://heritage.center/plan-your-visit/']],
  th=[39.92253,-83.81124],thn='Parking lot off South Fountain Avenue (OpenStreetMap; the society names its lot here)',
  brick='yes',hours='Museum Tuesday to Friday 9 a.m. to 4 p.m., Saturday 9 a.m. to 3 p.m.'),

N('st-raphael-church-springfield-oh','St. Raphael\'s Catholic Church','Springfield','oh','worship','standing',39.92292,-83.80618,'exact','open','walk','','1892–1898',
  'Springfield\'s first Catholic parish, set up in 1849. Its first small brick church was pulled down in early 1892 and this one took six years to build; the Archbishop of Cincinnati consecrated it on July 17, 1898. The architect was Charles A. Cregar, the first Springfield-born architect. On the National Register.',
  'High Gothic Revival in Berea sandstone, with two front towers of 135 and 184 feet that stand out on the city skyline; Gothic stained glass, including a Crucifixion window in the apse.',
  '',
  'An active parish church at 225 East High Street, part of the St. Rose Family of Parishes; Mass times are from the parish bulletin of October 18, 2026. Street parking.'+DT,
  [W('St. Raphael\'s Catholic Church (Springfield, Ohio)'),['Parish bulletin, October 18, 2026','https://irp.cdn-website.com/688904a6/files/uploaded/20261018.pdf']],
  brick='no',hours='Sunday Mass 10:30 a.m. and 3:30 p.m. (Haitian Creole); Wednesday and Thursday 12:10 p.m.'),

N('st-johns-lutheran-springfield-oh','St. John\'s Evangelical Lutheran Church','Springfield','oh','worship','standing',39.92581,-83.81435,'exact','view','walk','','1895–1897',
  'A German Lutheran congregation formed in 1845. The cornerstone of this church was laid on November 3, 1895 and it was consecrated on April 26, 1897. The architect was Charles A. Cregar, who also drew the city hall and St. Raphael\'s. The congregation, now in the Evangelical Lutheran Church in America, still uses the building, which is on the National Register.',
  'Romanesque Revival with a tall corner tower over the main door, the walls mostly brick with plenty of limestone and other stone; two great gabled fronts on the corner each hold a very large window. Interior not checked.',
  '',
  'An active church at 27 North Wittenberg Avenue; seen from the street. No page of its own giving service times could be read when this was written.'+DT,
  [W('St. John\'s Evangelical Lutheran Church (Springfield, Ohio)')],
  brick='?'),

N('bushnell-building-springfield-oh','Bushnell Building','Springfield','oh','civic','standing',39.92499,-83.80952,'exact','view','walk','','1893',
  'A downtown block commissioned by Asa S. Bushnell, partner in the farm-machine makers Warder, Bushnell & Glessner and governor of Ohio from 1896 to 1900, and designed by Shepley, Rutan and Coolidge, the successors to H. H. Richardson. Finished in 1893, it held the First National Bank and a dry-goods store on the ground floor, offices above, and the first Springfield Masonic Temple on the fifth floor; it is best known for Wren\'s department store. Part of the Main Street Buildings listing on the National Register.',
  'Three-storey arches and mixed stone with Second Renaissance Revival symmetry; terra-cotta panels of cherubs and swags of fruit over the second and third floor windows, lion heads on the cornice, and two stone wreaths beside the middle arch with Bushnell\'s initials and the year it was finished. Interior not checked.',
  '',
  'A privately owned building at 14 East Main Street, on the central square; seen from the street.'+DT,
  [['Westcott House: Bushnell Building','https://www.westcotthouse.org/node/2730']],
  brick='?'),

N('bushnell-house-springfield-oh','Asa S. and Ellen L. Bushnell House','Springfield','oh','landmark','standing',39.92157,-83.79647,'exact','ask','walk','','1886–1888',
  'The house of Asa Bushnell, later governor of Ohio, on a three-acre ridge on East High Street, then the town\'s best address. Richardson had died and his successors were taking no new clients, so the Bushnells hired the New York architect Robert H. Robertson; Richardson\'s builders, the Norcross Brothers, put it up, and it was finished in the autumn of 1888, the first Richardsonian Romanesque building in Springfield. After Bushnell died in 1904 it stayed a house until the 1930s, when it became a funeral home.',
  'Rock-faced blue Ohio River limestone with red East Longmeadow sandstone trim and arches, turrets, tall chimneys and a porte-cochere; a limestone wall capped with red sandstone along East High and Walnut streets. A carriage house and a shingled caretaker\'s house by the same architect stand on the grounds. In the East High Street Historic District.',
  '',
  'Now the Richards, Raff and Dunbar Memorial Home, a working funeral home at 838 East High Street; SAH Archipedia says architectural tours are given by appointment. Otherwise seen from the street; be considerate during services. Street parking.',
  [['SAH Archipedia: Asa S. and Ellen L. Bushnell House','https://sah-archipedia.org/node/79157'],W('East High Street Historic District (Springfield, Ohio)')],
  brick='no'),

N('warder-public-library-springfield-oh','Warder Public Library','Springfield','oh','civic','standing',39.9228,-83.80722,'exact','view','walk','','1890',
  'A gift to the city from Benjamin H. Warder of the Champion harvester firm, in memory of his parents, dedicated June 12, 1890. Shepley, Rutan and Coolidge, Richardson\'s successors, designed it; its plan follows Richardson\'s library at Malden, Massachusetts. It was the main library for Clark County until 1989 and now houses the Clark County (Warder) Literacy Center. On the National Register since 1978.',
  'An L-shaped Richardsonian Romanesque building of buff Ohio sandstone trimmed with Worcester brownstone under an orange clay tile roof, with an arcaded entrance porch and a stair tower where the wings meet; the old reading room has a stone fireplace 18 feet tall. Interior not checked.',
  '',
  'At the southwest corner of East High Street and Spring Avenue, now the literacy center; seen from the street. Opening hours not checked.'+DT,
  [W('Warder Public Library')],
  brick='no'),

N('odd-fellows-home-springfield-oh','Odd Fellows\' Home for Orphans, Indigent and Aged','Springfield','oh','inst','standing',39.94025,-83.79988,'exact','view','drive','','1898',
  'A home built by the Odd Fellows for orphans and old members, designed by Yost & Packard of Columbus and opened in 1898, in a mix of Renaissance and Chateauesque. Additions followed in 1906 and 1907, a hospital in 1916 and a nursery in 1925. On the National Register since 1980. A renovation in 1987 and 1988 took down the 1907 wings, the hospital and parts of the first building for new wings, according to a 2025 architecture blog; the same blog says it is used for assisted living.',
  'The south front of the 1898 building is the part that keeps its first look: two hexagonal towers with tall conical roofs, a steep roof and a central dormer, hood moulds over the arched windows. Interior not checked.',
  '',
  'Private, at 404 East McCreight Avenue, on a lawn back from the street; who runs it now was not checked. Seen from the street only. Street parking.',
  [W('Odd Fellows\' Home for Orphans, Indigent and Aged'),['herr2ck: To Relieve the Distressed','https://herr2ck.blogspot.com/2025/11/to-relieve-distressed.html']],
  brick='?',conf='mixed'),

N('recitation-hall-wittenberg','Recitation Hall, Wittenberg University','Springfield','oh','inst','standing',39.93405,-83.81547,'exact','view','walk','','1883–1886',
  'The second building on Wittenberg\'s campus. The cornerstone was laid on May 24, 1883, classes began in it that year, and it was formally dedicated on June 16, 1886. It held classrooms, the college literary societies and the first campus chapel. It is now the university\'s main administration building, with an annex added behind it in the 1950s. Within the Wittenberg University Historic District on the National Register.',
  'A big old hall on West Campus Drive, in the oldest part of the campus. Interior not checked.',
  '',
  'Owned by Wittenberg University, 3 West Campus Drive; seen from the campus drives. Visitor parking on campus not checked.',
  [['Wittenberg University: Recitation Hall','https://wittenberg.edu/node/8409'],['Wittenberg University: historical timeline','https://wittenberg.edu/node/7874']],
  brick='?'),

]

PIN_NOTES={
 'clark-county-courthouse-springfield-oh':'ArcGIS address point for 101 North Limestone Street; the Wikipedia coordinate is about 400 m east of the corner the article names.',
 'clark-county-heritage-center':'ArcGIS address point for 117 South Fountain Avenue; agrees with the Wikipedia coordinate.',
 'st-raphael-church-springfield-oh':'ArcGIS address point for 225 East High Street; agrees with the Register list point.',
 'st-johns-lutheran-springfield-oh':'ArcGIS address point for 27 North Wittenberg Avenue; agrees with the Register list point.',
 'bushnell-building-springfield-oh':'ArcGIS address point for 14 East Main Street.',
 'bushnell-house-springfield-oh':'ArcGIS address point for 838 East High Street.',
 'warder-public-library-springfield-oh':'ArcGIS address point; agrees with the Wikipedia coordinate for the corner of High Street and Spring Avenue.',
 'odd-fellows-home-springfield-oh':'ArcGIS address point for 404 East McCreight Avenue.',
 'recitation-hall-wittenberg':'ArcGIS address point for 3 West Campus Drive.',
}
