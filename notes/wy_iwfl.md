# wy_iwfl: Carbon County, Wyoming
state: Wyoming
region: wy
date: 2026-11-19
places: 17
file: data_wy_iwfl.py

## What this batch is
Seventeen places in Carbon County (and one just over the line at Devil's Gate), drawn at random: Fort Fred Steele State Historic Site; in Rawlins the Wyoming Frontier Prison, the 1901 Union Pacific depot, the Ferris Mansion and France Memorial church; the Parco Inn at Sinclair; Carbon ghost town and cemetery (ask first: private land, gated county road, appointment through the Hanna Basin Museum); the Hanna Community Hall; at Medicine Bow the depot museum, the Fossil Cabin (moved there in May 2026, behind a fence in October 2026), the Virginian Hotel and the 1929 airway beacon field; the Elk Mountain Hotel; Hotel Wolf in Saratoga; the Grand Encampment Museum with its tramway towers and the Encampment opera house; and the Tom Sun Ranch (Martin's Cove visitors' centre). Sources: Wikipedia raw text (`wiki_raw.py`), NPGallery Register forms (Carbon Cemetery, Parco, Medicine Bow intermediate field, the 1973 Boston-Wyoming smelter and Ferris-Haggarty forms), and through `page.py` Wyoming State Parks, wyomingfrontierprison.org, rawlinswy.gov, the Carbon County Visitors Council pages, the hotels' own sites, WyoHistory.org, WyoFile, HMdb and Cowboy State Daily. Not checked: anything on the ground; hours for the Virginian, Hotel Wolf, the opera house and the Tom Sun Ranch; fees at Fort Fred Steele and the museums; whether the Parco Inn is in use; whether the Ferris Mansion still takes guests (it was put up for sale); which buildings still stand at Fort Fred Steele. Pins: Fort Fred Steele moved off the railroad tracks onto the fort buildings; the airway field is the Register point on the field (`area`), the beacon tower could not be picked out; the Fossil Cabin is `area` on the museum grounds. Brick: depot, Ferris Mansion and Hotel Wolf `yes` from Wikipedia photographs; the prison, the fort, Carbon, Parco, the Encampment pair and the ranch left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Rudefeha and Dillon (Ferris-Haggarty mine camp) | Sierra Madre west of Battle Pass, off WY 70 at the Copperton sign, Forest Road 862, Carbon County, WY | ghosttowns.com and the county visitors' blog say the mine shaft is open, some buildings stand, and Dillon a mile west has many log-cabin foundations; the 1973 Register form (73001928, address restricted) gave the owner as private (Morse Bros) | A coordinate, and who owns it now (Medicine Bow National Forest or private) |
| Boston-Wyoming smelter site | Encampment, WY (Register list 41.209722, -106.779444) | 1973 Register form (73001927): only foundations and traces of walls left; private then | Current owner and whether it can be seen from a public road |
| Old Battle townsite | Battle Pass, WY 70, Carbon County, WY (Wikipedia, about 41.156, -106.982) | Wikipedia: town 1898-1905 on the wagon road to the Ferris-Haggarty mine; the county blog says a few residences remain | What is left to see and who owns it |
| Arlington (Rock Creek stage station) | I-80 and WY 13, Carbon County, WY (41.595, -106.2094) | Wikipedia: Overland Trail stage stop and toll bridge about 1860; Register district 1983 | What stands and whether any of it is public |
| Fort Halleck | near Elk Mountain, WY | Register 70000668, address restricted | Whether the public may visit, and where |
| Pick Bridge and Butler Bridge | North Platte at Saratoga and Encampment, WY (41.5394, -106.8808; 41.2564, -106.6394) | Register list only | What kind of bridge, whether it stands, a source |
| Wyoming Bar, Front Street | Rawlins, WY | Cowboy State Daily (November 1, 2026) headline: the last original Front Street building, 136 years old, is being torn down | Not added: being demolished. Check whether anything is left |

## Tips
- Wyoming State Parks pages (wyoparks.wyo.gov) carry about 9,000 characters of menu before the text: read with `page.py --all -n 30000` and cut at the last "Our Apps"; hours sit after "Hours . ." on the site's "about" page.
- The Carbon County Visitors Council pages (wyomingcarboncounty.com, snowmobileinwyoming.com, same text) give hours, address and coordinates for every museum in the county in one line each; `page.py -g 'Open|Address'` reads them.
- Web search results in this session gave titles only, no quoted text; every page had to be opened.
- The Wikipedia picture for the Wyoming State Penitentiary is an aerial of the new prison outside town, though its caption names the 1901 building; it does not settle brick for the Frontier Prison.
- `start.py` and the federal names, mines and OSM-ruins layers have nothing for Wyoming yet (0 leads within 120 km of Rawlins).
