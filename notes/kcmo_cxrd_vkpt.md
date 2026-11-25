# kcmo_cxrd_vkpt: Kansas City: older commercial and industrial buildings
state: Missouri
region: kcmo
date: 2026-11-25
places: 13
file: data_kcmo_cxrd_vkpt.py

## What this batch is
Thirteen older office, warehouse and factory buildings in downtown Kansas City, the Crossroads and Hyde Park (the Gumbel, Baker-Vawter, Dierks, Insurance, Firestone, 2020 Grand, Land Bank, R. A. Long, Stine & McClure, Corrigan and Belger Cartage buildings, the Jensen-Salsbery Laboratories and Janssen Place), none of which the Atlas had. The ground first drawn was Lee's Summit and the country south of it (claimed as Missouri); the briefing showed that earlier batches (kcmo_jcse, kcmo_lsb_hvtn, kcmo_lex2_pdrb, kcmo_ind2_qfhm) had already taken every listing there that is worth a visit, and the rest are districts of ordinary houses, so the session moved to the downtown Register listings that no batch had added. The Register lists for Kansas City were compared with the place lists by name to find the gaps.
Sources: the Clio walking-tour pages (Crossroads, Financial District, downtown) and Clio entries, each of which cites the Register form it was written from; the Jackson County Historical Society's Janssen Place article; Wikipedia as raw text. The Register forms themselves were not read (the state's PDFs answer 404 and NPGallery gives placeholders for the older ones). Coordinates are the Register list's, except the Land Bank Building and Belger Cartage (OpenStreetMap); every pin was looked at on the aerial and is on a building of the right size. Not checked: hours, who owns each building today, interiors, whether any is open to visitors, and brick (all `?`; no source or picture opened said what the walls are). The Belger Arts Center's "by appointment" comes from Clio, not from its own page. Pictures: eleven found on Commons, two with none (Baker-Vawter, Belger).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kirk Building (Kansas City Slide Company, where Walt Disney worked) | Crossroads, Kansas City, MO | Clio: built 1908, the slide company was there 1913 to 1920, expanded 1925, renovated 1983, a charter school since 2012 | The street address and a pin |
| James Fitzpatrick Saloon Building (The Majestic) | Garment District, Kansas City, MO | Clio: built 1911, a Pendergast-era jazz venue | The address and a pin |
| Phoenix Hotel building (1888) | 8th Street, Kansas City, MO | Clio: three-storey Neo-Romanesque with a cast-iron arch, a jazz club since 1990 | The address and a pin |
| Roasters Block (Swofford Building, 1899), site of the Lathrop School destroyed by the 1886 tornado | Quality Hill, Kansas City, MO | Clio | The address and a pin |
| Jackson County Democratic Club building (Pendergast headquarters, 1926) | Crossroads, Kansas City, MO | Clio | The address and a pin |
| Donnelly Garment Company building (Walnut Street) | Crossroads, Kansas City, MO | Clio | The address and a pin |
| Other downtown Register listings: Warehouses and offices (Murdock Manufacturing, Stenzel, Studna Garage, Townley Metal & Hardware, Vitagraph Film Exchange, Kelley-Reppert Motor, Safeway warehouse, Interstate Securities, Kellogg-Mackay) | Downtown and Crossroads, Kansas City, MO | On the Register list with coordinates; Wikipedia has no article for them | A readable source for each (Clio has none that turned up) |
| Bailey Family Farm, Sherwood Manufacturing Building | Lee's Summit, MO | On the Register list | Still no readable source; the Register forms were not reachable |

## Tips
- Clio's tour pages are a good source for downtown Kansas City buildings: `page.py --all -n 60000 https://theclio.com/tour/<id>` prints every stop's text (without `-n` it stops at 12,000 characters). Tours used: 2305 (Crossroads), 2310 (Financial, Library and Garment districts), 251 (downtown), 573 (Power and Light). Clio's tour pages carry no links to the entries and no addresses.
- The Lee's Summit, Raytown, Grandview and Independence ground is worked out; three earlier notes said so, and it was true again. The downtown Register lists (`wiki_raw.py --rows "...: Downtown Kansas City"` and `"...: Kansas City other"`) still hold many names the Atlas lacks; comparing names against `tools/data_*.py` finds them in one pass.
- `choose.py --claim ... --state mo` reports a region with only 17 places, but the Kansas City ground itself is `kcmo` and is where the gaps are.
