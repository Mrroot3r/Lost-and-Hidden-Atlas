# hours_eqdb: hours for the last 17 waiting churches, then 8 museums and public buildings
state: several (New York, North Dakota, Arkansas, Hawaii, Massachusetts, Vermont, Nebraska, Kansas, Utah, Delaware, New Hampshire, District of Columbia, Missouri, Mississippi, Colorado, Arizona)
region: several
date: 2026-11-21
places: 0
file: hours_eqdb.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. `tools/hours.py list --kind worship` showed only 17 churches waiting in all (5 in New York); every one was looked up, so after this batch no church waits anywhere and the next session goes straight to museums. Then 8 museums and public buildings from `tools/hours.py list` without `--kind`. 25 places recorded: 9 with times or a visiting arrangement from the page of whoever runs the place, read in this session with `tools/hours.py page`; 16 recorded `?`.

Hours recorded (address or town on each page checked against the place):
- Smith Clove Meetinghouse, Highland Mills: Cornwall Quakers' own site; the meeting worships weekly in Cornwall and the home page shows only "the annual Smithclove Meeting House gathering, August 2026". Recorded as no regular services, one August gathering. Not marked open.
- Old Stone Church, West Boylston: the West Boylston Historical Society page, which reprints the DCR notice on use (open to the public in daylight hours, free, groups of 25 or fewer need no permit). A mass.gov DCR event page (history walk, Sunday November 8, 2026, 1 to 2 p.m., 130 Beaman St.) also opened through `hours.py page`. Already `public`, so not marked open.
- Wyman Tavern, Keene: Historical Society of Cheshire County page; by appointment only (the hours printed on that page are the society's own building at 246 Main Street, not the tavern). Open.
- Eastern Market, Washington: its own site (225 Seventh Street SE). Open.
- Vanderbilt Mansion, Hyde Park: NPS basic information page (mansion by tour; buildings typically close 5 p.m.). The NPS "hours" page draws its times by script. Open.
- Harriet Tubman Home, Auburn: NPS place page; visitor center by appointment only. Open.
- John Wornall House, Kansas City: Wornall/Majors page (6115 Wornall Rd). Open.
- Mississippi State Capitol: the Legislature's "About the Capitol" page (400 High Street). Open.

Also looked up but NOT in the file: Fort Ticonderoga (fortticonderoga.org/visit gives May 1 to October 31, 2027, Tuesday to Sunday 9:30 a.m. to 5 p.m.) and Opus 40 (opus40.org refused). Both are thin `lm-` landmark pins, and `check.py` refuses an `lm-` id in an hours file ("not a place id"), so `hours.py list` offers places it cannot record. Fix in the tool: leave `lm-` ids out of `hours.py list`, or let `check.py` accept them.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| St. Ann & the Holy Trinity, Brooklyn | stannholytrinity.org (worship page, home) | 403; an Internet Archive copy of 2026-11-16 exists but the web fetch tool's approval went unanswered |
| Hurley Reformed Church, Hurley NY | zeffy.com donation page; searches | No site of its own found (New Hurley Reformed is a different church); zeffy 403 |
| Ponckhockie Union Chapel, Kingston | searches; NPS travel page | Only directories and old articles |
| Church of Rockwell Falls, Lake Luzerne | PC(USA) church-trends page; searches | 404; only directories |
| Sims Lutheran Church, Almont ND | nordicamericanchurches.org; ndtourism.com | Both 403 |
| St. John's Church, Hebron ND | hebron.municipalimpact.com/worship | City's list of churches, no service times |
| Beecher Bible and Rifle Church, Wabaunsee KS | searches | Only the Wamego visitors' page and directories |
| First United Methodist, Nebraska City | searches | No site of its own found |
| Roasting Ear Church and School, Onia AR | searches | Nothing; privately owned when listed |
| West Richwoods Church and School, AR | searches | Nothing; privately owned when listed |
| Ahuʻena Heiau, Kailua-Kona | the hotel's experiences page on marriott.com | 403 |
| Hale Hālāwai O Hōlualoa (Living Stones), Kona | searches | No church site found; only directories |
| Logan Tabernacle, Utah | churchofjesuschrist.org searches; bearriverheritage.com | No visiting hours on a church page |
| Fletcher Union Church, Vermont | searches; Friends of the Union Meeting Hall donation page | No times |
| Old Christ Church, Laurel DE | delaware.church Episcopal service lists; history.delaware.gov | Not listed by the diocese; no page of its own |
| Argo Mill and Tunnel, Idaho Springs | argomilltour.com home and /tours/ | No times in the page text (probably a booking widget) |
| Sharlot Hall Museum, Prescott | sharlot.org | 403 / 404 |

No church was found closed or sold in this batch.

## Leads
| Place | State | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
