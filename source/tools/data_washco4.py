# November 17, 2026: one place in Washington County, New York, kept from pull request #49.
# Three sessions were given "you choose" in the same hour and all took Washington County. #48, #50 and #51 were merged;
# #49 (another session's `data_washco.py`, 11 places) repeated ten of their places under the same file name and ids and
# was closed. This is its one place that the others did not have, copied as that session wrote and sourced it; the
# reviewer who moved it here looked at its pin and its parking point on the aerial and did not re-open its sources.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'washco4','label':'Washington County, New York: the bridge piers at Hudson Crossing','added':'2026-11-17 18:11'}
GUIDE=L('Lakes to Locks Passage: The Northern Inland Passage, Champlain Canal guidebook (PDF, 2019)','https://passageport.org/wp-content/uploads/2021/06/Champ-Canal-Guidebook-Interior-7.pdf')
GHOST=L('Wash Wild blog (2022): Ghost Bridges','https://wcny.blogspot.com/2022/08/ghost-bridges.html')
PLACES=[
N('hudson-crossing-bridge-piers','Trolley and railroad bridge piers at Hudson Crossing','Thomson','wash','rail','traces',43.11689,-73.57558,'area','view','walk','','1890s–1920s',
  'Two lines of piers cross the Hudson between the Northumberland Dam and the Dix Bridge. Hudson Crossing Park says the Greenwich and Schuylerville Electric Railroad was formed in 1895 and built a trolley bridge here, powered from a dam on the Battenkill at Middle Falls; the line passed to the Hudson Valley Railway, which ran from Greenwich to Thomson until 1928. A Washington County blogger dates the laid-stone trolley piers downstream to a line abandoned in 1909, and the concrete piers just upstream to a Greenwich and Johnsonville Railway bridge first used on August 5, 1903, later shared by steam trains and trolleys; another rail historian dates that bridge to 1901. The dates do not agree.',
  'Cut-stone and concrete piers in the river, seen from the Dix Bridge, an old road bridge now for walkers and bikes; the guidebook says the trolley bridge was 900 feet long. A hiker in 2015 found trolley abutments, ties and paper mill foundations on the Thomson shore; that ground was not checked and is not part of this entry.',
  '',
  'Hudson Crossing Park, on the island made by Champlain Canal Lock 5: open every day of the year from dawn to dusk, free. Park at its lot off County Route 42 and walk to the Dix Bridge.',
  [L('Hudson Crossing Park: Hudson Valley Railway wayside','https://www.hudsoncrossingpark.org/virtual-heritage-wayside-hudson-valley-railway'),
   L('Hudson Crossing Park','https://www.hudsoncrossingpark.org/'),GHOST,
   L('Rich\'s PedalPoint (2015): Thomson pulp and paper mill ruins','https://rc-pedalpoint.blogspot.com/2015/11/thomson-pulp-and-paper-mill-ruins-part.html?m=1'),
   L('Rich\'s PedalPoint (2015): abandoned railroad and trolley bridges, Schuylerville','https://rc-pedalpoint.blogspot.com/2015/11/abandoned-railroad-and-trolley-bridges.html'),GUIDE],conf='mixed',
  th=[43.11448,-73.57741],thn='Hudson Crossing Park lot, County Route 42'),
]
PIN_NOTES={
 'hudson-crossing-bridge-piers':'The Dix Bridge, read off the aerial with tools/look.py and tools/pix.py (OpenStreetMap maps it there too); the pin check shows the bridge across the ring. The piers stand in the river upstream, between the bridge and the Northumberland Dam, and were not picked out on the aerial. The trailhead tile shows the park\'s gravel lot.',
}
