# conf_pbhx: Watervliet and the old houses of Loudonville and Colonie
state: New York
region: albco, conf
date: 2026-11-22
places: 12
file: data_conf_pbhx.py

## What this batch is
Twelve places drawn at random in region `conf` (`choose.py --state ny`). Cohoes, Waterford, Green Island and Watervliet's canal and bell sites were already well worked, so this batch takes what was left: three in Watervliet (the St. Patrick's Church site, demolished 2013 for a supermarket; Edwin Emery's Canalside Store; the James Roy Mills marker) and nine Register-listed houses of the old Town of Watervliet, now Colonie and Loudonville, filed under `albco` like the Pruyn House: the Ebenezer Hills Jr. Farmhouse (about 1785), the Jedediah Strong House (about 1795), the Frederick Cramer House, the Bacon-Stickney House, the George H. Lawton House, the Royal K. Fuller House, the Gorham House, the Whitney Mansion and the Turner Farmhouse at 475 Loudon Road. Sources: Wikipedia read as raw text (`wiki_raw.py`; the infoboxes gave each house's address), HMdb markers, two Times Union articles and the governor's September 2022 Register nominations release, all through `page.py`. Pins: addresses placed with the ArcGIS geocoder and OpenStreetMap building outlines, each checked on the leaf-off aerial; St. Patrick's and the Whitney Mansion were moved with `pix.py`. Not checked: anything on the ground, interiors, whether the Hills and Strong barns survive, which part of 600 3rd Avenue is the old canal store (one source only, `conf='mixed'`), and whether any James Roy mill building stands. All the houses are private and view-only. Red brick settled only for the Cramer House (its Wikipedia photograph); the rest are `?`. Commons had no picture for any of the eight places without one.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mark House | Colonie, NY (Register 100008066) | Governor's June 2022 nominations release: 1791 farmhouse of Isaac Mark, a Van Rensselaer tenant, rebuilt in the 1840s in the Dutch tradition; in the family until 1881 | Its address: the release gives none and spotlightnews.com answered 429 |
| St. Brigid's Church (update to the existing row) | Watervliet, NY (HMdb 253752 says the NW corner of 4th Avenue and 7th Street; the older row says 695 Fifth Avenue) | HMdb: dedicated July 11, 1851; its 1883 Troy Meneely bell is now on show at the Broadway gateway near Schuyler Lane | Whether the church stands; troyirish.org answers 403 to `page.py`, and the aerial does not settle it |
| Corporation Hall (update to the existing rows) | Green Island, NY (George and Clinton Streets) | HMdb 256010 again; OpenStreetMap maps no building of that name, only the Town Hall at 69–73 Hudson Avenue, 125 m away | Which building it is |
| Springwood Manor, Wheeler Home, Treemont Manor, Alfred H. Renshaw House, Isaac M. Haswell House | Loudonville and Colonie, NY (498 and 485 Loudon Road, Treemont 42.714, -73.764, 33 Fiddlers Lane, 67 Haswell Road) | Wikipedia: Register houses of the 1979 Loudonville and 1985 Colonie listings | Left out as less worth a visit than those added; each needs only a pin check |

## Tips
- NPGallery's text route gave the one-page placeholder for every 1979 Loudonville and 1985 Colonie form tried (8 of them); the 2022 Turner Farmhouse number returned a PNG. The Wikipedia infobox `location=` line in `research/wikiraw/` gives the street address for most of these houses.
- `wiki_raw.py` prints "a -story house" where the article has `{{frac|2|1|2}}`: grep the cached raw text for `frac` before writing a storey count.
- troyirish.org and spotlightnews.com would not open through `page.py` (403 and 429).
