# calgaryvid_wqtn: Calgary: the sandstone city, its churches, bank, courthouse and bridge
state: Alberta
region: ab
date: 2026-11-27
places: 11
file: data_calgaryvid_wqtn.py

## What this batch is
Eleven places in downtown Calgary and the Beltline, from the names in one video of old photographs of the city (job 9, video aSx-HVOvBis; the record is source/videos/20220320_aSx-HVOvBis.md). Added: the Fort Calgary site (The Confluence), the Imperial Bank of Canada building, the Hudson's Bay Company store on Stephen Avenue (now to become condominiums, CTV News, April 2026), Central United, Knox United and First Baptist churches, Courthouse No. 2, the Centre Street Bridge, Fire Hall No. 1, the Calgary Public Building (on the site of the 1894 post office) and the cupola of the demolished Central School in James Short Park. Sources: Canadian Register statements on historicplaces.ca read with page.py one at a time, the City of Calgary's Historic Downtown and Connaught-Beltline walking-tour PDFs and its James Short Park historical research PDF (all three have a text layer), Wikipedia as raw text, The Confluence's visit page and Knox United's own page. Not checked: service times for Central United and First Baptist (no page of either congregation was found), present use of Courthouse No. 2 and Fire Hall No. 1, whether the Public Building lobby is open, which object in the park is the cupola (the pin is the park's address), and the interiors. Brick for Central United and First Baptist comes from the Commons pictures chosen for them.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Calgary Land Titles Office | Calgary, AB | Named in the video; not researched | Whether an old building stands, and a source |
| Alexander Corner | 8 Avenue and 1 Street SW, Calgary, AB | A University of Calgary archive caption, seen only in search results, says it was pulled down in 1929 for the Hudson's Bay store | A page that opens and confirms it is gone |
| Knox Presbyterian stone church of 1886 | Centre Street and 7 Avenue, Calgary, AB | The Register: the first large stone building in Calgary, enlarged 1905 | What became of it |
| Calgary Courthouse No. 1 (1880s) | 7 Avenue SW, Calgary, AB | The Register: built 1888 on the block of Courthouse No. 2; the walking tour gives 1886 | Whether anything is left |

## Tips
- The City of Calgary's walking-tour PDFs (calgary.ca/PDA/pd/Documents/Heritage-planning/heritage-walking-tours/...) read with page.py, but `--all` cuts at 12,000 characters: add `-n 60000`. The Stephen Avenue tour PDF is a scan with no text layer; the Historic Downtown one covers the same buildings.
- In the Wikipedia list "List of historic places in the Calgary Region", the fields idp, idf and idm are the historicplaces.ca place-lieu ids.
- digitalcollections.ucalgary.ca and avenuecalgary.com refused page.py and the web fetch tool (202 and 403).
