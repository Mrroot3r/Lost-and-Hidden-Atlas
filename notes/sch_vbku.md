# sch_vbku: Schenectady County: the Stockade's buildings, Union College, Rotterdam and Alplaus
state: New York
region: sch
date: 2026-11-19
places: 14
file: data_sch_vbku.py

## What this batch is
Fourteen places in Schenectady County, a third pass after `sch_gqli` and `sch_ywhu` (region `sch`, drawn at random by `choose.py --state ny`; it offered Esperance, over the line in Schoharie County, so the session stayed in Schenectady County, where the Stockade's own buildings, Alplaus and western Rotterdam had nothing). Stockade: a full entry for the district (replaces the thin pin `lm-stockade-historic-district`), St. George's Episcopal Church (begun 1759; service times from the Episcopal Asset Map, the parish site did not connect), the First Reformed Church (1863 stone walls inside the 1950 rebuilding; service times from its own site), the Brouwer House at 14 North Church Street (`mixed`: its two plaques say before 1700 and ca. 1665, Wikipedia says 1735), the county historical society's museum at 32 Washington Avenue (hours from its page) and the John Glen House of 1740. Union College: the Nott Memorial and Ramée campus (replaces `lm-nott-memorial`; hours from the Mandeville Gallery page). Glenville: the Yates house at Alplaus (National Register form of 2018 read as text) and the Van Eps cement mill site (from `LEADS.md`; added as a marker only, row deleted). Rotterdam: the Arent Bradt house of 1736 (Pearson, 1883, on the Schenectady Digital History Archive, and HMdb photographs of 2018 and 2025), the Vedder burying ground kept at Rotterdam Square mall, the Dellemont–Wemple farm (`mixed`: about 1790 on Wikipedia, about 1760 in a 2017 sale listing) and the Klondike Stairs and Ramp site in the city (`mixed`: remnants seen in 2012 per the Grems-Doolittle blog, nothing recognisable on the aerial or LiDAR). Duanesburg: the Reformed Presbyterian churchyard and 1829 parsonage (the 1837 church burned in 1951, per a newspaper report quoted on HMdb). Sources: Wikipedia through `wiki_raw.py`; HMdb marker pages (the nearby list round the Stockade, Rotterdam, Glenville and Duanesburg), the society, diocese, asset map, church and college pages through `page.py`. Not checked: anything on the ground; red brick everywhere except where a source names stone, iron or frame (nine left `?`); whether the Wemple barn still stands; who owns the Duanesburg cemetery; parking for the Yates and Bradt houses and the Wemple farm (private houses, seen from the road). Pins that mark only an area: the Stockade (Lawrence statue), the Bradt house (marker at the road bend; two houses beside it, the right one not settled), the Van Eps site (the marker). Two pins moved with `pix.py`: the Nott Memorial onto the building and the Duanesburg churchyard onto its headstones.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Vedder Tavern | Glenville, NY, NY 5 a mile from Route 103 (HMdb 130349: 42.88762, -74.05381) | HMdb: built by the Schermerhorn family in 1676 and 1769, long kept as a tavern by Albert Vedder | Whether it still stands, and which building |
| Stevens House | Alplaus, Glenville, NY, Ronald Reagan Way by NY 24 (HMdb 135688: 42.85045, -73.91700) | HMdb: built 1693 by Jonathan Stevens, Indian interpreter at Ael Plaets | Whether a house stands there; a second source |
| St. Mary's Roman Catholic Church Complex | Schenectady, NY, 820–828 Eastern Avenue and 104 Irving Street | National Register form 100001071 (2017) reads as text: stone church and buildings of the early 1900s for the Polish parish | The form was not read past its first page; whether the church still holds services, and its page |
| Robert Sanders House | Schenectady, NY, 43 Washington Avenue (HMdb 77588) | 1932 marker: 1750, Washington visited 1775, later the Schenectady Female Academy; the marker was missing in April 2026 | A source on the house as it stands |
| Schenectady Public Market and Scale House | Schenectady, NY | On the National Register (100007377) | NPGallery returns a picture, not the form; any source |

## Tips
- The parish site `stgeorgesschenectady.org` resets the connection to `page.py`; the Episcopal Asset Map page for a parish (`episcopalassetmap.org/node/<n>`) gives its service times and reads in full.
- HMdb nearby lists answered most requests at once but several marker pages came back empty when read quickly in a loop; a four-second pause between pages fixed it.
- `wiki_raw.py` knows "Brouwer House", "St. George's Episcopal Church (Schenectady)" and "Yates House (Schenectady, New York)" only as red links: the Brouwer house is described in the "Schenectady County Historical Society" article, and the Yates House of the 2018 Register listing is in Alplaus (Glenville), not the Stockade's Yates house on Union Street.
- A web search for the Duanesburg Reformed Presbyterian church finds only its 1935 marker; the HMdb page's commentary says the church burned in 1951, so it is a churchyard, not a standing church.
