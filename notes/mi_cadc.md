# mi_cadc: Michigan: Marquette, Negaunee and Ishpeming
state: Michigan
region: mi
date: 2026-11-20
places: 22
file: data_mi_cadc.py

## What this batch is
The first full batch for Michigan: 22 places in Marquette County on the Marquette Iron Range and the Lake Superior shore. Iron: the Carp River Forge (1848) below the Michigan Iron Industry Museum, the Jackson Mine pits in Negaunee's West Old Town, the Cliffs Shaft Mine Museum, the Cleveland Mine engine house, the 1931 Lower Harbor Ore Dock, the Republic open-pit overlook, and Gwinn, the Cliffs company model town. Marquette's standing buildings: St. Peter Cathedral, the courthouse, the old city hall, the Harlow Block, Holy Family Orphanage, the Upper Peninsula Brewing office and the 1889 branch prison. Also the Ishpeming city hall, the Mather Inn, the Negaunee freight depot and the Vista Theater, three lighthouses (Marquette Harbor, Presque Isle breakwater, Big Bay Point) and the 1914 Trunk Line Bridge No. 1 in Van Riper State Park. Sources were Wikipedia (`wiki_raw.py`) and its Register list for the county, HMdb marker pages (three nearby lists), and the managing bodies' own pages read with `page.py`: the Michigan History Center and DNR pages for the Iron Industry Museum and Van Riper, the Marquette Maritime Museum, St. Peter Cathedral, Big Bay Point Lighthouse, and the City of Ishpeming. Not checked: anything on the ground; the Cliffs Shaft hours, which are the 2024 season's as the city announced them; the Mather's lounge hours; courthouse and Ishpeming city hall office hours; whether the Presque Isle breakwater may be walked; the owner of the Lower Harbor Ore Dock and of the Republic overlook; and what of the Carp River Forge can be seen today. Pins that mark only a general area: Jackson Mine (the workings spread widely; the LiDAR shows the pits just south-west of the pin), the Negaunee freight depot (could not be picked out on the aerial) and Gwinn (the marker park). The Cleveland Mine engine house and the old Marquette city hall pins are on the right block but the building could not be told apart. Marquette Harbor Light was left brick='?' (the picture shows a red building, but whether that is red brick or red paint could not be told); Big Bay Point Light, Ishpeming city hall and the Mather Inn were set to red brick from the Wikipedia pictures.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Carp River Furnace | Marquette, MI (46.51892, -87.38445, HMdb marker 278588) | Blast furnace at the mouth of the Carp River built by John Burt in 1874, burned 1882, ran again to 1907, dismantled 1916; its last beehive charcoal kiln collapsed in 2016 (HMdb) | What, if anything, is left to see beside the marker, and who owns the ground |
| Old Kloman Bridge | Republic, MI (46.40613, -87.98160, HMdb 154300) | A Republic landmark named for Andrew Kloman, seen from Munson Park over the Michigamme River (HMdb) | Its date and what the old bridge is now; the marker text says neither |
| Granot Loma | Marquette County, MI (46.699444, -87.548333, Register list) | Louis G. Kaufman's great log lodge on Lake Superior, Register-listed | Private: whether anything can be seen from a public way |
| Sam Cohodas Lodge | Champion, MI (46.525833, -88.004167, Register list) | 1934–35 log lodge on Lake Michigamme, later a bed and breakfast (Wikipedia) | Current use and owner; whether it can be seen from US 41 or Van Riper State Park |
| Bishop Baraga House | Marquette, MI (615 South 4th Street; HMdb 206057) | Baraga died here in 1868; part of the house was moved from behind the cathedral (state marker) | Whether it is open (the Baraga association's page was not read) |
| Forestville Fireplace | Marquette County, MI (46.61566, -87.5103, OpenStreetMap lead) | A mapped ruin | Any source |
| Huron Islands Light and Granite Island Light | Lake Superior off Big Bay and Marquette (Register list) | Register-listed island lights; Granite Island is private | Boat access and owners |

## Tips
- Michigan: the City of Negaunee's site (`cityofnegaunee.com`) answers HTTP 403 to `page.py`, and its archived copies could not be fetched.
- Michigan: michigan.gov museum and DNR pages read well with `page.py --all`; the Iron Industry Museum's front page carries reopening notices that the visitor-information page does not (it was shut by roof damage from February to June 2, 2026).
- Michigan: `stpetercathedral.org` sub-pages are reported as DRAWN BY SCRIPT but the short text `page.py` gets back does hold the hours, Mass times and parking.
- `geo.py` works outside New York: for Marquette County it gave PointAddress hits on the courthouse and orphanage, but put St. Peter Cathedral and the old city hall in the street, and "420 Rail Street, Negaunee" 600 m from the Register point.
- `publish.sh` stopped once because two other batches merged while this one was being written; `resync.sh` then the rebuild took a few minutes and nothing was lost.
