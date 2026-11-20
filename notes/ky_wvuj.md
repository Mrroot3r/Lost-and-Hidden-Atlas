# ky_wvuj: Kentucky: a first statewide scatter
state: Kentucky
region: ky
date: 2026-11-20
places: 16
file: data_ky_wvuj.py

## What this batch is
Sixteen places spread across Kentucky, which had 15 (all round Harrodsburg and Danville) and was claimed with `choose.py --thinnest`: in Frankfort the Old State Capitol, Liberty Hall and the Switzer Covered Bridge; Old Washington (Maysville); Federal Hill (My Old Kentucky Home) and the Basilica of St. Joseph Proto-Cathedral in Bardstown; Historic Locust Grove (Louisville); Ashland (Lexington); White Hall (Richmond); Camp Nelson (Jessamine County); Riverview at Hobson Grove (Bowling Green); South Union Shaker Village (Logan County); the Old Mulkey Meetinghouse (Monroe County); Columbus-Belmont State Park (Hickman County); Center Furnace (Land Between the Lakes) and Cottage Furnace (Daniel Boone National Forest). Sources read: Wikipedia (`wiki_raw.py`, county Register lists with `--rows`), Register forms for Cottage Furnace and Old Mulkey (npgallery text layers; Center Furnace's form is not on line), the Kentucky Historical Society's marker and Old State Capitol pages, HMdb, the Forest Service's Daniel Boone site pages, and the operators' own pages for Liberty Hall, Locust Grove, Riverview (city of Bowling Green), South Union, Ashland, the Proto-Cathedral parish, My Old Kentucky Home and Camp Nelson (NPS). Old Mulkey's hours come from the Office of Kentucky Nature Preserves' page. Not checked: hours for White Hall and Columbus-Belmont (parks.ky.gov is drawn by script and its static mirror answers 403), the days of the week for Federal Hill tours, Liberty Hall's season (Wikipedia says mid-March to mid-November), Old Washington's visitor-centre hours (only a Lewis and Clark Trail listing), Camp Nelson's hours outside Memorial Day to Labor Day, and parking at most town sites. Whether you may walk through the Switzer bridge was not checked, so it is view-only. Sources disagree on Switzer's length (120 or 126 ft). Nothing seen on the ground. Pins that mark only a general area: Camp Nelson (on the Oliver Perry House by the visitor centre; the forts spread over 525 acres) and Columbus-Belmont (by the park lot; where the chain and anchor stand was not found). Federal Hill and White Hall were moved by eye onto the house on the aerial. Fitchburg Furnace was left out: it is already in `data_states.py`. Red brick from Wikimedia photographs: yes for Liberty Hall, Federal Hill, the Proto-Cathedral, Riverview, White Hall and Ashland; no for the log meeting house, the timber bridge and the sandstone furnace (from sources); the rest '?' (Locust Grove and South Union have only black-and-white photographs).

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Wickliffe Mounds | Wickliffe, Ballard County, KY (36.97102, -89.09286) | Mississippian town with two platform mounds and a museum, run by Kentucky State Parks (Wikipedia) | A Native American site: needs the managing body's own page inviting visitors (CLAUDE.md, the native category); parks.ky.gov could not be read |
| Bennett's Mill Covered Bridge | Greenup County, KY (38.630556, -82.926944, Register list) | On the Register list, 76000892 | Any source read for date, condition and access |
| Oldtown Covered Bridge | Oldtown, Greenup County, KY (38.431389, -82.895, Register list) | On the Register list, 76000893 | Same |
| Mount Vernon AME Church | Gamaliel, Monroe County, KY (36.674444, -85.799167, Register list) | Built by emancipated slaves in the late 1840s (Register list) | Article and access not read |
| Laura Furnace site | Land Between the Lakes, KY (Wranglers area, off Laura Furnace Creek) | LBL trail page: large stones up the hill mark the furnace, which stopped in 1880; a marker and the Little Drummer Boy's grave nearby | A coordinate; which side of the Kentucky/Tennessee line |

## Tips
- parks.ky.gov stays unreadable (drawn by script; the `kyp-kyparks-static.azurewebsites.net` mirror answers 403). The Office of Kentucky Nature Preserves (`eec.ky.gov/Nature-Preserves/Locations/...`) lists some state historic sites with their hours: it gave Old Mulkey's. My Old Kentucky Home has its own site, `visitmyoldkyhome.com`.
- The Daniel Boone National Forest pages are at `fs.usda.gov/r08/danielboone/recreation/<name>-interpretive-site` (the address without `-interpretive-site` is 404); they read cleanly with `page.py --all` and give a coordinate, hours and directions.
- Before writing up a well-known Kentucky place grep `data_states.py` too: Fitchburg Furnace is the state's worked example there and `start.py` showed nothing within 15 km of Frankfort to warn of it.
- Several N(...) lines were written without the empty tags field; `build_sites.py` caught it at once ("has tags='1796–1800', which looks like years").
