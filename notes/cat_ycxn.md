# cat_ycxn: Central Sullivan County, NY: Monticello, Liberty, Bethel, Woodbourne and the Borscht Belt hamlets
state: New York
region: cat
date: 2026-11-21
places: 22
file: data_cat_ycxn.py

## What this batch is
Twenty-two places in central Sullivan County, New York (region `cat`, drawn at random by `choose.py --claim --state ny`, which offered Onteora Park, Monticello and New Kingston; the Atlas had nothing in Monticello, Liberty, Woodbourne, Hurleyville, Glen Wild, Mountain Dale, Bethel or Grahamsville). Monticello: the 1909 courthouse, the Rialto Theatre front block (auditorium gone), St. John's Episcopal. Liberty: the downtown district (with the Town and Country Building in its text), the Munson Diner, St. Paul's Lutheran. Fallsburg: the 1815 Hasbrouck Stone House (Register form of 2019 read in full), the Sullivan County Museum in the 1912 Hurleyville school (open, hours from the county's page), the 1886 Fallsburg Tunnel of the O&W seen from the Tunnel Bypass Trail (pin on the northwest portal, which the LiDAR shows), the Woodbourne Shul, Woodbourne Reformed Church and the derelict Center Theatre, the Mountain Dale synagogue and mikvah, the Anshei Glen Wild synagogue and Glen Wild Methodist Church (both now an artist's), the Loch Sheldrake synagogue, and the Silver Lake Dam, the D&H Canal feeder (a lead from `notes/cat_csek.md`, row deleted). Bethel: the Woodstock festival field and 1984 monument. Mamakating: the Masten-Quinn House and the Mamakating Park cottage colony. Neversink: the C. Burton Hotel and the Grahamsville district. Sources: Wikipedia through `wiki_raw.py` (most entries rest on the Register-based articles alone), the Hasbrouck form through NPGallery, and through `page.py` the Sullivan O&W Rail Trail pages, sullivanny.gov, scnyhistory.org, bethelwoodscenter.org/visit, nps.gov, HMdb 310116, courthouses.co, WAMC, the River Reporter (2019), Radio Catskill and Cinema Treasures. Not checked: nothing on the ground; no service times for any church or synagogue (all `view`, `hours='?'`); whether the Munson Diner still serves (2019 article is the newest read); the Center Theatre's state rests on one Cinema Treasures visitor; Silver Lake Dam pin is within about 50 m (the dam could not be picked out on the aerial); the C. Burton Hotel's two coordinates disagree by 2 km (pin is Wikipedia's, `area`, `conf='mixed'`); the Woodbourne Shul and Center Theatre pins fall on the same block 15 m apart. Brick is `?` for nine places no picture was opened for.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Pines Hotel ruins | South Fallsburg, NY | Borscht Belt resort closed 1998, 96 acres, abandoned; large fires damaged several structures (Radio Catskill) | Fire date, owner, and whether anything can be seen from a public road |
| Fallsburg O&W Neversink River crossing | Between the Fallsburg Tunnel and the Neversink, South Fallsburg | Trail page: "last mile" from the tunnel to a pedestrian bridge over the Neversink expected in 2026 | Whether the bridge opened and what railway remains it passes |
| Hillig Castle | Liberty vicinity, NY (Register 100007082, no list coordinate) | Register list name only | Any source, position and owner |
| Time and the Valleys Museum and the Lost Catskill Farm | 332 Main Street, Grahamsville, NY (41.84921, -74.54912) | Museum of the villages taken for the city reservoirs; 1930s farm group opened 2018 (museum's page) | Whether the farm buildings are old or rebuilt; season hours (page says reopening Memorial Day weekend 2027) |
| Broadway Historic District | Monticello, NY (41.6554, -74.6885, Register list) | Nominated 2019 for its early 20th-century blocks (WAMC); listed (100004915) | The form (searching found an Indiana form under a similar NPGallery address); which buildings are worth naming |

## Tips
- Newer New York Register forms (about 2012 on) are on NPGallery under `npgallery.nps.gov/GetAsset/<uuid>`; a web search for the property name finds the address, and `page.py` reads the PDF. Check the form's first lines: one search result for "Sullivan County Courthouse" was Indiana's.
- The National Archives copies of New York forms (`s3.amazonaws.com/NARAprodstorage/lz/electronic-records/rg-079/NPS_NY/<ref>.pdf`) answer 403 from here.
- bethelwoodscenter.org answers 406 to `page.py` except `/visit`, which has the museum hours.
- `geo.py` put "265 Main Street, Hurleyville" in Woodbourne (StreetAddress); `nom.py` had the right address point.
- sullivanoandw.com pages (one per town section) give trailhead addresses and the trail rules, and read in full.
