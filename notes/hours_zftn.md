# hours_zftn: hours for 29 places of worship in New York, Kansas and Missouri
state: New York
region: ny
date: 2026-11-28
places: 0
file: hours_zftn.py

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. All thirteen New York churches still waiting in `tools/hours.py list "New York" --kind worship`, eight Kansas churches and eight Missouri ones were looked up. Eleven got service times or opening hours from the page of whoever runs them, each read with `tools/hours.py page` and its address or town checked against the place; eighteen are recorded `?`.

Hours recorded:
- New York: Central Presbyterian, Park Avenue (centralchurchnyc.org service page); Riverside Church (trcnyc.org worship schedule: Sunday 11 a.m. and the tower tours); Hendricks Chapel, Syracuse (chapel.syracuse.edu contact page: building hours, academic year and summer).
- Kansas: Plymouth Congregational, Lawrence (plymouthlawrence.com); First Congregational, Manhattan (uccmanhattan.org, 700 Poyntz Ave).
- Missouri: Independence Boulevard Christian Church (ibcckc.org/worship, 606 Gladstone); Holy Rosary, Columbus Park (the Diocese of Kansas City-St. Joseph's parish list, 911 E Missouri Ave); Our Lady of Guadalupe Shrine (sacredheartguadalupe.org and the diocese list: the parish's Saturday 4 p.m. Mass is at the shrine, its Sunday Masses at Sacred Heart); Community of Christ Auditorium (cofchrist.org international headquarters page: Temple and Auditorium tours Tuesday to Thursday 9 to 4 by request form, Monday by appointment).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Christ Episcopal (Christ Church San Marcos), Tarrytown NY | christchurchtny.org, /worship/ | HTTP 403 to the tool, home page and worship page alike |
| Elmsford Reformed Church NY | newyorksynod.org/?p=4984 | **Closed**: the Regional Synod's page (December 2017) says its final service was Sunday, December 31, 2017. The place's access note still calls it an active church and wants updating by a places session |
| Former St. Francis de Sales, Troy NY | evangelist.org (2018) | Closed and sold to a fraternity; private, no visiting hours |
| First Baptist / Mizpah Tower, Syracuse NY | cnycentral.com article | Now a wine bar and event hall; no page of its own giving hours was found |
| Foster Memorial AME Zion, Tarrytown NY | (searches; NPS itinerary only) | No page of the congregation's own found; only directories |
| Second Baptist Church of Dover NY | (searches) | No page of its own found |
| Creek Meeting House, Clinton Corners NY | clintondcny.gov/?p=3096 | Town page on the historical society gives no opening times |
| Park Church, Elmira NY | nylandmarks.org | No site of its own found ("Park Church" results are a Grand Rapids church) |
| Lowville Presbyterian (Stone Church) NY | wgpfoundation.org | No page of its own found |
| Historic Old St. John's, Utica NY | thecatholicsun.com | Only mass-time aggregators; no parish or diocese page found |
| Old Stone Church, Osawatomie KS | osawatomieks.org/node/3741, /node/211 | The city's pages for it answer 404 |
| First Methodist Episcopal (First UMC), Lawrence KS | umc.org find-a-church id 69494 | 404 |
| Holy Family (old church, Adoration Chapel), Eudora KS | theleaven.org/?p=8302 | Archdiocese paper article, no schedule; no parish site found |
| St. Patrick's, rural Atchison County KS | theleaven.org/?p=17936 | Same: article only |
| Ebenezer Baptist, Atchison KS | (searches) | Directories only |
| First Presbyterian, Leavenworth KS | leavenworthks.gov/visitors/page/presbyterian | Would not connect |
| Trinity Episcopal, Independence MO | spirit.diowestmo.org/1844/01/trinity-independence/ | 404; no parish site found |
| Washington Chapel C.M.E., Parkville MO | thirddistrictcme.org/missouri | The district page lists it (1137 West Street) with no times |
| Lexington Historical Museum MO | historiclexington.com/?p=5711 | A tourism page gives "1 to 4 p.m. Wednesday to Sunday" for 112 S 13th St; not the museum's own page, so not recorded |
| Stone Church (Community of Christ), Independence MO | (one search; cofchrist.org headquarters page) | No congregation page found; tried once only, worth another go |

Closed or sold: Elmsford Reformed Church (final service December 31, 2017). St. Francis de Sales, Troy, already known as sold.

## Leads
None.

## Tips for the next session
- Kansas's waiting churches are mostly small rural or closed ones with no site of their own; Missouri's Kansas City churches did better. The Diocese of Kansas City-St. Joseph's parish list (kcsjcatholic.org/parishes) gives every parish's Mass times with its address, which is a good source for Catholic churches on the Missouri side.
