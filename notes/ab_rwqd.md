# ab_rwqd: Alberta from Fort Chipewyan to Cardston: an oil-sands plant, a straw church, mills and a temple
state: Alberta
region: ab
date: 2026-11-23
places: 13
file: data_ab_rwqd.py

## What this batch is
Thirteen places across Alberta (46 before, 59 after), spread from Fort Chipewyan and Bitumount in the far north through the parkland and Edmonton to Calgary, Cochrane, Raymond, Cardston and Waterton. Each was read from its Canadian Register of Historic Places statement (historicplaces.ca, one request at a time) with Wikipedia as raw text for coordinates and a few facts; hours and access came from web-search results only, because the operators' own pages were scripted or would not open (Dickson Store, Donalda museum) or gave nothing. Not checked: hours for Dickson Store and Donalda Creamery (listings disagree, so `hours='?'`), whether the Rossdale tours still run, ownership of Newbrook Observatory, Raymond Buddhist Church and the Fort Chipewyan church, and anything on the ground. Pins: Fort Chipewyan (the Register point is on a river island) moved to the middle of the hamlet, Cochrane Ranche (Register point in a housing area) moved to the mapped park, the Cardston temple moved onto the building; Bad Heart, Donalda, Fort Chipewyan and Cochrane could not be matched to a building on the aerial and are `prec='area'`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bad Heart Straw Church | Teepee Creek, AB (55.485, -118.288) | On the Atlas, but the pin is only the Register point in open farmland | The church itself on the aerial, and whether it is kept up |
| Stirling Agricultural Village, Blood Indian Hospital (Cardston), Alberta Wheat Pool elevator at Paradise Valley, Russo-Orthodox Church of the Transfiguration (Star) | southern and central Alberta | Listed in the Register lists on Wikipedia with Register ids 7773, 9737, 10403 | Not read this session |

## Tips
- historicplaces.ca pages are long; cut the text between "Description of Historic Place" and "Recognition" and you have what is wanted.
- Wikipedia's Alberta Register lists give the same coordinate as the Register, and four of them were wrong here (an island in the Athabasca, a housing estate, open fields).
- The Edmonton and Calgary list titles are "List of historic places in the Edmonton Capital Region" and "...the Calgary Region"; "...in Edmonton" and "...in Calgary" are redirects with no rows. Read them from research/wikiraw/ by splitting on `{{HPC row`.
- `nom.py` knows almost nothing in rural Alberta; `look.py` at 700 m could not pick out a church in Fort Chipewyan.
- The Commons sign photograph at Bitumount ("No unauthorized entry") is a better access source than any page found.
