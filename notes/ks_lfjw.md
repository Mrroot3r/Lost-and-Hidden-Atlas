# ks_lfjw: Leavenworth County and Jefferson County, Kansas
state: Kansas
region: ks
date: 2026-11-24
places: 14
file: data_ks_lfjw.py

## What this batch is
Fourteen places: five on Fort Leavenworth (the Rookery, the Sherman, Sheridan and Grant Halls, the Memorial Chapel, the national cemetery and the Buffalo Soldier Monument), the old Kansas State Penitentiary at Lansing, five Leavenworth districts or works (the industrial district, North Esplanade, Arch Street, Third Avenue, and Abernathy Plant K), and three in Oskaloosa (the Union Block, Old Jefferson Town, the Newell-Johnson-Searle House). Every Kansas City part of the list had been worked at least once, so this took the one with the fewest places, Leavenworth, and reached into Jefferson County. Sources: the Army's wayside leaflet and the Historic American Buildings Survey record for the Rookery, National Register forms read as text, the Kansas Historical Society register search, the City of Leavenworth's district pages, the Lansing Historical Society's tour page, Wikipedia one article at a time. Not checked: interiors, the Memorial Chapel's service times, the national cemetery's hours (the VA page returned 404), and Old Jefferson Town's hours (no page of the society's own was found). The Rookery's pin is on the road corner by its block of houses; the aerial did not show which house it is (prec site). Pictures were chosen for seven places; the penitentiary and Plant K have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Buck Creek School | Two miles east of Williamstown, Jefferson County, KS (OpenStreetMap 39.06583, -95.29692; Register list 39.06778, -95.29472) | National Register 1988 form read: c. 1878 one-room limestone school with a wooden bell tower, now a homemakers' hall | Neither coordinate falls on a building that looks like a limestone school on the 2024 aerial; need the road address |
| Morris Harris Farmstead | 16010 US 24, Perry, KS | National Register 2023: six stone farm buildings of 1909 | The address lookup gave two points a mile apart and the Register point falls on the highway; need an owner's or the Register's own location |
| Delaware River Parker Truss Bridge, Perry; Delaware River Composite Truss Bridge, Valley Falls | Jefferson County, KS | Register 2003 listings in the Metal Truss Bridges thematic group | The forms were not read |
| Methodist Episcopal Church of Oskaloosa | Oskaloosa, KS (39.2174, -95.3144) | Register 2023; Commons photographs describe a one-storey Richardsonian Romanesque church with a bell tower | The form was not read; no service times |
| Leavenworth Landing, Union Park, Abernathy/Lyle House | Leavenworth, KS | State and National Register listings | Only the Register's one-line style; the City of Leavenworth's district pages for Union Park and the Landing were not read |
| Biehler Barn | Easton, KS | National Register 1977 | No source found that gives a location or a description |

## Tips
- The City of Leavenworth's historic-district pages (leavenworthks.gov/cd/page/<district>-historic-district) are full, plain descriptions; page.py reads them whole.
- The Rookery's HABS record (denix.osd.mil army-pre1919-pchh) gives a UTM point; convert it by hand because pyproj is not installed.
- A web search for the Fort Leavenworth wayside leaflet finds the Army's PDF, which has a short, usable paragraph for each stop.
- An address lookup for a rural Kansas address can return two points; check each on the aerial before pinning.
