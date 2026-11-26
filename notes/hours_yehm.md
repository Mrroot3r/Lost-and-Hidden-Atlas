# hours_yehm: hours for the last 8 waiting churches and 18 other places that take visitors
state: New York
region: ny
date: 2026-11-22
places: 0
file: hours_yehm.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. It took every place of worship still waiting anywhere (four in New York, two in Alabama, one each in Louisiana and Maryland), so after this batch no church waits, then 18 museums, capitols, inns and the like from `tools/hours.py list`. Thirteen got hours from the page of whoever runs them, each read in the session with `tools/hours.py page` and its address checked against the place; thirteen are recorded `?`.

Hours recorded:
- St. Peter's, Westchester Square, Bronx: the parish's own site, stpeterswsbronx.org (Sunday Mass, and the church open to visitors on Tuesdays). Its address is a P.O. box in 10461 with the same e-mail as the Episcopal Asset Map entry for 2500 Westchester Avenue.
- St. Ann's, Morrisania, Bronx: the parish's own page, stannssouthbronx.wordpress.com (295 St. Ann's Ave). The page is undated.
- Old Wye Church, Wye Mills MD: the Episcopal Asset Map entry for Old Wye (14114 Old Wye Mills Rd), Sunday 10 a.m. The parish's own site, wyeparish.org, gives no service time; the parish also has St. Luke's Chapel in Queenstown, and whether services alternate between the two was not found.
- Temple Emanu-El, Birmingham AL: the congregation's own worship page, ourtemple.org/worship (2100 Highland Ave South, by the Union for Reform Judaism's listing).
- Michigan, Missouri and California state capitols: each state's own visitor page. California's page shows only the coming weekday's hours (9 to 5) and says it is closed weekends and most holidays.
- Bar U Ranch AB (Parks Canada visitor centre page), Britannia Mine Museum BC (the museum's plan-your-visit page; days of the week not stated), Old Fort Meade Museum SD (the museum's Google site, 2026 season), Beaumont Inn KY (its own location page: tavern hours only; the dining page answered 503), Gadsden Hotel AZ (its food and drink page), Strand Center for the Arts, Plattsburgh (its own site: arts centre hours at 23 Brinkerhoff St; the theatre opens for shows).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| First Presbyterian, Plattsburgh NY | presbyplatt.org | Connection reset, 503, no archived copy. The Presbytery of Northern New York's 2020-21 directory PDF gives Sunday worship 10 a.m. at 34 Brinkerhoff St; not recorded because it is five years old |
| St. John the Baptist, Plattsburgh NY | holycrosspbg.org | 403 on every page, no archived copy; the Diocese of Ogdensburg's parish page gives office hours only |
| First United Methodist, Birmingham AL | (several guessed addresses for the church's site) | No site of the church's own found or opened; only directories and tourism listings |
| St. Martin de Tours, St. Martinville LA | 5339.sites.ecatholic.com | 403, no archived copy; only mass-time aggregators otherwise |
| Lyon Mountain station museum NY | lyonmountainmuseum.blogspot.com | Newest hours are for 2015 |
| Heart's Delight Farm, Chazy NY | whminer.org facility page | Says the exhibit and walk are open free; no days or times |
| Old State Capitol, Milledgeville GA | visitmilledgeville.org listing | Tourism listing, no times; no page of the museum's own found |
| Flat Top Manor NC | nps.gov Moses H. Cone page | Ranger tours "summer and fall", no times |
| Lincoln County Old Jail, Wiscasset ME | lincolncountyhistory.org | 403, no archived copy |
| SS Meteor, Superior WI | superiorpublicmuseums.org | Did not connect; an archived copy of 2025-07-17 exists that the tool could not fetch |
| Silver Reef Museum UT | washco.utah.gov Silver Reef page | Only a 2024 free-week event, no regular hours |
| Badger Mine and Museum WI | badgermineandmuseum.com | Drawn by script; the only times shown are the city office's |
| Hat Creek Ranch BC | historichatcreek.ca (and hatcreekranch.ca) | First did not connect; second is unrelated content |

Left unrecorded (looked at, not settled): Old Essex County Courthouse, Elizabethtown (the County Clerk at 7559 Court Street keeps 9 to 4:45, but whether the clerk is in the old courthouse building was not confirmed); Barre City Hall and Opera House (the City Clerk's hours did not say the office is in City Hall); Crescent Hotel, Geiser Grand Hotel, Frog Hollow Stone Mill (no hours on pages read). New York's other 18 waiting places are post offices, whose Postal Service pages give the tools nothing usable.

Closed or sold: none found. The Strand Center for the Arts, Plattsburgh, was reported in September 2026 (WAMC) as possibly closing for money reasons; its own site still lists events into December 2026.

## Leads
None.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
