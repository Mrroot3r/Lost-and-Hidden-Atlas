# November 26, 2026: Akron, Ohio. A "videos" session (PROMPTS.md job 9): the names came from one video's tour of
# old Akron buildings (the record is source/videos/20260227_VXfG4pjqO-A.md); the video is a tip and nothing here
# rests on it. Sources read: Wikipedia (each article named in the links), the National Register list for Akron and
# the Park Service's record for each listing, the National Register form for the Firestone buildings, the Hower House
# Museum's pages, the Akron Art Museum's visit page, the Diocese of Cleveland's page for St. Bernard, the First
# Congregational Church's history page, Signal Akron (October 2025) on old St. Paul's, the University of Akron's
# Rubber City Revisited and Akron Life on Glendale Cemetery, Clio on the 1929 post office, and the Cascade Locks Park
# Association's pages. Most older Register forms for Akron are scans without a text layer and were not read.
from data_b import N
from data_ma import W
BATCH={'key':'akron_wbrf','label':'Ohio: old Akron, the rubber city','added':'2026-11-26 21:33'}

DT=' OpenStreetMap maps several parking lots within a few hundred metres downtown; their owners, hours and fees were not checked.'
NR='https://npgallery.nps.gov/AssetDetail/NRIS/'

PLACES=[

N('summit-county-courthouse-akron','Summit County Courthouse','Akron','oh','civic','standing',41.07956,-81.51711,'exact','view','walk','','1905–1908',
  'The county courthouse at 209 South High Street, built from 1905 to 1908 in the Second Renaissance Revival style to the design of the Cleveland architect J. Milton Dyer. The Cleveland sculptor Herman Matzen made the seated figures of Justice and Law. The courthouse and its annex were put on the National Register in 1974.',
  'Two lions guard the South High Street side, and Matzen\'s seated figures of Justice and Law are on the building. Interior and public hours not checked.',
  '',
  'Owned by Summit County; seen from South High Street and the streets around it.'+DT,
  [W('Summit County Courthouse (Ohio)'),['National Register record',NR+'74001625']],
  brick='?'),

N('glendale-cemetery-akron','Glendale Cemetery and Civil War Memorial Chapel','Akron','oh','burial','standing',41.08498,-81.5252,'site','public','walk','','1839; chapel 1875',
  'Akron\'s oldest cemetery, founded in 1839 as the Akron Rural Cemetery by Dr. Jebediah Commins (Wikipedia gives J. D. Commons), who modelled it on Mount Auburn Cemetery near Boston. It is a rural or garden cemetery of about 150 acres, with curving drives, hills and mausoleums modelled on Egyptian, Greek and Roman temples and Gothic churches; in the late 1800s a railway tourist guide told visitors not to leave the city without seeing it. The cemetery is on the National Register (2001), and its four buildings by the Glendale Avenue entrance were listed in 1980: the caretaker\'s house of 1869, the Civil War Memorial Chapel of 1875, the bell tower of 1883 and the office of 1902.',
  'The stone Civil War Memorial Chapel has the names of the local people who died in the Civil War on its windows and carved into its walls. A row of mausoleums carries the names of Akron industrial families (Mustill, Sisler, Werner, Conger and others), and some still have the little foot bridges that once crossed a stream in front of them. The bell tower was not ringing in recent years; a fundraiser was held to restore it. Whether the chapel can be seen inside other than at events was not checked.',
  '',
  'Privately run by the cemetery\'s board (Akron Life), at 150 Glendale Avenue, a short walk west of downtown. The cemetery\'s own website could not be opened when this was written, so its gate hours were not checked; visit in daylight and keep to the drives. OpenStreetMap maps a lot on Locust Street about 110 m southeast of the entrance; its owner was not checked.',
  [W('Glendale Cemetery'),['Rubber City Revisited (University of Akron): Glendale Cemetery','https://blogs.uakron.edu/rubbercityrevisited/?p=958'],['Akron Life: Reimagining Glendale','https://www.akronlife.com/travel/reimagining-glendale_1/'],['National Register record (cemetery buildings)',NR+'80003236']],
  brick='?',hours='?'),

N('first-congregational-church-akron','First Congregational Church','Akron','oh','worship','standing',41.08139,-81.50861,'exact','view','walk','','1908–1910',
  'The church of Akron\'s first formally organized congregation, founded in 1833. Its first two buildings, on High Street and on North Main Street, were outgrown or lost (the Main Street church was levelled by fire in 1868). The cornerstone of this Bedford limestone church at East Market and Union streets was laid on June 7, 1908, and the first service was held in the unfinished building on March 20, 1910. It is in the United Church of Christ and was put on the National Register in 2004.',
  'A Romanesque Revival limestone church with a square bell and clock tower 100 feet tall. Inside, a Casavant Frères pipe organ of 1951 with more than 3,500 pipes, restored in 2006 behind a stencilled pipe front copied from the church\'s first organ of 1911. Service times were not found on the church\'s own pages.',
  '',
  'An active church at 292 East Market Street; seen from the street. The church office keeps weekday hours.'+DT,
  [W('First Congregational Church (Akron, Ohio)'),['First Congregational Church: About and history','https://akronfcc.org/about/']],
  brick='no',bcol='none'),

N('old-akron-post-office-art-museum','Old Akron Post Office (Akron Art Museum)','Akron','oh','civic','standing',41.08463,-81.51541,'exact','open','walk','','1899',
  'Akron\'s post office of 1899, an Italian Renaissance Revival building designed under the Treasury\'s supervising architect James Knox Taylor, at Main and Market streets. The Register record gives 1895 as its significant year. It is now the oldest part of the Akron Art Museum, which opened a large new wing beside it in 2007.',
  'A low-roofed brick building with big limestone-trimmed arches. Its first floor holds the museum\'s Western art of 1850 to 1950.',
  '',
  'The Akron Art Museum, 1 South High Street. Admission charged (adults $15 when this was written; children 17 and under free, and the galleries are free on Thursdays); hours from the museum\'s visit page.'+DT,
  [W('Akron Art Museum'),W('Main–Market Historic District'),['Akron Art Museum: Visit','https://akronartmuseum.org/visit/'],['National Register record',NR+'72001046']],
  brick='?',hours='Wednesday, Friday to Sunday 12 to 5 p.m.; Thursday 12 to 9 p.m.; closed Monday and Tuesday and major holidays'),

N('akron-post-office-federal-building','Akron Post Office and Federal Building (1929)','Akron','oh','civic','standing',41.08354,-81.51244,'site','view','walk','','1927–1929',
  'The second federal post office, begun in 1927 and finished in 1929 in the Beaux-Arts style to the designs of the Treasury\'s architects under James A. Wetmore. It was a post office until 1975 and then a display studio, and since the 2000s it has held medical offices.',
  'A granite terrace and Tuscan columns on pedestals. The inside was rebuilt as offices in 2007.',
  '',
  'Privately owned medical offices at 168 East Market Street; seen from the street.'+DT,
  [W('Akron Post Office and Federal Building'),['Clio: Akron Post Office and Federal Building','https://theclio.com/entry/28661'],['National Register record',NR+'83002059']],
  brick='?'),

N('st-bernard-church-akron','St. Bernard\'s Church','Akron','oh','worship','standing',41.07806,-81.51861,'exact','open','walk','','1902–1905',
  'A Catholic parish church at 44 University Avenue. The parish\'s first church of 1861 stood on another site; this one was begun in 1902 to the design of the Akron-born church architect William P. Ginther and opened in 1905. It was put on the National Register in 1989.',
  'Rock-faced stone walls of one colour, round-arched windows and symmetrical towers in the Richardsonian Romanesque manner. The inside was decorated by the Rambusch Decorating Company.',
  '',
  'An active parish of the Diocese of Cleveland; Mass times from the diocese\'s page for St. Bernard.'+DT,
  [W('St. Bernard\'s Church (Akron, Ohio)'),['Diocese of Cleveland: St. Bernard','https://www.dioceseofcleveland.org/parishes/directory/st-bernard']],
  brick='no',bcol='none',hours='Mass Saturday 4:30 p.m.; Sunday 10 a.m., 12 noon (Spanish) and 8 p.m.'),

N('old-st-pauls-church-akron','Old St. Paul\'s Episcopal Church (burned)','Akron','oh','worship','ruins',41.08083,-81.50694,'exact','view','walk','burned','1884–1885; fire 2018',
  'A Gothic Revival stone church and Sunday school built in 1884–85 for St. Paul\'s Episcopal Church, to the Akron Plan of classrooms round a central hall; Signal Akron names Jacob Snyder as its architect. The meetings its rector Walter F. Tunks hosted in the 1930s for the Oxford Group were a forerunner of Alcoholics Anonymous. After the congregation moved, it was the University of Akron\'s Firestone Conservatory of Music until 1976, and it stood empty from 2006. A fire on April 18, 2018 burned out the roof and inside; the 1909 addition took only smoke damage. A developer bought it in 2021 meaning to save it, but in September 2025 the city\'s vacant-buildings board ordered it pulled down, and the owner appealed in the county court (October 2025). Whether it still stands was not checked after that.',
  'The burned stone shell, propped by steel girders put in in 2019, behind a fence at the corner of East Market and South Forge streets.',
  '',
  'Privately owned and fenced; look from East Market and Forge streets only.'+DT,
  [W('St. Paul\'s Sunday School and Parish House'),['Signal Akron: Can this historic church in Akron be saved? (October 2025)','https://signalakron.org/can-this-akron-landmark-be-saved-owner-aims-to-preserve-historic-1884-church-from-demolition'],['National Register record',NR+'76001532']],
  conf='mixed',brick='no',bcol='none'),

N('stan-hywet-hall-akron','Stan Hywet Hall and Gardens','Akron','oh','landmark','standing',41.11861,-81.55139,'exact','open','drive','','1912–1915',
  'The country estate of F. A. Seiberling, co-founder of the Goodyear Tire and Rubber Company, and his wife Gertrude, built from 1912 to 1915 to the design of the Cleveland architect Charles Sumner Schneider after the family toured about twenty English manor houses. Warren Manning laid out the grounds. The name, loosely Old English for "stone hewn", recalls the old stone quarries on the land. The Seiberling children gave the estate to a foundation in 1957, and it is a National Historic Landmark.',
  'A Tudor Revival manor house, one of the largest houses in the United States, with a music room, an indoor swimming pool and a dining room for 40, furnished with Tudor antiques and 1915 pieces made to look old; restored room by room from 2015 to 2021. Around it about 70 acres of garden rooms (an English garden, a Japanese garden, a restored garden by Ellen Shipman), a greenhouse and a carriage house.',
  '',
  'A house museum run by the Stan Hywet Hall Foundation, on North Portage Path. Admission charged. Wikipedia gives the season as Tuesday to Sunday, April 1 to December 30; the estate\'s own website could not be read when this was written, so hours were not checked. OpenStreetMap maps a guest lot about 220 m east of the house on North Portage Path.',
  [W('Stan Hywet Hall and Gardens'),['National Register record',NR+'75002058']],
  th=[41.1193,-81.54891],thn='Guest parking, North Portage Path',brick='?',hours='?'),

N('hower-house-akron','Hower House','Akron','oh','landmark','standing',41.079556,-81.507778,'exact','open','walk','','1871',
  'A 28-room mansion finished in 1871 for John Henry Hower, an Akron industrialist in milling, reapers and cereal. He designed it with the Akron architect Jacob Snyder in the Second Empire Italianate style, on a floor plan taken from the Akron Plan that Snyder used for Sunday schools. The Hower family lived in it for over a hundred years before giving it to the University of Akron in 1970; it has been a house museum since the mid-1980s.',
  'A mansard roof and a tall tower; three floors with a ballroom and servants\' rooms on the third, and the furnishings the family collected from round the world. The inside is shown on tours.',
  '',
  'Run by the University of Akron at 60 Fir Hill, on the campus. Admission charged (adults $10 when this was written). Parking on site behind the Carriage House, entered from South Forge Street. The hours given are the holiday season\'s, from the museum\'s visit page; the museum closes in January.',
  [['Hower House Museum: Visit','https://www.uakron.edu/howerhousemuseum/visit-us'],['Hower House Museum: Our history','https://www.uakron.edu/howerhousemuseum/about-us/'],['National Register record',NR+'73001536']],
  brick='yes',bcol='red',hours='Holiday season: Thursday to Saturday 12 to 3 p.m., Sunday 1 to 4 p.m. (last entry an hour before closing); closed in January'),

N('akron-ymca-building','Akron YMCA Building','Akron','oh','civic','standing',41.08092,-81.52399,'exact','view','walk','','1930–1931',
  'The Akron YMCA\'s second building, an Art Deco tower begun in 1930 and finished in 1931 to the design of John R. Luxmore of the local firm Good & Wagner; the YMCA\'s first building of 1904 was elsewhere downtown. Remodelled in the late 1980s and early 1990s, it now holds 55 apartments and offices, and the YMCA leases its sports rooms on the lower floors. National Register, 1980.',
  'An Art Deco tower. The inside is private: YMCA rooms for members, apartments and offices.',
  '',
  'Privately owned; seen from the street.'+DT,
  [W('Akron YMCA Building'),['National Register record',NR+'80003237']],
  brick='?'),

N('ywca-building-akron','YWCA Building (CitiCenter Building)','Akron','oh','civic','standing',41.0811,-81.5175,'exact','view','walk','','1931',
  'An eleven-story building put up in 1931 for the Young Women\'s Christian Association. A developer bought it in 1985 and it held the CitiCenter Athletic Club, closed in 2018, and city offices. Plans for apartments and offices won a state tax credit in 2020, and it was sold again in 2025. National Register, 1982.',
  'An eleven-story tower downtown. Interior not checked; empty or being redeveloped in recent years.',
  '',
  'Privately owned; seen from the street.'+DT,
  [W('CitiCenter Building'),['National Register record',NR+'82001491']],
  brick='?'),

N('firestone-plant-1-akron','Firestone Plant No. 1, Triangle Building and Club House','Akron','oh','industry','standing',41.05174,-81.53039,'site','view','drive','','1910–1926',
  'The first buildings put up for the Firestone Tire and Rubber Company, founded in Akron by Harvey S. Firestone in 1900, and the last in Akron tied to him: Plant No. 1, a four-story factory and office building of 1910 by Harpster and Bliss; the Club House of 1915 by Trowbridge and Ackerman; and the Triangle Building, a warehouse and shipping building of 1926. They were listed on the National Register in 2014; the form then found Plant No. 1 largely empty, with Bridgestone/Firestone still making specialty racing tires in about a sixth of it.',
  'Plant No. 1 is buff brick over a reinforced concrete frame, its wings shaped like two letter H\'s side by side; the Triangle Building takes its shape from the railroad behind it. Present use not checked.',
  '',
  'Company property at 1200 Firestone Parkway, off South Main Street; seen from the public streets.'+DT,
  [['National Register record and form',NR+'14000338'],W('Firestone (company)')],
  brick='no',bcol='buff'),

N('cascade-locks-akron','Cascade Locks and Mustill Store','Akron','oh','canal','ruins',41.09197,-81.51822,'site','public','walk','canal','1827–1913',
  'The steepest stretch of the Ohio and Erie Canal between Lake Erie and the Ohio River: a staircase of locks, 10 to 16, down a ravine to the Little Cuyahoga River just northwest of downtown Akron. There were 21 locks round Akron and boats took six hours to pass through two miles. Mills along Crosby\'s mill race used the fall, among them the first mills of Ferdinand Schumacher, founder of Quaker Oats. The 1913 flood ended the canal, and several locks were blown up to keep the water from downtown. The Mustill Store across from Lock 15, once a cigar-box works with its own mill race and best known to canal boatmen as a drinking place, is now a canal museum and visitor centre.',
  'Stone locks and the ruins of waste weirs along a footpath beside the water, two railroad bridges over the gorge, and the Mustill Store and house. The Ohio and Erie Canal Towpath Trail runs through the park.',
  '',
  'Cascade Locks Park, the Cascade Locks Park Association\'s park; a footpath runs beside the locks and the public Ohio and Erie Canal Towpath Trail runs through it. Parking at the Mustill Store trailhead on West North Street. The museum\'s hours were not found on the association\'s pages.',
  [W('Cascade Locks Historic District'),['Cascade Locks Park Association','https://www.cascadelocks.org/'],['National Register record',NR+'92001627']],
  th=[41.09136,-81.51832],thn='Mustill Store lot, West North Street',brick='?'),

N('bf-goodrich-canal-place-akron','B.F. Goodrich factory complex (Canal Place)','Akron','oh','industry','standing',41.07251,-81.52614,'site','view','walk','','1870s–',
  'B. F. Goodrich moved his rubber company to Akron in 1871 after the town\'s citizens offered him $13,600. The downtown complex on South Main Street grew to 27 buildings, including the original factory and the company\'s headquarters. It is now offices and business space called Canal Place, and part of it was listed on the National Register in 2020 as the B.F. Goodrich Company Historic District.',
  'Large brick factory blocks on South Main Street beside the canal and the Towpath Trail. Which buildings date from when, and the inside, not checked.',
  '',
  'Privately owned offices; seen from South Main Street and the Towpath Trail.'+DT,
  [W('Goodrich Corporation'),W('National Register of Historic Places listings in Akron, Ohio')],
  conf='mixed',brick='yes',bcol='red'),

]

