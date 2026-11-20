# hours_yytg: hours for 24 places of worship in New York, Nova Scotia and Vermont
state: Nova Scotia
region: ns
date: 2026-11-20
places: 0
file: hours_yytg.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last five New York churches from `tools/hours.py list "New York" --kind worship`, all thirteen waiting in Nova Scotia, and six of Vermont's thirteen were looked up. Fourteen got service times or opening hours from the page of whoever runs them, each read in the session with `tools/hours.py page` and its address checked against the place; ten are recorded `?`.

Hours recorded:
- Nova Scotia, Anglican Diocese of NS and PEI pages and parish sites: St. Luke's, Annapolis Royal (stlukesannapolisroyal.com); St. John's, Lunenburg (stjohnslunenburg.org: Sunday times on the home page, the May-to-October daily opening on /visiting/, which gives no clock times); St. Barnabas', Blue Rocks (the diocese's parish page); St. James', Mahone Bay and Union Church, Indian Point (parishofmahonebay.ca, which lists Union Church's 4th-Sunday service); Old St. Edward's, Clementsport (the diocese's event page for its one annual service; no page giving the summer museum hours was found).
- Nova Scotia, own sites: St. Andrew's Presbyterian, Lunenburg (pccweb.ca); Trinity United, Mahone Bay (trinityunitedmahonebay.org); St. John's Lutheran, Mahone Bay (stjohnsmb.wordpress.com: its calendar shows the Sunday service at different times week to week, so no fixed time is recorded).
- New York: Bethel AME, Huntington (bethelamehuntington.org, 291 Park Ave; the page labels its 10 a.m. time "Summer").
- Vermont: South Starksboro Friends (the New England Yearly Meeting's page, 430 Dan Sargent Rd); Saint Anne's Shrine, Isle La Motte (its own mass-times page, season only); the Old Meeting House, East Montpelier (oldmeetinghouse.org, 1620 Center Road); St. John's Episcopal, Highgate Falls (Holy Trinity Swanton's page for it: no weekly services, used for special services and events spring to fall).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Old First Presbyterian, Huntington NY | oldfirstchurch.org/visitors/ | That site is an Old First church in Tallahassee, Florida. No site of the Huntington church's own was found |
| First Baptist, Charleston NY | nytownofcharleston.gov/history | Historical society owns it; only a historian's contact, no opening times. Tourism listings only otherwise |
| Reformed Dutch Church, Stone Arabia NY | visitmontgomerycountyny.com (a tourism listing) | No page of its own found |
| Trinity Lutheran, Stone Arabia NY | (web search only) | No page of its own found |
| Christ Church, New Ross NS | nspeidiocese.ca/programs/parish-of-new-ross | The diocese's parish page has the address but no service times; the parish has only a Facebook page |
| St. John Evangelist, LaHave Islands NS | lahaveislandsmarinemuseum.ca | The museum society keeps it; deconsecrated, used for an annual Fishermen's Memorial Service and events. The museum's own hours (100 LaHave Islands Rd) are not the church's |
| Zion Lutheran, Lunenburg NS | zionlutheranlunenburg.ca | That domain is now a casino advertising site, not the church. No other page of the congregation's own found |
| Goat Island Baptist, Upper Clements NS | atlanticbaptistheritage.omeka.net/items/show/11 | Status "Alternative Use"; owned since 2019 by the Goat Island Church Preservation Society, not a congregation. No opening times found |
| Starksboro Village Meeting House VT | starksboromeetinghouse.org | The society's own site; events only, no opening times |
| White Meeting House (Waterbury Congregational) VT | (web search; only directories) | No page of the church's own found |

Closed or sold: none found closed. Goat Island Baptist and St. John Evangelist, LaHave Islands are no longer congregations' churches (above); the entries may want their access notes updated by a places session.

## Leads
None.

## Tips for the next session
- Vermont still has seven churches waiting: Old West Church (Calais), Isle La Motte United Methodist, Union Meetinghouse (Ferrisburgh), Brownington Congregational, Cambridge Meetinghouse, Leicester Meeting House and Fletcher Union Church. Each had at most one search here and was left unrecorded, not `?`.
- The Anglican Diocese of NS and PEI keeps one page per parish under nspeidiocese.ca/<region>/parish-of-…; some give service times, all give the parish's own site if it has one. `curl` the region page to list them.
