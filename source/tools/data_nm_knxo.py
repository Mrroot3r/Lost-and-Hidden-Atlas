# November 20, 2026: New Mexico, a first scatter across the state (the state had 16 places, all but one round Lincoln
# County). Chosen with tools/choose.py --thinnest (nm). Spread from Colfax County in the north-east to Grant and Catron
# counties in the south-west: forts of the Santa Fe Trail and the Camino Real, the Salinas and Pecos mission ruins, three
# old adobe churches, the Las Vegas railroad hotels, a coal-camp cemetery and a silver camp.
# Sources read in this session: National Park Service pages (hours, directions, history, nps.gov/places), the Bureau of
# Land Management's Fort Craig page, National Register nomination forms (NPGallery "_text": Dawson Cemetery 92000249, Fort
# Bayard 02000726, Mogollon 87001541), Wikipedia (tools/wiki_raw.py), the San Miguel parish schedule, the UWC-USA visit
# page, the Plaza Hotel's own history page, New Mexico Magazine, KRWG, Atlas Obscura and the state tourism department.
from data_b import N
from data_ma import W
BATCH={'key':'nm_knxo','label':'New Mexico: forts, missions and old churches across the state','added':'2026-11-20 09:21'}

def NR(ref,label):
    return [label+' (National Register nomination)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/%s_text'%ref]
SAPU_HRS=['NPS: Salinas Pueblo Missions hours','https://www.nps.gov/sapu/planyourvisit/hours.htm']
SAPU_DIR=['NPS: Salinas Pueblo Missions directions','https://www.nps.gov/sapu/planyourvisit/directions.htm']
SAPU_ACC=('Salinas Pueblo Missions National Monument (National Park Service). The NPS hours page gives 9 a.m. to 5 p.m. daily all year for each unit and the Mountainair visitor centre, '
          'closed Thanksgiving, Christmas and New Year\'s Day, and says the park may shut in extreme weather; no camping. Fee not checked. ')
SAPU_HOURS='Daily 9 a.m. to 5 p.m. all year; closed Thanksgiving, Christmas and New Year\'s Day (NPS page)'
LV_DIR='Las Vegas is off I-25; the plaza is in the old town west of the Gallinas River.'

