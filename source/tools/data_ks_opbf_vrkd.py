# November 24, 2026: Overland Park and Stilwell, Johnson County, Kansas (fourth pass). The county's register lists were
# used by earlier batches; these four come from the Blackfeather Farm National Register form, a local history article,
# the National Park Service's page for the Santa Fe Trail campsite and a Clio entry for the old bank.
from data_b import N
from data_ma import W
BATCH={'key':'ks_opbf_vrkd','label':'Johnson County, Kansas (fourth pass)','added':'2026-11-24 20:49'}
PLACES=[
N('blackfeather-farm-stilwell-ks','Blackfeather Farm (Nelson Studebaker Riley Farm), Stilwell','Stilwell, Kansas','ks','landmark','standing',38.79789,-94.68045,'site','view','drive','','1928',
  'Nelson S. Riley, who ran the Midwest side of the Studebaker business, had this limestone farmhouse built in 1928 as a country retreat, in a Dutch Colonial Revival style with Craftsman touches. The land had earlier belonged to Shawnee families named Blackbob, whose name the farm keeps in the spelling Blackfeather. The Depression took it from Riley, a steel company used it for a fishing and shooting club from 1934, and the Richardson family bought it in 1947. It was listed on the National Register in 1996.',
  'The nomination form describes a house built into a rocky ridge above a branch of Wolf Creek, a gravel drive past a caretaker\'s bungalow, a barn and a chicken shed, a native-stone summer cottage and springhouse by a small lake, two conical stone huts over a spring and pump house, and in the woods the ruins of the dam and spillway of the original lake. Interior not checked.',
  '',
  'Private land on West 183rd Street, owned by a family; the form (1996) and a city-sourced history page say it has served as an event and horse venue, but no page read gives public hours or says visitors may walk the grounds. Treat as look-only from the public road unless the owners invite you; the pin is the street address.',
  [['National Register nomination form (NPGallery 96000918)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/96000918_text'],['Clio: Blackfeather Farm','https://theclio.com/entry/47569'],['Kansas Historical Society: Johnson County register listings','https://www.kansashistory.gov/natreg/natreg_listings/search/page:1/county:JO/records:all/submit:SEARCH']],
  conf='mixed',th=None,brick='no'),
N('graham-rogers-house-overland-park-ks','Graham Rogers House, Overland Park','Overland Park, Kansas','ks','landmark','standing',39.00614,-94.68507,'exact','view','drive','','c. 1840',
  'Graham Rogers (1818 to 1872), a Shawnee chief who had learned carpentry, built a double log cabin and farm here around 1840. When he moved with his tribe to Indian Territory in 1868, the farm went to Henry Coppock, who called it Oak Park Farm and sold it in 1880 to George Milburn. A local historian writes that the log cabin survives under a white frame covering. The Kansas State Register lists the house (1988) as Greek Revival; that style label and the log core are not reconciled in the sources read.',
  'A private house seen from the street: a white frame house, with the log cabin reported to be inside it. Interior not checked.',
  '',
  'Private home on Mackey Street (owned by a couple since 1987, according to the article). Look from the street only; no public hours. The pin is the house, from an OpenStreetMap address match.',
  [['Martin City Telegraph: History of the Rogers House, Part II','https://martincitytelegraph.com/history-of-the-rogers-house-part-ii-the-coppocks-and-milburns'],['Kansas Historical Society: Johnson County register listings','https://www.kansashistory.gov/natreg/natreg_listings/search/page:4/county:JO/records:all/submit:SEARCH']],
  conf='mixed',brick='no'),
N('overland-park-state-bank-building-ks','Overland Park State Bank Building (1910s), Overland Park','Overland Park, Kansas','ks','civic','standing',38.98378,-94.67130,'site','view','drive','','1910–1911',
  'The Overland Park State Bank opened on March 1, 1910 in the north room of the Strang Line depot and moved the next year into this building at the southeast corner of 80th Street and Overland Park Drive. It served the town for about 80 years until UMB Bank took it over. The Overland Park Landmark Commission named it a Landmark Building in 2016.',
  'Two markers, one from the Overland Park Historical Society and one from the Landmark Commission, stand on the building, which houses a hair salon. Interior not checked.',
  '',
  'Private business on the old downtown street; look from the sidewalk, free street parking nearby. The pin is the Clio street address (7341 80th Street), geocoded.',
  [['Clio: The Overland Park State Bank (1910)','https://theclio.com/entry/188909']],
  brick='?'),
N('sapling-grove-park-overland-park-ks','Sapling Grove (Santa Fe Trail campsite), Overland Park','Overland Park, Kansas','ks','landmark','marker',38.97978,-94.69679,'site','public','drive','','1820s–1860s',
  'From the late 1820s Sapling Grove, at the head of Turkey Creek, was a camp on the Santa Fe Trail. George Sibley listed it when he surveyed the trail in 1825 to 1827, and in 1841 the Bidwell-Bartleson party, the first emigrant wagon train of families to head west on the trail, met here. Travellers camped on the hill where Comanche Elementary School now stands. The 21-acre park next to it was Comanche Park until 2003, when the city renamed it for the campsite.',
  'A city park with interpretive signs, a picnic shelter and tables. Nothing of the camp remains on the ground; the signs and the park are what to see.',
  '',
  'City park managed by Overland Park Parks and Recreation at 8210 Grant Avenue (at 83rd Street). Free; park hours not read.',
  [['National Park Service: Sapling Grove, Overland Park','https://www.nps.gov/places/sapling-grove-overland-park.htm']],
  brick='?'),
]
PIN_NOTES={
'blackfeather-farm-stilwell-ks':'ArcGIS address match for 8140 West 183rd Street, the address on the National Register form. On the 2024 aerial the pin falls among the farm\'s barn and sheds; the house itself is in the trees on the ridge and was not picked out, so the pin marks the farm, not the house.',
'graham-rogers-house-overland-park-ks':'OpenStreetMap maps this address as the Graham Rogers House.',
'overland-park-state-bank-building-ks':'ArcGIS address match for the Clio address, 7341 West 80th Street, at the corner the marker text names.',
'sapling-grove-park-overland-park-ks':'ArcGIS address match for 8210 Grant Avenue, the address the National Park Service gives; OpenStreetMap puts the park about 20 m away.',
}
