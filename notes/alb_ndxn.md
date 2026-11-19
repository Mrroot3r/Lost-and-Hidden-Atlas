# alb_ndxn: Albany: oldest houses, derelict churches and downtown landmarks
state: New York
region: alb
date: 2026-11-19
places: 15
file: data_alb_ndxn.py

## What this batch is
Fifteen places in the City of Albany (region `alb`, drawn at random by `choose.py --state ny`). The Atlas's 44 Albany places were nearly all vanished sites from the first catalogue, so this batch takes what still stands. Derelict or closed: St. Joseph's Church on Ten Broeck Street (city-owned, for sale), St. John's Church on Green Street (stone-clad steel frame, roof open), the Church of the Holy Innocents (onion dome, partial rear collapse 2015), Public Bath House No. 2 (1905, closed 2010; the federal names file wrongly calls it vanished), the James Hall Office in Lincoln Park (Downing and Vaux, 1852, empty since 2011), and the old Erie Canal Lock One, dug out again in August 2026. Standing and open: the Van Ostrande–Radliff House (48 Hudson Avenue, 1728, Historic Albany Foundation First Fridays), the Quackenbush House and the Quackenbush Pumping Station (brewpub), the Cathedral of the Immaculate Conception, the Cathedral of All Saints, St. Peter's (Tiffany rose window), St. Mary's (1869, painted ceilings), the Albany Institute of History & Art and the Palace Theatre. Sources: Wikipedia through `wiki_raw.py`; through `page.py` Historic Albany Foundation's "Places in Peril 2024" page (the cached HTML had to be cleaned by hand to read each building's block: owner, date, condition), its 2026 First Friday event page, WAMC and Spectrum News (Lock One, Bath House), the Evangelist, HMdb, the cathedrals', St. Peter's (archived copy, Aug. 7, 2026) and the Albany Institute's pages, the heritage-area page for All Saints and the Albany Heritage Area walking-tour brochure (PDF). Red brick was settled from Wikipedia photographs with `brick.py look` for the Quackenbush House, the pump station and St. Mary's (yes), the James Hall Office (painted, no) and the Albany Institute (buff, no); 48 Hudson, Holy Innocents, All Saints and Lock One are `?`. Not checked: anything on the ground; whether the Lock One dig was left open or filled; who owns the Lock One ground; restaurant and theatre hours; the Palace's event schedule; who owns the Quackenbush House and pump station buildings. Every pin was looked at on the aerial and the LiDAR; all sit on their buildings except Lock One (`site`, a wooded strip by I-787 where LiDAR shows a straight ridge). No pin marks only a parking lot.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| New York State Executive Mansion | Albany, NY (42.64667, -73.76139) | Wikipedia: 1856–60 house, governors' home since 1875; free tours "suspended" | Whether tours have resumed (a state page) |
| Hook and Ladder No. 4 | Albany, NY (42.64167, -73.78028), Delaware Avenue | Wikipedia: Marcus T. Reynolds' 1912 Dutch Revival firehouse, still in use | Brick colour and whether it is worth a pin on its own |
| Nut Grove | Albany, NY (42.6335, -73.7685) | Register list: A. J. Davis's only Greek Revival house in the Hudson Valley | Article not read; owner and whether it can be seen from the street |
| Washington Avenue Armory | Albany, NY (42.65708, -73.76233) | Wikipedia: Isaac Perry's 1890 armory, now a sports and event arena | Current events page and access |
| Holland Avenue Tudors (100–112 Holland Avenue) | Albany, NY | Historic Albany Foundation, Places in Peril 2024: 1933–37 houses by Jesse Leonard, vacant about 15 years | Whether they still stand (the foundation shows a December 2025 photo); a coordinate |

## Tips
- Historic Albany Foundation's "Places in Peril" page (historic-albany.org/places-in-peril-2024) gives, per building, the address, date, architect, owner, last occupancy and condition: the best single source for derelict buildings in Albany. `page.py -g` returns only fragments of it because the text is broken by gallery markup; strip the tags from the cached file in `research/pages/` and search for "Owner:".
- The leads layer's "Public Bath Number 2" (federal names file, "vanished") is a standing building; other "vanished" Albany entries may be standing too.
- `places_test.js` still fails only on `onesquethaw-valley` ("18th century"), as earlier notes said; this batch changes nothing it reads.
- A 2009 Wikipedia photo of 48 Hudson Avenue shows the building mid-restoration with later additions round it; it does not settle the brick of the 1728 house.
