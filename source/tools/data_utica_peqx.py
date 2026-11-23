# November 23, 2026: Utica, New York. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Utica (the record is source/videos/20230629_mMW3jm2B02w.md); the video is a tip and nothing here rests on it.
# Sources read: the National Register nominations for the Downtown Genesee Street Historic District (2018) and the
# Bagg's Square East Historic District (2017) at NPGallery, Wikipedia (Hotel Utica, Utica Armory), the New York State
# Military Museum's armory pages, the Governor's office release on the Olbiston, the Masonic Care Community's own pages,
# and Mohawk Valley Museums' page on the Soldiers' Monument. Pins are address points or Register points, each looked at
# on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'utica_peqx','label':'New York: old downtown Utica','added':'2026-11-23 16:32'}

DGS=['National Register nomination: Downtown Genesee Street Historic District (2018)','https://npgallery.nps.gov/GetAsset/835149cd-a9aa-483a-952c-aeee4858abd1']
DT=' Street parking and city lots downtown; their hours and fees were not checked.'

PLACES=[

N('savings-bank-of-utica','Savings Bank of Utica (the Gold Dome)','Utica','mohw','civic','standing',43.10025,-75.23308,'exact','view','walk','','1898–1900',
  'A limestone bank with a gilded dome at 233 Genesee Street, designed by the New York architect Robert William Gibson and opened on February 26, 1900. It was enlarged in the same style in 1929, its banking room was renovated in 1929 and 1964, and a plain four-storey wing was added to the north in 1977–79. The Savings Bank of Utica later became Partners Trust, which M&T Bank took over in 2007; the building is a contributing part of the Downtown Genesee Street Historic District.',
  'Giant Corinthian columns carrying an open pediment on Genesee Street, broken pediments over the ground-floor windows and door, a big half-round window on the Bank Place side, and the paneled gilded dome over all. The 1929 bay to the north matches the original. Interior not checked.',
  '',
  'In use as a branch of M&T Bank; seen from Genesee Street and Bank Place. Whether the old banking room may be visited was not checked.'+DT,
  [DGS],
  brick='no'),

N('utica-central-fire-station','Central Fire Station (Utica)','Utica','mohw','civic','standing',43.10059,-75.22844,'exact','view','walk','','1911',
  'Utica\'s Central Fire Station of 1911 at 235 Elizabeth Street, designed by the Utica architect John A. Hobbes. It was altered about 1990 and now holds the Supreme Court law library. The block it stands on had been part of the city\'s African American neighbourhood round Post Street, of which nothing stands.',
  'A three-storey brick front six bays wide, its ground-floor arches once the doors for the fire engines, with a wealth of limestone trim: string courses, quoins, voussoirs and keystones, and a bracketed cornice over the second floor. The original parapet is gone and the windows are new. Interior not checked.',
  '',
  'A public building, now a court law library; seen from Elizabeth Street. Its opening hours were not checked.'+DT,
  [DGS],
  brick='?'),

N('st-johns-church-utica','St. John\'s Church (Historic Old St. John\'s)','Utica','mohw','worship','standing',43.10104,-75.22742,'exact','view','walk','','1869–1872',
  'A large brick Catholic church at Bleecker and John Streets, built from 1869 and consecrated in 1872, in the round-arched German style (Rundbogenstil) often taken for Romanesque Revival. Its twin square towers were added in 1893. The nomination calls St. John\'s the fourth Catholic parish in New York State. The church was repaired and repainted in 2012–13, and a marble altar from a closed church was brought in.',
  'Two square towers flank a triple-arched entrance; brick banding and corbelling cover the walls, and the transept ends have triple windows. The attached rectory has a mansard roof. Interior not checked.',
  '',
  'An active Catholic church at 240 Bleecker Street; its own web page refused to open when this was written, so service times were not checked.'+DT,
  [DGS],
  brick='yes',hours='?'),

N('oneida-county-courthouse-utica','Oneida County Courthouse (Utica)','Utica','mohw','civic','standing',43.10013,-75.22959,'exact','view','walk','','1903–1908',
  'The county courthouse at 200 Elizabeth Street, designed by Olin Wesley Cutter of Boston with Ward & Turner; the architect was announced in February 1903 and the building took five years. Remodellings in 1957–59, the 1960s and 1973 stripped much of its classical ornament to look modern; an addition went on the east end about 2000, and work from 2004 to 2012 restored some of the original courtrooms and public rooms.',
  'A five-storey brick building on a high rusticated stone base, seven bays wide, with pilasters and tall arched openings running through the second to fourth floors and a top floor made to look like a parapet. Interior not checked.',
  '',
  'In use as a courthouse; seen from Elizabeth and Charlotte Streets. Public hours were not checked.'+DT,
  [DGS],
  brick='no'),

N('hotel-utica','Hotel Utica','Utica','mohw','hotel','standing',43.10284,-75.23095,'exact','open','walk','hotels','1910–1912',
  'A steel-framed hotel at Lafayette and Seneca Streets, designed by Esenwein & Johnson of Buffalo and opened on March 11, 1912, with 200 rooms, a ballroom and four dining rooms; three more storeys were added in 1926. It closed as a hotel in 1972 and became adult homes, then stood empty until a $13 million restoration reopened it in 2001. Since 2017 it has been a DoubleTree by Hilton. It stands on the site of the Utica Opera House of 1871.',
  'Thirteen storeys of brick with a rusticated limestone ground floor and the original bracketed cornice at the ninth floor, the 1926 storeys above it. Inside, tall round-headed windows light the lobby and restaurant. The hotel was first decorated with murals by N. C. Wyeth; at least one was found in 1973 painted over in the former Lamplighter Room, and the lobby\'s mosaic floor was covered with new tile in 2016–17.',
  '',
  'A working hotel, a DoubleTree by Hilton, at 102 Lafayette Street. Whether visitors who are not guests may look round the lobby was not checked.'+DT,
  [W('Hotel Utica'),DGS],
  brick='?',hours='?'),

N('olbiston-utica','The Olbiston','Utica','mohw','landmark','standing',43.09346,-75.24688,'exact','view','walk','','1898',
  'A Romanesque Revival apartment house of brick and stone at 1431 Genesee Street, opened in 1898 and divided up again and again in the 20th century. It was decaying by the 1970s, and in 2021 the city shut it and its residents were moved out over unsafe conditions. A $67 million restoration with state and federal historic tax credits made it 153 affordable apartments, finished in August 2024. It is on the National Register.',
  'Sandstone and brick fronts with bay windows and balconies with cast-iron railings. Inside, the restoration kept the century-old marble floors and wood trim of the halls. Private apartments: seen from Genesee Street.',
  '',
  'Private apartments, owned by Liberty Affordable Housing; seen from Genesee Street. Street parking on Genesee Street was not checked.',
  [['Governor\'s office: Olbiston Apartments restoration completed (2024)','https://www.governor.ny.gov/news/governor-hochul-announces-completion-67-million-revitalization-historic-olbiston-apartments'],['National Register list, Oneida County','https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Oneida_County,_New_York']],
  brick='?'),

N('utica-armory','Utica Armory (Parkway East)','Utica','mohw','civic','standing',43.07915,-75.20794,'exact','view','drive','','1929–1930',
  'A National Guard armory at 1700 Parkway East, built in 1929–30 for Troop A of the 121st Cavalry to the design of the state architect William Haugaard, and renovated in 2007. It has a two-storey administration building with an attached three-storey drill shed, and was listed on the National Register in 1995. It replaced the Steuben Street armory of 1894, which had in turn replaced the Bleecker Street arsenal of 1862. The state military museum lists it as open and in use by the 107th Military Police Company and the 2nd Battalion, 108th Infantry.',
  'A steel-framed building with brick curtain walls; the administration block has Tudor towers, turrets and battlemented parapets. In military use: seen from Parkway East.',
  '',
  'A working New York National Guard armory; seen from Parkway East. It is not open to visitors.',
  [W('Utica Armory'),['New York State Military Museum: Utica, Parkway East Armory','https://museum.dmna.ny.gov/armories-arsenals/utica-armory-parkway-east']],
  brick='?'),

N('masonic-home-utica','Masonic Home (Masonic Care Community)','Utica','mohw','inst','standing',43.08824,-75.19115,'area','view','drive','','1891–1893',
  'The home the Masons of New York State built in Utica, chosen as the middle of the state, for old Masons, their wives and widows and their orphans. It opened in May 1893, paid for from the rents of the Masonic Hall in New York City, and between 1893 and 1982 more than 900 children were raised here. Wiley Hall was built for the boys in 1928; a babies\' home followed in 1923 and the Soldiers and Sailors Hospital in 1922. It is now the Masonic Care Community, a senior care campus of about 440 acres.',
  'The Daniel D. Tompkins Memorial Chapel, dedicated in 1893 and the oldest building on the campus, has Tiffany and Gorham stained glass, a zodiac light in its ceiling, a Buhl pipe organ, and Augustus Saint-Gaudens\'s statue Silence in its entrance; in front of the hospital stand a statue of Orville Parker Johnson and the 1922 "Spirit of Masonry" group. Interiors not checked.',
  '',
  'A private senior care community at 2150 Bleecker Street; its own page offers tours to people thinking of living there. Otherwise seen from the campus drives; whether casual visitors may walk the grounds was not checked.',
  [['Masonic Care Community: 130 years','https://masonichomeny.org/130-years-strong-promises-made-promises-kept/'],['Masonic Care Community: history','https://www.masonichomeny.org/about-us/history/']],
  brick='?'),

N('soldiers-monument-utica','Soldiers\' and Sailors\' Monument, Oneida Square','Utica','mohw','curio','standing',43.09597,-75.24228,'site','public','walk','','1889–1891',
  'Utica\'s Civil War monument in Oneida Square, where Genesee, State and Park Streets meet. The Soldiers\' Monument Association adopted Carl Gerhardt\'s design in February 1889; the contract was for $30,000, half raised by a fair and gifts and the rest by a tax the voters agreed to. It was unveiled on October 13, 1891.',
  'The inscription remembers the men of Utica who risked their lives to save the Union, "from Sumter, by land and sea, to Appomattox, 1861–1865". The square is a traffic circle: look from the sidewalks round it.',
  '',
  'A public monument in a city traffic circle; seen from the sidewalks of Oneida Square. Street parking nearby was not checked.',
  [['Mohawk Valley Museums: Plans for the Soldiers\' Monument (from the Utica Daily Observer)','https://mohawkvalleymuseums.us/this-day-in-history/mohawk-valley-history-february-16-1889-utica-ny/']],
  brick='no'),

N('baggs-square-east-utica','Bagg\'s Square East Historic District','Utica','mohw','town','standing',43.1030,-75.2233,'area','public','walk','','1875–1955',
  'The old warehouse and railroad quarter east of Genesee Street, between the New York Central tracks and the line of the Erie Canal (now Oriskany and Catherine Streets). Bagg\'s Square itself, where the Mohawk was forded and the town\'s first tavern stood, was taken for a highway and ramps in the late 1960s and is not part of it. The district\'s buildings date from about 1875 to 1955, when canal, railroad and industry made Utica a shipping centre. It is on the National Register; its nomination dates from 2017.',
  'Brick commercial and industrial buildings on Broad, Catherine, First, John, Main and Second Streets, near Union Station; several have their own listings (the Doyle Hardware, Hurd & Fitzgerald, Utica Daily Press and Hieber buildings). Seen from the streets.',
  '',
  'City streets, open at all times. Union Station\'s lot and street parking were not checked.',
  [['National Register nomination: Bagg\'s Square East Historic District (2017)','https://npgallery.nps.gov/GetAsset/1adb441b-12b2-42db-94de-bc85280913ad'],W('Bagg\'s Hotel')],
  brick='?'),

]

PIN_NOTES={
 'savings-bank-of-utica':'Address point for 233 Genesee Street.',
 'utica-central-fire-station':'Address point for 235 Elizabeth Street.',
 'st-johns-church-utica':'Address point for 240 Bleecker Street.',
 'oneida-county-courthouse-utica':'Address point for 200 Elizabeth Street.',
 'hotel-utica':'Address point for 102 Lafayette Street.',
 'olbiston-utica':'Address point for 1431 Genesee Street; the National Register point is 25 m away.',
 'utica-armory':'Address point for 1700 Parkway East.',
 'masonic-home-utica':'Address point for 2150 Bleecker Street, on the main care buildings; the chapel on the campus could not be picked out on the aerial.',
 'soldiers-monument-utica':'OpenStreetMap\'s point for Oneida Square, the traffic circle where the monument stands.',
 'baggs-square-east-utica':'National Register list point for the district.',
}
