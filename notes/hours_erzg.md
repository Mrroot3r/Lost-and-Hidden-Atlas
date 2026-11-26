# hours_erzg: hours for the last 4 churches and 26 other places that take visitors
state: New Mexico
region: nm
date: 2026-11-22
places: 0
file: hours_erzg.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The four places of worship still waiting anywhere (`tools/hours.py list --kind worship`), then museums, hotels and other open places in New Mexico (all 10), Newfoundland and Labrador (all 8), Florida (5 of 6) and Ohio (3 of 6). New York's 23 that wait are nearly all working post offices, whose Postal Service pages earlier sessions found unreadable, so they were left. 30 places are recorded: 10 with hours, each read in the session with `tools/hours.py page` from the page of whoever runs the place and its address or town checked; 20 as `?`.

Hours recorded:
- El Santuario de Chimayó NM (holychimayo.us/blank: Mass times and chapel hours).
- Palace of the Governors, Santa Fe NM (New Mexico History Museum's hours page; "open daily 10am–5pm" is in the page's own description, the first-Friday and holiday lines in its text).
- Hotel Eklund, Clayton NM (saloon and restaurant Thursday to Saturday evenings); Plaza Hotel, Las Vegas NM (Plaza Grill daily); El Rancho Hotel, Gallup NM (restaurant daily); St. James Hotel, Cimarron NM (Lambert's menu page gives lunch and dinner times but no days).
- Railway Coastal Museum, St. John's NL (summer season and times; the page gives no days of the week).
- Florida State Capitol (the Florida Historic Capitol Museum's own page, flhistoriccapitol.gov; the place text describes the 1845 capitol and its museum).
- Hotel Metropole / 21c, Cincinnati OH (the Metropole restaurant's page, 609 Walnut Street).
- The Arcade, Cleveland OH (its own hours page, hours.htm).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Hope Lutheran, Westcliffe CO | hopelutheranchurch3.cloversites.com | 404; not shown to be this church. No page of its own found in two searches; whether it still holds services is unknown |
| First Baptist Peddie Memorial, Newark NJ | newarkhistory.com/peddie1.html | Only directories and history pages found; no congregation site |
| Our Lady of Guadalupe, Conejos CO | Diocese of Pueblo PDF | No Mass times in it; only aggregators otherwise |
| Shuler Theater, Raton NM | shulertheater.com | Events only; no box-office or tour hours (the home page refuses plain fetches) |
| Kit Carson House, Taos NM | kitcarsonhomeandmuseum.com | Page drawn by script, empty to the tools |
| Blue Swallow Motel NM | blueswallowmotel.com | 403; an archived copy of 2026-08-23 exists but the web fetch tool needs approval |
| Fort Bayard NM | fortbayard.org | Connection reset; only Grant County Beat news items otherwise |
| No Scum Allowed Saloon NM | (web search) | No page of its own; travel articles only |
| Murray Premises, St. John's NL | murraypremiseshotel.com | Hotel page gives no public hours |
| Mallard Cottage NL | mallardcottage.ca | Domain does not resolve; directories only otherwise |
| Rorke Store and Carbonear Railway Station NL | carbonear.ca/?p=67 | The town's attractions page gives addresses and telephones, no hours |
| Cable Building, Bay Roberts NL | bayroberts.com/?p=7641 | Summer hours notice is from 2018; not used |
| Port Union Factory, Brigus Stone Barn NL | museumsnl.ca | Only the museums association's directory; no operator page found |
| Orman House, Fort Clinch, Fort Zachary Taylor, Koreshan FL | floridastateparks.org park pages | 403 to the tools; the web fetch tool's approval went unanswered. A session that can read floridastateparks.org should redo these four |
| Buxton Inn, Granville OH | buxtoninn.com/dine | The inn is in a "new chapter": regular dining opening details "forthcoming" (holiday dinners only). Not closed, but no hours yet |

Nothing was found closed or sold.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
