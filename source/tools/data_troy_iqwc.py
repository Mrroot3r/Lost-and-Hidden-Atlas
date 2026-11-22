# November 22, 2026: Troy and Lansingburgh, region troy (Troy & Lansingburgh), drawn at random by
# tools/choose.py --state ny. Troy already had about ninety places, so this batch fills gaps: two Catholic churches
# that still hold services (St. Joseph's with its Tiffany windows, St. Augustine's in Lansingburgh), Frear's Troy Cash
# Bazaar, the 1919 armory on Fifteenth Street, the Soldiers and Sailors Monument, the Theta Xi house and the Chapel +
# Cultural Center on the RPI hill.
# Sources opened in this session: Wikipedia as raw text (tools/wiki_raw.py), The Evangelist (Diocese of Albany),
# the Diocese of Albany's parish listing, St. Augustine's own site, the Lansingburgh Historical Society's pages,
# Brownstoner's two-part history of Frear's (2013), the New York State Military Museum's armory page, RPI's Institute
# Archives building history, the Rensselaer Newman Foundation's worship page, New Liturgical Movement and
# GCatholic.org, all through tools/page.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'troy_iqwc','label':'Troy and Lansingburgh: St. Joseph\'s, St. Augustine\'s, Frear\'s, the armory','added':'2026-11-22 06:37'}
LHS=lambda t,p:L('Lansingburgh Historical Society: '+t,'https://www.lansingburghhistoricalsociety.org/'+p)
PLACES=[
N('st-josephs-church-troy','St. Joseph\'s Church (Tiffany windows)','Troy','troy','worship','standing',42.71598,-73.69325,'exact','open','drive','','1847',
  'A Catholic parish founded in 1847 by Father Peter Havermans of St. Peter\'s, who also started St. Francis de Sales, Troy Hospital and St. Mary\'s Cemetery. The brick church at Third and Jackson Streets dates from the parish\'s early years: a 1997 diocesan article called it 150 years old. Around the turn of the twentieth century it was given stained glass from Louis Comfort Tiffany\'s studios in New York. Carmelite friars serve it, and it is one of the few churches that still says Mass in the old Latin Carmelite rite.',
  'A red brick church with a square corner tower and clocks (Wikimedia Commons photograph). Inside, the Tiffany windows: saints and Bible scenes, among them Christ giving the keys to St. Peter, "The Light of the World", and two large windows of the Ascension and the Assumption, with more Tiffany glass set into the sacristy walls. From outside you can see that the Tiffany windows are smaller than the first openings, which were filled in with brick round them. The diocesan article of 1997 also describes a high ceiling with stencilling and gold leaf, and a copper roof put on in the mid 1990s. The church is open for its Masses; at other times see it from the street.',
  'A South Troy church with a wall of Tiffany glass.',
  'St. Joseph\'s Church, 416 Third Street at Jackson Street (Carmelite friars, Roman Catholic Diocese of Albany). Mass times from the diocese\'s page for the parish (read November 2026); the diocese says to call (518) 274-6720 for holiday times. Street parking.',
  [L('The Evangelist: Light of God shines in Troy (St. Joseph\'s windows, 1997)','https://evangelist.org/news/2018/apr/06/light-of-god-shines-in-troy'),
   L('Diocese of Albany: St. Joseph Church, Troy','https://www.rcda.org/parishes/parish/st-josephs-church-troy-ny'),
   L('New Liturgical Movement: Carmelite rite in Troy','https://www.newliturgicalmovement.org/2019/12/christmas-eve-in-carmelite-rite-in-troy.html'),
   L('The Evangelist: Troy parish notes 175 years of faith (St. Peter\'s and its daughter parishes)','https://evangelist.org/news/2018/apr/06/troy-parish-notes-175-years-of-faith/')],
  brick='yes',hours='Sunday 9 a.m., noon (Carmelite Latin) and 3 p.m. (Spanish); Saturday vigil 4 p.m.; Monday to Saturday 8 a.m.; Friday also noon (Latin)'),
N('st-augustines-church-lansingburgh','St. Augustine\'s Church, Lansingburgh','Lansingburgh, Troy','troy','worship','standing',42.77418,-73.67453,'exact','open','drive','','1864–1866; parish 1842 or 1844',
  'Lansingburgh\'s Catholic parish began in a small frame church at John and North Streets; an 1880 county history gives 1842 as its founding and the diocese\'s parish list gives 1844. The present Gothic church at the corner of John and Market Streets was begun with a cornerstone laid by Archbishop McCloskey in June 1864, had its gilded cross raised on the spire in January 1865, and was dedicated by Bishop Conroy on May 6, 1866. The 1880 history puts its cost at $40,000; a school followed in 1869.',
  'The 1860s Gothic church with its spire, close to Trinity Church (the historical society\'s old photograph of it was taken from Trinity\'s churchyard). A Troy paper in 1866 wrote that its interior looked like St. Peter\'s in Troy; interior not checked. Open for Mass; at other times see it from the street.',
  '',
  'St. Augustine\'s Church (Roman Catholic), 25 115th Street, Lansingburgh. Mass times from the parish\'s own site (read November 2026). Street parking.',
  [LHS('St. Augustine\'s Church','saint-augustines-church'),
   L('St. Augustine\'s Church, Troy: Mass schedule','https://staugchurchtroy.com'),
   L('Wikipedia: List of parishes in the Diocese of Albany','https://en.wikipedia.org/wiki/List_of_parishes_in_the_Diocese_of_Albany')],
  brick='?',hours='Saturday 4 p.m.; Sunday 10:30 a.m.; Monday, Tuesday, Friday and Saturday 8:30 a.m.; Thursday 6 p.m.'),
N('frears-troy-cash-bazaar','Frear\'s Troy Cash Bazaar','Troy','troy','civic','standing',42.73226,-73.68980,'exact','view','drive','renewal','1897',
  'William Henry Frear opened a dry goods store in Troy in 1865 and by 1894 his Troy Cash Bazaar filled the whole of the Cannon Building on Monument Square. In 1897 he put up this marble-fronted department store at Third and Fulton Streets: four floors round a central atrium under a big skylight, reached by a double stair with cast-iron railings made in Troy. The family ran it until 1941, when the Rowley stores bought it and kept the name. In the 1960s its annex was torn down for urban renewal and the store became offices, with the stair hidden and part of it stored in the basement; New York State health offices were there until 2013, after which shops came back.',
  'The marble front with its three arched entrances on Third and Fulton Streets. What is left of the atrium and the stair inside, and which shops are open now, was not checked (the account read dates from 2013, when a pharmacy held one side and antique and clothing shops were opening on the other).',
  'The largest department store upstate in its day, with a Troy-made iron stair.',
  'Privately owned building at 2 Third Street, on the corner of Fulton Street, downtown Troy. See it from the street; go in only where a shop is open to customers. Metered street parking and city garages downtown (not checked).',
  [L('Brownstoner: Walkabout, Frear\'s Troy Cash Bazaar, part one (2013)','https://www.brownstoner.com/history/walkabout-frears-troy-cash-bazaar-part-one/'),
   L('Brownstoner: Walkabout, Frear\'s Troy Cash Bazaar, part two (2013)','https://www.brownstoner.com/history/walkabout-frears-troy-cash-bazaar-part-two')],
  brick='?'),
N('troy-armory-fifteenth-street','Troy Armory (RPI Alumni Sports and Recreation Center)','Troy','troy','civic','standing',42.72848,-73.67688,'exact','view','drive','','1918–1919 (or 1920)',
  'Troy\'s armory on Ferry Street burned in 1917, and the state built this one on Fifteenth Street to replace it, to designs by Lewis F. Pilcher: about 95,000 square feet on a 9.67-acre lot. Wikipedia and the state military museum give 1918 to 1919 for its building; RPI\'s archives say 1920. The 105th Infantry moved in from its temporary quarters in Lansingburgh in January 1922. RPI rented it for naval training in the 1940s and tried twice to buy it; it finally did in 1970–71, paying $1.6 million and giving 20 acres in East Greenbush for a new armory, and it has been the Alumni Sports and Recreation Center since 1973, with a pool added in 1984.',
  'The old armory building on Fifteenth Street at the edge of the RPI campus, still called "the Armory". Interior not checked; it is a university sports building.',
  '',
  'Rensselaer Polytechnic Institute, 15th Street. See it from the street; the inside is for the RPI community. Street parking nearby is mostly permit or metered (not checked).',
  [W('Alumni Sports and Recreation Center (Armory)'),
   L('New York State Military Museum: Troy, 15th Street Armory','https://museum.dmna.ny.gov/armories-arsenals/troy-armory-fifteenth-street'),
   L('RPI Institute Archives: Armory / ASRC','https://archives.rpi.edu/institute-history/building-histories/armory-alumni-sports-and-recreation-center-asrc'),
   LHS('State Armory (Bolton Hall, 1917–1922)','state-armory')],
  brick='?',conf='mixed'),
N('soldiers-sailors-monument-troy','Soldiers and Sailors Monument ("The Call to Arms")','Troy','troy','curio','standing',42.73162,-73.69167,'exact','public','drive','','1891',
  'The county\'s war monument in the middle of Monument Square, dedicated on September 15, 1891, to the men of Rensselaer County who fought in the Revolution, the War of 1812 and the Civil War. The Albany firm of Fuller & Wheeler designed it; the statue is by James E. Kelly, the bronze reliefs were modelled by Caspar Buberl, and the Henri-Bonnard Bronze Company of New York cast them. It was rededicated in September 1991.',
  'A granite column about 50 feet high topped by a 17-foot bronze Columbia, "The Call to Arms", facing north with a sword and a trumpet. On the base: wreaths round "1776", "1812" and "1861-65", relief panels of infantry, cavalry and artillery, and a sea fight between the Monitor and the Merrimack, a nod to the Monitor\'s armour plate rolled in Troy.',
  '',
  'In the middle of Monument Square, where Broadway, River Street and Second Street meet in downtown Troy: a public square in the street, so it can be seen at any time. Metered street parking.',
  [W('Soldiers and Sailors Monument (Troy, New York)')],
  brick='no'),
N('theta-xi-house-troy','Theta Xi Fraternity Chapter House ("The Zoo")','Troy','troy','landmark','standing',42.73041,-73.67522,'exact','view','drive','','1931',
  'The house of RPI\'s Alpha chapter of Theta Xi. The chapter tried from 1910 to build on land near the campus; the Sage Avenue lot was bought after 1926, but the Depression held the work back until 1931. RPI\'s president Palmer C. Ricketts, a Theta Xi brother, laid the first stone on June 13, 1931, and the house, designed by Joseph M. Lawlor and built by Rosch Brothers, was finished that September for about $57,000. It was listed on the National Register in 2013.',
  'A two-and-a-half-storey Tudor Revival house in Flemish-bond brick with half-timbering and stucco upstairs, a steep slate roof with crossing gables, tall chimneys, metal casement windows and a Tudor-arched limestone doorway. The Register form describes limestone fireplaces and oak beams inside; it is a fraternity house, so see it from the street.',
  '',
  'Private fraternity house, 1490 Sage Avenue. View from the street only. Street parking (permit rules near the campus not checked).',
  [W('Theta Xi Fraternity Chapter House')],
  brick='?'),
N('chapel-cultural-center-rpi','Chapel + Cultural Center at Rensselaer','Troy','troy','worship','standing',42.73181,-73.67223,'exact','open','drive','','1967–1968',
  'A Catholic chapel and arts hall built by the Rensselaer Newman Foundation after the Catholic community at RPI lost its regular chapel in the early 1960s. Levatich and Miller of Ithaca designed it in 1967, and it opened with a two-week dedication festival in October and November 1968. Plain unfinished block outside and one flexible hall within, it was written up in national magazines and the New York Times by 1969, and was listed on the National Register in 2011. It is the home of the University Parish of Christ Sun of Justice.',
  'Inside: an auditorium for up to 450 with movable seating, an altar chapel behind sliding wooden doors, a stained glass oculus by Ade Bethune in the east wall, Greek, Roman and Hebrew alphabets painted on the floor by Father Edward Catich, and a fragment of Eric Gill\'s carved "Spoil Bank Crucifix". The public can go in for Mass and for concerts and other events.',
  '',
  'Rensselaer Newman Foundation, 2125 Burdett Avenue (Wikipedia\'s infobox gives 2215), across from the Houston Field House. Mass times from the foundation\'s worship page (read November 2026). Parking not checked.',
  [W('Chapel + Cultural Center at Rensselaer'),
   L('Rensselaer Newman: Worship','https://rensselaernewman.org/worship/')],
  brick='no',hours='Sunday 10 a.m. and 5 p.m.; Monday and Tuesday 5 p.m.; Wednesday 9 a.m.'),
]
PIN_NOTES={
 'st-josephs-church-troy':'ArcGIS geocoder PointAddress for 416 3rd Street.',
 'st-augustines-church-lansingburgh':'ArcGIS geocoder PointAddress for 25 115th Street.',
 'frears-troy-cash-bazaar':'ArcGIS geocoder PointAddress for 2 3rd Street, the corner of Third and Fulton Streets.',
 'troy-armory-fifteenth-street':'OpenStreetMap sports-centre building (1616 15th Street); Wikipedia\'s point is 20 m away.',
 'soldiers-sailors-monument-troy':'Wikipedia infobox coordinate; on the aerial it is on the traffic island where the column\'s shadow starts, within about 6 m.',
 'theta-xi-house-troy':'ArcGIS geocoder PointAddress for 1490 Sage Avenue; Wikipedia\'s point is 20 m away.',
 'chapel-cultural-center-rpi':'ArcGIS geocoder PointAddress for 2125 Burdett Avenue.',
}
