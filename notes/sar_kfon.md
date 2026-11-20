# sar_kfon: Saratoga County: Milton mill hamlets, Ballston, East Line and Stillwater
state: New York
region: sar
date: 2026-11-20
places: 14
file: data_sar_kfon.py

## What this batch is
Fourteen places in central and eastern Saratoga County, region `sar` drawn at random by `choose.py --claim`. The country round Galway had already been worked by `sar_wqmx` the day before, so this batch took what that one lacked: the Town of Milton's mill hamlets (Rowland's Hollow, the Eagle Mill at Craneville, Bloodville) and the Old Stone Church at North Milton, all from the town's November 2022 "Listing of Historic Structures and Places" (a PDF on the town's revize.com document centre, read with `page.py --all`); the Colonial Inn on Courthouse Hill and the Hubbell house in Ballston; the East Line meeting house of 1809; the Leland House at Mechanicville; the Stillwater Blockhouse Museum (hours from the Town of Stillwater's park page); the closed Petrified Sea Gardens; the Todd house in Saratoga Springs and the Garnsey house near Rexford (Wikipedia); the cobblestone house on Malta Avenue and the Gere house in Galway (HMdb markers only, so `conf='mixed'`). Several stories come from the Saratoga County History Center's "This Week in Saratoga County History" articles, which are PDFs on brooksidemuseum.org written by the town historians. Not checked: anything on the ground; the exact spot of the standing grist-mill corner at Rowland's Hollow and of the Eagle Mill walls (both area pins on the road); the Garnsey house position (Register list point on the road, no building in the ring); service times for the Old Stone Church (`hours='?'`); parking at the Blockhouse (no lot mapped, sources silent). Red brick was set only where a source says what the building is made of; the rest are `'?'`. Every place but the Blockhouse is private and `view`. The Courthouse Hill lead row in `notes/sar_wqmx.md` was deleted, since the Colonial Inn entry covers that ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Dirck Swart House | Stillwater village, Hudson Avenue (HMdb 36811 at 42.94094, -73.64894) | 1977 village marker: General Schuyler's headquarters August 3–14, 1777; Arnold marched from here to relieve Fort Stanwix | Whether the house stands (the village page `villageofstillwaterny.gov/?p=821` answered HTTP 500) |
| Yellow Meeting House and cemetery | Stillwater, Route 75 at Van Ness Road (HMdb 133867 at 42.93928, -73.69729) | 1927 state marker: built 1764 at Stillwater, moved here, first Congregational church in northern New York; the Town of Stillwater page describes the old cemetery behind it | Whether the meeting house still stands; who owns the cemetery |
| Stillwater village walking tour | Stillwater, NY | The village brochure (villageofstillwaterny.gov 2021 PDF) gives an 1859 octagon house (651 Hudson Ave), a 1790s canal-builders' boarding house (841 Hudson Ave), the Vandenburg house and ferry of about 1732 and the former St. John's Episcopal church of 1874 (the library moved out in 2023) | A second source for each, and what the old church is now |
| Heisler Road trolley bridge | Milton, Heisler Road over the Kayaderosseras | Town of Milton listing: carried the Ballston Terminal trolley; still stands, unsafe, on private land | Whether it can be seen from a public road; position |
| Ballston Terminal stone waiting station | Rock City Falls, Route 29 opposite the George West house | Town of Milton listing: built by George West west of the Empire Mill, visible from Route 29, private | Position; could be folded into `rock-city-falls-west-mills` |
| Daketown School | Greenfield, NY | Saratoga County History Center article (Mary Carlson, April 2026) and town open-house news items: one-room school kept by the town | The town's pages (greenfieldny.gov news items) answer 404 and the archived copies need the web fetch tool; position and opening days |
| Dawson's Mill | Charlton, on the Alplaus Kill below the Crabb Kill | Dave Waite, Saratoga County History Center, 2025: mills from about 1785 to 1941 | Whether anything is left on the ground; position |

## Tips
- The Saratoga County History Center's article index (`brooksidemuseum.org/?p=12228`) links about 60 PDFs by town historians; grep the cached page for `uploads/...pdf` and read the first lines of each with `page.py --all -n 400` to find the ones about places. They gave the Colonial Inn, East Line, Leland House and Rowland's Hollow.
- The Town of Milton historian's listing (cms8.revize.com, "Historic Structures and Places Committee Listings.pdf") describes every old site in the town with an address and says what can still be seen; the same folder has per-hamlet PDFs.
- greenfieldny.gov news pages from 2025–2026 now answer 404; `page.py` names archived copies but cannot fetch them.
- `page.py --all` on a cached PDF prints the text on the second line, not the third: `tail -n +2`, not `sed -n 3p`.