PLACES=[
N('fort-union-nm','Fort Union','Watrous','nm','fort','ruins',35.90566,-105.01051,'site','open','walk','forts','1851–1891',
  'An army post founded in 1851 where the Mountain and Cimarron branches of the Santa Fe Trail met, and for forty years the main supply depot of the Southwest. A star-shaped earthwork, the second fort, was thrown up against the Confederate advance of 1862; the third fort was begun in 1863. The railroad replaced the trail in 1879 and the post was abandoned in 1891.',
  'The remains of the second and third forts along a self-guiding trail; the ruins of the ordnance depot and the site of the first fort across the valley to the west; and Santa Fe Trail ruts seen from the fort and its road (Wikipedia). A visitor centre has a museum and a film. Brick not checked.',
  'The biggest adobe ruin of the Santa Fe Trail, eight miles off the interstate.',
  'Fort Union National Monument (National Park Service), 3115 NM 161, Watrous: I-25 exit 366, then 8 miles on NM 161 (NPS directions). No fuel or food nearby; the nearest are in Las Vegas and Wagon Mound. Admission free per Wikipedia (fee not checked on the NPS page). Trails are for walking only; no bicycles on the grounds.',
  [['NPS: Fort Union hours','https://www.nps.gov/foun/planyourvisit/hours.htm'],['NPS: Fort Union directions','https://www.nps.gov/foun/planyourvisit/directions.htm'],W('Fort Union National Monument')],
  th=[35.90479,-105.01080],thn='Fort Union visitor centre lot',brick='?',hours="Daily 8 a.m. to 4 p.m.; closed Thanksgiving, Christmas and New Year's Day (NPS page)"),

N('pecos-mission-church-nm','Pecos Mission Church (Nuestra Señora de los Ángeles de Porciúncula)','Pecos','nm','worship','ruins',35.55001,-105.68921,'site','open','walk','','1717 (earlier church c. 1625)',
  'A Franciscan mission beside Pecos Pueblo. The first church, of 1617–1621, stood too far from the pueblo; a larger one was built 600 feet south of the pueblo from about 1625, with Pecos people as unpaid labour. It was burned in the Pueblo Revolt of 1680, and the smaller church whose walls stand today was finished in 1717 on its rubble (NPS).',
  'The adobe walls of the 1717 church with the walls of the convento in front of them, on the 1.25-mile self-guiding trail from the visitor centre that also passes the ruins of the pueblo (NPS, Wikipedia). A kiva built in front of the church during the revolt is part of the story told on the trail.',
  'A church built on the rubble of one burned in the Pueblo Revolt.',
  'Pecos National Historical Park (National Park Service), about 17 miles east of Santa Fe and just south of the village of Pecos on NM 63 (Wikipedia). No entrance fee; no camping in the park (NPS hours page). The ruins are part of a pueblo that is sacred ground to its descendants: keep to the trail.',
  [['NPS: Pecos Mission Church','https://www.nps.gov/places/pecos-mission-church.htm'],['NPS: Pecos hours','https://www.nps.gov/peco/planyourvisit/hours.htm'],W('Pecos National Historical Park')],
  th=[35.54978,-105.68600],thn='Pecos visitor centre lot',brick='?',hours='Park daily 8 a.m. to 4:30 p.m.; visitor centre 9 a.m. to 4 p.m. Nov.–May, 8:30 a.m. to 4 p.m. May–Oct.; closed Thanksgiving, Christmas, New Year (NPS)'),

N('quarai-mission-nm','Quarai Mission (La Purísima Concepción de Quarai)','Punta de Agua','nm','worship','ruins',34.5960,-106.2955,'site','open','walk','','1627–1678',
  'A Franciscan mission built for the Tiwa pueblo of Quarai: the church of La Purísima Concepción went up from 1627 to 1632 (NPS). Disease, drought, famine and Apache raids emptied the pueblo by 1678. Settlers of the Lucero family returned in the early 1800s and used the roofed church for services until an Apache raid of 1830 drove them out; the roof then fell. The state bought and stabilized the ruins in the 1930s.',
  'The tall walls of the mission church, probably one of the largest wall-and-beam buildings in North America, with the convento and its square kiva, among the mounds of the pueblo (Wikipedia, NPS). A visitor centre and a half-mile trail.',
  'Church walls standing alone on the plain since the 1670s.',
  SAPU_ACC+'Quarai is 8 miles north of Mountainair on NM 55 and 1 mile west (NPS directions).',
  [['NPS: Quarai','https://www.nps.gov/sapu/learn/historyculture/quarai.htm'],SAPU_HRS,SAPU_DIR,W('Quarai')],
  th=[34.59515,-106.29768],thn='Quarai visitor centre lot',brick='?',hours=SAPU_HOURS),

N('abo-mission-nm','Abó Mission (San Gregorio de Abó)','Abó','nm','worship','ruins',34.4503,-106.3752,'site','open','walk','','1623–1673',
  'Fray Francisco Fonte came to the Tompiro pueblo of Abó in 1622, and a first, smaller church and convento were built from 1623 to 1628, the convento holding a round kiva. From 1640 Fray Francisco Acevedo built a larger church round the first, finished by 1658. Disease, drought, famine and Apache raids emptied Abó in 1673; sheep herders tried to return in 1815, and settlers came back for good in 1865 (NPS).',
  'The walls of the larger church and its convento, with the round kiva in the convento court, among unexcavated pueblo mounds; the remains of the 19th-century settlers\' buildings lie south and east of the mission (NPS). Interpretive trail from the lot.',
  'A church built round a smaller church so Mass never stopped.',
  SAPU_ACC+'Abó is 9 miles west of Mountainair on US 60 and half a mile north on NM 513 (NPS directions).',
  [['NPS: Abó','https://www.nps.gov/sapu/learn/historyculture/abo.htm'],['NPS: Mission San Gregorio de Abó','https://www.nps.gov/subjects/travelspanishmissions/mission-san-gregorio-de-abo.htm'],SAPU_HRS,SAPU_DIR],
  th=[34.44987,-106.37488],thn='Abó lot',brick='?',hours=SAPU_HOURS),

N('gran-quivira-mission-nm','Gran Quivira: San Isidro and San Buenaventura churches','Gran Quivira','nm','worship','ruins',34.2597,-106.0923,'site','open','walk','','1629–1672',
  'The pueblo the Spanish called Las Humanas became a visita of Abó in 1629, when a first mission began in rooms of Mound 7. The church of San Isidro was finished in 1635. A resident friar came in 1659 and began the larger church of San Buenaventura, but disease, drought, famine and Apache raids emptied the pueblo by 1672 and the church was never finished (NPS, Wikipedia).',
  'The walls of the unfinished San Buenaventura church and what is left of San Isidro, beside Mound 7, a 226-room pueblo and the only one fully excavated here, on a half-mile trail from a small visitor centre (NPS, Wikipedia).',
  '',
  SAPU_ACC+'Gran Quivira is 26 miles south of Mountainair on NM 55 (NPS directions).',
  [['NPS: Gran Quivira','https://www.nps.gov/sapu/learn/historyculture/gran-quivira.htm'],SAPU_HRS,SAPU_DIR,W('Salinas Pueblo Missions National Monument')],
  th=[34.25884,-106.09395],thn='Gran Quivira visitor centre lot',brick='?',hours=SAPU_HOURS),

N('fort-craig-nm','Fort Craig','San Marcial','nm','fort','ruins',33.6348,-107.0122,'site','public','walk','forts','1853–1885',
  'An army post begun in 1853 on a bluff above the Rio Grande and the Camino Real, at the north end of the Jornada del Muerto, to replace the flood-prone Fort Conrad. Union troops marched from it to the Battle of Valverde in February 1862, a Confederate victory just to the north. It was abandoned in 1885 and sold in 1894; the land was given to the Archaeological Conservancy and passed to the Bureau of Land Management in 1981. Graves looted from its cemetery were reburied at Santa Fe National Cemetery in 2007.',
  'The ruins of the fort ("sun-bleached ruins", NPS) on a self-guided trail with signs, a 0.3-mile hardened loop and an overlook at its south-east end; a visitor centre with exhibits (BLM). Brick not checked.',
  'The fort the Union marched out of to lose the Battle of Valverde.',
  'Fort Craig Historic Site, owned and run by the Bureau of Land Management (Socorro Field Office). About 35 miles south of Socorro: from I-25 take the San Marcial exit (exit 124) or exit 115 from the south, then about 11 miles south on old Highway 1 and follow the signs. Gravel lot for about 50 cars, vault toilets, water, picnic shelters. No fee; day use only (BLM page).',
  [['BLM: Fort Craig Historic Site','https://www.blm.gov/visit/fort-craig-historic-site'],['NPS: Fort Craig Historic Site','https://www.nps.gov/places/fort-craig-historic-site.htm'],W('Fort Craig')],
  th=[33.63502,-107.01608],thn='Fort Craig lot',brick='?',hours='Trail and picnic area daily 8 a.m. to an hour before sunset (BLM page)'),

N('san-miguel-socorro-nm','San Miguel Church','Socorro','nm','worship','standing',34.0605,-106.8937,'exact','open','walk','','c. 1821 (mission c. 1627)',
  'The parish church of Socorro, built on the ruins of the mission of Nuestra Señora de Socorro of about 1627, which was destroyed in the Pueblo Revolt of 1680. The present church was most likely finished by 1821, when its first baptisms, burials and marriages were recorded. Manuel Armijo, the last Mexican governor of New Mexico, is buried here (Wikipedia).',
  'A piece of the adobe wall of the old mission church can be seen behind glass to the left of the altar (Wikipedia). Other interior fabric not checked. Active parish: Masses as listed.',
  '',
  'Active Catholic parish, 403 El Camino Real, a short walk north of the Socorro plaza. Service times from the parish\'s own schedule page; visiting outside services not checked. Parking not checked.',
  [['San Miguel parish: schedule','https://sdc.org/~smiguel/schedule.htm'],['NPS: Mission San Miguel de Socorro','https://www.nps.gov/subjects/travelspanishmissions/mission-san-miguel-de-socorro.htm'],W('San Miguel de Socorro')],
  brick='?',hours='Mass Sunday 8 and 10 a.m., Saturday 5 p.m.; weekdays Tue. 5:30 p.m., Wed. to Fri. 9 a.m. (parish page; the weekday church is not named)'),

N('fort-selden-nm','Fort Selden','Radium Springs','nm','fort','ruins',32.48419,-106.92064,'site','open','walk','forts','1865–1891',
  'An adobe army post set up in 1865 at Paraje de Robledo, an old camp of the Camino Real on the Rio Grande where travellers left the river for the Jornada del Muerto. Its garrisons included California volunteers and the 125th U.S. Colored Infantry. Captain Arthur MacArthur commanded it in 1884, with his son Douglas, then four. It was abandoned in 1891 and became a state monument in 1974 (Wikipedia).',
  'Crumbling adobe walls and earth mounds of 15 to 20 buildings round a central parade ground, some walls up to 10 feet high on stone foundations (NPS), on an interpretive trail, with a visitor centre of exhibits on frontier and military life.',
  'Where Douglas MacArthur spent part of his boyhood.',
  'Fort Selden Historic Site, a state historic site of New Mexico Historic Sites (Department of Cultural Affairs), at Radium Springs, 13 miles north of Las Cruces (NPS). Leasburg Dam State Park is next door. Hours and admission not checked: the state\'s page (nmhistoricsites.org) gave no hours to the page tool. The lot on Fort Selden Road is mapped in OpenStreetMap.',
  [['NPS: Fort Selden Historic Site','https://www.nps.gov/articles/000/new-mexico-fort-selden-historic-site.htm'],['New Mexico Historic Sites: Fort Selden','https://nmhistoricsites.org/fort-selden'],W('Fort Selden')],
  th=[32.48366,-106.91904],thn='Fort Selden Road lot',brick='no',hours='?'),

N('mogollon-nm','Mogollon','Mogollon','nm','town','standing',33.39792,-108.79640,'area','view','drive','','1889–1942',
  'A gold and silver camp in Silver Creek Canyon whose first cabin went up in 1889; the Little Fannie mine was the main employer, and in 1914 the district produced about 40 per cent of New Mexico\'s precious metals. Fires struck in 1904, 1910, 1915 and 1942, and the town rebuilt each time in more stone and adobe. The Fannie mill, the only local mill, closed with the Fannie mines in 1942 (Wikipedia).',
  'One street of buildings winding up the canyon, crossing and recrossing Silver Creek: commercial buildings clustered at the lower, western end, six of adobe or stone, with central doors between display windows, and one wood-frame church. Of 45 buildings put up between 1889 and 1942 only five had been much altered when the district was listed in 1987 (nomination). A saloon and store were built as a film set. The Register also lists the Fannie Hill mill above the town (not read).',
  'A silver camp at the end of a mountain road that is shut in winter.',
  'Most of the town is private: the 1987 nomination lists many owners. Look from NM 159, the public road through town. NM 159 leaves US 180 between Glenwood and Alma and winds up to Mogollon; east of the town it becomes the rough, unpaved Bursum Road, closed in winter (Wikipedia, "New Mexico State Road 159"). The town has a few homes and small businesses. Parking not checked.',
  [NR('87001541','Mogollon Historic District'),W('Mogollon, New Mexico'),W('New Mexico State Road 159')],
  brick='?'),

N('montezuma-castle-nm','Montezuma Castle (Montezuma Hotel)','Montezuma','nm','hotel','standing',35.6558,-105.2809,'exact','view','drive','hotels','1886',
  'A 400-room Queen Anne hotel built in 1886 by the Atchison, Topeka & Santa Fe Railroad at the Las Vegas Hot Springs, the third on the site: the first two, of 1881 and 1885, both burned. It closed as a hotel in 1903 and was later a YMCA property, a Baptist college and from 1937 to 1972 a seminary for Mexican Jesuits. Armand Hammer bought it in 1981 for the United World College; it was on the National Trust\'s endangered list in 1997, and the college restored it in 2000–2001 for over $10.5 million (Wikipedia).',
  'Now the college\'s Davis International Center, with dining hall, rooms and classrooms (Wikipedia). Seen from Hot Springs Boulevard (State Road 65), which the college\'s directions say passes it. Interior not open to the public.',
  'A railroad castle at a hot spring, now a school for students from 80 countries.',
  'Owned by UWC-USA (United World College). The college\'s visit page says the campus is closed to the public except for announced events and tours for prospective students; the Dwan Light Sanctuary on campus is open daily sunrise to sunset, with a key from the Welcome Center. Look at the castle from State Road 65, about 5 miles north-west of Las Vegas. Parking not checked.',
  [['UWC-USA: visit','https://www.uwc-usa.org/about/our-location/visit/'],W('Montezuma Castle (hotel)'),NR('74001203','Montezuma Hotel Complex')],
  brick='?'),

N('plaza-hotel-las-vegas-nm','Plaza Hotel','Las Vegas','nm','hotel','standing',35.5931,-105.2276,'exact','open','walk','hotels','1882',
  'Built in 1882 by businessmen led by Don Benigno Romero on the north side of the old Las Vegas plaza, three years after the railroad came, and billed as the finest hotel in the territory. Theodore Roosevelt\'s Rough Riders held their first reunion here in 1899. A film maker leased it from 1913 to 1915 as the Hotel Romaine, and it was restored in 1982; Allan Affeldt bought it with the Ilfeld building next door in 2014 (Wikipedia, hotel\'s history page).',
  'A three-storey brick building with an Italianate front; traces of the name "Hotel Romaine" can still be seen on the brick (Wikipedia), and faint lettering on the Hot Springs Road wall (hotel). The dining room and saloon were restored in 2014–2015. A working hotel: the lobby, restaurant and bar are its public rooms. A Wikimedia Commons photograph of the front shows red brick with painted cornices and window heads.',
  'Where the Rough Riders held their first reunion.',
  'A working hotel, 230 Plaza Street, on the old town plaza. '+LV_DIR+' Hours of the restaurant and bar not checked. Street parking round the plaza not checked.',
  [['Plaza Hotel: history','https://plazahotellvnm.com/history/'],W('Plaza Hotel (Las Vegas, New Mexico)')],
  brick='yes',hours='?'),

N('ranchos-de-taos-church-nm','San Francisco de Asís Church','Ranchos de Taos','nm','worship','standing',36.3584,-105.6084,'exact','open','walk','','1772–1816',
  'A Spanish colonial parish church built between 1772 and 1816 as the centre of a fortified plaza that sheltered the village from Comanche raids. It was restored in 1850, 1916, 1933 and 1967. Georgia O\'Keeffe painted it and Ansel Adams photographed it, and it is a National Historic Landmark (Wikipedia, NPS).',
  'Massive sculpted adobe buttresses, with beehive-curved ones at the ends of the transepts, two front bell towers, an adobe roof on vigas set in double corbels, and an adobe-walled yard on the south side. Inside, the altar has original Spanish woodwork and religious images, and the nave has room for visitors as well as worshippers (NPS). Every June parishioners and visitors spend two weeks re-mudding the walls.',
  'The church O\'Keeffe painted from behind.',
  'Active Catholic parish of the Archdiocese of Santa Fe, on St. Francis Plaza off NM 68 south of Taos. The NPS describes the nave as open to worshippers and visitors; Mass times and visiting hours not checked on a parish page (none found). Parking on the plaza not checked.',
  [['NPS: San Francisco de Assisi Mission Church','https://home.nps.gov/places/san-francisco-de-assisi-mission-church-ranchos-de-taos-new-mexico.htm'],W('San Francisco de Asís Mission Church')],
  brick='no',hours='?'),

N('las-trampas-church-nm','San José de Gracia Church','Las Trampas','nm','worship','standing',36.1312,-105.7582,'exact','view','walk','','1760–1776',
  'Built between 1760 and 1776 on the north side of the plaza of Las Trampas, a village on the High Road between Santa Fe and Taos that had 63 families when the church was finished. The village\'s isolation kept it almost unaltered; the roof has been replaced several times, in 1932 by the Society for the Preservation of New Mexico Mission Churches under John Gaw Meem (Wikipedia, NPS).',
  'Mud-plastered adobe walls 34 feet high on a cross plan, a roof on vigas with shaped corbels, and a clerestory window across the nave that lights the altar, otherwise lit by candles. Inside: wide-plank floors, a ceiling painted with 18th- and 19th-century designs and works by 18th- and 19th-century santeros (Wikipedia, NPS). When the interior is open not checked.',
  'A church still lit by candles and one window in the roof.',
  'Catholic church of the village of Las Trampas, on NM 76 (the High Road). Look from the plaza; no source read says when the church is open, so it is marked view-only. Parking not checked.',
  [['NPS: San José de Gracia Church','https://www.nps.gov/places/san-jos%C3%A9-de-gracia-church-las-trampas-new-mexico.htm'],W('San José de Gracia Church')],
  brick='no'),

N('dawson-cemetery-nm','Dawson Cemetery','Dawson','nm','burial','standing',36.6553,-104.7678,'site','view','drive','cemeteries','1913',
  'The cemetery of Dawson, a Phelps Dodge company coal town from 1901 until the mine closed in 1950, when the company sold the buildings to be carried away. About 600 marked graves; the largest section, inside an iron-pipe fence, holds miners killed in the explosions of 1913 and 1923, many of them immigrants from southern and eastern Europe and Mexico. Phelps Dodge restored the miners\' section in 1990 (nomination, state tourism department).',
  'Rows of white-painted iron crosses facing west toward the road, in three fenced sections at the foot of a mountain about three-quarters of a mile south-east of the old townsite (nomination, Wikipedia). Little else of the town is left.',
  'Hundreds of white iron crosses for two mine explosions.',
  'Take US 64 about 12 miles east of Cimarron, then north on A38 at the striped sign for about 5 miles; after it crosses the railroad tracks a second time, a dirt road on the right leads about 1,000 feet to the cemetery (Wikipedia). The state tourism department lists it as a ghost-town site to visit. Who owns the ground and the road was not checked: keep to the road and the cemetery, and do not enter the old townsite. Parking not checked.',
  [NR('92000249','Dawson Cemetery'),['New Mexico Tourism: Dawson','https://newmexico.org/places-to-visit/ghost-towns/dawson'],W('Dawson Cemetery'),W('Dawson, New Mexico')],
  brick='?'),

N('fort-bayard-nm','Fort Bayard','Santa Clara','nm','fort','standing',32.7955,-108.1510,'area','open','walk','forts','',
  'An army post founded after the Civil War, then the Army\'s first major tuberculosis hospital and later Veterans Administration Hospital No. 55; the National Register district of 2002 counts 70 contributing buildings round the old parade ground, state-owned. In 2014 the state put the old fort up for sale, saying repairs would cost about $30 million, much of it asbestos removal; a new hospital and a national cemetery stand nearby (nomination, KRWG).',
  'Officers\' houses with white porches and red roofs facing the parade ground, with a statue of Corporal Clinton Greaves, Medal of Honor 1879, in its centre (New Mexico Magazine). The Fort Bayard Historic Preservation Society runs a museum in the Commanding Doctor\'s house on the west side of the parade ground (Atlas Obscura, KRWG). New Mexico Magazine describes the buildings as still and the site as in limbo. Interior of the houses not checked.',
  'The Army\'s first tuberculosis hospital, now a parade ground of empty houses.',
  'State land (New Mexico), off US 180 east of Silver City at Santa Clara. Atlas Obscura gives guided tours on Saturdays from 10 a.m. from the museum, and a 2014 KRWG story says the museum opens on Saturdays; the society\'s own page was not found, so hours are not checked. Fort Bayard National Cemetery is just north-west. Pin is the parade ground. Parking not checked.',
  [NR('02000726','Fort Bayard Historic District'),['KRWG: Future unknown for Fort Bayard (2014)','https://www.krwg.org/regional/2014-03-14/future-unknown-for-fort-bayard'],['New Mexico Magazine: Fort Bayard','https://www.newmexicomagazine.org/blog/post/fort-bayard/'],['Atlas Obscura: Fort Bayard','https://www.atlasobscura.com/places/fort-bayard-historical-site']],
  conf='mixed',brick='?',hours='?'),
]

