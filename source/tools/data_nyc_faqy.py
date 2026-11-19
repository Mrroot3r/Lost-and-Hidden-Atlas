# November 19, 2026: the North Shore of Nassau County (Roslyn, Sands Point, Saddle Rock, Oyster Bay, Muttontown, Jericho,
# Old Westbury, Locust Valley) with Fort Totten and the New York State Pavilion just over the line in Queens.
# Region nyc drawn at random by choose.py --state ny (it offered Roslyn); tools/start.py found no Atlas place within 20 km.
# Facts come only from sources opened in this session: Wikipedia read as raw text (tools/wiki_raw.py), Nassau County's
# Muttontown Preserve and Saddle Rock Grist Mill pages, the Roslyn Landmark Society's pages (Knollwood hike, Cedarmere,
# Harbor Hill water tower), the Friends of Cedarmere, the Sands Point Preserve Conservancy, Raynham Hall Museum, the
# Planting Fields Foundation and NYS Parks, the National Park Service (Sagamore Hill), Old Westbury Gardens, NYC Parks
# (Fort Totten Park) and Long Island Press / Herald articles (Roslyn and Saddle Rock mills, Matinecock meetinghouse,
# Oyster Bay turntable).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
RLS=lambda slug,t: ['Roslyn Landmark Society: '+t,'https://www.roslynlandmarks.org/'+slug]

BATCH={'key':'nyc_faqy','label':'North Shore of Nassau County & Fort Totten','added':'2026-11-19 04:01'}

