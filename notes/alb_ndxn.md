# alb_ndxn: Albany: oldest houses, derelict churches and downtown landmarks
state: New York
region: alb
date: 2026-11-19
places: 15
file: data_alb_ndxn.py
tidied: 2026-11-26

## What this batch is
Fifteen places in the City of Albany (region `alb`, drawn at random by `choose.py --state ny`). The Atlas's 44 Albany places were nearly all vanished sites from the first catalogue, so this batch takes what still stands. Derelict or closed: St. Joseph's Church on Ten Broeck Street (city-owned, for sale), St. John's Church on Green Street (stone-clad steel frame, roof open), the Church of the Holy Innocents (onion dome, partial rear collapse 2015), Public Bath House No. 2 (1905, closed 2010; the federal names file wrongly calls it vanished), the James Hall Office in Lincoln Park (Downing and Vaux, 1852, empty since 2011), and the old Erie Canal Lock One, dug out again in August 2026. Standing and open: the Van Ostrande–Radliff House (48 Hudson Avenue, 1728, Historic Albany Foundation First Fridays), the Quackenbush House and the Quackenbush Pumping Station (brewpub), the Cathedral of the Immaculate Conception, the Cathedral of All Saints, St. Peter's (Tiffany rose window), St. Mary's (1869, painted ceilings), the Albany Institute of History & Art and the Palace Theatre. Sources: Wikipedia through `wiki_raw.py`; through `page.py` Historic Albany Foundation's "Places in Peril 2024" page (the cached HTML had to be cleaned by hand to read each building's block: owner, date, condition), its 2026 First Friday event page, WAMC and Spectrum News (Lock One, Bath House), the Evangelist, HMdb, the cathedrals', St. Peter's (archived copy, Aug. 7, 2026) and the Albany Institute's pages, the heritage-area page for All Saints and the Albany Heritage Area walking-tour brochure (PDF). Red brick was settled from Wikipedia photographs with `brick.py look` for the Quackenbush House, the pump station and St. Mary's (yes), the James Hall Office (painted, no) and the Albany Institute (buff, no); 48 Hudson, Holy Innocents, All Saints and Lock One are `?`. Not checked: anything on the ground; whether the Lock One dig was left open or filled; who owns the Lock One ground; restaurant and theatre hours; the Palace's event schedule; who owns the Quackenbush House and pump station buildings. Every pin was looked at on the aerial and the LiDAR; all sit on their buildings except Lock One (`site`, a wooded strip by I-787 where LiDAR shows a straight ridge). No pin marks only a parking lot.

## Leads
Moved to `LEADS.md` on 2026-11-26 by the tidy job (5 rows). New leads for this ground go in the note of the batch that finds them.

| Place | Where | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
