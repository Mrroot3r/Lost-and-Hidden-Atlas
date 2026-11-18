# sd_xdeo: Minnehaha County, South Dakota: Sioux quartzite, the falls and old truss bridges
state: South Dakota
region: sd
date: 2026-11-18
places: 16
file: data_sd_xdeo.py

## What this batch is
The first full batch for South Dakota: 16 places in Minnehaha County (Sioux Falls, Garretson, Dell Rapids, Brandon, Renner), most of them built of Sioux quartzite. The Queen Bee Mill ruins and the 1908 hydro plant in Falls Park; the Old Courthouse and Pettigrew museums; two railroad depots; the old penitentiary (view only, a working prison); four iron and steel truss bridges of 1895 to 1908 (Cherry Rock, Old Yankton, Iverson Crossing, Palisades); the Depression relief works in Split Rock Park and the Dell Rapids bathhouse; the Dell Rapids quartzite main street; two churches. Sources: Wikipedia through `wiki_raw.py`, the Register nomination texts from NPGallery through `page.py --all -n 60000`, HMdb markers, the Siouxland Heritage Museums pages (hours), SD Game, Fish and Parks (Palisades and the entrance licence) and Experience Sioux Falls. Not checked: City of Sioux Falls park hours (siouxfalls.gov answers 403), City of Garretson and Dell Rapids park hours, current use of the two depots, whether the Old Yankton Bridge is open to walkers, who owns the closed Iverson Crossing bridge, and every interior except the two museums. Nothing was seen on the ground. Pins moved on the aerial: Queen Bee Mill (onto the walled foundation), Old Yankton and Iverson Crossing bridges (onto the trusses), Renner church. The penitentiary and Dell Rapids main street are area pins; the depots' pins are not confirmed on the right roof.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Shafer Round Barn | Sioux Falls east edge, SD (43.54194, -96.64944) | 1920 hollow clay tile round dairy barn with 1919 tile silo, Register form 95001470 | No round building seen on the aerial at the Register point or within 400 m; may be gone. Needs a current source or photo before adding |
| Palisades mill and town site | Palisades State Park, Garretson, SD (43.68764, -96.51717) | SD GFP page: a large flour mill with a water wheel stood on the bluff and a town of Palisades grew round it | Dates, what (if anything) is left, and where |
| Terrace Park terraces and Japanese Gardens | Sioux Falls, SD (43.5542, -96.7417) | Quartzite-lined terraces and stairs, Register 15000566 (Wikipedia) | Build dates and park hours from the city (siouxfalls.gov 403) |
| Orpheum Theater | Sioux Falls, SD (43.55056, -96.72728) | Built 1913, still a stage theatre (Wikipedia) | Interior fabric and tour or show access |
| Dell Rapids Amphitheater and Warming House | Dell Rapids, SD (43.820833, -96.703056) | Register 02000020 and 100000691, relief-era park works | Nomination texts not read |

## Tips
- `page.py --all` stops at 12,000 characters; a Register form's description is usually further in. Add `-n 60000` and search the saved text yourself.
- The City of Sioux Falls (`siouxfalls.gov`) answers HTTP 403 to `page.py` with no archived copy; Experience Sioux Falls (`experiencesiouxfalls.com/fallspark`) read cleanly for Falls Park history.
- `cityofgarretson.com` shows only a browser "Client Challenge" page to `page.py`.
- The Siouxland Heritage Museums pages (`siouxlandmuseums.com/?p=111` and `?p=130`) give hours, parking and fees in full.
- South Dakota has no leads layers yet, so `start.py` prints nothing to work from; the Register list rows were the whole starting list.