PIN_NOTES={
 'fort-union-nm':'Moved with pix.py onto the walled ruins east of the visitor centre, near the NPS GPS point (35.9073, -105.0122); the fort ruins spread north of it.',
 'pecos-mission-church-nm':'Moved with pix.py onto the red-walled church seen on the aerial, south of the pueblo; the OpenStreetMap convento point is about 90 m south of it.',
 'quarai-mission-nm':'OpenStreetMap Quarai unit point; checked on the aerial.',
 'abo-mission-nm':'OpenStreetMap "Mission of San Gregorio de Abó"; checked on the aerial.',
 'gran-quivira-mission-nm':'OpenStreetMap "San Buenaventura" ruin; checked on the aerial.',
 'fort-craig-nm':'OpenStreetMap historic=fort "Fort Craig"; checked on the aerial.',
 'san-miguel-socorro-nm':'OpenStreetMap church "San Miguel de Socorro", 403 El Camino Real; checked on the aerial.',
 'fort-selden-nm':'The Wikipedia coordinate fell in brush by the river about 1.3 km north; moved with pix.py onto the walled rectangle seen on the aerial beside the OpenStreetMap lot on Fort Selden Road, taken to be the fort (not confirmed by a mapped point).',
 'mogollon-nm':'OpenStreetMap hamlet point moved 54 m south onto the canyon street (pix.py); the town, not one building.',
 'montezuma-castle-nm':'OpenStreetMap historic=castle "Montezuma Castle"; checked on the aerial.',
 'plaza-hotel-las-vegas-nm':'OpenStreetMap "Historic Plaza Hotel", 230 Plaza Street; checked on the aerial.',
 'ranchos-de-taos-church-nm':'OpenStreetMap church on St. Francis Plaza; checked on the aerial.',
 'las-trampas-church-nm':'OpenStreetMap "San Jose de Gracia Catholic Church", NM 76; checked on the aerial.',
 'dawson-cemetery-nm':'OpenStreetMap cemetery "Dawson Cemetery", agrees with the Register point; checked on the aerial.',
 'fort-bayard-nm':'The parade ground, placed near the OpenStreetMap hamlet point; checked on the aerial.',
}
