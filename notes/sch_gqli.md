# sch_gqli: Schenectady County: Duanesburg, Niskayuna and the canal locks
state: New York
region: sch
date: 2026-11-18
places: 12
file: data_sch_gqli.py

## What this batch is
Twelve places in Schenectady County, mostly outside the city, drawn at random by `choose.py` (region `sch`; the city itself already had 15). Duanesburg: Christ Episcopal Church (1793, box pews), the Quaker Street Friends Meeting House (1807–1813), the Christman Sanctuary farm (TNC), the Herrick farm cellar hole in the Town of Duanesburg Forest, and the Mariaville hamlet. Niskayuna: the 1843 railroad station at Lions Park, the 1852 Reformed Church and Barge Canal Lock E7 with the Vischer Ferry Dam. Rotterdam: Lock E8 and its movable dam. Scotia: the 1730s Abraham Glen House (the library). Schenectady: the Hotel Van Curler (Elston Hall) and the GE Realty Plot. Sources: Wikipedia through `wiki_raw.py`; HMdb marker pages (most of the facts and the marker positions), The Nature Conservancy, Schenectady County, Town of Niskayuna, NYS Canals, Schenectady County Public Library and the Christ Church parish site through `page.py`; a 2016 blog write-up of a Sacred Sites open day for the inside of Christ Church. The Register forms for Christ Church, the Christman Sanctuary, Quaker Street and the Niskayuna station came back as scans with no text layer and were not read. Not checked: anything on the ground; when the Quaker meeting house, the Niskayuna church and Elston Hall can be entered; the hours of Lock 7 Park, Lions Park and the Duanesburg Town Forest; which Christman farm buildings stand on preserve land; parking at Christ Church, Quaker Street and Mariaville; the colour of the brick everywhere except the Niskayuna station (the sources say "brick" for the Niskayuna church and Elston Hall, so `brick='?'`). Pins that mark only an area: the Christman Sanctuary (the Register's district point, in woods), the Herrick farm (the trail sign's HMdb position; the cellar hole was not seen on the aerial), Mariaville (road junction), the GE Realty Plot (a street in the middle of the district) and Lock E8 (the lot beside the lock). Three pins were moved on the leaf-off aerial with `pix.py` (Niskayuna Reformed Church, Abraham Glen House, Mariaville) and one off a yard (the GE Plot). The Niskayuna station's last year of railroad use differs between sources (Wikipedia 1964, the 2025 county marker passengers 1933 and freight 1984); both are given and the entry is `mixed`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Jenkins Octagon House | Duanesburg, NY, on NY 395 north of Delanson (Register point 42.758611, -74.185278) | Wikipedia: octagon farmhouse of about 1855 by "Boss" Jones, stacked-plank walls; private | The Register point is in woods 250 m west of NY 395 on the aerial, and the house could not be picked out among those on the road; an address would settle the pin |
| Shute Octagon House | Duanesburg, NY, McGuire School Road (Register point 42.774444, -74.219444) | Wikipedia: the other Boss Jones octagon of about 1855, with widow's walk and porte cochere of 1906; private | Pin not checked on the aerial; a second source |
| Indian Kill Preserve dam | Glenville, NY (Schenectady County preserve, open dawn to dusk) | nnywaterfalls.com: a small dam a little over 100 yards from the trailhead, and two falls | Any source for the dam's age or what it served; its position |
| North Mansion and Duane Mansion | Duanesburg, NY (42.75361, -74.11444 and 42.75444, -74.12806) | Wikipedia: General William North's Georgian house of about 1795 with a 1780s tenant house; James Duane's family's Federal mansion of 1812–1816 with carriage barns | Both private; whether either can be seen from a public road was not checked |
| Swart House and Tavern | Glenville, NY (42.88611, -74.05056) | Wikipedia: rear wing about 1750, enlarged about 1792, stone smokehouse; private | A second source and whether it is visible from the road |

## Tips
- The NPGallery `GetAsset/NRHP/<ref>_text` address returned a one-page scan with no text layer for all four Schenectady County forms tried (87000911, 70000433, 84003270, 07001205); do not spend more tries there for this county.
- Searching "Christ Church ... inside the church" returns `historicchristchurch.org`, which is Christ Church in Alexandria, Virginia, not Duanesburg; the Duanesburg parish is `christchurchduanesburg.org`.
- `duanesburg.gov` (the town historian's pages) answered 403 to `page.py` with no archived copy.
- Schenectady County put up a new series of HMdb-listed markers along the Empire State Trail in 2024–2025 (Lock 7, Lock 8, the Niskayuna station, the Kiwanis Park aqueduct); each gives a construction history and an exact position. The Kiwanis Park aqueduct marker (HMdb 272279) describes the Plotter Kill aqueduct already on the map.
- An HMdb nearby list caches in `research/pages/`; `grep -o "m\.asp?m=[0-9]*'>[^<]*<"` on it lists every marker number with its title in one go.
