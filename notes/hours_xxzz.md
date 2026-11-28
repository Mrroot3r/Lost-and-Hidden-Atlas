# hours_xxzz: hours for 26 places of worship in eighteen states and provinces
state: Louisiana
region: la
date: 2026-11-28
places: 0
file: hours_xxzz.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. No New York church was waiting, so the 58 churches still waiting anywhere were listed together (`tools/hours.py list --kind worship --n 60`) and worked through in the order given; most of them had been tried before. Thirteen got service times, tour times or a status from the page of whoever runs them, read with `tools/hours.py page` or, where the shell was refused (HTTP 403), with the web fetch tool; each page's address or town was checked against the place. Thirteen are recorded `?`.

Hours recorded:
- St. Stephen's Memorial Episcopal, Lynn MA (ststephenslynn.org/worship, 74 South Common St).
- First Presbyterian, Hot Springs AR (firstpreshotsprings.org, 213 Whittington Ave; "Morning Worship 10:30 am", no day printed beside it).
- St. Louis Cathedral, New Orleans LA (stlouiscathedral.org/mass-schedule; the cathedral's tours page also says it is open daily 9 a.m. to 4 p.m., not in the row).
- Old Ursuline Convent, New Orleans LA (stlouiscathedral.org/about/tours: museum tours Thu, Fri, Sat, Mon at 10, 11 and 1; 1112 Chartres St).
- St. Francis of Assisi, Sacramento CA (stfrancisparish.com schedule; the day headings of the weekend block did not come through, so the row says "weekend Masses").
- St. Paul's Memorial (United Methodist), South Bend IN (stpaulsmemorial.com, 1001 W Colfax Ave).
- St. Aloysius, Spokane WA (stalschurch.org/mass-schedule, 330 E Boone Ave).
- Cathedral of Our Lady of Lourdes, Spokane WA (the Diocese of Spokane's parish finder, 1115 W Riverside Ave; its weekday line is written "MSa 7:00 AM, 12:00 PM", recorded as weekday Masses).
- Sisters Chapel, Spelman College, Atlanta GA (spelman.edu religious life: Sunday 1 p.m. in the academic year).
- Temple Emanuel, Pueblo CO (templeemanuelpueblo.net home page: weekly Shabbat services and holidays, all invited; no times. Its /shabbat page reset the connection and the fetch tool was refused).
- Paris Tabernacle ID (churchofjesuschrist.org historic site: guided tours of about 30 minutes, contact for hours).
- St. Mark's Episcopal, Tonopah NV (ednv.org find-a-church: no regular services; another church uses it on Sundays).
- Christ Church, Maugerville NB: **closed**, see below.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Holy Transfiguration Chapel, Ninilchik AK | oca.org/parishes/oca-ak-nintol | OCA directory entry: served by diocesan clergy, no times |
| Rexburg Tabernacle ID | rexburgid.gov/o/arts/page/tabernacle/ | City arts page gives no opening hours (and two different addresses) |
| Mission San Xavier del Bac, Tucson AZ | sanxaviermission.org | HTTP 403 to the shell; the fetch tool was refused too |
| St. Dominic's (Maine Irish Heritage Center), Portland ME | maineirish.com | No hours on the page, drawn by script |
| St. Mary's (Steeple Square), Dubuque IA | steeplesquare.org | Connection reset; the tourism listing has no hours |
| Cathedral of Saint Joseph, Sioux Falls SD | stjosephcathedral.net (from the diocese's parish list) | HTTP 403; fetch tool refused |
| Cathedral Basilica, Mobile AL | mobilecathedral.org | HTTP 403; fetch tool refused |
| Kaʻahumanu Church, Wailuku HI | (two searches) | No page of its own found |
| First United Methodist, Tulsa OK | (two searches) | No page of its own found; firstchurchtulsa.org is First Presbyterian, not this church |
| Central Methodist (Asbury UMC), Atlantic City NJ | umc.org find-a-church id 13688 | 404; a 2023 conference article mentions jazz vespers on the 4th Sunday, too old to record |
| Old Hay Bay Church, Adolphustown ON | ucheritage.ca/?p=102 | United Church heritage page, no times; the county tourism page refused |
| First Baptist, Parkersburg WV | (two searches) | No page of its own found |
| First Congregational, Sioux Falls SD | (two searches) | No page of its own found |

Also looked at and not recorded: St. Vincent de Paul, Mobile AL (an ecatholic "SVdP" page gave times but printed no address, so it could not be tied to this church); Salt Lake Temple (closed for renovation, open house 2027, then members only); Église Saint-Pierre-aux-Liens, Caraquet NB (only the town's page, with town-office hours).

Closed or sold: **Christ Church, Maugerville NB was deconsecrated on November 2, 2025** (Anglican Diocese of Fredericton, "Deconsecrated Churches" page). Its access note still describes a parish church and wants updating by a places session.

## Leads
None.

## Tips for the next session
- Many parish sites (ecatholic, Squarespace, cathedral sites) answer 403 to the shell but open in the web fetch tool, which can be refused in an unattended run; ask it for several pages in one go.
- Diocesan parish finders (Spokane's at pvqxa.sites.ecatholic.com/parishfinder, the Episcopal Diocese of Nevada's ednv.org/find-a-church) give times with addresses and count as the denomination's page.
- The worship list left is mostly churches with no site of their own; museums are next once it runs dry.
