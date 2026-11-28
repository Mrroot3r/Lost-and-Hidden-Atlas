# ak_vfdr: Alaska: Anchorage, the Railbelt, the Yukon and the Arctic
state: Alaska
region: ak
date: 2026-11-28
places: 13
file: data_ak_vfdr.py

## What this batch is
Thirteen places across Alaska, which had 65: Old St. Nicholas Church at Eklutna, Potter Section House, the Crow Creek Mine at Girdwood and the Pioneer School House in the Anchorage area; the Nenana Depot, Tolovana Roadhouse, Ruby Roadhouse, Christ Church Mission at Anvik, Presentation of Our Lord Chapel at Nikolai, Slaven's Roadhouse on the Yukon, Central House on the Steese Highway and the Arctic Village mission church; and the Susitna River Bridge at Gold Creek. All were National Register listings the Atlas lacked (tools/gaps.py: Anchorage and Yukon-Koyukuk). Sources: the Park Service forms (tools/form.py), Wikipedia (tools/wiki_raw.py), the Alaska State Parks page for Potter, the Crow Creek Mine's front page and an AP story in the Anchorage Daily News. Web search was used only to find pages.
Not checked: hours for every place (the Eklutna park's and the Nenana Friends' pages would not open; no hours page found for the others), who owns or keeps the roadless village buildings today, whether Central House and the Anvik mission buildings still stand, and brick for most. Seven pins are prec 'area' because the Register point fell in forest, marsh or a car park on the aerial. The Susitna pin was moved 30 m onto the bridge. Pictures: only Tolovana has one (a USGS photograph); Ruby and Central House have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Anchorage Depot | Anchorage (61.21541, -149.89028) | 1942 Moderne reinforced-concrete depot, J.B. Warrack Co. (form read) | Left out as Moderne, in doubt under the modernism rule; an owner may decide |
| Old Mission House | Fort Yukon (66.56774, -145.27578) | Episcopal mission house, later a clinic; owner the Diocese of Alaska in 1978 (form read in part) | Description, present state, pin |
| Woodchopper Roadhouse, Coal Creek mining district, Beiderman Fish Camp | Eagle area, Yukon-Charley | Register listings 87001201, 95000573, 87001204 | Forms and access not read |
| Denali ranger cabins (86003206 to 86003231) | Denali National Park | Sixteen Register listings of 1980s patrol cabins | Not read; backcountry, permit needed |
| Fourth Avenue Theatre, Kimball's Store, Leopold David House, AEC cottages 23 and 25 | Anchorage | Register listings 82001620, 86001901, 86001900, 90000825, 96000094 | Not read |
| Bettles Lodge, Sourdough Inn | Bettles, Fort Yukon | Register listings 97000401, 97001585 | Not read |

## Tips
- page.py on guessed managing-body addresses mostly gave 404 (nps.gov yuch, dnr.alaska.gov potterhouse, eklutna-nsn.gov); a web search for the name found the real address (Potter: dnr.alaska.gov/parks/aspunits/chugach/potrangerst.htm).
- wiki_raw.py gave clean text where page.py on the same article returned raw template code; use it for Wikipedia.
- In Alaska most Register points for roadless village buildings and mines fall in forest on the aerial; expect prec 'area'.
- tools/app_smoke.js is for the Android app; for the hosted build use tools/smoke.js with dist served on port 8766.
