# November 24, 2026: Worcester, Massachusetts. A "videos" session (PROMPTS.md job 9): the names came from one video's
# tour of old Worcester buildings (the record is source/videos/20240809_cnGGQsNrjhQ.md); the video is a tip and nothing
# here rests on it. Sources read: Wikipedia (each article named in the links), the Register lists for Worcester,
# Lost New England (lostnewengland.com) on the armory, Central Church and Boynton Hall, Historic Buildings of
# Massachusetts on the armory, WPI's own historic-district exhibit, and the pages of the American Antiquarian Society,
# Mechanics Hall, the Worcester Art Museum and the City of Worcester for hours. The cathedral's own site refused every
# request, so no church hours are given.
# Pins are address-lookup points (PointAddress), OpenStreetMap building points or a Wikipedia point, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'worcvid_ktht','label':'Massachusetts: old Worcester, from the Common to Salisbury Street','added':'2026-11-24 20:33'}

PEARL=[42.26445,-71.80290]
PEARLN='Pearl-Elm Municipal Garage, Pearl Street'
DT=' Downtown street parking and city garages are close by; their hours and fees were not checked.'

PLACES=[
N('antiquarian-hall-worcester','Antiquarian Hall (American Antiquarian Society)','Worcester','worc','civic','standing',42.27723,-71.81029,'exact','open','walk','','1910',
  'The American Antiquarian Society was founded in 1812 and is the oldest historical society in the United States with a national scope; it collects everything printed in what is now the United States up to 1900. Its first library went up downtown in 1820 and a second at Highland Street in 1853. The present building, Antiquarian Hall, was designed by Winslow, Bigelow & Wadsworth in the Georgian Revival style and finished in 1910, and has been added to several times since. It is a National Historic Landmark.',
  'A domed Georgian Revival library at the corner of Park Avenue and Salisbury Street. The free public tour may take in the printing press, the conservation lab, the stacks and the reading room. The reading room is free for anyone over 18 with a reason to use the collections; the stacks are closed.',
  '',
  'Owned and run by the American Antiquarian Society, 185 Salisbury Street. Free public tours of the hall every Wednesday at 3 p.m.; groups under ten need not register (the society\'s tours page). Reading room hours were not checked on the society\'s own page. Parking was not checked; street parking on Salisbury Street and Park Avenue.',
  [W('American Antiquarian Society'),['American Antiquarian Society: public tours','https://www.americanantiquarian.org/visit/public-tours']],
  brick='?',hours='Free public tour Wednesdays at 3 p.m.'),

N('worcester-armory-salisbury-street','Worcester National Guard Armory','Worcester','worc','fort','standing',42.27363,-71.80065,'exact','view','walk','','1889–1890',
  'A castle-like armory built in 1889 and 1890 to replace the Waldo Street Armory, which had developed structural faults. Fuller & Delano designed it, and the rear addition of 1907. In 1994 it was refitted to hold the National Guard Museum and Archives; the museum moved to Concord in 2013, and in 2014 the building passed to Veterans, Inc., which serves homeless veterans and had leased part of it since 1991.',
  'Romanesque walls, turrets and a central tower that was cut down from its first height; apart from that tower the outside is little changed. It is a contributing building in the Institutional District on the National Register. Interior not checked.',
  '',
  'Owned by Veterans, Inc., at 44 Salisbury Street on the corner of Grove Street; not open to visitors. Look from Salisbury and Grove streets. Parking was not checked; street parking nearby.',
  [['Lost New England: National Guard Armory, Worcester','https://lostnewengland.com/2016/09/national-guard-armory-worcester-mass/'],['Historic Buildings of Massachusetts: Worcester National Guard Armory','https://mass.historicbuildingsct.com/?p=5234']],
  brick='yes'),

N('worcester-art-museum','Worcester Art Museum','Worcester','worc','civic','standing',42.27306,-71.80204,'exact','open','walk','','1897–1898',
  'Founded in 1896 by Stephen Salisbury III and friends, on land from the old Salisbury farm, and opened in 1898. The first building, a small three-story block by Stephen C. Earle, was built by the Norcross Brothers in 1897 and 1898 and was always meant to be one part of a much larger building. The big wing facing Salisbury Street, with the Chapter House and the Renaissance Court, was added in 1931 to 1933 to designs by William Truman Aldrich, and a fourth floor went on the first building in 1939 and 1940.',
  'Little of the 1898 building shows outside now. Inside are a whole medieval Chapter House brought over and rebuilt in 1932, Roman mosaics in the Renaissance Court floor, and, since 2013, the Higgins armor collection.',
  '',
  'Run by the Worcester Art Museum, 55 Salisbury Street; an admission fee, members free. The museum\'s visit page gives several free parking options for visitors and says renovations are under way. Closed Monday and Tuesday and on New Year\'s Day, Easter, Independence Day, Thanksgiving and Christmas.',
  [W('Worcester Art Museum'),['Worcester Art Museum: visit','https://www.worcesterart.org/visit/']],
  brick='?',hours='Wednesday to Sunday 10 a.m. to 4 p.m.'),

N('cathedral-st-paul-worcester','Cathedral of Saint Paul','Worcester','worc','worship','standing',42.2616,-71.8043,'exact','view','walk','','1868–1874',
  'The mother church of the Catholic Diocese of Worcester, a Gothic Revival church by E. Boyden & Son. The dates are not settled: Wikipedia\'s article gives 1874 as the year it was completed and also says it was built between 1868 and 1889. It was listed on the National Register in 1980.',
  'A cross-shaped church of rock-faced granite, 168 feet long, with a tall square tower on the right of the front and a smaller tower with a round turret on the left. Inside, a green and white marble altar with a Last Supper carved on its front, and the bishop\'s chair before a carved oak reredos. A statue of St. Francis stands in the small courtyard. Whether it opens outside Mass times was not checked.',
  '',
  'An active cathedral of the Diocese of Worcester, at 38 Chatham Street on the corner of High Street, one block west of Main Street. The cathedral\'s own site could not be opened when this was written, so Mass times were not checked. Look from Chatham Street.'+DT,
  [W('Cathedral of Saint Paul (Worcester, Massachusetts)'),['Cathedral of Saint Paul (official site)','https://cathedralofsaintpaul.net/']],
  brick='no',conf='mixed'),

N('worcester-city-hall','Worcester City Hall','Worcester','worc','civic','standing',42.26256,-71.80196,'exact','open','walk','','1898',
  'Designed by Peabody & Stearns and built by the Norcross Brothers in 1898, on the spot where the town\'s meeting houses had stood since 1719: in the Old South Meeting House on this site Isaiah Thomas read the Declaration of Independence on July 14, 1776, the first public reading in New England. That meeting house was pulled down in the 1890s. City Hall and the Common were listed on the National Register in 1978.',
  'A granite building modeled partly on Italian Renaissance palaces, with a tower like that of the Palazzo Vecchio in Florence. Inside, much marble and a central court with balconies on arches on the upper floors. On the Common behind it: the old burying ground with the Bigelow Monument, the Civil War Soldiers\' Monument and the Burnside Fountain ("Turtle Boy").',
  '',
  'Owned by the City of Worcester, 455 Main Street; the building is open for city business on weekdays (the city\'s contact page). The accessible entrance faces the Common. The Common is a public park.'+DT,
  [W('Worcester City Hall and Common'),['City of Worcester: contact and hours','https://worcesterma.gov/contact-us']],
  th=PEARL,thn=PEARLN,brick='no',hours='Monday to Friday 8:30 a.m. to 5 p.m.'),

N('union-congregational-church-worcester','Union Congregational Church','Worcester','worc','worship','standing',42.26429,-71.80494,'exact','view','walk','','1895–1897',
  'Also called the Chestnut Street Congregational Church. Designed by Earle & Fisher and built from 1895 to 1897, a Victorian Gothic church whose front recalls Notre Dame de Paris on a small scale. Some of its stained glass came from the churches of congregations that merged into the Union congregation. It was listed on the National Register in 1980.',
  'Twin towers flank three trefoil-arched doors, with a large rose window above and an arcade joining the towers; the open belfries have paired pointed openings, battlements and gargoyles. The slate roof was replaced in 1948. Present use and interior not checked.',
  '',
  'At 5 Chestnut Street. Who now uses it and whether it opens to visitors were not checked; look from Chestnut Street.'+DT,
  [W('Union Congregational Church (Worcester, Massachusetts)')],
  brick='?'),

N('central-congregational-church-worcester','Central Congregational Church (former)','Worcester','worc','worship','standing',42.27253,-71.80076,'exact','view','walk','','1884–1885',
  'Built for a congregation founded in 1820 that moved out of the crowded city center to Wheaton Square. Stephen C. Earle designed it in the Romanesque style, and it went up in 1884 and 1885 (some sources give 1886). Central Church merged with the Chestnut Street (Union) congregation in 1982 as the United Congregational Church, and in 2010 that congregation voted to give this building and its endowment to a mission society.',
  'Walls of Longmeadow brownstone, a tower and smaller turrets, round arches and stained glass. The street scene round Wheaton Square, with the armory, the 1891 historical society building and the 1889 North High School, is almost as it was in about 1906. A commenter on Lost New England reported that the inside was stripped after Central left; interior not checked.',
  '',
  'At 6 Institute Road, at Grove Street; private, look from the street. A contributing building in the Institutional District on the National Register. Parking was not checked; street parking nearby.',
  [['Lost New England: Central Congregational Church','https://lostnewengland.com/?p=5916'],['College of the Holy Cross: Stephen C. Earle\'s Romanesque Revival architecture','https://college.holycross.edu/projects/ArtandChurch1900/Central_Con_1.html']],
  brick='no',conf='mixed'),

N('donohue-federal-building-worcester','Harold D. Donohue Federal Building and Courthouse','Worcester','worc','civic','standing',42.26047,-71.80383,'exact','view','walk','','1930–1931',
  'Built in 1930 and 1931 as Worcester\'s U.S. Post Office and Courthouse, under the Public Buildings Act of 1926, to a design approved by Louis A. Simon of the Supervising Architect\'s office. It stands on the site of the 1897 post office, which was demolished to make room for it. It holds the only seat of the federal district court in Worcester.',
  'A five-story building mixing Classical and Renaissance Revival styles. Interior not checked.',
  '',
  'A working federal courthouse at 595 Main Street, with security screening at the door; look from Main Street.'+DT,
  [W('Harold D. Donohue Federal Building and United States Courthouse')],
  brick='?'),

N('mechanics-hall-worcester','Mechanics Hall','Worcester','worc','civic','standing',42.26558,-71.80071,'exact','open','walk','','1857',
  'Built in 1857 by the Worcester Mechanics Association, formed by workers in 1842, to house classes and cultural events. Its third-floor concert hall drew speakers and performers from Charles Dickens and Susan B. Anthony to Caruso and Ella Fitzgerald. It declined in the twentieth century and was restored in 1977 with $5 million raised in the city.',
  'A Renaissance Revival hall whose great room keeps the 1864 Hook organ, "The Worcester Organ", the oldest unaltered four-keyboard organ in the Western Hemisphere still where it was installed, with 52 stops and 3,504 pipes; it was restored in 1982 and again in 2014. The inside is seen at concerts and events, and the hall offers guided tours (dates on its calendar).',
  '',
  'Run by Mechanics Hall, 321 Main Street; tickets for events, by phone, at the box office or online. Directions and parking are on the hall\'s visit page; parking was not checked here.',
  [W('Mechanics Hall (Worcester, Massachusetts)'),['Mechanics Hall: visit','https://mechanicshall.org/visit/']],
  th=PEARL,thn=PEARLN,brick='?',hours='Box office Wednesday to Friday 11 a.m. to 5 p.m.; concerts and events on the hall\'s calendar'),

N('pilgrim-congregational-church-worcester','Pilgrim Congregational Church','Worcester','worc','worship','standing',42.25196,-71.81850,'exact','view','walk','','1887',
  'A brick Romanesque Revival church built in 1887 to designs by the Worcester architect Stephen Earle, on Main Street in the Main South neighborhood. It was listed on the National Register in 1980.',
  'Brick walls trimmed in sandstone round the windows, and a corner tower with rounded projecting corners, an open belfry of round arches and a steep roof with finials at its corners. Present use and interior not checked.',
  '',
  'At 909 Main Street; who now uses it and whether it opens to visitors were not checked. Look from Main Street; street parking nearby, not checked.',
  [W('Pilgrim Congregational Church (Worcester, Massachusetts)')],
  brick='yes'),

N('slater-building-worcester','Slater Building','Worcester','worc','civic','standing',42.26437,-71.80227,'exact','view','walk','','1907',
  'A ten-story office building at 390 Main Street, built in 1907 by the Norcross Brothers and the second skyscraper in Worcester, after the Second State Mutual Life building at 340 Main Street. Its inner workings were brought up to date in 1939 by Frost, Chamberlain & Edwards, who were tenants. It was listed on the National Register in 1980.',
  'A steel frame faced with granite on the two lowest floors and limestone above. The top two floors are set off by a trim line and have a recessed loggia framed by Corinthian columns. Interior not checked.',
  '',
  'A private office building; look from Main Street.'+DT,
  [W('Slater Building (Worcester, Massachusetts)')],
  th=PEARL,thn=PEARLN,brick='no'),

N('union-station-worcester','Union Station','Worcester','worc','rail','standing',42.26119,-71.79500,'exact','open','walk','','1911',
  'Worcester\'s second union station, opened on June 4, 1911, to designs by Watson & Huckel in a French Renaissance Revival style. It replaced the 1875 Ware & Van Brunt station east of Washington Square, which had a clock tower 212 feet tall. Two 175-foot white marble towers flanked the entrance until 1926, when they were taken down for structural reasons. Penn Central and Amtrak left the main building empty; it was listed on the National Register in 1980 while abandoned, and was later restored by Finegold Alexander & Associates.',
  'The Grand Hall, the first waiting room, has its elliptical stained-glass ceilings, marble columns and mahogany trim restored. The two towers are fiberglass copies of the ones removed in 1926.',
  '',
  'A working station of the MBTA commuter rail (Framingham/Worcester line) and Amtrak\'s Lake Shore Limited, with the city bus hub beside it, at 2 Washington Square. The station\'s opening hours were not checked on its operator\'s page. OpenStreetMap shows MBTA commuter parking on Shrewsbury Street, close by; its fees were not checked.',
  [W('Union Station (Worcester, Massachusetts)')],
  brick='?',hours='?'),

N('fenwick-hall-holy-cross','Fenwick and O\'Kane Halls, College of the Holy Cross','Worcester','worc','inst','standing',42.23918,-71.80795,'exact','view','walk','','1843–1895',
  'The College of the Holy Cross, founded in 1843 by Bishop Benedict Joseph Fenwick, was the first Catholic college in New England. Its first main building, later called Fenwick Hall, was finished in January 1844 and its east wing in 1846; a fire in 1852 badly damaged the main part, which was rebuilt. O\'Kane Hall was added in 1891 to 1895, attached at a right angle, and for many years the two held the whole college. The pair was listed on the National Register in 1980.',
  'A long range on the hill mixing Second Empire, Gothic, Classical, Romanesque and Renaissance details, with O\'Kane\'s clock tower over Linden Lane, which runs in from the main gate on College Street. The former chapel in Fenwick is now Brooks Recital Hall and keeps its large stained-glass windows. Interior otherwise not checked.',
  '',
  'Owned by the College of the Holy Cross, 1 College Street. The college\'s rules for visitors on campus were not checked; look from Linden Lane and College Street. The college\'s visitor and employee parking is the Lower Hogan lot on Mahoney Way.',
  [W('College of the Holy Cross')],
  th=[42.23665,-71.80785],thn='Lower Hogan visitor lot, Mahoney Way',brick='yes'),

N('boynton-hall-wpi','Boynton Hall, Worcester Polytechnic Institute','Worcester','worc','inst','standing',42.27348,-71.80735,'exact','view','walk','','1868',
  'The first building of Worcester Polytechnic Institute, dedicated in 1868 and named for John Boynton, the tinware maker who gave his savings of $100,000 to found the school on condition that the people of Worcester gave the land and the granite. Stephen Earle designed it (WPI\'s pages also name James E. Fuller with him) in the Gothic Revival style, and it held classrooms and laboratories, while the Washburn Shops beside it held the workshops. It is now the institute\'s main administration building.',
  'Granite walls and a clock tower, one of WPI\'s "two towers" with the Washburn Shops, standing for theory and practice. Interior not checked.',
  '',
  'Owned by Worcester Polytechnic Institute, 100 Institute Road. The institute\'s rules for visitors on campus were not checked; look from Institute Road. Parking was not checked.',
  [W('Worcester Polytechnic Institute'),['WPI Digital Exhibits: Boynton Hall (1868)','https://exhibits.wpi.edu/spotlight/wpi-historic-district/feature/boynton-hall-1868'],['Lost New England: Boynton Hall','https://lostnewengland.com/2016/09/boynton-hall-worcester-mass/']],
  brick='no'),
]

