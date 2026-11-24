# wv_hqmn: West Virginia: a third scatter across the state
state: West Virginia
region: wv
date: 2026-11-24
places: 14
file: data_wv_hqmn.py

## What this batch is
Fourteen places in twelve West Virginia counties that had none (Hancock, Ritchie, Tyler, Doddridge, Barbour, Brooke, Preston, Randolph, Greenbrier, Hardy, Monroe and Pocahontas): the Peter Tarr and Valley furnaces, Rehoboth Church, the Wells Inn, the Old Stone House, Old Stone Tavern, Bethany's Old Main, two covered bridges, the Fairfax Stone, the decagonal barn, Helvetia, Cheat Summit Fort and the Blue Sulphur Springs Pavilion. Chosen from the county National Register lists (`wiki_raw.py --rows`); facts come from the Wikipedia articles, the United Methodist history commission page (Rehoboth) and quoted search results (Greenbrier Historical Society, Hancock County park, Forest Service). Not checked: any hours except Rehoboth's start time and the pavilion's 8 to 5 viewing; parking for every place; who owns Center Point Bridge, the decagonal barn and the Old Stone Tavern; what stands of the Peter Tarr Furnace beyond the 1968 rebuild. Pins: the Register points for Wells Inn and the Blue Sulphur pavilion were off (a park; woods 220 m away) and were moved, the first by the geocoder, the second by the aerial. Peter Tarr and Helvetia are area pins. Pictures: two chosen, Valley Furnace none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cook's Mill | Greenville, Monroe County (37.545, -80.687) | Grist mill of 1857 on a 1796 site, Register 1989 | Whether visitors can enter; owner |
| Mollohan Mill | Replete, Webster County (38.682, -80.471) | Mill of 1894, ran to 1953, Register 1982 | Owner and access |
| Salt Sulphur Springs Historic District | Union, Monroe County (37.57, -80.569) | Register district of an old spa | Not read at all |
| Fish Creek Covered Bridge | Hundred, Wetzel County (39.672, -80.4525) | Kingpost bridge of 1881, replaced by another in 2001 | Whether any of the old bridge survives |
| Sam Black Church | Smoot, Greenbrier County (37.899, -80.631) | Carpenter Gothic church of 1902 on the Midland Trail | Services; interior |

## Tips
- Ritchie County Historical Society (`ritchiehistoricalsociety.com`) answered 502 and Swiss Historical Village (`swisshistoricalvillage.org`) 403 from `page.py`; neither archived copy could be read.
- `gcah.org/landmarks/` pages (United Methodist history commission) give visiting times plainly with `page.py -g`.
- The Register list coordinates for the Blue Sulphur Springs pavilion fell in woods 220 m from it; the pavilion is a small roofed square beside the road on the aerial.
