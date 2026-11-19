# November 17, 2026: Washington County, New York (region 'wash'), four places that complement data_washco.py and data_washco2.py.
# Two sessions worked this county at the same time; this batch keeps only what the other's batches (data_washco.py:
# canal locks, Skene Manor, covered bridges; data_washco2.py: the Feeder Canal, Eagleville) lack: the raised hull of the War of 1812 schooner
# Ticonderoga at Whitehall, the Knapp estate carriage roads at Shelving Rock, the Susan B. Anthony childhood house
# and the William Miller farm with Ascension Rock.
# Facts come from the linked sources only: Wikipedia read as raw text (tools/wiki_raw.py); HMdb marker pages, the
# DEC Lake George Wild Forest page, the Adventist Heritage Ministries page, the Skenesborough Museum friends' page, a
# 2020 Glens Falls Business Journal article, the Bike It or Hike It trail log, Northern New York Waterfalls and a
# hiking blog through tools/page.py. Where sources disagree the text gives both; where a source is silent the entry
# says "not checked". Nothing here was checked on the ground.
# Pins: an HMdb marker position, a Wikipedia
# coordinate, or a parking lot as OpenStreetMap maps it (tools/parking.py), as each pin note says. Every pin was
# looked at with tools/pincheck.py --lidar (research/pincheck_washco3_*.jpg).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'washco3','label':'Washington County, NY: Ticonderoga hull, Anthony house, Miller farm, Shelving Rock','added':'2026-11-17 17:55'}
BIKE=L('Bike It or Hike It: Champlain Canalway Trail, Fort Edward to Whitehall','https://bikeitorhikeit.org/champlain_canalway_trail_fort_edward_fort_ann_whitehall.htm')
TICM=L('HMdb: U.S.S. Ticonderoga','https://www.hmdb.org/m.asp?m=89671')
SKMUS=L('Skenesborough Museum (site run by friends of the museum)','https://skenesborough.com/skenesborough-museum/')
GFBJ=L('Glens Falls Business Journal (Sept. 2020): state plan to fix the Anthony home','https://www.glensfalls.com/glensfallsbusinessjournal/2020/09/state-has-plan-to-fix-home-of-suffragette-susan-b-anthony-in-washington-county')
AHM=L('Adventist Heritage Ministries: historic sites','https://adventistheritage.org/?p=1508')
MILLCH=L('HMdb: William Miller Chapel','https://www.hmdb.org/m.asp?m=58227')
DEC=L('DEC: Lake George Wild Forest','https://dec.ny.gov/places/lake-george-wild-forest')
NNYW=L('Northern New York Waterfalls: Shelving Rock Falls','https://www.nnywaterfalls.com/shelvingrockbrook/shelvingrockfalls')
SKIER=L('The Saratoga Skier and Hiker: Shelving Rock Mtn (2016)','https://saratogaskier.blogspot.com/2016/05/shelving-rock-mtn-05212016.html')
PLACES=[
N('uss-ticonderoga-hull','Hull of the USS Ticonderoga (1814)','Whitehall','wash','landmark','ruins',43.55272,-73.40277,'site','public','walk','','1814–1825',
  'Built as a merchant steamer at Vergennes, Vermont, in 1814, bought by the Navy and turned into a schooner, the Ticonderoga fought in Macdonough\'s squadron at the Battle of Plattsburgh on September 11, 1814, where she forced the sloop Chubb aground and helped take the Finch. After the war she was laid up at Whitehall and sold as not worth repairing in 1825. Her hull sank in East Bay and was found in 1958; the marker says it was raised that year, Wikipedia the year after.',
  'The wooden remains of the hull in an enclosure behind the marker, beside the Skenesborough Museum in the waterfront park.',
  'A War of 1812 warship\'s bones, sitting in a village park.',
  'In Whitehall\'s waterfront park beside the Skenesborough Museum (Skenesborough Drive). The museum was founded in 1959; the only hours found are for 2021 (Friday and Saturday, 10 to 4) on a site that says it cannot speak for the museum, so hours were not checked. Who owns the park was not checked (Washington County is not in the state parcel file).',
  [W('USS Ticonderoga (1814)'),TICM,SKMUS,BIKE],th=[43.55401,-73.40260],thn='Skenesborough Drive lot'),
N('susan-b-anthony-childhood-house','Susan B. Anthony childhood house','Battenville','wash','landmark','standing',43.11048,-73.42282,'exact','view','drive','','1832–33',
  'Susan B. Anthony\'s father built this brick house in 1832–33 (Wikipedia gives 1832) after moving the family from Adams, Massachusetts, to run a cotton mill on the Batten Kill. She lived here from about 13 to 19, and the family lost the house in 1839 after the financial crash of 1837. The state parks office bought it at foreclosure in 2006, in disrepair, and in 2020 began a $695,000 stabilization of the roof, masonry and drainage.',
  'The two-storey brick house on NY 29 with its stone retaining wall and carriage barn. Its use after the 2020 stabilization was left undetermined, and its state today was not checked.',
  'Where the young Susan B. Anthony lived, and the house the state nearly lost.',
  'Owned by the state (Office of Parks, Recreation and Historic Preservation). Not open as a museum: look from NY 29. In 2020 the state agreed to buy the four-acre lot next door, with a former tavern, for future parking; whether that happened was not checked.',
  [W('Susan B. Anthony Childhood House'),GFBJ]),
N('william-miller-farm','William Miller farm, chapel and Ascension Rock','Hampton','wash','worship','standing',43.5954,-73.31243,'site','open','drive','','1815–1849',
  'The farm of William Miller, the Baptist preacher whose reading of Bible prophecy began the Millerite movement, from which the Seventh-day Adventists and Advent Christians grew. His house dates from 1815 and he built the chapel in 1848. On October 22, 1844, some of his followers gathered on a limestone outcrop here, Ascension Rock, to wait for the Second Coming. The chapel and the rock were listed on the National Register in 1975 and the farm added in 1994.',
  'The farmhouse, the 1848 chapel and the outcrop called Ascension Rock; the HMdb marker says several restored farm buildings can be visited.',
  'Where a crowd stood on a rock in October 1844 and waited for the end of the world.',
  'Owned as a historic site by Adventist Heritage Ministries, whose page lists the William Miller Farm (Whitehall, NY) as open all year. Hours and parking were not checked; the farm is on County Route 11.',
  [W('William Miller Farm'),MILLCH,AHM]),
N('shelving-rock-knapp-carriage-roads','Knapp estate carriage roads, Shelving Rock','Fort Ann','wash','hotel','traces',43.55550,-73.59846,'area','public','hike','','1902–1917',
  'George Knapp, whom the waterfall guide calls the founder of the Union Carbide Company, built an estate at Shelving Rock in 1902 and laid out carriage roads through it. His mansion burned in 1917 and the state later took the land into the Forest Preserve. A hiking blog says the carriage roads were built for Knapp\'s hotel on Log Bay; the two accounts differ on whether it was a hotel or a private estate.',
  'The old carriage roads, now trails: the Shelving Rock Mountain Trail climbs 610 feet in 1.7 miles from Day Use Parking Area #4 on switchbacked carriage road. Where the mansion stood was not found in any source read.',
  'A millionaire\'s Gilded Age roads, still carrying hikers above Lake George.',
  'Lake George Wild Forest, part of the Adirondack Forest Preserve (DEC): open year-round, free. In the Shelving Rock Special Management Area camping is only at designated sites or more than 500 feet from Shelving Rock and Dacy Clearing roads, and the Pines is day use only.',
  [NNYW,SKIER,DEC],conf='mixed',th=[43.55550,-73.59846],thn='Shelving Rock Day Use Parking Area #4'),
]
PIN_NOTES={
 'uss-ticonderoga-hull':"The HMdb position of the U.S.S. Ticonderoga marker; the hull is in the enclosure behind it. The leaf-off aerial shows a long narrow roofed structure at the pin and the LiDAR a raised rectangle beside it. Wikipedia's coordinate is 270 m north.",
 'susan-b-anthony-childhood-house':'Wikipedia coordinate (2835 NY 29) fell in the field west of the house; moved 21 m east onto the house on the leaf-off aerial with tools/pix.py. The federal public-land map names the lot Susan B. Anthony Childhood Home.',
 'william-miller-farm':'The HMdb position of the William Miller Chapel marker, on County Route 11 with a small building beside it on the leaf-off aerial. Ascension Rock and the farmhouse were not picked out. No parking point: none is mapped within 1.5 km.',
 'shelving-rock-knapp-carriage-roads':'Pin and trailhead are Day Use Parking Area #4 as OpenStreetMap maps it (Parking Lot #4, Shelving Rock Road), where the DEC page starts the Shelving Rock Mountain Trail. The leaf-off aerial shows only conifer tops; the LiDAR shows Shelving Rock Road just south of the pin. The carriage road climbs from here; area precision.',
}
