# hours_xqvd: hours for 26 places in New York, Delaware and elsewhere (the last waiting churches, then museums)
state: New York
region: ny
date: 2026-11-22
places: 0
file: hours_xqvd.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last seven churches waiting anywhere (five in New York, two in Delaware), then nine New York museums and houses and ten museums elsewhere, from `tools/hours.py list`. Seven got opening or service times from the page of whoever runs them, read in the session with `tools/hours.py page` and the address checked; nineteen are recorded `?`. No church now waits in any state.

Hours recorded:
- Christ Church, Dover DE: the Episcopal Church's own Asset Map page for it (501-523 S State St). The parish's own site (christchurchdover.org) refused the connection. The Asset Map text looks some years old; worth a fresh look when the parish site answers.
- William Miller House, Miller Place NY: Miller Place-Mount Sinai Historical Society's home page (75 North Country Road).
- St. James General Store NY: Suffolk County Parks' page (516 Moriches Rd).
- National Memorial Day Museum, Waterloo NY: the Waterloo Library & Historical Society's own booking page (picktime.com), which states the museum's days and hours.
- Hawkins-Mount House, Stony Brook NY: the Long Island Museum's event page; only special tours on three Saturdays in 2026, all now past.
- Iolani Palace HI: the palace's own visit page.
- Beaufort Arsenal SC: the Beaufort History Museum's hours page (the times carry an asterisk the page does not explain in the text read).

Not checked: nothing seen on the ground, no telephone call.

Post offices (about fifteen New York ones wait, all `open`) were left alone: the USPS locator page is drawn by script and gives no hours to `page.py`. They are not marked `?`, so a later session with a way to read USPS's own location pages can take them.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| St. Paul the Apostle, Mechanicville NY | rcda.org parish page; allsaintsny.us | The diocese's page sends to allsaintsny.us, which answers 403 |
| St. Paul's Episcopal, Waterloo NY | episcopalrochester.org | 403; no page of the parish's own found |
| First Presbyterian, Waterloo NY | (web search only) | No page of its own; the bulletins found are First Presbyterian, Waterloo, Iowa |
| Old St. Luke's, Mechanicville NY | mechanicvilleny.gov; albanyepiscopaldiocese.org | The congregation is now St. Luke's on the Hill; the old church is the Arts Center on the Hudson, which has no page of its own found. Not a working church |
| Lodi Methodist, Lodi NY | (web search only) | No page of its own; lodiumc.blogspot.com is Lodi, Ohio. Whether it is still a congregation is not known |
| Cool Spring Presbyterian, Lewes DE | (web search only) | No page of its own; only newspaper items and directories |
| Thompson House, Setauket NY | wmho.org | The Ward Melville Heritage Organization's pages describe the house and a new exhibit but give no visiting hours |
| Rose Hill Mansion, Fayette NY | historicgeneva.org | 403 on every page |
| Old Essex County Courthouse, Elizabethtown NY | essexcountyny.gov | No visiting hours for the old courthouse |
| Hotel Lafayette, Buffalo NY | wyndhamhotels.com | A hotel; no hours for the public rooms |
| Guaranty Building, Buffalo NY | hodgsonruss.com | The owner's page gives no lobby or interpretive centre hours |
| Eleazer Arnold House, Lincoln RI | historicnewengland.org | 403. Hearthside House's page (a neighbour, not the manager) says "open weekends from June to October" |
| Parson Thorne Mansion, Milford DE | (web search) | No page of the Milford (Delaware) Historical Society's own found; milfordhistoricalsociety.org is Milford, Connecticut |
| Teackle Mansion, Princess Anne MD | visitsomerset.com | A county tourism listing (Thursday, Saturday, Sunday 1 to 3 p.m., April to November); no page of the historical society's own |
| Oscar Anderson House, Anchorage AK | muni.org historic preservation page | 404 |
| Cottonwood House, Quesnel BC | barkerville.ca/cottonwood/ | Drawn by script |
| Fort Harker, Kanopolis KS | (web search) | No page of the county historical society's own |
| Maison Olivier, St. Martinville LA | lastateparks.com | 403; an archived copy of May 2026 exists |
| Point Clark Lighthouse ON | parks.canada.ca | The Parks Canada page gives no visiting hours |

No church was found closed or sold, apart from Old St. Luke's, Mechanicville, which is now an arts centre.

## Leads
| Place | Town | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
