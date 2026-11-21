# albco_zlrn: Northern Greene County: Oak Hill, Durham, Greenville and the Cunningham stone bridges
state: New York
region: albco
date: 2026-11-21
places: 17
file: data_albco_zlrn.py

## What this batch is
Seventeen places in northern Greene County, just south of the Albany County line (region `albco`, drawn at random by `choose.py --state ny`, which offered Greenville and Oak Hill; the Atlas had nothing in either). All standing. Oak Hill: the hamlet as a whole (2017 Register district), the brick Tripp house and stores, the 1859 Methodist church, St. Paul's Lutheran (first built for Episcopalians) and the cemetery. Greenville: Christ Church (1857, red sandstone, original glass and pews; diocese says Upjohn, the Register form says Henry C. Dudley, both given), the Presbyterian church with the old academy (now the library), and the Prevost manor house at Norton Hill. Durham: the Cornwallville cemetery, the Durham Center Museum in the 1837 schoolhouse (with the High Rock railroad-wreck marker), and six of Jeremiah Cunningham's dry-laid stone arch bridges of 1886–1893. Coxsackie: a full entry for the Bronck House and 13-sided barn, replacing the thin pin `lm-bronck-house` (`was=`). Sources: Wikipedia raw text (`wiki_raw.py`); Register forms read through NPGallery's text layer for Christ Church, the Oak Hill district and the Cornwallville cemetery; HMdb markers; the Episcopal Diocese of Albany's parish page; the Greene County Historical Society's tour page; Upstater; the Greene County Historical Journal vol. 7 no. 4. Not checked: anything on the ground; the Durham Center Museum's hours (it has no website); service times for the Presbyterian, Lutheran and Methodist churches (no own page found) and the Methodist church's present use; who keeps the two cemeteries. Pins: the Prevost manor pin is the state marker on Route 81, not the house (the Register point is in woods; a Commons photo of the house was taken about 270 m from it); the Woodward Road and Allan Teator Road bridges are Register points where the LiDAR shows a road over a ravine, the arches themselves are under trees; the Shady Glen bridge pin is an unnamed road crossing 38 m from the Register point. Brick was settled from Commons photographs for the Bronck House and the Tripp house (red brick beside stone and frame: `some`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Peter Houghtaling Farm and Lime Kiln | West Coxsackie, NY (Register list 42.393333, -73.855; 523 Lime Kiln Road) | Wikipedia: 1794 stone house, farm buildings, burial ground, and a mortared limestone lime kiln of 1850–1880; real-estate listings show it for sale as a private estate | Whether the kiln can be seen from Lime Kiln Road; the Register form is only a placeholder on NPGallery |
| Stone bridge of 1800 on the Susquehanna Turnpike | East Durham, NY (HMdb 131398, 42.38269, -74.11803) | One-line 1963 marker by the Durham Center Museum: built 1800 as part of the turnpike | No stream or road crossing is mapped at the marker; any second source and the bridge's position |
| Stevens Hill Farm | Greenville, NY (4082 Grapeville Road) | 2018 Register form (text read): story-and-a-half house reworked in Greek Revival, Reed then Stevens family, 18 acres | Private; whether it is worth a place beside the Greenville churches |
| Dunix | Cornwallville, NY (Register list 42.3456, -74.1424) | Register list: 1855 stone house, later the summer retreat of John Matthews, the soda-fountain maker | Any source beyond the list row; owner |
| Weldon House | East Durham, NY (42.365278, -74.081389) | Wikipedia: 1923 Irish-resort hotel with 60 rooms and a verandah on three sides | Whether it still operates as a hotel |

## Tips
- `start.py "Greenville, New York"` geocoded to Greenville in Orange County, not the one `choose.py` named; give the latitude and longitude `choose.py` prints instead.
- greenvillechurch.org, the first search result for the Greenville Presbyterian Church, is Greenville Community Church in Westchester County.
- The Greene County Historical Society's tour page (`gchistory.org/schedule-tour`) gives the Bronck Museum's days, times and fees; the county tourism page carries older tour times.
- NPGallery gave full text for the 2015–2018 Greene County forms (Christ Church, Oak Hill district, Cornwallville cemetery, Stevens Hill Farm) and placeholders for the 1986 and 2007–2008 ones (Houghtaling farm, the stone arch bridges).
- The Register coordinates for the Cunningham bridges are given to four decimals in some rows; OpenStreetMap's `bridge=yes` road segments put three of them within 10 m.
