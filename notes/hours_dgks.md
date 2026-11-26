# hours_dgks: hours for 3 New York churches and 26 New York museums and public buildings
state: New York
region: several
date: 2026-11-21
places: 0
file: hours_dgks.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had three churches left waiting; none of them has a page of its own, and after them no place of worship waits in any state, so the rest came from `tools/hours.py list "New York"` (museums, house museums and public buildings). Twenty-nine were looked up: fourteen got hours from the page of whoever runs them, read in the session; fifteen are recorded `?`.

Hours recorded (address or town on each page checked against the place; all marked open):
- Herkimer Home: NY State Parks page (200 State Route 169, Little Falls). The page gives the tour season both as Memorial Day to Columbus Day and as to Labor Day; both are in the row.
- Old Fort Johnson: its own site. Only the 2025 season (June 3 to Oct 17) is posted; the row says so.
- Cobblestone Museum: its own admission page (Ridge Road, Albion). Shoulder season, call for tour times.
- Swart-Wilcox House: its own site; Sundays in summer, no clock times given.
- Bronck House: Greene County Historical Society tour page (closed Oct 17, 2026 to May 29, 2027).
- Olana: the Olana Partnership's tours page (late-2026 tour days); park hours from its Hours + Directions page (olana.org/?p=715).
- North Creek station: North Creek Depot Museum's own site (5 Railroad Place); closed for 2026.
- Elmendorph Inn: Historic Red Hook visit page (7562 North Broadway); open days are posted one by one.
- Cheney Library: its own site (73 Classic Street).
- Fort Ticonderoga, Thomas Cole House: their own visit pages.
- New York State Capitol: Empire State Plaza (OGS) hours page, read through the web fetch tool.
- Gilboa Museum: Gilboa Historical Society page at northerncatskillshistory.com/?p=125 (122 Stryker Road), read through the web fetch tool.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Duane Methodist Episcopal, Duane; First Union Protestant, Mountain View; First Congregational, Malone | searches only | No page of their own found (two searches each); only Wikipedia and directories |
| Van Alen House, Kinderhook | cchsny.org/visit/luykas-van-alen-house/ and /visit/ | No hours on either page (closed for the season) |
| Penfield Homestead, Crown Point | penfieldmuseum.org | Pages drawn by script; no hours came back |
| Oyster Bay Railroad Museum | obrm.org | HTTP 403; an archived copy of 2026-08-13 exists but could not be fetched unattended |
| Fulton County Museum, Gloversville | fultoncountyhistoricalsociety.org | Page returned no text |
| Oliver House, Penn Yan | yatescountyhistory.org | Would not connect |
| Montauk Point Light | montauklighthouse.com | Would not connect |
| Lisbon Depot Museum | townoflisbonny.gov/depot-museum.html | Gives the farmers market (Wed 2–6) but no museum hours |
| Louis Miller Museum, Hoosick Falls | hoosickhistory.com | Connection reset twice; archived copy blocked |
| Opus 40, Saugerties | opus40.org/visit | HTTP 403 and web fetch blocked |
| Hook Windmill; Van Alstyne Homestead; Hamden District No. 1 School; Margaret Reaney Library | searches only | No page of their own found |

No church or museum was found to be closed for good or sold.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
