# Austin, Texas: standing buildings named in a video about the city's old buildings, each checked against the
# National Register list for Travis County, Wikipedia, Texas Historical Commission marker texts and the owners' pages.
from data_b import N
from data_ma import W

def THC(n, label): return [label + ' (Texas Historical Commission marker)', 'https://atlas.thc.texas.gov/Details/%d' % n]
DT = 'Downtown Austin street; parking not checked.'

BATCH={'key':'austin_nlta','label':'Austin, Texas: hotels, mansion, cathedral, opera house and the old asylum','added':'2026-11-26 15:32'}

PLACES=[
N('driskill-hotel-austin','Driskill Hotel','Austin','tx','hotel','standing',30.26814,-97.74172,'exact','open','drive','hotels','1886–',
  'Built by the cattleman Jesse Driskill and completed in 1886 to plans by the Austin architects J. N. Preston & Son, in Romanesque Revival style, it is the oldest hotel still operating in Austin. A 13-storey annex was joined to it in 1930. Every Texas governor since Sul Ross in 1887 has held an inaugural ball in its ballroom. Hyatt has run it since 2013; it was listed on the National Register in 1969.',
  'The four-storey 1886 block of pressed brick with white limestone trim, with big round arches over the entrances on the south and east sides and stone busts of Driskill and his two sons on three fronts (Jesse Driskill faces Sixth Street). The open rotunda inside lost its domed skylight to air conditioning in 1950. Interior not checked.',
  'A cattle baron\'s hotel where every Texas governor since 1887 has danced.',
  'A working hotel at 604 Brazos Street, on the corner of East Sixth Street. '+DT+' Opening hours of the public rooms not checked.',
  [W('Driskill Hotel')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('texas-governors-mansion','Texas Governor\'s Mansion','Austin','tx','landmark','standing',30.27280,-97.74309,'site','open','drive','','1854–1856',
  'The Greek Revival house of the governors of Texas, designed and built by Abner Cook and lived in by every governor since 1856, the oldest house in Texas that has been lived in without a break. It was enlarged in 1914. An arson fire badly damaged it on June 8, 2008, in the middle of a renovation; nobody was ever charged, and the restoration was finished in 2012. It was the first Texas historic landmark (1962) and is a National Historic Landmark (1974).',
  'A white columned house in the middle of a block of trees and gardens, at 1010 Colorado Street. The free tour lasts about 30 minutes and is about the people and events connected with the house.',
  'The governor\'s house that an arsonist nearly destroyed in 2008.',
  'Home of the governor and family, run for tours by the Texas State Preservation Board. Tours are free, at most 20 people, by reservation at least a week ahead through the Board\'s page; there are no walk-up tours, every adult needs government identification and passes a security check, and bags, food and drink are not allowed. Visitors wait on the sidewalk at 10th and Colorado streets. '+DT,
  [W('Texas Governor\'s Mansion'), ['Texas State Preservation Board: Governor\'s Mansion tours','https://www.tspb.texas.gov/prop/tgm/tgm-tour/tgm-tour.html'], ['Tour guidelines','https://tspb.texas.gov/prop/tgm/tgm-tour/tgm-guidelines.html']],
  conf='', th=None, thn=None, brick='?', hours='Free 30-minute guided tours by reservation at least one week ahead, on the days the State Preservation Board lists; no walk-ups'),

N('littlefield-building-austin','Littlefield Building','Austin','tx','civic','standing',30.26824,-97.74222,'site','view','drive','','1912–',
  'An office building on the corner of Congress Avenue and Sixth Street, built for George W. Littlefield, a Confederate veteran who made his fortune ranching and driving cattle and founded the American National Bank in 1890. C. H. Page Jr. designed it in Beaux Arts Classical style, and it opened in 1912 with a garden on the roof and the bank on the ground floor. Bronze doors for the corner entrance, cast by Tiffany\'s, were later given to the University of Texas. A Recorded Texas Historic Landmark since 2002.',
  'A nine-storey classical office block at 601 Congress Avenue, seen from the street. Interior not checked.',
  'A cattleman\'s bank tower with a roof garden on Congress Avenue.',
  'Private office building. View from Congress Avenue and East Sixth Street. '+DT,
  [THC(5453012734,'Littlefield Building')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('millett-opera-house-austin','Millett Opera House (Austin Club)','Austin','tx','civic','standing',30.27097,-97.74084,'exact','view','drive','','1878–',
  'Built in 1878 by Charles Millett, a lumber seller, on one of his lots, to plans by Frederick Ruffini, it was one of the largest halls in Texas, with 800 removable seats and limestone walls two feet thick. The Austin schools bought it in 1940; it escaped demolition in the 1950s, held a printing company until 1979, and was then taken on by the Austin Club, a private social club that now owns it. The club divided the hall into three floors.',
  'The stone front at 110 East Ninth Street. Part of the original hand-painted ceiling survives in one of the club\'s meeting rooms, which are not open to the public.',
  'Austin\'s great 1878 opera hall, now a private club.',
  'Owned by the Austin Club, a private club. View from East Ninth Street. '+DT,
  [W('Millett Opera House')],
  conf='', th=None, thn=None, brick='no', hours=''),

N('stephen-f-austin-hotel','Stephen F. Austin Hotel','Austin','tx','hotel','standing',30.26912,-97.74195,'exact','open','drive','hotels','1924–',
  'T. B. Baker of Baker Hotels opened this hotel in 1924 on the site of the Keystona Hotel. It was to have been called "The Texas" but was named for Stephen F. Austin in answer to local wishes. The Fort Worth firm Sanguinet, Staats and Hedrick designed it in Beaux Arts style, and five storeys were added in 1938. It was restored in 2000 and is a Recorded Texas Historic Landmark.',
  'A tall hotel at 701 Congress Avenue. After the 2000 restoration much of the original classical detail survives inside and out (Texas Historical Commission marker). Interior not checked otherwise.',
  'The hotel that was nearly called "The Texas".',
  'A working hotel on Congress Avenue at Seventh Street. '+DT+' Opening hours of the public rooms not checked.',
  [THC(5453013141,'Stephen F. Austin Hotel')],
  conf='', th=None, thn=None, brick='?', hours='?'),

N('pemberton-castle-austin','Pemberton Castle (Fisher-Gideon House)','Austin','tx','landmark','standing',30.29162,-97.75491,'site','view','drive','','1890s–',
  'A small Gothic Revival castle in the Pemberton Heights neighbourhood. It began in the 1890s as a round water tower and was made into a castle in the 1920s; the company that developed Pemberton Heights used it as its sales office. Samuel Gideon, a professor of architecture at the University of Texas, bought it in 1937 and worked into his house bricks and stained glass salvaged from the university\'s Old Main Building, torn down in 1934. It is a Recorded Texas Historic Landmark (marker 1996) and an Austin city landmark.',
  'The castle at 1415 Wooldridge Drive, seen from the street. A private house: no tours.',
  'A water tower turned castle, built partly from the university\'s demolished Old Main.',
  'Private house. View from Wooldridge Drive only; do not go onto the grounds. Street parking in a residential neighbourhood.',
  [THC(5507014290,'Pemberton Castle (Fisher-Gideon House)'), W('Pemberton Heights, Austin, Texas'), W('Main Building (University of Texas at Austin)')],
  conf='', th=None, thn=None, brick='?', hours=''),

N('o-henry-hall-austin','O. Henry Hall (U.S. Post Office and Federal Building)','Austin','tx','civic','standing',30.26849,-97.74380,'exact','view','drive','','1879–',
  'The federal courthouse and post office, designed by James G. Hill and built partly under the eye of the Austin architect Abner Cook; Wikipedia gives it as completed in 1879 at a cost of $200,000, and files it under buildings completed in 1881. The federal court met here until 1936; in February 1898 William Sidney Porter, later the writer O. Henry, was tried and convicted of embezzlement in it. The University of Texas System bought it in 1968 and named it for him; the Texas State University System bought it in 2015 and uses it as its headquarters.',
  'A three-storey stone federal building on West Sixth Street at Colorado Street, seen from the street. Interior not checked.',
  'The courthouse where O. Henry was convicted.',
  'Offices of the Texas State University System. View from West Sixth Street. '+DT,
  [W('O. Henry Hall')],
  conf='mixed', th=None, thn=None, brick='?', hours=''),

N('st-mary-cathedral-austin','Saint Mary Cathedral','Austin','tx','worship','standing',30.27102,-97.73953,'exact','open','drive','','1872–1874',
  'The Catholic cathedral of Austin. The parish began in the 1850s with a small stone church, St. Patrick\'s, at 9th and Brazos streets. The cornerstone of this Gothic Revival church, designed by Nicholas Clayton, was laid in 1872 a block to the north; it was finished in 1874 and dedicated in 1884, and its towers and spires were completed in 1907. It became the cathedral when the Diocese of Austin was formed in 1948. It is on the National Register (1973).',
  'Stained glass, some of it added in the 1890s, and pointed arches. Much of the Gothic decoration inside was removed in a 1948 remodelling, when the altars and altar rail were replaced in marble; the building was restored in 2013.',
  'A Nicholas Clayton cathedral with spires finished in 1907.',
  'An active parish at 203 East 10th Street. Mass times are from the Diocese of Austin\'s own news page about the cathedral; the parish\'s site could not be opened when this was written. '+DT,
  [W('Cathedral of Saint Mary (Austin, Texas)'), ['Diocese of Austin: St. Mary Cathedral','https://austindiocese.news/st-mary-cathedral-sits-heart-diocese-austin']],
  conf='', th=None, thn=None, brick='?', hours='Daily Mass 6:30 a.m. and 12:05 p.m.; confession Monday to Saturday 11 a.m. to noon; Sunday Mass times not checked'),

N('ut-main-building-austin','Main Building and Tower, University of Texas','Austin','tx','inst','standing',30.28577,-97.73950,'exact','view','walk','','1937–',
  'The 307-foot tower at the centre of the University of Texas campus, designed by Paul Philippe Cret and completed in 1937 on the site of the Victorian Gothic Old Main Building of 1882, which was torn down in 1934 over the objections of many students and teachers. The tower was first meant as the library stacks. On August 1, 1966, a gunman shot from its observation deck; the deck was closed and reopened several times, the last time in 2004.',
  'A carillon of 56 bells, the largest in Texas, at the top. All that is left of Old Main are its chime bells, the Burleson Bells, shown outside Bass Concert Hall; some of its bricks and stained glass went into Pemberton Castle.',
  'The tower that took the place of Old Main.',
  'University of Texas at Austin, 110 Inner Campus Drive; the campus grounds are open to walk. The University Unions\' page said tower tours were unavailable when this was written. Parking not checked.',
  [W('Main Building (University of Texas at Austin)'), ['University Unions: Tower Tours','https://universityunions.utexas.edu/tower-tours']],
  conf='', th=None, thn=None, brick='?', hours=''),

N('austin-state-hospital-old-main','Austin State Hospital (Texas State Lunatic Asylum)','Austin','tx','inst','standing',30.30827,-97.73715,'area','view','drive','','1857–1861',
  'Chartered by the Texas Legislature in 1856 as the Texas State Lunatic Asylum and known by that name until 1925, it is the oldest psychiatric hospital in Texas and the oldest still working west of the Mississippi. Its Main Building opened to patients on March 11, 1861. Older buildings were cleared from 2020 for a new hospital, which the state showed in May 2024; the state said the Old Main Building, a Texas Historic Landmark, would stay. The asylum is on the National Register (1987).',
  'The Old Main Building of 1861 is the piece of the original asylum still standing. Which building on the campus it is was not settled from the aerial picture.',
  'The 1861 asylum Texas kept when it rebuilt its oldest hospital.',
  'A working state psychiatric hospital run by the Texas Health and Human Services Commission, 4110 Guadalupe Street. Not open to visitors; view from the public streets only. The pin marks the campus.',
  [W('Austin State Hospital'), ['Texas HHSC: demolition done, construction begins (December 2020)','https://content.govdelivery.com/accounts/TXHHSC/bulletins/2af255d']],
  conf='', th=None, thn=None, brick='?', hours=''),
]

PIN_NOTES={
 'driskill-hotel-austin':'Address lookup for 604 Brazos Street, on the building.',
 'texas-governors-mansion':'Address lookup for 1010 Colorado Street; the house stands in the middle of its block.',
 'littlefield-building-austin':'OpenStreetMap outline of the Littlefield Building at Congress Avenue and Sixth Street.',
 'millett-opera-house-austin':'Address lookup for 110 East Ninth Street, on the building.',
 'stephen-f-austin-hotel':'Address lookup for 701 Congress Avenue, on the building.',
 'pemberton-castle-austin':'Address lookup for 1415 Wooldridge Drive; the pin marks the lot.',
 'o-henry-hall-austin':'OpenStreetMap outline of O. Henry Hall on West Sixth Street.',
 'st-mary-cathedral-austin':'Address lookup for 203 East 10th Street, on the building.',
 'ut-main-building-austin':'OpenStreetMap outline of the Main Building.',
 'austin-state-hospital-old-main':'OpenStreetMap point for the hospital; the aerial shows a small building among cleared ground, so the pin marks the campus, not the Old Main Building itself.',
}
