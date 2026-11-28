# November 28, 2026: a fourth scatter of places across British Columbia, claimed with tools/choose.py --thinnest (bc had
# 63 places). Twelve places from the Canadian Register of Historic Places statements (historicplaces.ca): four in
# Victoria (the 1863 synagogue, the 1875 Carpenter Gothic church, St. Andrew's Cathedral, the Malahat Building), the
# Chinese cemetery at Harling Point in Oak Bay, St. Paul's Church on the Mission reserve in North Vancouver, Chilliwack's
# 1912 city hall, the 1911 Sikh temple at Abbotsford, the Church of the Holy Cross at Skatin, the Chee Kung Tong
# building in Barkerville, and the sites of two fur-trade posts (Kootenae House near Invermere and Fort Alexandria on the
# Fraser). Sources read in this session: the Register statements (each also gives the coordinate used), Wikipedia
# (tools/wiki_raw.py) for Kootenae House, and the pages of Church of Our Lord, St. Andrew's Cathedral and the Chilliwack
# Museum for hours. Nothing was checked on the ground.
from data_b import N
from data_ma import W
BATCH={'key':'bc_vqzk','label':'British Columbia: a fourth scatter','added':'2026-11-28 09:40'}

PLACES=[
N('church-of-our-lord-victoria','Church of Our Lord','Victoria','bc','worship','standing',48.4204,-123.3644,'exact','open','walk','','1875',
  'A wooden Gothic Revival church built in 1875 for the Reformed Episcopal Church after a schism in Victoria\'s Anglican diocese led by the Reverend Edward Cridge. The Register says it was designed by John Teague and built by Haywood and Jenkinson, and that it is one of the finest examples of Carpenter\'s Gothic on the West Coast: brick-and-stone Gothic forms translated into California redwood, with board and batten siding, corner pinnacles and a roof-top spire. A complementary annex, the Cridge Memorial Hall, was added in 1913 to a design by Samuel Maclure. It became a National Historic Site in 1990.',
  'From the street, the redwood board-and-batten walls, the rose window over the porch, the pinnacled buttresses and the spire. Inside, the Register lists a Gothic hammer-beam truss spanning the nave. Whether the nave can be entered outside services was not checked.',
  'A brick-and-stone Gothic church carved in wood.',
  'A working Anglican congregation at 626 Blanshard Street, downtown Victoria. Its own page gives services on Sundays at 8 and 10 a.m. and an office open Monday, Tuesday and Thursday 10 a.m. to 2 p.m. and Friday 10 a.m. to 1 p.m. (read November 28, 2026). Street and nearby paid parking, not checked.',
  [['Church of Our Lord (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=12642'],['Church of Our Lord','https://www.churchofourlord.ca/']],
  brick='no',bcol='none',hours='Services Sundays 8 and 10 a.m.; office Mon, Tue, Thu 10 a.m.–2 p.m., Fri 10 a.m.–1 p.m.',
  arch='John Teague; Samuel Maclure',builder='Haywood & Jenkinson',archw='Canadian Register statement: Teague designed the church (1875), Haywood & Jenkinson built it, Maclure designed the 1913 annex'),

N('congregation-emanu-el-victoria','Congregation Emanu-El','Victoria','bc','worship','standing',48.42732,-123.36157,'exact','open','walk','','1863',
  'The oldest synagogue building in Canada, built in 1863 just five years after the first Jewish settlers reached British Columbia, and still used as a synagogue. The Register describes a two-storey red brick building in the Romanesque Revival style, set back about two metres from the sidewalk on a prominent downtown corner, designed by the west coast architect John Wright. It became a National Historic Site in 1979.',
  'The pedimented central section between corner pavilions, with hipped roofs, and the well-kept interior detailing the Register lists. Inside: not checked beyond that.',
  'Canada\'s oldest synagogue, still in use.',
  'Owned and used by the congregation at 1461 Blanshard Street, at Pandora Avenue. Its own page would not open from here. A web search result quoting it said tours are offered by arrangement (summer 2019 tours ran Tuesday to Thursday noon to 1 p.m.; that may have changed), so hours are not checked: write or phone the office before going. Street and nearby paid parking, not checked.',
  [['Congregation Emanu-el Temple (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=11944'],W('Congregation Emanu-El (Victoria, British Columbia)')],
  brick='yes',bcol='red',hours='?',
  arch='John Wright',archw='Canadian Register statement: design by the west coast architect John Wright'),

N('st-andrews-cathedral-victoria',"St. Andrew's Roman Catholic Cathedral",'Victoria','bc','worship','standing',48.42553,-123.36193,'exact','open','walk','','1890–1892',
  'A twin-towered Gothic Revival cathedral designed in 1892 by Perrault and Mesnard of Montreal and built by the contractor J.H. Donovan. The Register calls it a fine example of the style, with French Gothic details: a triple entrance, a rose window over the doors, red brick walls with grey stone trim and a polychrome slate roof, and diaper-work panels on the front. It became a National Historic Site in 1990. The Register gives its construction as 1890 to 1892.',
  'The red brick and grey stone front with its asymmetrical towers and tall spire. Inside the Register lists ornamental vaulting, stained and coloured glass, decorative plaster and galleries.',
  'A red brick French Gothic cathedral with a polychrome roof.',
  'The Catholic cathedral at 740 View Street. Its own page lists Mass on Saturday at 9:30 a.m. and 5 p.m., Sunday at 9 and 11 a.m. and 5 p.m., and weekdays at 12:10 p.m., and says the church is open Monday to Friday 10 a.m. to 4 p.m. and Saturday and Sunday 8 a.m. to 6 p.m. (read November 28, 2026). Street and nearby paid parking, not checked.',
  [["St. Andrew's Roman Catholic Cathedral (Canadian Register of Historic Places)",'https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=13349'],["St. Andrew's Cathedral, Victoria",'https://www.standrewscathedral.com/']],
  brick='yes',bcol='red',hours='Church open Mon–Fri 10 a.m.–4 p.m., Sat–Sun 8 a.m.–6 p.m.; Mass Sat 9:30 a.m. and 5 p.m., Sun 9 and 11 a.m. and 5 p.m., Mon–Fri 12:10 p.m.',
  arch='Perrault and Mesnard',builder='J.H. Donovan',archw='Canadian Register statement: designed in 1892 by Perrault and Mesnard of Montreal, built by contractor J.H. Donovan'),

N('malahat-building-victoria','Malahat Building (Old Victoria Custom House)','Victoria','bc','civic','standing',48.4243,-123.36976,'exact','view','walk','','1874–1875',
  'A three-storey, mansard-roofed brick building of 1874 to 1875 on the Victoria harbour front, the customs house for the city from 1875 to 1899. The Register says mining licences for the Klondike gold rush were issued here and that it is a rare surviving example of a Second Empire federal building put up after Confederation, in the style of the first Chief Architect of the Department of Public Works, Thomas Seaton Scott. It became a National Historic Site in 1987.',
  'The mansard roof and brick walls from Wharf Street and the harbour side. Its brick colour, its present use and whether anything inside can be seen were not checked.',
  'A Gold Rush customs house in the Second Empire style.',
  'At 1002 Wharf Street. Who owns it now and whether the public may go in were not checked; look from the street. Street and paid parking nearby, not checked.',
  [['Malahat Building / Old Victoria Custom House (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=4225']],
  brick='?'),

N('harling-point-chinese-cemetery','Chinese Cemetery at Harling Point','Oak Bay','bc','burial','standing',48.4066,-123.32273,'site','view','walk','','1903–1961',
  'A cemetery on a sloping 3.5-acre point above the Strait of Juan de Fuca, founded in 1903 by the Chinese Consolidated Benevolent Association, which still owns and maintains it. It was used for private burials until 1950 and closed in 1961 when the remains of 849 Chinese pioneers, whose return to China had been blocked since 1937, were buried here. The Register says it keeps the largest group of Chinese burial features from before 1950 in Canada: about 300 headstones, 13 mass graves, two incinerator towers and an altar, all set by feng shui principles with no trees or straight paths. It became a National Historic Site in 1995.',
  'Open grass with tight rows of graves facing the water, the two incinerator towers and the altar platform, with the Olympic Mountains across the strait. It is a burial ground: keep to the paths and treat it with respect.',
  'Where Chinese pioneers were laid to face the sea.',
  'Owned by the Chinese Consolidated Benevolent Association, at Crescent Road and Penzance Street in Oak Bay. Whether it has posted visiting hours was not checked; look from the public edge unless the association says otherwise. Street parking, not checked.',
  [['Chinese Cemetery at Harling Point (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=9167']],
  brick='no',bcol='none'),

N('st-pauls-church-north-vancouver',"Saint Paul's Roman Catholic Church",'North Vancouver','bc','worship','standing',49.31589,-123.0880,'exact','open','walk','','1884–1910',
  'A Gothic Revival church with twin 26-metre spires on the Mission reserve of the Squamish Nation, on the north shore of Burrard Inlet. The Register says the reserve, set up in 1864, was the first permanent settlement in what is now North Vancouver and that the Oblates of Mary Immaculate built a chapel in the mid-1860s. The 1884 frame church was kept and rebuilt in 1909 with twin spires, transepts and round chapels, and reopened in 1910 named for Father Durieu. It is the last surviving mission church of that size in British Columbia and a National Historic Site (1980).',
  'The twin spires, wood clapboard and shingles, the wide wooden stair and Gothic arched windows, some with stained glass. Inside the Register lists original millwork and pews and two chancel columns from the 1884 church; whether visitors can enter was not checked.',
  'A twin-spired mission church, last of its size in the province.',
  'A parish church at 426 Esplanade West, on the Mission reserve, which is Squamish Nation land: be a considerate guest. Service times and whether it opens to visitors were not checked (hours not checked). Street parking, not checked.',
  [["Saint Paul's Roman Catholic Church (Canadian Register of Historic Places)",'https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=12683']],
  brick='no',bcol='none',hours='?'),

N('chilliwack-city-hall','Chilliwack City Hall (Chilliwack Museum)','Chilliwack','bc','civic','standing',49.16908,-121.95668,'exact','open','walk','','1910–1912',
  'A small Beaux-Arts civic building designed by the west coast architect Thomas Hooper and finished in 1912. The Register says it is the only Canadian municipal hall from before 1930 built entirely of reinforced concrete, with cast concrete walls painted white, banding that imitates cut stone, a pediment with a portico, paired columns, twin curved staircases and a ceremonial balcony. It once held police and court rooms as well as council, stopped serving as city hall in 1980 and now houses the Chilliwack Museum. A cenotaph of 1923 and a pair of copper beeches planted in 1915 stand in the grounds. National Historic Site, 1984.',
  'The white pedimented front with its paired columns and curved stairs, the war memorial and the old trees. The museum is inside.',
  'The only pre-1930 concrete city hall in Canada, now a museum.',
  'Home of the Chilliwack Museum and Archives. Its page says admission is always free and the museum is open Monday to Saturday 9 a.m. to 4:30 p.m. (Thursdays to 8 p.m. from April to August), closed on statutory holidays except Remembrance Day and Canada Day (read November 28, 2026). It gives the address as 48820 Spadina Avenue; the Register gives 45820. Parking, not checked.',
  [['Chilliwack City Hall (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=7408'],['Chilliwack Museum and Archives: plan your visit','https://www.chilliwackmuseum.ca/plan-your-visit']],
  brick='no',bcol='painted',hours='Mon–Sat 9 a.m.–4:30 p.m. (Thu to 8 p.m. April–August); closed statutory holidays except Remembrance Day and Canada Day; free',
  arch='Thomas Hooper',archw='Canadian Register statement: designed by Thomas Hooper'),

N('abbotsford-sikh-temple','Gur Sikh Temple (Abbotsford Sikh Temple)','Abbotsford','bc','worship','standing',49.05125,-122.30703,'exact','open','drive','','1911',
  'The oldest surviving Sikh temple in North America, opened in 1911 and used continuously since. The Register describes a simple rectangular wood-frame building with a gabled roof and a false front typical of Canadian commercial buildings, with a veranda along three sides of the upper floor. It holds the elements of a Sikh temple: a prayer hall upstairs, the room where the Guru Granth Sahib was kept, the Granthi\'s quarters, a communal kitchen and a dining area below. It became a National Historic Site in 2002.',
  'The false-front wood building on its hill, with the second-floor veranda and four doors into the prayer hall. It is a working temple: ask about visiting etiquette and tours before going in.',
  'North America\'s oldest surviving Sikh temple, in a plain wooden frame.',
  'A working gurdwara at 33089 South Fraser Way, on a one-acre lot at the crest of a hill. Its own pages would not open from here; a web search said its heritage site offers tours that can be booked, but no hours from an operator\'s page were read (hours not checked). Parking, not checked.',
  [['Abbotsford Sikh Temple (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=9358'],W('Gur Sikh Temple')],
  brick='no',bcol='none',hours='?'),

N('holy-cross-church-skatin','Church of the Holy Cross, Skatin','Skatin','bc','worship','standing',49.93622,-122.39685,'area','view','drive','','1905–1906',
  'A Gothic Revival mission church in wood in the Skatin (Skookumchuck) village of the Stl\'atl\'imx Nation, facing the Lillooet River. The Register says it was built by and for members of the community, in a mission church style of the Oblates of Mary Immaculate, with three slender octagonal spires over the front and cedar shingles on the roof. Inside it describes a highly decorated altar with a carved screen, a carved wooden dove, pews with carved ends and two carved confessionals, mixing European and First Nations motifs. A National Historic Site since 1981. The Register\'s construction date was not read, so none is given here.',
  'The three spires and white-painted siding from the village road. The interior is described in the Register, but whether visitors may enter was not checked.',
  'Three wooden spires in a remote Lillooet River village.',
  'In the village of Skatin, on First Nation land. Treat it as view-only and ask the community before going in: this is a living place of worship in a small village. The road in, parking and any opening times were not checked.',
  [['Church of the Holy Cross (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=7410']],
  conf='mixed',brick='no',bcol='none'),

N('chee-kung-tong-barkerville','Chee Kung Tong Building, Barkerville','Barkerville','bc','landmark','standing',53.06667,-121.51667,'area','open','walk','','1874–1877',
  'A two-storey board-and-batten building with two log lean-tos in the middle of Barkerville\'s Chinatown, built between 1874 and 1877 for the Chee Kung Tong, a Chinese benevolent society. The Register says it is a rare surviving example of the society\'s buildings in Canada: a hostel, kitchen and social room on the ground floor, a society hall and altar room above. It served Chinese miners and merchants of the Cariboo and is among the oldest buildings standing in Barkerville. National Historic Site, 2007 or 2008 (the Register gives both years).',
  'The plain wooden hall on the east side of the main street, in the Chinatown row. Inside, the Register describes the hostel, kitchen, hall and altar room; whether the building is open to visitors was not checked.',
  'A Chinese society hall from the Cariboo gold rush.',
  'In Barkerville Historic Town and Park, a provincial historic site; the town\'s visitor season and admission are on the Barkerville entry. The Register point sits at the middle of the town, not on this building, so the pin is the Chinatown area. Parking is the lot on the Barkerville Highway, not checked on the ground.',
  [['Chee Kung Tong Building (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=11971']],
  conf='mixed',brick='no',bcol='none',hours='?',
  apart='barkerville: the Chee Kung Tong building is its own National Historic Site, one building in the town'),

N('kootenae-house-site','Kootenae House site','Invermere','bc','fort','traces',50.52649,-116.04559,'site','public','walk','','1807–1812',
  'The site of the first fur-trading post in the Columbia Basin, built in 1807 by Jaco Finlay for the North West Company under David Thompson at the meeting of Toby Creek and the Columbia River, to trade with the Ktunaxa. Thompson used it as a base for exploring the upper Columbia until it was abandoned in 1812 after hostility from the Peigans east of Howse Pass. Its land was given to the Government of Canada in 1935, and the site became a National Historic Site in 1934. The Register says some above-ground remains and surface depressions mark where the fort stood on a terrace over the water. Parks Canada dug here in 2005 with Ktunaxa members, and signs were added in 2009 (Wikipedia).',
  'Hollows and low remains in open grass and Douglas fir on a terrace above Toby Creek, with signs telling the story. The historic site covers only about 0.77 acre.',
  'David Thompson\'s first post west of the Rockies.',
  'A Parks Canada site off Westside Road north of Invermere, said by the Register to be 0.77 acre. Hours, parking and the exact walk in were not checked; do not dig or collect anything here, it is an archaeological site.',
  [['Kootenae House (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=9614'],W('Kootanae House')],
  brick='no',bcol='none'),

N('fort-alexandria-site','Fort Alexandria site','Alexandria','bc','fort','gone',52.56278,-122.48111,'site','view','drive','','1821–1860s',
  'The site of the last trading post the North West Company built west of the Rockies, in 1821, on the west side of the Fraser River, named for Alexander Mackenzie, who had stopped at a First Nation village here in 1793. After 1826 it was where goods brought up from Fort Okanagan by pack train were moved to boats for the New Caledonia posts, until roads replaced the brigades in the 1860s. The Cariboo Wagon Road reached it in 1863. The Register says no above-ground remains are known; the site, 100 metres in radius, was fixed by archaeological survey in the late 1990s. National Historic Site, 1925.',
  'Open pasture beside the Fraser with views of the river; nothing of the fort shows. The Register lists the undisturbed pastureland and the view across the river as what matters.',
  'The last fur post west of the Rockies, now a field.',
  'On the west side of the Fraser near Alexandria, beside the Cariboo Highway. Who owns the pasture and any public way in were not checked; look from the highway and do not cross fenced land. No marker or parking was found.',
  [['Fort Alexandria (Canadian Register of Historic Places)','https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=17741'],W('Alexandria, British Columbia')],
  brick='no',bcol='none'),
]

