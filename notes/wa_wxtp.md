# wa_wxtp: Washington: a first scatter
state: Washington
region: wa
date: 2026-11-21
places: 20
file: data_wa_wxtp.py

## What this batch is
Twenty places spread across Washington, claimed with `choose.py --thinnest` because the state had the fewest places (18, nearly all in Port Townsend and Olympia). West: Gas Works Park (Seattle), Union Station (Tacoma), the Wilkeson coke ovens, Fort Vancouver, Fort Columbia, Fort Casey with Admiralty Head Light, Northern State Hospital, the Monte Cristo townsite. Centre: Roslyn's historic district and its 26 cemeteries, Liberty, Fort Simcoe, the Maryhill Stonehenge, the Douglas County Courthouse at Waterville. East: Whitman Mission, the Dayton depot, the Garfield County Courthouse at Pomeroy, Fort Spokane, the Barron flour mill at Oakesdale, Old Molson. Sources read: Wikipedia with `wiki_raw.py` (and `--rows` on the Columbia, Whitman and Kittitas Register lists), the Barron mill's Register form (NPGallery, text layer), Washington State Parks park pages, NPS pages (Fort Vancouver hours, Whitman Mission hours, Fort Spokane history and its March 2026 repair notice), Seattle Parks, the Forest Service Monte Cristo trail page, Molson Museums, the Dayton Chamber of Commerce, the Port of Skagit and the Port of Whitman County, the Mountains to Sound Greenway, the Spokesman-Review, the Courier-Herald (2008, 2010) and OPB. Pins: looked at on the aerial and LiDAR; Gas Works, Wilkeson (oven row seen on LiDAR), Fort Casey (batteries), Fort Columbia (fort buildings by the lot), Maryhill and the Barron mill were moved with `pix.py`. Not checked: anything on the ground; Union Station rotunda entry; Whitman Mission visitor centre hours; Fort Spokane museum reopening after the 2026 repairs; the coke ovens' present state (newest source 2010); Roslyn cemeteries' rules; county courthouse office hours; whether the Barron mill machinery is still inside and who holds the deed now; the Maryhill hours come from a 2024 newspaper, not the museum's own page. Pins that mark a general area, not the thing: Monte Cristo (Wikipedia townsite point, `area`) and Fort Spokane (OpenStreetMap place point on the parade ground, `area`). The Barron mill pin is on the building taken to be the mill (`site`); the Roslyn pin is the corner the company store stands on. Two date conflicts are given both ways (coke ovens 1885 or 1890; Fort Spokane school years and guardhouse date). Brick: Union Station from Wikipedia (red brick, Flemish bond); Liberty, the Dayton depot, the Barron mill and Northern State set `no` from Commons photographs (wood, stucco); the courthouses and several forts left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Columbia County Courthouse | Dayton, WA (near the depot) | A Commons caption calls it the oldest working courthouse in the state | A source read in a session; Wikipedia article and access |
| Admiralty Head Light as its own entry | Fort Casey State Park, WA | 1903 lighthouse, climbable on set days (State Parks page) | Folded into the Fort Casey entry; a separate entry would need its own history source |
| Molson Schoolhouse Museum | Molson, WA | Open 10 to 5 daily, Memorial Day to Labor Day (Molson Museums) | Folded into Old Molson; a pin on the school itself |
| Fort Simcoe interior hours | White Swan, WA | Wikipedia: interpretive centre and houses April to September, Wednesday to Sunday; park page: book a tour by phone | Which is current |

## Tips
- `pincheck.py --batch <key> --lidar` took over two minutes for 20 places plus 10 trailheads and was killed by the shell's 2-minute limit; run it with nohup in the background and wait.
- Washington State Parks pages read well with `page.py --all` (hours, Discover Pass, interior hours); the old `/find-parks/state-parks/fort-columbia-historical-state-park` address answers 404 but `parks.wa.gov/506/Fort-Columbia` works.
- `page.py --all` prints one very long line: piping it through `tr -s ' .'` and `grep -o 'Hours.\{0,200\}'` pulls the hours out cheaply.
- The Wikipedia coordinates for Fort Casey and Fort Columbia both fell in forest; the forts are a little way off.
