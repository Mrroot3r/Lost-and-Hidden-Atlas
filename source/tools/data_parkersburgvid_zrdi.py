# November 28, 2026: Parkersburg, West Virginia (Wood County). Buildings named in an Old World Exploration video about the
# city, researched as leads. The video is a tip only; every fact below comes from the sources linked on each place:
# Wikipedia articles, the National Register records and forms (NPGallery), SAH Archipedia's Buildings of West Virginia
# entries, the 2023 Downtown Parkersburg Historic District nomination (WV Culture), and the pages of the hotel, the
# churches and Wood County. Interiors were not visited by any source opened unless the entry says so.
from data_b import N
from data_ma import W

BATCH={'key':'parkersburgvid_zrdi','label':'Parkersburg, West Virginia: from a video walk-through','added':'2026-11-28 08:45'}

def NR(ref): return ['National Register record '+ref,'https://npgallery.nps.gov/AssetDetail/NRIS/'+ref]
def SAH(t,n): return ['SAH Archipedia: '+t,'https://sah-archipedia.org/node/'+n]
DPHD=['Downtown Parkersburg Historic District nomination (2023)','https://wvculture.org/wp-content/uploads/2023/11/WV_WoodCo_DowntownParkersburgHistoricDistrict_Form.pdf']
DOWNTOWN='Downtown Parkersburg: street parking and city lots and garages nearby (OpenStreetMap maps the Towne Square Garage on Juliana Street, by 4th Street); rates not checked.'