PIN_NOTES={
'church-of-our-lord-victoria':'Register point; on the aerial it falls on a wooded block with a roof under trees at Blanshard Street, the church.',
'congregation-emanu-el-victoria':'Register point; on the aerial it sits on the corner building at Blanshard and Pandora. Brick colour is from the Register text.',
'st-andrews-cathedral-victoria':'Register point; on the aerial it falls on a long-roofed building with towers at the front, consistent with the cathedral.',
'malahat-building-victoria':'Register point, on the harbour front at Wharf Street; the aerial shows a roofed building there beside the water, so it is the building, not checked closer.',
'harling-point-chinese-cemetery':'Register point; the aerial shows a grassy headland above the water, matching the open-grass cemetery. The pin marks the cemetery, not a single feature.',
'st-pauls-church-north-vancouver':'Register point; on the aerial it falls on a building among trees and houses with a rail line to the west, which fits the church on the Mission reserve.',
'chilliwack-city-hall':'Register point; on the aerial it is on a pale building at a street corner beside a green park, the city hall and cenotaph grounds.',
'abbotsford-sikh-temple':'Register point; on the aerial it falls on a small building with a pale roof beside a parking lot on the hill. Not checked closer.',
'holy-cross-church-skatin':'Register point only. The aerial here is thin cloud and tree cover and the church cannot be picked out, so the pin marks the village area, not the building.',
'chee-kung-tong-barkerville':'The Register point is the middle of the town. On the aerial it falls in the Chinatown row of wooden buildings; which one is the Chee Kung Tong was not picked out, so the pin marks the area.',
'kootenae-house-site':'Register point, matching the Wikipedia coordinate. The aerial shows an open terrace beside a track and the creek; the hollows of the fort cannot be seen at this scale.',
'fort-alexandria-site':'Register point. The aerial shows pasture beside the river; nothing of the fort shows, as the Register says.',
}
