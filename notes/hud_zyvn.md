# hud_zyvn: Kingston and Hurley: the Stockade, the Rondout and Old Hurley
state: New York
region: hud
date: 2026-11-21
places: 21
file: data_hud_zyvn.py

## What this batch is
Twenty-one places in Kingston and the hamlet of Hurley, Ulster County (region `hud`, drawn at random by `choose.py --state ny`, which offered Livingston, Philmont and Hurley; start.py showed nothing on the Atlas in the Stockade or in Old Hurley). Nearly all standing. Uptown Kingston: the Stockade District (area pin), the Senate House, the Old Dutch Church, the 1818 courthouse, the Persen House at the Four Corners (closed for the 2026 season), the Fred J. Johnston House, the Frog Alley ruins (the one ruin; it was an unnamed OpenStreetMap lead), the Van Steenburgh house. Midtown and the Rondout: City Hall, the Rondout–West Strand district, Rondout Light (boat only; the Maritime Museum is its th= point), the 1921 suspension bridge, the Trolley Museum, the 1870 poured-concrete Ponckhockie chapel, the Fitch bluestone office in Wilbur, the City Almshouse (now Landmark Place apartments). Hurley: the historic district, the Reformed church, the Van Deusen house, the DuMond "Spy" house and the Heritage Society museum. Sources read in the session with `wiki_raw.py` and `page.py`: Wikipedia, the parks.ny.gov Senate House page, the Ulster County Clerk's Persen House page, olddutchchurch.org, tmny.org, hrmm.org, kingston-ny.gov, fohk.org and its 2016 Stockade walking-tour PDF, hurleyheritagesociety.org (museum page, Main Street history, walking-tour PDF), two NPGallery Register forms, the Governor's 2022 release on Landmark Place and a 2022 Hudson Valley One article. Not checked: nothing on the ground; the courthouse's present use and whether it can be entered; whether Frog Alley's walls are still as the 2016 brochure describes and whether the little park is open; the Fitch office's owner and use; service times for the Hurley and Ponckhockie churches (no page of their own found); the Hurley church's date (1853 or 1854 in the society's two texts) and the Van Deusen house's (c. 1744 in the brochure, 1723 on the state marker seen in a photograph), both conf='mixed'. Pins are geocoder PointAddress or OpenStreetMap points, each looked at on the aerial; Senate House, Van Deusen and Ponckhockie are prec='site' because the point is beside the building, and the Stockade and Rondout pins are area pins. Pictures: 14 of 21 places have one (Wikipedia or a chosen Commons photo in `pics_rrch.py`); none fitted the Persen House, Frog Alley or the DuMond house.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sleight-Tappen House (DAR Wiltwyck Chapter House) | Kingston, NY (Green and Crown streets) | Late 1600s, restored by Myron Teller after the DAR bought it in 1905; "open to the public for special events" (Friends of Historic Kingston brochure, 2016) | The chapter's own page for open days; a pin |
| Ulster Performing Arts Center (Community Theatre, 1926) | Kingston, NY (Broadway) | Brick Classical Revival movie palace run by the Bardavon (Wikipedia) | Box office or tour hours from the Bardavon's page |
| Hudson River Maritime Museum and the tug Mathilda (1898) | Kingston, NY, 50 Rondout Landing (41.91877, -73.9812) | Old boat shop, tug in the yard (Wikipedia); its home page shows Friday to Sunday times without a season | Its own hours page (visit.html is 404) |
| M. E. Church (mapped ruin) | Eddyville, NY (41.89404, -74.02147) | OpenStreetMap ruin lead near the D&H Canal's tidewater end | Any source; not looked at |
| Kingston City Almshouse outbuildings | Kingston, NY, 300 Flatbush Avenue | Laundry, barn, stone cottage, brick office behind the almshouse (Register form) | Whether they survived the Landmark Place building work |

## Tips
- The Friends of Historic Kingston Stockade walking-tour PDF (`fohk.org/wp-content/uploads/2016/07/StockadeIWT2016wMAP-3.pdf`) reads in full with `page.py --all` and gives date, builder and address for 50 Stockade buildings; the Hurley Heritage Society's walking-tour PDF does the same for 27 Hurley houses. The NPS Kingston itinerary (`nps.gov/NR/travel/kingston/...`) is 404.
- Kingston has both a Wall Street and a South Wall Street: `geo.py` returns both for a house number; take the PointAddress in the Stockade.
- The unnamed OpenStreetMap ruin lead at 41.93577, -74.02306 in Kingston is the Frog Alley ruins.
- `publish.sh` stopped twice in a row because research batches merged minutes apart; each time `resync.sh`, a fresh batch time and a rebuild, then a new branch name, worked.
