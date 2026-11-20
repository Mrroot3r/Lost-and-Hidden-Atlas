# November 20, 2026: the old Town of Watervliet's country round Cohoes: the Boght, Latham, Loudonville and Menands.
# Drawn at random by tools/choose.py --state ny (region conf). Cohoes, Waterford, Watervliet and Green Island had been
# worked five times already (data_conf_simf.py, data_conf_biei.py, data_conf_kovn.py, data_conf_edvk.py,
# data_conf_fmbb.py), so this batch takes the ground just west and south of them in the Town of Colonie, which the
# start.py briefing showed with no Atlas place at all in Loudonville or Menands. Places in Colonie are filed under albco,
# as the earlier conf batches filed the Pruyn House and the Newtonville places. The one Cohoes lead tried, the Godfrey Farmhouse, went back to the note.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); historypointer.com's copies of the
# National Register entries for street addresses; the Town of Colonie multiple resource nomination (NPGallery text,
# 64000545); HMdb marker pages; the Village of Menands' Sage Estate Trails pages and trail map.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'conf_fvsv','label':'The Boght, Loudonville and Menands','added':'2026-11-20 09:39'}
HM=lambda n,t: L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
HP=lambda r,t: L('historypointer (National Register entry): '+t,'https://historypointer.com/nris/resource/'+r)
MRA=L('National Register: Town of Colonie multiple resource area (NPGallery text)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/64000545_text')
PLACES=[
N('boght-road-dutch-houses-colonie','Boght Road: the Van Denbergh-Simmons House, the Simmons Stone House and the Boght church site','Colonie','albco','landmark','standing',42.78547,-73.73442,'exact','view','drive','','about 1720–1849',
  'The Boght, the bend of the Mohawk above Cohoes, was settled from 1704 by Dutch families on land the Mohawks gave in 1667 to Hilletje van Olinde, interpreter for the province; Boght Road follows the old northern boundary of the manor of Rensselaerswyck (1929 state marker). The Van Denbergh-Simmons House at 537 Boght Road grew in three parts: a Dutch house of about 1720 to 1760, a kitchen ell of about 1790 with a beehive oven, and an Italian villa wing with a square tower of about 1847, added by the Cohoes industrialist Daniel Simmons. The Colonie survey found it the only house of its type left in the town, and its Dutch part the only building left from the manor period. Simmons also built the stone house at 554 Boght Road in 1847–49, the only historic stone house in the town. The Reformed Dutch Church of the Boght, organized in 1784 and the first church north of Albany, stood nearby; a 1932 state marker gives its site.',
  'From the road: the low Dutch house with the tall towered villa wing beside it at 537, and 200 m west the cruciform stone house of rough ashlar with its wide eaves and cobblestone-based porch at 554. The church marker is on Boght Road (Route 9R) by number 583, and the 1929 marker for the Boght settlement is beside it. The register also lists the remains of a barn foundation at 537 (not seen). Interiors not checked.',
  'A 1720s Dutch farmhouse with a Victorian tower bolted on, still standing on the old manor line.',
  'Both houses are private homes: look from Boght Road (NY 9R) and do not go onto the lawns. No parking lot; Boght Road is busy, so stop only where the shoulder is wide.',
  [W('Van Denbergh-Simmons House'),W('Simmons Stone House'),MRA,HM(24730,'Reformed Dutch Church of the Boght'),HM(24731,'The Boght'),HP('85002751','Van Denbergh-Simmons House, 537 Boght Rd.'),HP('85002747','Simmons Stone House, 554 Boght Rd.')],brick='?'),
N('bryans-store-loudonville','Bryan\'s Store and the Loudon Road Historic District','Loudonville','albco','civic','standing',42.70583,-73.75431,'exact','view','drive','','1862 (moved here); district about 1811–1930s',
  'Bryan\'s Store began as a saloon and was moved to this spot on the Loudon road in 1862, where it became the hamlet\'s general store and post office. It is a two-story frame building with a slate roof on a brick foundation, listed on the National Register in 1979. The Loudon Road Historic District, listed the same year, runs along Loudon Road from Crumite Road to Menands Road and holds twenty buildings from Loudonville\'s growth: the Elias Ireland house of about 1820, a school of 1811 rebuilt about 1850, late-19th-century summer cottages including Judge Ira Harris\'s, and Georgian Revival houses of the early 1900s.',
  'The old store at 435 Loudon Road, a long clapboard building with a gable and a shopfront: the photograph on its Wikipedia article (undated) shows it as a shop, Genoa Importing Co.; whether that shop is still there and its hours were not checked. The district\'s buildings are along the same road. Interiors not checked.',
  '',
  'View from Loudon Road (US 9), a busy four-lane road; the store and the district\'s houses are private property. Owner and present use not checked.',
  [W('Bryan\'s Store'),W('Loudon Road Historic District'),HP('79003246','Bryan\'s Store, 435 Loudon Rd.'),HP('79003247','Loudon Road Historic District')],brick='no'),
N('ddt-moore-farmhouse-loudonville','D. D. T. Moore Farmhouse','Loudonville','albco','landmark','standing',42.69263,-73.75404,'exact','view','drive','','1850',
  'Daniel D. Tompkins Moore, an abolitionist and superintendent of the West Albany stockyards, bought 52 acres here in 1845. His Middlebrook farm and peach orchard was named the best farm in New York State in 1851 and grew to 2,500 acres, much of it now the Corporate Woods office park. The house, of 1850, is a two-and-a-half-story frame farmhouse mixing Colonial and Greek Revival, given its porches in the 1890s. After Moore died in 1858 the land was sold off and the place became an estate; it was listed on the National Register in 1979.',
  'The farmhouse at the corner of Leslie Court and Loudon Road, white-painted frame with its porches (Wikipedia photograph), among hemlock, maple and beech left from the grounds. Wikipedia carries a photograph dated 2025. Private; interior not checked.',
  'The best farm in New York in 1851, now a lone house beside Route 9 and an office park.',
  'Private home. Look from Loudon Road (US 9) or Leslie Court only.',
  [W('D. D. T. Moore Farmhouse'),HP('79003244','D. D. T. Moore Farmhouse, 352 Loudon Rd.')],brick='no'),
N('goodrich-school-colonie','Goodrich School','Colonie','albco','civic','standing',42.7291,-73.7469,'area','view','drive','','about 1922',
  'A one-story brick district school of about 1922 in the Classical Revival style, with a hipped-roof wing of about 1926 and two additions of the 1950s on the south side. Its front has a portico with a curved underside on six fluted Doric columns, and an octagonal wooden cupola with a copper roof sits on the roof. It was listed on the National Register in 2000. Nearby, the former Colonie Village School was demolished, as the Preservation League of New York State reported.',
  'The six-column portico and the copper-roofed cupola, from Fiddlers Lane; the Wikipedia photograph shows red brick walls with the white portico. Present use and owner not checked; interior not checked.',
  '',
  'View from the street only. Present use not checked: the Register gives its address only as Fiddlers Lane.',
  [W('Goodrich School'),HP('00001156','Goodrich School, Fiddlers Ln.'),L('Preservation League of NYS: Demolition alert, former Colonie Village School','https://preservenys.org/blog/demolition-alert-former-colonie-village-school')],conf='mixed',brick='yes'),
N('hedge-lawn-menands','Hedge Lawn','Menands','albco','landmark','standing',42.70581,-73.71454,'exact','view','drive','','1870',
  'A mansion of 1870 on Broadway between Watervliet and Albany, two and a half stories in an odd mix of Greek Revival and Second Empire: a mansard roof of scalloped slate with three pedimented dormers over a full-height portico of six heavy Doric columns. A carriage house, two wagon sheds, an iron fence and old plantings survive with it. The Colonie survey notes that its owners, the Jermains, were benefactors of the Menands Home for Aged Men up the road (see Menands Manor). Listed on the National Register in 1985.',
  'The six-column portico under the mansard, the iron fence and the carriage house, from Broadway. Present use not checked; interior not checked.',
  '',
  'Private. View from Broadway (NY 32). Present owner and use not checked.',
  [W('Hedge Lawn'),MRA,HP('85002710','Hedge Lawn, 592 Broadway')],brick='?'),
N('menands-manor','Menands Manor (Home for Aged Men)','Menands','albco','inst','standing',42.69297,-73.72495,'exact','view','drive','','before 1840; 1877',
  'A house built before 1840 was made over in 1877, in the Stick and Eastlake style, as the Home for Aged Men. It is a U-shaped brick building with a many-gabled slate roof, two three-story corner towers with pyramid roofs and iron cresting, and a two-story porch across the front; a brick wing was added in the 1920s. In 1982 it was the Home for Aged Men and Women. Listed on the National Register in 1985.',
  'The two towers with their iron cresting and the long porch, from Broadway at 272. Present use not checked; interior not checked.',
  '',
  'View from Broadway (NY 32). Present owner and use not checked; if it is still a residence for the elderly, do not go in or onto the grounds.',
  [W('Menands Manor'),MRA,HP('85002743','Menands Manor, 272 Broadway')],brick='?'),
N('menand-park-louis-menand-house','Menand Park bungalows and the Louis Menand House','Menands','albco','town','standing',42.70291,-73.72292,'site','view','walk','','about 1840; 1881; 1913–1925',
  'Louis Menand, whose name the village carries, had his farmhouse at the cemetery gates: a rear part of about 1840 and a Queen Anne front of 1881 with fishscale shingles in the gables; the foundation of his greenhouse is listed with it. St. Agnes Cemetery bought the house and three and a half acres in 2016, and it is now the office of Albany Diocesan Cemeteries. Round it, the Menand Park Historic District holds 21 houses of 1913 to 1925, bungalows and Prairie-style houses with low roofs, wide eaves, exposed rafters and porches on massive brick or cobblestone piers.',
  'The Menand house at 40 Cemetery Avenue, then a walk through the streets between Menand Road, Broadway and Tillinghast Avenue for the bungalows, their cobblestone piers and chimneys. Interiors not checked.',
  '',
  'The house is the cemeteries\' office and the bungalows are private homes: look from the streets. Office hours not checked. Albany Rural and St. Agnes cemeteries are next door (see those places).',
  [W('Louis Menand House'),W('Menand Park Historic District'),HP('85002742','Louis Menand House, 40 Cemetery Ave.'),HP('85002708','Menand Park Historic District')],brick='?'),
N('sage-estate-trails-menands','Sage Estate Trails (the Fern Brook estate woods)','Menands','albco','inst','traces',42.6905,-73.7335,'area','public','walk','','1890s',
  'In the 1890s Henry M. Sage, of the Albany lumber family, bought the Isaac Chapman estate south of Menand Road and built Fern Brook, a country mansion designed by Marcus T. Reynolds. It was a working farm as well as a showplace, with a dairy barn, sheep, gardens, a carriage house, root cellars, and a 200-foot concrete and stone "Rainbow Bridge" across the gully of the Rutgers Kill to the orchards and hayfields on the south side. Sage died in 1933 and his widow Cornelia lived there until 1972; the estate went to Rensselaer Polytechnic Institute, which sold it in 1973 to Albany International. The village of Menands took the land south of the gully to keep it "forever wild", and the bridge was torn down in the 1990s.',
  'About 65 acres of woods with trails that, the village says, sometimes follow the estate\'s old carriage and wagon roads, down into the gully of the Rutgers Kill. The bridge is gone; the village pages name no other ruin on the trails, and none was checked. The mansion (National Register 1980) stands on private ground to the north among the Sage Estates houses, and was not checked.',
  'Walk the carriage roads of a lumber baron\'s estate, where his 200-foot bridge used to be.',
  'The woods south of the Rutgers Kill belong to the Village of Menands, which bought them to keep forever wild (village history page); open dawn to dusk (village page). Main entrance and parking lot off Park Drive; other entrances at Upland Avenue, by Menands School, and at Littles Lake on Van Rensselaer Boulevard (village trail map). Dogs on leash, no motor vehicles, no hunting, no fires, no camping. The mansion grounds are private.',
  [L('Village of Menands: Sage Estates Trail history','https://menandsny.gov/sage-estates-trail-history/'),L('Village of Menands: Sage Estate Trails, uses and regulations','https://menandsny.gov/sage-estates-trail-uses/'),L('Village of Menands: Sage Estate Trails, main entrance and map','https://menandsny.gov/sage-estates-trail/'),W('Henry M. Sage Estate')],
  th=[42.68901,-73.73590],thn='Sage Estate Trails main entrance lot, Park Drive',hours='Dawn to dusk',brick='?'),
]
PIN_NOTES={
 'boght-road-dutch-houses-colonie':'ArcGIS PointAddress for 537 Boght Road (the Van Denbergh-Simmons House); the Simmons Stone House is the PointAddress for 554, about 330 m west, and the church marker HMdb gives at 42.78367, -73.7404. The leaf-off aerial shows a house under the ring.',
 'bryans-store-loudonville':'ArcGIS PointAddress for 435 Loudon Road, the Register address; Wikipedia gives 42.70556, -73.75472. The aerial shows a building beside Loudon Road under the ring.',
 'ddt-moore-farmhouse-loudonville':'ArcGIS PointAddress for 352 Loudon Road, the Register address; Wikipedia gives 42.69333, -73.75556. The aerial shows a house under the ring.',
 'goodrich-school-colonie':'Wikipedia point; the Register gives only Fiddlers Lane, and the geocoder put the lane at 42.72038, -73.75557. The aerial shows a building beside a school lot and playground in the ring; which wing is the 1922 school was not settled.',
 'hedge-lawn-menands':'ArcGIS PointAddress for 592 Broadway, Menands, the Register address; Wikipedia gives 42.70583, -73.71528. The aerial shows a large white-roofed house in grounds under the ring.',
 'menands-manor':'ArcGIS PointAddress for 272 Broadway, Menands, the Register address; Wikipedia gives 42.69306, -73.72528. The aerial shows a large building with wings under the ring.',
 'menand-park-louis-menand-house':'ArcGIS PointAddress for 40 Cemetery Avenue (the Louis Menand House); the district lies round it between Menand Road, Broadway and Tillinghast Avenue. The aerial shows a small building by the railway, at the cemetery side, under the ring.',
 'sage-estate-trails-menands':'The middle of the trails on the village trail map, by the event pavilion over the gully; the leaf-off aerial shows only treetops there and the LiDAR straight trail and road lines and the gully. The parking point is the paved stub running north into the woods from the road on the aerial, 74 m from where OpenStreetMap puts its "Sage Estate Preserve Main Entrance Lot" (which falls on the road); the village map puts the main entrance and parking there.',
}
