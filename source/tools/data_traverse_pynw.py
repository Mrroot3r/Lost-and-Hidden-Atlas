# November 27, 2026: Traverse City, Michigan. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Traverse City buildings (the record is source/videos/20251017_ti6FAoC4260.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), SAH Archipedia (Buildings of Michigan, 2012),
# The Ticker (Traverse City) news reports, American Courthouses, and for hours and services the pages of Grand Traverse
# County, the City of Traverse City, The Village at Grand Traverse Commons and Central United Methodist Church.
# Pins are street-address points and OpenStreetMap features, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'traverse_pynw','label':'Michigan: old Traverse City','added':'2026-11-27 01:39'}

DT=' Downtown parking is in city lots, ramps and street meters; their hours and fees were not checked.'
SAH='https://sah-archipedia.org/buildings/MI-01-'
TICK='https://www.traverseticker.com/news/'

PLACES=[

N('grand-traverse-commons-building-50','Northern Michigan Asylum (Building 50, Grand Traverse Commons)','Traverse City','mi','inst','standing',44.75513,-85.64250,'exact','open','walk','','1883–1885',
  'The Northern Michigan Asylum, later the Traverse City State Hospital, was the state\'s third asylum, voted in 1881 to relieve crowding at Kalamazoo and Pontiac; Perry Hannah used his influence to bring it to his town. The Detroit architect Gordon W. Lloyd drew the main building, Building 50, on the Kirkbride plan: a long, shallow V of wards stepping back from a central administration block so every ward looked toward Grand Traverse Bay. Building began in April 1883 and the first patients came in November 1885; cottages, infirmaries and a farm followed. The 1885 centre was pulled down in 1963 as a fire hazard and replaced by a modern block. The hospital closed in 1989, and since 2002 the Minervini Group has turned Building 50 and the cottages into homes, shops and restaurants as The Village at Grand Traverse Commons.',
  'A three-storey Italianate front of pale yellowish brick with sandstone window caps, belt courses and brackets, on a rock-faced stone base; the two long wings stand, while the middle is the 1960s replacement. The redevelopment\'s history page puts the bricks for the main building at over eight million, from the brickyard at Cedar Lake; Buildings of Michigan says the brick came from yards in Greilickville. The shops and restaurants inside are open to all. Guided tours take visitors through an unrenovated patient cottage and an 1883 brick steam tunnel.',
  'The tunnels under the asylum are on the guided tour.',
  'Privately owned and redeveloped by the Minervini Group as The Village at Grand Traverse Commons, off West Eleventh Street; parking lots round Building 50. Guided tours (2 hours, $30, ages 12 and over; evening and golf-cart tours too) are booked through The Village\'s tour page, which publishes dates one to two months ahead. The hospital farm is now Historic Barns Park, run by Garfield Township. Do not enter closed or unrenovated buildings except on a tour.',
  [W('Traverse City State Hospital'),['SAH Archipedia: Grand Traverse Commons',SAH+'GT8'],['The Village at Grand Traverse Commons: history','https://www.thevillagetc.com/history'],['The Village: tours','https://www.thevillagetc.com/tour']],
  th=[44.75596,-85.64364],thn='Lot off Cottageview Drive, behind Building 50',
  brick='no',bcol='buff',hours='Guided tours on dates published one to two months ahead; shops keep their own hours'),

N('perry-hannah-house-traverse-city','Perry Hannah House','Traverse City','mi','landmark','standing',44.76138,-85.62661,'exact','view','walk','','1891–1893',
  'The retirement house of Perry Hannah (1824–1904), the lumberman whose firm Hannah, Lay and Company logged the Grand Traverse country from 1851 and later went into banking and a department store. The Grand Rapids architect William G. Robinson designed it in 1891 and it was finished in 1893: a three-storey Queen Anne house of more than forty rooms, every room panelled in a different wood. After the family could no longer keep it, it passed through the American Legion to a funeral home; the Reynolds-Jonkhoff Funeral Home has used and kept it since 1976. A Michigan State Historic Site since 1971 and on the National Register since 1972.',
  'Round corner turrets, cross gables, carved and inlaid wooden festoons and crests along the bargeboards and window surrounds, and a wide sweeping porch. Inside, a curved staircase with a balcony climbs from the lower hall; the hardwood rooms are a working funeral home and were not checked for visiting. A two-and-a-half-storey carriage house stands behind.',
  '',
  'A working funeral home at 305 Sixth Street, by Hannah Park; seen from the street. It is not a museum.'+DT,
  [W('Perry Hannah House'),['SAH Archipedia: Perry and Anna Hannah House',SAH+'GT7']],
  brick='?'),

N('city-opera-house-traverse-city','City Opera House','Traverse City','mi','civic','standing',44.76379,-85.62344,'exact','open','walk','','1891',
  'A Richardsonian Romanesque commercial block with an opera house on its upper floors, built in 1891 for three merchants, Charles Wilhelm, Anton Bartak and Frank Votruba, on a site bought from Perry Hannah, to plans by Edwin R. Prall of Pontiac. Shops on the street floor paid toward the theatre above. A movie-house chain leased it in 1920 and shut it to stop the competition; it stayed closed until the 1980s. The owners gave it to the city in 1980, and a long restoration was largely finished in the 2000s. Wikipedia and Buildings of Michigan give 1891 for the opening; the opera house\'s own page says 1892.',
  'Three storeys of red brick and sandstone on Front Street, with three shopfronts below. Upstairs the theatre has eight barrel vaults and a dome with painted clouds and cherubs, and a balcony sweeping round; the floor can be cleared of seats for dances. The public goes in for performances and events.',
  '',
  'Owned by the City of Traverse City and run as a performing-arts and events hall at 106–112 East Front Street; the entrance and stairs are in the storefront to the west. No public opening hours were found on its page: go to a show or event.'+DT,
  [W('City Opera House (Traverse City, Michigan)'),['SAH Archipedia: City Opera House',SAH+'GT4'],['City Opera House: about','https://www.cityoperahouse.org/about']],
  brick='yes',bcol='red',hours='?'),

N('grand-traverse-county-courthouse','Grand Traverse County Courthouse','Traverse City','mi','civic','standing',44.76134,-85.61645,'exact','open','walk','','1898–1900',
  'The county\'s first courthouse and jail, built in 1854 on land given by Hannah, Lay and Company, burned in 1862, and the county rented rooms for the next generation. In 1898 it took plans by Rush, Bowman and Rush of Grand Rapids, but after a quarrel over costs the board brought in Cassius M. Prall, then building at the asylum, to finish the job; the courthouse was completed in 1900. Beside it stood the county jail and sheriff\'s house of 1882–1883, now gone. After a new city-county government centre was built nearby, the courthouse was renovated in 1979–1981 for the courts.',
  'A red brick and sandstone Richardsonian Romanesque courthouse on the highest ground in town, with a big arched entrance and a clock tower rising from the roof. Inside, terrazzo floors in the halls; the circuit court sits upstairs.',
  '',
  'Owned by Grand Traverse County and in use as the Historic Courthouse, 328 Washington Street, housing the 13th Circuit Court; the hours are from the county\'s page. Expect court security at the door.'+DT,
  [['SAH Archipedia: Grand Traverse County Courthouse',SAH+'GT1'],['American Courthouses: Grand Traverse County','https://courthouses.co/?p=10528'],['Grand Traverse County: Historic Courthouse','https://gtcountymi.gov/1235/Historic-Courthouse']],
  brick='yes',bcol='red',hours='Monday to Friday 7:30 a.m. to 5 p.m.; closed holidays'),

N('park-place-hotel-traverse-city','Park Place Hotel','Traverse City','mi','hotel','standing',44.76256,-85.61794,'exact','open','walk','','1929–1930',
  'A nine-storey hotel with a tower on the tenth floor, built in 1929–1930 by Hannah, Lay and Company to designs by Benjamin Marshall of Chicago, known for the Drake Hotel. It took the place of the three-storey Italianate Campbell House, built in 1873 by Henry D. Campbell and bought by Hannah and Lay, which was pulled down in 1929. A beacon on the tower once shone forty miles. It became the Park Place Motor Inn in 1963; the dome on top was added in 1976 for a summer theatre, and Rotary Charities bought and restored the hotel in 1989.',
  'Grey brick walls trimmed with Bedford limestone, Renaissance Revival detail and the domed top floor over State Street. The lobby was panelled in pine; how much of that survives was not checked. A working hotel.',
  '',
  'A working hotel at 300 East State Street; the lobby is open to guests and diners.'+DT,
  [['SAH Archipedia: Park Place Hotel',SAH+'GT3'],['The Ticker: Traverse City\'s hotel scene, then and now',TICK+'traverse-citys-hotel-scene-then-and-now']],
  brick='no',hours='?'),

N('hannah-lay-mercantile-building','Hannah & Lay Mercantile Building','Traverse City','mi','civic','standing',44.76430,-85.62343,'exact','view','walk','','1883',
  'Called the "Big Store" when Perry Hannah\'s firm built it in 1883, it was the largest store north of Grand Rapids. It was extensively renovated in 2010 and has since held a bank and offices; in 2019 a developer signed to buy it for condominiums.',
  'A large old commercial block at the corner of Front and Union streets. Inside not checked.',
  '',
  'A privately owned office building at 109 East Front Street; seen from the street.'+DT,
  [['The Ticker: agreement to purchase the Hannah Lay building',TICK+'agreement-in-place-to-purchase-redevelop-historic-hannah-lay-building/']],
  brick='?'),

N('traverse-city-state-bank-clocktower','Traverse City State Bank Building (the clocktower building)','Traverse City','mi','civic','standing',44.76434,-85.62421,'exact','view','walk','','1904',
  'Known in town as the clocktower building, it was built in 1904 by Perry Hannah for the Traverse City State Bank and designed by his son Julius, at the corner of Front and Union streets. It has always held a bank, most recently a Fifth Third branch, which has announced that it will close.',
  'A corner bank with a clock tower over Front Street. Inside not checked.',
  '',
  'A privately owned bank building at 102 West Front Street; seen from the street.'+DT,
  [['The Ticker: what next for the clocktower building',TICK+'whats-next-for-fifth-third-bank-iconic-downtown-clocktower-building/']],
  brick='?'),

N('traverse-city-fire-station-no-1','Old Fire Station No. 1','Traverse City','mi','civic','standing',44.76338,-85.62136,'exact','view','walk','','1890–1974',
  'The Traverse City Fire Department was organised in 1876 in the 200 block of East Front Street, with volunteers who included Julius Hannah, Perry Hannah\'s son. In 1890 it moved to this station on Cass Street, and the department answered some of the town\'s worst fires from here until 1974, when a new Station 01 opened on West Front Street. The old firehouse later held a restaurant, Bistro Foufou, which closed in 2019.',
  'The old firehouse on Cass Street. Inside not checked.',
  '',
  'A privately owned building at 118 Cass Street; seen from the street. Whether it has a tenant now was not checked.'+DT,
  [['City of Traverse City: fire department history','https://www.traversecitymi.gov/government/city-departments/fire-department/about.html'],['The Ticker: babies were born there, now Elks reside',TICK+'babies-were-born-there-now-elks-reside']],
  brick='?'),

N('central-united-methodist-traverse-city','Central United Methodist Church','Traverse City','mi','worship','standing',44.76215,-85.62150,'exact','open','walk','','1913',
  'Methodist preaching began here with D. R. Latham, who arrived in 1857, and in 1867 Hannah, Lay and Company gave land on Washington Street for the first church. The congregation was reincorporated as Central Methodist Church in 1911 because it was moving, and the present church on Cass Street was dedicated on June 22, 1913. A mosaic mural was dedicated in 1960.',
  'A working downtown church; the 1960 mosaic mural is the one inside feature the church\'s own history names. Interior otherwise not checked. Go in at a service.',
  '',
  'A working United Methodist church at 222 Cass Street; the service times are from the church\'s own page.'+DT,
  [['Central United Methodist Church: history','https://www.tccentralumc.org/history/'],['Central United Methodist Church: worship','https://www.tccentralumc.org/worship/']],
  brick='?',hours='Sunday 9 and 11 a.m.'),

N('oakwood-cemetery-traverse-city','Oakwood Cemetery','Traverse City','mi','burial','standing',44.75545,-85.58767,'site','public','drive','cemeteries','1861',
  'The city\'s garden-style cemetery, opened in 1861. It is really four cemeteries on one property: the Catholic, the City, the Jewish and the Northern Michigan Asylum cemetery, whose graves are mostly unmarked. The city lists among those buried here Perry Hannah, the town\'s founder, Henry Campbell, who built the first hotel on the Park Place site in 1873, and Joseph Maddy, founder of the Interlochen music camp.',
  'Old family plots of the town\'s founders; the asylum section has few markers.',
  '',
  'Owned by the City of Traverse City, off Eighth Street on the east side of town; open between sunrise and sunset. Drive in on the cemetery lanes and park along them.',
  [['City of Traverse City: Oakwood Cemetery','https://www.traversecitymi.gov/oakwoodcemetery.asp'],['City of Traverse City: Oakwood Cemetery, local influencers','https://www.traversecitymi.gov/government/city-departments/oakwood-cemetery/local-influencers.html']],
  brick='no',hours='Sunrise to sunset'),

]

PIN_NOTES={
 'grand-traverse-commons-building-50':'On the south wing of Building 50 as OpenStreetMap maps it (Building 50S), seen on the aerial; the Wikipedia point fell in the woods south of the road.',
 'perry-hannah-house-traverse-city':'Street-address point for 305 Sixth Street, checked on the aerial.',
 'city-opera-house-traverse-city':'Street-address point for 106 East Front Street, checked on the aerial.',
 'grand-traverse-county-courthouse':'Street-address point for 328 Washington Street, which is also where OpenStreetMap maps the courthouse.',
 'park-place-hotel-traverse-city':'Street-address point for 300 East State Street, checked on the aerial.',
 'hannah-lay-mercantile-building':'Street-address point for 109 East Front Street, checked on the aerial.',
 'traverse-city-state-bank-clocktower':'Street-address point for 102 West Front Street, checked on the aerial.',
 'traverse-city-fire-station-no-1':'Street-address point for 118 Cass Street, checked on the aerial.',
 'central-united-methodist-traverse-city':'Street-address point for 222 Cass Street, checked on the aerial.',
 'oakwood-cemetery-traverse-city':'The middle of the cemetery as OpenStreetMap maps it; the pin marks the grounds, not one grave.',
}
