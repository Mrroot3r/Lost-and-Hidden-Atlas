# az_rqhw: Yavapai County, Arizona
state: Arizona
region: az
date: 2026-11-19
places: 16
file: data_az_rqhw.py

## What this batch is
Sixteen places in Yavapai County, Arizona, the first batch in central Arizona (only Cochise County had been worked). Ruins: Tuzigoot pueblo and Montezuma Castle (Sinagua, 1100s–1400s). Standing: Fort Verde (Camp Verde); in Jerome the town itself, the Douglas Mansion (Jerome State Historic Park), the Jerome Grand Hotel (the 1926 United Verde Hospital) and the Audrey shaft headframe; in Prescott the Sharlot Hall Museum and 1864 Governor's Mansion, the Yavapai County Courthouse, the Hassayampa Inn and the old Sacred Heart church (now the Prescott Center for the Arts); in the Bradshaws the Walker charcoal kiln, Palace Station stage stop, the Crown King Saloon, the Mayer Red Brick Schoolhouse and Stanton. Sources: Wikipedia read with `wiki_raw.py` (the Yavapai County and Prescott Register lists with `--rows`); Arizona State Parks facility pages (Fort Verde, Jerome, Audrey Headframe) and NPS fee and things-to-do pages read with `page.py`; the Jerome Historical Society's Mine Museum and Audrey pages; HMdb (Mine Museum/Fashion Saloon); the Palace Station Register form (NPGallery text); Arizona Highways' Prescott to Crown King drive; the Jerome Grand Hotel's own page; one hiking write-up (prestonm.com) for the Walker kiln trail and parking. Not checked: current hours at Tuzigoot and Montezuma Castle (the NPS hours pages are drawn by script; only 2015–16 releases were read), Sharlot Hall Museum (its site answered 403), the Hassayampa Inn and Crown King Saloon (site would not connect); the Prescott National Forest's own pages for the kiln and Palace Station; whether visitors may enter Stanton (LDMA camp) or Palace Station. Pins that mark an area, not the thing: Tuzigoot (pueblo walls not seen on the aerial), Walker kiln (under pines), Mayer schoolhouse (Register two-decimal point on a ballfield), Audrey headframe (placed by eye next to the state park), Stanton, Jerome (pin on the Mine Museum). Audrey Headframe Park was closed for restoration as of the state park page read in this session. Brick: Mayer schoolhouse 'yes' (article: red brick walls); 'no' from the sources' materials for the adobe mansion, concrete hotel, granite courthouse, stone pueblos and kiln, log Palace Station and wooden headframe; seven left '?'. Nothing was seen on the ground.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Woolsey Ranchhouse Ruins | Humboldt, AZ (34.511944, -112.231111) | Register row and stub article: remnant of King Woolsey's 1863 ranch, 0.8 acre north of Humboldt off Route 69 | Owner and any public access; ruin not looked for on the aerial |
| Little Daisy Hotel | Jerome, AZ | Jerome State Historic Park article: Douglas's concrete miners' dormitory, now a private house | Pin; view-only entry would do |
| Clarkdale Historic District, Clark Memorial Clubhouse | Clarkdale, AZ (34.774167, -112.058611) | Register rows; United Verde company town for the smelter | Article text has little; no description of what stands read |
| UVX smelter complex, Clemenceau school | Cottonwood, AZ (34.7325, -112.026111) | Register rows: copper smelter buildings 1917–36; Clemenceau school now a museum | Not read |
| Santa Fe, Prescott and Phoenix depot; Elks Theater; Hotel Vendome | Prescott, AZ | Register rows; Vendome has an article (1917 hotel) | Not read; prescottelkstheater.org would not connect |
| Perkinsville Bridge, Little Hell Canyon Bridge | Perkinsville / Drake, AZ | Perkinsville: 1913/1921 spans moved from San Carlos in 1936 (article) | Access and condition |
| Maxton (Senator Mine) remains | Senator Highway, Prescott NF | Arizona Highways: steel skeleton and concrete base at about mile 10 | Coordinate and Forest Service page |
| Mingus Lookout Complex | Mingus Mountain, AZ (34.694167, -112.127222) | 1935 steel tower with wooden cab (article) | Access from the Forest Service |
| Camp Date Creek | Date Creek, AZ (34.2625, -112.923333) | Register row (Camp McPherson) | Owner, what is left |

## Tips
- NPS `planyourvisit/hours.htm` pages for Tuzigoot and Montezuma Castle return only headings to `page.py` (the hours are drawn by script); the `things2do.htm`, `basicinfo.htm` and `fees.htm` pages read in full.
- Arizona State Parks: `azstateparks.com/<park>/explore/facility-information` gives hours, holiday hours and fees in one page with `page.py --all`; the park's `things-to-do/<name>` pages carry closures (Audrey headframe).
- sharlothallmuseum.org answers 403 with no archived copy; web search returned only directories for its hours.
- Wikipedia coordinates for Montezuma Castle and the Douglas Mansion fell on roads; `osmnear.py ... -g 'viewpoint'` found the trail viewpoint below the castle.
- Several web searches here returned titles and links only, with no quoted text, so hours could not be read from the results.
