# troy_vhio: Monument Square, South Troy and Uncle Sam's Troy: museums, firehouses, the 1904 blocks
state: New York
region: troy
date: 2026-11-20
places: 15
file: data_troy_vhio.py

## What this batch is
Fifteen places in the city of Troy (region `troy`, drawn at random by `choose.py --state ny`), south of the Lansingburgh ground that `troy_qbqw` worked. Five give full entries to thin `lm-` landmark pins (`was=`): the Burden Iron Company office (Burden Iron Works Museum), the W. & L. E. Gurley Building, the Troy Savings Bank Music Hall, the Hart-Cluett House and Proctor's Theater. New: the Ilium and McCarthy buildings (1904), the 1936 post office with Waldo Peirce's 1938 murals, the J. C. Osgood (Engine 6) and Esek Bussey (Engine 8) firehouses, Public School No. 10, the Oakwood Avenue Presbyterian Church, and three marked sites: the Liberty Street Presbyterian Church (Henry Highland Garnet's), "Uncle Sam" Wilson's house and brickyard on Ferry Street, and the Old Mount Ida Cemetery. Sources: Wikipedia through `wiki_raw.py` and the Rensselaer County Register list (`--rows`), HMdb marker pages found with the nearby list round Monument Square, the Hudson Mohawk Industrial Gateway's museum and building pages, the Hart Cluett Museum's visit page and the Music Hall's box-office page (hours read November 20, 2026), historypointer.com for Register addresses. Positions from the ArcGIS geocoder (PointAddress) and OpenStreetMap; all fifteen pins were looked at on the leaf-off aerial and sit on their buildings or, for the markers, on the street. Not checked: anything on the ground; the post office's lobby hours (`hours='?'`); whether the Oakwood Avenue church still holds services (`conf='mixed'`); the Esek Bussey Firehouse's present use; owners and opening rules of the Old Mount Ida Cemetery; the insides of every building except the Music Hall, Hart-Cluett House and Burden office. Every Register form tried on NPGallery (00001231, 94001281, 12000959, 73001252) was the one-page placeholder. Red brick: Burden office, Gurley, Esek Bussey and Osgood `yes` (sources and, for Osgood, a 2025 Wikimedia photograph); the Music Hall `no` from Wikipedia's street photograph; Proctor's, Ilium, McCarthy and School No. 10 left `?`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Rice Building | Troy, NY (First Street at River Street) | Central Troy Historic District article: 1871 five-storey flatiron building by Frederick Clarke Withers, now RPI's | A coordinate and a second source |
| Rensselaer County Courthouse | Troy, NY (80 Second Street; HMdb 261939 at 42.72886, -73.69199 is the first courthouse marker in front of it) | Central Troy Historic District article: Classical Revival courthouse by Marcus and Frederick Cummings, the third on the site | Its year and whether visitors may go in |

## Tips
- The thin `lm-` pin for Oakwood Cemetery and Earl Chapel is about 1.1 km from the cemetery's main gate, so a full entry cannot replace it with `was=`; `start.py` could warn when an `lm-` pin lies off the place it names.
- The HMdb nearby list round Monument Square (one request, then grep the cached page for `m.asp?m=`) found the Uncle Sam Trail markers, the Liberty Street church marker and Old Mount Ida Cemetery, none of which are on the Register list.
- The Esek Bussey Firehouse's Register list point is 450 m east of the building; the ArcGIS PointAddress for 302 Tenth Street lands on it, and so does Wikipedia's point.
- `brick.py look` saved nothing for Proctor's Theater (the picture title has an encoded apostrophe, `%27`), with no error message.