PLACES=[
N('blennerhassett-hotel-parkersburg','Blennerhassett Hotel','Parkersburg','wv','hotel','standing',39.26484,-81.56150,'exact','open','drive','hotels','1883–1889',
  'A Queen Anne hotel at Market and 4th streets, built by the Parkersburg businessman William Nelson Chancellor in the oil and gas boom. Work began in 1883 and it opened on May 6, 1889, with about fifty guest rooms round a central staircase; the rounded ground-floor corner held the First National Bank. It stood empty for several years before it was listed on the National Register in 1982, and was refurbished, enlarged and reopened in 1986. It is still a working hotel.',
  'Four storeys of brick trimmed with stone, the southern bay rising to five, with a mansard roof, Chateauesque dormers, gables and a round corner tower with a conical roof and finial; corbelled cornice and brick and terra cotta ornament (Register form; the 2023 district nomination). A three-storey addition stands on 4th Street. The ground floor was remodelled long ago (the 1982 form mentions an Art Deco corner entrance). The hotel says it has 82 rooms and suites, a spa and restaurants in the one 1889 building; the lobby and public rooms were not checked for original fabric.',
  'Six years to build, and still taking guests.',
  'A privately owned working hotel; the public rooms and restaurants are open to guests and diners. '+DOWNTOWN,
  [W('Blennerhassett Hotel'),NR('82001768'),SAH('Blennerhassett Hotel','22847'),DPHD,['The Blennerhassett (hotel)','https://theblennerhassett.com/']],
  th=[39.26550,-81.56243],thn='Towne Square Garage, Juliana Street',brick='yes',bcol='red',
  hours='Working hotel, open year-round; restaurant and spa hours not checked',
  arch='William Nelson Chancellor',archw='Wikipedia: "Designed and built by William Chancellor"; the 2023 district nomination says it was built by Colonel William Nelson Chancellor'),

N('wood-county-courthouse-parkersburg','Wood County Courthouse','Parkersburg','wv','civic','standing',39.26472,-81.56278,'site','open','drive','','1899–1901',
  'Wood County\'s fifth courthouse and the third on Court Square, built in 1899 to 1901 to plans by L. W. Thomas of Canton, Ohio, by the local contractors Caldwell & Drake, for about $100,000. Its cornerstone was laid in the county\'s centennial year. It was modelled on H. H. Richardson\'s Allegheny County Courthouse in Pittsburgh. Urban renewal threatened it in the 1970s, when a survey team documented it for the Historic American Buildings Survey, and it was kept. The steeple taken off its tower in 1952 was replaced in July 2020.',
  'Richardsonian Romanesque in quarry-faced sandstone from nearby Quincy Street Hill, laid in broad and narrow bands, with a central tower over the main entrance, now topped again by a steeple (Wikipedia gives the height as 164 feet). Look for the two carved figures under the rounded two-storey oriels over the side entrances, a woman on the southwest side and a bearded man on the northeast (SAH Archipedia). In front of the Market Square entrance is the 1899 memorial fountain with a bronze bust of J. J. Jackson by the sculptor J. Massey Rhind (district nomination). Two courtrooms are on the second floor; the interior was not otherwise checked.',
  'A small-town copy of Richardson\'s Pittsburgh courthouse, saved from urban renewal.',
  'Wood County\'s working courthouse, 1 Court Square. The county offices inside keep weekday hours (Wood County Clerk\'s page, read November 28, 2026); expect a security check at the door. '+DOWNTOWN,
  [W('Wood County Courthouse (West Virginia)'),NR('79002606'),SAH('Wood County Courthouse','22822'),DPHD,['Wood County: County Clerk','https://www.woodcountywv.com/county-clerk']],
  brick='no',hours='Monday to Friday 8:30 a.m. to 4:30 p.m. (county offices)',
  arch='L. W. Thomas',builder='Caldwell & Drake',archw='Wikipedia: built "by local contractors Caldwell & Drake, according to the plans of architect L. W. Thomas of Canton, Ohio"; SAH Archipedia names L. W. Thomas'),

N('trinity-episcopal-church-parkersburg','Trinity Episcopal Church','Parkersburg','wv','worship','standing',39.26630,-81.56126,'exact','open','drive','','1878–1879',
  'An Episcopal parish formed in the 1840s, whose first church (finished 1850) was pulled down in 1878 for this stone Gothic church by A. C. Nash of Cincinnati, consecrated in 1879 and lengthened in 1898. The 1913 flood ruined its organ, furnaces and floor. Beside it stand the mansard-roofed rectory of 1863, now the parish house, and Trinity Hall of 1881. For the 37 years Bishop George W. Peterkin lived in Parkersburg it served unofficially as the cathedral of the new Diocese of West Virginia.',
  'Rock-faced stone with a corner tower, turrets, large and small rose windows and a flying buttress; the entrance is a gabled porch below the buttress, not the tower (SAH Archipedia; Register form). Inside (SAH Archipedia): an open hammer-beam ceiling, Victorian stained glass, ranks of organ pipes and Gothic woodwork of native pine. The parish house on the corner of Juliana and 5th streets has a cast-iron porch.',
  'The church that served as West Virginia\'s first cathedral, unofficially.',
  'An active Episcopal parish, 430 Juliana Street. Anyone may come to its services (times from the parish\'s own page, read November 28, 2026). '+DOWNTOWN,
  [W('Trinity Episcopal Church (Parkersburg, West Virginia)'),NR('82001790'),SAH('Trinity Episcopal Church','22845'),['Trinity Episcopal Church (parish page)','https://trinity-church.org']],
  brick='no',hours='Holy Eucharist Sunday 8 and 10:30 a.m., Wednesday 12:15 p.m., Saturday 5:30 p.m.',
  arch='A. C. Nash',archw='National Register record and SAH Archipedia name A. C. Nash (of Cincinnati, per the Register form)'),

N('st-francis-xavier-church-parkersburg','St. Francis Xavier Church','Parkersburg','wv','worship','standing',39.26618,-81.55927,'exact','open','drive','','1867–1870',
  'The Catholic church of Parkersburg, one of the four original churches of the Diocese of Wheeling. It replaced a small brick church of 1849. Patrick C. Keely of Brooklyn drew this Romanesque Revival church, Lysander Dudley built it, and work begun in 1867 was slowed for 18 months by the shortage of materials after the Civil War; the cornerstone was laid on May 9, 1869 and the church dedicated on October 2, 1870. Wikipedia calls it the oldest church building in the city. Its present belfry and domed cupola date from 1915, built for a 3,000-pound bell.',
  'A large brick church whose tower, with the main door at its base, dominates downtown (SAH Archipedia). Inside: seven trompe-l\'oeil murals in the apse and side altars painted about 1870 by Daniel Muller of Munich, which look like white relief sculpture on a pale blue ground, a stained glass half-dome over the altar, and Joseph Daris\'s carved confessionals, altar and communion rail. Most of the windows are by the G. C. Riordan Company of Cincinnati, put in after an 1895 riverboat explosion broke the first ones. The 1978 restoration put in pews copied from the originals.',
  'Murals that look carved, by a Munich painter, in a river-town church.',
  'An active Catholic parish, 532 Market Street (parish office across the street at 609 Market). Anyone may attend Mass; times from the parish\'s own page, read November 28, 2026. '+DOWNTOWN,
  [W('St. Francis Xavier Church (Parkersburg, West Virginia)'),NR('78002813'),SAH('St. Francis Xavier Roman Catholic Church','22849'),['St. Francis Xavier parish','https://www.stx-pburg.org']],
  brick='yes',bcol='red',hours='Mass Saturday 5 p.m.; Sunday 10:30 a.m. and 5 p.m.; Monday and Friday 12:10 p.m.; Tuesday and Thursday 8 a.m.; Wednesday 7 p.m.',
  arch='Patrick Charles Keely',builder='Lysander Dudley',archw='SAH Archipedia: "Patrick C. Keely, architect; Lysander Dudley, builder"; Wikipedia also names Keely'),

N('first-baptist-church-parkersburg','First Baptist Church','Parkersburg','wv','worship','standing',39.26790,-81.55689,'exact','view','drive','','1871–1877',
  'A Baptist congregation founded in 1817 built its first church here in 1837 and this one from 1871. Lysander Dudley, who had just finished St. Francis Xavier and was a deacon here, brought plans of a new church in his old home town of Wallingford, Connecticut; he was killed by a runaway wagon as building began. It is a two-storey brick church in the round-arched German manner called Rundbogenstil (SAH Archipedia; Wikipedia calls it Italianate).',
  'Brick, three bays by six, with round-arched windows and doors, heavy lintels and a corbelled cornice, a central steeple and a corner turret (Wikipedia; SAH Archipedia). The steeple is a 1973 aluminium copy of the original wooden one, taken down as unsafe. The auditorium has been remodelled several times and the Christian Education Building was added at the back in 1958 to 1959. Interior not checked.',
  'Built from a Connecticut church\'s plans by a man who died as it began.',
  'An active church at 813 Market Street (corner of 9th Street), in the Avery Street Historic District. View from the street; no page of the congregation\'s own giving service times was found. Street parking.',
  [W('First Baptist Church (Parkersburg, West Virginia)'),NR('82001774'),SAH('First Baptist Church','22850')],
  brick='yes',bcol='red',arch='Lysander Dudley',archw='SAH Archipedia names Lysander Dudley'),

N('first-presbyterian-church-parkersburg','First Presbyterian Church (St. Patrick\'s Anglican Church)','Parkersburg','wv','worship','standing',39.26845,-81.55496,'exact','view','drive','','1894',
  'A Presbyterian church of 1894 at 946 Market Street, later the Calvary Temple Evangelical Church, and since 2016 the home of St. Patrick\'s Anglican Church. It is two storeys of brick and stone in a mix of Romanesque and Gothic Revival, with a bell tower on the corner, and is part of the Avery Street Historic District. The 2023 downtown nomination says the Cincinnati architects Crapsey & Brown designed the Presbyterian church as well as the old City Building.',
  'Brick and stone walls and a corner bell tower (Wikipedia). Interior not checked.',
  '',
  'An active church; view from the street. Service times not checked. Street parking.',
  [W('First Presbyterian Church (Parkersburg, West Virginia)'),NR('82001775'),DPHD],
  brick='?'),

N('first-united-methodist-church-parkersburg','First United Methodist Church','Parkersburg','wv','worship','standing',39.26999,-81.55614,'exact','view','drive','','1909–1911',
  'A Neo-Gothic church of 1909 to 1911 by George W. Kramer at Juliana and 10th streets, the fifth building of Parkersburg\'s Methodist congregation, with an 800-seat sanctuary. It stands among the big houses of the Julia-Ann Square neighbourhood.',
  'Walls of quarry-faced Berea, Ohio sandstone laid in random, mostly level courses, broad Tudor-arched openings filled with art glass by the Rossbach Company of Columbus, and a battlemented corner tower (SAH Archipedia). Interior not checked.',
  '',
  'An active United Methodist church, 1001 Juliana Street. View from the street; the congregation\'s own page could not be opened when this was written, so service times are not given. Street parking.',
  [SAH('First United Methodist Church','22852')],
  brick='no',arch='George W. Kramer',archw='SAH Archipedia names George W. Kramer'),

N('masonic-temple-parkersburg','Masonic Temple','Parkersburg','wv','civic','standing',39.26776,-81.55616,'exact','view','drive','','1915',
  'A Classical Revival Masonic lodge building of 1915 at 900 Market Street, designed by Frank L. Packard of Columbus, Ohio, with a Parkersburg architect, Theodore T. Sansbury, supervising. It is part of the Avery Street Historic District. Wikipedia calls it three storeys; the 1982 Register form calls it four.',
  'A limestone ground storey and red brick above, three bays wide, with rounded (elliptical) bays on either side of the central bay of the front (Wikipedia; Register form). Interior not checked.',
  '',
  'A lodge building, not open to the public as far as any source read says. View from Market Street. Street parking.',
  [W('Masonic Temple (Parkersburg, West Virginia)'),NR('82001779')],
  brick='yes',bcol='red',conf='mixed',
  arch='Frank L. Packard',archw='National Register record and Wikipedia: "designed by Columbus architect Frank Packard"'),

N('union-trust-building-parkersburg','Union Trust Building','Parkersburg','wv','civic','standing',39.26690,-81.55782,'exact','view','drive','','1903–1904',
  'A seven-storey bank and office building of 1903 to 1904 at Market and 7th streets, ordered by Senator Johnson N. Camden, the oilman who had sold his refining company to Standard Oil, and later the Union Trust National Bank. It was the tallest building downtown for decades and is the tallest old building in the Downtown Parkersburg Historic District.',
  'A U-shaped block, five bays by seven, in the classical column scheme of base, shaft and capital: a smooth dressed stone base with arched corner openings, a shaft of wide windows with brick relieving arches and stone keystones, a projecting three-sided bay window up the middle and a metal cornice with cartouches. The windows are replacements (Register form; 2023 district nomination). Interior not checked.',
  'An oil baron\'s tower in a town of twelve thousand.',
  'A private office building, 700 Market Street. View from the street. '+DOWNTOWN,
  [W('Union Trust National Bank'),NR('82001791'),DPHD],
  brick='?'),

N('jackson-memorial-fountain-parkersburg','Jackson Memorial Fountain','Parkersburg','wv','curio','standing',39.26956,-81.53202,'site','public','drive','','1903',
  'A large cast-iron fountain at the entrance to City Park, paid for by a $5,000 bequest from a grandson of General John Jay Jackson, whose family gave West Virginia a governor, a federal judge and a congressman. SAH Archipedia dates it 1903 and Wikipedia 1905. It had three tiers, the second topped by a female figure pouring water from a vase. Wikipedia says lightning destroyed the cast-iron bowls in the early 1990s, a storm in October 2018 destroyed their fibreglass replacements and the rest of the old fountain, and a replica was put up in 2020.',
  'What stands now is, by Wikipedia\'s account, the 2020 replica of the fountain, with the lady of the lake on top. Not checked on the ground.',
  'The city park\'s centrepiece, lost to a storm and cast again.',
  'City Park, owned by the City of Parkersburg, at Park Avenue and 17th Street. Park parking on City Park Drive (OpenStreetMap). Park hours not checked.',
  [W('Jackson Memorial Fountain'),NR('84003686'),SAH('Jackson Memorial Fountain','22838')],
  th=[39.27116,-81.53045],thn='City Park Drive parking, City Park',brick='no',bcol='none',conf='mixed'),

N('julia-ann-square-historic-district-parkersburg','Julia-Ann Square Historic District','Parkersburg','wv','town','standing',39.27111,-81.55583,'area','public','walk','','1836–1915',
  'The houses of Parkersburg\'s oil and gas money, along Juliana and Ann streets from 9th Street to Riverview Cemetery: 116 contributing buildings, most of them built between 1875 and 1915 in late Victorian, Queen Anne and Colonial Revival styles. The oldest of note is the Van Winkle-Wix House, begun in 1836 by Peter Van Winkle and enlarged with a third floor, a wing, turrets and spires through the 1870s to 1890s. The Peter G. Van Winkle House at 600-602 Juliana Street was pulled down in 1994. A historical marker in the square says the Parkersburg architects Richard Adair and William Howe Patton designed a number of the houses.',
  'A walk of two parallel streets of big houses above the Ohio River (Wikipedia; SAH Archipedia). The houses are private.',
  '',
  'Public city streets of Parkersburg; the houses are private homes, seen from the sidewalk. Street parking.',
  [W('Julia-Ann Square Historic District'),NR('77001380'),SAH('Julia-Ann Square Historic District','22858')],
  brick='?'),

N('parkersburg-bridge-csx','Parkersburg Bridge (Sixth Street Railroad Bridge)','Parkersburg','wv','rail','standing',39.27081,-81.56483,'site','view','drive','','1869–1871',
  'The Baltimore and Ohio Railroad\'s bridge over the Ohio River to Belpre, Ohio, built from May 1869 to January 1871 and said to be the longest bridge in the world when finished, at 7,140 feet. It used 50,000 cubic yards of stone for its 53 piers. The approach spans were replaced in 1898 to 1900 and the river spans in 1904 to 1905 on the old piers; the steelwork was rebuilt again about 1914 to 1917, and one channel span after a barge explosion in 1972. It was the B&O\'s main line from Baltimore to St. Louis. It still carries trains: Wikipedia says those of the Belpre Industrial Parkersburg Railroad.',
  'The stone piers and steel spans of the long trestle running along 6th Street and out over the river (Register form; the downtown nomination photographs the trestle looking north along 6th Street).',
  'The longest bridge in the world in 1871, still on its stone piers.',
  'A working railroad bridge: stay off the tracks, trestle and piers. View it from 6th Street and the streets below it.',
  [W('Parkersburg Bridge (CSX)'),NR('82001785')],
  brick='no',
  arch='Jacob Linville; W. E. Porter',archw='Wikipedia: "Designed by Jacob Linville"; the National Register record names W. E. Porter as its engineer'),

N('parkersburg-high-school-wv','Parkersburg High School and Stadium Field','Parkersburg','wv','civic','standing',39.27871,-81.54482,'site','view','drive','','1917',
  'The city\'s high school, on a 27-acre campus at 2101 Dudley Avenue, built in 1914 to 1917 in the Jacobethan Revival style to designs by Frank L. Packard, with wings added in 1929. Its 10,000-seat stadium was finished in 1924 for a football team that had won state titles in 1919, 1921 and 1923. The school and the houses of Washington Avenue around it were listed together on the National Register in 1992.',
  'The brick main building set well back from Dudley Avenue, and the stadium\'s brick grandstand of 18 bays with stone-capped parapet and two brick gatehouses with canted sides and tent roofs (Register form). The field house of 1951 and the band room are later and not part of the listing.',
  '',
  'A working public high school: view from Dudley Avenue and the public streets; the buildings are not open to visitors. Stadium events not checked.',
  [NR('92000895')],
  brick='yes',bcol='red',arch='Frank L. Packard',archw='National Register form: "constructed in 1917 in the Jacobethan Revival style by Frank L. Packard"'),
]

