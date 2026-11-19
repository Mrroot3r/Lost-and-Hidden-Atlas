# November 18, 2026: Staten Island (Richmond County, New York City), the first places in region nyc.
# Region nyc drawn at random by choose.py; Staten Island picked inside it as the borough with the most colonial survivors
# and ruins outside Manhattan's crowds.
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py), the National Park
# Service's Gateway pages (Fort Wadsworth, Staten Island FAQ), the Historic House Trust's house pages, Historic Richmond
# Town's visit page, Snug Harbor's visit page, NYS DEC's Mount Loretto Unique Area page, HMdb.org marker 155238, and news
# and history write-ups on the Farm Colony (6sqft, JLC Online) and the boat graveyard (Forgotten New York, Freshkills Park).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
HM=lambda n,t: ['HMdb: '+t,'https://www.hmdb.org/m.asp?m=%d'%n]
HHT=lambda slug,t: ['Historic House Trust: '+t,'https://historichousetrust.org/houses/%s/'%slug]
NPSFW=L('NPS: Fort Wadsworth (hours, visitor center)','https://www.nps.gov/gate/learn/historyculture/fort-wadsworth.htm')
NPSFAQ=L('NPS: Staten Island FAQ (tours)','https://www.nps.gov/gate/faq-staten-island.htm')
HRT=L('Historic Richmond Town: hours and admission','https://www.historicrichmondtown.org/visit')
HRTACC=('Historic Richmond Town (Staten Island Historical Society, on city land) gives its public hours as Wednesday to Sunday, 11 am to 4 pm, '
        'with guided tours (Two Centuries Tour Wednesday to Friday at 2, weekends at 12 and 2) included in general admission, '
        'which is sold at the Village Store in the Third County Courthouse; admission is free on Thursdays 2 to 4 pm from May to December, '
        'and the village is closed the first two weeks of January (its visit page, read November 18, 2026). ')

BATCH={'key':'nyc_opzz','label':'Staten Island, New York City','added':'2026-11-18 15:48'}

