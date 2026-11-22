# November 22, 2026: three places in Detroit, Michigan, taken from the names in one walk-through video of Detroit
# buildings that were torn down (the record is source/videos/20261106_rt2tQMGQuhw.md). Nearly every building the video
# names is gone; these three are what a reader can still go and see: the one standing church it names, the marble
# fountain that once stood in front of the old opera house, and the memorial gate of the Water Works Park whose tower
# the video shows. Sources read: Wikipedia, HistoricDetroit.org, the cathedral's own visit page, WXYZ news (August 2026)
# and a Waymarking page for the fountain's position.
from data_b import N
from data_ma import W

BATCH={'key':'detroit_wksl','label':'Detroit: what is left of a lost city','added':'2026-11-22 13:22'}

PLACES=[
N('cathedral-st-paul-detroit','Cathedral Church of St. Paul','Detroit','mi','worship','standing',42.35622,-83.06331,'exact','open','walk','','1907–',
  'The cathedral of the Episcopal Diocese of Michigan, on Woodward Avenue in Midtown. Its congregation, formed in 1824, was the first Episcopal and the first Protestant church in Michigan Territory, and worshipped downtown before this building. Ralph Adams Cram designed it, and it was built from 1907 of limestone by medieval methods, with no steel frame. Its bell tower was never finished. Henry Ford\'s funeral was held here in April 1947.',
  'Gothic pointed arches, wide stained-glass windows and carved tracery. The square stub where a tower was meant to rise is plain to see from Woodward. Open to visitors on Fridays (Open Cathedral, with docents) and at services; at other times the cathedral office arranges a visit by telephone. Free, donations welcome.',
  'The cathedral that never got its tower.',
  'The Episcopal Diocese of Michigan\'s cathedral, 4800 Woodward Avenue, next to Wayne State University. Enter from the parking lot off Cathedral Lane or by the front doors on Woodward. Hours from the cathedral\'s visit page; Evensong is not held in summer.',
  [W('Cathedral Church of St. Paul (Michigan)'),['Cathedral Church of St. Paul: visit us','https://detroitcathedral.org/visit/']],
  brick='no',
  hours='Open Cathedral Fridays 11 a.m. to 2 p.m.; Sunday 7:30, 8:15 and 11 a.m., Evensong 4 p.m. September to June; Wednesday 12:15 p.m.'),
N('merrill-fountain-palmer-park','Merrill Fountain','Detroit','mi','curio','standing',42.42091,-83.11027,'exact','public','walk','','1901–',
  'A white marble fountain in the Italian Renaissance style by Carrère and Hastings, given by Lizzie Merrill Palmer in memory of her father, the lumberman Charles Merrill. It first stood on Campus Martius downtown, in front of the old Detroit Opera House. When Woodward Avenue was widened it was moved to the south edge of Palmer Park. The dates differ: HistoricDetroit gives its dedication as July 16, 1901 and the move as 1925; Wikipedia says built in 1904 and moved in 1926.',
  'The marble basin and balustrade, with an arch carved with cattails and water lilies over a niche holding a marble turtle between two fish. It has been dry for more than 50 years and pieces have been stolen or broken. In 2024 and 2025 the city put money toward restoring it; a news report of August 2026 said it is to be restored and moved closer to Woodward at the park\'s southern entrance, with work hoped for in 2027, so it may be fenced off or gone from this spot.',
  'The downtown fountain that went to the park and ran dry.',
  'City of Detroit, Palmer Park, on the north side of Merrill Plaisance Street near Second Avenue. Park in the park\'s lot along Merrill Plaisance to the west. Park hours not checked: the city\'s Palmer Park page could not be opened when this was written.',
  [W('Palmer Park (Detroit)'),['HistoricDetroit.org: Merrill Fountain','https://historicdetroit.org/buildings/merrill-fountain'],['WXYZ: Merrill Fountain to be restored and relocated (August 2026)','https://www.wxyz.com/news/voices/detroits-historic-merrill-fountain-to-be-restored-and-relocated-at-palmer-park']],
  conf='mixed', th=[42.42077,-83.11119], thn='Palmer Park lot on Merrill Plaisance',
  brick='no', hours='?'),
N('hurlbut-memorial-gate-detroit','Hurlbut Memorial Gate','Detroit','mi','landmark','standing',42.36083,-82.98159,'exact','view','walk','','1894',
  'The grand entrance of Water Works Park, a limestone triumphal arch 132 feet long and over 50 feet high, by Herman A. Brede and Gustave Mueller. It was paid for from the estate of Chauncey Hurlbut, a grocer and long-serving president of the city\'s water board, who left his fortune to beautify the park in 1885. The park, opened as a public pleasure ground beside the pumping station, was closed in the World Wars and for good in 1951; it is sealed off today. Its 185-foot water tower with an observation deck, the park\'s great sight, was shut in 1945 and is gone.',
  'Three tiers of arches with stairways up to a terrace, carved garlands, water fonts and roundels, and a spread eagle on top. Hurlbut\'s statue in the central dome and the iron carriage gate are gone. Restored in 2007.',
  'A triumphal arch for a park nobody may enter.',
  'Detroit\'s water works, on East Jefferson Avenue at Cadillac Boulevard. The park behind the gate is closed to the public for the security of the water supply: see the gate from the Jefferson Avenue sidewalk. Street parking nearby, not checked on the ground.',
  [W('Hurlbut Memorial Gate'),['HistoricDetroit.org: Hurlbut Memorial Gate','https://historicdetroit.org/buildings/hurlbut-memorial-gate'],['HistoricDetroit.org: Water Works Park Tower','https://historicdetroit.org/buildings/water-works-park-tower']],
  brick='no'),
]

PIN_NOTES={
 'cathedral-st-paul-detroit':'OpenStreetMap\'s point for the cathedral; the street-address lookup for 4800 Woodward Avenue lands 25 m away on the same building.',
 'merrill-fountain-palmer-park':'Placed on the fountain\'s white marble seen on the aerial, 5 m from the position a Waymarking page gives. The parking point is the park lot seen on the aerial along Merrill Plaisance.',
 'hurlbut-memorial-gate-detroit':'OpenStreetMap\'s outline of the gate, which matches the Register coordinate.',
}
