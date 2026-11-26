# hours_rjxg: hours for the last four New York churches, then 26 museums and other open places in New York, West Virginia and Massachusetts
state: several (New York, West Virginia, Massachusetts)
region: several
date: 2026-11-22
places: 0
file: hours_rjxg.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. New York had four churches waiting, the last anywhere; after them no church waited in any state, so the session went on to the other places that take visitors (`tools/hours.py list` without `--kind worship`): New York, then West Virginia and Massachusetts. Thirty places were looked up: six got hours from the page of whoever runs them, read in the session; twenty-four are recorded `?`.

Hours recorded (address or town on each page checked against the place):
- Amsterdam City Hall (Sanford Mansion): City of Amsterdam, City Clerk's Office page (61 Church Street on the page). Monday to Friday 8 to 4.
- Old Post Office (Oneonta City Hall): City of Oneonta, City Clerk page (258 Main Street; Wikipedia says city offices moved into the old post office in 1980). Weekdays 8 to 4.
- Graceland, Elkins: Davis & Elkins College facility page (160 Graceland Drive). Restaurant dinner and brunch times.
- Cass company town: WV State Parks, Cass Scenic Railroad additional-information page (12363 Cass Road). Park hours only.
- Mansion House, Point Pleasant, and Lighthorse Harry Lee Cabin, Lost River: WV State Parks park pages. Park hours only; the house's and the cabin museum's own days are not on those pages, and the row says so.

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Columbus Community Church, Columbus NY | searches only | No site of its own found |
| Peekskill Presbyterian Church | searches only | Only directories |
| Rockdale Community Church | searches only | No site of its own found |
| First Presbyterian, Bainbridge NY | searches only | Only directories |
| Rochester City Hall | cityofrochester.gov/locations/rochester-city-hall | HTTP 403; an Internet Archive copy of 2026-07-08 exists but the fetch was not approved unattended |
| Windfall Dutch Barn | townofmindenny.gov points of interest | Address and telephone, no hours |
| Starr Clark Tin Shop, Mexico | searches | Only tourism directories |
| Galli-Curci Theatre, Margaretville | searches | Only directories |
| The Tepee, Cherry Valley | searches | Only directories and news |
| Fountain Arts Center, Belmont | searches | Only the county arts council's listing |
| Paddock Arcade, Watertown | searches | Only directories |
| Batcheller Mansion Inn | batchellermansioninn.com | Address only, no hours |
| The Moviehouse, Millerton | searches | Only showtime aggregators |
| Williamsville Water Mill | searches | Only history pages |
| West Virginia State Capitol | wvculture.org FAQ | Gives the State Museum's hours, not the capitol's tours |
| Camden Park, Huntington | searches | Only tourism listings |
| Beckley Exhibition Coal Mine | searches | Only directories and e-WV |
| B&O Martinsburg Roundhouse | nps.gov "explore the roundhouse" | Its hours read as the park's, not the Roundhouse Authority's |
| Glen Ferris Inn | glenferrisinn.com | Telephone and address, no hours |
| West Brookfield depots | westbrookfield.org (Quaboag Historical Society) | Post-office box only |
| Miss Worcester Diner, Boulevard Diner | searches | Only directories and news |
| New Bedford Fire Museum | searches | Only directories |
| Jabez Howland House | pilgrimjohnhowlandsociety.org | HTTP 403 again |

## Left waiting on purpose
About fifteen New York post offices (Beacon, Whitehall, Troy, Hudson and others) and the Old Essex County Courthouse were not recorded at all, so a later session can still try them. The USPS locator page (tools.usps.com/locations/details/...) draws its hours by script and the page reader gets a sample page; in a headless browser the hours stayed blank too. Essex County's treasurer page gives office hours (September to April Monday to Friday 9 to 5; May to August 8 to 4) but does not say the office is in the old courthouse.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
