# hours_pdma: hours for 32 museums, courthouses and other open places in seven states
state: several (New York, Nebraska, Illinois, Nevada, Pennsylvania, Wyoming, North Dakota)
region: several
date: 2026-11-22
places: 0
file: hours_pdma.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had one place of worship left waiting (Temple of Israel, Amsterdam) and no other state had any, so the rest came from `tools/hours.py list "<state>"` without `--kind worship`: museums, courthouses, historic sites and a library. Thirty-two were settled: nineteen got days and times from the page of whoever runs them, one was found closed, twelve are recorded `?`.

Hours recorded (address or town on each page checked against the place):
- Former Governors' Mansion and Camp Hancock, Bismarck: State Historical Society of North Dakota site pages.
- Metamora, Mount Pulaski and Cahokia courthouses, Jubilee College: Illinois DNR site pages (`dnrhistoric.illinois.gov/experience/sites/site.<slug>.html`).
- Dangberg Home Ranch (dangberg.org/visit), Boulder City/Hoover Dam Museum in the Boulder Dam Hotel (bchdmuseum.org).
- Buffalo Bill Ranch and Fort Hartsuff: outdoornebraska.gov location pages (Fort Hartsuff gives months, no clock times).
- Arbor Lodge: Arbor Day Farm's contact page (Friday to Sunday). The Nebraska City Museum Association page says Tuesday to Sunday; the operator's page was used.
- G.A.R. Memorial Hall and Old Freighters Museum (Russell, Majors & Waddell House), Mayhew Cabin: nebraskacitymuseums.org/museums. The page sets names and hours in alternating columns; the pairing was made from the page's block order (medium confidence). Mayhew Cabin is by appointment; its foundation's site says the site closed after the 2019 flood and the cabin reopened at an event on June 19, 2026, with no regular hours since.
- Newlin Grist Mill (newlingristmill.org; the mill is not grinding while a new wheel is built), East Broad Top Railroad (eastbroadtop.com FAQ, 2026 season), Martin's Cove visitors' centre at Tom Sun Ranch (the Church's historic-site page; no season given), Hudson Hall (hudsonhall.org gallery hours), Amsterdam Free Library (its own site, read from the site's page data).

Closed: **Kamp Store, Kampsville** — the Center for American Archeology says the museum has been closed since the 2019 flood and is closed for repairs until further notice; a move of the building is on hold until 2027. The access note on the place still quotes greatriverroad.com's old hours and should be corrected by someone editing that place.

Not checked: nothing was seen on the ground and no telephone call was made. Several pages (outdoornebraska.gov, hudsonhall.org, newlingristmill.org) refuse a plain fetch and were read through the web page tool.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Temple of Israel, Amsterdam NY | Wikipedia; searches | A church (Templo Esperanza de Israel) since 2008; no page of its own found |
| Maltese Cross Cabin, Medora | nps.gov thingstodo page | Open daily "during visitor center hours"; the visitor-center times are drawn by script and could not be read |
| Magnolia Manor, Cairo IL | searches only | No Cairo Historical Association page found |
| McGill Drugstore, NV | wpmuseum.org exhibit page | No hours for McGill; the footer's hours are for the Ely museum |
| Million Dollar Courthouse, Pioche | lincolncountynv.gov | Nothing found |
| Eureka Opera House | eurekacountynv.gov opera-house page | Shown only as a meeting venue; no times |
| Belmont Courthouse, NV | searches only | Only tourism listings |
| Dredge Captain Meriwether Lewis, Brownville | lewisdredge.org | 502 error |
| Champion Mill, NE | chasecounty.com/champion.html | 404 |
| Greersburg Academy, Darlington PA | littlebeaverhistorical.org event page | 403 |
| Shandaken Historical Museum | shandaken.gov | No museum page |
| Bagg Bonanza Farm, ND | searches; baggbonanzafarm.org | No page of its own read |

Not recorded and still waiting: Boulton Historic Site (jacobsburghistory.com says open only during special events May to December, tours on request; `hours.py set` would not take that as days and times), Fort Sidney, Dowse Sod House, Medicine Bow depot museum, J.C. Penney House, Grassy Butte Post Office, Rensselaerville Grist Mill (no operator pages found in two searches; not recorded as `?`).

No church was found to be closed or sold.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
