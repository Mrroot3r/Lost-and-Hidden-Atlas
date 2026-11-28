# November 28, 2026: Lynn, Massachusetts: standing buildings named in a video about the city's old buildings, each
# checked against sources opened for this batch (the video itself is only a tip). Sources read: the National Register
# records and nomination forms (National Park Service), Wikipedia (the Lynn Register list and the buildings' own
# articles), SAH Archipedia (Buildings of Massachusetts), the City of Lynn's library page and Washington Street Baptist
# Church's own page. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W

def L(t,u):
    return [t,u]

def NR(n):
    return ['National Register record '+n,'https://npgallery.nps.gov/AssetDetail/NRIS/'+n]

BATCH={'key':'lynnvid_ndvk','label':'Massachusetts: Lynn, buildings named in a video','added':'2026-11-28 14:32'}

DT='Downtown Lynn, on a city street. Metered street parking and city lots round Central Square, and the MBTA garage at Lynn station on Union Street, a few minutes\' walk.'
CM='On Lynn Common, a city park open to all. Street parking on North and South Common Streets; the MBTA garage at Lynn station on Union Street is about ten minutes\' walk east.'
SAH='https://sah-archipedia.org/node/13862'

PLACES=[
N('lynn-armory','Lynn Armory','Lynn','nshore','fort','standing',42.46347,-70.95431,'exact','view','walk','','1893',
  'A state armory for Lynn\'s militia companies, built in 1893 to plans by the Lynn firm of Wheeler and Northend to replace the Franklin Street armory of 1888. A head house with round corner towers and a crenellated parapet, made to look like a fortified castle, fronts a drill shed about 140 feet long. The Register form of 1979 calls it among the best Romanesque Revival buildings in the city and in original condition. In August 2018 a state law approved its sale to a nonprofit that planned to make it into apartments for military veterans.',
  'The castle front on South Common Street: two round towers 22 feet across, four stories high, a carved sandstone panel of the state seal on the northwest tower, and the long slate-roofed drill shed behind. The Register form describes pressed red brick with sandstone trim on a granite base; Wikipedia says it was built of red sandstone. Whether the apartments have been built was not checked. Interior not checked.',
  '','36 South Common Street, facing Lynn Common. Look from the street and the Common; whether anyone may go in was not checked. '+CM,
  [W('Lynn Armory'),NR('79000332'),L('SAH Archipedia: Lynn Common Historic District',SAH)],brick='yes',bcol='red',
  arch='Wheeler & Northend',archw='National Register record and form 79000332'),
N('high-rock-tower-lynn','High Rock Tower and High Rock Park','Lynn','nshore','landmark','standing',42.46807,-70.94643,'exact','public','walk','','1840s–1905',
  'High Rock is a porphyry hill above downtown Lynn with views to Boston, Nahant and Salem. In the 1840s Jesse Hutchinson of the Hutchinson Family Singers, an abolitionist singing group, bought the summit and built Gothic cottages and a wooden observation tower; Wikipedia says the tower burned during a celebration of the end of the Civil War. The present granite tower replaced it on land given to the city: the Register form says it was built by 1904 to plans by H. K. Wheeler and C. Betton of Lynn, and Wikipedia says it was completed in 1905 and dedicated on December 16. The park round it was laid out by the Olmsted Brothers in 1907, according to Wikipedia.',
  'A tapering square tower about 85 feet high of reddish granite rubble with gray granite quoins and crenellations, with a brick stair cylinder inside. Wikipedia says the tower was restored after 1998 with a new observatory on top, that the city opens the tower and its telescope to the public from time to time, and that it is lit by colored lights at night. Below it stand High Rock Cottage, of local porphyry (about 1847), and the wooden Daisy Cottage, both in the Register listing.',
  '','High Rock Park, a City of Lynn park off Essex Street, with granite stairs up from Essex Street to the foot of the tower. Street parking in the streets round the hill; the city lots on Buffum and Washington Streets downtown are a short, steep walk below. The cottages below the tower are not part of the park; look from the street. Opening nights for the tower and observatory were not checked.',
  [W('High Rock Tower Reservation'),NR('09000086')],brick='no',
  arch='H. K. Wheeler; C. Betton',archw='National Register form 09000086: the present tower designed by H. K. Wheeler and C. Betton of Lynn'),
N('lynn-public-library-common','Lynn Public Library','Lynn','nshore','civic','standing',42.46444,-70.95361,'exact','open','walk','','1898–1900',
  'Lynn\'s main library, built from 1898 to 1900 after a bequest of 1896, to a Renaissance Revival design by George A. Moore. Wikipedia says the choice of architect and the cutting of trees on the Common for the site were both argued over, and that the $175,000 cost included no public money. In 1900 the library commissioned the first mural of the painter F. Luis Mora.',
  'A two-and-a-half-story limestone building on a granite base with a two-story Corinthian portico of four columns, reached by granite stairs that spread three ways from the door. The Register form of 1979 calls it unaltered except for aluminum and glass entrance doors of about 1970. Inside, the form and Wikipedia were not read for what survives; interior not checked. It is a working public library.',
  '','5 North Common Street, run by the City of Lynn; open to the public during library hours (not checked: the city\'s page gives the address and telephone but no hours). '+CM,
  [W('Lynn Public Library'),NR('79000334'),L('City of Lynn: Public Library','https://lynnma.gov/city_government/departments/public_library')],brick='no',bcol='none',
  arch='George A. Moore',archw='National Register record 79000334; Wikipedia',hours='?'),
N('old-post-office-lynn','Old Post Office Building, Lynn','Lynn','nshore','civic','standing',42.46472,-70.94833,'site','view','walk','','1897–1898',
  'Lynn\'s post office from 1898 until a new one replaced it in the 1930s. The Register form says the site was chosen in 1895, a first Romanesque design by government architects was dropped, and the present design was accepted in July 1896 and built in 1897 and 1898. After the post office left it served as a Marine Corps armory and then as offices. The form calls it Renaissance Revival; Wikipedia calls it Colonial Revival.',
  'Two stories of yellow brick with glazed yellow terracotta trim on a granite basement. Its two round corner entrance bays, each with polished granite columns and marble Ionic capitals, are capped by high domes sheathed in copper embossed with a fish-scale pattern. The form says the outside was in original condition apart from the doors. Interior not checked.',
  '','360 Washington Street, an office building; look from the street. '+DT,
  [W('Old Post Office Building (Lynn, Massachusetts)'),NR('81000118')],brick='no',bcol='buff'),
N('st-stephens-memorial-church-lynn','St. Stephen\'s Memorial Episcopal Church','Lynn','nshore','worship','standing',42.46306,-70.95639,'exact','view','walk','','1881',
  'An Episcopal church on Lynn Common, built in 1881 to designs by Ware and Van Brunt of Boston. Enoch Reddington Mudge paid for it as a memorial to his children Charles, killed at Gettysburg in 1863, and Fanny. The cornerstone was laid on May 19, 1881 and the church dedicated on November 2, 1881; Mudge died in October, after looking over the interior decoration, and the family is buried in a closed courtyard between the church and the parish house.',
  'Walls of reddish granite from Mudge\'s Swampscott estate, trimmed with red brick and brown sandstone, under red slate roofs, with a tower 130 feet high facing the Common. The Register form of 1979 says the inside keeps its parquet and mosaic floors, hammer-beam trusses with carved timber ends, stencilled walls and stained glass; SAH Archipedia says some windows are by Tiffany. The original altar, font and brass lights are gone. Whether the church is open outside services was not checked.',
  '','74 South Common Street, an active parish of the Episcopal Diocese of Massachusetts. Service times were not checked. '+CM,
  [W('St. Stephen\'s Memorial Episcopal Church'),NR('79000335'),L('SAH Archipedia: Lynn Common Historic District',SAH)],brick='some',bcol='red',
  arch='Ware & Van Brunt',archw='National Register form 79000335; Wikipedia; SAH Archipedia'),
N('vamp-building-lynn','Vamp Building','Lynn','nshore','industry','standing',42.46250,-70.94722,'exact','view','walk','','1903–1907',
  'An eight-story shoe factory built for the Lynn Realty Company in 1903, to designs by Henry Warren Rogers, and enlarged until 1907 to fill a whole triangular block. Its V shape, like the vamp of a shoe, gave the name. The Register form says it was the largest factory the company built and was thought locally to be the largest shoe factory in the world. It was one of the few factories to come through the downtown fire of November 1981, losing its top floor; Wikipedia says its strong walls and new sprinklers helped stop the fire.',
  'A freestanding triangle of red brick with buff brick trim, eight stories, with full-height pilasters, paired windows under segmental arches and a courtyard opening on the inside of the V. The form says the windows are replacements from a rehabilitation. Interior not checked.',
  '','3 to 15 Liberty Square, at Broad and Union Streets; a private building, look from the street. '+DT,
  [W('Vamp Building'),NR('83000587')],brick='yes',bcol='red',
  arch='Henry Warren Rogers',archw='National Register record 83000587; Wikipedia'),
N('mowers-block-lynn','Mowers\' Block','Lynn','nshore','industry','standing',42.46417,-70.94556,'site','view','walk','','1891',
  'A six-story shoe factory and commercial block built in 1891 for Mower and Brother, ladies\' shoe makers, on the site of their brick factory in which the Great Fire of November 26, 1889 began; that fire destroyed most of Lynn\'s business district. Wikipedia says it was the largest building in the burned area when it was finished. The Register form says it is the best kept of the many factories designed by Edwin Earp of Lynn in the 1880s and 1890s.',
  'Six stories of brick at Willow and Blake Streets: fluted cast-iron posts round the shop windows, round brick arches on rock-faced granite springers, decorative brick panels and a corbelled top. The form calls the design Victorian Gothic (panel brick) and nearly all original. Interior not checked.',
  '','7 Willow Street and Blake Street, at the west end of Central Square; a private building, look from the street. '+DT,
  [W('Mowers\' Block'),NR('82001991'),W('Central Square Historic District (Lynn, Massachusetts)')],brick='?',
  arch='Edwin Earp',archw='National Register record and form 82001991'),
N('english-high-school-lynn','English High School (former), Lynn','Lynn','nshore','civic','standing',42.46640,-70.94710,'site','view','walk','','1892–1924',
  'Lynn\'s second high school, built in 1892 to designs by Wheeler and Northend across Liberty Street from the first one. A wing in matching style was added in 1916. Wikipedia says a fire on March 29, 1924 destroyed the original 1892 front, which was replaced the same year by the present Jacobethan block by George A. Cornet. It was the high school until 1932, then a junior high school (Cobbet Junior High) until the city closed it in 1980, and Wikipedia says it has since become housing.',
  'Three parts of brick at Essex and Liberty Streets: the 1924 front block with a Tudor-arched entrance pavilion, parapets and panels carved with owls, and behind it a four-story section with buttresses and a corbelled brick cornice. The Register form is not clear on how much of the 1892 school survives; Wikipedia says the oldest portion was Romanesque. Interior not checked.',
  '','498 Essex Street, now private housing; look from the street. '+DT,
  [W('English High School (1892 building)'),NR('86002508')],brick='yes',bcol='red',conf='mixed',
  arch='Wheeler & Northend; George A. Cornet',archw='National Register record 86002508; Wikipedia: Wheeler & Northend for 1892, George A. Cornet for 1924'),
N('old-lynn-high-school','Old Lynn High School','Lynn','nshore','civic','standing',42.46639,-70.94592,'exact','view','walk','','1850–1876',
  'Lynn\'s first high school, a two-story wooden Italianate building of 1850 that opened in 1851 and was lengthened by three bays in 1876. After the English High School opened across Liberty Street in 1892 it became that school\'s vocational shop, and from 1924 to 1975 it held the Lynn Independent Industrial Shoemaking School. Wikipedia says it stood empty and was damaged by vandals and an attempted arson before it was rehabilitated and enlarged; it is now the home of Girls Incorporated of Lynn.',
  'A long two-story wooden schoolhouse on a rise above downtown. Wikipedia says the second floor still shows the three original classrooms either side of a central hall. Interior not checked by a visit.',
  '','50 High Street, home of a youth organization; look from the street. '+DT,
  [W('Old Lynn High School'),NR('02000130')],brick='no',bcol='none',
  apart='english-high-school-lynn: the first high school of 1850 and the second of 1892 are two buildings on opposite sides of Liberty Street'),
N('lynn-masonic-hall-ymca','Lynn Masonic Hall (old YMCA building)','Lynn','nshore','civic','standing',42.46333,-70.94972,'site','view','walk','','1880–1881',
  'Built in 1880 and 1881 for the Lynn YMCA to a competition design by H. J. Preston of Boston, and claimed at the time as the first building in Massachusetts built for a YMCA. The Masons bought it in 1922. The Register form of 1979 says it is the last large Victorian Gothic building in downtown Lynn: the others were lost in the fire of 1889 or pulled down in the 1960s and 1970s.',
  'A four-story block at Market and Liberty Streets of pressed brick with buff sandstone trim, pointed-arch wall panels and cast-iron cresting between the chimneys; a slate hip roof covers the old auditorium. The ground-floor shop fronts and doors are modern. What the building is used for now was not checked. Interior not checked.',
  '','64 to 68 Market Street, at Liberty Street; a private building, look from the street. '+DT,
  [W('Lynn Masonic Hall'),NR('79000333'),L('SAH Archipedia: Market Street District','https://sah-archipedia.org/node/13867')],brick='?',
  arch='Henry J. Preston',archw='National Register record and form 79000333; SAH Archipedia'),
]

