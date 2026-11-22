# scho_exwh: Chenango County, NY: New Berlin, Sherburne and the hill churches and schoolhouses
state: New York
region: scho
date: 2026-11-22
places: 18
file: data_scho_exwh.py

## What this batch is
Eighteen places in Chenango County, New York, a second pass after `scho_wopf` (region `scho`, drawn at random by `choose.py --state ny`, which offered New Berlin, Owego and Windsor; the Atlas had nothing within 10 km of New Berlin). All standing or traces. New Berlin: St. Andrew's Episcopal Church (Upjohn, 1848; open for Sunday services shared with Norwich and South New Berlin), the Horace O. Moss stone house (1831) and the village historic district with its markers. Sherburne: the historic district, the School Street one-room schoolhouse (a lead from `scho_wopf`), the old high school (1924–35), West Hill Cemetery with Col. William S. Smith's grave, and the Chenango Canal bed on County Route 12B. Hill hamlets: Columbus Community Church (1844), Rockdale Community Church (1860), the Smithville Valley Grange (an 1842 Universalist church), District Schools 2 and 4 at Coventry with the "Coffin Man" gravestone, South Otselic with the Gladding works and the Newton octagon house. Valley villages: Greene (district and the canal slip scoop), Bainbridge (1831 Presbyterian church on the green), Afton's Main Street. Sources: Wikipedia raw text (`wiki_raw.py`, the county Register list and each listing's article), HMdb nearby lists round seven village centres and about 50 marker pages (`page.py`), the Big Red Door Episcopal churches' visit page, the Earlville Opera House page (only to find it was already on the map). NOT checked: anything on the ground; interiors of every building; owners of the schoolhouses, the octagon, the old high school and the Moss house; whether the Columbus, Rockdale, Bainbridge and Smithville buildings hold services or open (all left `view`); the New Berlin depot's survival; who keeps West Hill Cemetery. Five pins mark only an area (Moss house, Columbus church, both Coventry schools, the octagon) because the aerial did not settle which building it is; the canal bed pin is the roadside marker. Most Register articles here are one-paragraph stubs, and every NPGallery form tried was a placeholder.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| N.Y.O.&W. depot, New Berlin (1869) | Genesee Street (Route 80), New Berlin, NY (marker 42.62467, -75.32857) | HMdb 230546: board-and-batten depot, the largest the Oswego Midland built; now mentioned in the New Berlin district entry | A source that it still stands, and its use |
| Beaver Meadow Hotel | County Road 16 at Cole Hill Road, Beaver Meadow (Otselic), NY (HMdb 132756, 42.65978, -75.68023) | Marker: hotel built about 1872, closed 1916 | Whether the building stands; owner |
| Smyrna Opera House history | townofsmyrnany.gov/assets/History-of-the-Smyrna-Opera-House.pdf | The town's own history of the 1907 town hall (already on the map as smyrna-town-hall-opera-house) | The PDF answered 403; an archived copy of January 2026 exists but this session could not open it |
| Sherburne Historic Park | School Street, Sherburne, NY (ArcGIS POI 42.68917, -75.50108, next to the schoolhouse) | A search result names a "Sherburne Historic Park Society and Museum" (chenangohistorical.org, 403) | Whether the schoolhouse belongs to it and when it opens |
| Hoboken mill site, New Berlin | Route 80 at County Route 18 (HMdb 170168, 42.62702, -75.32199) | Marker: 1832 Arkwright cotton mill and the 1899 Borden condensery, "world's largest" | Anything left to see |

## Tips
- HMdb nearby lists (5-mile radius) round New Berlin, Sherburne, Greene, Bainbridge, Earlville, Afton and Smyrna gave about 350 markers in one pass; the cached-page grep in GUIDE.md section 16 lists them.
- `start.py` at 15 km round New Berlin did not show `scho_wopf`'s Earlville, Smyrna, Upperville, Calvary and Bainbridge places (they are 15 to 40 km off); grep `tools/data_*.py` for the county's hamlet names before writing.
- The ArcGIS geocoder found Rockdale Community Church and Bainbridge's First Presbyterian as POIs on the building, but put Columbus Community Church 3 km away; `nom.py` had none of the three.
- Every Chenango County NPGallery form tried (1973 to 2009) was a placeholder; townofsherburne.net posts answered 404 and chenangohistorical.org 403.
