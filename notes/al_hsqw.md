# al_hsqw: Alabama: a first scatter, Tennessee Valley to Mobile Bay
state: Alabama
region: al
date: 2026-11-20
places: 17
file: data_al_hsqw.py

## What this batch is
A first scatter of 17 places across Alabama, which had one place (Old Cahawba) when the session began. North: Belle Mont (Tuscumbia), Mooresville, Clarkson–Legg and Horton Mill covered bridges, Cornwall and Janney furnaces. Centre: Sloss Furnaces, Tannehill and Brierfield ironworks, Kymulga mill and covered bridge, the old capitol ruins in Capitol Park (Tuscaloosa), Fort Toulouse/Fort Jackson. Black Belt: Gaineswood, St. Andrew's Church at Prairieville. South: Old St. Stephens, Blakeley and its breastworks, the Fort Mims site. Facts came from Wikipedia (tools/wiki_raw.py) and, for hours and access, the managing body's own page read with tools/page.py: the Alabama Historical Commission's "Plan your visit" pages (Gaineswood, Belle Mont, Fort Toulouse, Fort Mims), the Tannehill, Brierfield, Historic Blakeley and St. Stephens Historical Park sites, and slossfurnaces.org. National Register forms were not read. Nothing was checked on the ground. Not checked: hours for Cornwall Furnace, Janney Furnace, Kymulga (the city page would not open), Clarkson (county parks page would not open) and Old St. Stephens; parking everywhere (OpenStreetMap maps almost no lots in Alabama, and the three it did map near Horton Mill, Clarkson and Fort Gaines fell on a road, in trees and inside the fort walls on the aerial, so no th= point was given). Pins at area precision: Mooresville (the village), Blakeley (the town site), St. Andrew's Church (the building could not be told on the aerial), Janney Furnace (the stack could not be picked out under trees). Red brick from a source or a Wikipedia photo; nine places are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Morgan | Gulf Shores, AL (30.22806, -88.02306) | Written up in full in this session and dropped before publishing: brick third-system fort of 1819–1834, AHC state historic site, fort and grounds daily 8 a.m. to 5 p.m., museum 9 to 4 (ahc.alabama.gov/FtMorganPlanYourVisit.aspx); Wikipedia courtyard photo shows red brick casemates beside concrete batteries (brick='some'); pin inside the star fort on the aerial | check.py refuses the pin: tools/outlines.py's Alabama outline stops 8–15 km short of Mobile Point and Dauphin Island. Needs the outline widened (a tool change), then the entry can go in as written |
| Fort Gaines | Dauphin Island, AL (30.24833, -88.07556) | Written up and dropped for the same reason: established 1821, Battle of Mobile Bay; Dauphin Island Park and Beach Board; daily 9 a.m. to 5 p.m., $10 adults, $5 ages 5–12 (townofdauphinisland.org/fort-gaines); 2008 facade photo shows buff brick (brick='no') | The Alabama outline, as above |
| Huntsville Depot | Huntsville, AL (34.73444, -86.59083) | Oldest surviving railroad depot in Alabama, 1860; Civil War prisoners' graffiti on its walls (Wikipedia) | Wikipedia says the museum left in October 2024 and the city was weighing its future: current access unknown |
| Rock Run Furnace and town | Rock Run, Cherokee County, AL (34.02778, -85.49528) | HAER photographs show furnace foundations (Wikipedia) | A source for what is left, the exact spot and the owner |

## Tips
- tools/outlines.py: Alabama's outline misses the Gulf shore by 8–15 km (Mobile Point, Dauphin Island), so check.py stops any pin there. The Mississippi and Florida panhandle coasts may have the same fault; check before writing up a coastal place in them.
- www.dauphinisland.org (the Park and Beach Board's old address) now serves a gambling spam page; Fort Gaines hours are on townofdauphinisland.org/fort-gaines.
- slossfurnaces.com does not answer; the museum's current site is slossfurnaces.org.
- The Alabama Historical Commission's pages ahc.alabama.gov/<Site>PlanYourVisit.aspx read cleanly with page.py and give hours for each state historic site.
- start.py's region list for Alabama is one code (al) for the whole state; tools/parking.py finds almost nothing in rural Alabama.
