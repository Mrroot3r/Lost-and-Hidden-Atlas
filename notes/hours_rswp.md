# hours_rswp: hours for 32 places of worship in New York and New Hampshire
state: New York, New Hampshire
region: ny, nh
date: 2026-11-20
places: 0
file: hours_rswp.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last 20 New York places of worship waiting in `tools/hours.py list "New York" --kind worship`, then all 12 waiting in New Hampshire. Four got times from a page of whoever runs them, read in the session; 28 are recorded `?` after two searches turned up no page of their own with times. New York now has no church waiting; New Hampshire has none either.

Hours recorded (the page read is in the file):
- Agudas Achim, Livingston Manor: the congregation's own home page says monthly Shabbat services on the first or second Friday, visitors invited; no clock time on that page (an older 2021 page gave 7:30 p.m., not used).
- Holy Resurrection Orthodox, Berlin NH: the Orthodox Church in America's parish page, address 20 Petrograd St checked.
- Dover Friends Meetinghouse NH: New England Yearly Meeting's 2026 meeting listings (PDF), Dover Monthly Meeting at 141 Central Ave, Sunday 10:30 a.m.
- Third Fitzwilliam Meetinghouse (Town Hall) NH: the town's own "How do I" page, Selectmen's Office hours under "What are the Town Hall hours?"; Town Hall is 13 Templeton Turnpike per the same page.

Not checked: nothing was seen on the ground and no call was made. No church was found to be closed or sold, but First Baptist, Cohoes has its records at the New York State Library, which may mean the congregation is gone (the library page would not open): worth a look.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| Fly Creek Methodist; Newtonville Methodist | unyumc.org church pages | The Upper New York conference's church pages answer 404 now (the site seems rebuilt); an archived copy of Fly Creek's page from 2026-02-06 exists |
| Mentz Church, Montezuma | townofmontezuma.org/?p=3709 | 403 to scripts, no archived copy |
| Dover Friends | fgcquaker.org, quaker.org | 403; the NEYM listing PDF was used instead |
| Park Hill Meetinghouse | westmorelandhistoricalsociety.org | 403 |
| Sandown Old Meetinghouse | sandown.us/node/6279 | Connection reset |
| Fremont Meeting House | fremont.nh.gov/node/1759 | 404 |
| New Durham Meetinghouse | newdurhamnh.us/node/65 | 404 |
| Trinity Church, Holderness | trinitychurchyardcemeteryassociation.org | Says it is available for weddings and services; gives no dates |
| Norway Baptist (History Center) | mohawkvalleymuseums.us | An association's listing, not the society's own page; says call for admission |
| The rest (Log Cabin Church, Hartford Baptist, Lordville, Camroden, Taylor Center, Richville Welsh, Mount Moriah, Hartwick Seminary, Reformed Church on Staten Island, St. Andrew's Walden, Calvary McDonough, First Baptist Carthage, Sand Beach, St. Peter's Spencertown, Centre Village Enfield, Danville, Rindge, Stark Union Church) | searches | No page of their own found; only directories, Wikipedia and markers |

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (3 tips).
