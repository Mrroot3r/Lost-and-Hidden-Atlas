# ct_fhib: Winsted, Riverton, Norfolk and Collinsville, Connecticut
state: Connecticut
region: ct
date: 2026-11-18
places: 16
file: data_ct_fhib.py

## What this batch is
Sixteen places in the northeast corner of Litchfield County (Winsted, Barkhamsted and Riverton, Colebrook, Norfolk, New Hartford) and Collinsville in Canton, region `ct` drawn at random by `choose.py`. Mostly standing places: the CCC museum and log shelter in the two Barkhamsted state forests, a cheese-box factory wheel pit on the Henry Buck Trail, Saville Dam, the 1829 Union Church and the 1811 inn at Riverton, the Gilbert clock works and the Winsted hosiery mill, the Winchester Soldiers' Monument tower, the Solomon Rockwell House, the 1812 Colebrook Store, the Haystack Mountain and Dennis Hill summit buildings, the abandoned Norfolk Downs golf shelter, Gillette's grist mill with its wheel, and the Collins Company axe works with the Canton Historical Museum. Sources read: Wikipedia with `wiki_raw.py` (the National Register rows for Litchfield and Hartford counties), CT DEEP park pages (ctparks.com and portal.ct.gov, hours read from the "Open Daily" line), DEEP's letterbox page for American Legion State Forest (the only source for the cheese-box factory), the Peoples State Forest Nature Museum and Canton Historical Museum sites, ConnecticutHistory.org, Buildings of New England and one Lakeville Journal article. Not checked: anything on the ground; the cheese-box ruin's exact spot (area pin on the trail); whether the Old Riverton Inn and Colebrook Store still trade, and their hours; the glass studio's hours in Union Church; the Solomon Rockwell House's current hours (the Winchester Historical Society's own site was not found: searches return Winchester, Massachusetts); the MDC's rules at Saville Dam (its rules PDF answered 404); who owns the Norfolk Downs shelter and the Winsted monument park; which Collinsville buildings were Collins Company buildings; the Canton museum's hours outside its November 15 to December 6 holiday hours. Red brick from the Wikipedia descriptions: yes for the clock factory and hosiery mill, some for the inn's brick basement, unset for Saville Dam and the Collins works. Barkhamsted Lighthouse is already on the map (`data_woods.py`) and was left alone.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Hitchcock Chair factory | Riverton, Barkhamsted, CT | Lambert Hitchcock opened a chair factory here in 1818; John Kenney found it abandoned in 1946 and revived the company until 2006 (Wikipedia, Lambert Hitchcock) | A source on the building that stands, its date, and a pin |
| Hitchcock-Schwarzmann Mill site | Foote and Vineyard Roads, Burlington, CT (41.78167, -72.96167) | Mill of about 1781, Register 1977, since demolished; foundation remnants survive beside the 18th-century miller's house (Wikipedia) | Owner and whether anything shows from the road; likely private |
| Camp White remnants | Youth group camping area, American Legion State Forest, Barkhamsted, CT | DEEP says remnants of the CCC camp are visible in and around the group camping area | What the remnants are and where; folded into the CCC shelter entry for now |
| Norfolk town green and churches | Norfolk, CT | Register district with a Federal church of the early 1800s, a Romanesque church, the 1888 Keller library and a Stanford White fountain (Wikipedia, Norfolk Historic District) | Each building's own source and whether the churches open |
| Pine Meadow power canal | New Hartford, CT (41.87528, -72.96778) | Roger Sheldon dammed the West Branch in 1806 and dug a power canal across the bend between Wickett and Main Streets (Wikipedia, Pine Meadow Historic District) | Whether any of the canal can be seen, and from where |

## Tips
- CT DEEP's newer park pages are at `portal.ct.gov/deep/state-parks/parks/<name>`; for the state forests the working address was `ctparks.com/parks/<name>` (`portal.ct.gov/deep/state-parks/forests/peoples-state-forest` answered "Oops", 404).
- DEEP's "Seedling letterbox" clue pages (`portal.ct.gov/deep/forestry/letterboxing/...`) describe ruins along a forest trail step by step; they gave the only account of the cheese-box factory on the Henry Buck Trail.
- `wiki_raw.py` prints only the first 1,500 characters of an article; the rest is in `research/wikiraw/<title>.txt`, or read it with `-g`.
- The Register list coordinate for the Solomon Rockwell House, Winsted, falls in woods 50 m west of the house; the ArcGIS geocoder found 225 Prospect Street on it.
- Searches for the Winchester Historical Society (Connecticut) return the one in Winchester, Massachusetts first; its hours page is not Winsted's.