PLACES=[
N('conference-house-tottenville','Conference House (Billop House)','Tottenville','nyc','landmark','standing',40.50313,-74.25322,'exact','open','walk','','c. 1680–',
  'Christopher Billopp, a Royal Navy captain granted the southern tip of Staten Island, built this two-storey fieldstone manor house around 1680; a map shows a building on the site before 1680. On September 11, 1776 his grandson hosted the Staten Island Peace Conference here, the failed attempt to end the Revolutionary War quickly. The house opened as a museum in 1927. The ground round it, Burial Ridge at Ward\'s Point, is the largest pre-European site in New York City.',
  'The fieldstone house with high gabled end walls that hold the fireplaces and chimney stacks; inside, two parlours off a central hall on the main floor and two bedchambers above (Historic House Trust). The Conference House Association restored the roof, the stairs to the basement, the second floor and the old well. Open inside on weekend afternoons (below). The park runs down to Raritan Bay at the southern tip of New York State.',
  'Where the British offered the Americans a way out in 1776, at the southern tip of New York.',
  'Conference House Park, New York City Parks; the house is run by the Conference House Association. The Historic House Trust gives its hours as Saturday and Sunday, 12 to 4 pm. The mapped lot on the park greenway is about 200 m east of the house.',
  [W('Conference House'),HHT('conference-house','Conference House')],th=[40.50226,-74.25131],thn='Conference House Park lot (greenway)',brick='no'),

N('voorlezers-house-richmond-town','Voorlezer\'s House, Historic Richmond Town','Richmondtown','nyc','civic','standing',40.57142,-74.1475,'exact','open','walk','','1760s (traditionally before 1696)',
  'A Dutch-style clapboard house long held to be the oldest schoolhouse in the United States, built for the voorlezer, the lay reader who led services and taught school in Dutch settlements. It was traditionally dated before 1696, but Wikipedia says it was more likely built in the 1760s by Jacob Rezeau, whose family owned the land from 1705; the date is not settled. Near demolition by 1936, it was bought by the museum in 1939, restored, and opened in 1942; it became a National Historic Landmark in 1961.',
  'Foundation walls of undressed fieldstone laid in mud and mortar, a massive stone-and-brick chimney at the north-east end, white pine floors of wide boards, a large first-floor room for church services and the upstairs room believed to have been the school, with an extra set of floor beams to carry a crowd. The leaded casement windows were put in at the second restoration (reopened 1985) to match a house of about 1696. One of some thirty old buildings in Historic Richmond Town; the Third County Courthouse (the visitor entrance) and St. Andrew\'s Church are a short walk.',
  'The schoolhouse that was too old by about seventy years.',
  HRTACC+'The Visitor Parking lot off Clarke Avenue is about 250 m south-east.',
  [W("Voorlezer's House"),HRT],conf='mixed',th=[40.57048,-74.14474],thn='Historic Richmond Town visitor parking, Clarke Avenue',brick='?'),

N('st-andrews-church-richmondtown','Church of St. Andrew, Richmondtown','Richmondtown','nyc','worship','standing',40.57286,-74.14736,'exact','view','walk','','1708–',
  'An Episcopal congregation founded in 1708; its first church went up in 1708 to 1712 and was enlarged in 1770. The British used it as a hospital in the Revolution. Fires in 1867 and 1872 badly damaged it, and it was rebuilt about 1872 in Gothic style; Burch Hall was added in 1924 to match. The 1818 rectory across the road is listed separately as the Moore-McMillen House.',
  'A fieldstone Gothic church with red brick trim on its stopped, chamfered edges, on the north side of Richmondtown at Arthur Kill and Old Mill Roads. The churchyard holds the graves of old Staten Island families, the Woods among them, and a large mausoleum of the Johnston family. Interior not checked.',
  'A 1708 parish that served as a British hospital, rebuilt after two fires.',
  'An active parish church; the churchyard and outside are seen from Arthur Kill Road and Old Mill Road. When the church is open to visitors was not checked. Park at Historic Richmond Town\'s visitor lot off Clarke Avenue, about 400 m south-east.',
  [W("St. Andrew's Church (Staten Island)")],th=[40.57048,-74.14474],thn='Historic Richmond Town visitor parking, Clarke Avenue',brick='some'),

N('billiou-stillwell-perine-house','Billiou–Stillwell–Perine House','Dongan Hills','nyc','landmark','standing',40.59343,-74.1,'exact','view','drive','','c. 1662–1830',
  'The oldest standing building on Staten Island. Pierre Billiou, a Huguenot who reached New Amsterdam in 1661 and founded Oude Dorp (Old Town), raised its stone section around 1662. His son-in-law Thomas Stillwell enlarged it about 1680, and later owners added to it until 1830; the Perine family held it from 1758 to 1913. The Staten Island Antiquarian Society bought it in 1915, and it passed to the Staten Island Historical Society in 1922.',
  'A Dutch Colonial house with a shingled sloping roof; inside, a high jambless fireplace with a large stone hearth and a ceiling of very large beams. The roof was restored in 2013.',
  'Staten Island\'s oldest building, grown in five stages over 170 years.',
  'Owned by Historic Richmond Town (Staten Island Historical Society), which opens it occasionally on a limited schedule or by appointment (Wikipedia); the schedule was not checked on the society\'s own pages. Otherwise seen from the street. No public lot was found nearby; street parking not checked.',
  [W('Billiou–Stillwell–Perine House'),HRT],brick='?'),

N('battery-weed-fort-wadsworth','Battery Weed (Fort Richmond), Fort Wadsworth','Fort Wadsworth','nyc','fort','standing',40.60528,-74.05472,'exact','public','walk','forts','1806–',
  'A four-tier masonry fort at the water\'s edge of the Narrows, built 1845 to 1861 under the federal Third System on the site of New York State\'s red sandstone Fort Richmond of 1806 to 1808. Only Castle Williams on Governors Island and Fort Point in San Francisco share its four-tier plan. A light on its top was made obsolete when the Verrazzano–Narrows Bridge opened in 1965. Fort Wadsworth, which held it, was claimed as the longest continuously garrisoned post in the country until it closed in 1994; it is now part of Gateway National Recreation Area.',
  'The tiers of gun openings facing the Narrows under the bridge, seen from the overlook and the shore road. The inside is open only on ranger-led tours (Wikipedia; check the park\'s events calendar). The visitor center has exhibits on the fort.',
  'A four-storey Civil War-era gun fort sitting under the Verrazzano Bridge.',
  'Gateway National Recreation Area (National Park Service). Fort Wadsworth is open daily 6 am to 9 pm; the visitor center Saturday and Sunday 10 am to 4 pm (NPS page read November 18, 2026). The S51 bus from the St. George ferry terminal stops at the Bay Street entrance. Mapped lot on Tompkins Street, about 150 m south-west.',
  [W('Battery Weed'),W('Fort Wadsworth'),NPSFW,NPSFAQ],th=[40.60432,-74.05585],thn='Fort Wadsworth lot, Tompkins Street',brick='?'),

N('fort-tompkins-staten-island','Fort Tompkins, Fort Wadsworth','Fort Wadsworth','nyc','fort','standing',40.60503,-74.05652,'site','public','walk','forts','1847–1861',
  'The landward fort on Signal Hill that guarded the shore batteries below from attack overland. A Dutch blockhouse stood here in the 1600s, and the hill was the Patriot (then British) Flagstaff Fort in the Revolution; New York State built a red sandstone pentagon here in 1806 to 1808. The present fort was built 1847 to 1861 and served until newer defences replaced it about 1898. It is the last of four forts in the state named for Daniel D. Tompkins.',
  'The fort\'s walls on the hill above Battery Weed. The National Park Service offers tours of Fort Tompkins through the season, free (its Staten Island FAQ; dates on its events calendar). Interior beyond the tours not checked.',
  'The fort built to defend the fort.',
  'Gateway National Recreation Area (National Park Service); Fort Wadsworth is open daily 6 am to 9 pm (NPS page read November 18, 2026). Park on Tompkins Street or Headquarters Road.',
  [W('Fort Tompkins (Staten Island)'),NPSFW,NPSFAQ],th=[40.60391,-74.05706],thn='Fort Wadsworth lot, Headquarters Road',brick='?'),

N('snug-harbor-temple-row','Sailors\' Snug Harbor: Temple Row and Building C','Livingston','nyc','inst','standing',40.64457,-74.10214,'exact','public','walk','','1833–',
  'A retirement home for sailors paid for by Robert Richard Randall, who left his estate to it at his death in 1801. Building C, the first, opened in 1833 for 37 men; the complex grew through the 1800s to five joined Greek Revival buildings (Temple Row, A to E), a chapel, a music hall and infirmary. The institution moved to North Carolina after a long preservation fight, and since 1976 the Snug Harbor Cultural Center has run the campus. Buildings A to E and the chapel were among New York City\'s first twenty landmarks (1965).',
  'Temple Row\'s colonnaded fronts along Richmond Terrace, joined by brick passageways ("hyphens"); the rear walls are brick. Building C\'s main hall has ash floors, a vaulted ceiling shaped like an upturned keel, a domed skylight with a mural and sun-and-moon clerestory windows; the chapel (now Veterans Memorial Hall) keeps stained glass of 1883. Also the 1917 Beaux-Arts Great Hall, a north gatehouse with brick corbels, and a marble monument to Randall.',
  'A retired sailors\' home built like a row of Greek temples.',
  'Snug Harbor Cultural Center and Botanical Garden, on city parkland. The grounds and gardens are free and open every day, dawn to dusk; after dark all gates are locked except the West Gate on Snug Harbor Road, with earlier closing October to March (its visit page, read November 18, 2026). Indoor galleries and gardens have their own hours and fees, not checked. The visit page warns its lots fill on summer weekends and asks visitors to come by transit.',
  [W('Snug Harbor'),L('Snug Harbor: hours and admissions','https://snug-harbor.org/visit/')],brick='?'),

N('nyc-farm-colony-ruins','New York City Farm Colony ruins','Willowbrook','nyc','inst','ruins',40.59398,-74.13827,'site','view','walk','','1829–1975',
  'Richmond County bought this farm in 1829 for its poor farm; the city took it over in 1898 as the New York City Farm Colony, a poorhouse where the able residents worked the land, run with Seaview Hospital across Brielle Avenue from 1915. It closed in 1975 and its Dutch Revival buildings fell into deep ruin, overgrown and covered in graffiti. With Seaview it is a city historic district (1985) and on the National Register. In 2016 the city approved "Landmark Colony", a $91 million plan for 344 homes for over-55s that would rehabilitate five buildings, take down five more and reuse their stone, keep one dormitory as a stabilized ruin, and open 17 acres and the old roads to the public. How far that work has gone was not checked.',
  'The masonry shells of the old buildings among trees, seen from Brielle Avenue and the edge of the Greenbelt. Part of the colony land (about 25 acres) was handed to the Greenbelt as parkland in the 1980s; baseball fields were built on another part in 1993 and 2001.',
  'The city poorhouse left to the woods for forty years.',
  'The ruined buildings are city property set aside for the Landmark Colony development and are closed; do not enter. Look from Brielle Avenue or from the Greenbelt parkland beside it (NYC Parks). No public lot was found by the ruins; parking not checked.',
  [W('New York City Farm Colony'),W('Seaview Hospital'),L('6sqft: New York City Farm Colony','https://www.6sqft.com/place/new-york-city-farm-colony/'),L('JLC Online: Historic Staten Island ruins slated for redevelopment','https://www.jlconline.com/coastal-contractor-news/historic-staten-island-ruins-slated-for-redevelopment_o/')],conf='mixed',brick='?'),

N('staten-island-boat-graveyard','Staten Island boat graveyard (Witte Marine)','Rossville','nyc','water','ruins',40.55588,-74.21667,'site','view','drive','','1930s–',
  'A marine scrapyard on the Arthur Kill where old tugs, ferries and cargo ships were left in the mud to be stripped for parts; its official name since 2014 is the Donjon Iron and Metal Scrap Processing Facility. Wikipedia says John J. Witte founded it in the 1930s; Forgotten New York says Arthur Witte Jr. in the 1950s, and Freshkills Park says Witte Marine began buying boats after the Second World War. It once held about 400 hulks and now about 100, among them the FDNY fireboat Abram S. Hewitt, command post at the 1904 General Slocum disaster.',
  'Rusting hulls in the shallows of the Arthur Kill off Arthur Kill Road near Rossville Avenue. Classic Harbor Lines has run boat tours past it (Freshkills Park).',
  'An accidental museum of New York harbour boats, rusting in the mud.',
  'A working private scrapyard, posted No Trespassing: do not enter. Seen from the water on a harbour boat tour or, partly, from Arthur Kill Road; how much shows from the public road was not checked. No public lot; the mapped lots nearby are private.',
  [W('Staten Island boat graveyard'),L('Forgotten New York: Ship graveyard, Rossville','https://forgotten-ny.com/?p=19995'),L('Freshkills Park: abandoned ship graveyard','https://freshkillspark.org/blog/farther-afield/from-behind-the-mounds-abandoned-ship-graveyard-in-our-backyard')],conf='mixed',brick='no'),

N('swinburne-island-quarantine','Swinburne Island quarantine station','Lower New York Bay','nyc','inst','ruins',40.56606,-74.05018,'site','view','boat','','1870–',
  'A man-made island in Lower New York Bay, built from dredged sand from 1860 and named for the physician John Swinburne, who made it a quarantine hospital in 1870. Immigrants arriving sick with contagious disease were held here, while those without symptoms waited on Hoffman Island to the north. The Merchant Marine trained on both islands from 1938 through the Second World War. The city deeded them to the National Park Service in 1972.',
  'Remnants of the wartime Quonset huts were still on Swinburne in 2017; Hoffman Island has old dock remains, foundations and a brick chimney, likely of the crematorium, in dense growth. Harbour seals and grey seals have hauled out on Swinburne since the 2000s.',
  'The island where New York kept its sick immigrants.',
  'Gateway National Recreation Area (National Park Service). Both islands are closed to the public as bird and wildlife sanctuaries; landing is not allowed. Seen at a distance from the Staten Island shore (Midland Beach, about 2.5 km away, measured on the map) or from a boat.',
  [W('Swinburne Island'),W('Hoffman Island')],brick='?'),

N('alice-austen-house','Alice Austen House (Clear Comfort)','Rosebank','nyc','landmark','standing',40.61492,-74.06361,'exact','open','walk','','1690s–',
  'A one-room Dutch Colonial house built in the 1690s or early 1700s on the shore of the Narrows, enlarged through the 1800s and remodelled in 1844 by John Haggerty Austen, who named it Clear Comfort. His granddaughter, the photographer Alice Austen, lived here most of her life. The city bought it in 1975 and it opened as a museum in 1985; in 2021 it was the first New York site dedicated to a woman to be recognised by the LGBT historic sites project.',
  'The house and lawn on the water at 2 Hylan Boulevard looking at the Narrows and the bridge; inside, a museum of Austen\'s photographs with guided tours on the hour. What original fabric survives inside was not checked.',
  'A 1690s farmhouse turned Victorian cottage, home to a pioneering photographer.',
  'Owned by New York City Parks, run by the Friends of Alice Austen House. Open Tuesday to Friday 12 to 5 pm, Saturday and Sunday 11 am to 5 pm; closed Thanksgiving, the day after, and December 23 to January 2 (Historic House Trust page, read November 18, 2026). Admission not checked. Street parking.',
  [W('Alice Austen House'),HHT('alice-austen-house','Alice Austen House')],brick='?'),

N('seguine-mansion','Seguine Mansion','Prince\'s Bay','nyc','landmark','standing',40.51522,-74.19753,'exact','view','walk','','1838–',
  'Joseph H. Seguine, whose grandfather bought land on Lemon Creek in the 1780s, built this Greek Revival house in 1838 with a hay barn, carriage house and stables; he founded several companies, among them the Staten Island Railroad. The family lost it in 1868, bought it back in 1916 and kept it until 1981, when George Burke bought it in poor repair, restored it over five years, filled it with his collection and gave it to the city.',
  'The columned Greek Revival front above a sloping lawn that looks down to the bay, beside the stables of the equestrian center Burke set up. Inside: Burke\'s art and furnishings, seen on ranger-led tours when they run.',
  'A Greek Revival house saved by one man and his sixty gallons of paint.',
  'Owned by New York City Parks (Lemon Creek Park), a member of the Historic House Trust. The Trust says the mansion and gardens open for scheduled Urban Park Ranger tours in spring, summer and fall, but the same page (read November 18, 2026) marks it "temporarily closed to the public"; see it from outside. Mapped lot in Lemon Creek Park on Seguine Avenue, about 350 m south.',
  [W('Seguine Mansion'),HHT('seguine-mansion','Seguine Mansion')],conf='mixed',th=[40.51205,-74.19748],thn='Lemon Creek Park lot, Seguine Avenue',brick='?'),

N('kreischer-house-charleston','Kreischer House','Charleston','nyc','landmark','standing',40.5325,-74.23833,'exact','view','drive','','c. 1885–',
  'Balthasar Kreischer, a German immigrant, built two mansions for his sons about 1885; this one, Edward\'s, is the survivor. It is a large wood-frame Queen Anne house. Edward Kreischer died of a gunshot in 1894, ruled a suicide though murder has been suggested, and tales of hauntings since made the house a filming location, Boardwalk Empire among them. It was sold in 2024 to new owners who restored it with $445,000 of state money.',
  'From the road: the asymmetric frame house with wide verandas, gables with jigsaw bargeboards, tall chimneys and a corner tower. How much of it shows from the road was not checked.',
  'A Queen Anne mansion with more stories than rooms.',
  'A private home: view only from the public road. Not open.',
  [W('Kreischer House')],brick='?'),

N('staten-island-range-light','Staten Island Light (Ambrose Channel Range Light)','Lighthouse Hill','nyc','light','standing',40.57606,-74.14125,'exact','view','drive','','1912–',
  'A 90-foot tower built in 1912 on Richmond Hill, 141 feet above the sea, as the rear range light for the Ambrose Channel, paired with the West Bank Light more than five miles out in the bay. It is still a working aid to navigation, and keeps its second-order Fresnel lens and glass reflector, though its oil lamp was replaced by a 1000-watt electric lamp. A New York City landmark since 1968.',
  'The tower above the houses of Lighthouse Hill; it shows a fixed white light seen up to 18 miles away. Interior not checked.',
  'A lighthouse on a hilltop nearly three miles from the sea, still lit with its original lens.',
  'An active navigation light in a residential neighbourhood; seen from the street. Whether it ever opens was not checked. Street parking; the houses round it are private.',
  [W('Staten Island Light')],brick='?'),

N('princes-bay-light-mount-loretto','Prince\'s Bay Lighthouse and the Mount Loretto bluffs','Pleasant Plains','nyc','light','standing',40.50769,-74.21342,'exact','view','walk','','1864–',
  'The lighthouse was built in 1864 on the highest point of Staten Island\'s south shore, with a brownstone keeper\'s cottage finished in 1868; it went dark in 1922. The Mission of the Immaculate Virgin, a Catholic orphanage at Mount Loretto, bought it in 1926. In 1999 New York State and the Trust for Public Land bought the lighthouse, the bluffs and the land round them from the Archdiocese, and it is now the Mount Loretto Unique Area. Both buildings became city landmarks in 2016.',
  'The tower and attached cottage on the bluff; on the beach below the trail behind the lighthouse, the remains of a concrete bulkhead with old cot legs and bed frames from the orphanage inside it, and the red bluff soil (DEC marker on HMdb). Interior not checked.',
  'A Civil War-era lighthouse above a beach still full of orphanage bedsteads.',
  'Mount Loretto Unique Area, NYS Department of Environmental Conservation: open year-round, dawn to dusk, with the Wetlands, Grassland and Beach Loop trails (DEC page, read November 18, 2026). Whether the lighthouse and cottage are open inside was not checked; see them from the grounds. DEC names a Hylan Boulevard parking area; the mapped lot nearest the lighthouse is on Kerny Road, about 430 m north-west.',
  [W("Prince's Bay Light"),L('NYS DEC: Mount Loretto Unique Area','https://dec.ny.gov/places/mount-loretto-unique-area'),HM(155238,'Mount Loretto Bluffs')],th=[40.50921,-74.21811],thn='Mount Loretto Unique Area lot, Kerny Road',brick='?'),

N('reformed-church-port-richmond','Reformed Church on Staten Island','Port Richmond','nyc','worship','standing',40.63972,-74.1325,'exact','view','walk','','1844 (congregation 1660)',
  'A Dutch Reformed congregation founded in 1660 and on this site since 1680. Its 1717 church was destroyed by the British in the Revolution, and the third, of 1787, gave way to the present church in 1844. The churchyard is the congregation\'s old cemetery.',
  'A Greek Revival brick church on a fieldstone foundation, with a portico of twin brick pilasters at each side and a central pair of fluted Doric columns, at 54 Port Richmond Avenue, beside its cemetery. Interior not checked.',
  'A congregation 366 years old on the same ground for 346 of them.',
  'An active church; the outside and cemetery are seen from Port Richmond Avenue. When it opens to visitors was not checked. Street parking.',
  [W('Reformed Church on Staten Island')],brick='?'),

N('woodrow-methodist-church','Woodrow Methodist Church','Woodrow','nyc','worship','standing',40.54309,-74.20127,'exact','view','drive','','1842–',
  'A Greek Revival church built in 1842, a temple-form wood-frame building with clapboard walls. The three-stage open bell tower and spire, Italianate in style, were added in 1876. A clapboard house of about 1850, enlarged in 1860 and 1861, stands on the same lot.',
  'The four Doric columns of the portico under a plain pediment, with the 1876 belfry and spire above, at 1109 Woodrow Road. Interior not checked.',
  'A country temple of 1842 still standing among Staten Island\'s suburbs.',
  'An active church; seen from Woodrow Road. When it opens to visitors was not checked. Street parking.',
  [W('Woodrow Methodist Church')],brick='no'),
]

