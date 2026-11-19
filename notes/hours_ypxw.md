# hours_ypxw: hours for 28 New York places of worship and old churches
state: New York
region: ny
date: 2026-11-19
places: 0
file: hours_ypxw.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. Twenty-eight New York places from `tools/hours.py list "New York" --kind worship` were looked up. Nineteen got service times or opening hours from the page of whoever runs them, each read in the session; nine are recorded `?` because no page of their own gave any.

Hours recorded (the page read is in the file; the address on each page was checked against the place):
- The Diocese of Albany's pages: Christ Church, Cooperstown; St. John's, Johnstown; Calvary, Burnt Hills; Zion, Colton (the church only: the town's museum page gives no museum hours).
- The Episcopal Church's own listing (episcopalassetmap.org): St. Mary's, Springfield Center (node 2020) and Christ Church, Walton (node 2029). The diocese's pages for these two give no times.
- Their own sites: Trinity, Roslyn; St. John in the Wilderness, Copake Falls; Pullman Memorial, Albion (the home page lists each coming Sunday at 11:00 a.m.); St. Nicholas Ukrainian, Watervliet (cerkva.com); Holy Trinity Monastery, Jordanville; Congregation Bnai Israel, Fleischmanns (summer season only; the page says "Weekly services resume June 2026", so it is a season old); Emmanuel, Norwich (bigreddoor.squarespace.com: worship moves among three churches, so no fixed time is recorded); Hamilton Union, Guilderland (an undated brochure page on its own site).
- St. Mark's, Hoosick Falls: its own site gives only a Wednesday evening service ("A Table in the Wilderness"; the day is on /ministries, the times on the home page) and no Sunday time.
- William Miller farm and chapel: Adventist Heritage Ministries' page for the farm (tours, pre-registration asked).
- Universal Preservation Hall, Saratoga Springs: the Proctors Collaborative box-office page; it opens for shows, not at set visiting hours.
- Broad Street United Methodist, Norwich: the Upper New York conference's page, which gives "Main Service" times and no day.
- First Old School Baptist Church, Denver: the Roxbury Arts Group lists it as a venue; recorded as no regular hours, and not marked open.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Matinecock Friends Meetinghouse | nyym.org/matinecock/ (404); fgcquaker.org/quaker-finder/matinecock-friends-meeting/ | The Quaker finder page has the address (267 Duck Pond Rd) and a "Worship Times" heading with nothing under it |
| Jericho Friends Meeting House | fgcquaker.org/quaker-finder/jericho-friends-meeting/ | Same: address, empty "Worship Times". jerichofriends.org is a meeting in Winchester, Indiana |
| Jay Gould Memorial Reformed Church, Roxbury | roxburyny.gov/places-of-worship | The town's list gives address and telephone only; no site of the church's own was found |
| West Charlton United Presbyterian | albanypresbytery.org | 403; no site of the church's own was found |
| Hopewell Presbyterian, Thompson Ridge | hopewellpc.org/visiting | That site is a Hopewell Presbyterian in Franklin, Indiana. None found for the Town of Crawford church |
| First Congregational, Walton | (web search only) | No page of its own found |
| St. Paul's Lutheran, Dansville | stpaulslutheranchurch.snappages.site | That site is St. Paul's in Sioux City, Iowa; locator.lcms.org/church/C/207136 is St. Paul in Cortland. None found for Dansville |
| Old Stone Church, Rhinebeck | oldstonechurch.org | That site is the Old Stone Church in Cleveland, Ohio. None found for the Rhinebeck church |
| Petersburgh United Methodist | unyumc.org/find-a-church/petersburgh-umc | Opens with the right address (12 Head of Lane Road); "Main Service" is blank |
| Hamilton Union, Guilderland | hamiltonunionpresbyterianchurch.org | The tool gets 403 on the home page; the brochure page was read with the web fetch tool instead |

No church in this batch was found to be closed or sold.

## Leads
None.

## Tips
- Churches share names: three of the first sites a search offered were namesakes in other states (Indiana, Iowa, Ohio) and one a Zion in Douglaston, Queens. `hours.py page` prints the address line; read it before the times.
- For Episcopal churches in the Diocese of Albany try `albanyepiscopaldiocese.org/<name>-church-<town>-ny/` first; when it gives no times, the same church's episcopalassetmap.org page often does.
- unyumc.org/find-a-church/<town>-umc works for Upper New York Methodist churches, but "Main Service" is often blank.
- Not tried this session and likely to have pages of their own: First Presbyterian, Cooperstown; Reformed Church on Staten Island; Zion, Rome; St. Andrew's, Walden; Woodrow Methodist; Sand Lake Center for the Arts (slca.org is not it).
- Batchellerville Presbyterian: the Town of Edinburg's page says services there are in July and August at 9:00 a.m. (Northville the rest of the year). That is a town list, not the church's page, so it was not recorded; the Northville church's own page is the one to find.
