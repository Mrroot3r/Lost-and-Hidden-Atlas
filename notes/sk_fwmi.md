# sk_fwmi: Saskatoon, Batoche and the South Branch, Saskatchewan
state: Saskatchewan
region: sk
date: 2026-11-18
places: 15
file: data_sk_fwmi.py

## What this batch is
The first places in Saskatchewan: fifteen in Saskatoon and the South Saskatchewan country north of it. On the South Branch: Batoche (church, rectory and village site), the Tourond's Coulee / Fish Creek battlefield, the St. Laurent shrine and its 1883 rectory, and Fort Carlton (a 1967 partial reconstruction over the real post's remains). Near Rosthern and Blaine Lake: Seager Wheeler's farm and the Doukhobor Dugout House. In Saskatoon: the Marr Residence, the Little Stone Schoolhouse, the College Building, the CPR station, the Bessborough, the Pioneer (Nutana) Cemetery, Next of Kin Memorial Avenue, the Forestry Farm (Sutherland nursery station) and Wanuskewin. Sources: Wikipedia through `wiki_raw.py`; the Canadian Register of Historic Places statement for each place (historicplaces.ca reads fully with `page.py --all`; it gives character-defining elements, which is what survives); City of Saskatoon heritage-register and park pages; Parks Canada (Tourond); the Museums Association of Saskatchewan listings; Tourism Saskatchewan; and the Seager Wheeler Farm, Wanuskewin, Diefenbaker Canada Centre and Town of Borden pages. Red brick was settled from the Wikipedia photographs (`brick.py look`) for the Bessborough (yes) and the Forestry Farm's Superintendent's Residence (some); the CPR station is yellow brick by its register entry (no). **Not checked:** hours for Batoche (Parks Canada's hours page is drawn by script; the Museums Association's May 15 to September 15, 9 to 5 was used), Fort Carlton (Sask Parks' page is drawn by script), the St. Laurent shrine, the Pioneer and Woodlawn cemeteries; Fish Creek, the shrine, the Dugout House and the Seager Wheeler farm have no mapped parking; the Dugout House, Forestry Farm and Wanuskewin pins mark the general area, not one feature; the Little Stone Schoolhouse is hidden by trees on the aerial. The Borden page's "436-foot dugout for nine families" is not in the register (conf mixed). The schoolhouse date is 1887 (City) or 1888 (Wikipedia). Nothing was checked on the ground. There is no public-land layer for Canada, so every pin printed CHECK ACCESS; each access note names the owner from its source.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Battle of Duck Lake site | Duck Lake, SK (52.8242, -106.2742 from the Wikipedia list) | National historic site, 12-hectare grassed lot with a 1950 HSMBC cairn, within Beardy's and Okemasis' reserve (Canadian Register 12916) | Whether and how visitors may go onto reserve land; a cairn only |
| Gabriel's Crossing, Clarke's Crossing | South Saskatchewan above Batoche | Named in the Batoche and Fish Creek articles as 1885 ferry crossings | Any source saying something is left to see, and access |
| Fort Battleford, Old Government House | Battleford, SK | Parks Canada fort (1876) and the 1879 Government House, both national historic sites on the Wikipedia list | Not researched (about 140 km from Saskatoon); a good next batch with the Battleford Court House |
| Prince Albert: former City Hall, Keyhole Castle, Diefenbaker House | Prince Albert, SK | National historic sites on the Wikipedia list (1893, 1913) | Not researched; a next batch with Fort à la Corne |
| Claybank Brick Plant | Claybank, SK (50.05, -105.23) | National historic site, brick works 1914–1989; made the Bessborough's bricks | Not researched (southern Saskatchewan) |

## Tips
- `tools/ortho.py`: Esri's World_Imagery `export` answered HTTP 500 at pin-check zoom for every rural pin in Saskatchewan (Batoche, Fort Carlton, Rosthern, Blaine Lake) while it worked in Saskatoon and at wider views; the same imagery came as tiles. This batch added a tile fallback after the export in `ortho()`; before it, every rural tile was a red DOWNLOAD FAILED however often it was rerun.
- historicplaces.ca (the Canadian Register) reads fully with `page.py --all`; cut the text from "Description of Historic Place" to "Recognition Authority". Wikipedia's national-historic-site list gives each place's register id in `{{CRHP|id|...}}`.
- `wiki_raw.py --rows` finds no rows on Canadian list pages (they are not NRHP tables); read the saved raw text in `research/wikiraw/` and split it on `|-`.
- Parks Canada hours pages (`parks.canada.ca/lhn-nhs/sk/batoche/visit/heures-hours`) and Sask Parks pages (`saskparks.tourismsaskatchewan.com/...`) are drawn by script; the Museums Association of Saskatchewan listings (`saskmuseums.org/places/...`) give season and hours in plain text.
- Wikipedia's Nutana Pioneer Cemetery coordinate is a degree south (51.10); `nom.py` finds the cemetery at 52.1005, -106.6833.
- `start.py` lists Saskatoon as Saskatchewan's start city and has no leads layers for Canada, so the briefing is empty; begin from the Wikipedia national-historic-site list.
