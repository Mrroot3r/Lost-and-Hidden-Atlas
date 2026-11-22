# wi_plir: Wisconsin: a first scatter from Lake Superior to Lake Michigan
state: Wisconsin
region: wi
date: 2026-11-22
places: 16
file: data_wi_plir.py

## What this batch is
Sixteen places spread over Wisconsin outside the lead region that wi_axaz covered: the Plummer Mine headframe (Pence) and the Hokenson Brothers Fishery (Little Sand Bay) in the north, the SS Meteor whaleback (Superior), the Mabel Tainter building (Menomonie), the Octagon House (Hudson), Hixon House (La Crosse) and Villa Louis (Prairie du Chien) on the west, the Indian Agency House and the Fort Winnebago Surgeons Quarters at Portage, the Grignon Mansion (Kaukauna), the Cana Island and Eagle Bluff lighthouses in Door County, the Cedarburg covered bridge and the Grafton lime kilns in Ozaukee County, Wade House (Greenbush) and St. Joan of Arc Chapel (Milwaukee). All standing except the lime kilns (ruins). Sources: Wikipedia raw text and the county Register list rows (`wiki_raw.py`), the Plummer Register form (NPGallery, text layer), HMdb, and each manager's own page read with `page.py` (NPS, Door County, Door County Maritime Museum, Door County Historical Society, Wisconsin DNR, Wisconsin Historical Society, Marquette, City of Kaukauna, agencyhouse.org, fortwinnebagosurgeonsquarters.org, mabeltainter.org, hudsonoctagonhouse.org, lchshistory.org). Not checked: anything on the ground; the SS Meteor's hours (superiorpublicmuseums.org did not answer); the Surgeons Quarters' days and times (its visit page answers 404); Eagle Bluff's 2026 hours (only the society's 2025 notice was read); Villa Louis's days and times; Hixon House's summer hours; the owner of the Plummer headframe park and of Lime Kiln Park's hours; the Hokenson site's season. Wade House hours come from the Wisconsin Historical Society's own 2026 release as reprinted by Urban Milwaukee. The Lime Kiln Park pin was moved with `pix.py` onto masonry the aerial shows by the lot, taken to be the kilns; Villa Louis's onto the house on the mound (aerial taken in a flood). Red brick: 'no' for the three houses whose Commons photo (chosen in this batch) shows white clapboard, and from sources for the rest; '?' where nothing opened settles it. `check.py` warns that the SS Meteor pin is just outside Wisconsin's outline: it is on Barkers Island in Superior, on the Wisconsin side.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Davidson Windmill | Lakeside, Douglas County, WI (46.648889, -91.905833, Register list) | Finnish immigrant Jacob Davidson's 1900 windmill, grist mill worked 1904–1926 (Wikipedia; Register list). Travel Wisconsin lists it with an Eskolin log house at 3196 South River Road West, South Range | Who owns it, whether it can be visited, and whether it still stands where the Register point is |
| Fort Winnebago Site | Portage, WI (address restricted in the Register list) | The 1828–1845 fort; the Surgeons Quarters is its one surviving building | Whether anything is visible and whether the public may go there |
| Port Washington Light Station | Port Washington, WI (43.391111, -87.8675) | 1860 lighthouse and keeper's house (Register list) | Manager's page and hours |
| Cedarburg mills (Cedarburg Mill, Concordia Mill, Hilgen and Wittenberg Woolen Mill) | Cedarburg, WI (43.296667, -87.986111 and nearby) | Limestone mills of 1853–1865 on Cedar Creek (Register list) | What each is now and whether any can be entered |
| Upper Kickapoo Valley / La Farge dam | La Farge, WI | The valley that was almost dammed (Register list row for the archaeological district) | A source on the abandoned dam works and the Kickapoo Valley Reserve's access rules |

## Tips
- `wiki_raw.py` gave an empty article for "Wade House" (the article exists): read the Register list row instead.
- Guessed titles failed for most Wisconsin houses ("Grignon Mansion", "Hixon House", "Octagon House (Hudson, Wisconsin)"); `--rows -g` on the county list gives the exact names (Charles A. Grignon House, Gideon C. Hixon House, John S. Moffat House).
- The Wisconsin Historical Society's site pages for Villa Louis and Wade House carry only "closed, reopening May 2027" in November; its yearly season releases (wisconsinhistory.org/Records/Article/CS...) give dates and hours.
- `nom.py` answered HTTP 629 once after a run of quick lookups; a few seconds' pause was enough.
