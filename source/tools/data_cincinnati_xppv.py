# November 22, 2026: Cincinnati, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Cincinnati buildings (the record is source/videos/20220827_nfyI7eW_vUE.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links); the Cincinnati Parks page for Eden Park and
# its park-hours rule; the Friends of Music Hall tours page; the Wise Temple's page for Plum Street Temple; the
# Cathedral Basilica's own calendar; the 21c Museum Hotel's page; the HMdb text of the Ohio Historical Society's
# "Cincinnati Breweries" marker; Soapbox Media (2008) and Ronny Salerno's Queen City Discovery (2010) on the Clyffside
# Brewery. Pins are ArcGIS address points or the Wikipedia point, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'cincinnati_xppv','label':'Ohio: old Cincinnati, from Music Hall to Eden Park','added':'2026-11-22 08:32'}

DT=' Downtown street meters and public garages are close by; their hours and fees were not checked.'
EDEN='Eden Park is a city park run by Cincinnati Parks; its rules close city parks from 10 p.m. to 6 a.m. '
EDENL=['Cincinnati Parks: Eden Park','https://cincinnati-oh.gov/cincyparks/visit-a-park/find-a-parkfacility/eden-park/']
HRS=['Cincinnati Parks: park hours rule','https://www.cincinnati-oh.gov/cincyparks/news/new-park-hours-for-minors-under-18/']

