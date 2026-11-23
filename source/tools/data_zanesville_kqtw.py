# November 23, 2026: Zanesville, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Zanesville buildings (the record is source/videos/20231111_q9GZEtrU8O4.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links) and the National Register list for Muskingum
# County; for hours and access the pages of whoever runs each place (the St. Thomas Aquinas parish, St. James Episcopal,
# St. John's Lutheran, Muskingum County History for the Stone Academy, the Muskingum County Library System), the county
# visitors' bureau pages, an Ohio Department of Natural Resources river map and a WHIZ news report on the river locks.
# The National Register forms for these places are not on line (placeholders at NPGallery). Pins are ArcGIS address
# points or Register points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'zanesville_kqtw','label':'Ohio: old Zanesville and the Y-Bridge','added':'2026-11-23 15:46'}

DT=' Street parking and several small lots downtown; their owners, hours and fees were not checked.'
REG=['National Register list, Muskingum County','https://en.wikipedia.org/wiki/National_Register_of_Historic_Places_listings_in_Muskingum_County,_Ohio']

PLACES=[

N('y-bridge-zanesville','Y-Bridge','Zanesville','oh','landmark','standing',39.94042,-82.01431,'exact','public','walk','','1984',
  'A three-way bridge shaped like a Y over the meeting of the Licking and Muskingum rivers, carrying U.S. Route 40 and Linden Avenue; you can cross it and stay on the same side of the river. The crossing was first bridged in 1814, and floods and wear brought four more: a trestle, two wooden bridges (the third, covered, stood from 1832 to 1900), a 1902 concrete bridge damaged in the 1913 flood, and the present concrete and steel bridge, opened in 1984. The site is on the National Register.',
  'The 1984 bridge has solid side rails that hide much of the view from the deck; the Y shape is best seen from the riverbanks. Nothing of the older bridges was checked.',
  '',
  'A public road bridge carrying U.S. Route 40, open at all times; whether it has sidewalks was not checked. Street parking on Main Street and Linden Avenue at either end was not checked.',
  [W('Y-Bridge (Zanesville, Ohio)'),REG],
  brick='no'),

N('muskingum-county-courthouse','Muskingum County Courthouse','Zanesville','oh','civic','standing',39.94056,-82.00722,'exact','view','walk','','1870s',
  'The county courthouse at Fourth and Main Streets, designed by T. B. Townsend and H. E. Myer in the Second Empire style, of stone, brick and slate. The ground was the site of Ohio\'s capitol from 1810 to 1812, when the legislature met in the earlier building here; that building then served the county until the present courthouse replaced it. Wikipedia gives the building date as both 1870 and 1874, and files it under 1877.',
  'A pale stone front with a clock tower and a mansard roof. The 1809 date stone from the old building is set over the front steps. The courthouse and jail are on the National Register. Interior and public hours not checked.',
  '',
  'Owned by Muskingum County and in use as its courthouse; seen from Main and Fourth Streets.'+DT,
  [W('Muskingum County Courthouse'),REG],
  conf='mixed',brick='no'),

N('st-thomas-aquinas-zanesville','St. Thomas Aquinas Church','Zanesville','oh','worship','standing',39.94250,-82.00616,'exact','open','walk','','1842',
  'The older of Zanesville\'s two Catholic parishes, on North Fifth Street. Its English Gothic church was begun in 1842, with stone given by a Quaker, John Howard, and help from the town\'s Protestants; the steeple followed in 1871. A tornado threw the steeple into the nave during Mass on June 16, 1912, killing three; the 1913 flood damaged the church again. Dominican friars served it until 2017; it is now a parish of the Diocese of Columbus and on the National Register.',
  'A pale stone Gothic church with a corner tower and clock. Pictorial stained glass ordered in 1914 from Joseph Osterrath of Liège, Belgium, put in after the First World War. Open for Mass at the times below.',
  '',
  'An active Catholic parish church at 130 North Fifth Street; the hours are from the parish\'s own page. The parish also lists confession on Saturdays from 3:30 to 4:15 p.m.'+DT,
  [W('St. Thomas Aquinas Church (Zanesville, Ohio)'),['St. Thomas Aquinas parish','https://saintthomaszanesville.org/'],REG],
  brick='no',hours='Mass Saturday 4:30 p.m.; Sunday 7:45 and 11 a.m.; Tuesday to Friday 9 a.m.'),

N('st-nicholas-zanesville','St. Nicholas Catholic Church','Zanesville','oh','worship','standing',39.94007,-82.00108,'exact','view','walk','','1897–1899',
  'The church of the German Catholic parish founded in 1836 at the east end of Main Street. The present church was begun in January 1897, its cornerstone laid in July 1898 and dedicated in August 1899, in the Italian Renaissance style; its dome has stood over the Zanesville skyline since. The inside was decorated slowly: frescoes and gold leaf in 1919, and a remodelling in 1960. On the National Register since 1975.',
  'A domed church at 925 East Main Street. Frescoes and gold leaf of 1919 inside, much changed in 1960 and again in 1986. Service times not checked.',
  '',
  'An active Catholic parish church at 925 East Main Street. The parish\'s own site refused to open when this was written, so service times were not checked.'+DT,
  [['Wikipedia: St. Nicholas Catholic Church (Zanesville, Ohio)','https://en.wikipedia.org/wiki/St._Nicholas_Catholic_Church_(Zanesville,_Ohio)'],REG],
  brick='?'),

N('st-james-episcopal-zanesville','St. James Episcopal Church','Zanesville','oh','worship','standing',39.94292,-82.00518,'exact','open','walk','','1843',
  'A Gothic Revival church of the Episcopal Diocese of Southern Ohio at 155 North Sixth Street, built in 1843 and on the National Register since 1978.',
  'A dark stone Gothic church with a tall square front tower. Interior not checked. Sunday services at the times below.',
  '',
  'An active Episcopal church; the service times are from the church\'s own page.'+DT,
  [W('St. James Episcopal Church (Zanesville, Ohio)'),['St. James Episcopal Church','https://stjameszanesville.org/'],REG],
  brick='no',hours='Sunday services 8 and 10 a.m.'),

N('st-johns-lutheran-zanesville','St. John\'s Lutheran Church','Zanesville','oh','worship','standing',39.94215,-82.00360,'exact','open','walk','','1926',
  'A Gothic Revival Lutheran church at Market and North Seventh Streets, built in 1926 and on the National Register since 1982.',
  'A red-brick Gothic church with white stone trim and a pinnacled front. Interior not checked. Sunday worship at the time below.',
  '',
  'An active Lutheran church at 116 North Seventh Street; the service time and office hours (Monday to Thursday, 9 a.m. to 2 p.m.) are from the church\'s own page.'+DT,
  [W('St. John\'s Lutheran Church (Zanesville, Ohio)'),['St. John\'s Lutheran Church','https://stjohnszanesville.org/'],REG],
  brick='yes',hours='Sunday worship 9 a.m.'),

N('zanesville-federal-building','Old Post Office and Federal Building','Zanesville','oh','civic','standing',39.939167,-82.006944,'site','view','walk','','1904',
  'The former United States post office and courthouse of Zanesville, built in 1904 in the Beaux-Arts style to the design of Cleveland architect George F. Hammond. It is on the National Register.',
  'A buff stone Beaux-Arts building with columns along its front. What it is used for now, and whether the public can go in, was not checked.',
  '',
  'Seen from the street. Owner and present use not checked.'+DT,
  [W('United States Post Office and Federal Building (Zanesville, Ohio)'),REG],
  brick='no'),

N('john-mcintire-library','John McIntire Library','Zanesville','oh','civic','standing',39.94411,-82.00603,'exact','open','walk','','1906–1908',
  'Zanesville\'s Carnegie library. The town\'s subscription library of 1828, the Athenaeum, became a free public library named for John McIntire, the town\'s founder, in 1905. The Chamber of Commerce won a Carnegie grant and the building contract was let in October 1906; it cost $62,000, Carnegie giving $52,500. The library says Carnegie let it carry McIntire\'s name and not his own, said to be the first time he allowed that. A new wing opened in 1991.',
  'A red-brick Carnegie building with pale stone trim and a pedimented entrance on Fifth Street. It has restored stained-glass skylights and hosts art exhibits. Free and open to all.',
  '',
  'The main library of the Muskingum County Library System, at 220 North Fifth Street. The library\'s own hours page is drawn by script and could not be read when this was written; call before going. The county visitors\' bureau page says there is free parking in the library lots off Shinnick Street and Sixth Street.',
  [['Muskingum County Library System: about the library','https://muskingumlibrary.org/about-us/'],['Visit Zanesville: John McIntire Library','https://www.visitzanesville.com/Explore/Destinations/292/John-McIntire-Library/']],
  brick='yes',hours='?'),

N('zanesville-ywca','Zanesville YWCA (Bryan Place)','Zanesville','oh','civic','standing',39.94127,-82.00529,'exact','view','walk','','1926',
  'Built in 1926 to a design by Howell and Thomas for the Young Women\'s Christian Association, which let rooms to single women and ran social and sports activities for young women. The YWCA closed in 1993 and the building is now called Bryan Place. On the National Register since 1978.',
  'A red-brick building with arched ground-floor windows and dormers. Interior not checked.',
  '',
  'At 49 North Sixth Street; seen from the street. Present owner not checked.'+DT,
  [W('Zanesville YWCA'),REG],
  brick='yes'),

N('black-elliott-block','Black-Elliott Block','Zanesville','oh','civic','standing',39.940278,-82.005833,'site','view','walk','','1876',
  'An Italianate commercial building on Main Street near the courthouse, built in 1876 by Henry Elliott and Peter Black, who each kept a store in it; the same pair were behind other downtown buildings including the Clarendon Hotel. S. S. Kresge\'s store was the main tenant from 1916 to 1977. Listed on the National Register in 1979, chiefly for its front: Wikipedia says no other late 1800s Italianate building of its kind survives downtown.',
  'A two-storey Italianate front with tall arched windows, painted in colours over its brick, above a sandstone base with iron details. Interior not checked.',
  '',
  'A private commercial building on Main Street; seen from the street.'+DT,
  [W('Black-Elliott Block'),REG],
  brick='no'),

N('stone-academy-zanesville','Stone Academy','Zanesville','oh','civic','standing',39.93160,-82.00619,'exact','open','walk','','1809',
  'Built in 1809 in Putnam, then a town of its own across the river, by Increase Mathews, Levi Whipple and Ebenezer Buckingham, in the hope that it would be Ohio\'s capitol; Zanesville won, and was the capital from 1810 to 1812. The Ohio Anti-Slavery Society met here in 1835 and 1839, and both times a mob from Zanesville attacked. It was a station on the Underground Railroad and became a house in 1840. It stands in the Putnam Historic District, on the National Register, near the 1835 Putnam Presbyterian Church, whose first pastor was a brother of Harriet Beecher Stowe.',
  'Now a museum: a trap door under the stairs to a crawl space where people escaping slavery were hidden, rooms on the Y-Bridge, the Sixth Street bridge, pottery and county history.',
  '',
  'Run as a museum by Muskingum County History at 115 Jefferson Street; the hours are from its own page, which says other times by appointment. The county visitors\' bureau page gives different days (Wednesday to Saturday) and an adult fee of $5; check before going. Street parking in Putnam not checked.',
  [W('Putnam Historic District'),['Muskingum County History','https://muskingumcountyhistory.org/'],['Visit Zanesville: Stone Academy','https://www.visitzanesville.com/Explore/Destinations/170/']],
  conf='mixed',brick='?',hours='May to September: Thursday to Saturday 1 to 4 p.m.; other times by appointment'),

N('muskingum-lock-10-zanesville','Muskingum River Lock No. 10 and Canal','Zanesville','oh','canal','standing',39.933889,-82.003194,'site','public','walk','canal','',
  'The Zanesville lock and dam of the Muskingum River navigation, the state-run chain of locks and dams from Zanesville to the Ohio River at Marietta, which a news report calls the only complete working system of hand-operated river locks in the country. Boats pass the dam by a short lock canal on the left bank (going downstream), with the lock and the lock tender\'s house on it. The lock and canal are on the National Register.',
  'A lock canal with its lock and lock tender\'s house and dock; the dam is in the river beside it. Whether the lock is working this season, and its hours, were not checked.',
  '',
  'Part of the Muskingum River Parkway, run by the Ohio Department of Natural Resources; its river map lists Zanesville Lock and Dam No. 10 at river mile 76.8, and the visitors\' bureau gives the address as 1000 Hughes Street. The locks are worked at no charge for pleasure boats, according to a WHIZ news report. The state park\'s own web page was empty when this was written. Keep off the dam and lock walls.',
  [['ODNR: Muskingum River Parkway map','https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/parks/parkmaps/muskingumparkmap.pdf'],['WHIZ: Historic Muskingum River lock opens to public','https://www.whiznews.com/?p=1327774'],['Visit Zanesville: Dam and Lock No. 10','https://www.visitzanesville.com/Explore/Destinations/339/'],REG],
  brick='?'),

]

PIN_NOTES={
 'y-bridge-zanesville':'Wikipedia\'s coordinate, on the middle of the Y on the aerial.',
 'muskingum-county-courthouse':'Wikipedia\'s coordinate, checked on the aerial.',
 'st-thomas-aquinas-zanesville':'Address point for 130 North Fifth Street, checked on the aerial.',
 'st-nicholas-zanesville':'Address point for 925 East Main Street, checked on the aerial.',
 'st-james-episcopal-zanesville':'Address point for 155 North Sixth Street, checked on the aerial.',
 'st-johns-lutheran-zanesville':'Address point for 116 North Seventh Street, checked on the aerial.',
 'zanesville-federal-building':'National Register list coordinate, checked on the aerial.',
 'john-mcintire-library':'Address point for 220 North Fifth Street, checked on the aerial.',
 'zanesville-ywca':'Address point for 49 North Sixth Street, checked on the aerial.',
 'black-elliott-block':'National Register list coordinate, checked on the aerial.',
 'stone-academy-zanesville':'Address point for 115 Jefferson Street; on the aerial it falls on a small building under trees.',
 'muskingum-lock-10-zanesville':'National Register list coordinate; on the aerial it falls on the lock canal beside the river, with the lock walls just south.',
}
