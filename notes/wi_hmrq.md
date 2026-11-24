# wi_hmrq: Wisconsin: mills, barns, a logging camp and a lighthouse in counties not yet covered
state: Wisconsin
region: wi
date: 2026-11-24
places: 11
file: data_wi_hmrq.py

## What this batch is
Eleven places in Manitowoc, Portage, Eau Claire, Ashland, Oconto, Wood, Green Lake and Waukesha counties, none near the earlier Wisconsin batches: Rock Mill (Maribel), Lutze Housebarn (Newton), Rawley Point Light, Rising Star Mill (Nelsonville), Dells Mill (Augusta), the Basswood Island brownstone quarry, Holt and Balcom Logging Camp, the Marshfield fair round barn, Wakeley's Tavern (Nekoosa), Thrasher Opera House (Green Lake) and Delafield Fish Hatchery. Facts come from the Register county lists (`wiki_raw.py --rows`), the nomination forms on NPGallery (`page.py`), and the pages of the DNR, the Park Service, the Oconto County Historical Society, dellsmill.com, historicpointbasse.com and Wikipedia. Not checked: any interior; hours beyond what those pages say (Rock Mill, Lutze, Rising Star and Delafield have none on record; the Thrasher and Holt-Balcom lines come from the owners' pages and a search result); whether the Lutze housebarn can be seen from a road. Rock Mill's pin is the roadside marker, with the mill hidden by trees on the aerial, so it is marked as an area pin. Two pictures were chosen from Commons (Rock Mill and Holt-Balcom).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Sheboygan Valley Land and Lime Company kilns (Quasius Quarry) | Rhine, WI (43.8551, -88.0276) | Four limestone kilns of 1911, listed 2016, private (form 2015) | The Register point falls on a road bridge; the kilns could not be seen on the aerial and no public viewing point is known |
| Gooseville Mill | Adell, WI (43.5878, -88.0206) | 1879 board-and-batten mill with its belts, listed 1984, private | The Register point is a yard by a road, and no building matched; nom.py found nothing |
| Daniel E. Krause Stone Barn | Chase, WI (44.7183, -88.1786) | 1903 cobblestone barn, listed 2000, private farm | The Register point is a park-like gravel lot with no barn on the aerial |
| Pureair Sanatorium | Bayfield, WI (46.7908, -90.8472) | 1918 to 1923 brick and brownstone TB sanatorium, listed 1981 | An Asylum Projects entry says demolished, with no date; nothing current opened |
| Loreto Shrine Chapel and St. Nazianz buildings | St. Nazianz, WI (43.9994, -87.9289) | 1870 chapel, a communal society's village | The NPGallery form is a placeholder and no other source was read |
| Kiel Mill, Hillsboro Condensed Milk Company | Kiel and Hillsboro, WI | Listed 2019 and 2020 | The NPGallery forms returned no text |

## Tips
- NPGallery `_text` forms read well for Wisconsin listings from 1974 on, but some (St. Nazianz chapel, Kiel Mill, Hillsboro) return a placeholder.
- Most Wisconsin mill and barn Register points are on private farms: the pin check could not match the Register point to a building for four of the sixteen first picks, so those were left as leads.
- `nom.py` found OpenStreetMap points for the museums but nothing for the private mills; the roadside marker point it gave for Rock Mill was the best anchor.
- The Wisconsin Historical Society's property pages (`wisconsinhistory.org/Records/Property/HI...`) read well with `page.py`.
