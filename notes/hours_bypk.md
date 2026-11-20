# hours_bypk: hours for 31 New York places of worship
state: New York
region: ny
date: 2026-11-20
places: 0
file: hours_bypk.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. Thirty-one New York places of worship from `tools/hours.py list "New York" --kind worship` were looked up. Four got service times from the page of whoever runs them, each read in the session with `hours.py page`; twenty-seven are recorded `?` because no page of their own gave any after two searches. Most of the `?` ones are small rural or museum-held churches that seem to have no web page of their own at all.

Hours recorded (the page read is in the file):
- St. Matthew's Episcopal, Moravia: the Episcopal Church's own listing (episcopalassetmap.org/node/2419), address 14 Church Street checked.
- St. Mark's Lutheran (Centerpointe Community Church), Guilderland Center: the congregation's own SermonAudio page, address 481 Route 146 checked.
- Owasco Reformed Church: its own site, which describes the church at the centre of the hamlet for over 200 years.
- First Presbyterian Church of Lansingburgh: the Upper New York Methodist conference's page for Cornerstone Community Church, 570 3rd Ave. The NRHP nomination for the former Methodist church (3rd Ave and 116th St) says the Methodist and Presbyterian congregations merged as Cornerstone and the Methodist building closed in 2006, so Cornerstone is taken to meet in the Presbyterian building. That 570 3rd Ave is the Presbyterian building on the old Green was not confirmed on a map: worth a look.

Not checked: nothing was seen on the ground, and no telephone call was made. No church was found to be closed or sold in this session.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Zion Church, Rome | cnyepiscopal.org | The diocese's site answered 403; zionepiscopal.org is Zion, Douglaston (Queens), not Rome |
| Christ Church, Binghamton | episcopalassetmap.org | No listing for it found; no parish site found |
| Church of the Holy Cross, Troy | rensselaernewman.org/mass-times/ | The RPI Newman masses are at the Chapel + Cultural Center and Our Lady of Victory, not Holy Cross |
| Batchellerville Presbyterian | edinburgny.gov/community/religous-organizations | The town's list says services in Batchellerville July and August 9 a.m. (Northville September to June). A town directory, so not used; a lead for the next session if the church's own page turns up |
| Seventh Day Baptist, DeRuyter | tromptown.github.io | The society's museum hours are for its old bank building at 712 Utica Street, not the church |
| Stone Mills Union Church | users.westelcom.com/stonemillsmuseum/ | The society's site was last updated in 2010 and gives no hours |
| Tomhannock Methodist | Pittstown Historical Society site | Says nothing of the church opening |
| Sand Lake Center for the Arts | its Squarespace overview page | No box office or event times on the page read |
| Hawleyton Methodist | unyumc.org | No page under the slugs tried; only the Town of Binghamton's event notices mention it |
| First Presbyterian, Cooperstown; Woodrow Methodist; Preston Hollow Baptist; First Methodist (Vineyard), Cohoes; Preble Congregational; Ohave Shalom, Woodridge | searches | Only directories and news found, no page of their own |
| Christian Church, East Delhi; White Store Church; Union Valley; Otsdawa Baptist; Second Old School Baptist, Roxbury; Snells Bush; Christ Episcopal, Belvidere; East Genoa; Trinity, Fairfield; Nelson Welsh; Heritage Hall, Cincinnatus; Reformed Dutch, Latham | searches | Only Wikipedia, NRHP, HMdb and history pages; none gives opening times |

## Tips for the next session
- The search engine available here returns few small-church sites; the denomination listings work best: episcopalassetmap.org/node/<n> (Episcopal) and unyumc.org/find-a-church/<slug> (Upper New York Methodists).
- White Store Church holds a public Memorial Day service and summer socials (Evening Sun news, 2018 and 2019); an annual event page of its own would give it hours.
