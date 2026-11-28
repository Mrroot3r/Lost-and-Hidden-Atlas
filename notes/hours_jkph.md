# hours_jkph: hours for 31 places of worship in Manitoba, Michigan, South Carolina, British Columbia, North Dakota, Illinois and Wisconsin
state: Manitoba
region: mb
date: 2026-11-28
places: 0
file: hours_jkph.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had no church waiting, so this took the provinces and states with the most churches left: all nine in Manitoba, then all four each in Michigan, South Carolina, British Columbia and North Dakota, and the three each in Illinois and Wisconsin. Four got service or opening times from the page of whoever runs them, each read with `tools/hours.py page` (one through the web fetch tool) and its address or town checked; twenty-seven are recorded `?`.

Hours recorded:
- First Congregational Church UCC, Jackson MI (jacksonucc.com/home.html: Sunday 10 a.m. in person and on Zoom; the page gives no street address, but its e-mail is fcc120nj, for 120 North Jackson Street).
- Church of the Holy Cross, Stateburg SC (holycrossstateburg.com, 335 North Kings Hwy: Sunday Eucharist 10 a.m.).
- St. Paul's, North Vancouver BC (the parish's own page on netministries.org, 426 W Esplanade: Sunday Mass 11 a.m. at St. Paul's; the 9 a.m. Mass is at Infant Jesus of Prague, not this church).
- Rockefeller Memorial Chapel, Chicago (rockefeller.uchicago.edu: Sunday 11 a.m. October to mid-May; open to the public Tuesday to Friday 11 to 5).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Old St. James Anglican, Winnipeg (Tylehurst St) | stjamesanglicanchurch.ca, rupertsland.ca St. James | The parish's services are at the newer church, 195 Collegiate St; nothing for the old church |
| St. Anne's, Poplar Point MB | rupertsland.ca/manitoba-north/st-anne | Diocese page gives only "Hwy. 26", no times |
| Frelsis Lutheran, Grund MB | rmofargyle.ca/churches (the owner, the RM of Argyle) | History only; the congregation joined Baldur Immanuel in 1964; points to a Facebook page |
| St. Elias Ukrainian Orthodox, Sirko MB | uocc.ca/parish/st-elias-parish-7/ | Parish listed, no service times |
| Griswold United MB | rmofsifton.com/places-of-worship | A municipal directory says "Griswold worship service every 2nd and 4th Sunday at 9:30 am"; a directory, not the church's own page, so not recorded |
| St. Paul's Anglican, Churchill MB; Our Lady of Seven Sorrows, Camperville MB | searches | No page of the parish's own found |
| St. John the Divine (Sipiweske Museum), Wawanesa MB; St. Michael's, Trembowla MB | searches | Only directories (Travel Manitoba, Association of Manitoba Museums) |
| Old St. Mary's, Detroit | oldstmarysdetroit.com | HTTP 403; only mass-time aggregators otherwise. Worth another go with the web fetch tool |
| Trinity Episcopal, Bay City MI | trinitybaycity.org | That is a different Trinity (1010 33rd St); no page of this church found |
| First Unitarian (100 N State St), Ann Arbor MI | none | **No longer a church**: the place's note says it is a private office building |
| Christ Church, Hope BC | vancouver.anglican.ca/yale/christ-church-hope | Diocese page says weekly services, gives no times |
| Gur Sikh Temple, Abbotsford BC | canadiansikhheritage.ca | Temple page has no hours; the book-a-tour page reset the connection |
| Holy Cross, Skatin BC | none | First Nation village; no page; left as view |
| Saints Peter and Paul, New Hradec ND | Dickinson bulletins (searches) | Only an old newspaper directory line (Sunday 11 a.m., 2022); not recorded |
| Old Stone Church, Buffalo ND; South Wild Rice, Galchutt ND; Our Savior's, Coulee ND | none further | Kept by a historical society or cemetery association; no visiting times found |
| Rembert Church, Woodrow SC; Hebron, Bucksville SC; Stoney Creek Chapel, McPhersonville SC | SC historic properties records | No page of a congregation's own |
| B'nai Sholom Temple, Quincy IL | stlpr.org 2019 | **Closed and sold**: last service 2019, now private |
| Cumberland Presbyterian (Musicians Hall), Peoria IL | none | **Not a church**: a bank branch, per the place's note |
| Emmanuel Lutheran, La Crosse WI | emmanuellutheranchurch.360unite.com | That is Emmanuel, Elk River MN |
| Wesley UMC, La Crosse WI | wesleyunited.org | That is Wesley United, Austin TX; no La Crosse page found |
| St. James, La Crosse WI | searches | Only mass-time aggregators |

## Tips for the next session
- Manitoba's rural churches rarely have a page of their own; the provincial heritage pages give owners, not times.
- Several places listed as waiting churches are not churches any more (Ann Arbor office, Peoria bank, Quincy temple); a places session could set them to `view` with a plain note so they stop being asked.
