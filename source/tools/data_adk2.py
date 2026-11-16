# November 16, 2026: Adirondacks, a pass for places you walk to. Six ruins and traces beside marked trails or at a
# trailhead, each on public land. Facts from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py),
# the state's own land pages (dec.ny.gov/places/..., parks.ny.gov) for trails, parking and hours, and for the Rock
# Pond mine the Iron Miners mine history page and CNY Hiking. Who manages the ground under each pin is from the
# federal protected-areas database (tools/pad.py).
# New for this batch: each woodland pin was also looked at on the state's LiDAR ground model and leaf-off aerial
# (tools/lidar_sheet.py), and where that showed the feature the pin was put on it. The pin notes say which.
from data_b import N
from data_ma import W
DEC=lambda name,slug:['NYS DEC: '+name,'https://dec.ny.gov/places/'+slug]
BATCH={'key':'adk2','label':'Adirondacks: ruins you walk to','added':'2026-11-16 23:30'}
PLACES=[
N('adirondac-upper-works','Upper Works: the Adirondac ironworks and its 1854 furnace','Newcomb','adk','industry','ruins',44.07886,-74.05626,'exact','public','walk','','1826–1850s',
  'An ironworks was begun here in 1826, deep in the mountains. Its last blast furnace, finished in 1854, stood ten feet taller than the one before it, and was close to obsolete the day it was done: other works were moving to bigger stacks burning anthracite, and this one still burned charcoal. Titanium in the ore had made the iron hard to work all along. In 1940 a new mine opened nearby for that same titanium; its buildings stood until after 2005 and have since been taken down. The works was put on the National Register in 1977.',
  'The stone blast furnace stands beside Upper Works Road; the leaf-off aerial shows a roofed structure and a pull-off at the pin. The village of Adirondac that served the works is about a kilometre further up the road, where OpenStreetMap marks it, near a parking area at the road\'s end.',
  'A furnace that was out of date the day it was finished, at the door of the High Peaks.',
  'On Upper Works Road north of Tahawus. The ground is the Tahawus Core Historic Area, 210 acres owned by the Town of Newcomb, where the public has recreation rights under a conservation easement that the state manages. The sources read give no hours or fee. Look from the paths: old stone and ironwork are not for climbing on.',
  [W('Adirondack Iron and Steel Company'),W('Tahawus, New York'),DEC('High Peaks Wilderness Complex','high-peaks-wilderness-complex')]),
N('crown-point-forts','Crown Point: the ruins of two forts','Crown Point','adk','fort','ruins',44.02917,-73.43111,'site','public','walk','','1730s and 1759',
  'The French built Fort Saint-Frédéric here in the 1730s, with thick limestone walls, at a narrows of Lake Champlain. The British went after it twice in the French and Indian War, and in the summer of 1759 the French destroyed it themselves. That year British and colonial troops built Fort Crown Point beside it, the largest earthen fortress built in the American colonies.',
  'The earth and stone ruins of both forts, a National Historic Landmark, on an open point in the lake.',
  'Two forts, one blown up by its own garrison, side by side on the lake.',
  'Crown Point State Historic Site. The grounds are open from sunrise to sunset all year, free of charge. The museum opens at 9:30 am, with last entry at 4:30 pm, Wednesday to Sunday, from early May to mid October (May 9 to October 18 in 2026).',
  [W('Fort Crown Point'),['NYS Parks: Crown Point State Historic Site','https://parks.ny.gov/visit/historic-sites/crown-point-state-historic-site']]),
N('jayville','Jayville, an iron-mining hamlet','Pitcairn','nny','town','traces',44.15417,-75.18889,'area','public','walk','','1850–after 1914',
  'A mining hamlet from 1850, on what became the Carthage and Adirondack Railroad. The iron property was opened in 1854. The ore was awkward in its make-up and hard to get at, and the mines were given up in favour of Benson Mines, further east along the railroad. An attempt to reopen them in 1914 failed, and a fire finished the hamlet.',
  'The article says remnants can be found off the abandoned railroad station on state land. On LiDAR the old railroad bed shows as a long straight embankment beside Jayville Road, with a round pond about 40 m across against it that may be a flooded pit, and rough ground on the hillside to the north-west. The leaf-off aerial shows the pond and woods. What is a mine working and what is natural was not settled from the air.',
  'A mine that lost out to the next one down the line, then burned.',
  'State land south-east of Harrisville on Jayville Road; the protected-areas database names it Aldrich Pond Wild Forest. No parking place or trail to the remains was found in the sources read. Old mine pits can be deep and flooded: keep back from the edges.',
  [W('Jayville, New York'),DEC('Aldrich Pond Wild Forest','aldrich-pond-wild-forest')],conf='mixed'),
N('forest-lodge-lake-lila','Forest Lodge site, Lake Lila','Long Lake','adk','inst','traces',44.0040,-74.7752,'site','public','hike','','1890s–1979',
  'William Seward Webb put together a private preserve, Nehasane Park, in 1892 while building his railroad through the Adirondacks, and built a Great Camp called Forest Lodge on the west shore of the lake, which he renamed for his wife Lila. New York State bought the land round the lake in 1979, and the state razed the lodge at the family\'s request as part of the purchase. The railroad station that served it still stands.',
  'On LiDAR: level terraces cut into the slope just above the west shore, beside an old road that runs behind them. The leaf-off aerial shows open hardwoods, one small structure by the road, and nothing else standing. The pin is on the terraces. Not checked on the ground.',
  'A Vanderbilt-family Great Camp, taken down by the state that bought it.',
  'State land: the protected-areas database names it Nehasane Primitive Area, and Lake Lila is the largest lake in the park whose whole shore is state-owned. The state\'s page says only that a long dirt access road from County Route 10 leads to the parking area; the sources read do not give the distance from there to the lodge site.',
  [W('Lake Lila'),DEC('Lake Lila','lake-lila')]),
N('calamity-trail-quarry','Granite quarry on the Calamity Trail','Westport','adk','industry','traces',44.21706,-73.38526,'area','public','hike','','19th century',
  'The state\'s page for Split Rock Mountain says its Calamity Trail passes through the remnants of a 19th-century granite quarry. It gives no more of the quarry\'s story than that.',
  'Whatever is left lies somewhere along a 1.6-mile trail. At the pin, a point on the trail, LiDAR shows knobby bare rock and no clear quarry face, so the exact spot is still to be found.',
  'A quarry the trail walks straight through.',
  'Split Rock Mountain Wild Forest, state land. The Calamity Trail runs 1.6 miles from the Lake Shore Road Trailhead to the Barn Rock Bay Trail, climbing 100 feet in the first half mile.',
  [DEC('Split Rock Mountain Wild Forest','split-rock-mountain-wild-forest')]),
N('rock-pond-graphite-mine','Rock Pond graphite mine','Ticonderoga','adk','industry','ruins',43.8540,-73.5952,'site','public','hike','','1901–1906',
  'Gray Brothers opened a graphite mine on this pond in 1901. The next year the Ticonderoga Graphite Company built a ten-stamp mill to crush the ore; the Columbia Graphite Company tried the ore in 1903 and worked the mine in 1904 and 1905, then leased it to Pettinos Brothers in 1906. Nothing is known of it being worked after that.',
  'An adit tunnel, a large open cut where nearly all the graphite came out, and a steam boiler still in place; a hiker\'s account adds foundations just past the mine on the way to the lean-to. On LiDAR a steep-sided cut shows on the north shore, and the pin is on it.',
  'A boiler and a tunnel on the shore of a back-country pond.',
  'Pharaoh Lake Wilderness, state land. The usual way in is from Putnam Pond Campground, about 1.6 miles one way to the Rock Pond lean-to; the Rock Pond Trail is a 1.9-mile loop round the shore. A day-use fee is charged to park at the campground when it is open. Old mine tunnels are not safe to enter.',
  [['Iron Miners: Rock Pond Mine','https://ironminers.com/mine-history/rock-pond-mine'],DEC('Pharaoh Lake Wilderness','pharaoh-lake-wilderness'),['CNY Hiking: Rock Pond','https://cnyhiking.com/RockPondPLW.htm']]),
]
PIN_NOTES={
 'adirondac-upper-works':'Pin is the OpenStreetMap feature "McIntyre Blast Furnace" on Upper Works Road (Nominatim), about 90 m from the Wikipedia coordinate. Looked at on LiDAR and the leaf-off aerial: a roofed structure and a pull-off beside the road.',
 'crown-point-forts':'Pin is the coordinate given in the Wikipedia article for the fort.',
 'jayville':'Pin is the coordinate given in the Wikipedia article. Looked at on LiDAR and the leaf-off aerial: the old railroad bed and a round pond are within 150 m; no single ruin could be picked out, so the pin is rated approximate.',
 'forest-lodge-lake-lila':'Pin is on level terraces that LiDAR shows above the west shore, about 110 m east of the OpenStreetMap point for Nehasane. Looked at on LiDAR and the leaf-off aerial. That these terraces are the lodge site is a reading of the ground model, not something a source states.',
 'calamity-trail-quarry':'Pin is a point on the Calamity Trail from OpenStreetMap (Nominatim), not the quarry itself, which was not found on LiDAR there. Rated approximate.',
 'rock-pond-graphite-mine':'Pin is a steep-sided cut on the north shore that LiDAR shows, taken to be the mine\'s open cut; the sources put the mine on the north shore between the pond\'s west end and the lean-to. Looked at on LiDAR and the leaf-off aerial.',
}