PIN_NOTES={
 'conference-house-tottenville':'Moved about 55 m north-east from the Wikipedia coordinate (open lawn) to the OpenStreetMap museum point, on the dark-roofed house the leaf-off aerial shows at the edge of the lawn.',
 'voorlezers-house-richmond-town':'Wikipedia coordinate, which matches the OpenStreetMap building of this name within 3 m; on a small roof by Arthur Kill Road on the leaf-off aerial.',
 'st-andrews-church-richmondtown':'Wikipedia coordinate; on the church beside its churchyard on the leaf-off aerial.',
 'billiou-stillwell-perine-house':'The Register list coordinate fell on the Richmond Road intersection; moved 72 m north to the OpenStreetMap building of this name (1476 Richmond Road), which the leaf-off aerial shows as a house among others.',
 'battery-weed-fort-wadsworth':'Wikipedia coordinate; inside the walls of the fort on the leaf-off aerial.',
 'fort-tompkins-staten-island':'OpenStreetMap fort-site point; in the middle of the walled fort on the hill on the leaf-off aerial.',
 'snug-harbor-temple-row':'The Wikipedia coordinate fell on the lawn in the middle of the campus; moved about 230 m north to the OpenStreetMap outline of Building C (Main Hall), the centre of Temple Row on Richmond Terrace.',
 'nyc-farm-colony-ruins':'Moved 50 m north-east from the Wikipedia coordinate (woods) onto a roofless building shell the leaf-off aerial and the LiDAR both show; a roofed long building stands 150 m west. No construction site showed in the 300 m square on the aerial, whose date the tool does not give.',
 'staten-island-boat-graveyard':'The Wikipedia coordinate fell on the shore by Arthur Kill Road; moved 89 m north-west onto the hulks the leaf-off aerial shows in the shallows.',
 'swinburne-island-quarantine':'OpenStreetMap islet point, the middle of the island on the leaf-off aerial (the Wikipedia point was on its south-west shore).',
 'alice-austen-house':'Wikipedia coordinate; checked on the leaf-off aerial.',
 'seguine-mansion':'Wikipedia coordinate; on the house on the leaf-off aerial.',
 'kreischer-house-charleston':'Wikipedia coordinate; on the house on its hilltop clearing on the leaf-off aerial.',
 'staten-island-range-light':'Wikipedia coordinate; checked on the leaf-off aerial.',
 'princes-bay-light-mount-loretto':'Wikipedia coordinate; on the lighthouse and cottage on the bluff on the leaf-off aerial.',
 'reformed-church-port-richmond':'Wikipedia coordinate; checked on the leaf-off aerial.',
 'woodrow-methodist-church':'OpenStreetMap place-of-worship point (1101 Woodrow Road), 34 m east of the Wikipedia coordinate (which was in trees); it falls on a building set back from Woodrow Road on the leaf-off aerial.',
}
