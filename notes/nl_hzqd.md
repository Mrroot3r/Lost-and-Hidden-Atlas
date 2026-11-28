# nl_hzqd: across Newfoundland and Labrador (2026-11-28)

## What this batch is
Fourteen places spread over parts of the province the three earlier batches did not reach (region nl, drawn by the thinnest-ground rule): the Labrador coast (Battle Harbour, Hopedale Mission, Hebron Mission), the Great Northern Peninsula and Gros Morne (L'Anse aux Meadows, Lobster Cove Head), the south coast (Rose Blanche), Corner Brook (Glynmill Inn), Notre Dame Bay (Long Point at Twillingate, Bleak House at Fogo, Tilting), Greenspond Courthouse, and the southern Avalon (Colony of Avalon at Ferryland, Cape Race, Castle Hill at Placentia).

Sources: the Canadian Register of Historic Places statement for each place (read with page.py); Wikipedia's regional lists of historic places (raw) for the Register ids and positions. Hours and seasons came from web search results that quote the managing body's own pages (Parks Canada, Battle Harbour, Colony of Avalon, Town of Fogo Island); the pages themselves are drawn by script and page.py could not read the hours. The entries say so. Provincial tourism listings were the only source for Long Point and Rose Blanche. Brick is "?" where no picture or source was opened.

Not checked: the interiors; parking for most places (no th= points); owners of Rose Blanche, Long Point, Glynmill, Tilting; Hebron's access (sources differ on whether it is inside Torngat Mountains National Park). Pins: Hopedale, Rose Blanche, Glynmill, Bleak House, Greenspond, Cape Race and Castle Hill were moved from the Register position by looking at the aerial or using OpenStreetMap. L'Anse aux Meadows' aerial would not load twice (red tile), so its pin is the Register's and marked "area". Pictures: 14 chosen on Commons.

## Leads not finished
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Port au Choix National Historic Site | Port au Choix | Register id 11464 (archaeological site) and a Parks Canada page | Not read |
| Red Bay National Historic Site (Basque whaling station) | Red Bay, Labrador | Parks Canada page found | Not read |
| Rigolet: Hudson's Bay Company Net Loft | Rigolet | Register id 2235 | Not read |
| Argentia 282 Coastal Defence Battery | Placentia | Register list entry | Not read |
| Woody Point heritage houses (Bond Store, Old Loft, Haliburton House) | Woody Point | Register ids 4048, 4032, 4049 | Not read |
| Mistaken Point and the Myrick Wireless Interpretation Centre | Portugal Cove South | Seasonal centre, 709-438-1100 (listing) | Not read |
| Boyd's Cove Beothuk NHS; Ashbourne's premises; Harbour Breton and Gaultois sites | Notre Dame Bay, south coast | In the Register lists | Not read |

## Tips
- historicplaces.ca pages read at 3-second pauses with no resets in this session. Its text carries no street address or coordinate: take the position from the Wikipedia list's `lat`/`lon` (the `{{HPC row` fields), which were wrong for rural lighthouses and the Hopedale mission (by 100 m to 2 km); OpenStreetMap via nom.py fixed most.
- parks.canada.ca "visit" pages drew their hours by script; a web search for the site's name and "hours of operation 2026" quotes them.
- The aerial for L'Anse aux Meadows (51.598, -55.562) came back as a red tile on three tries.
- `choose.py --claim --thinnest` worked as the prompt said.