PIN_NOTES={
 'antiquarian-hall-worcester':'Address lookup of 185 Salisbury Street (a match on the house number).',
 'worcester-armory-salisbury-street':'Address lookup of 44 Salisbury Street (a match on the house number).',
 'worcester-art-museum':'Address lookup of 55 Salisbury Street (a match on the house number).',
 'cathedral-st-paul-worcester':'Wikipedia\'s point for the cathedral; the address lookup of 38 Chatham Street fell along the street to the west.',
 'worcester-city-hall':'Address lookup of 455 Main Street (a match on the house number).',
 'union-congregational-church-worcester':'Address lookup of 5 Chestnut Street (a match on the house number).',
 'central-congregational-church-worcester':'Address lookup of 6 Institute Road (a match on the house number).',
 'donohue-federal-building-worcester':'Address lookup of 595 Main Street (a match on the house number).',
 'mechanics-hall-worcester':'Address lookup of 321 Main Street (a match on the house number).',
 'pilgrim-congregational-church-worcester':'Address lookup of 909 Main Street, which fell in the street; moved about 20 m onto the church as seen on the aerial.',
 'slater-building-worcester':'Address lookup of 390 Main Street (a match on the house number).',
 'union-station-worcester':'Address lookup of 2 Washington Square (a match on the house number).',
 'fenwick-hall-holy-cross':'OpenStreetMap\'s outline of Fenwick Hall.',
 'boynton-hall-wpi':'OpenStreetMap\'s outline of Boynton Hall.',
}
