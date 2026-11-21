# hours_bvka: hours for 31 places of worship in eight states
state: New York
region: ny
date: 2026-11-21
places: 0
file: hours_bvka.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last five New York places of worship, then most of those waiting in Vermont, Mississippi, Connecticut, Hawaii, Massachusetts, Maine and Pennsylvania, were looked up. Seven got service times from the page of whoever runs them, each read in the session with `tools/hours.py page` (or `tools/page.py`) and its address checked against the place; twenty-four are recorded `?`.

Hours recorded (all marked open):
- Avon Congregational, Avon CT: avon-church.org (6 West Main St).
- Old Trinity Church, Brooklyn CT: oldtrinity.net, one historic Anglican service a year on Trinity Sunday.
- First Church of Christ, Farmington CT: firstchurch1652.org (75 Main Street).
- First Church of Christ, Wethersfield CT: firstchurch.org/visiting. The page names a traditional and a contemporary Sunday service but gives no times except the 10 a.m. combined service on first Sundays; that is what is recorded.
- Old Kennett Meetinghouse PA: kennettfriends.org, worship there on the last Sunday of June, July and August; no time given.
- St. Benedict's Painted Church, Honaunau HI: thepaintedchurchhawaii.org (84-5140 Painted Church Rd), mass times on the home page.

Not checked: nothing was seen on the ground and no telephone call was made. The web fetch tool could not be used (its approval goes unanswered in an unattended run), so archived copies that `page.py` could not fetch were not read.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Church of the Messiah, Glens Falls NY | messiahgf.org (linked from the Albany diocese page, which gives 296 Glen St but no times) | 403; no archived copy readable |
| Society of Friends Hall, Glens Falls NY | web search only | No page of whoever uses it now |
| Voorhees Computing Center (RPI chapel), Troy NY | archives.rpi.edu | A university building, no visiting times |
| Bush Memorial Center, Troy NY | hmdb.org | College hall, events only; no page with times |
| First Baptist, Troy NY | baptistnews.com | Sold; a fraternity house (see below) |
| Isle La Motte United Methodist VT | champlainislandsumcworship.org | The domain now carries gambling spam, not the church |
| Old West Church, Calais VT | web search | Only concert listings on Front Porch Forum; no page of its own |
| Union Meetinghouse, Ferrisburgh; Brownington Congregational; Cambridge Meetinghouse; Leicester Meeting House VT | web search | No page of their own found |
| Sacred Heart Church, Grand Gulf MS | grandgulfpark.ms.gov/church | Connection fails; the archive copy (2026-07-13) could not be fetched |
| Rodney Presbyterian MS | rodneyhistory.org/rodney-presbyterian | Connection reset; the archive copy (2025-09-06) could not be fetched |
| Christ Church, Church Hill MS | dioms.org news page | Only a 2020 bicentennial notice; no weekly times found |
| First Presbyterian, Port Gibson MS | web search | No page of its own found |
| Mokuʻaikaua Church, Kailua-Kona HI | mokuaikaua.com | Phone numbers only, no service times |
| ʻImiola Church, Waimea; Kalahikiola Church, Kapaau HI | web search | No page of their own found |
| St. Patrick's, Newcastle ME | 8yqx7a.sites.ecatholic.com/st-patricks (All Saints Parish) | 403 |
| Union Church, Riverton CT; Old St. Mary's, Warwick PA; Chichester Friends PA; Apponegansett Meeting House MA; Warren First Congregational (Emmanuel Orthodox) MA; The Grotto, Nesquehoning PA | web search | No page of their own found |

Closed or sold: First Baptist Church of Troy is a fraternity house (the place already says so). None other found closed.

## Leads
None.

## Tips for the next session
- Still waiting and not tried here: Fletcher Union Church VT; Temple Gemiluth Chessed, Oakland Memorial Chapel and Bethel Presbyterian MS; Ahuʻena Heiau and Hale Hālāwai O Hōlualoa HI; Unitarian Meetinghouse, Brooklyn CT; Pembroke Friends, Old Parish Sheffield, Old Stone Church West Boylston MA; Maine's four meetinghouses; Uwchlan Meetinghouse PA.
- Small rural meetinghouses and historic churches in these states rarely have a page of their own; the yield was under one in four. A session after more hours would do better on museums or on states with active parish sites.
- A search for a church's name often returns a same-named church elsewhere (a Messiah Episcopal in St. Paul MN, a St. John's in Warren OH): check the address on every page.