PIN_NOTES={
'lynn-armory':"Wikipedia's coordinate; on the 2023 aerial it falls on the armory's head house on South Common Street.",
'high-rock-tower-lynn':"The National Register list's coordinate fell on the round summit plaza; moved about 60 m southeast onto the square tower, which shows on the 2023 aerial with its long shadow.",
'lynn-public-library-common':"Wikipedia's coordinate; on the 2023 aerial it falls on the library's pale roof on North Common Street.",
'old-post-office-lynn':"Wikipedia's coordinate; on the 2023 aerial it falls at the edge of a building among downtown blocks, so the pin marks the site.",
'st-stephens-memorial-church-lynn':"Wikipedia's coordinate; on the 2023 aerial it falls on the church's red slate roofs facing the Common.",
'vamp-building-lynn':"Wikipedia's coordinate; on the 2023 aerial it falls on a large dark-roofed block beside the railroad viaduct at Liberty Square.",
'mowers-block-lynn':"Wikipedia's coordinate; on the 2023 aerial it falls on the street at the west end of Central Square, so the pin marks the site.",
'english-high-school-lynn':"The National Register list's coordinate; on the 2023 aerial it falls on a large building at Essex and Liberty Streets.",
'old-lynn-high-school':"Wikipedia's coordinate; on the 2023 aerial it falls on a building on the rise of High Street.",
'lynn-masonic-hall-ymca':"The National Register list's coordinate; on the 2023 aerial it falls in the street at Market and Liberty Streets, so the pin marks the site.",
}
