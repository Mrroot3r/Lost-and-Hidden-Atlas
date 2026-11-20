# or_xqmn: Baker County, Oregon
state: Oregon
region: or
date: 2026-11-20
places: 21
file: data_or_xqmn.py

## What this batch is
A first pass over Baker County, Oregon (drawn at random, region `or`), with three places just over the line in Grant County: 21 places. Gold-rush ground: the Sumpter Valley dredge and narrow-gauge railroad, the Superintendent's House and the 1917-fire bank vault in Sumpter, the ghost towns of Cornucopia (jailhouse), Whitney, Bourne and Granite, the Ah Hee Diggings, the Fremont Powerhouse, the Oregon Trail ruts at Flagstaff Hill, the Chinese cemetery, and Baker City's tuff-stone public buildings (courthouse, city hall, Carnegie library, cathedral, old St. Elizabeth Hospital), the Geiser Grand Hotel and the Natatorium; also the CCC-built Antlers Guard Station and Unity Ranger Station. Sources: National Register forms read as text from NPGallery, HMdb marker texts (an HMdb nearby list round Sumpter, Baker City, Auburn and Cornucopia gave most positions), the pages of Oregon State Parks, the BLM, the Forest Service, the Sumpter Valley Railroad, the cathedral parish and Crossroads, SAH Archipedia, the Oregon Encyclopedia, Baker City Herald and La Grande Observer articles, recreation.gov, historicsumpter.com, and Wikipedia with `wiki_raw.py`. Pins checked on Esri satellite and the LiDAR sheet (1 m LiDAR covered all but one tile); the dredge, Carnegie, city hall, St. Elizabeth and Unity pins were moved. NOT checked: nothing was seen on the ground; the hours of the Geiser Grand (its site is drawn by script), the Baker Heritage Museum (only a 2022 newspaper's hours) and the courthouse (county site would not connect); what stands in Granite rests on one local site (historicsumpter.com); who owns the Bank of Sumpter vault lot and the Bourne cabins; parking at the Ah Hee panels; which wing of the St. Elizabeth block is the 1915 hospital. Whitney, Bourne and Granite are `area` pins on the town.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Alder Creek stone houses ("Rock House") | Near I-84 about 12 miles south-east of Baker City, north of Dogtown Creek by Alder Creek, Baker County, OR (about 44.67, -117.62) | A cluster of two-story tuff-stone buildings of about 1905, private (GS Cattle Ranch), seen from I-84; Baker County Library District page | The buildings could not be picked out on a 1,500 m aerial; needs a closer look along I-84 and a view-only access note |
| Auburn townsite | Baker County, OR (44.69932, -117.94522) | First county seat, 1862; the Oregon Encyclopedia and a Baker City Herald article say nothing remains and most of the site is private north of Old Auburn Road | Only worth adding if a marker or the Auburn cemetery on public land can be sourced |
| Eastern Oregon Museum | 610 Third St, Haines, OR | Museum in the 1931 school gymnasium, opened 1959; La Grande Observer, May 2024 | Its own page and hours; whether the building itself is worth the trip |
| Churchill School | 3451 Broadway, Baker City, OR (44.77775, -117.84927) | 1926 Georgian Revival brick school by Charles B. Miller, vacant in the 2008 Register form | What it is used for now |
| Tipton Station | Highway 7 near Forest Road 2620, Baker County, OR (44.65299, -118.41281) | Sumpter Valley Railway summit depot and town site, Forest Service sign (HMdb 284119) | Whether anything is left to see |
| Red Boy Mine | Near Granite, Grant County, OR (44.79472, -118.47803) | 1880s–1900s gold mine whose owners built the Fremont Powerhouse (HMdb 106767) | What is left, and whether it is private patented ground |

## Tips
- Oregon: `geisergrand.com` and `bakercountyor.gov` cannot be read from a cloud session (drawn by script; connection refused). `sos.oregon.gov/archives/exhibits/ghost/...` pages answer 404 and their archived copies could not be fetched.
- One HMdb nearby list round each of four points (Sumpter, Baker City, Auburn, Cornucopia, 10 miles) gave positions for almost every place in eastern Baker County; the grep in GUIDE.md section 16 pulls them out of `research/pages/`.
- The ArcGIS geocoder's PointAddress for 1655 1st Street, Baker City landed 15 m off city hall, and a StreetAddress for the Carnegie library landed in the street; `osmnear.py ... buildings` gave both buildings by name or address.
- Wikipedia's coordinate for the Unity Ranger Station falls in an empty field 150 m south of the buildings; the Register list coordinate is on them.
