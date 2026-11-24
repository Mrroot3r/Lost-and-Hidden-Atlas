# November 24, 2026 (UTC): Pottsville, Schuylkill County, Pennsylvania (region pane), names taken as leads from one
# Old World Exploration video about the town and checked one by one. Standing buildings of the anthracite county seat:
# the 1851 jail where Molly Maguires were hanged, the 1892 courthouse, the 1913 armory, the Yuengling brewery, the
# Henry Clay column, the old grammar school that holds the county historical society, the library, the Necho Allen
# hotel, the United Presbyterian church, Garfield Square, the North Centre Street business blocks and the high school.
# Facts come from the linked sources only: SAH Archipedia (George E. Thomas, Buildings of Pennsylvania), Wikipedia read
# as raw text, and the pages of Yuengling, the county historical society and the library. The National Register forms
# for the downtown district, the brewery and the armory are not on line. HMdb answered 403.
# Where sources disagree the text gives both; where a source is silent it says "not checked".
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def SAH(n,t): return L('SAH Archipedia: '+t,'https://sah-archipedia.org/buildings/PA-02-SC'+n)

BATCH={'key':'pottsville_zxpw','label':'Pottsville, Pennsylvania','added':'2026-11-24 04:44'}

GARAGE=[40.68360,-76.19541]
GARAGEN='Mahantongo Street parking garage (South 2nd Street), as mapped on OpenStreetMap; fees not checked'

