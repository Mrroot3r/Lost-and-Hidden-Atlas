# hours_dkdn: the last 40 churches waiting, then New York libraries and museums
state: several (New York, Saskatchewan, Utah, Indiana, and the last waiting churches in 19 states and provinces)
region: several
date: 2026-11-28
places: 0
file: hours_dkdn.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. When it began, 40 places of worship waited anywhere (none in New York). All 40 were looked up: 3 got times or an entry arrangement from the page of whoever runs them, and 37 are recorded `?`. With no church left waiting, the session turned to New York's other open places (libraries, museums, a music hall): 17 got hours. 57 entries in all: 20 with hours, 37 `?`.

Hours recorded (address or town on each page checked against the place):
- Notre Dame d'Auvergne, Ponteix: Archdiocese of Regina parish page (Ponteix Masses on a monthly rota). Open.
- Salt Lake Temple: Temple Square page (closed for renovation; public open house by reserved ticket April 5 to October 1, 2027). Not marked open, because it is not open now.
- South Bend Civic Theatre (former Christian Science church): the theatre's general-information page (403 N. Main Street; box office hours). Open.
- New York Public Library Carnegie branches (96th Street, Aguilar, Fort Washington, Mott Haven, Port Richmond, Melrose, Tompkins Square, Tottenville, 115th Street, Hudson Park, Columbus): nypl.org location pages, which are drawn by script, so they were read in a headless browser. The week read had a late noon opening on Friday December 4, so Fridays are given only as "until" the closing time.
- Mount Vernon, Canastota and Irvington (Lord & Burnham Building) libraries: their own sites (adult hours for Mount Vernon).
- Ticonderoga Heritage Museum: its own Google site; it says the season's dates are not yet set, so the row says so.
- Hancock House, Ticonderoga: the Ticonderoga Historical Society's hours page (6 Moses Circle), read through the web fetch tool because the shell could not connect.
- Tarrytown Music Hall: its ticket site (box office opens 3 hours before shows).

Not checked: nothing was seen on the ground and no telephone call was made.

## Churches recorded `?` (no page of its own with times found or readable)
Searched once or twice each this session, after an earlier session had also found nothing: St. Alphonsus (New Orleans), Harmony Presbyterian (Arkansas), Vibank Convent, Randolph Tabernacle (the church's ward page gave 404), Ilfeld Memorial Chapel, Williston-West (offices), Wakamiya Inari Shrine, Third Avenue United (Saskatoon), Gardiner Church (Battleford's town page has its history but no hours), old Dixwell library (New Haven), Ely tabernacle (now the Centennial Fine Arts Center; no page with hours), Winona Church, First Baptist (Bridgeport), Clear Creek Church (Camp Verde: rented through the historical society; no opening times), Hopewell Presbyterian (Oxford MS), First Presbyterian / St. Patrick's (Parkersburg), San Antonio de Padua (Pecos: only mass-time aggregators found), Nikolai chapel, Waihee Church, The Steeple (Mobile, event venue), Sardis Baptist, St. Vincent de Paul (Mobile: only aggregators), The Church nightclub (Denver), First Mission House (Bethel), Plymouth Congregational (New Haven, offices), Bridgeport Islamic Community Center (its site gives no prayer times without script; its PDF schedules are from 2019-20), First Christian (Tulsa, being converted), Presbyterian Mission Church (Las Vegas NM), The Abbey (San Diego, event venue), Visitors Chapel AME (Hot Springs), Zion Baptist (Collinsville), St. Luke's UMC (Dubuque: no site of its own found), Melville Ukrainian Orthodox, Saint-Pierre-aux-Liens (Caraquet: no parish page found), Oark church, Rock Church (Auburn WY).
Manti Temple is recorded `?`: the church's temple page gives closures, and the temple is entered by church members only.

No church was found closed or sold beyond what the place notes already say (event venues in Mobile, San Diego and Denver; offices in Portland and New Haven; Tulsa's church being converted).

## Pages that would not open
- bklynlibrary.org location pages: 403 to the shell and a bot check in the headless browser. The Brooklyn Carnegie branches still wait.
- queenslibrary.org: the shell cannot connect; through the web fetch tool, Poppenhusen's page showed no hours and the others were refused. The Queens Carnegie branches still wait.
- metmuseum.org (Met Cloisters): 429.
- nypl.org pages for Yorkville, Muhlenberg, 67th Street and Hamilton Grange did not draw their hours in time; try again.

## Tips for the next session
- nypl.org location pages need a browser: in Playwright, wait for the page to draw (about 7 seconds) and read the rows that start with a day name and a date. The rest of the NYPL Carnegie branches (Yorkville, Muhlenberg, 67th Street, Hamilton Grange, Washington Heights, Epiphany, Seward Park, Chatham Square, Webster, Morrisania, Harlem, St. Agnes, 125th Street) can be done the same way.
- Croghan Depot: the only hours found are on an undated page on nygenweb.net (Saturday 9 to 5, Sunday 1 to 4); not recorded, because it may not be the society's own current page.
- Warsaw Public Library's home page shows only the current week (it was Thanksgiving week); read it in an ordinary week.
- Post offices wait in numbers; the USPS locator is drawn by script.
