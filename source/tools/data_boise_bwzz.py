# November 26, 2026: buildings of downtown Boise and the North End, Idaho, taken from the names in one walk-through video
# (a tip only; nothing in these entries comes from it). Sources read: Wikipedia articles and the Register list for Ada
# County, National Register nomination forms on NPGallery, the City of Boise's history bollard pages for Julia Davis
# Park, the Idaho Architecture Project (Preservation Idaho), and the Cathedral of St. John the Evangelist's own page.
# No interior was seen by any source unless the entry says so.
from data_b import N
from data_ma import W
BATCH={'key':'boise_bwzz','label':'Boise, Idaho: downtown and the North End','added':'2026-11-26 09:45'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
def IAP(slug,label):
    return ['Idaho Architecture Project: '+label,'https://www.idahoarchitectureproject.org/properties/%s/'%slug]
BOL='https://www.cityofboise.org/departments/parks-and-recreation/julia-davis-park-rotary-grand-plaza/decorative-bollards/'

PLACES=[
N('st-johns-cathedral-boise','Cathedral of St. John the Evangelist (St. John\'s Cathedral)','Boise','id','worship','standing',43.62146,-116.19855,'exact','open','walk','','1906–1921',
  'The cathedral of the Catholic Diocese of Boise. Bishop Alphonse Glorieux bought the block between Fort, Hays, Eighth and Ninth Streets and laid the cornerstone in 1906; the congregation worshipped in the finished lower level while the walls and roof went up, which were done in 1912, and the cathedral was dedicated at Easter 1921. Tourtellotte & Hummel of Boise designed it in the Romanesque Revival style, taking the cathedral of Mainz and the basilica of Saint-Sernin in Toulouse as models. It was listed on the National Register in 1978.',
  'A Romanesque church with two front towers that were meant to carry spires and were never finished. Inside, the nave windows show the life of Christ, Saint Cecilia is in the window over the organ, and the three-manual organ was installed by Tellers-Kent in 1921 (Wikipedia). The cathedral\'s own page offers self-guided visits and Sunday docent tours.',
  'Spires drawn for the front towers in 1906 and never built.',
  'An active Catholic cathedral at 775 North 8th Street, run by its parish. Visiting times and Mass times are from the cathedral\'s own page; outside them, look from the street. Street parking round the block; mapped lots on West Franklin and West Washington Streets are about 110 to 180 m away (owners not checked).',
  [W('Cathedral of St. John the Evangelist (Boise, Idaho)'),['Cathedral of St. John the Evangelist: home page','https://boisecathedral.org'],NR('78001035','St. John\'s Cathedral')],
  brick='?',hours='Self-guided visits Mon and Tue 1:30-3 p.m., Thu and Fri 10-11:30 a.m.; docent tours Sun 3-4:30 p.m.; Sunday Mass 8 and 10:30 a.m., 1 p.m. (Spanish), 5 p.m.'),
N('boise-high-school','Boise High School','Boise','id','civic','standing',43.621163,-116.202603,'site','view','walk','','1908–',
  'Boise\'s first high school building, laid in 1902, was red brick and was soon outgrown. Tourtellotte & Hummel, later the architects of the State Capitol, designed its successor in white brick in a grand classical manner: the east wing went up in 1908 and the west wing in 1912, and a central wing later replaced the old red building between them (Wikipedia; City of Boise). Idaho\'s first radio station broadcast from the east wing\'s basement. The campus is on the National Register.',
  'A white brick school with a columned classical front filling the block on West Washington Street between Ninth and Eleventh. Still a working public high school; interior not checked.',
  '',
  'A working public school of the Boise School District at 1010 West Washington Street. Look from the street; the grounds and buildings are not open to visitors during school hours. Street parking.',
  [W('Boise High School'),['City of Boise: Boise High School 1903',BOL+'boise-high-school-1903/'],NR('82000180','Boise High School Campus')],
  brick='no'),
N('idanha-hotel-boise','Idanha Hotel','Boise','id','hotel','standing',43.61693,-116.2054,'exact','view','walk','','1901–',
  'A six-storey hotel at Tenth and Main, designed by W. S. Campbell and built in 1901 for $125,000, at the time the costliest building in Boise. It ran as a hotel until it was turned into apartments in the 1970s, and was listed on the National Register in 1974.',
  'Red brick in the French château manner, with round turrets on three corners and a mansard roof, on a sandstone basement, one of the few downtown buildings left on one. Now apartments, with a restaurant and shops on the ground floor and in the basement (Wikipedia). The upper floors are private; interior not checked.',
  'Boise\'s grandest hotel of 1901, with its turrets still on.',
  'Privately owned apartments at Tenth and Main Streets. Look from the street; the ground-floor businesses keep their own hours. Street parking and downtown garages.',
  [W('Idanha Hotel'),NR('74000728','Idanha Hotel')],
  brick='yes'),
N('hoff-building-boise','Hoff Building (Hotel Boise)','Boise','id','hotel','standing',43.617609,-116.202198,'site','view','walk','','1930–',
  'Built in 1930 as Hotel Boise, eleven storeys of Art Deco by Tourtellotte & Hummel and counted Boise\'s first skyscraper; it stands where a Methodist church had been. It was a hotel until 1976, when Hoff Companies bought it, turned it into offices, added two floors and took off the Art Deco details; a later owner put the details back two years after.',
  'A tall Art Deco block at Eighth and Bannock with patterned ornament at the top; offices inside. A contributing building of the Boise Capitol Area District on the National Register. Interior not checked.',
  '',
  'A private office building at 802 West Bannock Street. Look from the street. Street parking and downtown garages.',
  [W('Hoff Building')],
  brick='no'),
N('owyhee-hotel-boise','Owyhee Hotel','Boise','id','hotel','standing',43.61729,-116.207531,'site','view','walk','','1910–',
  'A six-storey hotel opened in 1910, designed by Tourtellotte & Hummel and fitted out to outdo the Idanha, Boise\'s one other large hotel then; its roof garden had a restaurant, a bar and a dance floor. Decades of alterations from the 1970s on took away much of the original work, and from 2013 the building was renovated into apartments and offices, with new windows on the old pattern and bricked-up ground-floor openings reopened (Idaho Architecture Project).',
  'The hotel\'s original billiards room, the one space that kept its 1910 character, was made into a restaurant; the lobby\'s dome was moved to the entry of the Idaho History Museum (Idaho Architecture Project). Upper floors private; interior not checked otherwise.',
  '',
  'Privately owned apartments and offices at 1109 West Main Street. Look from the street; ground-floor businesses keep their own hours. Street parking.',
  [IAP('owyhee-plaza-hotel','Owyhee Plaza Hotel')],
  brick='no'),
N('old-post-office-boise','Old U.S. Post Office and Federal Building (Borah Building)','Boise','id','civic','standing',43.61735,-116.2013,'site','view','walk','','1902–1905',
  'The first federal building in Boise, at Eighth and Bannock, drawn by the Supervising Architect James Knox Taylor in 1899 and built from 1902 (the Idaho Architecture Project; other sources give 1901) to 1905 as the post office and federal court. Short of money, Taylor used brick with sandstone from the Table Rock quarry above town, and the granite of the steps was said to be the largest block quarried in the area. It was enlarged later; the federal courts moved to a new building on Fort Street in 1968.',
  'A classical stone-and-brick building facing the Capitol along Eighth Street. The Idaho Architecture Project says much of the 1902 fabric is kept: varnished oak panelling, chipped-glass vestibule panes, bronze door fittings and ornamental elevator metalwork. Who uses it now and when it is open were not checked.',
  '',
  'At 304 North 8th Street, across from the Capitol. The Idaho Architecture Project says the federal government sold it to the state; current use and opening hours not checked, so look from the street. Street parking and downtown garages.',
  [IAP('original-us-post-office','Original US Post Office')],
  conf='mixed',brick='no'),
N('old-ada-county-courthouse-boise','Old Ada County Courthouse','Boise','id','civic','standing',43.616792,-116.198011,'site','view','walk','','1938–1939',
  'Built in 1938 and 1939 with Depression public-works money; Wayland & Fennell with Tourtellotte & Hummel designed it in Art Deco, faced in Indiana limestone. It was the county courthouse and jail from 1939 to 1999. The Legislature met in it in 2008 while the Statehouse was renovated, and from 2015 it housed the Idaho Law and Justice Learning Center (City of Boise; Idaho Architecture Project).',
  'Nine storeys, limestone on the lower four, with pink Tennessee marble in the lobby. Inside are 26 murals painted on canvas in 1940 under the New Deal art programme, the largest such set in Idaho; one, showing a lynching, has been kept covered (City of Boise; Idaho Architecture Project). Whether the public can see them now was not checked.',
  'Twenty-six New Deal murals in a courthouse that was nearly torn down.',
  'Owned by the State of Idaho, at 514 West Jefferson Street just east of the Capitol. Current opening hours not checked; look from the street. Street parking and the state\'s Capitol Mall garages.',
  [['City of Boise: Ada County Courthouse',BOL+'ada-county-courthousefallen-soldiers-memorial/'],['Idaho Architecture Project: Old Ada County Courthouse','https://www.idahoarchitectureproject.org/?p=1587']],
  brick='no'),
N('carnegie-library-boise','Carnegie Public Library','Boise','id','civic','standing',43.619601,-116.200562,'site','view','walk','','1904–1905',
  'Boise\'s public library began in 1895 as a subscription reading room in City Hall. A Carnegie grant of 1904 paid for this building, designed by Tourtellotte & Hummel and opened in June 1905. The library moved out in 1973; the building was then a law office and since 2018 has been studios for artists. It was listed on the National Register in 1974.',
  'A small Neoclassical library of white brick fired in Boise, trimmed with sandstone from Table Rock. Interior not checked.',
  '',
  'Privately used, at 815 West Washington Street. Look from the street. Street parking.',
  [W('Carnegie Public Library (Boise, Idaho)'),NR('74000725','Carnegie Public Library')],
  brick='no'),
N('longfellow-school-boise','Longfellow School','Boise','id','civic','standing',43.627951,-116.198968,'site','view','walk','','1906–',
  'A two-storey Mission Revival school of brick and sandstone in the North End, designed by Wayland & Fennell and finished in 1906, the seventh schoolhouse of Boise\'s school district. It was built with separate entrances for boys and girls, twelve classrooms and a basement flat for the janitor, and has been a school ever since. It was listed on the National Register in 1982.',
  'Look for the Mission Revival front and the two entrances. Still a working school; interior not checked.',
  '',
  'A working public elementary school at 1511 North 9th Street. Look from the street; not open to visitors during school hours. Street parking.',
  [W('Longfellow School (Boise, Idaho)'),NR('82000219','Longfellow School')],
  brick='?'),
N('fort-boise-officers-house','Fort Boise Officers\' House (Building No. 1)','Boise','id','fort','standing',43.62038,-116.18779,'area','view','walk','','1863–1864',
  'The army founded Fort Boise in 1863 to guard the gold country of the Boise Basin, and Boise was laid out at the same time. Its builders had to quarry sandstone and make their own bricks and lime, and an English architect, Charles May, oversaw the first buildings. The commander\'s house, the first of officers\' row, was begun in 1863 and finished in 1864. The army left in the 1930s, and the Veterans Administration took the post over; the house became its administration building (Idaho Architecture Project).',
  'The 1972 Register form says some 1864 buildings still stand, chief among them the quartermaster\'s building and the one house left of the original officers\' row, both of native sandstone, among later post buildings and the veterans\' hospital. Interior not checked.',
  'The oldest buildings in Boise are the army\'s, not the town\'s.',
  'On the grounds of the Boise VA Medical Center at 500 West Fort Street, a federal hospital: look from Fort Street and do not go into working buildings. Visitor parking is the hospital\'s; street parking on Fort Street.',
  [IAP('fort-boise-officers-home','Fort Boise Officer\'s House'),NR('72000433','Fort Boise')],
  brick='no'),
]

PIN_NOTES={
 'st-johns-cathedral-boise':'The address lookup for 775 North 8th Street fell on a small building on the block; moved about 60 m onto the cathedral as seen on the aerial, matching the Wikipedia coordinate.',
 'boise-high-school':'Street address 1010 West Washington Street, found with an address lookup; the pin marks the campus.',
 'idanha-hotel-boise':'OpenStreetMap\'s point for the Idanha Hotel building at 928 West Main Street.',
 'hoff-building-boise':'Street address 802 West Bannock Street, found with an address lookup and checked on the aerial.',
 'owyhee-hotel-boise':'Street address 1109 West Main Street, found with an address lookup and checked on the aerial.',
 'old-post-office-boise':'Street address 304 North 8th Street, found with an address lookup and checked on the aerial.',
 'old-ada-county-courthouse-boise':'Street address 514 West Jefferson Street, found with an address lookup and checked on the aerial.',
 'carnegie-library-boise':'Street address 815 West Washington Street, found with an address lookup and checked on the aerial.',
 'longfellow-school-boise':'Street address 1511 North 9th Street, found with an address lookup; the pin marks the school grounds.',
 'fort-boise-officers-house':'The address 500 West Fort Street is the whole hospital campus and its lookup fell on a modern hospital block. The pin is moved to a small building on the east side of the grounds that OpenStreetMap dates to 1863; which of the old buildings is the officers\' house was not confirmed, so the pin marks only the area of the old post buildings.',
}
