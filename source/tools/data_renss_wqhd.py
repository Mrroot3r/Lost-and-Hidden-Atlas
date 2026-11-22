# November 22, 2026: southern and western Rensselaer County (East Greenbush, North Greenbush, Schodack, the City of
# Rensselaer, Sand Lake and the Alps in Nassau), with Valley Falls in the north and the North Chatham depot just over
# the Columbia County line. Drawn at random by tools/choose.py --state ny (region renss, 66 places). Mostly leads that
# earlier Rensselaer sessions left (Staats house, Van Alen home, Sharpe homestead, Smith Boughton's house, the Arlington
# Hotel, Valley Falls), plus the one surviving building of the War of 1812 Greenbush Cantonment, Citizen Genet's
# churchyard, a brewery-turned-shoddy mill and two Hudson River railroad bridges. Sources opened in this session:
# Wikipedia as raw text (tools/wiki_raw.py), HMdb marker pages, the Valley Falls Historic District Register form (text
# layer read), the Town of East Greenbush historic-sites legend and cantonment slide show, the Town of North Greenbush
# historian's column, the NYS Military Museum's fort page, the Sand Lake Historical Society's marker page and newsletter,
# NYSDEC's Barnet Mills brownfield papers, NYS Parks' Schodack Island page, the I LOVE NY listing for the Papscanee
# preserve and two news pages on the Livingston Avenue Bridge replacement.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def HM(n,t): return L('HMdb: '+t,'https://www.hmdb.org/m.asp?m='+n)
BATCH={'key':'renss_wqhd','label':'Rensselaer County: Greenbush, Schodack, Sand Lake and the river bridges','added':'2026-11-22 01:38'}
EGLEG=L('Town of East Greenbush: historic sites legend (Natural Resources Inventory map 25, PDF)','https://cms2.revize.com/revize/eastgreenbushny/Documents/Departments/Planning%20&%20Zoning/Natural%20Resources%20Inventory/25_-_Historic_Sites_Legend.pdf')
CANT=L('Town of East Greenbush historian: An injustice at Greenbush Cantonment (PDF)','https://cms2.revize.com/revize/eastgreenbushny/Documents/Departments/Historian/An%20injustice%20at%20Greenbush%20Cantonment%20use.pdf')
DMNA=L('NYS Military Museum: Greenbush Cantonment','https://museum.dmna.ny.gov/forts/greenbush')
NGWAR=L('North Greenbush Notes: Greenbush in the War of 1812 (PDF)','https://townofng.com/sites/default/files/2024-05/NGN_20120605_GreenbushInTheWarOf1812.pdf')
BLOG1812=L('War of 1812 bicentennial blog: Greenbush Cantonment, part 3','https://warof1812bicentennialblog.blogspot.com/2023/01/greenbush-cantonment-part-3.html')
SLHS=L('Sand Lake Historical Society: historical markers','https://sandlakehistory.org/markers.htm')
CALICO=L('Sand Lake Historical Society, Historical Highlights 25-3: Smith Boughton and his house (PDF)','https://www.sandlakehistory.org/historical-highlights/back-issues/HH25-3.pdf')
BCP=L('NYSDEC: Former Barnet Mills brownfield fact sheet, December 2023 (PDF)','https://extapps.dec.ny.gov/data/der/factsheet/c442065riwp.pdf')
BCPA=L('NYSDEC: Former Barnet Mills brownfield application, 2022 (PDF)','https://extapps.dec.ny.gov/data/DecDocs/C442065/Application.BCP.C442065.2022-10-27.Complete%20BCP%20Application%20.pdf')
SCHOD=L('NYS Parks: Schodack Island State Park','https://parks.ny.gov/visit/state-parks/schodack-island-state-park')
LIVRN=L('Railway News: Livingston Avenue Bridge replacement, 2026 update','https://railwaynews.net/livingston-ave-railroad-bridge-replacement-project-albany-county-ny.html')
PAPS=L('I LOVE NY: Papscanee Island Nature Preserve','https://www.iloveny.com/listing/papscanee-island-nature-preserve/12677/')
VFNR=L('National Register nomination: Valley Falls Historic District (text)','https://npgallery.nps.gov/NRHP/GetAsset/NRHP/100003118_text')
PLACES=[
N('greenbush-cantonment-officers-quarters','Greenbush Cantonment officers\' quarters (War of 1812)','East Greenbush','renss','fort','standing',42.62304,-73.72370,'site','view','drive','forts','1812–1831',
  'In 1812 the federal government bought about 400 acres near Greenbush and built the headquarters of the Army\'s Northern Division: barracks for over 4,000 men, officers\' quarters, a 100-bed hospital, an arsenal, armory, magazine, stables and guard houses. It was declared surplus in 1819, a few troops stayed on, and in May 1831 the government sold the land to Hathorne McCulloch, who made his house in one of the officers\' quarters. Every other building was taken down; the salvaged timber went into the Greenbush and Schodack Academy and the McCulloch House of 1843. The town historian\'s slide show also tells of the 1814 execution of Private Samuel Helms here for desertion.',
  'One wooden officers\' quarters is all that is left of the cantonment, now a well-kept private house at 250 McCullough Place; the Red Mill School stands on the old parade ground. Seen only from the street. Interior not checked.',
  'The last barracks of an army of 4,000.',
  'Private house: look from the public street only. The town and state sources call it the one surviving building; none says whether it can be seen well from the road. No parking area; the street is residential.',
  [EGLEG,CANT,DMNA,NGWAR,BLOG1812],conf='mixed',brick='?',hours=''),
N('greenbush-reformed-church-genet','Greenbush Reformed Church and Citizen Genet\'s grave','East Greenbush','renss','worship','standing',42.58837,-73.69990,'exact','view','drive','cemeteries','1861 (congregation 1787)',
  'The Reformed congregation of Greenbush was founded in 1787, and this 1861 church on the Columbia Turnpike is the third building on the site. In the churchyard behind it is buried Edmond-Charles Genet, "Citizen Genet", the French envoy whose 1793 mission caused a crisis with Washington\'s government; he stayed in America, farmed at Prospect Hill two miles west, and died in 1834. A 1949 state marker in front of the church points to the grave.',
  'The 1861 church, still a Reformed congregation, and the family burial ground of the Genets behind it. Interior not checked; no page of the church\'s own was found.',
  'Where the man who nearly started a war with Washington ended up.',
  'Active church on US 20 (Columbia Turnpike) at Hays Road; the marker is by the sidewalk in front. No service times were found on a page of the church\'s own (only directories), so it is marked view only. Visit the churchyard with respect and outside services.',
  [EGLEG,W('Edmond-Charles Genêt'),HM('138138','Citizen Genet')],brick='?',hours=''),
N('van-alen-house-defreestville','John Evert Van Alen House','Defreestville','renss','landmark','standing',42.65426,-73.69796,'site','view','drive','','1793–1794',
  'John Evert Van Alen bought a 400-acre tract here in 1778 and built this house in 1793–94, while he sat in Congress (1793 to 1799). It is a two-story, five-bay Federal frame house with a two-story wing of about 1840 to 1854; an L-shaped barn and the Van Alen family burial ground are on the property. It was listed on the National Register in 2004.',
  'Clapboarded Federal house with its later wing and barn; a 1932 state marker stands on Washington Avenue in front. Interior not checked.',
  '',
  'Private house at 1745 Washington Avenue, just east of NY 43: look from the road only.',
  [W('John Evert Van Alen House'),HM('145274','Van Alen Home')],brick='?',hours=''),
N('blooming-grove-reformed-church','Blooming Grove Reformed Church','Defreestville','renss','worship','standing',42.65282,-73.69679,'exact','view','drive','','1925 (congregation 1814)',
  'Farm families of Blooming Grove, now Defreestville, had worshipped across the river in Albany and then at Wynantskill before forming their own Reformed congregation late in 1814. Their first church was finished in January 1817 and replaced in 1867; that one burned on New Year\'s Eve 1910, saving only the communion ware and the steeple bell. With money short and the First World War in between, the present sanctuary was not dedicated until April 1925, the third building on the site.',
  'The 1925 church, still a Reformed congregation, with a 1960s education wing and parsonage. Whether the old bell hangs in the new steeple is not said in the sources read. Interior not checked.',
  '',
  'Active church at 706 Bloomingrove Drive, just south of Washington Avenue; a town marker stands by the road. No service times were found on a page of the church\'s own, so it is marked view only.',
  [L('North Greenbush Notes: Happy Birthday Blooming Grove Reformed Church (PDF)','https://townofng.com/sites/default/files/2024-05/Happy-Birthday-Bloomingrove-Reformed-Church.pdf'),HM('145275','Blooming Grove')],brick='?',hours=''),
N('smith-boughton-calico-house','Big Thunder\'s house (Dr. Smith Boughton\'s Calico House)','Alps','renss','landmark','standing',42.59562,-73.50950,'exact','view','drive','','1799–1810 (estimated)',
  'Dr. Smith Boughton, who led the tenants of the Van Rensselaer manor as "Big Thunder" in the Anti-Rent War of the 1840s, lived in this modest house on NY 43 from 1838 to 1888. Its owners in the Sand Lake Historical Society\'s newsletter called it the Calico House after the calico disguises of the anti-rent "Indians"; a restoration expert put its building at between 1799 and 1810. They also wrote that it was said to have been an Underground Railroad stop, which no source opened here confirms.',
  'A small early house with a big stone fireplace inside (owners\' account); a marker "Home of \'Big Thunder\'" stands in the front yard. Interior not checked.',
  'The house of the man who led the tenants against the patroons.',
  'Private house at 2093 NY 43, near Alps Mountain Road: look from the road. The marker is on the shoulder side of the yard.',
  [CALICO,HM('315226','Home of Big Thunder'),HM('145270','Big Thunder')],brick='?',hours=''),
N('arlington-hotel-west-sand-lake','Arlington House (former Arlington Hotel, trolley stop 22)','West Sand Lake','renss','hotel','standing',42.64573,-73.59460,'exact','view','drive','hotels','1895–1925 (trolley stop)',
  'The Arlington Hotel, first called the Elkhorn, was stop 22 on the Troy & New England Railway, the electric trolley that ran nine miles from the Albia section of Troy to Averill Park from 1895 to March 31, 1925. It is one of the few buildings left from the line. A 2024 Pomeroy Foundation marker stands in front; the person who sent the marker to HMdb wrote that the place, now the Arlington House, was still in business in 2024.',
  'The old roadside hotel on NY 43 with its trolley marker. Whether it still serves and when was not checked: no page of its own was found.',
  '',
  'At 3532 NY 43. A private business; this batch found no page of its own with hours, so check before going.',
  [HM('284354','Arlington Hotel')],conf='mixed',brick='?',hours=''),
N('barnet-mills-rensselaer','William Barnet & Son shoddy mill (Barnet Mills)','Rensselaer','renss','industry','standing',42.65823,-73.73433,'site','view','walk','','1873–1977',
  'The mill complex on Forbes Avenue began as a brewery, the Stroebel malt house, in the late 1800s (the site\'s brewery and mill use is dated from 1873). From 1905 to 1977 the William Barnet Company ran it as a shoddy mill, reclaiming wool scraps from textile mills for reuse. After the 1960s the buildings were rented to artists, musicians, a photographer, a garage and small factories. Listed on the National Register in 2020 (four contributing buildings). In 2023 the site was vacant, in the state brownfield program, with plans to rehabilitate the buildings as apartments and shops.',
  'Red brick and white-painted mill blocks along the railroad (Commons photograph); several empty buildings, old foundations and debris piles (state fact sheet, December 2023). Whether work has begun was not checked.',
  'From beer to old wool to lofts.',
  'Private, vacant and under brownfield cleanup: look from Forbes Avenue or from the city\'s Hilton Park and boat ramp, which the brownfield papers place just west of it. Do not enter.',
  [BCP,BCPA,L('City of Rensselaer: brownfield public notice, Former Barnett Mills','https://rensselaerny.gov/news/public-notice-brownfied-cleanup-program-site-name-former-barnett-mills')],brick='some',hours=''),
N('livingston-avenue-bridge','Livingston Avenue Bridge (1902 swing bridge)','Albany','alb','rail','standing',42.65431,-73.74178,'site','view','walk','','1866; 1901–1902',
  'The first railroad bridge across the Hudson at Albany, the Hudson River Bridge, opened in 1866; the present bridge was built on its piers in 1901–02, with a swing span that turns to let ships pass. It carries Amtrak\'s Empire Corridor between Albany-Rensselaer station and the west, and freight. Worn out, it lets one train cross at a time at 15 mph. In 2024 Skanska was chosen to build a two-track replacement with a vertical lift span just south of it, and a path for walkers and cyclists; trains stay on the old bridge until the new one is finished, planned for 2028, after which the 1902 bridge is to go.',
  'The old swing span on its 1866 piers, with the new bridge rising beside it. See it while it lasts.',
  'The last years of the Hudson\'s oldest railroad crossing at Albany.',
  'Active railroad: never walk on the tracks. Seen from the Albany shore in the Corning Preserve (city park land, per the federal public-land map), or from the Rensselaer bank; the old walkway on the bridge is closed. Hours of the preserve not checked.',
  [W('Livingston Avenue Bridge'),LIVRN],brick='?',hours=''),
N('alfred-h-smith-bridge','Alfred H. Smith Memorial Bridge (Castleton Cut-Off)','Castleton-on-Hudson','renss','rail','standing',42.5087,-73.775,'site','view','walk','','1921–1924',
  'Built in 1921–24 for the New York Central\'s Castleton Cut-Off, which took freight around the bottleneck at Rensselaer, and named for the railroad\'s president Alfred H. Smith, who died after a riding fall in Central Park in 1924, the year it opened. The steel trusses came from Bethlehem Steel\'s McClintic-Marshall. Since the Poughkeepsie bridge burned in 1974 it has been the southernmost rail freight crossing of the Hudson, owned today by CSX.',
  'The long steel truss bridge high over the river and Schodack Island. Its piers and trusses can be seen from the state park on the island below.',
  '',
  'CSX freight line: no access to the bridge. Seen from Schodack Island State Park (open all year, dawn to dusk; vehicle fee in season; NYS Parks page), whose lots are about 1 km south of the bridge.',
  [W('Alfred H. Smith Memorial Bridge'),SCHOD,W('Schodack Island State Park')],th=[42.50035,-73.77410],thn='Schodack Island State Park lot',brick='?',hours=''),
N('joachim-staats-house','Joachim Staats House and the Gerrit Staats house site','Schodack','renss','landmark','standing',42.57045,-73.74988,'site','view','walk','','1696',
  'A two-story stone house of 1696 on Papscanee Island (now joined to the shore), with a brick addition of about 1790 and a wood one of about 1880. The Staats family seat Hooghbergh was here from the 1600s; brothers Gerrit and Jochem Staats lived on the island in the 1700s, and Jochem was known to river travellers as a host. The 1758 Gerrit Staats house burned in 1973 and nothing of it shows. As of 2012 the house was still owned by a family company, nine generations having lived in it.',
  'One of the oldest houses in New York, by the river at the end of the lane. The red-roofed house shows on the leaf-off aerial. Whether it can be seen from the preserve\'s trails was not checked.',
  'Nine generations in one 1696 house.',
  'Private family property: do not go up the lane. The Papscanee Island Nature Preserve around it is open free, dawn to dusk every day; its lot is off Staats Island Road from NY 9J (I LOVE NY listing).',
  [W('Joachim Staats House and Gerrit Staats Ruin'),PAPS,L('NYS Museum (Bielinski): the Staats family','https://exhibitions.nysm.nysed.gov//albany/bios/s/staats.html')],th=[42.57280,-73.74740],thn='Papscanee preserve lot (Red trail)',brick='?',hours=''),
N('north-chatham-depot','North Chatham depot and substation (Albany & Hudson)','North Chatham','hud','rail','standing',42.47529,-73.63363,'site','view','drive','stations','1900',
  'Built in 1900 on the Albany & Hudson, the first American interurban run by an electrified third rail (1900 to 1929). It was both a passenger depot, with a waiting room, freight doors and a bay window on the tracks, and one of three brick substations where 12,000-volt power from Stuyvesant Falls was turned into 600 volts for the rail; it is the only substation left, and the only one that was also a depot. It became a fire station in 1940, was restored in 2013, and houses the North Chatham Historical Society. It is in the North Chatham Historic District (2023).',
  'The restored red brick depot, with its deep eaves and bay window (Commons photograph), beside the Albany-Hudson Electric Trail, with the trail\'s interpretive panel. Interior and opening days not checked.',
  'The only third-rail substation left from America\'s first.',
  'The panel is at Depot Street; the trail is open ground. The building belongs to the historical society, which had no page with opening times that this batch could find.',
  [HM('197984','North Chatham Depot'),W('North Chatham Historic District'),HM('229846','Passenger and Freight Depots')],conf='mixed',brick='yes',hours=''),
N('valley-falls-historic-district','Valley Falls mill village','Valley Falls','renss','town','standing',42.8992,-73.5613,'area','public','walk','','1830s–1940',
  'A factory village that grew up around cotton mills on both banks of the Hoosic River in the early 1800s and boomed after James Thompson\'s linen mill opened in the early 1870s. The Schaghticoke bank is all houses, from owners\' to workers\'; the Pittstown bank has a brick Romanesque union school of 1893, a brick Gothic Catholic church of 1890, a buff brick Methodist church of 1923, a little stucco Arts and Crafts library of 1912, shops, a post office and the ruin of the last mill. The mill race now makes hydroelectric power. Listed on the National Register in 2018.',
  'Mill housing on both banks, the 1893 school and 1890 church on Charles Street, the 1912 library at Lyon and State Streets, the old railroad abutments over State Street, and a stone bridge abutment at the foot of Bunker Hill Road where wooden bridges stood from 1815. The Thompson mill ruin is its own entry.',
  '',
  'The village streets (NY 67, State Street, Charles Street) are public roads; the buildings are private homes, churches and a school: look from the sidewalks.',
  [VFNR],brick='some',hours=''),
]
PIN_NOTES={
'blooming-grove-reformed-church':'OpenStreetMap\'s mapped church at 706 Bloomingrove Drive (nom.py), 20 m from the town marker.',
'greenbush-cantonment-officers-quarters':'ArcGIS PointAddress for 250 McCullough Place, the address the War of 1812 blog gives.',
'greenbush-reformed-church-genet':'OpenStreetMap\'s mapped church (nom.py), 688 Columbia Turnpike, 12 m from the HMdb marker.',
'van-alen-house-defreestville':'ArcGIS PointAddress for 1745 Washington Avenue Extension, the marker\'s address.',
'smith-boughton-calico-house':'ArcGIS PointAddress for 2093 State Route 43, the marker\'s address.',
'arlington-hotel-west-sand-lake':'ArcGIS PointAddress for 3532 NY 43, the marker\'s address.',
'barnet-mills-rensselaer':'ArcGIS PointAddress for 20 Forbes Avenue, the Register and brownfield address. On the leaf-off aerial it falls in the cleared yard at the river end of the row of mill buildings along the tracks.',
'livingston-avenue-bridge':'Wikipedia point, on the bridge over the river.',
'alfred-h-smith-bridge':'Wikipedia point, on the bridge.',
'joachim-staats-house':'Moved with pix.py onto the red-roofed house by the river that the leaf-off aerial shows 56 m from the Wikipedia point.',
'north-chatham-depot':'HMdb position of the North Chatham Depot panel at Depot Street. On the leaf-off aerial the old trolley bed (now the trail) runs southwest from here with two buildings beside it; which one is the depot was not made out, so the pin stays on the panel.',
'valley-falls-historic-district':'Register list point for the district; area pin.',
}
