# hours_gecv: hours for 32 places of worship across the US and Canada
state: (several)
region: (several)
date: 2026-11-28
places: 0
file: hours_gecv.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had no church waiting, so the list was taken from every state (`tools/hours.py list --kind worship`). 32 places looked up: 14 got service times or opening hours from the page of whoever runs them, each read with `tools/hours.py page` (or, where the tool got HTTP 403, the web fetch tool) and its address or town checked; 18 are recorded `?`.

Hours recorded: St. Mary, New Haven (parish "visit us" page: open-for-prayer hours; its Mass-times page is drawn by script and gave no times); St. Ninian's Cathedral, Antigonish; First Congregational, Portland OR; Greenock Church, St. Andrews NB (the Charlotte County pastoral charge's page gives 146 Montague St; the place note says 134 — same church, the only Greenock church in town); First Congregational, Akron; St. Joseph Cathedral, San Diego (the schedule on its front page sits beside 2024–2025 notices, so it may be old); St. Raphael's Cathedral, Dubuque (an **interim** pastorate schedule to January 15, 2027: look again after that); First UMC, Parkersburg (firstumcparkersburg.org; a search result at firstumc.org is a Lakeland, Florida church); First Baptist (White Temple), Portland OR; Immanuel Presbyterian, Los Angeles; St. James Cathedral, Seattle (archdiocese parish page); First Baptist, Philadelphia; St. Leo's, Lewistown MT; Church of the Redeemer, Salmon ID (diocese's church table).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Holy Trinity, Canora SK | uocc.ca/parish/4605 | Parish page gives no times, and its address is 904 Main St, not the designated church at 710 Main: the old church may no longer be the parish's |
| Immaculate Conception, Pawhuska OK | diocese parish finder (ecatholic) | No parish page found; only aggregators and tourism listings |
| First Congregational, Ann Arbor | searches | No site of its own found |
| First Lutheran, West Ave, La Crosse | firstlu.squarespace.com | That is First Lutheran of **Onalaska**, not this building; who uses the La Crosse church was not found |
| St. Nicholas Chapel, Seldovia AK | searches | No parish page |
| First Presbyterian, Lapwai ID | cityoflapwai.gov article | Drawn by script, nothing read |
| St. Stanislaus Kostka Mission, Rathdrum ID | searches; diocese PDF not read | Only aggregators found |
| First Universalist, Elgin IL | uuce.org | HTTP 403, and the web fetch tool's approval went unanswered |
| First Parish, Portland ME | firstparishportland.org | HTTP 403, same (its newsletter gives 425 Congress St but no times) |
| Congregation Emanu-El, Victoria BC | congregationemanuel.ca | Read; office hours only, no service times |
| Central Methodist (now First UMC), Hot Springs AR | searches | Only directories |
| Second Baptist, Olathe KS | searches | Only directories |
| Grace Episcopal, Rosedale MS | searches | No page of its own or diocese listing found |
| Forest Lawn Chapel, Saginaw | searches | No city page with cemetery hours found |
| First Congregational, Saginaw; First Presbyterian, Bay City; First Presbyterian, Pueblo | searches | Only directories or chamber listings (a Pueblo bulletin PDF found was not shown to be this church) |
| St. Nicholas of Tolentine, Atlantic City | searches; diocese news | No parish Mass-times page found |

## Not asked
Places in the list that are no longer churches and have no hours of their own were left alone: The Abbey, San Diego (event hall); Plymouth Congregational, New Haven (offices); Cumberland Presbyterian, Peoria (bank); Steeple Square, Dubuque; Baptist Temple, Philadelphia (Temple University). Perhaps `hours.py list` should not list them.

## Tips for the next session
- The web fetch tool answers 403 sites, but in an unattended run its approval prompt goes unanswered after a few pages; use it once, early, for a batch of 403 pages.
- Search results at a bare domain like firstumc.org can be another town's church: check the page's address every time.