PIN_NOTES={
 'summit-county-courthouse-akron':'Wikipedia\'s coordinate, on the courthouse.',
 'glendale-cemetery-akron':'The address point for 150 Glendale Avenue, on a small building by the entrance drive where the chapel and the other old buildings stand; which one is the chapel was not told on the aerial.',
 'first-congregational-church-akron':'Wikipedia\'s coordinate, on the church.',
 'old-akron-post-office-art-museum':'The address point for 70 East Market Street, on the 1899 building.',
 'akron-post-office-federal-building':'Wikipedia\'s coordinate, which falls on East Market Street by the building; on the aerial it could not be told which of the buildings beside it is the old post office, so the pin is within about 100 m.',
 'st-bernard-church-akron':'Wikipedia\'s coordinate, on the church.',
 'old-st-pauls-church-akron':'Wikipedia\'s coordinate, at East Market and Forge streets.',
 'stan-hywet-hall-akron':'Wikipedia\'s coordinate, on the manor house.',
 'hower-house-akron':'The National Register coordinate, on the house.',
 'akron-ymca-building':'Wikipedia\'s coordinate, on the building.',
 'ywca-building-akron':'The National Register coordinate.',
 'firestone-plant-1-akron':'The address point for 1200 Firestone Parkway.',
 'cascade-locks-akron':'The Mustill Store as mapped on OpenStreetMap; the locks run north and south of it.',
 'bf-goodrich-canal-place-akron':'The address point for 520 South Main Street.',
}
