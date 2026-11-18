# mec_lqkw: Lincoln County, Maine: colonial meeting houses, forts, pounds and a schooner hulk
state: Maine
region: mec
date: 2026-11-18
places: 18
file: data_mec_lqkw.py

## What this batch is
Eighteen places in Lincoln County, Maine (region `mec`, drawn by `choose.py`; nothing was on the map within 25 km of Wiscasset before): Fort Edgecomb, Colonial Pemaquid with Fort William Henry, Whaleback Shell Midden, the Cora F. Cressey schooner hulk at Keene Narrows, Clary Mill, the stone pounds of Jefferson and Waldoboro, the meeting houses of Walpole, Harrington (Bristol), Alna and the Old German Meeting House at Waldoboro, St. Patrick's Church at Damariscotta Mills, the Pownalborough Court House, the Old Jail at Wiscasset, the Chapman-Hall House, the Red Brick School at Wiscasset, Pemaquid Point Light and the Thompson Ice House. Facts come from Wikipedia read as raw text with `wiki_raw.py`, and from `page.py` reads of the Maine Bureau of Parks and Lands pages, the Colonial Pemaquid brochure PDF, the state day-use fee table, Coastal Rivers Conservation Trust, Maine Historic Preservation Commission "Did you know" pages, the Old German Meeting House, Thompson Ice House and Fishermen's Museum sites, and Lincoln County News, Wiscasset Newspaper, Bangor Daily News and Island Institute articles. Not checked: nothing on the ground; the Lincoln County Historical Association's hours (its site answered 403; hours are from 2019 and 2025 newspaper notices, so those three places are `conf='mixed'`); Fort Edgecomb's season (from Fort Tours, not the state; the state's own page for it was not found); St. Patrick's Mass times (parish page 403); whether the Red Brick School is still a gallery; Clary Mill's present condition; the owners of the Jefferson pound and Clary Mill (both view-only from the road). No public shore viewpoint was found for the Cora F. Cressey: it is marked `boat`. Pins: eight were moved with `pix.py` or set to an ArcGIS address point after the aerial; the Jefferson pound is `area` (neither aerial nor LiDAR shows it); the Whaleback parking is the Round Top Farm lot, since the site's own small lot is not mapped.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hendricks Head Light | Southport, ME (43.82258, -69.68973) | 1875 tower and keeper's house; keeper's house a private summer home (Wikipedia) | A public viewpoint (beach or road) from a source |
| Glidden Shell Midden | Newcastle, ME, across the Damariscotta from Whaleback | Largest midden in Maine (Wikipedia, Whaleback article) | Owner and whether any public way reaches or views it besides from the river |
| Fort Popham and the Popham Colony site | Phippsburg, ME (Sagadahoc County, region mec) | Not researched this session | Everything; next county west |
| Burnt Island Light, Cuckolds Light, Ram Island Light | Boothbay Harbor and Southport, ME | Register-listed light stations | Access (boat tours?) from the managing bodies |
| Head Tide Historic District | Alna, ME (44.114722, -69.624444) | Register-listed village with a mill-dam site on the Sheepscot | A source for what stands and can be seen |

## Tips
- lincolncountyhistory.org answers 403 to `page.py`, and the archived copy could not be fetched; Lincoln County News (lcnme.com) and Wiscasset Newspaper season notices carry the LCHA museum dates.
- The Maine state park day-use fee page (maine.gov/DACF/parks/park_passes_fees_rules/park_day_use_fees.shtml) reads with `page.py --all` and gives fees for every state historic site in one place; no maine.gov page for Fort Edgecomb's season turned up in search.
- bristolmaine.org's park pages (Pemaquid Point Lighthouse Park) answer 404 at the addresses search results give; thefishermensmuseum.org gives the park season.
- Wikipedia coordinates in Lincoln County were often 30 to 200 m off the building (8 of 18 moved); the ArcGIS geocoder's PointAddress hits were on or near the buildings.
- `places_test.js` still fails only on `onesquethaw-valley` (as the mes_vpdi note said); this batch does not touch it.
