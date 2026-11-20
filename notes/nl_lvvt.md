# nl_lvvt: The Bonavista Peninsula: Trinity, Port Union, Elliston and Bonavista, Newfoundland
state: Newfoundland and Labrador
region: nl
date: 2026-11-20
places: 22
file: data_nl_lvvt.py

## What this batch is
Twenty-two places on the Bonavista Peninsula, the third batch in the province and the first here (nothing within 40 km before). Trinity: the Lester-Garland Premises and the rebuilt brick Lester-Garland House (one entry), the Green Family Forge, Hiscock House, the 1903 Court House, Gaol and General Building (now the Trinity Chocolate Company's kitchen), St. Paul's Anglican (unpainted interior), the Church of the Most Holy Trinity (1833), the Mortuary Chapel, the Fort Point battery (four cannon of the 1746 fort), and the Trinity Train Loop with the derelict Trinity Loop Fun Park. Also All Saints in English Harbour (now an arts centre; Trinity Bay Disaster graves), Port Union (the Factory and the union-built town as one entry) and its 1917 hydro station, St. Peter's in Catalina, in Elliston the Upstairs-Downstairs root cellars, the Tom Porter root cellar, St. Mary's Anglican and the Elliston Ridge radar station ruins, and in Bonavista the Ryan Premises, Mockbeggar Plantation, Cape Bonavista Lighthouse, St. Joseph's RC and the Alexander Chapel. Sources: the Canadian Register statement for each designated place (historicplaces.ca, `page.py --all -n 60000`; the Register id is the `idp` field, or `idf`/`idm` when `idp` is empty, of the `{{HPC row}}` templates in "List of historic places in the Bonavista Bay region"); seethesites.ca; Parks Canada's Ryan Premises pages; trinityhistoricalsociety.com; the English Harbour Arts Association; Museums NL; the Town of Elliston and Hidden Newfoundland for the radar site; The Canadian Press (2019) for the Trinity Loop; Wikipedia through `wiki_raw.py`. **Not checked:** anything on the ground; service times for all six churches (no parish pages found; `hours='?'`); the Factory's and the Fort Point interpretation centre's hours; whether the Court House has a shop open to visitors; the year of the Trinity Historical Society's posted season (June 2 to October 12, no year); the Trinity Loop's state since 2019 and whether the province cleaned it up; who owns the Elliston Ridge site and Fort Point; the hydro station's owner. Pins marking only an area: the Mortuary Chapel (Register point in trees), Fort Point (moved onto a building near the tip, which may not be the keeper's house), both Elliston root cellar entries (OSM and Register points; the cellars were not picked out). Red brick is '?' for the Lester-Garland House (brick, colour not seen) and the Green Family Forge (brick chimney, colour not given).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Trinity Wreck (probably the Speedwell, 1781) | Trinity Harbour, NL (Register 3596, 48.3665, -53.3485) | Register: a mid-1700s merchant vessel sunk in shallow water, a Provincial Historic Site | Underwater; whether divers may visit; left out |
| James Ryan Shop | Elliston, NL (48.6339, -53.0391, Register 2301) | Register: 1900 three-storey merchant's store with a "JAMES RYAN LTD." sign on the gable end and a dumbwaiter | Present use and a look at the pin |
| Clarenville Railway Station | Clarenville, NL (7 Stanley Crescent, Register 7280) | Register: 1942 hip-roofed CN station with verandah; Clarenville was a railway service centre from 1891 with a roundhouse | Present use, hours, pin |
| The Currie Premises | Britannia, Random Island, NL (48.1461, -53.7207, Register 2061) | Register: 1921 house with its original slate roof, tied to the Welsh-run Currie slate industry | Present use, pin; the slate quarries themselves |
| John Quinton Limited premises | Red Cliffe, NL (48.5752, -53.4943, Register 2338 and three more) | Register: shop, post office, residence and fish and salt store of a merchant firm | Statements for the other three, pin |
| Holy Martyrs Anglican Church and the Coaker gravesite | Port Union, NL | Register heritage district: Gothic Revival church with twelve memorial stained glass windows; Coaker's marble tomb and bronze bust on the hilltop; The Bungalow | Own pins and visiting times |
| Bonavista Bay region houses | Bonavista and Trinity, NL (Register list) | Many registered houses (Bridge House, Templeman houses, Lawrence Cottage, Slade House, Gover House) | Present use; mostly private houses |

## Tips
- Canadian Register list pages use `{{HPC row}}`, which `wiki_raw.py --rows` does not read ("0 rows"); parse the cached raw text in `research/wikiraw/` for `idp`/`idf`/`idm`, `lat`, `lon`, `name`. `idp` worked as the historicplaces.ca id.
- `page.py https://www.seethesites.ca/sites/trinity/` returned an image's bytes; the Trinity Sites page is `https://www.seethesites.ca/?p=37`.
- The Register list point for the Trinity Train Loop is about 5.5 km off (at Goose Cove); OSM's "Trinity Rail Loop" line and the "Trinity Loop Fun Park" area are at 48.3657, -53.3983. The Register point for the Dan Goodland root cellar is in Elliston village, 1.4 km from Maberly where the Register text puts it.
- heritage.nf.ca reset the connection again.
- A web search for Elliston root cellars returned only Australian wineries; search the town's site (townofelliston.ca) instead.
