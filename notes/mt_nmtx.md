# mt_nmtx: Granite, Powell and Deer Lodge counties, Montana: ghost towns, the old prison and the copper towns
state: Montana
region: mt
date: 2026-11-18
places: 13
file: data_mt_nmtx.py

## What this batch is
Thirteen places in the upper Clark Fork country of Montana, the first pass at this ground (region mt drawn by choose.py): the ghost towns of Garnet (BLM) and Granite (state park), the Charter Oak mine and mill (Forest Service), the Old Montana Prison and its 1915 brickyard, the Grant-Kohrs Ranch and the Rialto in Deer Lodge, and in Anaconda the smelter stack, Glenn's Dam, the Washoe Theater, Club Moderne and City Hall, plus the Philipsburg historic district. Facts come from Wikipedia read with wiki_raw.py, National Register nomination texts from NPGallery read with page.py (Miners Union Hall, Superintendent's House, Prison Brickyard, Charter Oak, Grant-Kohrs, Northern Pacific completion site), and the managing bodies' pages through page.py (BLM Garnet, FWP Granite and Anaconda Stack, NPS Grant-Kohrs, the Old Prison museum). Not checked: anything on the ground; the Prison Brickyard's present state and owner (the 1988 form is the only source, so it is view-only and `mixed`); the Granite union hall's present state beyond FWP calling it a ruin; Charter Oak's gate and open days (only a tourism listing and Legends of America; the 2000 form said the gates were locked); the Washoe and Rialto show times; the Copper Village Museum hours (tourism listing only); who manages the Glenn's Dam trail. Pins: Old Prison moved 97 m off a house across Main Street into the prison yard; Granite and the brickyard are `area` because the ruins could not be picked out on the aerial; Glenn's Dam is pinned on the North Cable Road bridge beside the pump house (`area`). Red brick: only the brickyard (`yes`, red brick kiln walls in the form) and the Granite union hall (`some`, red brick upper storeys on a granite base) are settled; the rest are `?`, Charter Oak `no` (wood, stone and metal per its form).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Bearmouth stage stop | Granite County, MT (Wikipedia 46.71028, -113.33139) | Wikipedia and ghosttowns.com: Mullan Road stage stop whose two-storey balconied inn and livery stable still stand | The Wikipedia coordinate falls on I-90 and the railway; the inn could not be found on a 1.2 km aerial; owner unknown |
| Coloma ghost town | Garnet Range, Missoula County, MT (Wikipedia 46.84306, -113.38056) | Wikipedia: 1893 gold camp, 1916 mill; Visit Montana: cabins, shafts and machinery a couple of miles north of Garnet at the end of a trail | Who owns it (BLM not confirmed), the trail, a pin check |
| Northern Pacific completion site, 1883 | Gold Creek, Powell County, MT (46.550833, -112.86) | Register form 83001075: last-spike site, reached on foot 3/4 mile along the rails from the Clark Fork bridge at the Phosphate exit | Walking along an active railroad is not a legal way in; look for a public viewpoint or marker |
| Old Works Historical Trail | Anaconda, MT | A travel blog: a trail on the ridge west of the Old Works golf course with interpretive signs and smelter ruins | A source from the county or the golf course; discoveranaconda.com answered 403 |
| Anaconda Hearst Free Library, St. Mark's Episcopal, Kohrs Memorial Library, Trask Hall | Anaconda and Deer Lodge, MT | Register list rows with coordinates | An article or form read for each, what survives inside, hours |

## Tips
- NPGallery nomination texts (`https://npgallery.nps.gov/NRHP/GetAsset/NRHP/<ref>_text`) read well with page.py for Montana forms of the 1970s to 2000s; the Glenn's Dam form (100005107, a 2020 listing) came back with only 893 characters. Historic Montana (`historicmt.org/items/show/<n>`) has the state preservation office's summary for such recent listings.
- The National Register list coordinate for the Old Montana Prison lands on a house across Main Street from the prison wall.
- `gh api .../pulls` printed nothing at all in this session (no error, no list); start.py's own open-pull-request count was used instead.
- discoveranaconda.com answers 403 to page.py.
