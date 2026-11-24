# November 24, 2026: Elmira, New York, from the names in one video that walks through the city's old buildings (the
# video is only a list of names to look up; nothing in these entries comes from it).
# Sources opened: Wikipedia as raw text (the Chemung County Register list, the Elmira Civic Historic District, Park
# Church, Erste Deutsche Evangelische Kirche, Elmira College and its Old Campus, Elmira Correctional Facility, the
# 30th Separate Company Armory), the Chemung County Historical Society's blog (City Hall), the Parish of the Most Holy
# Name of Jesus home page (Mass times), the Churches of Rochester pages for St. Patrick and Ss. Peter and Paul,
# railfanguides.us and elmira-ny.com (the Erie station), and the Library of Congress record of the Erie station survey.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
NRC=W('National Register of Historic Places listings in Chemung County, New York')
CIVIC=W('Elmira Civic Historic District')
STREET=' Street parking or a downtown lot nearby.'

BATCH={'key':'wny_qohv','label':'Elmira, NY: City Hall, churches, the college, the reformatory and the Erie station','added':'2026-11-24 14:32'}

PLACES=[
N('elmira-city-hall','Elmira City Hall','Elmira','wny','civic','standing',42.09159,-76.80302,'exact','view','walk','','1895–',
  'Elmira\'s City Hall was designed in 1895 by the local firm of Joseph Pierce and Hiram Bickford, who also drew the county courthouse buildings round the corner. Fire hit the upper floors in 1909; the damage was small and was soon repaired. It is a contributing building of the Elmira Civic Historic District, listed on the National Register in 1980. The Richardsonian Romanesque armory that stood a few doors along at 307 East Church Street lost its front in a windstorm in 2006 and was pulled down in 2010.',
  'A Beaux-Arts or Neo-Renaissance city hall (the sources use both words) in pale stone at Church and Lake Streets, with ornate decoration on the Lake Street front. The Chemung County Historical Society says the four buildings on the corners of Lake and Church were nicknamed Fascination, Salvation, Damnation and Procrastination, City Hall being Procrastination. Interior not checked.',
  'The corner Elmira called Procrastination.',
  'City of Elmira offices at 317 East Church Street; seen from the street. When the offices are open to the public was not checked.'+STREET,
  [CIVIC,L('Chemung County Historical Society: the corners of Lake and Church','https://chemungcountyhistoricalsociety.blogspot.com/search/label/*2022%20Walking%20Tour'),W('30th Separate Company Armory')],brick='no',hours=''),
N('park-church-elmira','Park Church','Elmira','wny','worship','standing',42.08902,-76.80872,'exact','view','walk','','1874–1876',
  'A congregation that left the First Presbyterian Church over slavery built this church in 1874–1876, replacing a much smaller wooden one. Horatio Nelson White designed it. Thomas Kennicott Beecher, brother of Harriet Beecher Stowe, was its pastor from 1854 until he died in 1900. It was listed on the National Register in 1977.',
  'A highly eclectic church of limestone and brick that runs the length of a whole city block, at 208 West Gray Street. Interior not checked; the congregation\'s own service times were not found.',
  'The Beecher family\'s abolitionist church, a block long.',
  'An active church at 208 West Gray Street; seen from the street. Service times not checked.'+STREET,
  [W('Park Church'),W('Thomas K. Beecher'),NRC],brick='?',hours=''),
N('erste-deutsche-kirche-elmira','Erste Deutsche Evangelische Kirche (First United Church of Christ)','Elmira','wny','worship','standing',42.09019,-76.79818,'exact','view','walk','','1898–1899',
  'Built in 1898 and 1899 for Elmira\'s large German American congregation, in the Rhenish Romanesque style. It is now the First United Church of Christ. The church and its parsonage were listed on the National Register in 2007.',
  'A Romanesque church with a tower at 160 Madison Avenue; the original German name is carved over the door. Interior not checked.',
  '',
  'An active church; seen from Madison Avenue. Its own page would not open when this was written, so service times are not checked.'+STREET,
  [W('Erste Deutsche Evangelische Kirche'),NRC],brick='?',hours=''),
N('st-patricks-church-elmira','St. Patrick\'s Church and its 1880s school and convent','Elmira','wny','worship','standing',42.09429,-76.81093,'exact','open','walk','','1873–',
  'St. Patrick\'s parish was formed in 1869 for Elmira\'s growing Irish Catholic population, and the church was built in 1873. Father James J. Bloomer was its pastor for 62 years, until 1932. A parochial residence, convent and school followed between 1884 and 1894; that group, with the school in the Second Renaissance Revival style, was listed on the National Register in 1992. Since 2018 it has been one of the two churches of Elmira\'s single Catholic parish, the Most Holy Name of Jesus.',
  'The red brick church with two spires at 604 Park Place, with the residence, convent and school of 1884–1894 beside it. Mass is said here, so the church can be seen inside then. Interior not checked.',
  '',
  'An active Catholic church; visitors may come to Mass. Times from the parish home page (elmiracatholic.org), which also lists weekday Masses at St. Mary\'s.'+STREET,
  [L('Parish of the Most Holy Name of Jesus','https://elmiracatholic.org/'),L('Churches of Rochester: St. Patrick, Elmira','https://packetduck.duckdns.org/churches/stpatrickelmira/'),NRC],brick='yes',
  hours='Sunday Mass 7:30 and 10:30 a.m.; Monday and Tuesday 8 a.m.'),
N('sts-peter-paul-church-elmira','Ss. Peter and Paul Church (closed)','Elmira','wny','worship','standing',42.09074,-76.79682,'exact','view','walk','','1857–2021',
  'Elmira\'s first Catholic parish, established by 1848 and possibly as early as 1834. The church on High Street was dedicated on July 19, 1857. In 2018 the parish was folded into the Most Holy Name of Jesus parish, and the church was closed in November 2021 because of falling attendance and income.',
  'The 1857 church at 161 High Street. The Churches of Rochester page shows its ceiling paintings, Stations of the Cross and stained glass from before it closed; what has become of them since is not checked.',
  'The city\'s oldest Catholic church, shut since 2021.',
  'Closed church; seen from High Street only. Who owns it now was not checked.'+STREET,
  [L('Churches of Rochester: Ss. Peter and Paul, Elmira','https://packetduck.duckdns.org/churches/ssppelmira/')],brick='?',hours=''),
N('elmira-college-old-campus','Elmira College Old Campus (Elmira Female College)','Elmira','wny','inst','standing',42.09642,-76.81635,'site','view','walk','','1855–',
  'Elmira College was founded in 1855 as a college for women, the first in the country to give women degrees on a par with men\'s. It took men in all its programmes from 1969. The historic core, listed on the National Register as the Elmira College Old Campus, holds Cowles Hall, Hamilton House, Gillett Hall, Carnegie Science Hall, Fassett Commons, Tompkins Hall, Hamilton Hall and Mark Twain\'s octagonal study.',
  'Victorian and Collegiate Gothic buildings round the green off Park Place and College Avenue. Interiors not checked.',
  'The first women\'s college with men\'s degrees.',
  'A private college campus; buildings seen from the streets and walks. The Mark Twain Study has its own entry.'+' Visitor parking at McGraw Hall on West 5th Street (OpenStreetMap).',
  [W('Elmira College Old Campus'),W('Elmira College'),NRC],brick='?',hours=''),
N('elmira-reformatory','Elmira Reformatory (Elmira Correctional Facility)','Elmira','wny','inst','standing',42.11497,-76.83084,'site','view','drive','','1876–',
  'Opened in 1876 as the Elmira Reformatory under Zebulon Brockway, who ran it on reform ideas with strict, military-style discipline and sentences that ended only when the warden judged a man ready. He was accused of brutal punishment in 1893 and retired in 1900; by then six other states had copied the Elmira system. It is now a maximum-security state prison known as "The Hill".',
  'An active prison on the hill north of the city, off Davis Street. Nothing can be visited.',
  'The reformatory that set a pattern for a dozen states.',
  'Operated by the New York State Department of Corrections and Community Supervision. Not open to visitors; seen only from the public road. Do not stop or photograph at the gates.',
  [W('Elmira Correctional Facility')],brick='?',hours=''),
N('erie-station-elmira','Erie Railroad station, Elmira','Elmira','wny','rail','standing',42.093514,-76.808328,'site','view','walk','stations','1895',
  'The Erie Railroad reached Elmira in 1849. A local postcard history says every railroad in town at first shared the Union Station, shown in an 1895 postcard, and that it soon became the Erie\'s station; it was closed to all passengers in the 1970s. A railfan guide says the Pennsylvania Railroad used it as well, its tower is gone, and it is the only one of Elmira\'s depots still standing. The Historic American Engineering Record documented it (survey HAER NY-36).',
  'The former station on Railroad Avenue by the elevated Norfolk Southern line, which used to be the Erie. Its building date was not confirmed. Present use not checked.',
  'The last of Elmira\'s depots.',
  'Ownership and present use not checked; seen from the street. Stay off the railway, which is active.'+STREET,
  [L('Railfan Guides: Elmira','https://railfanguides.us/ny/elmira/index.htm'),L('elmira-ny.com: old postcards','https://elmira-ny.com/images/PhotoAlbums/Postcards/index.shtml'),L('Library of Congress: Erie Railway, Elmira Station (HAER NY-36)','https://www.loc.gov/item/ny0497/')],conf='mixed',brick='?',hours=''),
]

PIN_NOTES={
'elmira-city-hall':'OpenStreetMap town-hall point for 317 East Church Street.',
'park-church-elmira':'ArcGIS PointAddress for 208 West Gray Street (the OpenStreetMap church point is 15 m away).',
'erste-deutsche-kirche-elmira':'ArcGIS PointAddress for 160 Madison Avenue (OpenStreetMap\'s First United Church of Christ point is 10 m away).',
'st-patricks-church-elmira':'ArcGIS PointAddress for 604 Park Place.',
'sts-peter-paul-church-elmira':'ArcGIS PointAddress for 161 High Street.',
'elmira-college-old-campus':'ArcGIS PointAddress for 1 Park Place, the college\'s address; the pin marks the old campus, not one building.',
'elmira-reformatory':'OpenStreetMap prison point (1879 Davis Street); the pin marks the prison grounds.',
'erie-station-elmira':'The position the railfan guide gives for the former Erie depot.',
}