PLACES=[
N('knollwood-ruins-muttontown','Knollwood estate ruins (King Zog\'s mansion), Muttontown Preserve','Muttontown','nyc','landmark','ruins',40.82538,-73.53594,'site','public','hike','','1906–1959',
  'A 60-room granite mansion built on the Knollwood estate for Charles Hudson in the early 1900s (the Roslyn Landmark Society, quoting a 2013 write-up, gives 1906 to 1920 and calls him a steel tycoon; Nassau County calls him a Wall Street investor). King Zog of Albania bought the estate in 1951 as a home in exile but never came to the United States, and sold it in 1955 to Lansdell Christie. Left empty, it was stripped by vandals hunting for treasure Zog was rumoured to have hidden in the walls, and the Christie family had it demolished in 1959. The land is now part of Nassau County\'s 550-acre Muttontown Preserve.',
  'In the woods just north of Muttontown Road: the grand double staircase that led up to the house, with an alcove on either side, a broken fountain where the stairs meet (its carved face is badly damaged) and stone garden ruins round about. Trails are poorly marked, so bring a map; the county page says maps and brochures are available for self-guided walks. The house itself is gone.',
  'A king\'s house that the king never saw, reduced to a staircase in the woods.',
  'Muttontown Preserve, Nassau County Department of Parks, Recreation and Museums (main entrance off NY 25A west of Jericho-Oyster Bay Road, Muttontown Lane, East Norwich; phone 516-571-8500 on the county page). Hours not checked: the county page gives none. The Roslyn Landmark Society suggests parking at the preserve\'s equestrian center; the mapped lot on Muttontown Road is about 350 m south-west of the pin, on preserve land.',
  [L('Nassau County: Muttontown Preserve','https://www.nassaucountyny.gov/2839/Muttontown-Preserve'),W('Muttontown Preserve'),
   RLS('news/nearby-historic-hikes-exploring-the-ruins-of-the-charles-hudsons-knollwood-in-the-muttontown-preserve/','exploring the Knollwood ruins')],
  conf='mixed',th=[40.82328,-73.53901],thn='Muttontown Preserve lot, Muttontown Road',brick='no'),

N('roslyn-grist-mill','Roslyn Grist Mill','Roslyn','nyc','industry','standing',40.80048,-73.64951,'exact','view','walk','','1715–1741 (mill on the site c. 1701)',
  'John Robeson built a gristmill here in the first decade of the 1700s; Jeremiah Williams is believed to have built the present one between 1715 and 1741. Hendrick Onderdonk, who also ran paper mills in what was then Hempstead Harbor, owned it from 1758, and George Washington mentions the mill in his diary of a 1790 visit. The Hicks family milled here until 1916, then ran it as a tea house and museum until Nassau County took it over in 1975 and it stood empty. It is one of the few Dutch colonial commercial frame buildings left in the country.',
  'A timber-framed mill, 50 by 25 ft, covered in weatherboard, with a wing over the race on the west side and a hook-and-pulley loft door in the attic gable. Some original gearing was still inside in 1986. The Roslyn Landmark Society is restoring it as a museum of the village\'s water-powered industries: a new foundation raising it back to street level was finished in 2024, a cedar shingle roof in late 2025, and new siding was due in spring 2026 (Long Island Press, January 2026). Not yet open inside.',
  'A 1700s Dutch-framed mill being lifted back to street level.',
  'Owned by Nassau County, to pass to the Village of Roslyn when restored; the Roslyn Landmark Society runs the work. Seen from Old Northern Boulevard by the mill pond. Mapped lots on Old Northern Boulevard and Glen Avenue are within 150 m; whether they are public was not checked. Village Municipal Parking Field 4 on East Broadway is about 250 m east.',
  [W('Roslyn Grist Mill'),L('Long Island Press: Roslyn Grist Mill restoration moves forward (January 6, 2026)','https://www.longislandpress.com/2026/01/06/roslyn-grist-mill-siding')],
  th=[40.80127,-73.64682],thn='Village of Roslyn Municipal Parking Field 4, East Broadway',brick='no'),

N('roslyn-main-street-clock-tower','Roslyn Main Street and the Ellen E. Ward Clock Tower','Roslyn','nyc','town','standing',40.79976,-73.6505,'area','view','walk','','1773–1895',
  'Roslyn grew up in the mid-1600s as Hempstead Harbor, a port for Hempstead and the farms to the south. Its first gristmill came in 1700 and Hendrick Onderdonk\'s paper mill in 1773; the oldest house on Main Street, number 150, was built about then by Wilson Williams, a cooper who worked for Onderdonk. The houses on the street quadrupled in the 1800s, mostly Federal and Greek Revival homes built by local builders and merchants. The stone clock tower at Main Street and Old Northern Boulevard went up in 1895; the street was listed as a Register district in 1974 after the Roslyn Landmark Society worked to save it.',
  'Some fifty buildings along Main Street from NY 25A to East Broadway, with Tower Street and parts of Glen Avenue and Paper Mill Road, nearly all from before the Civil War and little changed. Start at the stone clock tower (pin) and walk south. The houses are private homes: look from the street.',
  'A Long Island mill village that the suburbs went round.',
  'Public streets in the Village of Roslyn; the houses are private. Changes to them need the village\'s Historic District Board. Village Municipal Parking Field 4 on East Broadway is about 300 m north-east of the clock tower.',
  [W('Main Street Historic District (Roslyn, New York)')],th=[40.80127,-73.64682],thn='Village of Roslyn Municipal Parking Field 4, East Broadway',brick='?'),

N('cedarmere-roslyn-harbor','Cedarmere (William Cullen Bryant\'s home)','Roslyn Harbor','nyc','landmark','standing',40.81122,-73.64603,'exact','public','walk','','1787–',
  'The poet and New York Evening Post editor William Cullen Bryant bought a small house here in 1843 (built by Joseph Moulton; the first known house on the land was a Quaker farmer\'s, of 1787) and enlarged house and grounds through the 1850s and 1860s on the cottage principles of Andrew Jackson Downing. It stayed in the family until 1975, when the last owner left it at her death to Nassau County as a memorial to him. The inland part of his land became the Bryce and Frick estate, now the Nassau County Museum of Art.',
  'A stuccoed house on a stone foundation behind a high stone wall above Hempstead Harbor, with two ponds, a stone bridge and an Olmsted-designed landscape. By the pond stands the Mill, a Gothic Revival folly with a brick basement, board-and-batten walls, carved bargeboards and a slate roof, said to be by Calvert Vaux; it was never a working mill. A side window of the house has Bryant\'s initials etched in the top panes (Wikipedia). The house opened as a museum in 1994 and closed in 2008; now only the first floor is shown, on guided tours, and the Mill is closed for interior restoration (Friends of Cedarmere).',
  'A poet\'s retreat with a mill that never ground anything.',
  'Nassau County Department of Parks, Recreation and Museums, with the Friends of Cedarmere. Grounds open year-round; house tours of the first floor only, Thursdays at 2 pm and 3 pm (Friends of Cedarmere page, read November 19, 2026). 225 Bryant Avenue. The nearest mapped lot is the Nassau County Museum of Art\'s on Museum Drive, about 500 m south-east; parking at Cedarmere itself not checked.',
  [W('Cedarmere-Clayton Estates'),L('Friends of Cedarmere: about and hours','https://www.friendsofcedarmere.org/about'),RLS('profiles/cedarmere','Cedarmere')],
  th=[40.80781,-73.64239],thn='Nassau County Museum of Art lot, Museum Drive',brick='?'),

N('trinity-church-roslyn','Trinity Church Complex, Roslyn','Roslyn','nyc','civic','standing',40.80502,-73.64464,'exact','view','walk','','1906–',
  'An Episcopal church complex built in 1906 to designs by McKim, Mead & White, one of the firm\'s works for the estate owners of the North Shore. The Roslyn-Trinity Cooperative Day School, founded in 1951, is part of the complex, and a child care centre opened there in 2016. It was listed on the National and State Registers in 1986.',
  'The church and its buildings on Northern Boulevard (NY 25A) at the north edge of the village. Interior not checked.',
  'A McKim, Mead & White parish church for Gold Coast Roslyn.',
  'An active parish (Trinity Episcopal Church, 1579 Northern Boulevard); seen from the road. Visiting hours not checked. Village Municipal Parking Field 4 on East Broadway is about 450 m south.',
  [W('Trinity Church Complex (Roslyn, New York)')],th=[40.80127,-73.64682],thn='Village of Roslyn Municipal Parking Field 4, East Broadway',brick='?'),

N('mackay-estate-water-tower','Mackay Estate Water Tower (Harbor Hill)','East Hills','nyc','water','standing',40.79743,-73.6395,'exact','view','drive','','1899–1902',
  'A water tower designed in 1899 by Stanford White of McKim, Mead & White and built 1900 to 1902 for Clarence Mackay\'s Harbor Hill estate. The steel tank, made by Tippett and Wood of Phillipsburg, New Jersey, is hidden inside a tall tower of random ashlar stone under a Guastavino tile dome. The great house and grounds are gone, the estate cut up for 1950s houses; the tower is one of three outbuildings that survive (the gate lodge and the dairyman\'s cottage are the others).',
  'The stone tower and its dome on a slight rise among trees and grass, in an open area just west of Redwood Drive, surrounded by suburban houses (Roslyn Landmark Society).',
  'A Stanford White folly hiding a water tank, all that stands of a vanished palace.',
  'Who owns the ground round the tower was not checked; look from Redwood Drive, a residential street in the Village of East Hills, and do not cross yards. No public lot was found; street parking not checked.',
  [W('Mackay Estate Water Tower'),RLS('profiles/harbor-hill-water-tower','Harbor Hill Water Tower')],brick='no'),

N('saddle-rock-grist-mill','Saddle Rock Grist Mill','Saddle Rock','nyc','industry','standing',40.79775,-73.75117,'exact','view','walk','','c. 1700–',
  'A tide mill on Little Neck Bay, built around 1700, that ground corn and wheat for the farms of the Great Neck peninsula using the rise and fall of the tide. It stayed with the families of its first owners until 1950; a descendant, Louise Udall Skidmore Eldridge, left it to the Nassau County Historical Society, which gave it to the county in 1955. Restored to its mid-1800s look in the 1950s, it was for years a county museum and school field-trip stop, and was listed on the Register in 1978 as the only surviving tidal grist mill on Long Island.',
  'The mill building on the shore of Little Neck Bay at the end of Grist Mill Lane. Wikipedia says the museum is now closed; interior not checked.',
  'Long Island\'s last tide mill, which ran on the moon.',
  'Owned by Nassau County (Department of Parks, Recreation and Museums). Closed as a museum (Wikipedia); no current hours were found on the county page. A mapped lot on Grist Mill Lane, about 140 m south, lies in a village park; whether outsiders may use it was not checked.',
  [W('Saddle Rock Grist Mill'),L('Nassau County: Saddle Rock Grist Mill','https://www.nassaucountyny.gov/2947/Saddle-Rock-Grist-Mill'),
   L('Long Island Press: the Village of Saddle Rock (January 5, 2026)','https://www.longislandpress.com/2026/01/05/focus-on-the-g-n-peninsula-the-village-of-saddle-rock')],
  th=[40.7966,-73.75172],thn='Grist Mill Lane lot (village park)',brick='?'),

N('castle-gould-hempstead-house','Castle Gould and Hempstead House, Sands Point Preserve','Sands Point','nyc','landmark','standing',40.86119,-73.69768,'site','public','walk','','1900–1912',
  'Howard Gould, a son of Jay Gould, bought the land in 1900 and built an estate whose limestone stables and servants\' quarters, Castle Gould (about 100,000 sq ft), are bigger than the 40-room main house finished in 1912. Gould sold it in 1917 to Daniel Guggenheim, who renamed the main house Hempstead House. The Guggenheims gave it to the Institute of Aeronautical Sciences in 1942; the Navy held it from 1946 to 1967, and the federal government passed the deed to Nassau County in 1971.',
  'Castle Gould (pin), with the welcome centre, and Hempstead House about 500 m north-west, with its 80 ft tower. Inside Hempstead House: the oak organ case in the entry foyer with show pipes still on the walls, the walnut-panelled library copied from a palace of James I with relief portraits on the plaster ceiling, and a billiard room with carved oak from a 17th-century Spanish palace (Wikipedia). Hempstead House and the Guggenheim house Falaise are shown on guided tours only.',
  'A railroad heir\'s stable block grander than his house.',
  'Sands Point Preserve, Nassau County, run with the Sands Point Preserve Conservancy, 127 Middle Neck Road. Open Wednesday to Sunday, closed Monday and Tuesday; in winter (November 5, 2025 to March 29, 2026) 9 am to 5 pm, and later in spring, summer and fall; closed Thanksgiving and Christmas Eve to New Year\'s Day. Admission $15 a car or $4 on foot; dogs on leash; no bicycles, swimming or drones. The south end of the estate is private (Conservancy hours page, read November 19, 2026). Lot beside Castle Gould.',
  [W('Hempstead House'),L('Sands Point Preserve: hours and admission','https://www.sandspointpreserveconservancy.org/?p=6519')],
  th=[40.86155,-73.69857],thn='Castle Gould lot (mapped lot on an unpaved oval by the castle)',brick='?'),

N('raynham-hall-oyster-bay','Raynham Hall','Oyster Bay','nyc','landmark','standing',40.87228,-73.53168,'exact','public','walk','','1738–',
  'Samuel Townsend bought a two-up, two-down house here in 1738 and enlarged it to an eight-room saltbox. In the Revolution it was the headquarters of John Graves Simcoe\'s Loyalist Queen\'s Rangers, while Townsend\'s son Robert worked in Manhattan as a spy in Washington\'s Culper Ring. A grandson renamed it Raynham Hall and remodelled it in Victorian style in 1851. The family deeded it to the local DAR in 1941; it passed to the Town of Oyster Bay, which keeps it as a museum.',
  'A house that shows two eras: the colonial saltbox and the 1851 Victorian enlargement. Officers of the Queen\'s Rangers etched compliments to the Townsend sisters on panes of glass, and Simcoe gave Sally Townsend a valentine in 1778 (Wikipedia; whether the glass is on show was not checked). Tours take in the house and an exhibition hall.',
  'A Patriot spy\'s family home with Loyalist officers living in it.',
  'Owned by the Town of Oyster Bay, run by the Friends of Raynham Hall Museum, 20 West Main Street. Self-guided tours Tuesday, Thursday and Saturday hourly 1 to 4 pm; guided tours Wednesday, Friday and Sunday at 1 and 3 pm; closed Monday (museum tours page, read November 19, 2026). Admission charged ($10 for students and seniors per the Village of Upper Brookville page; full price not checked). Town Parking Field O-2 is beside the house.',
  [W('Raynham Hall Museum'),L('Raynham Hall Museum: tours and tickets','https://raynhamhallmuseum.org/?p=9385'),L('Village of Upper Brookville: Raynham Hall','https://upperbrookville.gov/raynham-hall-museum/')],
  th=[40.8718,-73.53169],thn='Parking Field O-2, West Main Street',brick='?'),

N('oyster-bay-station-turntable','Oyster Bay station and turntable (Oyster Bay Railroad Museum)','Oyster Bay','nyc','rail','standing',40.87502,-73.5316,'exact','public','walk','stations','1889–',
  'The Victorian depot opened on June 24, 1889 as the end of the line from Locust Valley. In 1891 a 1,000 ft wharf let whole passenger cars go onto a ferry to Connecticut on a short-lived New York to Boston route, and that September locomotive No. 113 blew up while idling at the station. Theodore Roosevelt commuted through it, and in 1902 Bradford Lee Gilbert enlarged it for the crowds expected at the Summer White House. The old depot and the turntable were listed on the Register separately in 2005; the Town of Oyster Bay owns the depot and the Oyster Bay Railroad Museum has restored it.',
  'The 1889 depot with its western and southern fronts restored and a rebuilt ticket window, holding museum exhibits and three LIRR cab simulators. The turntable, said to be 117 years old when it turned again in 2021, is in the museum\'s open-air display yard on the east side of Theodore Roosevelt Memorial Park, a short walk away (about 40.87502, -73.52854). Trains still use the modern platform beside the depot.',
  'The station that took trains onto ferries and a president to his summer home.',
  'Depot owned by the Town of Oyster Bay, run by the Oyster Bay Railroad Museum. Open weekends from April to November (Wikipedia); the museum\'s own page refused to open (HTTP 403), so hours not checked there. Mapped lots on Hamilton Avenue and Audrey Avenue (Parking Field O-5) are within 170 m.',
  [W('Oyster Bay station'),L('Herald: taking a spin on a railroad turntable (July 2021)','https://www.liherald.com/stories/taking-a-spin-on-a-railroad-turntable,133328'),L('Oyster Bay Railroad Museum','https://www.obrm.org/')],
  th=[40.87355,-73.53106],thn='Parking Field O-5, Audrey Avenue',brick='?'),

N('planting-fields-main-house','Planting Fields Main House (Coe Hall)','Upper Brookville','nyc','landmark','standing',40.8649,-73.55765,'exact','public','walk','','1918–1921',
  'William Robertson Coe bought the estate in 1913. Its first mansion burned to the ground on March 19, 1918, and the present Main House was built 1918 to 1921 in Tudor Revival style to designs by Walker & Gillette. The Olmsted Brothers and Lowell & Sargent laid out the grounds, with camellia and main greenhouses from 1914 on. Coe gave the estate to New York State in 1949; it was a first home for what became Stony Brook University until 1968, and is now a state historic park.',
  'A 65-room Tudor Revival house faced in Indiana limestone, kept with furnishings of the estate years and shown on guided tours. Also on the grounds: the wrought-iron Carshalton Gates made in 1712 for Carshalton Park in England and brought here in 1921, the Camellia Greenhouse (1917), the main greenhouse, the Italian Blue Pool Garden with its 1915 tea house, and five miles of woodland trails.',
  'A Tudor manor rebuilt after the first one burned, with 1712 English gates.',
  'Planting Fields Arboretum State Historic Park (NYS Parks with the Planting Fields Foundation). Park open daily 9 am to 5 pm, closed December 25; parking $8 a car, collected on weekends and holidays in April, daily from early May to Labor Day and on fall weekends to mid-November; greenhouses 10 am to 4 pm, closed Tuesdays; Main House by tour (the foundation\'s visitor centre is open Friday to Sunday 11 am to 4 pm) (foundation and NYS Parks pages, read November 19, 2026). West Parking is about 240 m south-east.',
  [W('Planting Fields Arboretum State Historic Park'),L('Planting Fields Foundation: hours and admission','https://plantingfields.org/hoursandadmission/'),
   L('NYS Parks: Planting Fields','https://parks.ny.gov/historic-sites/plantingfields/details.aspx')],
  th=[40.86404,-73.555],thn='Planting Fields West Parking',brick='no'),

N('sagamore-hill-roosevelt','Sagamore Hill (Theodore Roosevelt\'s home)','Cove Neck','nyc','landmark','standing',40.88558,-73.50107,'exact','public','walk','','1885–',
  'Theodore Roosevelt had Lamb & Rich design this Shingle-style Queen Anne house in 1884; it was built in 1885 and was his home until he died in 1919. It was the "Summer White House" for the seven summers of 1902 to 1908. Congress made it a national historic site in 1962. The museum is in Old Orchard, the 1938 house of his son Theodore Jr.; the visitor centre burned on Christmas Eve 2018.',
  'Inside the house nearly all the furnishings are original (Wikipedia), seen on a ticketed tour. The grounds, the Old Orchard Museum and a nature trail are open to walk.',
  'The Summer White House, still furnished as Roosevelt left it.',
  'Sagamore Hill National Historic Site (National Park Service). Grounds open daily, sunrise to 30 minutes after sunset, free. The house by advance reservation only. Old Orchard Museum Thursday 1 to 4:30 pm and Friday to Sunday noon to 4:30 pm. Closed Thanksgiving, December 25 and January 1 (NPS hours page, read November 19, 2026). Lot on Sagamore Hill Road about 180 m east.',
  [W('Sagamore Hill'),L('NPS: Sagamore Hill hours and seasons','https://www.nps.gov/sahi/planyourvisit/hours.htm')],
  th=[40.88671,-73.49862],thn='Sagamore Hill lot, Sagamore Hill Road',brick='?'),

N('matinecock-friends-meetinghouse','Matinecock Friends Meetinghouse','Matinecock','nyc','civic','standing',40.86638,-73.59426,'exact','view','drive','','1725–',
  'A Quaker meeting house built in 1725 at Piping Rock and Duck Pond Roads, one of the oldest houses of worship on Long Island in continuous use. Friends Academy, the Quaker school founded in Locust Valley in 1876, still sends students and staff to meeting for worship here. The North Shore Historical Museum opened an exhibit on its 300 years in November 2025.',
  'A shingled meeting house two bays wide and four long, on the north-west corner of Piping Rock and Duck Pond Roads. Interior not checked.',
  'Three hundred years of Quaker meetings in one shingled room.',
  'An active Quaker meeting; seen from the road. When visitors may attend was not checked. No public lot was found nearby; parking not checked.',
  [W('Matinecock Friends Meetinghouse'),L('Long Island Press: 300 years of the Matinecock Meetinghouse (November 3, 2025)','https://www.longislandpress.com/2025/11/03/north-shore-historical-museum-unveils-exhibit-celebrating-300-years-of-the-matinecock-quaker-meetinghouse')],
  brick='no'),

N('jericho-friends-meeting-house','Jericho Friends Meeting House and Elias Hicks\'s grave','Jericho','nyc','civic','standing',40.7949,-73.53654,'exact','view','drive','cemeteries','1788–',
  'A Quaker meeting house of 1788 with the Friends\' schoolhouse of 1793, a large shed of about 1875 and the Friends\' burying ground. The preacher Elias Hicks (1748–1830) helped build the meeting house and is buried in the cemetery. Listed on the Register in 2002.',
  'A two-storey timber-framed meeting house with a gable roof, clad in wood shingles, beside the old schoolhouse, the shed and the burying ground, at 6 Old Jericho Turnpike. Interior not checked.',
  'The meeting house Elias Hicks helped build, with his grave beside it.',
  'An active Quaker meeting; seen from Old Jericho Turnpike. When visitors may enter the grounds or attend was not checked. Parking not checked.',
  [W('Jericho Friends Meeting House Complex')],brick='no'),

N('westbury-house-old-westbury-gardens','Westbury House, Old Westbury Gardens','Old Westbury','nyc','landmark','standing',40.77375,-73.59474,'exact','public','walk','','1903–1906',
  'John Shaffer Phipps, an heir to the Phipps family fortune, began the estate in 1903 for his bride Margarita Grace, and the house was ready for the family in 1906. Next to it is a mid-1860s farmhouse, enlarged, known as Orchard Hill. The estate opened as a museum in 1959. Scenes of North by Northwest, Love Story and many other films were shot here.',
  'Westbury House and its gardens, including the walled garden. John Singer Sargent\'s portrait of Mrs. Henry Phipps and her grandson Winston (1906–07) hangs in the dining room. The ground floor rooms seen in Love Story are on the house tour.',
  'A Gold Coast house left as the Phipps family lived in it.',
  'Old Westbury Gardens (a nonprofit), 71 Old Westbury Road, which is the only entrance. The gardens and Westbury House are open weekends only in November, 10 am to 5 pm, last entry 3 pm for non-members, closed Thanksgiving week and weekdays in November; tickets required; dogs only on set dog weekends (its plan-your-visit page, read November 19, 2026). Wikipedia gives the main tour season as April to October. Parking at the entrance; the lot was not checked on the aerial.',
  [W('Old Westbury Gardens'),L('Old Westbury Gardens: plan your visit','https://www.oldwestburygardens.org/?p=4879')],brick='?'),

N('fort-totten-willets-point','Fort Totten (Fort at Willets Point)','Bayside','nyc','fort','ruins',40.79536,-73.7796,'site','public','walk','forts','1862–1974',
  'The Army began a granite fort at Willets Point in 1862, under the Third System, to guard the East River approach to New York with Fort Schuyler across the water. Work stopped after the Civil War, when masonry forts were seen to be obsolete, and the fort was never finished. The post was the Army\'s Engineer School from 1869 to 1901, was renamed Fort Totten in 1898, got Endicott-era gun and mortar batteries from 1897, and was disarmed by 1935. It closed as a regular Army post in 1974; most of it is now a New York City park and a city historic district.',
  'The unfinished granite water battery on the point (pin), and the 1870s tunnel that joined it to the upper battery; the castle-style Officers\' Club of the 1870s, now the Bayside Historical Society; and many dilapidated, unused post buildings (Wikipedia). NYC Parks Urban Park Rangers lead tours of the fortress, and the visitor centre has a museum on the fort\'s history.',
  'An unfinished Civil War fort that became the Army\'s engineering school.',
  'Fort Totten Park, NYC Parks; parts of the old post are still used by the Army Reserve, the NYPD and the FDNY and are closed. Park and visitor centre hours not checked (the NYC Parks park page gives none). The federal land map marks the point where the pin sits as Coast Guard land; keep to park paths and go with a ranger tour if unsure. Reached by the Cross Island Parkway and the Clearview Expressway. A mapped lot inside the park on Willets Street is about 300 m south of the fort; the lot nearer the fort is on Coast Guard land.',
  [W('Fort Totten (Queens)'),L('NYC Parks: Fort Totten Park','https://www.nycgovparks.org/parks/fort-totten-park')],
  th=[40.79297,-73.78061],thn='Fort Totten Park lot, Willets Street',brick='no'),

N('new-york-state-pavilion','New York State Pavilion (1964 World\'s Fair)','Flushing Meadows','nyc','amuse','standing',40.74358,-73.84438,'exact','view','walk','','1962–',
  'Philip Johnson and Richard Foster designed the pavilion for the 1964 World\'s Fair, with Lev Zetlin as engineer: the Tent of Tomorrow, three observation towers (the tallest 226 ft) and the drum-shaped Theaterama. It opened April 23, 1964. After the fair the towers never reopened; the Tent was briefly a concert hall and roller rink in the 1970s and was then left to decay, while the Theaterama became the Queens Theatre in 1989. The Tent was repainted in 2014 and a restoration began in 2019; its first phase won a preservation award in 2023, and the towers\' repair was due to finish in October 2026.',
  'The steel ring of the Tent of Tomorrow, 250 by 350 ft, which once roofed a terrazzo road map of New York State, and the three concrete towers that once carried elevators to an observation deck, near the Unisphere. Whether the towers are open now that the restoration was due to end was not checked; look from the paths.',
  'The World\'s Fair towers that stood empty for half a century.',
  'Owned by NYC Parks in Flushing Meadows–Corona Park; the structures are closed apart from the Queens Theatre. Park hours not checked. The nearest mapped park lot, off Meridian Road, is about 760 m north-west.',
  [W('New York State Pavilion')],th=[40.75008,-73.84867],thn='Flushing Meadows–Corona Park lot, Meridian Road',brick='no'),
]

