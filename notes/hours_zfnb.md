# hours_zfnb: hours for 33 places of worship in Massachusetts, Missouri and Delaware
state: several (Massachusetts, Missouri, Delaware)
region: several
date: 2026-11-28
places: 0
file: hours_zfnb.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had no church left waiting, so the work took every church waiting in Massachusetts (15), then Missouri (10) and Delaware (8), from `tools/hours.py list "<state>" --kind worship`. Thirty-three were looked up: nine got times from the page of whoever runs them, read in the session; twenty-four are recorded `?`.

Hours recorded (address or town on each page checked against the place):
- St. Patrick's, Lowell: the parish's own Mass schedule page (282 Suffolk Street on the site). Open.
- St. Anne's Shrine, Fall River: the shrine's own page (818 Middle Street) gives a healing Mass on the third Thursday of each month, all welcome; no clock time on the page. Open.
- Central Congregational (former), Worcester: United Congregational Church's own site, 6 Institute Road, worship Sundays 10:30 in Merriman Chapel. Open. The place note calls the building private; the congregation's page shows it in use, so the note may want a look.
- The Mother Church, Boston: christianscience.com services page (250 Massachusetts Avenue). Open.
- Cathedral of Saint Paul, Worcester: the Diocese of Worcester parish finder (the shell could not read it; read with the web fetch tool). The diocese gives the cathedral's address as 19 Chatham Street, not the 38 in the place note.
- Notre Dame, Southbridge: the same diocesan parish finder, times given for "Notre Dame Church: 446 Main St." Open.
- St. Mary's Cathedral, Fall River: the Diocese of Fall River's list of Masses livestreamed from the cathedral (Our Lady of Fall River Catholic Community). Its own diocesan parish page gives no times; this list may cover only livestreamed Masses.
- St. James, Mill Creek (Stanton, Delaware): the parish's worship page (2106 St. James Church Road). The page gives both a 9:30 Sunday service and an older-looking 8 & 10:15 (9 in summer) schedule; both are in the row.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Cathedral of Saint Paul, Worcester (own site) | cathedralofsaintpaul.net | 403 to the shell; web fetch not approved unattended (diocesan page used instead) |
| Notre Dame, Southbridge (parish site) | stjp2parish.org | 403 to the shell; web fetch not approved unattended (diocesan page used instead) |
| St. Anne's Episcopal, Lowell | diomass.org | 403 to the shell; the diocesan page found is a 2024 news story with no times |
| St. Patrick's, Fall River (Good Shepherd Parish) | fallriverdiocese.org | No parish site of its own found; only aggregators |
| Church of the Ascension / Holy Spirit, Fall River | diomass.org profile PDF | No page with service times found |
| Union Congregational, Worcester | searches only | No page of whoever uses it now found |
| Pilgrim Congregational, Worcester | searches only | No page of its own found |
| Elm Street Congregational, Southbridge | searches only | Only directories |
| First United Baptist, Lowell | searches only | Only directories |
| Weston United Methodist, Weston MO | westonhistoricalmuseum.org | 403; only directories otherwise |
| Old Presbyterian (Christian Assembly), Weston MO | searches only | Only directories |
| Beth Shalom (Victorious Life Church), Kansas City | searches only | Only directories and food-pantry listings |
| Linwood Presbyterian, Kansas City | searches only | No page of present users found |
| Siloam Spring Baptist (Barbee Memorial), Excelsior Springs | searches only | Only directories |
| First Swedish Baptist, New Hope Primitive Baptist, Pleasant Ridge Baptist (MO) | searches only | No pages of their own |
| Indian Mission, Todd's Chapel, Griffith's Chapel, Thomas Chapel, Cow Marsh, Old Fort (DE) | Delaware archives marker pages, searches | No congregation pages found |

## Churches found closed, sold or no longer churches
- Central Congregational (The Historic Abbey), Fall River: listed for sale (real-estate listings for 100 Rock Street) and used as a restaurant and events venue; not a church.
- Lee's Summit Christian Church Building: restored by a development firm (press items on a restoration award); present use not read.
- Zion AME, Lexington MO: the place note already says it was restored as an event space and sold.
- St. Georges Presbyterian, Delaware: run by the historical society as a community centre (state archives page); no visiting hours found.

## Tips for the next session
- The Episcopal Asset Map (episcopalassetmap.org/node/<n>) is the denomination's own page and reads from the shell; check the address on each node, as node numbers are not near one another by place.
- The Diocese of Worcester parish finder holds times for every parish but is not readable by `hours.py page`; the web fetch tool read it.
