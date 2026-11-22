# hours_czfq: hours for the last 9 waiting churches and 20 museums and sites
state: several (New York, Minnesota, New Jersey, Ohio, Alberta, Michigan, South Dakota, Connecticut, Oklahoma, District of Columbia, Pennsylvania, Maryland, British Columbia, Alaska, Wyoming, Rhode Island, Nova Scotia, Ontario, New Brunswick)
region: several
date: 2026-11-22
places: 0
file: hours_czfq.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. It took the last churches waiting anywhere (seven in New York, two in Minnesota), then museums and other open places from `tools/hours.py list` without `--kind worship`. Twenty-nine were looked up: fourteen got times or a visiting arrangement from the page of whoever runs them, read in the session; fifteen are recorded `?`.

Hours recorded (address or town on each page checked against the place):
- Methodist Church, Sandy Creek: Upper New York Conference UMC page; 2031 Harwood Drive geocodes onto the church's pin. Sunday 10:30. Open.
- Trinity Episcopal, Watertown: the parish's own site; 227 Sherman Street geocodes to the church. Open.
- Soldiers' and Sailors' Monument, Cleveland; Craftsman Farms (Stickley Museum FAQ page); Alberta Provincial Police Barracks (Crowsnest Museum page: winter hours from November 1; its top banner also says Tuesday to Saturday, which disagrees); Gulf of Georgia Cannery ("Open daily 10am to 5pm" in the site's footer); Alasa Farms (Cracker Box Palace); Minuteman Delta-01 (NPS, reservations required).
- By appointment or with no regular hours: Amasa Day House, Parsons-Taylor House, Wheelock Academy, Hays House (page says call for museum hours).
- Peirce Mill: the NPS page says only that the mill is open seasonally; the grounds' daylight hours are recorded.
- Cornish Pump, Iron Mountain: page says closed for the season; no season dates given.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| St. Paul's Episcopal, Watertown | cnyepiscopal.org | 403; no parish site found, only directories (a Yelp listing gives 314 Clay Street) |
| Zion Church, Pierrepont Manor | Episcopal asset map searches | No page for this church found |
| First Baptist, Sandy Creek | searches | Only directories |
| Bristol Hill Church, Volney | searches | No congregation page found |
| Thomas Memorial AME Zion, Watertown | searches | Place note says not in regular use |
| Little Stone Church, Ottawa MN | searches | Le Sueur County Historical Society has no page of its own found; only Explore Minnesota |
| St. Nicholas Orthodox, Caribou MN | searches | Occasional use only; no page |
| Fosterfields | morrisparks.net | 403; an archived copy of 2026-09-07 exists but was not fetched |
| Clemence-Irons House | historicnewengland.org | 403; archived copy of 2026-07-07 not fetched |
| Gold Dredge 8 | golddredge8.com | No times on the home page |
| Medicine Bow depot | Carbon County visitors' page | Only a tourism page ("daily in summer and hunting season"), not the museum's own |
| German Reformed Parsonage, Germantown | germantownny.gov | Only committee meeting times |
| Sinclair Inn, Annapolis Royal | annapolisheritagesociety.com | Hours not in the page text (likely drawn by script) |
| Murney Tower | parks.canada.ca | Connection reset |
| Cape Enrage | capeenrage.ca | 403 |

No church was found to be closed or sold.

## Tips for the next session
- No church waits anywhere now; the rest of the list is museums, theatres, post offices and capitols.
- The Fosterfields and Clemence-Irons archived copies could be read by a session that can approve the web fetch tool.
