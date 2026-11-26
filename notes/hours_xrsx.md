# hours_xrsx: hours for the last seven churches (New York, Utah, South Dakota), then 19 museums and other open places in twelve states
state: several (New York, Utah, South Dakota, Washington, Alabama, Georgia, Texas, Louisiana, Maryland, Vermont, Idaho, New Jersey, Ohio, Colorado, Virginia)
region: several
date: 2026-11-22
places: 0
file: hours_xrsx.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. Seven churches were still waiting (two in New York, four in Utah, one in South Dakota); none had a page of its own that gave times, so all seven are recorded `?`. After them no church waits anywhere, and the session went on to museums and other places that take visitors (`tools/hours.py list` without `--kind worship`). Twenty-six places were recorded in all: six got hours from the page of whoever runs them, read in the session; twenty (the seven churches and thirteen others) are recorded `?`.

Hours recorded (address or town on each page checked against the place):
- Port Townsend City Hall (Museum of Art and History): Jefferson County Historical Society museum page (540 Water Street). Thursday to Sunday 11 to 4; first Saturday free, open to 7.
- Alabama State Capitol: Alabama Historical Commission's Plan Your Visit page for the Capitol. Weekdays 8 to 4; group tours by appointment.
- Georgia State Capitol: Georgia Capitol Museum visit page (University of Georgia Libraries, 206 Washington Street SW). Weekdays 8 to 5 and walk-in tour times.
- Bridge House, Albany GA: City of Albany downtown page for the Albany Welcome Center (112 N Front St).
- Market House Museum, Goliad: Goliad County's page for the museum (205 South Market St., run by the county historical commission).
- Old Louisiana State Capitol: the museum's own visit page (100 North Blvd.). Closed Sunday, Monday and Thursday.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Union Reformed Church, Unionville NY | searches | Only directories; no site of its own |
| Adamsville Baptist Church, Kingsbury NY | searches | Only directories; no site of its own |
| Torrey Log Church and Schoolhouse, UT | searches | Only marker and wiki pages |
| Corinne Methodist Episcopal Church, UT | searches | Only news (Deseret News, KSL) |
| Parowan Old Rock Church, UT | parowan.org/node/6163, /node/6242 | Both HTTP 404 |
| Box Elder Stake Tabernacle, UT | searches incl. churchofjesuschrist.org | No church page with tour times |
| Brown Earth Church, Stockholm SD | episcopalchurchsd.org/article/1212464 | Page nearly empty (drawn by script) |
| Tintic Mining Museum, Eureka UT | eureka.utah.gov/tintic-historical-society | Telephone numbers only; no set hours |
| Benson Grist Mill, UT | bensonmill.org, nps.gov | Events only, no regular hours |
| Georgia State Railroad Museum | chsgeorgia.org/GSRM | HTTP 403; an Internet Archive copy of 2025-10-17 not fetched |
| Port Townsend Carnegie Library | cityofpt.us/library | Connection refused; the copy read gave closures only |
| Hyde Log Cabin, Grand Isle VT | vermonthistory.org/hyde-log-cabin | No times on the page |
| Rose Hill Manor, Frederick MD | recreater.com pages | HTTP 404 |
| Wallace Carnegie Library, ID | wallace.lili.org | Drawn by script |
| New Jersey State House | njleg.state.nj.us tour brochure | School tour programmes only; the public tour times found were on a tourism site, not used |
| Germantown Colony Museum, LA | sos.la.gov museum page | HTTP 404 |
| Home Building Association Bank, Newark OH | new.explorelc.org welcome-centre page | Connection refused |
| Museum of Colorado Prisons | prisonmuseum.org | Connection reset; an Internet Archive copy of 2026-10-17 exists but the fetch was not approved unattended |
| Prestwould, Clarksville VA | prestwould.org | Connection reset |
| Boise Basin Museum, Idaho City | idahocitychamber.org foundation page | Connection reset |

## Left waiting on purpose
- The New York post offices (19 now), as before: USPS pages give no usable hours to the tools.
- Oakland B&O station, MD: garrettcountymuseums.com/hours gives Wednesday to Saturday 10 to 3 for the History Museum and the Transportation Museum, but does not name the station, so it was not recorded.
- Kirby's Mill, Medford NJ: the medfordhistorical.org page a search returned is for Medford, Massachusetts; not used.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
