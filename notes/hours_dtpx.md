# hours_dtpx: hours for 38 New York places (the last 6 churches, then museums, inns, halls)
state: New York
region: several
date: 2026-11-21
places: 0
file: hours_dtpx.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. `tools/hours.py` showed only six churches still waiting anywhere, all in New York; after them came New York's other open-to-visitors places from `tools/hours.py list "New York"`. Thirty-eight were looked up: seven got hours from the page of whoever runs them, read in the session; thirty-one are recorded `?` after two tries (a search, then the place's own site or the best candidate).

Hours recorded (address or town on each page checked against the place):
- Beekman Arms, Rhinebeck: Beekman Arms & Delamater Inn dining page (6387 Mill Street). Open. The page's meal labels sit beside the times and were read as brunch, lunch and dinner from their order.
- The Sagamore, Bolton Landing: Opal Collection page for The Pavilion (110 Sagamore Road): hotel check-in and the Pavilion's Friday and Saturday hours only; whether that is seasonal was not shown.
- Troutbeck, Amenia: its Eat & Drink page (515 Leedsville Road) says the Dining Room is open to the public. Open.
- Schenectady City Hall: the city's home page (105 Jay Street) gives "Opening Hours: 8am - 4pm" with no days.
- Walton Theatre: its own site (30 Gardiner Place): regular film times; live shows on other dates.
- Fly Creek Grange: Fly Creek Area Historical Society meetings page: public meetings in the Grange, April to October, fourth Wednesday 6:30 p.m.
- Watts de Peyster Fireman's Hall, Tivoli (the village hall): Village of Tivoli "Office and Officials" page: the Monday to Friday 9 to 4 hours are listed under the treasurer, so they were recorded as hers, not as the building's.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Oak Hill Methodist, Durham | nylandmarks.org | No page of the congregation's own found; only directories |
| St. Paul's Lutheran, Oak Hill | two searches | No page of its own found |
| Grace Methodist (Mountain Community), Speculator | unyumc.org search | No conference page for it found |
| Church of the Transfiguration, Blue Mountain Lake | albanyepiscopaldiocese.org | Diocese page names a summer vicar but gives no times |
| Greenville Presbyterian, Greenville | two searches | greenvillechurch.org is a Scarsdale church, not this one |
| Wells Baptist Church (The Revival) | two searches | Private events venue; no page of its own |
| Miss Amelia's Cottage | amagansetthistory.org | No hours on the page |
| Stissing House | stissinghouse.com | Drawn by script |
| Bartlett House | bartletthouse.com, Toast page | No times; Toast refused (403) |
| Crandell Theatre | crandelltheatre.org /visit and /tickets | No box-office hours |
| Shirt Factory, Glens Falls | shirtfactorygf.com, events subdomain | No times; subdomain would not connect |
| Rivoli Theatre | scdw.net | No times |
| Irondequoit Inn | irondequoitinn.com | 403 |
| Horseheads depot museum, Zim House | horseheadshistoricalsociety.org | Would not connect |
| Durham Center Museum | durhamcentermuseum.org | Would not connect |
| Overackers Corners Schoolhouse | middlesexheritagegroup.org | Would not connect |
| Pulp Mill Museum | hadleylakeluzernehistoricalsociety.org | Would not connect |
| Old Allegany County Courthouse | angelicany.org | No office hours on the page |
| Rockwells Mills Old Mill | guilfordny.gov hamlet page | No times |
| Kelly Round Barn | pakatakan.com | Drawn by script (market days not read) |
| Fireman's Hall, Alfred | alfredny.org | 403 |
| Henry Lloyd Manor | huntingtonny.gov page, lloydharborhistoricalsociety.org | No times; 403 |
| Mt. Van Hoevenberg bobsled run | lakeplacidlegacysites.com | 403 (lakeplacid.com is a tourism site, not used) |
| Grooms Tavern | passageport.org, old cliftonpark.org page | No times; 404 |
| Quackenbush House (Olde English Pub) | theoldeenglish.com | HTTP 522 |
| Albany Pump Station | evansale.com | **The domain now serves unrelated spam; the brewery's site seems to have moved or lapsed.** A person may want to check the place's links |
| Sherman Free Library | shermanfreelibrary.org | Drawn by script |
| Mountainside Free Library | queensburyny.gov library page | 403 |
| Utica Union Station | oneidacountyny.gov project page | No hours |
| Queensbury Hotel | queensburyhotel.com | 403 |

No church was found closed or sold in this batch (Wells Baptist was already known to be a private venue).

## Leads not finished
- The New York post offices left waiting were not tried: earlier notes say USPS pages give no usable hours to these tools.
- Several "?" places have sites that are drawn by script or refuse plain fetches; a session with a browser could fill them.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
