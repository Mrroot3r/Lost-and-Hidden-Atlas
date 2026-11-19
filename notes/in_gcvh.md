# in_gcvh: Indiana: a first scatter, Lake Michigan to the Ohio
state: Indiana
region: in
date: 2026-11-19
places: 19
file: data_in_gcvh.py

## What this batch is
Indiana's first real batch: 19 places spread across the state (Indiana had only Rose Island before). Mostly standing places people can go into: the territorial and first state capitols (Vincennes, Corydon), Grouseland, Lanier Mansion, the Levi and Catharine Coffin house, West Baden Springs Hotel, the Rotary Jail, the Indiana Medical History Museum, the Old Michigan City lighthouse, the Bailly Homestead, and mills at Spring Mill, Mansfield and Bonneyville; with Cannelton Cotton Mill, Duck Creek Aqueduct, the Laughery Creek "Triple Whipple" bridge and Huddleston Farmhouse to see from outside, and two ruins/traces: Brough's unfinished railroad tunnel in Clifty Falls State Park and the lost town of Hindostan Falls. Facts come from Wikipedia (`wiki_raw.py`) and the managing bodies' own pages read with `page.py` (Indiana State Museum plan-your-visit pages, DNR park pages and the DNR Brough's Folly brochure, Grouseland, Indiana Landmarks, Michigan City Historical Society, Elkhart County Parks, imhm.org, rotaryjailmuseum.org, NPS). Not checked: anything on the ground; interiors beyond what Wikipedia describes; Mansfield Roller Mill's hours (the DNR page answers 404); park entrance fees at Clifty Falls and Spring Mill; Hindostan Falls hours and where exactly the mill holes are (pin is the DNR ramp); who owns the Laughery Creek bridge now (marked view, conf mixed); most parking. Huddleston Farmhouse was sold by Indiana Landmarks to a private family (Inside INdiana Business), so it is view-only even though older pages offer tours. Red brick was set only where a source says: Grouseland and the Rotary Jail are red brick; Lanier (painted ochre) and the Coffin house (painted red) are 'no'; West Baden, Huddleston, the medical museum, the lighthouse, Bailly and Mansfield are '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| New Harmony Harmonist buildings | New Harmony, IN | A New Harmony State Historic Site exists under Indiana State Museum | The right page (the guessed address served another site's page); pick the best single building |
| Old Treasury Building and Posey House | Corydon, IN | Named in the Corydon Historic District article | Own sources and whether they open |
| Fort Knox II and Sugarloaf Mound | Vincennes, IN | ISM page: free self-guided outdoor visits Wednesday to Sunday | A description of what is left at Fort Knox II |
| Wabash and Erie Canal remains | Delphi / Fort Wayne, IN | Wikipedia article on the canal | A particular lock or section with a public way in |

## Tips
- indianamuseum.org: a wrong slug under /historic-sites/<slug>/plan-your-visit/ quietly serves the T. C. Steele page (identical text for every guess). The real slugs found: corydon-capitol-historic-site, lanier-mansion-historic-site, vincennes-state-historic-site, levi-and-catharine-coffin-state-historic-site, whitewater-canal-historic-site.
- Indiana DNR's nature-center page for Mansfield Roller Mill answers 404 on both www and secure, and page.py could not fetch the archived copy.
- The pin check's land map holds Indiana state parks, state historic sites and the Hindostan Falls fishing area, but not the Whitewater Canal site at Metamora.
