# November 26, 2026: Schenectady, from the names in one Old World Exploration video about the city (the video is only a
# tip; every fact below is from a source opened for this batch). Most buildings it shows were already on the Atlas or are
# gone; these five were not: the old YMCA, the two county courthouses, St. John the Evangelist Church and the Masonic
# temple at State Street and Erie Boulevard.
# Sources: Wikipedia as raw text; the Historical Society of the New York Courts' county legal history of Schenectady
# (PDF, text layer read); Schenectady HistoryForge; Buildings of New England; the parish's own site; the Schenectady
# Metroplex Development Authority; OpenStreetMap for the positions.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'sch_vid_smzo','label':'Schenectady: the old YMCA, the two courthouses, St. John the Evangelist and the Masonic temple','added':'2026-11-26 04:33'}
COURTS=L('Historical Society of the New York Courts: Schenectady County legal history (PDF; "Courthouse" chapter)','https://history.nycourts.gov/wp-content/uploads/2023/02/County-Legal-History_Schenectady-min.pdf')
PLACES=[
N('ymca-schenectady-13-state-street','Young Men\'s Christian Association building (13 State Street Apartments)','Schenectady','sch','civic','standing',42.81545,-73.94868,'site','view','walk','','1926–1928',
  'Schenectady\'s YMCA built this four-story red brick building with cast stone trim between 1926 and 1928, and added to it in 1968. The YMCA stayed until 2014, and the building went on the National Register in 2015. It has since been turned into apartments.',
  'A long red brick front on lower State Street with twin main entrances and a raised two-story verandah on heavy wooden columns; the upper floors are E-shaped behind. Private apartments: see it from the street. Interior not checked.',
  '',
  'Private apartment building at 13 State Street, at the foot of State Street by the Stockade. Street parking.',
  [W('YMCA of Schenectady')],
  brick='yes'),
N('old-schenectady-county-courthouse','Old Schenectady County Courthouse (108 Union Street)','Schenectady','sch','civic','standing',42.8163,-73.94644,'site','view','walk','','1831–1833',
  'Schenectady County was split from Albany County in 1809 and held court in borrowed rooms until this courthouse and jail went up in 1831 to 1833, to a design by John W. Teller. Until 1881 it was also the city hall. It served the county for eighty years, until the new courthouse on State Street opened in 1913; afterwards it was the city school department\'s headquarters and then offices. The courts\' historical society says it is owned by MVP; another history page calls it apartments today.',
  'A two-story Greek Revival temple front on Union Street in the Stockade: Doric columns on an Onondaga limestone base, bluestone steps, triglyphs in the cornice and pediment, and painted brick walls. The front door keeps its original transom and sidelights; the doors themselves are later. Private: see it from the street. Interior not checked.',
  'The county\'s first purpose-built courthouse, 1833.',
  'Private building at 108 Union Street, in the Stockade Historic District. Street parking.',
  [COURTS,L('Schenectady HistoryForge: 108 Union St (description of the building)','https://schenectady.historyforge.net/buildings/56')],
  brick='no'),
N('schenectady-county-courthouse-612-state','Schenectady County Courthouse (612 State Street)','Schenectady','sch','civic','standing',42.81049,-73.93978,'site','view','walk','','1913',
  'Built as part of the city\'s centennial, this courthouse took three and a half years and was finished in 1913, when it replaced the old courthouse on Union Street. The architects were Stoddart and Weathers and the builder John McDermott. It is in the Classical Revival style and is still the county\'s courthouse; the main courtroom was named for Judge Howard A. Levine in 2021.',
  'A Classical Revival courthouse on State Street across from Crescent Park. The Joseph F. Egan Memorial Library of the county bar is on its third floor. It is a working court building; interior not checked.',
  '',
  'Schenectady County\'s working courthouse at 612 State Street. See it from the street; visiting hours not checked. Street and garage parking downtown.',
  [COURTS],
  brick='?'),
N('st-john-the-evangelist-schenectady','St. John the Evangelist Church','Schenectady','sch','worship','standing',42.81423,-73.93182,'exact','open','walk','','1898–1900s',
  'Monsignor John L. Reilly began the church in 1898, buying land across Union Street from Union College and collecting money for a church fit for the city; he went to Europe for ideas. Edward Loth of Troy designed it. The church is about 120 by 130 feet, with a small tower at each corner and a central spire 230 feet high, which was built of steel and glass to light the sanctuary and has since been covered with a metal roof. It is still a Catholic parish church. Buildings of New England calls it a stone church, but a 2013 photograph of one of its corner towers shows red brick walls under a green roof; what it is built of was not settled.',
  'The huge four-towered church on Union Street opposite Union College, in the Union Street Historic District. Open for Mass (times below); interior not checked.',
  'Four corner towers and a 230-foot central spire, opposite Union College.',
  'St. John the Evangelist Church, 806 Union Street (parish mailing address; the church is at the corner by the parish school), a parish of the Catholic Diocese of Albany. Mass times from the parish\'s own site (read November 26, 2026). Street parking.',
  [L('St. John the Evangelist Church (Mass times)','https://sjechurch.com'),L('Buildings of New England: St. John the Evangelist Church','https://buildingsofnewengland.com/2021/05/16/st-john-the-evangelist-church-1900/'),L('Wikimedia Commons: statue of St. John before a corner tower of the church (2013)','https://commons.wikimedia.org/wiki/File:%22I_love_my_new_iPad%E2%80%A6%22_(8849936908).jpg')],
  conf='mixed',brick='some',hours='Saturday vigil Mass 4 p.m.; Sunday Mass 10:30 a.m.'),
N('st-georges-masonic-temple-schenectady','St. George\'s Masonic Temple (302 State Street)','Schenectady','sch','civic','standing',42.81394,-73.94388,'site','view','walk','','1911',
  'The building on the corner of State Street and Erie Boulevard was put up in 1911 as Brown\'s furniture store, on the bank of the Erie Canal, and later became the temple and club of St. George\'s Lodge No. 6 of the Masons. In 2025 the state announced that it would go on the State and National Registers, and the city and county said the tax credits would help renovate it. When the Masons left and how long it has stood empty were not confirmed.',
  'A five-story L-shaped brick building with its main front on State Street and a temple-style entrance at the back corner facing Erie Boulevard. It was empty and waiting for renovation when last reported; see it from the street. Interior not checked.',
  '',
  'Privately owned building at 302 State Street, corner of Erie Boulevard. See it from the street. Street and garage parking downtown.',
  [L('Schenectady Metroplex Development Authority: statement on the Masonic building\'s historic designation','https://schenectadymetroplex.com/?p=9305'),L('National Register nomination: St. George\'s Lodge No. 6 Masonic Temple and Club (PDF; could not be opened when this was written)','https://www.parks.ny.gov/documents/shpo/national-register/StGeorgesLodgeNo6MasonicTempleandClubSchenectadySchenectadyCo.pdf')],
  conf='mixed',brick='?'),
]
PIN_NOTES={
 'ymca-schenectady-13-state-street':'OpenStreetMap address point for 13 State Street; on the leaf-off aerial it falls on the long building on the north side of State Street.',
 'old-schenectady-county-courthouse':'OpenStreetMap address point for 108 Union Street; on the leaf-off aerial it falls on the building at that address.',
 'schenectady-county-courthouse-612-state':'OpenStreetMap courthouse named Schenectady County Court House, 612 State Street; on the leaf-off aerial it falls on the courthouse facing Crescent Park.',
 'st-john-the-evangelist-schenectady':'OpenStreetMap place of worship named Saint John the Evangelist Catholic Church on Union Street; on the leaf-off aerial it falls on the cross-shaped church.',
 'st-georges-masonic-temple-schenectady':'OpenStreetMap address point for 302 State Street, at the corner of Erie Boulevard; on the leaf-off aerial it falls on the corner building.',
}
