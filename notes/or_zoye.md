# or_zoye: Oregon, a first scatter
state: Oregon
region: or
date: 2026-11-22
places: 14
file: data_or_zoye.py

## What this batch is
A first scatter of 14 places across Oregon, the state with the fewest places when the session began (23, nearly all from the Baker County batch `or_xqmn`), claimed with `choose.py --thinnest`. One or two places in each of eleven counties, every one standing: Pete French Round Barn and Frenchglen Hotel (Harney), Kam Wah Chung (Grant), Shaniko and the Columbia Southern Hotel and the Fort Dalles surgeon's quarters (Wasco), Thompson's Mills (Linn), Golden and Wolf Creek Inn (Josephine), the Beekman Bank (Jackson), Hot Lake Hotel (Union), the Pelota Fronton at Jordan Valley (Malheur), Heceta Head Lighthouse (Lane), Vista House (Multnomah) and McLoughlin House (Clackamas). Facts from Wikipedia (`wiki_raw.py`), Oregon State Parks park pages (`page.py`), the NPS, the Fort Dalles Museum, Historic Jacksonville, Inc., the Oregon Encyclopedia and one La Grande Observer article (2020). Not checked: anything on the ground; Hot Lake Hotel's present state (its own web address now belongs to an unrelated business, so whether it takes guests is unknown); the Columbia Southern Hotel's hours (no page of its own was read); who owns the Pelota Fronton; where to park at Golden and Kam Wah Chung; the interiors of most buildings. Sources disagree, and both are given, on the Frenchglen Hotel's date (about 1917 or 1924), Kam Wah Chung's (about 1865 or 1866) and the Round Barn's (1883–84, or late 1870s to early 1880s, and when it passed to the state). All pins looked at on the aerial; Thompson's Mills (45 m) and Hot Lake Hotel (120 m, onto the OpenStreetMap building of that name) were moved.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Stevens batteries (Battery Russell and others) | Hammond, OR (Fort Stevens State Park, 46.18422, -123.95682 park point) | Fort built 1863–64, shelled by a Japanese submarine in June 1942, decommissioned 1947 (Wikipedia); Oregon State Parks page says underground battery tours run in summer through the Friends of Old Fort Stevens | A source describing Battery Russell itself and a pin on it; visitfortstevens.org would not connect |
| Fort Rock Valley Historical Homestead Museum | Fort Rock, OR (43.356, -121.054 for the town) | Wikipedia links the museum's photos of homestead buildings | The museum's site (fortrockmuseum.com) would not connect; its archived copy needs the web fetch tool |

## Tips
- Oregon State Parks publishes every park's name, point and status note as JSON at `https://stateparks.oregon.gov/services/park.cfc?method=getAll` (one plain request); park pages are `https://stateparks.oregon.gov/index.cfm?do=park.profile&parkId=<id>` and read well with `page.py`. The status note sometimes holds the only hours (Heceta Head lighthouse).
- Oregon State Parks' park points and Wikipedia's differ by up to 1.3 km (Pete French Round Barn); look at both on the aerial.
- hotlakesprings.com no longer belongs to the Hot Lake resort.
- `photo_find.py` named this session's pics file after the workspace's letters (`pics_gfch.py`), not the batch key, as an earlier note also said.
