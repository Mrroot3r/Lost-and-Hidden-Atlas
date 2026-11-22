# November 22, 2026: round the edges of the Cohoes, Waterford and Watervliet ground. Drawn at random by
# tools/choose.py --state ny (region conf). Cohoes, Waterford village, Watervliet, Green Island, Crescent and Newtonville
# were worked closely between November 18 and 20, so this batch takes what was still missing a little further out:
# two churches in Mechanicville, a Waterford-gabled house in Waterford village, three Register farmhouses of the 1985
# Colonie survey, the Cyrus Rexford House, and three small burying grounds in Halfmoon and Clifton Park that carry
# Halfmoon Historical Society, bicentennial or Pomeroy Foundation markers. Places in Saratoga County outside Waterford
# are filed under sar and places in Colonie under albco, as earlier batches did.
# Sources were opened in this session: Wikipedia as raw text (tools/wiki_raw.py); HMdb marker pages; the City of
# Mechanicville historian's article "Seeing the Light"; the Episcopal Diocese of Albany's page for St. Luke's on the
# Hill; historypointer.com's copies of Register entries (addresses), all through tools/page.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'conf_zmqk','label':'Mechanicville churches, Colonie farmhouses, Clifton Park burying grounds','added':'2026-11-22 19:51'}
HM=lambda n,t: L('HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n)
HP=lambda r,t: L('historypointer.com: '+t+' (Register entry '+r+')','https://historypointer.com/nris/resource/'+r)
MECH='https://www.mechanicvilleny.gov/SeeingtheLight'
PLACES=[
N('st-paul-apostle-mechanicville','St. Paul the Apostle Church, Mechanicville','Mechanicville','sar','worship','standing',42.90644,-73.68480,'exact','view','drive','','1912–1917',
  'Mechanicville\'s Catholic church, built for a congregation that had its first church by 1872. The cornerstone was laid on June 2, 1912, and the church was dedicated on October 14, 1917. Edward W. Loth of Troy designed it in the Gothic Revival style: a cross-shaped church 148 feet long, of steel and masonry clad in Potsdam sandstone, with a 146-foot tower. It is now part of the parish of All Saints on the Hudson.',
  'Outside: the rough-coursed sandstone walls with cast-stone trim and the tall tower on North Main Street. Inside, by Wikipedia\'s description, are a plaster rib-vaulted ceiling with grapevine reliefs, oak wainscot, lancet windows by the Pike studio of Rochester showing the life of St. Paul, plaster Stations of the Cross by the Joseph Sibbel studio of New York City, and an 1872 Meneely & Kimberly bell of about 1,900 pounds moved from the first church in 1919. Mass times not checked: the parish site could not be read when this was written.',
  'A sandstone Gothic church with a 146-foot tower in the smallest city in the state.',
  'Active Catholic church at 121 North Main Street; parish office 52 William Street, telephone (518) 664-3354 (the Diocese of Albany\'s parish page). Street parking. Go in at Mass times; the parish website (allsaintsny.us) refused to open when this was written, so hours are not given here.',
  [W('St. Paul the Apostle Church (Mechanicville, New York)'),L('Roman Catholic Diocese of Albany: All Saints on the Hudson Parish, Mechanicville','https://www.rcda.org/parishes/parish/all-saints-hudson-parish-mechanicville-site')],
  hours='?',brick='no'),
N('old-st-lukes-mechanicville','Old St. Luke\'s Episcopal Church (Arts Center on the Hudson), Mechanicville','Mechanicville','sar','worship','standing',42.90283,-73.68619,'exact','view','walk','','1897–1898',
  'St. Luke\'s stands on the site of Mechanicville\'s first church, a wooden building put up about 1830 by subscription as a church for all denominations, which became Episcopal in 1832. Dr. Newton H. Ballou, who died in 1895, left $40,000 for a new church on the condition that it be built on the old site of rock-faced stone within three years. The old church and rectory were moved off, the cornerstone was laid on July 6, 1897, the stained glass came from Boston that December and Bishop Doane dedicated the church on April 18, 1898. The congregation moved to a new building, St. Luke\'s on the Hill on McBride Road in Halfmoon, in 2008.',
  'The rock-faced stone church at Park Avenue and South Main Street. The city historian singled out its stained glass window facing Park Avenue, lit in the evenings when he wrote, about 2000; whether it is still lit was not checked. OpenStreetMap now names the building the Arts Center on the Hudson, with "Saint Luke\'s Episcopal Church" as its old name; its present use and whether it opens to visitors were not checked. Interior not checked.',
  'A country doctor\'s will built a stone church on the spot where the town\'s first church stood.',
  'At 2 South Main Street, at the corner of Park Avenue, in the middle of the city. Owner and present use not checked: look from the street. Street parking.',
  [L('City of Mechanicville, city historian: "Seeing the Light"',MECH),L('Episcopal Diocese of Albany: St. Luke\'s on the Hill, Mechanicville','https://albanyepiscopaldiocese.org/st-lukes-mechanicville-ny/')],
  conf='mixed',brick='?'),
N('isaac-eddy-house-waterford','Isaac Eddy House, Waterford','Waterford','conf','landmark','standing',42.78929,-73.67865,'exact','view','walk','','1826',
  'Isaac Eddy built this house in 1826. He owned the Franklin Ink Works in Waterford and devised a way of grinding the ingredients of printer\'s ink to powder; his sons George and Thomas Eddy also became Waterford industrialists. The RiverSpark marker calls it an example of the "Waterford gable" design.',
  'The house at Middle and Third Streets in Waterford village, with its stepped "Waterford gable" ends. A marker stands at the corner. Next door south, at 20 Third Street, a village marker points out the parsonage of the old Dutch Reformed church, which stands; the church itself, moved to 22 Third Street in 1799, was torn down in 1876. Both are private houses; interiors not checked. Red brick: not checked.',
  '',
  'Private house at 37 Middle Street, in the Waterford Village Historic District; look from the street. Street parking in the village.',
  [HM(145305,'Issac Eddy House'),HM(145303,'Parsonage of Dutch Church')],
  brick='?'),
N('martin-dunsbach-house-colonie','Martin Dunsbach House, Colonie','Colonie','albco','landmark','standing',42.78374,-73.75610,'exact','view','drive','','about 1840',
  'A two-storey brick farmhouse of about 1840 in the Greek Revival style, on the road to the old Dunsbach ferry across the Mohawk. Its lower ell has eyebrow windows and takes in an unusual two-bay carriage shed. It was listed on the National Register in 1985 as part of the Town of Colonie\'s survey of historic buildings.',
  'From the road: the brick main block and the long ell with its small eyebrow windows under the eaves and the carriage-shed openings. Private house; interior not checked. Red brick: not checked (the sources say brick but not its colour). Whether it still looks as described in 1985 was not checked on a recent source.',
  '',
  'Private house at 140 Dunsbach Ferry Road (the Register address as copied by historypointer.com); look from the road only. The Mohawk Hudson Bike-Hike Trail and the Dunsbach ferry site in Halfmoon are a short drive north.',
  [W('Martin Dunsbach House'),HP('85002705','Martin Dunsbach House')],
  brick='?'),
N('isaac-haswell-house-colonie','Isaac M. Haswell House, Colonie','Colonie','albco','landmark','standing',42.74821,-73.72592,'site','view','drive','','1880',
  'A two-storey Italianate farmhouse built in 1880, one of the farmhouses the Town of Colonie\'s 1985 survey put on the National Register. Its one-storey porch is dressed with ornate brackets, finials and carved rope mouldings.',
  'The carved front porch with its brackets, finials and rope decoration. Private house; interior not checked. Red brick: not checked.',
  '',
  'Private house at 67 Haswell Road (the Register address as copied by historypointer.com); look from the road only.',
  [W('Isaac M. Haswell House'),HP('85002707','Isaac M. Haswell House')],
  brick='?'),
N('friend-humphrey-house-colonie','Friend Humphrey House, Colonie','Colonie','albco','landmark','standing',42.69224,-73.76326,'exact','view','drive','','about 1841',
  'A two-storey frame farmhouse of about 1841 with a gable roof and two matching chimneys, between the Federal and Greek Revival styles; a one-storey ell was added about 1880. It is named for Friend Humphrey, a member of the State Senate and mayor of Albany. Listed on the National Register in 1985 in the Colonie survey.',
  'From the road: the plain, symmetrical farmhouse with its paired chimneys. Private house; interior not checked. Red brick: not checked. Whether it still looks as described in 1985 was not checked on a recent source.',
  '',
  'Private house at 372 Albany-Shaker Road, Loudonville (the Register address as copied by historypointer.com); look from the road only.',
  [W('Friend Humphrey House'),HP('85002713','Friend Humphrey House')],
  brick='?'),
N('cyrus-rexford-house','Cyrus Rexford House, Rexford','Clifton Park','sar','landmark','standing',42.85593,-73.88910,'exact','view','drive','','about 1850, 1883',
  'A three-storey Stick-style house of 1883 in the canal hamlet of Rexford, built onto a rear block of about 1850 with a one-storey ell behind. It has a steep hipped roof on a bracketed overhang, a busy mix of decorative woodwork and a painted scheme in several colours. A carriage house and a gambrel-roofed barn stand with it. Listed on the National Register in 2011.',
  'From Route 146: the tall hipped-roof house with its Stick-style trim and many-coloured paint, and the carriage house and barn. Private house; interior not checked. Red brick: not checked. The Rexford aqueduct ruins and Erie Lock 21 are a few hundred metres south and west.',
  '',
  'Private house at 1643 Route 146 (the Register address as copied by historypointer.com); look from the road only.',
  [W('Cyrus Rexford House'),HP('10001135','Cyrus Rexford House')],
  brick='?'),
N('millious-cemetery-north-church-clifton-park','Millious Cemetery and the "North Church" site, Clifton Park','Clifton Park','sar','burial','standing',42.85507,-73.79047,'site','view','drive','cemeteries','about 1795',
  'Two markers stand together on Clifton Park Center Road. A Clifton Park bicentennial marker gives this as the site of the Clifton Park Dutch Reformed Church of about 1795, called the "North Church", sold in 1862 and taken down. A Pomeroy Foundation marker of 2025 names the Millious Cemetery as the grave of Samuel Hicks (1740–1830), who served in the 12th Regiment of the Albany County Militia in the Revolution.',
  'The two roadside markers and the small cemetery. Nothing of the church is known to show. Who owns the cemetery and whether its stones can be reached from the road were not checked.',
  '',
  'On Clifton Park Center Road west of Maxwell Road (HMdb). Owner not checked: look from the road. No parking area is known; the road shoulder only.',
  [HM(136451,'Church c. 1795'),HM(313721,'Patriot Burials: Millious Cemetery')],
  conf='mixed',brick='?'),
N('moe-family-cemetery-clifton-park','Moe Family Cemetery, Clifton Park','Clifton Park','sar','burial','standing',42.83390,-73.79392,'site','view','drive','cemeteries','1826',
  'A family burying ground on Moe Road, marked in 2025 by the Pomeroy Foundation and the Sons of the American Revolution as the grave of Abraham Moe, buried here in 1826, who served in the Albany County and Dutchess County militias in the Revolution. Moe Road takes its name from the family; a bicentennial marker about 700 m north, at Grooms Road, marks School No. 5 (the "Little Red Schoolhouse"), which is a separate place in the Atlas.',
  'The marker and the family plot by the road, among the houses of the Clifton Knolls neighbourhood. What stones survive was not checked.',
  '',
  'On Moe Road north of Englemore Road, by 2 Towline Lane (HMdb). Owner not checked: look from the road; no parking area.',
  [HM(303862,'Patriot Burials: Moe Family Cemetery'),HM(154737,'School c. 1860')],
  conf='mixed',brick='?'),
N('newtown-baptist-burying-ground-halfmoon','Newtown Baptist burying ground, Halfmoon','Halfmoon','sar','burial','standing',42.89023,-73.71961,'exact','view','drive','cemeteries','1791',
  'A Halfmoon Historical Society marker of 2016 at Pruyn Hill Road and Farm to Market Road says the Newtown Baptist Church stood on this corner in 1791, and that its cemetery holds the graves of the first settlers.',
  'The marker on the northwest corner and the old cemetery. Nothing of the church is known to show. The size of the cemetery and the age of its stones were not checked.',
  '',
  'At Pruyn Hill Road (County Road 1345) and Farm to Market Road (County Road 109), west of Mechanicville (HMdb). Owner not checked: look from the road; road shoulder only.',
  [HM(125363,'Newtown')],
  conf='mixed',brick='?'),
]
PIN_NOTES={
 'st-paul-apostle-mechanicville':'ArcGIS geocoder PointAddress match for 121 North Main Street, 5 m from the church as OpenStreetMap maps it.',
 'old-st-lukes-mechanicville':'OpenStreetMap building named Arts Center on the Hudson, old name Saint Luke\'s Episcopal Church, 2 South Main Street.',
 'isaac-eddy-house-waterford':'ArcGIS geocoder PointAddress match for 37 Middle Street, Waterford; the HMdb marker is at the corner about 30 m away.',
 'martin-dunsbach-house-colonie':'ArcGIS geocoder PointAddress match for 140 Dunsbach Ferry Road; Wikipedia\'s point is about 140 m north.',
 'isaac-haswell-house-colonie':'ArcGIS geocoder match for 67 Haswell Road, interpolated along the street (not a house point); it falls on the road among several houses, so the pin marks the stretch of road, not the house.',
 'friend-humphrey-house-colonie':'ArcGIS geocoder PointAddress match for 372 Albany-Shaker Road, Loudonville, within 30 m of Wikipedia\'s point.',
 'cyrus-rexford-house':'ArcGIS geocoder PointAddress match for 1643 Route 146, Rexford, within 45 m of Wikipedia\'s point.',
 'millious-cemetery-north-church-clifton-park':'HMdb position of the 2025 Millious Cemetery marker, on the road edge; the church-site marker is 25 m west. The leaf-off aerial shows no gravestones near it, so where the cemetery lies was not seen.',
 'moe-family-cemetery-clifton-park':'HMdb position of the 2025 Moe Family Cemetery marker, on the edge of Moe Road; no gravestones show on the leaf-off aerial (woods east of the road, a house lot west), so the plot itself was not seen.',
 'newtown-baptist-burying-ground-halfmoon':'Moved about 50 m northwest from the HMdb position of the 2016 marker at the crossroads onto the rows of gravestones the leaf-off aerial shows behind the corner, south of a house.',
}