PLACES=[
N('cincinnati-music-hall','Cincinnati Music Hall','Cincinnati','oh','civic','standing',39.10934,-84.51871,'exact','open','walk','','1878',
  'A concert hall finished in 1878, built with a big central auditorium for music and side wings for industrial exhibitions. It stands across from Washington Park in Over-the-Rhine, on ground that had been a paupers\' cemetery. It became a National Historic Landmark in 1975 for its Venetian Gothic design, was put on the National Trust\'s list of the eleven most endangered historic places in 2014, and reopened in 2017 after a renovation of more than a year costing $143 million. It is home to the city\'s symphony, pops, opera, ballet and May Festival chorus.',
  'A long Venetian Gothic front with a steep gable roof, corbelled brick, traceried windows and a large rose window. Inside, the main hall is Springer Auditorium, named for the founding patron Reuben Springer, with a large Czech chandelier hung in the early 1970s; the ballroom has the Wurlitzer theatre organ from the old Albee Theater. Friends of Music Hall runs guided tours inside (75 to 90 minutes, starting at the south end of the building, 1241 Elm Street) and outdoor building tours.',
  'Built over a paupers\' graveyard, and said to be one of the most haunted halls in America.',
  'Owned by the city and used for concerts. Tours by Friends of Music Hall: tickets in advance online or by telephone, up to three hours before the start; adults pay more than the $5 children\'s price (group rates on its page); not recommended under age 8. Washington Park across Elm Street is open to all.'+DT,
  [W('Cincinnati Music Hall'),['Friends of Music Hall: tours','https://friendsofmusichall.org/music-hall-tours/']],
  brick='yes',hours='Guided inside and outdoor tours on dates listed by Friends of Music Hall, tickets in advance; concerts and shows on their own dates'),

N('plum-street-temple-cincinnati','Plum Street Temple (Isaac M. Wise Temple)','Cincinnati','oh','worship','standing',39.10372,-84.51831,'exact','open','walk','','1863–1866',
  'A synagogue built chiefly during the Civil War for the congregation K.K. B\'nai Yeshurun and dedicated on August 24, 1866, in honour of Rabbi Isaac Mayer Wise, one of the founders of Reform Judaism in America. James Keys Wilson designed it, taking the Alhambra at Granada as his model; it cost $275,000. It is among the oldest synagogue buildings in the United States, was listed on the National Register in 1972 and made a National Historic Landmark in 1975. The congregation built a new home in Amberley Village in 1976 and still uses this one for some Shabbat services and other events.',
  'A Byzantine and Moorish front with two slim minaret towers, a rose window and a white alabaster window. It stands across Plum Street from the Cathedral of St. Peter in Chains, next to the site of St. Paul Episcopal Cathedral, which was pulled down in 1937. The congregation calls it one of only two temples of this style in the country. Interior shown by tour only.',
  'A Civil War synagogue modelled on the Alhambra, across the street from a Catholic cathedral and City Hall.',
  'Owned by the Wise Temple congregation, 720 Plum Street, at Eighth Street. Its page gives tours on Thursday mornings, by appointment only, through the congregation\'s office; a lift is at the Eighth Street entrance.'+DT,
  [W('Isaac M. Wise Temple'),['Wise Temple: Plum Street Temple','https://www.wisetemple.org/?p=190']],
  brick='yes',hours='Tours Thursday mornings by appointment only; some Shabbat services'),

N('st-peter-in-chains-cathedral-cincinnati','Cathedral Basilica of St. Peter in Chains','Cincinnati','oh','worship','standing',39.10351,-84.51936,'exact','open','walk','','1841–1845',
  'The cathedral of the Catholic Archdiocese of Cincinnati. Bishop John Baptist Purcell laid the cornerstone in May 1841 and consecrated the building on November 2, 1845; it was the first large church west of the Alleghenies. The front portico was finished in 1855. It was remodelled in the 1930s with new transepts and altars and twelve new bells in 1937, re-dedicated as the cathedral on November 3, 1957, and named a minor basilica in 2020.',
  'A Greek Revival church at Eighth and Plum streets with a white limestone spire 224 feet high, for many years the tallest thing in Cincinnati, and portico columns 33 feet high. Inside, a Venetian glass mosaic 35 feet high and 40 feet wide fills the apse, showing Christ enthroned. Mass is open to anyone.',
  '',
  'An active cathedral of the Archdiocese of Cincinnati, 325 West Eighth Street. The service times here are from the cathedral\'s own calendar as read in November 2026 and change with the season.'+DT,
  [W('Cathedral Basilica of St. Peter in Chains'),['Cathedral Basilica: calendar and Mass times','https://cathedralaoc.org']],
  brick='no',hours='Sunday Mass 10 a.m. and 4 p.m., vigil Mass 3 p.m. the evening before; weekday Mass 7 a.m.'),

N('cincinnati-city-hall','Cincinnati City Hall','Cincinnati','oh','civic','standing',39.10426,-84.51907,'exact','view','walk','','1888–1893',
  'Samuel Hannaford designed the city hall, finished in 1893 for $1.61 million on the site of the first city hall of 1852, which was pulled down in 1888 to make room. The builder was the David Hummel company of Cincinnati. With H. H. Richardson\'s Chamber of Commerce building demolished in 1911, it is the best Richardsonian Romanesque building left in the city. It was listed on the National Register in 1972.',
  'Four and a half storeys with a nine-storey clock tower, in stone quarried in Wisconsin, Ohio, Missouri and Indiana. Wikipedia says the stairs and wainscoting are Italian and Tennessee marble, the columns Vermont granite, and stained glass windows show Cincinnatus and early Cincinnati. Interior not checked.',
  '',
  'The working seat of city government, 801 Plum Street, between Eighth and Ninth streets. Look from the sidewalks; when the public may go in was not checked.'+DT,
  [W('Cincinnati City Hall')],
  brick='no',hours=''),

N('hamilton-county-courthouse-cincinnati','Hamilton County Courthouse','Cincinnati','oh','civic','standing',39.10702,-84.51022,'exact','view','walk','','1915–1919',
  'The sixth courthouse of Hamilton County and the fourth built downtown. William Howard Taft laid the cornerstone on October 1, 1915, and Warren G. Harding dedicated it on October 18, 1919; it cost $3,022,000. Three earlier courthouses burned: in 1813, in 1849 from a fire in a pork plant next door, and in the riots of 1884.',
  'A Renaissance Revival courthouse at 1000 Main Street, joined to the county jail by a skybridge. It holds the Common Pleas, Municipal and Small Claims courts. Interior not checked.',
  'Three courthouses lost to fire in seventy years: this one was built to last.',
  'A working county courthouse. Look from Main Street and Court Street; going in means the usual court security, and its hours were not checked.'+DT,
  [W('Hamilton County Courthouse (Ohio)')],
  brick='no',hours=''),

N('hotel-metropole-cincinnati','Hotel Metropole (21c Museum Hotel)','Cincinnati','oh','hotel','standing',39.10317,-84.51249,'exact','open','walk','','1912–1913',
  'A Neoclassical hotel opened in 1913, the idea of the lawyer Joseph C. Thoms, who thought the city lacked luxury hotels; Joseph Steinkamp and Brother drew it up. Strikes by steamfitters and carpenters held up the work in 1912. It became the Mid-Towne Apartments, for low incomes, in 1973, and a hotel again in 2012 as the 21c Museum Hotel.',
  'A tall Neoclassical front on Walnut Street. The hotel runs as a contemporary art museum as well: its page describes lobby galleries, a fibre-optic tapestry in the nine-storey inner light court, and a restaurant named Metropole. Original fabric inside was not checked.',
  '',
  'A working hotel at 609 Walnut Street. Its page describes the art galleries and the restaurant but gives no gallery hours.'+DT,
  [W('Hotel Metropole (Cincinnati, Ohio)'),['21c Museum Hotel Cincinnati','https://www.21cmuseumhotels.com/cincinnati/']],
  brick='yes',hours='?'),

N('doctors-building-cincinnati','Doctors\' Building','Cincinnati','oh','civic','standing',39.10415,-84.51453,'exact','view','walk','','1923',
  'An eight-storey office block finished in 1923 to designs by Tietig and Lee, one of the city\'s leading firms. It was the only large building in Cincinnati put up only for doctors\' offices, and one of the city\'s few Late Gothic Revival commercial buildings. It changed hands several times from 1986 on; in 2024 a new owner announced a conversion into 52 apartments with offices and shops on the lower floors, planned to finish by March 2026. Whether that was done was not checked.',
  'A Gothic front faced in terracotta tiles over brick and reinforced concrete, with a flat roof and small penthouse. It stands on the south side of Garfield Place, so it can be seen from across the park. Interior not checked.',
  '',
  'Private building at 19 Garfield Place. Look from Garfield Place and the park in front.'+DT,
  [W("Doctors' Building (Cincinnati, Ohio)")],
  brick='no',hours=''),

N('eden-park-stand-pipe-cincinnati','Eden Park Stand Pipe (water tower)','Cincinnati','oh','water','standing',39.11722,-84.49028,'exact','public','walk','','1894',
  'A water tower 172 feet high that Samuel Hannaford designed in 1894 to give the Walnut Hills district enough water pressure. Eden Park Station No. 7 pumped Ohio River water up into it. It went out of use in 1916, when newer towers were built, and its copper spire was taken down for a war scrap drive in 1943. The city uses it now as a communications tower. It was listed on the National Register in 1980.',
  'A tall round tower of red brick banded with lighter stone, standing by itself near the top of Eden Park. Visitors can no longer climb to the observation level it once had. Nearby, a road from the Twin Lakes crosses the old Melan Arch Bridge towards the park overlook.',
  'A castle turret with no castle: a water tower that lost its spire to the Second World War scrap drive.',
  EDEN+'The tower itself is closed. Mapped park parking on Cliff Drive and Lake Drive, both in Eden Park, about 200 to 300 m away.',
  [W('Eden Park Stand Pipe'),W('Eden Park (Cincinnati)'),EDENL,HRS],
  th=[39.11547,-84.48966],thn='Eden Park parking, Cliff Drive',brick='yes',hours='Park open 6 a.m. to 10 p.m.'),

N('eden-park-station-no-7-cincinnati','Eden Park Station No. 7 (pumping station)','Cincinnati','oh','water','standing',39.11306,-84.49111,'site','public','walk','','1889–1894',
  'A pumping station that raised Ohio River water to the Eden Park Stand Pipe, built from 1889 to 1894 to plans by Samuel Hannaford, with the David Hummel company as builder. It worked as designed only for a few years: a new station in the East End replaced it in 1907, after Deer Creek, by then a sewer, had fouled the river nearby. In 1939 its tower was turned into a police radio station.',
  'Brick walls and a brick chimney on a stone foundation, with sandstone arches under a Neoclassical pediment. Interior not checked.',
  '',
  EDEN+'Seen from the park roads; the building is not open. Mapped park parking on Cliff Drive.',
  [W('Eden Park Station No. 7'),EDENL,HRS],
  th=[39.11547,-84.48966],thn='Eden Park parking, Cliff Drive',brick='?',hours='Park open 6 a.m. to 10 p.m.'),

N('elsinore-arch-cincinnati','Elsinore Arch','Cincinnati','oh','water','standing',39.11306,-84.49968,'exact','public','walk','','1883',
  'A valve house built in 1883 for the Cincinnati Water Works at Gilbert Avenue and Elsinore Place, to control the main that ran down from the Eden Park reservoir. The Water Works wanted it to double as a gateway to the park, and its castle look is said to come from the Elsinore Castle stage set of a Hamlet performed at Music Hall that spring. It was listed on the National Register in 1980.',
  'A small grey stone castle with two towers and an arch over the path, at the foot of the hill on Gilbert Avenue: one of the park\'s entrances.',
  'A water valve dressed up as Hamlet\'s castle.',
  EDEN+'The arch stands on the public way at Gilbert Avenue and Elsinore Place; a mapped Eden Park lot on Mount Adams Drive is about 300 m away.',
  [W('Elsinore Arch'),W('Eden Park (Cincinnati)'),HRS],
  th=[39.11165,-84.49679],thn='Eden Park parking, Mount Adams Drive',brick='no',hours=''),

N('spring-house-gazebo-cincinnati','Spring House Gazebo and Mirror Lake','Cincinnati','oh','landmark','standing',39.11425,-84.49351,'exact','public','walk','','1904',
  'A Moorish-style gazebo by the architect Cornelius M. Foster, the oldest park structure left in Cincinnati\'s city parks and the one drawn in the Park Board\'s logo. It replaced an old spring house; people carried the spring water away by the bucket until it was found to be fouled, and the well was sealed in 1912. Beside it, Mirror Lake fills part of the old Eden Park reservoir, built from 1866 to 1878 to hold 96 million gallons and taken out in the early 1960s; the reservoir\'s dam still stands.',
  'Brightly painted arches and ball finials on the gazebo, overlooking Mirror Lake, a reflecting pool with a walk round it and a seasonal fountain that throws water 60 feet up.',
  '',
  EDEN+'Mapped Eden Park parking on Mount Adams Drive, about 400 m away.',
  [W('Spring House Gazebo'),W('Eden Park (Cincinnati)'),EDENL,HRS],
  th=[39.11165,-84.49679],thn='Eden Park parking, Mount Adams Drive',brick='?',hours='Park open 6 a.m. to 10 p.m.'),

N('over-the-rhine-cincinnati','Over-the-Rhine Historic District','Cincinnati','oh','town','standing',39.11444,-84.515,'area','public','walk','','1800s',
  'A neighbourhood north of downtown, settled in the 1800s by German immigrants who crossed the Miami and Erie Canal, nicknamed "the Rhine", to get to work; hence the name. It is one of the largest and most intact urban historic districts in the country, on the National Register since 1983. The canal was drained and covered by Central Parkway in the 1920s, its bed meant for the Cincinnati subway, which was never finished. The Brewery District at its north end holds most of the city\'s surviving brewery buildings.',
  'Street after street of 1800s row buildings, Music Hall and Findlay Market. An Ohio Historical Society marker at West McMicken Avenue and Dunlap Street, by Hanna Park, maps the brewery buildings left, from Christian Moerlein and Kauffman to the Clyffside and Bellevue works, and says the lager was kept in deep cellars and tunnels cut into the hillside.',
  'Over the "Rhine": a German town that grew on the far bank of a canal that is now a parkway, with an unfinished subway in its bed.',
  'Seen from the city\'s public streets and sidewalks; the buildings themselves are mostly private. The pin is the middle of the district, not one building.'+DT,
  [W('Over-the-Rhine'),['HMdb: Cincinnati Breweries marker','https://www.hmdb.org/m.asp?m=24835']],
  brick='?',hours=''),

N('clyffside-brewery-cincinnati','Clyffside Brewery','Cincinnati','oh','industry','standing',39.11991,-84.52282,'exact','view','walk','','1846–1957',
  'A brewery on West McMicken Avenue that began as the Hamilton Brewery in 1846, took the name Clyffside in 1933 and was the headquarters of the Red Top Brewing Company from 1945 until brewing stopped in 1957. The Ohio Historical Society marker in the Brewery District lists it among the surviving brewery buildings as Sohn, Mohawk, Clyffside and Red Top. In 2008 a $3 million conversion into 19 townhomes and lofts was announced; whether it was finished was not checked.',
  'A large red-brick brewery on the hillside, with a tall chimney; photographs from 2019 show the word Felsenbräu painted high on one wall and scaffolding along the street front. A 2010 write-up describes belt-driven machinery left on the wooden floors and lagering cellars below; whether any of that is still there after the planned conversion was not checked.',
  '',
  'Private property at 244 West McMicken Avenue. Look from the street only; do not go in. Mapped parking lots are close by on Central Parkway and Branch Alley; their owners and fees were not checked.',
  [['HMdb: Cincinnati Breweries marker','https://www.hmdb.org/m.asp?m=24835'],['Soapbox Media: Clyffside condo renovation (2008)','https://soapboxmedia.com/?p=15924'],['Queen City Discovery: the Clyffside and Kauffman breweries (2010)','https://ronnysalerno.com/queencitydiscovery/2010/02/clyffside-and-kauffman-breweries.html']],
  conf='mixed',brick='yes',hours=''),
]

