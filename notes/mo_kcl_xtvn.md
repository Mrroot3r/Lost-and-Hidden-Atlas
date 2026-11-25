# mo_kcl_xtvn: Kansas City area: leftovers
state: Kansas, Missouri
region: kcmo, ks
date: 2026-11-25
places: 3
file: data_mo_kcl_xtvn.py

## What this batch is
Three places: the Liquid Carbonic Company Building and the Kansas City Club Building in downtown Kansas City, Missouri, and the Leavenworth federal penitentiary. The ground was the Kansas City area on both sides of the line (an attempt at Cass, Lexington, Johnson, Douglas, Leavenworth, Wyandotte and Miami counties first). Every National Register list and Kansas State Register list for those counties was compared with the place lists by name and almost nothing was missing, so this batch is small on purpose. Sources were Wikipedia (read with wiki_raw.py), the Clio Crossroads walking tour page, and the Kansas Historical Society register search. Not checked: interiors, hours, present use of the Liquid Carbonic building beyond the walking-tour page, whether the penitentiary cemetery is open to anyone. The Liquid Carbonic pin falls in the street at 20th and Baltimore on the aerial and is marked as an area pin. No pictures were needed: all three have Wikipedia pictures.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Judge D.B. Wilson Homestead (stone ruin, two stories built into a hillside) | Paola, KS, under two miles north of Osawatomie | Kansas State Register 2023; nomination form read; private farmland with the owners living beside it | A coordinate, and the owner's word that visitors are welcome |
| Gorrill Farmstead (1880s limestone house by Mark Migliario) and O'Sullivan Farmstead (1866) | Lawrence and Overbrook, Douglas County, KS | Register forms list them; both private working farms with addresses not for publication | Coordinates and any public way to see them |
| Mugan-Olmsted House (stone, about 1866), Fox House, McCurdy House | Lawrence, KS | Register listings (2017, 2023, 2001); KSHS summary only | A readable nomination and a public view |
| Smallwood V. Noland House | Independence, MO (39.0817, -94.4369 per the Register list) | Register 1994, Greek Revival | A source that says what stands |
| Kessler Apartments, Kansas City Water Department Building, Police Station Number 4 | Kansas City, MO | Named in Wikipedia's building list for the city; Wikipedia articles are one or two sentences | A fuller source (nomination forms, city pages) for each |
| Jake's Branch of Middle Creek Bridge | Louisburg, KS (38.5197, -94.7158 per the Register list) | Masonry arch bridge, Register 1985 | Its form is a scan with no text |

## Tips
- Compare candidate names against the place lists by the place's id as well as its name: a check on the name text said "missing" for the AXA Building in Leavenworth, which was already on the map (data_ks_lvft_rxne.py). build_sites.py caught it as a duplicate id.
- The Register lists for Cass, Johnson, Leavenworth, Miami, Douglas, Wyandotte, Clay, Platte, Jackson and Lafayette counties are about used up. Further work near Kansas City needs other lists (the Kansas City local register, Wikipedia building categories for the city) and sources beyond one-sentence articles.
- A scheduled run with no live person has no way to approve web fetches; WebSearch worked and returned useful summaries.
