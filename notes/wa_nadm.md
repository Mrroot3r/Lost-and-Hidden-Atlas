# wa_nadm: Jefferson County, Washington
state: Washington
region: wa
date: 2026-11-19
places: 15
file: data_wa_nadm.py

## What this batch is
Fifteen places in Jefferson County, Washington, drawn at random as region `wa` by `choose.py`: the three Army posts of the Port Townsend area (Fort Townsend of 1856, and the Endicott-era Fort Worden and Fort Flagler), Point Wilson Light, Port Townsend's courthouse, 1891 city hall (now the Museum of Art and History), customs house and post office, Carnegie library, St. Paul's Episcopal church (1865), the stone Leader (Fowler) Building of 1874, the Rothschild House with its own contents, the Starrett House, Manresa (Eisenbeis) Castle, the ruins of the Irondale iron and steel works, and the 1931 Enchanted Valley Chalet in Olympic National Park. Sources were read with `wiki_raw.py`, National Register forms from NPGallery through `page.py` (all had a text layer), Washington State Parks' park pages and park-history pages, the Jefferson County Historical Society's pages, the Department of Ecology's Irondale cleanup page, the NPS East Fork Quinault trail page, the Peninsula Daily News, the Port Townsend Leader and PCAD. Not checked: anything on the ground; hours for the courthouse, customs house lobby, Carnegie library, St. Paul's and Irondale Beach Park; Point Wilson's summer tour days; whether the Starrett House or Manresa Castle now takes guests; whether the 1911 Irondale jail still stands; where the Irondale foundations and kilns are inside the park (the pin is the park lot); where the Navy's brick Torpedo X-Ray Tower at Fort Townsend is. Pins that mark a lot or general area, not the thing: Fort Townsend (a mapped parking point by a clearing, prec area) and Irondale (park lot). Manresa Castle and the Leader Building are prec site because the aerial did not settle which building it is. Brick: St. Paul's set from a Commons photograph (white clapboard); the courthouse from its form (red brick); the rest from forms or left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Irondale Jail | Irondale, WA (foot of Moore Street) | 1911 plank jail with two cells and a "solitary"; sinking and decaying in 1983 (Register form 83003327) | Whether it still stands, and on whose land |
| Old Alcohol Plant (Inn at Port Hadlock) | 310 Hadlock Bay Road, Port Hadlock, WA | Former alcohol plant later a 47-room hotel, closed 2011, partly reopened as the Bayside Hotel housing programme (Peninsula Daily News) | A source for the plant's history and dates, and current use |
| Methodist Episcopal Church of Port Hadlock | Randolph and Curtiss streets, Hadlock, WA (48.03417, -122.76917) | 1905 church, a private house by 1983 (form 83003329) | Probably just a house now; left out |
| Christian Congregational Church of Port Ludlow | Port Ludlow, WA (47.9368, -122.7006) | Listed 2020 (100006061) | The NPGallery text route gave under 900 characters; no source read |
| Torpedo X-Ray Tower | Former Fort Townsend land, WA | 65-foot brick Navy explosives laboratory of the Second World War (State Parks history page) | Its location, owner and whether it can be seen |
| Interrorem Guard Station | Duckabush vicinity, WA (47.6786, -122.9927) | Olympic National Forest cabin on the Register (13000506) | `wiki_raw.py` found no article under that title; a Forest Service page |

## Tips
- Washington State Parks pages read well with `page.py`: each park page holds hours, Discover Pass fees and links to a "park history" page (`/about/news-center/field-guide-blog/<park>-history`) with a long, sourced history; museum sub-pages give the museum's hours by season.
- jchsmuseum.org is a Wix site: `page.py --all` reads its pages, but its old `/Sites/...` addresses answer 404; the live ones are `/museum` and `/visit/historic-houses/`.
- pointwilsonlighthouse.org is drawn by script; `page.py` gets only one line ("weekend tours are suspended for the winter").
- For Port Townsend, Register list coordinates and Wikipedia points were close except the courthouse (105 m off, on a house); ArcGIS PointAddress answers landed on buildings, but its street-address answer for 526 Moore Street in Irondale fell on the road among houses.
- Many web searches returned links only, with no quoted text, so facts had to come from opening the pages.
