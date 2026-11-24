# November 24, 2026: downtown Syracuse and the Syracuse University hill, New York: standing buildings named in a
# walking-tour video about the city, each checked against sources opened for this batch (the video itself is only a tip).
# Sources read: Wikipedia through tools/wiki_raw.py (the Syracuse Register list with --rows, and the buildings' own
# articles), Syracuse University Libraries' building histories, the Assumption parish's own pages, the Landmark
# Theatre's own page and a CNY Central report of July 2026 on the Mizpah. Interiors were not visited by any source
# opened unless the entry says so.
from data_b import N
from data_ma import W

def L(t,u):
    return [t,u]

BATCH={'key':'syrvid_ssav','label':'New York: downtown Syracuse and the university hill','added':'2026-11-24 10:38'}

SUL='https://library.syracuse.edu/special-collections-research-center/university-archives/buildings/'
SU_ACC='Syracuse University campus. The grounds are open to walk; the building is a working university building, and whether visitors may go in was not checked. Paid parking in university and city lots and garages nearby; street parking is metered.'
DT_ACC='Downtown Syracuse, on a city street. Metered street parking and paid lots and garages within a few blocks.'

PLACES=[
N('crouse-college-syracuse','Crouse College, Syracuse University','Syracuse','cny','civic','standing',43.03847,-76.13724,'exact','view','walk','','1888–1889',
  'A brownstone college hall on the hill above downtown, begun in 1888 and dedicated in September 1889. The banker John Crouse paid for it as a memorial to his late wife and named it a college for women; he died before it was finished, and his son completed it. Archimedes Russell designed it and the Norcross Brothers of Worcester built it. It now holds the university\'s music school and was listed on the National Register in 1974.',
  'Romanesque Revival walls of Longmeadow brownstone on a granite base, with carved musical instruments and an artist\'s palette over the front door, four chimneys and a bell tower. The university\'s history page says the inside has a carved wooden staircase up to a 700-seat auditorium, stained glass by the Syracuse craftsman Henry Keck, a rebuilt organ, and the first tower chimes in Syracuse. Interior access for visitors not checked.',
  '',SU_ACC,
  [W('Crouse College'),L('Syracuse University Libraries: Crouse College','https://library.syracuse.edu/special-collections-research-center/university-archives/buildings/crouse-college/')],brick='no'),
N('hendricks-chapel-syracuse','Hendricks Chapel, Syracuse University','Syracuse','cny','worship','standing',43.03763,-76.13512,'exact','view','walk','','1929–1930',
  'A domed, eight-sided chapel for all faiths at the head of the university\'s main quadrangle. The former mayor and state senator Francis Hendricks left $500,000 for it in memory of his wife Eliza Jane. The cornerstone was laid in June 1929 and it was dedicated in June 1930, designed by the New York architects John Russell Pope and Dwight James Baum. Seating 1,450, it was then the third largest university chapel in the country.',
  'Georgian Revival portico with columns under the dome; the university\'s history page gives the walls as Georgia limestone and brick. Its pulpit was the Class of 1918\'s gift and its organ is a 1952 Walter Holtkamp instrument. When it is open to visitors was not checked.',
  '',SU_ACC,
  [W('Hendricks Chapel'),L('Syracuse University Libraries: Hendricks Chapel','https://library.syracuse.edu/special-collections-research-center/university-archives/buildings/hendricks-chapel/')],brick='some'),
N('lyman-hall-syracuse','Lyman Hall (John Lyman Hall of Natural History)','Syracuse','cny','civic','standing',43.03845,-76.13191,'exact','view','walk','','1905–1907',
  'The university\'s natural history building, begun in 1905 and in use from 1907, paid for by a bequest from the trustee John Lyman in memory of his daughters. It held biology, botany, geology, zoology, psychology and geography, and a natural history museum on the top floor. In January 1937 a fire that began in a laboratory destroyed the top floor, the roof and much of the museum; the building was repaired by that September.',
  'A Renaissance-style hall on a marble base, built of brick and Indiana limestone, according to the university\'s history page. The first two floors were refitted in 2009. Interior not checked.',
  '',SU_ACC,
  [L('Syracuse University Libraries: Lyman Hall','https://library.syracuse.edu/special-collections-research-center/university-archives/buildings/lyman-hall')],brick='some'),
N('syracuse-city-hall','Syracuse City Hall','Syracuse','cny','civic','standing',43.05005,-76.14909,'exact','view','walk','','1889–1893',
  'The city hall of Syracuse, built from 1889 to 1893 in the Romanesque Revival style, which Wikipedia calls unusual for an American civic building. Hughes Brothers of Syracuse built it on a bid of $238,750. It is on the National Register.',
  'A stone hall with a tall corner tower on East Washington Street, still the seat of the city government. City offices are inside; their hours were not checked.',
  '',DT_ACC,
  [W('Syracuse City Hall')],brick='no'),
N('onondaga-county-courthouse-syracuse','Onondaga County Courthouse','Syracuse','cny','civic','standing',43.04639,-76.14806,'exact','view','walk','','1904–1907',
  'The county\'s fourth courthouse, opened on Columbus Circle in 1907 to replace the one on Clinton Square. Archimedes Russell designed it with Melvin King in the Beaux-Arts style. In 1915 it held the libel trial Barnes against Roosevelt. It stands in the Montgomery Street–Columbus Circle Historic District.',
  'A granite base with Indiana limestone above, a columned front with a pediment facing Columbus Circle, and a big copper dome with four smaller ones. Wikipedia says the building is round a central lightwell. It is a working courthouse; visitors go through the court\'s own entrance rules, which were not checked.',
  '',DT_ACC+' The courthouse faces Columbus Circle, a public square.',
  [W('Onondaga County Courthouse'),W('Montgomery Street–Columbus Circle Historic District')],brick='no'),
N('mizpah-tower-syracuse','First Baptist Church and Mizpah Tower','Syracuse','cny','worship','standing',43.04727,-76.14971,'exact','open','walk','','1912',
  'A Gothic church with a tall tower on Columbus Circle, dated 1912 in the Register\'s list for the Montgomery Street–Columbus Circle Historic District, which describes it as block veneer with religious and residential uses: the church below, rooms in the tower above. The First Baptist congregation itself goes back to 1821, according to an 1896 county history. In July 2026 the building reopened as a wine bar and private event hall named The Mizpah.',
  'Gothic church and tower faced in stone-like block, across Columbus Circle from the courthouse. CNY Central\'s July 2026 report says original architectural features were kept in the restoration. Opening hours were not checked.',
  '',DT_ACC+' The building is now a wine bar and event hall (The Mizpah, 350 Montgomery Street); check its own page for hours.',
  [W('Montgomery Street–Columbus Circle Historic District'),L('Onondaga\'s Centennial (1896): First Baptist Church','https://onondaga.nygenweb.net/CHURCH/SYR1STBA.HTM'),L('CNY Central: Inside the historic Mizpah\'s stunning transformation (July 2026)','https://cnycentral.com/newsletter-daily/inside-the-historic-mizpahs-stunning-transformation')],brick='no',hours='?'),
N('hotel-syracuse','Hotel Syracuse (Marriott Syracuse Downtown)','Syracuse','cny','hotel','standing',43.04469,-76.15119,'exact','open','walk','','1922–1924',
  'A big downtown hotel designed by William Stone Post of George B. Post & Sons, begun in 1922 and opened in August 1924. Charles Lindbergh spoke there in 1927. It closed in 2004 after bankruptcy, and after a $57 million restoration with 261 new rooms it reopened in August 2016 as the Marriott Syracuse Downtown.',
  'Wikipedia says the restoration returned the main historic rooms, among them the Grand Ballroom of 1924 and the lobby, to their old look. It is a working hotel.',
  '',DT_ACC+' A working hotel at 100 East Onondaga Street; its own page could not be opened when this was written.',
  [W('Marriott Syracuse Downtown')],brick='yes',hours='?'),
N('landmark-theatre-syracuse','Landmark Theatre (Loew\'s State Theatre)','Syracuse','cny','civic','standing',43.04731,-76.15261,'exact','open','walk','','1926–1928',
  'A movie palace by Thomas W. Lamb, announced by Loew\'s in February 1926 and opened as Loew\'s State on February 18, 1928, with vaudeville acts and films. It closed in 1975 and faced demolition; a citizens\' group bought it in 1977 and named it the Landmark. Wikipedia calls it the city\'s only surviving example of the grand theatres of the 1920s. It is on the National Register.',
  'Inside, the red and gold decoration and several large murals have been kept and restored; the Wurlitzer organ is gone. Wikipedia says the restored lobby is open only for events, so the way to see the inside is a ticket to a show.',
  '',DT_ACC+' A working theatre at 362 South Salina Street; its own page gives the box office hours.',
  [W('Landmark Theatre (Syracuse, New York)'),L('Landmark Theatre (its own page)','https://www.landmarktheatre.org/')],brick='no',hours='Box office Monday to Friday 10 a.m. to 5 p.m., and from two hours before curtain on show days'),
N('niagara-mohawk-building-syracuse','Niagara Mohawk Building','Syracuse','cny','civic','standing',43.05119,-76.15618,'exact','view','walk','','1932',
  'An Art Deco office tower finished in 1932 as the headquarters of the Niagara Hudson power company, then the largest electric utility in the country, designed by Melvin L. King with Bley and Lyman of Buffalo. Its stepped stories and lighting were meant as a symbol of electricity in the Depression years. The company is now part of National Grid.',
  'A 28-foot stainless steel winged figure, the Spirit of Light, stands on the front, with tube lights behind chrome panels between the display windows. The exterior lighting, dark in the war, was restored in 1999 and again in 2024, so the building is best seen after dark. Offices; interior not checked.',
  '',DT_ACC+' Seen from Erie Boulevard West.',
  [W('Niagara Mohawk Building')],brick='no'),
N('syracuse-savings-bank-building','Syracuse Savings Bank Building','Syracuse','cny','civic','standing',43.0511,-76.15168,'exact','view','walk','','1875–1876',
  'A Gothic bank tower by Joseph Lyman Silsbee, built in 1875 beside the Erie Canal and opened in 1876. At 171 feet it was the tallest building in Syracuse, and its passenger elevator, the first in the city, drew sightseers. It is on the National Register.',
  'The tower stands on Clinton Square, across Erie Boulevard, the old canal, from the Gridley Building. Interior not checked.',
  '',DT_ACC+' Clinton Square is a public square.',
  [W('Syracuse Savings Bank Building')],brick='no'),
N('gridley-building-syracuse','Gridley Building (Onondaga County Savings Bank)','Syracuse','cny','civic','standing',43.05076,-76.15176,'exact','view','walk','','1867',
  'A bank built in 1867 for the Onondaga County Savings Bank beside what was then the Erie Canal, on Clinton Square and Hanover Square, designed by Horatio Nelson White, who also designed the university\'s Hall of Languages. It was later M&T Bank\'s regional offices at 101 South Salina Street; M&T agreed in January 2020 to sell it to Douglas Development and moved out that year. It is on the National Register.',
  'A stone bank with a corner tower. M&T\'s 2020 announcement quotes the buyer calling the old banking hall magnificent and planned as event space. Interior not checked.',
  '',DT_ACC+' Clinton Square is a public square.',
  [W('Gridley Building'),L('M&T Bank: Douglas Development to purchase Salina Street landmark (January 2020)','https://newsroom.mtb.com/2020-01-21-Douglas-Development-to-Purchase-Salina-Street-Landmark-in-Downtown-Syracuse')],brick='no'),
N('third-national-bank-syracuse','Third National Bank (Community Chest Building)','Syracuse','cny','civic','standing',43.05143,-76.15185,'exact','view','walk','','1885',
  'A bank on James Street designed by Archimedes Russell in 1885, later called the Community Chest Building. It was listed on the National Register in 1972.',
  'A Queen Anne bank front just north of Clinton Square. Interior not checked.',
  '',DT_ACC,
  [W('Third National Bank (Syracuse, New York)')],brick='yes'),
N('assumption-church-syracuse','Franciscan Church of the Assumption','Syracuse','cny','worship','standing',43.06263,-76.15424,'exact','open','walk','','1865–1872',
  'The church of a parish founded in 1845 by German Catholic families on the North Side, served by the Franciscan Friars Conventual, whose St. Francis Friary of 1859 adjoins it. The parish\'s own history says the present church was built between 1865 and 1872 and dedicated on May 5, 1867; the Register description of the North Salina Street Historic District dates it about 1880 and names Horatio N. White as its architect. The two dates are not reconciled here.',
  'A large church on North Salina Street with the friary beside it. Interior not checked. The parish runs a food pantry and soup kitchen.',
  '',DT_ACC.replace('Downtown Syracuse','The North Side of Syracuse')+' Parish church at 812 North Salina Street; the parish page gives Sunday Mass at 10 a.m.',
  [L('Assumption Church: our history','https://assumptionsyr.org/history'),L('Assumption Church: Mass','https://assumptionsyr.org/mass'),W('North Salina Street Historic District')],conf='mixed',brick='?',hours='Sunday Mass 10 a.m.'),
]

PIN_NOTES={
 'crouse-college-syracuse':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'hendricks-chapel-syracuse':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'lyman-hall-syracuse':'OpenStreetMap building, 100 College Place; the aerial shows the pin on the building.',
 'syracuse-city-hall':'OpenStreetMap town hall, 233 East Washington Street; the aerial shows the pin on the building.',
 'onondaga-county-courthouse-syracuse':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'mizpah-tower-syracuse':'OpenStreetMap building, 350 Montgomery Street; the aerial shows the pin on the building.',
 'hotel-syracuse':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'landmark-theatre-syracuse':'OpenStreetMap theatre, 362 South Salina Street; the aerial shows the pin on the building.',
 'niagara-mohawk-building-syracuse':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'syracuse-savings-bank-building':'Wikipedia article coordinate; the aerial shows the pin on the building.',
 'gridley-building-syracuse':'OpenStreetMap building; the aerial shows the pin on the building.',
 'third-national-bank-syracuse':'OpenStreetMap building, James Street; the aerial shows the pin on the building.',
 'assumption-church-syracuse':'OpenStreetMap place of worship on North Salina Street; the aerial shows the pin on the building.',
}