PIN_NOTES={
 'blennerhassett-hotel-parkersburg':'ArcGIS PointAddress for 320 Market Street, Parkersburg.',
 'wood-county-courthouse-parkersburg':'Wikipedia article coordinate, on Court Square.',
 'trinity-episcopal-church-parkersburg':'ArcGIS PointAddress for 430 Juliana Street.',
 'st-francis-xavier-church-parkersburg':'ArcGIS PointAddress for 532 Market Street.',
 'first-baptist-church-parkersburg':'ArcGIS PointAddress for 813 Market Street.',
 'first-presbyterian-church-parkersburg':'ArcGIS PointAddress for 946 Market Street.',
 'first-united-methodist-church-parkersburg':'ArcGIS PointAddress for 1001 Juliana Street.',
 'masonic-temple-parkersburg':'ArcGIS PointAddress for 900 Market Street.',
 'union-trust-building-parkersburg':'ArcGIS PointAddress for 700 Market Street.',
 'jackson-memorial-fountain-parkersburg':'Moved about 20 m from the Wikipedia coordinate onto the round fountain basin seen on the aerial at the park entrance.',
 'julia-ann-square-historic-district-parkersburg':'Wikipedia article coordinate, in the middle of the district; the pin marks the area.',
 'parkersburg-bridge-csx':'Moved from the National Register list point onto the truss over the river near the West Virginia bank, as seen on the aerial.',
 'parkersburg-high-school-wv':'ArcGIS PointAddress for 2101 Dudley Avenue.',
}
