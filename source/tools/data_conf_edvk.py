# November 19, 2026: Green Island, Cohoes and Waterford, a fourth pass over region conf (drawn at random by
# tools/choose.py --state ny). Earlier batches (conf_simf, conf_biei, conf_kovn) took the old Champlain Canal, the
# Waterford village district, downtown Cohoes, Harmony Mills and Watervliet. This batch finishes two lead rows
# (St. Mark's in Green Island, now the town offices; the D&H Green Island branch bridges and William Moore House) and
# adds what the HMdb markers round Cohoes and Green Island point to that the Atlas lacked: the Troy & Schenectady's
# High Street platform, the Van Schaick burial plot, the Cataract House site at the falls, the Gibbonsville basin in
# Watervliet, the Beattie Machine Works, and two Waterford churches standing apart from the village pin.
# Sources opened in this session: Wikipedia as raw text (tools/wiki_raw.py); HMdb marker pages, the Spindle City
# Historic Society's 2023 downtown tour and its "Forgotten Railroads of Cohoes" article on preserve.org, the Times
# Union's "Sacred buildings' afterlives", the Village of Green Island's town page, the Episcopal Diocese of Albany's
# Grace Church page, the Waterford Historical Museum's 2009 walking tour, The Evangelist, GCatholic, catholicmasstime.org,
# the Governor's 2022 Register nominations release, gohistoric.com and Discover Albany, all through tools/page.py.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'conf_edvk','label':'Green Island, Cohoes markers and two Waterford churches','added':'2026-11-19 16:40'}
SCHS=L('Spindle City Historic Society: Historic Downtown Cohoes self-guided tour (2023)','https://www.spindlecity.net/Brochures/downtown%20sites%20brochure%202023.pdf')
RAIL=L('Spindle City Historic Society: The Forgotten Railroads of Cohoes, part 2 (Steve Lackmann)','https://preserve.org/spindle/The%20Forgotten%20Railroads%20of%20Cohoes%20-%20R&S2.htm')
WTOUR=L('Waterford Historical Museum: Walking Tour of the Village of Waterford (2009)','https://passageport.org/wp-content/uploads/2020/11/Water-fors-Walking-Tour-Brochure-2009.pdf')
GIM1=L('HMdb: Welcome to Green Island','https://www.hmdb.org/m.asp?m=255785')
GIM2=L('HMdb: Water Fire Iron / .7 Sq. Mi. / Age of Rail','https://www.hmdb.org/m.asp?m=256004')
PLACES=[
N('st-marks-green-island','St. Mark\'s Episcopal Church (Green Island Town Offices)','Green Island','conf','worship','standing',42.74151,-73.69106,'exact','open','drive','','1866–67',
  'A Gothic Revival stone church at 69–75 Hudson Avenue, with a two-storey brick rectory added in 1883–84; it was listed on the National Register in 1978. Wikipedia gives the building years as 1866–1867, while the village\'s 2024 marker on the Empire State Trail says it was built in 1886, so both are given. The parish is gone: the Times Union reported that the church was refitted to hold the village and town offices and the Green Island Power Authority, and the town\'s own page gives its offices as 69 Hudson Avenue.',
  'From the street (Wikipedia\'s description): a steep roof of patterned coloured slate with three steep dormers, three pointed Gothic windows and a rose window in the front gable, and a stone bell tower; the walls are stone trimmed with brick. A March 2010 Wikimedia Commons photograph opened in this session shows grey stone walls with red brick arches and bands, the rose window still filled with coloured glass, and the brick rectory beside it. Inside it is offices now; whether any church fittings or glass survive was not checked.',
  'A Gothic church that became a town hall.',
  'Town of Green Island offices, open to the public on weekdays; the town\'s page says to call first because hours may vary. Street parking on Hudson Avenue and nearby streets. Hours from villageofgreenisland.com/town, read November 2026.',
  [W('St. Mark\'s Episcopal Church (Green Island, New York)'),L('Times Union: Sacred buildings\' afterlives','https://www.timesunion.com/local/article/Sacred-buildings-afterlives-4323634.php'),L('Village of Green Island: Town offices','https://villageofgreenisland.com/town/'),GIM1],
  conf='mixed',brick='some',hours='Monday to Friday 9 a.m. to 12:30 p.m. and 1:30 to 4:30 p.m., closed holidays'),
N('black-bridge-green-island','The "Black Bridge" and the D&H Green Island branch','Green Island','conf','rail','standing',42.76141,-73.68754,'exact','public','walk','','1835 line; spans early 1900s',
  'The Rensselaer and Saratoga Railroad laid track across Van Schaick Island in 1835, and its bridge from Green Island to Troy, opened that year, was the first railroad crossing of the Hudson. The line north to Waterford needed bridges over three mouths of the Mohawk. After the Delaware and Hudson took over in 1871 it became the D&H Green Island branch; its bridges were rebuilt before the First World War by the American Bridge Company, and the last freights ran in the mid-1980s.',
  'The steel spans still stand. The one from the north end of Green Island to Van Schaick Island, the "black bridge", now carries the Empire State Trail (OpenStreetMap maps it as the Black Bridge Trail), with two village history panels at its south end. Of the other two, one carries cars to Peebles Island and the other, from Peebles Island to Waterford, stood stripped of track when the Spindle City article was written. Light rail of the old branch could still be seen then in the weeds in front of the Van Schaick Mansion; not checked now.',
  'Walk the 1835 railroad\'s route across a mouth of the Mohawk.',
  'Empire State Trail, a paved walking and cycling path open to the public; who owns the bridge itself was not checked. The off-road part begins at the end of Cannon Street in Green Island, where there is a third panel; street parking there. Trail hours not checked.',
  [RAIL,GIM2,GIM1,L('HMdb: Unique Urban Village / Resilient Factory Town / Ford','https://www.hmdb.org/m.asp?m=256010')],
  conf='mixed',th=[42.75839,-73.68816],thn='End of Cannon Street, Empire State Trail',brick='?'),
N('high-street-station-cohoes','High Street station platform, Troy & Schenectady Railroad','Cohoes','conf','rail','traces',42.77232,-73.70535,'exact','public','walk','','1903',
  'The Troy and Schenectady Railroad ran through Cohoes, crossing the Enlarged Erie Canal at High Street. Traffic grew so heavy after the Civil War that in 1903 a railroad bridge was built and High Street lowered to pass under it, and a new station went up at Younglove Avenue on the north side in place of the old depot on the south. Passenger service ended in the late 1920s, freight in the 1970s, and in 1981 the state bought the bed for the Mohawk-Hudson bike-hike trail.',
  'A passenger platform of the station, beside the trail at the east bend of Younglove Avenue, with a marker photographed in 2024. Nothing else of the station stands.',
  '',
  'Mohawk-Hudson Bike-Hike Trail (Empire State Trail), state-owned since 1981. Street parking on Younglove Avenue. Trail hours not checked.',
  [L('HMdb: High Street Station','https://www.hmdb.org/m.asp?m=255800')],
  brick='?'),
N('william-moore-house-cohoes','William Moore House (former YWCA)','Cohoes','conf','landmark','standing',42.77314,-73.69974,'exact','view','drive','','about 1874',
  'A Second Empire house of about 1874 built for William Moore, an Irish-born woollen and knitting manufacturer who was president of the Erie Knitting Mill and a founder of the Manufacturers\' Bank of Cohoes. Moore sold it to the Cohoes YWCA in 1892, and many of the young women who came from Canada to work in the mills stayed there; it was the YWCA until the 1980s.',
  'A 6,800-square-foot red brick house with its original ornate iron fence on three sides. The Spindle City tour says it has been restored and houses the Spiral Design Studio; interior not checked.',
  '',
  'Private; a business. Look from Mohawk Street. Street parking downtown.',
  [SCHS],
  conf='mixed',brick='yes'),
N('beattie-machine-works-cohoes','Beattie Machine Works','Cohoes','conf','industry','standing',42.77056,-73.7122,'exact','view','drive','','1896',
  'An 1896 building of a Cohoes maker of textile machinery, whose patents and machines, the state says, mattered to the textile trade at home and abroad; the firm fought noted patent cases and turned its works to war production in the first half of the twentieth century. It is an example of "slow-burn" mill construction, and was listed on the National Register in 2022.',
  'From the street at 24 Amity Street. What the building is used for now and its condition were not checked; interior not checked.',
  '',
  'Private; view from Amity Street. Owner not checked.',
  [L('Governor\'s office: 27 nominations to the State and National Registers (September 2022)','https://www.governor.ny.gov/news/governor-hochul-announces-27-nominations-state-and-national-registers-historic-places'),L('Go Historic: Beattie Machine Works','https://gohistoric.com/places/1729528')],
  conf='mixed',brick='?'),
N('van-schaick-burial-plot-cohoes','Van Schaick burial plot and Camp Van Schaick','Cohoes','conf','burial','marker',42.76888,-73.68632,'site','view','walk','','',
  'The first settlers of Cohoes, the Van Schaicks, owners of the Half Moon patent, are buried here near their house on Van Schaick Island; the state put up a marker in 1932. A second 1932 marker at the corner of Van Schaick Park marks Camp Van Schaick, where the Continental Army\'s Northern Department under Generals Schuyler and Gates camped from August 15 to September 8, 1777.',
  'The burial-plot marker, reached from Delaware Avenue, and the camp marker at the north-west corner of Van Schaick Park (Park Avenue and Myrtle Avenue). Whether gravestones can be seen was not checked.',
  '',
  'The markers stand by the street; the Van Schaick Mansion (DAR) is about 130 m south. Who owns the burial ground was not checked; stay on the street.',
  [L('HMdb: Van Schaick Burial Plot','https://www.hmdb.org/m.asp?m=7249'),L('HMdb: Camp Van Schaick','https://www.hmdb.org/m.asp?m=7665')],
  conf='mixed',brick='?'),
N('cataract-house-cohoes','Cataract House site, Cohoes Falls','Cohoes','conf','hotel','gone',42.78585,-73.70967,'area','public','walk','','1860–1912',
  'The Cataract House opened on a bluff above Cohoes Falls in 1860. Rebuilt and enlarged after a fire, it was run by William Gwynn from 1867 until 1912 and burned to the ground soon after. Its advertisements offered an observatory, gondolas on the pond, a billiard room with views of the falls and a ballroom for sleighing parties.',
  'Nothing of the hotel; an interpretive panel at Falls View Park shows its lithograph. The 70-foot falls are the reason to go.',
  'A vanished resort above the biggest falls east of Niagara.',
  'Falls View Park (Discover Albany\'s listing does not name the owner), reached on foot over a footbridge across the power canals from North Mohawk Street, beside the School Street hydro plant. Discover Albany says it is open in daylight from May through October, with off-street parking; read November 2026, not checked on the city\'s own page.',
  [L('HMdb: Sightseeing / Cataract House, Cohoes Falls','https://www.hmdb.org/m.asp?m=11612'),L('Discover Albany: Falls View Park','https://www.albany.org/listing/falls-view-park/2416/')],
  brick='?',hours='Daylight, May to October'),
N('gibbonsville-basin-watervliet','Gibbonsville basin and Erie Canal dry dock markers','Watervliet','conf','canal','marker',42.72423,-73.70305,'site','public','drive','canal','',
  'The original Erie Canal ran along what is now Second Avenue in Watervliet. The Watervliet Historical Society has marked the Gibbonsville boat basin, where cargo was loaded and unloaded; a dry dock for repairing canal boats below the waterline, which stood where the city\'s public works yard is now; and the 14th Street bridge, one of 16 bridges over the canal in the city.',
  'Three small markers along Second Avenue (Route 32) between 13th and 14th Streets. Nothing of the basin shows.',
  '',
  'City sidewalk on Second Avenue; street parking.',
  [L('HMdb: Gibbonsville Basin','https://www.hmdb.org/m.asp?m=276647'),L('HMdb: Erie Canal Drydock','https://www.hmdb.org/m.asp?m=276644'),L('HMdb: 14th Street Bridge','https://www.hmdb.org/m.asp?m=276655')],
  brick='?'),
N('st-marys-waterford','St. Mary of the Assumption Church','Waterford','conf','worship','standing',42.79141,-73.68105,'exact','view','drive','','early 1900s; parish 1843',
  'The Catholic parish of St. Mary was founded in 1843 and given to the Augustinian order in 1858, which still staffed it in 2018. Mass was said in the town hall and then the parish hall until the church was built in the early 1900s. Locally it is called the "cathedral of the north".',
  'A Gothic church of granite with a limestone front and stained glass windows, on the hill above Broad Street (The Evangelist, 2018). Interior not checked.',
  '',
  'Active parish church, 119 Broad Street. A Mass-times directory (catholicmasstime.org) lists Sunday Masses at 8 and 10:30 a.m. and Saturday at 4 p.m.; not checked on the parish\'s own page. Street parking.',
  [L('The Evangelist: St. Mary\'s, Waterford: small town, mighty parish (2018)','https://evangelist.org/news/2018/apr/06/st-marys-waterford-small-town-mighty-parish'),L('GCatholic: Church of St. Mary of the Assumption','https://gcatholic.org/churches/usa-02/18192'),L('catholicmasstime.org: St. Mary of the Assumption','https://catholicmasstime.org/church/st-mary-of-the-assumption/6603')],
  brick='no',hours='?'),
N('grace-church-waterford','Grace Episcopal Church','Waterford','conf','worship','standing',42.78995,-73.67906,'exact','view','drive','','1841 or 1867',
  'The parish was founded in September 1810. The Diocese of Albany says the present church was put up in 1841, after the July 1841 fire that burned the first one; the Waterford museum\'s walking tour says it was built in 1867 and rebuilt after a fire in 1929. Both are given. A parish hall, kitchen and guild room were added later.',
  'A Gothic church; the walking tour points to the parish house\'s pointed-arch windows and ribbed vaults. Interior not checked.',
  '',
  'Active parish, 34 Third Street, in the Waterford Village Historic District. Service times were not found on a page read. Street parking.',
  [L('Episcopal Diocese of Albany: Grace Church, Waterford','https://albanyepiscopaldiocese.org/grace-church-waterford-ny/'),WTOUR],
  conf='mixed',brick='?',hours='?'),
]
PIN_NOTES={
 'st-marks-green-island':'OpenStreetMap building "Green Island Town Hall", 69–73 Hudson Avenue; the ArcGIS PointAddress for 69 Hudson Avenue falls on it. The Wikipedia point is 50 m west.',
 'black-bridge-green-island':'OpenStreetMap bridge way "Black Bridge Trail" over the Mohawk mouth north of Green Island; the HMdb panels are about 140 m south at the bridge foot.',
 'high-street-station-cohoes':'HMdb marker position for High Street Station, at the east bend of Younglove Avenue on the trail.',
 'william-moore-house-cohoes':'ArcGIS PointAddress for 135 Mohawk Street, Cohoes.',
 'beattie-machine-works-cohoes':'ArcGIS PointAddress for 24 Amity Street (the address Go Historic gives); the Register list point is 42.7705, -73.7120.',
 'van-schaick-burial-plot-cohoes':'HMdb position of the Van Schaick Burial Plot marker; the Camp Van Schaick marker is about 200 m west at Park and Myrtle Avenues.',
 'cataract-house-cohoes':'HMdb position of the Cataract House panel in Falls View Park; the hotel stood on the bluff nearby, spot not found.',
 'gibbonsville-basin-watervliet':'HMdb position of the Gibbonsville Basin marker on Second Avenue; the dry dock and bridge markers are within 70 m.',
 'st-marys-waterford':'OpenStreetMap building "Saint Mary\'s Roman Catholic Church"; the ArcGIS point for 119 Broad Street fell on the building 30 m east, likely the rectory.',
 'grace-church-waterford':'OpenStreetMap building "Grace Episcopal Church"; the ArcGIS point for 34 Third Street fell 25 m south-east among the parish buildings.',
}
