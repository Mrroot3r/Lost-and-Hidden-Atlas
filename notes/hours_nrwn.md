# hours_nrwn: hours for 30 New York places of worship
state: New York
region: ny
date: 2026-11-19
places: 0
file: hours_nrwn.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. Thirty New York places of worship from `tools/hours.py list "New York" --kind worship --n 30` were looked up. Nine got service times or opening hours from the page of whoever runs them, each read in the session with `hours.py page`; twenty-one are recorded `?` because no page of their own gave any.

Hours recorded (the page read is in the file):
- Zion Episcopal, Morris, and All Saints Chapel, Morris: the Diocese of Albany's pages.
- Church of St. Andrew, Richmondtown, and St. Paul's, Chittenango: the Episcopal Church's own listing (episcopalassetmap.org), address checked on each.
- Reformed Dutch Church of Claverack: its own site.
- Willard Memorial Chapel, Auburn: its own site, willard-chapel.com (willard-chapel.org is a parked domain).
- St. Ann Maronite (Ohio Street Methodist), Watervliet: the Eparchy of Saint Maron's parish list. The parish's own site, stann1905.com, gives no times and its newest post is from 2020.
- Holland Patent Stone Churches: only First Presbyterian ("the Twin Churches", 7835 Church Street), from its own site, whose footer is dated 2021, so the time may be old. Nothing was found for Grace Episcopal or the other churches on the green.

Not checked: nothing was seen on the ground, and no telephone call was made. Whether the Twin Churches page describes the same stone buildings the pin stands for was not confirmed beyond the street address.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Trinity Chapel, Morley | albanyepiscopaldiocese.org/trinity-church-morley-ny/ | Opens, no service times. The diocese's county list puts it in the care of Grace Church, Canton, whose site mentions a "Morley Chapel friends' event" and no hours: occasional openings only, by the look of it |
| Smithfield Presbyterian (National Abolition Hall of Fame), Peterboro | nationalabolitionhalloffameandmuseum.org | No days or hours on the page. peterborony.org has the 2024 season only (not used) |
| Stone Meeting House, Remsen | villageremsen.digitaltowpath.org:10043 | Connection reset; the society's own site, Remsen-Steuben-History.org, would not connect |
| St. Paul's, Waddington | albanyepiscopaldiocese.org/447-2/ | The county list gives an address (129 Lincoln Ave) and telephone, no times; the parish has no page of its own on the diocese's site |
| Fort Herkimer Church | mohawkvalleymuseums.us/museums/fort-herkimer-church/ | No times; tours by appointment, as the place's note already says |
| Fenner Baptist (Community) Church | townoffenner.com/fenner-community-church/ | The town's page says it "holds seasonal services" and gives no dates or times |
| Guilford Center Presbyterian | guilfordhistoricalsociety.blogspot.com | Posts from 2010 to 2013, no hours; chenangohistorical.org/town/guilford/ answered 403 |
| Helderberg Lutheran (St. Paul's), Berne; First Reformed, Berne | albanyhilltowns.com | Would not connect. No page of either congregation was found; a newspaper shows the Lutheran church in use in 2025 |
| Bloomingburg Reformed Dutch Church | sullivancatskills.com listing | Empty; no page of the foundation was found. A 2018 news story says the town made the foundation compete for the lease, so who runs it now is not known |
| Dexter Universalist Church | northcountryatwork.org; villageofdexterny.gov | The first returns an error, the second has no museum hours |
| Holland Patent, Grace Episcopal | cnyepiscopal.org | 403 |
| South Granville Congregational; Ten Mile River Baptist; Upperville Meeting House; McGraw Presbyterian; Old School Baptist, Halcottsville; First Presbyterian, Cherry Valley; Livingston Memorial Church; Fort Miller Reformed; St. Bernard's, Cohoes; First Presbyterian, Deposit; UCC of Wadhams | searches | No page of their own found in two or more tries: only directories, Wikipedia and Register files |

No church was found to be closed or sold.

## Leads

## Tips
- Web search gave titles only, and for a small rural congregation it returns directories almost every time. What worked: the denomination's own lists. The Diocese of Albany's pages (albanyepiscopaldiocese.org/<name>-<town>-ny/) and its county list at /447-2/; the Episcopal Church's episcopalassetmap.org (check the street address: a search for "St. Paul's" offers other towns' nodes); the Maronite eparchy's stmaron.org/parishes-n, which has a "Liturgical Schedule" for every parish.
- A village's or town's own site sometimes links the congregation (hollandpatentny.gov/religious-organizations led to twinchurches.org).
- pcusa.org and rca.org gave nothing usable for single congregations in this session.
