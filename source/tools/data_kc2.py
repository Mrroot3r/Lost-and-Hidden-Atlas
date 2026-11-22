# November 16, 2026: Kansas City, second pass. The first pass (data_kc.py) was the well-known places inside the city.
# This one starts on the harder-to-find ones round the metropolitan area, on both sides of the state line, for a
# tester who has already been to the easy ones. It is a beginning: three places, with the research leads that could
# not be finished listed in LEADS.md. The same pull request adds the vanished-places, old-mines and OpenStreetMap
# lead layers for Missouri and Kansas, which put several hundred unchecked leads round the city on the map.
# Facts from the linked sources only (Wikipedia read as raw text with tools/wiki_raw.py; Visit Kansas City Kansas,
# KCUR and KC Today for how Quindaro can be seen). Pins were checked on Esri satellite (research/pincheck_kc2_*.jpg).
from data_b import N
from data_ma import W
PLACES=[
N('quindaro-ruins-overlook','Quindaro ruins overlook','Kansas City, Kansas','ks','town','ruins',39.15139,-94.65911,'exact','view','drive','','1857–1860s',
  'Wyandots sold this land in 1856 for a town planned as a Free-State port on the Missouri River, a way into Kansas Territory for settlers opposed to slavery. Building began in 1857 and about 600 people lived here at its peak. It shrank quickly in a national depression and the Civil War, and the lower, commercial part of town under the bluff was abandoned and grew over. Archaeologists found it again in the late 1980s. In 2019 it was named a National Commemorative Site.',
  'A stone platform at the top of the bluff looks down a wooded slope toward the river, where the ruins of the lower town lie. Panels and a marker at the platform tell the story. The ruins themselves are closed: a 2026 radio report says the site is closed to the public and can only be viewed from the overlook, and a local news site says the trail down is closed unless a tour is booked through the city.',
  'A whole abolitionist river port, abandoned in the 1860s, under the trees below a bluff.',
  'The overlook is at 3507 North 27th Street, at Sewell Avenue. View from the platform only: do not go down to the ruins without a booked tour. The sources read give no opening hours for the overlook and do not say who owns the ground. The Quindaro Underground Railroad Museum is nearby in the former Quindaro Colored School.',
  [W('Quindaro Townsite'),['Visit Kansas City Kansas: the Northeast','https://visitkansascityks.com/plan/neighborhoods/northeast'],['KCUR, April 2026','https://www.kcur.org/podcast/up-to-date/2026-04-21/quindaro-isnt-a-national-historic-landmark-yet-kansas-citys-congress-members-want-to-fix-that'],['KC Today: Ruins of Quindaro','https://kctoday.6amcity.com/quindaro-town-ruins-kansas-city-ks-underground-railroad']],was='quindaro-townsite'),
N('sunflower-army-ammunition-plant','Sunflower Army Ammunition Plant','De Soto, Kansas','ks','industry','traces',38.9336,-95.0076,'area','view','drive','','1942–1992',
  'Set up in 1941 on 10,747 acres after Pearl Harbor, this was the largest smokeless-powder plant in the world. The Hercules Powder Company ran it for the government under a contract signed in May 1942. The farm community of Prairie Center stood on the land: the government bought the whole town and razed it, and graves were moved to Eudora and De Soto. The plant went on and off standby with each war, last made propellant in 1992, and was declared surplus in 1998.',
  'A very large fenced tract south of De Soto. The Army handed it to a redevelopment group; more than 6,000 acres were annexed into De Soto in 2022, when work began on a Panasonic battery plant, and a data-centre company bought about 1,435 acres in April 2026. The source does not say how much of the old plant still stands. On Esri satellite the ground round the pin is rows of bare rectangular pads where buildings have been taken down, with one large building to the east.',
  'The plant that swallowed a town, now being swallowed in turn.',
  'Closed land. The sources read describe no public access of any kind: treat it as something to see from public roads only, and expect construction traffic. The pin is the article\'s coordinate for the plant, not a viewpoint.',
  [W('Sunflower Army Ammunition Plant')]),
N('longview-farm','Longview Farm','Lee\'s Summit','kcmo','inst','standing',38.90556,-94.44694,'site','view','drive','','1914',
  'The lumberman R. A. Long had this show farm built in 1913 and 1914: more than 50 buildings on 1,780 acres, finished in 18 months, nearly all of stucco with red tile roofs. It had horse barns for draught, saddle and brood horses, a show-horse barn and arena, dairy and hog barns, a chapel, a school room and its own telephone and plumbing systems. His daughter Loula Long showed horses from here for 65 years. The farm was put on the National Register in 1985.',
  'What is left stands inside a planned neighbourhood called New Longview, built on the last of the farm\'s land with the old buildings restored among new houses and shops. The show-horse arena was turned into an elementary school, dedicated in 2005, and the farm chapel of 1915 is still a working church.',
  'A millionaire\'s model farm with a neighbourhood grown up through it.',
  'See it from the public streets of New Longview. The arena is a school in use and the chapel an active church, and the other buildings are private: none is open to wander into. The sources read give no visiting hours or tours.',
  [W('Longview Farm')]),
]
BATCH={'key':'kc2','label':'Kansas City, second pass: harder-to-find places','added':'2026-11-16 22:30'}
PIN_NOTES={
 'quindaro-ruins-overlook':'On Esri satellite the pin is a small structure at the end of the street, at the edge of the woods. Pin is the OpenStreetMap building "Quindaro Ruins Overlook Structure" on North 27th Street (Nominatim), which matches the street address given by a map listing. The Wikipedia coordinate for the townsite is about 350 m to the north-west, down the slope.',
 'sunflower-army-ammunition-plant':'Pin is the coordinate given in the Wikipedia article, inside a tract of more than 10,000 acres: it marks the plant, not a place to stand. On Esri satellite it sits among rows of cleared building pads.',
 'longview-farm':'Pin is the coordinate given in the Wikipedia article. On Esri satellite it falls on a roundabout among the new houses of New Longview; the old farm buildings are spread round it, so the pin is rated "on site".',
}
