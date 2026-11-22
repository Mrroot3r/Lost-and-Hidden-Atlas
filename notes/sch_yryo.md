# sch_yryo: Schenectady County: Princetown, Niskayuna, Scotia and the city's schools
state: New York
region: sch
date: 2026-11-22
places: 11
file: data_sch_yryo.py

## What this batch is
Eleven places in region `sch`, drawn at random by `choose.py --state ny`. Princetown had nothing on the Atlas; it gets the 1895 stone railroad arch at Kelly's Station (from the town historian's 1998 history on the Schenectady Digital History Archive, with OpenStreetMap's tunnel and abandoned-railway lines; one local source). Niskayuna: Rosendale Common School (now the Grange hall; from LEADS.md) and the George Westinghouse Jones House. Glenville: the Beukendaal 1748 battle markers (marker only). Scotia: the 1939–40 post office with Amy Jones's 1941 mural. Schenectady city: the 1912 post office, the Franklin, Horace Mann and St. Columba's schools, the Foster Building (Hotel Foster, restored by 2018) and St. Mary's three-towered Polish church (1903; from the sch_vbku note's leads; its 2017 Register form read as text). Wikipedia was read with `wiki_raw.py`; HMdb, the county library's archive, the Governor's press office, Downtown Schenectady and the Register form with `page.py`; pins came from OpenStreetMap buildings (`nom.py`, `osmnear.py`) and were all looked at on the aerial and LiDAR. Not checked: any interior, post office hours (hours='?'), whether St. Mary's church (OpenStreetMap: "Renaissance Hall" events venue) can be visited, which building on Craig Street is the Horace Mann School (pin `area`), and Kelly's Station tunnel's present state beyond the aerial. Commons had no picture for any of the eight places without an article picture.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Seeley Farmhouse ("Little Richard's Tavern") | Glenville, NY, Freemans Bridge Road (Wikipedia 42.83167, -73.93056; HMdb 125398) | Wikipedia: L-shaped Greek Revival farmhouse of about 1850, NRHP 1978; 2016 town marker: John F. Seeley, broom-corn grower | The Register point lands on the Water's Edge Lighthouse restaurant (2 Freemans Bridge Road); whether the farmhouse is that building, or still stands |
| Vedder Tavern | Glenville, NY, NY 5 (HMdb 130349: 42.88762, -74.05381) | Grems-Doolittle Library blog (2015): the Swart and Vedder taverns stood "into the 20th century"; photo of the Vedder Tavern in Glenville | Whether it stands today, and which building |
| Cheeseman's Tavern (Gifford house) | Giffords, Princetown, NY, on US 20 | Princetown town historian (1998, schenectadyhistory.org): brick tavern of about 1784, bricks made on the spot, third-floor ballroom; HABS photos | Whether it stands, and a position; loc.gov answered 403 |
| Maalwyck (Toll house) | Glenville, NY (HMdb 95599: 42.83011, -73.97624) | 1930s state marker: house built about 1712 by Karel Hansen Toll | Whether the house stands |
| Stanford Home (Stanford mansion) | Niskayuna, NY | Schenectady Digital History Archive lists it under Niskayuna's historic buildings; savethepinebush.org has a series on it | Every page tried was drawn by script; any readable source and its present state |
| HABS houses of 1930s photos: Schermerhorn House and Van Slyck House (Rotterdam, NY 5S), Tymeson House and Veeder Farmhouse (2201 Rosendale Road, Niskayuna), Glenville Centre Reformed Church (Bolt Road), Van Epps Hotel (Glenville) | Schenectady County | Listed on schenectadyhistory.org's buildings pages for each town, with HABS photographs | Whether each stands; loc.gov refuses `page.py` (403) |

## Tips
- schenectadyhistory.org (`/buildings/<town>/index.html`, `/<town>/history.html`) reads with `page.py --all` and lists each town's HABS-photographed buildings: a quick list of candidates for Schenectady County's towns.
- loc.gov item pages (HABS) answer 403 to `page.py`, and the archived copies cannot be fetched either.
- savethepinebush.org pages come back "drawn by script".
- `photo_find.py look` output: a place with nothing on Commons prints one long "Nothing on Commons" line; do not filter long lines out or it looks as if the tool printed nothing.
