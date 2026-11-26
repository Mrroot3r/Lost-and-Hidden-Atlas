# hours_pcbn: hours for 38 places in New York, Massachusetts, New Hampshire and Florida
state: several (New York, Massachusetts, New Hampshire, Florida)
region: several
date: 2026-11-21
places: 0
file: hours_pcbn.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. The last nine churches waiting anywhere (all in New York) were looked up first; with no church left waiting, the rest were museums, house museums and theatres from `tools/hours.py list` for New York, Massachusetts, New Hampshire and Florida. Thirty-eight places in all: 12 got days and times from the page of whoever runs them, read in the session; 26 are recorded `?`.

Hours recorded (address on each page checked against the place):
- Springfield Armory: NPS hours page (Wed to Sun 9:30 to 4).
- Naumkeag: The Trustees' page, summer 2026 season (now over for the year).
- Isaac Winslow House: its own site, summer tour hours.
- Old State House, Boston: Revolutionary Spaces visit page (daily 10 to 5).
- Hanover Theatre (Franklin Square Theatre), Worcester: box office hours from its own site.
- Mahaiwe Theater and Stanley Theatre, Utica: "for performances on its calendar" with the box office telephone from their own sites.
- Enfield Shaker Village: museum visit page, 2026 season May to October 31.
- Fort Pickens: NPS Gulf Islands page (gate 8 a.m. to sunset; park store 9 to 4:30).
- Strawbery Banke: its own home page (November tours on select dates; self-guided admission resumes May 1, 2027).
- Sandown Depot: its own site (Saturdays May to October, 10 to 2).
- Wentworth-Coolidge Mansion: NH State Parks page (house closed for the season; grounds dawn to dusk).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| The nine New York churches (Greenbush Reformed, Blooming Grove Reformed, Bloomville Methodist, West Delhi Presbyterian, North Harpersfield, Charlotte Valley Presbyterian at Davenport, St. Peter's Hobart, St. John's Delhi) and West Kortright Centre | two searches each; Albany diocese pages for Hobart and Delhi; umc.org finder (404) | Only directories found. The diocese pages give the street address but no service times. westkc.org gives no hours (events only) |
| Frisbee House, Delhi | dcha-ny.org | 403 twice |
| Jonesville Store, Clifton Park | classiccrust.com | A 2020 Saratoga Business Journal story says the store became Classic Crust, a wood-fired pizza restaurant; its site now reads as catering and gives no hours. The place's note may want updating |
| Baird's Tavern, Warwick | whsny.org/the-properties | Gives hours only for the society's office and 1810 store at 80 Main Street, not the tavern |
| Dr. Best House | drbesthouse.com | No hours on the page |
| Old Third District Courthouse | nps.gov/nebe hours and visitor center pages | Hours page empty (drawn by script) |
| Mission House, Ashley House, Bidwell House, Emerson House (MA) | their own pages | The pages say "garden open daily, year-round", "exhibit open seasonally, sunrise to sunset", "grounds open daily, year-round", "tours late April through October", but no clock times, which `hours.py set` requires. A person could put these words into the places' own `hours=` |
| Job Lane House | joblanefarmmuseum.org | No regular hours |
| Jackson House, Gilman Garrison (Historic New England) | historicnewengland.org | 403, as for earlier sessions |
| Ximenez-Fatio House, Oldest House (St. Augustine Historical Society) | their own sites | 403 |
| Villa Zorayda | villazorayda.com | No hours on the page read |
| NH Farm Museum | nhfarmmuseum.org | Only an event time on the home page |
| Bronson-Mulholland House | palatka-fl.gov facility page | No hours |

Florida state parks' pages (floridastateparks.org) answered 403, so Fort Clinch, Fort Zachary Taylor and Koreshan were left waiting, not recorded.

## Tips for the next session
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