PIN_NOTES={
 'knollwood-ruins-muttontown':'OpenStreetMap ruin lead "Knollwood Estate". The aerial shows only bare woods; the LiDAR sheet shows a terraced platform edged by wall lines at the pin and a walled rectangle about 100 m east (OSM maps a "Walled Garden" 250 m north). The exact spot of the staircase was not confirmed.',
 'roslyn-grist-mill':'OpenStreetMap building, 1347 Old Northern Boulevard (nom.py); the Register point is 25 m away.',
 'roslyn-main-street-clock-tower':'OpenStreetMap point of the clock tower at the north end of the district; the district runs about 500 m south along Main Street.',
 'cedarmere-roslyn-harbor':'OpenStreetMap building, 225 Bryant Avenue (nom.py).',
 'trinity-church-roslyn':'OpenStreetMap place of worship, 1579 Northern Boulevard (nom.py).',
 'mackay-estate-water-tower':'OpenStreetMap water tower on Redwood Drive (nom.py); matches the Register point within 20 m.',
 'saddle-rock-grist-mill':'OpenStreetMap watermill, 190 Grist Mill Lane (nom.py).',
 'castle-gould-hempstead-house':'OpenStreetMap point for Castle Gould (nom.py); Hempstead House is about 500 m north-west.',
 'raynham-hall-oyster-bay':'OpenStreetMap point, West Main Street (nom.py); matches the Wikipedia point.',
 'oyster-bay-station-turntable':'OpenStreetMap point of the station museum, 1 Railroad Avenue (nom.py); the Register point for the depot is 1.3 km north and wrong.',
 'planting-fields-main-house':'OpenStreetMap point for Coe Hall (nom.py).',
 'sagamore-hill-roosevelt':'OpenStreetMap museum point, 10 Sagamore Hill Road (nom.py), on the house on the aerial. The lot point was moved with pix.py from a small building onto the lot.',
 'matinecock-friends-meetinghouse':'OpenStreetMap place of worship, 267 Duck Pond Road (nom.py).',
 'jericho-friends-meeting-house':'OpenStreetMap place of worship on Old Jericho Turnpike (nom.py).',
 'westbury-house-old-westbury-gardens':'OpenStreetMap building, Westbury House, 71 Old Westbury Road (nom.py).',
 'fort-totten-willets-point':'OpenStreetMap building tagged historic=fort on the point (osmnear.py); the LiDAR sheet shows the long fort wall with its row of bays right under the pin. The federal public-land map puts this ground in a Coast Guard station; NYC Parks says rangers lead tours of the fortress, so the boundary there was not settled.',
 'new-york-state-pavilion':'Moved with pix.py from the Wikipedia point (on the Theaterama side) to the middle of the Tent of Tomorrow ring seen on the aerial; the towers are just west.',
}
