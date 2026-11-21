# wny_vqqk: Steuben County, NY: Hammondsport wine cellars, Bath, Corning and Hornell
state: New York
region: wny
date: 2026-11-21
places: 20
file: data_wny_vqqk.py

## What this batch is
Twenty places in Steuben County, drawn at random by `choose.py --state ny` (region `wny`, which offered Hammondsport); the Atlas had nothing within 25 km of Hammondsport and nothing in Corning or Hornell. Keuka Lake wine country: the Pleasant Valley Wine Company at Rheims (Bonded Winery No. 1, shut in 2025 per the Governor's July 2026 release; its own visit page is stale), the empty Gold Seal (Urbana Wine Company) cellars on West Lake Road, Germania Wine Cellars, the 1836 Mallory stone mill, Pulteney Square and the Younglove Octagon House (now a B&B). Bath: Magee House (Steuben County Historical Society) and the Soldiers' and Sailors' Home with Bath National Cemetery, and the Cobblestone House. Corning and Painted Post: the 1796 Benjamin Patterson Inn, the DL&W depot museum, Old City Hall (Rockwell Museum), the Little Joe draw tower and Market Street. Hornell and Canisteo: the armory, Temple Beth-El, the Erie Depot Museum and the Canisteo Living Sign. Also the Town Line Church at Cameron Mills and the Church of the Redeemer, Addison. Sources: Wikipedia raw text, HMdb (nearby lists round four towns, marker texts with `page.py --all`), one Register form (14000585, Western New York Wine Co.; the others were placeholders), and the managing bodies' pages for hours (heritagevillagesfl.org/hours, rockwellmuseum.org/visit, cityofhornell.gov, cem.va.gov). Not checked: anything on the ground; every interior; the Magee House hours come from the society's undated blog; owners of Germania, Mallory Mill, Temple Beth-El and the Town Line Church; which house is the Cobblestone House (pin on the street, `area`); which building at 111 Loder Street is the Erie depot (`site`); the Little Joe pin falls on the headquarters, not the tower itself (`site`); whether the 1877 B&H depot in Hammondsport stands. Red brick: Magee House (source) and Hornell Armory (picture) are `yes`; Rockwell left `?` after Wikimedia refused the picture twice.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Western New York Wine Company | Pulteney, NY, 9683 Middle Road | 1880s stone winery and house built for Philip Argus, closed by Prohibition; Register 2014 (form 14000585, read) | Present use and owner, a pin, and whether it can be seen from Middle Road |
| Rockland Silk Mill (Amalgamated Silk) | Hornell, NY (42.3296, -77.6672) | Register 2021 (100007076) | The form text: the NPGallery uuid a search gave was the Lincoln School's form |
| Wood Road Metal Truss Bridge | Campbell, NY | Register 2005 (05000169) | Form is a placeholder; no location or description found |
| M. J. Ward Feed Mill and Erie Freighthouse district | Bath, NY (42.3325, -77.3233) | Register 1991 | Both forms are placeholders; no other source read |
| Presbyterian Church of Atlanta | Atlanta, NY (42.5538, -77.4731) | Register 2010 | Form is a placeholder; no parish page found |
| Kanestio Castle and Oldest House in Steuben County markers | Canisteo, NY (42.2695, -77.6040; 42.2870, -77.6231) | HMdb markers 171111 and 114597 | Marker texts did not come through `page.py`; the house is private |

## Tips
- The Wikipedia point for Temple Beth-El, Hornell (42.157, -77.796) is 19 km off; the geocoder's PointAddress for 12 Church Street is right.
- `pleasantvalleywine.com/visit` still gives visitor-centre hours, but the Governor's release of July 2026 says the winery shut in 2025: check a business's news before taking its own hours page.
- heritagevillagesfl.org: `/hours/` reads in full and holds both the Patterson Inn and the Painted Post depot hours; `/our-village/` is drawn by script.
- The Steuben County Register forms tried were mostly NPGallery placeholders (91000236, 05000169, 10000030, 99000196, 91000235).
- An HMdb marker's text needs `page.py --all`; with `-g` only the "nearby markers" lines come back.