PLACES=[

N('schuylkill-county-jail-pottsville','Schuylkill County Jail','Pottsville','pane','civic','standing',40.68849,-76.19913,'site','view','drive','',
  '1851–1852',
  'The county prison was designed by Napoleon LeBrun and built in 1851–1852 behind the courthouse, with a central tower over a heavy Gothic front, much like his Montgomery County jail. LeBrun and his sons added to it in 1876–1877, while the trials and hangings of the Molly Maguires were under way; the courthouse that stood here then saw several of those trials and executions.',
  look='A fortress-like Gothic front of local brownstone woven through rougher yellow sandstone, with a central tower; the prison walls and the 1876 wing are sandstone. It is still the Schuylkill County Prison, at 230 Sanderson Street, so it is seen only from the street. Interior not open.',
  hook='',
  accn='A working county prison: look from Sanderson Street and the public streets round the courthouse, and do not photograph people or try to go in. Street parking in downtown Pottsville, or the Mahantongo Street garage (fees not checked).',
  links=[SAH('17','Schuylkill County Jail'),SAH('16','Schuylkill County Courthouse'),L('JailExchange: Schuylkill County Prison (address)','https://www.jailexchange.com/city-and-county-jails/pennsylvania/city/pottsville')],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('schuylkill-county-courthouse-pottsville','Schuylkill County Courthouse','Pottsville','pane','civic','standing',40.68781,-76.19843,'site','view','drive','',
  '1892; wing 1931',
  'The courthouse was built in 1892 to designs by Milton E. Beebe, the most prolific builder of Pennsylvania courthouses of the late 1800s, on the site of the 1849–1851 Italianate courthouse where several of the Molly Maguires were tried. Beebe took his model from H. H. Richardson\'s state capitol in Albany. Eric Fisher Wood added the wing with aluminum panels in 1931.',
  look='Grouped round-arched windows in the upper stories and a mansard roof, in the manner of the Albany capitol. Inside, the interior has been modernized, but Beebe\'s cast-iron stairs with heavy chamfers remain. Pottsville City Hall (1936), a Moderne cube, stands nearby at Laurel and North Centre streets.',
  accn='A working county courthouse at 401 North Second Street; the offices inside keep weekday business hours, which were not read from a county page here. Expect a security screening at the door. Street parking downtown, or the Mahantongo Street garage (fees not checked).',
  links=[SAH('16','Schuylkill County Courthouse')],
  conf=None,th=None,thn=None,brick='no',hours=''),

N('pottsville-armory','Pottsville Armory (Schuylkill YMCA)','Pottsville','pane','civic','standing',40.69022,-76.19781,'site','view','drive','',
  '1913',
  'Built in 1913 as the armory of Company H, Eighth Infantry, Pennsylvania National Guard, to designs by McCormick and French of Wilkes-Barre, who also drew the armory in nearby Tamaqua. It is a brick T-plan building in a mixed Romanesque and Gothic Revival style, listed on the National Register in 1991, and now houses the Schuylkill YMCA.',
  look='A small battlemented castle on the main street: a two-story office block with a three-story central tower and crenellations along the top, and behind it a drill hall under a shallow arched roof. Interior not checked.',
  accn='Now the Schuylkill YMCA at 502 North Centre Street: look from the street; the inside is the YMCA\'s and its hours and rules were not checked. Street parking on North Centre Street.',
  links=[W('Pottsville Armory'),SAH('18','Company H, Eighth Infantry Pennsylvania National Guard Armory')],
  conf=None,th=None,thn=None,brick='?',hours=''),

N('yuengling-brewery-pottsville','D. G. Yuengling and Son Brewery','Pottsville','pane','industry','standing',40.68267,-76.19736,'exact','open','drive','',
  '1831–1930s',
  'David G. Yuengling started the Eagle Brewery on Centre Street in 1829; after it burned in 1831 the brewery moved to Mahantongo Street at Fifth Street, where it still brews. It is called the oldest operating brewery in America. Its centerpiece is a five-story brew house from the early years; the additions of about 1900 are by the Philadelphia brewery architects Otto Wolf and Clarence Wunder. The complex was listed on the National Register in 1985.',
  look='The five-story brew house, whose louvered cooling panels on the third and fourth floors were replaced by large windows, and the turn-of-the-century additions. Across Mahantongo Street are the terra-cotta friezes and curved gables of the former Yuengling Ice Cream and Dairy Plant (1919, Amos W. Barnes). The free tour takes about an hour and climbs about 160 stairs.',
  accn='The working brewery gives free tours for all ages (about an hour; closed shoes required; not wheelchair accessible; ID needed to sample). Closed Memorial Day, Independence Day, Labor Day, Thanksgiving, Christmas and New Year\'s Day, and on some listed dates; hours from Yuengling\'s own Pottsville page, read November 2026. Street parking on Mahantongo Street, or the Mahantongo Street garage (fees not checked).',
  links=[L('Yuengling: tour America\'s oldest brewery','https://www.yuengling.com/americas-oldest-brewery-pottsville-pa'),SAH('8','D. G. Yuengling and Son Brewery'),W('Yuengling')],
  conf=None,th=GARAGE,thn=GARAGEN,brick='?',hours='Shop Monday to Saturday 9 a.m. to 5 p.m.; tours Monday to Saturday 10 a.m. to 3 p.m. (hourly, every half hour on Saturdays March to December); Sunday closed'),

N('united-presbyterian-church-pottsville','United Presbyterian Church','Pottsville','pane','worship','standing',40.68412,-76.19575,'site','view','drive','',
  '1874',
  'John Fraser designed this austere Presbyterian church of 1874 at 214 Mahantongo Street. Wilson, Harris and Richards altered it in 1909, and Ralph Adams Cram oversaw the 1926 renovation that gave it its present interior. Two signed Tiffany windows that had been in the sanctuary for a century were sold to the Allentown Art Museum about 2018, and exact replicas now fill their places. The Tiffany census also records a Tiffany window moved here from Second Presbyterian Church when the two congregations merged in 1968.',
  look='An immense tracery rose window over the entrance, and the two replica Tiffany windows facing South Third Street. Inside, Cram\'s 1926 chancel with richly carved furniture (from SAH Archipedia; the church\'s service times and whether it opens to visitors were not checked).',
  accn='An active church; look from Mahantongo and South Third streets. Service times not checked. Street parking, or the Mahantongo Street garage nearby (fees not checked).',
  links=[SAH('6','Reading Anthracite Company (the church is described in this entry)'),L('Synod of the Trinity: sale of Tiffany windows helps United Church (2018)','https://www.syntrinity.org/featured/sale-of-rare-stained-glass-tiffany-windows-help-united-church-with-improvements-programs/'),L('Synod of the Trinity: the windows go to Allentown, replicas in place (2025)','https://www.syntrinity.org/featured/sale-of-tiffany-windows-allows-united-church-to-share-them-with-the-world/'),L('Tiffany Census: Second Presbyterian Church, Pottsville','https://cambridge2000.com/tiffany/html/site/33.55.3.html')],
  conf=None,th=GARAGE,thn=GARAGEN,brick='?',hours=''),

N('henry-clay-monument-pottsville','Henry Clay Monument','Pottsville','pane','curio','standing',40.68152,-76.19269,'exact','view','drive','',
  '1852–1855',
  'Pottsville raised this cast-iron Doric column and statue to Henry Clay, whose protective tariffs helped the anthracite trade, soon after his death. The cornerstone was laid on July 26, 1852, and the monument was dedicated on July 4, 1855. Frank Hewson designed the column, made by George B. Fissler; the statue was designed by H. Wesche and cast at Robert Wood\'s foundry in Philadelphia (SAH Archipedia calls the founder Richard Wood). It was restored from 1983 and rededicated in 1985.',
  look='A white-painted cast-iron column on a stone base, high on the ridge above South Centre Street, with Clay facing north over the city. The heights given differ widely: Wikipedia\'s sources give about 66 feet overall with a statue of about 15 feet, while SAH Archipedia gives a column of nearly 175 feet. Inscriptions on three faces of the base, the south one recording the 1985 restoration.',
  accn='Seen from South Centre Street near West Washington Street, below the ridge; who owns the ground and whether a public path climbs to the base were not checked. Parking: a mapped lot on South Centre Street about 110 m away, or the Union Street lot on Progress Street (both as mapped on OpenStreetMap; owners and fees not checked).',
  links=[W('Henry Clay Monument'),SAH('2','Henry Clay Monument')],
  conf='mixed',th=[40.68081,-76.19176],thn='Lot on South Centre Street, as mapped on OpenStreetMap; owner not checked',brick='no',hours=''),

N('female-grammar-school-pottsville','Female Grammar School (Schuylkill County Historical Society)','Pottsville','pane','civic','standing',40.68704,-76.19697,'exact','open','drive','',
  '1863',
  'John Fraser designed this corbeled grammar school for girls, built in 1863 during the Civil War at North Centre and Race streets. It is now the headquarters and museum of the Schuylkill County Historical Society, founded in 1903, which collects the county\'s records from coal mining to the Underground Railroad.',
  look='The corbeled front at the head of the North Centre Street business blocks. Inside, the society\'s museum and research collections, with guided or self-guided tours; what is on show was not checked.',
  accn='The Schuylkill County Historical Society, 305 North Centre Street. Hours from the society\'s own newsletter of May 2023 (its website gives none): check before going. Street parking on North Centre Street.',
  links=[L('Schuylkill County Historical Society: what we do','https://www.schuylkillhistory.org/what-we-do'),L('Schuylkill County Historical Society newsletter, May 2023 (hours)','https://orca-marlin-583a.squarespace.com/s/Newsletter-2023-05-compressed.pdf'),SAH('15','North Centre Street')],
  conf=None,th=None,thn=None,brick='?',hours='Wednesday to Friday 10 a.m. to 4 p.m.; Saturday 10 a.m. to 2 p.m. except January and February (as given in May 2023)'),

N('north-centre-street-pottsville','North Centre Street business blocks','Pottsville','pane','town','standing',40.68512,-76.19514,'area','public','walk','',
  'c. 1860–c. 1923',
  'The commercial heart of Pottsville, inside the Pottsville Downtown Historic District listed in 1982 (336 contributing buildings). Between Mahantongo and Race streets stand the six-story Schuylkill Trust Company (1923, Mowbray and Uffinger), a small-town skyscraper over a banking hall at West Norwegian Street; the restored Majestic Theatre (1910) at 209 North Centre; and terra-cotta, stone and glass fronts by the local architect Frank X. Reilly, among them the Yeager Building (1898) at 20 North Centre and the Union National Bank (1912) at Mahantongo.',
  look='Walk North Centre Street from Mahantongo Street to the old Female Grammar School at Race Street. Reilly\'s Green\'s Jewelry building (1896), Miller and Miller Building (1917) and Cowen drugstore (1915) are just south, at 8 to 13 South Centre. The Capitol Theatre that stood at 218–220 North Centre was razed in 1982.',
  accn='Public streets, any time; the buildings are private businesses and offices. Street parking, or the Mahantongo Street garage (fees not checked).',
  links=[SAH('15','North Centre Street'),W('Pottsville Downtown Historic District'),L('Cinema Treasures: Capitol Theatre, Pottsville','https://cinematreasures.org/theaters/3840')],
  conf=None,th=GARAGE,thn=GARAGEN,brick='some',hours=''),

N('necho-allen-hotel-pottsville','Necho Allen Hotel','Pottsville','pane','hotel','standing',40.6842,-76.19467,'site','view','drive','',
  '1926',
  'A midsized hotel of 1926 by Thomas, Martin and Kirkpatrick, Art Deco simplified and joined to English Regency, the up-to-date hotel of a small eastern Pennsylvania city. The same firm built the Eastonian in Easton the same year. Travel changed, the hotel trade left, and the building was turned into housing for older people.',
  look='The hotel block at 101 Mahantongo Street, at the foot of the hill where Mahantongo meets Centre Street. It is housing now: look from the street. Interior not checked.',
  accn='Private residential building: view from Mahantongo and Centre streets. Street parking, or the Mahantongo Street garage across the block (fees not checked).',
  links=[SAH('5','Necho Allen Housing (Necho Allen Hotel)')],
  conf=None,th=GARAGE,thn=GARAGEN,brick='?',hours=''),

N('pottsville-free-public-library','Pottsville Free Public Library','Pottsville','pane','civic','standing',40.68495,-76.19692,'exact','open','drive','',
  '1922',
  'The library opened in 1911 in rented rooms at 208 West Market Street, where some books were kept in an iron oven left from the building\'s saloon days. A Carnegie grant of $45,000 followed, but post-war prices left it short, and the present building, a plain Georgian Revival design by Harris and Richards (successors to the Wilson Brothers), opened on May 1, 1922. It has since been enlarged.',
  look='The 1922 Georgian Revival front on West Market Street, a block from Garfield Square. Interior not checked.',
  accn='A public library at 215 West Market Street, free to Schuylkill County residents; its opening hours could not be read on its own website. Street parking on Market Street.',
  links=[L('Pottsville Free Public Library: about','https://www.pottsvillelibrary.org/about'),SAH('13','Pottsville Free Public Library')],
  conf=None,th=None,thn=None,brick='?',hours='?'),

N('garfield-square-pottsville','Garfield Square','Pottsville','pane','inst','standing',40.6842,-76.1989,'site','view','drive','',
  'before 1829',
  'Laid out before 1829 as Pottsville\'s market square, before trade moved to Centre Street, it is now a landscaped square with several sculptures, among them the Soldiers and Sailors Monument of 1891 by August Zeller. The First Methodist Church (1903), a late Richardsonian Romanesque building by the New York church architect George Kramer, anchors one corner, and the Garfield Diner, a 1953 Kullman diner, stands opposite.',
  look='The Soldiers and Sailors Monument, the First Methodist Church on the corner, and the Garfield Diner. Which other churches face the square was not checked.',
  accn='The square lies along Market Street between Fourth and Sixth streets and is seen from the street; who owns it and its rules were not checked. Street parking on Market Street.',
  links=[SAH('12','Garfield Square')],
  conf=None,th=None,thn=None,brick='?',hours=''),

N('pottsville-area-high-school','Pottsville Area High School','Pottsville','pane','civic','standing',40.68133,-76.21391,'site','view','drive','',
  '1932',
  'Pottsville\'s high school, founded in 1853, moved from the Jackson Street building to the Garfield building at Fifth and West Norwegian streets in 1894, to the Patterson building at Twelfth and Market in 1916, and in January 1933 to this building at Sixteenth Street and Elk Avenue, built in 1932. It is the largest public high school in Schuylkill County.',
  look='A large building in Italian Gothic brickwork. Inside are a 1,499-seat auditorium, a little theater and a planetarium and observatory (from Wikipedia; interior not checked). It is a working school.',
  accn='A working public school: look from Elk Avenue and Sixteenth Street, and keep off the grounds during school hours.',
  links=[W('Pottsville Area High School')],
  conf=None,th=None,thn=None,brick='yes',hours=''),
]

PIN_NOTES={
 'schuylkill-county-jail-pottsville':'Address point for 230 Sanderson Street from the ArcGIS geocoder.',
 'schuylkill-county-courthouse-pottsville':'Address point for 401 North Second Street from the ArcGIS geocoder.',
 'pottsville-armory':'OpenStreetMap sports-centre point for the YMCA on North Centre Street; the geocoder\'s street match for 502 North Centre Street fell on the road about 35 m south.',
 'yuengling-brewery-pottsville':'OpenStreetMap building mapped as the Yuengling Brewery on Mahantongo Street.',
 'united-presbyterian-church-pottsville':'Address point for 214 Mahantongo Street from the ArcGIS geocoder.',
 'henry-clay-monument-pottsville':'OpenStreetMap memorial point for the Henry Clay statue; the Wikipedia coordinate is about 15 m away.',
 'female-grammar-school-pottsville':'Address point for 305 North Centre Street from the ArcGIS geocoder.',
 'north-centre-street-pottsville':'The corner of North Centre and West Norwegian streets (the Schuylkill Trust Company corner), from the ArcGIS geocoder; the blocks run north and south of it.',
 'necho-allen-hotel-pottsville':'Address point for 101 Mahantongo Street from the ArcGIS geocoder.',
 'pottsville-free-public-library':'Address point for 215 West Market Street from the ArcGIS geocoder.',
 'garfield-square-pottsville':'The corner of West Market and Fifth streets from the ArcGIS geocoder, in the middle of the square\'s stretch of Market Street.',
 'pottsville-area-high-school':'OpenStreetMap building mapped as Pottsville Area High School, 1600 Elk Avenue.',
}