PIN_NOTES={
 'cincinnati-music-hall':'Address point for 1241 Elm Street; on the east side of the hall on the aerial.',
 'plum-street-temple-cincinnati':'Address point for 720 Plum Street; on the temple\'s roof on the aerial.',
 'st-peter-in-chains-cathedral-cincinnati':'Address point for 325 West Eighth Street; on the cathedral\'s green roof on the aerial.',
 'cincinnati-city-hall':'Address point for 801 Plum Street; on the city hall roof by its tower on the aerial.',
 'hamilton-county-courthouse-cincinnati':'Address point for 1000 Main Street; on the courthouse on the aerial.',
 'hotel-metropole-cincinnati':'Address point for 609 Walnut Street; on the hotel on the aerial.',
 'doctors-building-cincinnati':'Address point for 19 Garfield Place; on the building on the aerial.',
 'eden-park-stand-pipe-cincinnati':'Wikipedia point for the stand pipe; on the round tower, whose long shadow shows on the aerial.',
 'eden-park-station-no-7-cincinnati':'Wikipedia and National Register point for the station; on its red roof on the aerial.',
 'elsinore-arch-cincinnati':'Wikipedia point for the arch; on the small structure at the road corner on the aerial.',
 'spring-house-gazebo-cincinnati':'Wikipedia point for the gazebo, at the north end of Mirror Lake; the gazebo is small and the pin is within a few metres of it on the aerial.',
 'over-the-rhine-cincinnati':'National Register list point for the district: the middle of the neighbourhood.',
 'clyffside-brewery-cincinnati':'Address point for 244 West McMicken Avenue; on a large building on the hillside street on the aerial.',
}
