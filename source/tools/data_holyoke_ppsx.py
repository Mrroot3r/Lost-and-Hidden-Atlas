# November 26, 2026: Holyoke, Massachusetts. A "videos" session (PROMPTS.md job 9): the names came from one video's
# look at old Holyoke (the record is source/videos/20220721_4JhhAg_5B3U.md); the video is a tip and nothing here rests on
# it. Sources read: Wikipedia (each article named in the links); the Holyoke Public Library's own history and hours pages;
# the City of Holyoke (City Hall hours, Anniversary Hill Park, the 2020 study of the armory); Holyoke Gas & Electric's
# fishway page; Historic Buildings of Massachusetts (the armory); WHDH (the armory's 2016 collapse); the Daily Hampshire
# Gazette (Scott Tower, November 30, 2025); Mount Holyoke College's archives guide to the architects of its buildings.
# Pins are OpenStreetMap points, each looked at on the aerial.
from data_b import N
from data_ma import W
BATCH={'key':'holyoke_ppsx','label':'Massachusetts: Holyoke, the Paper City','added':'2026-11-26 00:32'}

DT=' Downtown street parking and city lots are close by; their hours and fees were not checked.'

PLACES=[
N('holyoke-city-hall','Holyoke City Hall','Holyoke','pv','civic','standing',42.20657,-72.6075,'exact','open','walk','','1871–1876',
  'Holyoke\'s city hall, at 536 Dwight Street on the corner of High Street. Work began in 1871 to a Gothic Revival design by Charles B. Atwood; when his drawings ran late the design passed to Henry F. Kilburn in 1874, and the building was finished two years later for about $500,000. It has held the city\'s offices ever since, and was listed on the National Register in 1975.',
  'A big building of Monson granite with pointed-arch windows, buttresses, and a slate roof banded in red and green, under a tower about 220 feet tall. The tower clock has a Seth Thomas movement of 1877 and four faces of milk glass. Inside, stained glass windows by the Boston artist Samuel West light the stairs to the auditorium and the auditorium itself. On the corner of Dwight and High streets stands a granite temperance fountain of 1901 in the same Gothic manner.',
  'A Gothic city hall built for a mill city\'s workers, with a clock they could read from the street.',
  'Owned by the City of Holyoke and still its city hall; the building is open on weekdays, hours from the city\'s own directory page.'+DT,
  [W('Holyoke City Hall'),['City of Holyoke: city directory and City Hall hours','https://www.holyoke.org/city-directory']],
  brick='no',hours='Monday to Friday 8:30 a.m. to 4:30 p.m.; closed on holidays'),

N('holyoke-dam','Holyoke Dam (Hadley Falls Dam)','Holyoke','pv','water','standing',42.21342,-72.60234,'site','public','drive','','1895–1900',
  'A granite dam across the Connecticut River at the Great Falls between Holyoke and South Hadley, the third dam on the spot. The first, a timber crib dam of 1848, gave way in 1848; the second was finished in 1849 and powered the mills along the Holyoke canals for half a century. The present dam was begun in 1895 and its last stone laid on January 5, 1900. Holyoke Gas & Electric, the city\'s own utility, bought it and its power stations in 2001.',
  'A long curving wall of granite with the river pouring over it, seen from the County Bridge or the riverbank. At its Holyoke end the Robert E. Barrett Fishway lifts migrating fish over the dam in an elevator, and a glass viewing room lets the public watch them in spring. The dam and canals are an engineering landmark for the testing work done here on the Venturi meter and the Hercules turbine.',
  'The dam a whole city was laid out to use.',
  'Owned by Holyoke Gas & Electric. The dam can be seen at any time from the public road and bridge at its Holyoke end. The fishway, at 1-3 County Bridge, opens for a few weeks of the spring fish run (Wednesday to Sunday in past seasons) and was closed for the season when this was written; its page posts each year\'s dates. Group tours are booked through the same page.',
  [W('Holyoke Dam'),['Holyoke Gas & Electric: the Robert Barrett Fishway','https://www.hged.com/fishway']],
  brick='no',hours='Fishway only, for a few weeks of the spring fish run; dates posted each year on its page'),

N('holyoke-public-library','Holyoke Public Library','Holyoke','pv','civic','standing',42.20415,-72.61264,'exact','open','walk','','1902',
  'The city library, a neoclassical building of 1902 in a park between Maple and Chestnut streets, designed by the Holyoke architect James A. Clough, who also designed the summit houses on Mount Tom. The library corporation raised the money from the city\'s mill owners, among them William Whiting and William Skinner. A renovation by Finegold Alexander Architects restored most of the 1902 building and replaced its old glass and iron book-stack wing with a new addition; it reopened on October 28, 2013.',
  'A pale building of Indiana limestone and white glazed brick with a columned front facing Maple Street, and the 2013 wing behind it on Chestnut Street. Inside, most of the 1902 rooms were restored; the library has a local history room with its own hours.',
  '',
  'Run by the City of Holyoke; the entrance is at 250 Chestnut Street. Hours are from the library\'s own page; summer hours are shorter, and some summer Saturdays it is closed.'+DT,
  [W('Holyoke, Massachusetts'),['Holyoke Public Library: history of the library','https://www.holyokelibrary.org/Pages/Index/227278/history-of-the-library'],['Holyoke Public Library: hours','https://holyokelibrary.org/our-hours/']],
  brick='no',hours='September to May: Monday to Thursday 8:30 a.m. to 8:30 p.m., Friday and Saturday 8:30 a.m. to 4 p.m.; closed Sundays and holidays'),

N('scott-tower-holyoke','Scott Tower (Walter Scott Memorial Tower)','Holyoke','pv','landmark','standing',42.21216,-72.63766,'exact','public','walk','','1939–1940',
  'A round stone lookout tower about 55 feet tall in Anniversary Hill Park, built of stone dug from the hill and finished in 1940 (one source gives 1939). The park land was given from 1923 on to mark the city\'s fiftieth year, by Colonel Walter Scott among others, and the tower was used for blackout watches in the Second World War. Interstate 91 cut the park in two in the early 1960s, and the tower fell to graffiti and neglect until the city began restoring the park.',
  'A rough stone tower with a spiral stair to a lookout platform, on a stone terrace with steps. A new accessible trail to it was finished in 2024. The city planned new steps, a ramp and a new stair inside the tower in work from July 2026 to about May 2027, so parts may be fenced off for now.',
  'A wartime lookout tower in a park the interstate cut in half.',
  'Anniversary Hill Park is a City of Holyoke park, managed with the city\'s Office of Conservation and Sustainability. The new trails begin at the dead end of Overlook Drive, where there are parking spaces. Park hours were not found on the city\'s pages.',
  [W('Scott Tower'),['City of Holyoke: Anniversary Hill Park improvements','https://holyoke.org/phase-i-anniversary-hill-park-improvements-set-to-begin-in-holyoke'],['Daily Hampshire Gazette: Scott Tower park improvement project (November 30, 2025)','https://gazettenet.com/2025/11/30/holyokes-scott-tower-park-set-for-725k-improvement-project']],
  conf='mixed',brick='no'),

N('holyoke-armory-castle','Holyoke Armory, the "Castle" front','Holyoke','pv','fort','ruins',42.20287,-72.61811,'exact','view','walk','forts','1907',
  'A National Guard armory at 163 Sargeant Street, built in 1907 for the Massachusetts Volunteer Militia to a design by the Holyoke architect William J. Howe; its castle front was said to copy Hawarden Castle, the home of the British prime minister William Gladstone. In 1990 the county sheriff took it over to hold extra prisoners. It then stood empty, the city took it for unpaid taxes in 2013, and in 2016 the drill shed behind collapsed and was pulled down in an emergency demolition.',
  'The castle front with its towers is what is left. A study for the city found its three old outer walls could be kept but the floors and roof inside had collapsed in many places, and the building cannot be entered. Nothing later than that study, posted by the city in January 2023, was found on whether the front still stands.',
  'A castle front with nothing left behind it.',
  'Owned by the City of Holyoke, which has offered it to developers. It is unsafe and closed: look from Sargeant Street only.',
  [['Historic Buildings of Massachusetts: Holyoke Armory (1907)','https://mass.historicbuildingsct.com/?p=4875'],['City of Holyoke: Holyoke Armory study report','https://storage.googleapis.com/proudcity/holyokema/uploads/2023/01/Holyoke-Armory_Final-Study-Report.pdf'],['WHDH: emergency demolition of Holyoke armory (2016)','https://whdh.com/news/emergency-demolition-of-holyoke-armory-is-underway/']],
  conf='mixed',brick='yes'),

N('mary-lyon-hall-mount-holyoke','Mary Lyon Hall, Mount Holyoke College','South Hadley','pv','inst','standing',42.25663,-72.57571,'exact','view','walk','','1897',
  'A college hall built in 1897, with the Mary Lyon Chapel, on the site of the college\'s first building, the 1837 seminary that burned in September 1896. Both were designed by Gardner, Pyne and Gardner of Springfield. The college grew out of the Mount Holyoke Female Seminary that Mary Lyon opened in 1837, the oldest of the Seven Sisters colleges.',
  'A college hall of 1897 on the spot where the first seminary building stood. It holds college offices; interior not checked.',
  '',
  'Owned by Mount Holyoke College, a private college that welcomes visitors to its campus year-round. Look from the campus walks; parking on campus follows the college\'s rules, which were not checked.',
  [W('Mount Holyoke College'),['Mount Holyoke College archives: architects of the buildings','https://lits.mtholyoke.edu/archives-special-collections/asc-research/research-guides/architects-mount-holyoke-buildings']],
  brick='?'),
]

PIN_NOTES={
 'holyoke-city-hall':'OpenStreetMap point for the city hall at 536 Dwight Street.',
 'holyoke-dam':'OpenStreetMap line of the dam, at its Holyoke end.',
 'holyoke-public-library':'OpenStreetMap point for the library at 250 Chestnut Street.',
 'scott-tower-holyoke':'OpenStreetMap point for the tower, on the tower on the aerial. The trail parking at the dead end of Overlook Drive could not be told apart from the houses on the aerial, so it is not pinned.',
 'holyoke-armory-castle':'OpenStreetMap point for the Castle of the Holyoke Armory, 163 Sargeant Street.',
 'mary-lyon-hall-mount-holyoke':'OpenStreetMap building of Mary Lyon Hall.',
}
