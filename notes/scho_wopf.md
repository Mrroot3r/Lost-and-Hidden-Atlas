# scho_wopf: Chenango County, NY: Norwich, Oxford, the Chenango Canal and the hill hamlets
state: New York
region: scho
date: 2026-11-19
places: 22
file: data_scho_wopf.py

## What this batch is
Twenty-two places in Chenango County, New York, drawn at random by `choose.py --state ny` (region `scho`, which offered Norwich, Morris and Oxford); the Atlas had nothing within 30 km of Norwich. Chenango Canal (1837–1878): Lock 99 (Chenango Land Trust, ask first), the Fly Creek aqueduct arch north of Norwich, and the Oxford turning basin. Standing: in Norwich the 1837 courthouse, Isaac Perry's Emmanuel Episcopal (limestone) and Broad Street Methodist (brick) churches, the Norwich Pharmacal (Unguentine) warehouse with its ghost sign, the DL&W gateman's tower and depot, and the county historical society's museum in Ward School No. 2; elsewhere the Earlville Opera House, the Rockwells Mills stone mill (Old Mill Restaurant), the Theodore Burr House (Oxford library), the Rexford Falls bowstring footbridge, the Young and Bates round barns, the Strong Leather mill in Bainbridge, the Guilford Center church (1817), the White Store union meetinghouse (1820), the Upperville meeting house, Smyrna's town hall and opera house, Calvary Episcopal in McDonough, and the Genegantslet "stone ruin" (marker only). Sources: Wikipedia raw text and the county Register list (`wiki_raw.py`), HMdb nearby lists round seven towns and the marker pages, chenangocounty.org (museum hours, canal), the Oxford library and village pages, the Earlville Opera House page, the Town of Guilford's Rockwells Mills page, the Chenango Land Trust home page, The Evening Sun, the Norwich Pharmacal Register form (text layer on NPGallery) and Uncovering New York for Rexford Falls parking. Not checked: nothing on the ground; interiors of every church; owners of the Fly Creek arch, the White Store church, Upperville and the Genegantslet ruin; restaurant and court hours. Pins that mark only a marker or a road, not the thing: Lock 99 (marker in woods; LiDAR shows a walled hollow that may be the lock), Fly Creek arch (marker on Route 12), Oxford turning basin (marker on the street), Genegantslet ruin (marker on County Route 2), Calvary Episcopal (moved onto North Street) and the Strong Leather mill (street corner). The Genegantslet "first refrigeration plant" claim rests on one marker. Red brick left '?' wherever no source said; Wikimedia refused pictures twice, so no `brick.py look` was done.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Newton Homestead (octagon house, c. 1860) | Ridge Road, South Otselic, NY (Register point 42.65111, -75.78556 is in woods) | Wikipedia: concrete and stucco octagon by Leroy and Courtland Newton, once the Gladding fishing museum, now private | The house on the aerial: the Register point is off it and no geocoder found it |
| Chenango Canal Prism, Towpath and Lock 106 (Walker's Lock) | Stillwater Road (County Route 32), Chenango Forks, NY | Register 100005922 (historypointer.com); the NPGallery text is a placeholder | A position, the county it lies in, and the owner |
| Chenango Canal stone arch near Greene | Route 12 east of Williams Road, Greene, NY (marker 42.37722, -75.65422) | HMdb 94138: original stone arch carrying the canal over a creek about 150 yards east of the marker | Whether it can be seen from the road; owner |
| Chenango Canal lock and feeder pond south of Norwich | Route 12, Norwich (town), NY (marker 42.46156, -75.56537) | HMdb 92595: remains of a lock and feeder pond east of the road | The lock on the aerial or LiDAR; owner |
| N.Y.O.&W. depot, New Berlin (1869) | Genesee Street (Route 80), New Berlin, NY (marker 42.62467, -75.32857) | HMdb 230546: board-and-batten depot, the largest the Oswego Midland built | A source that it still stands, and its use |
| One-room schoolhouse, Sherburne | School Street, Sherburne, NY (marker 42.68889, -75.50041) | HMdb 93162: District 12 and 14 school, 1890–1947, given in memory of the Kehoes in 1991 | Owner and whether it can be visited |
| Columbus Community Church (1844) and Smithville Valley Grange (1842) | Columbus (42.68361, -75.37333) and Smithville Flats (42.39917, -75.80917), NY | Wikipedia articles read | Pin check, access; left out for time |

## Tips
- chenangohistorical.org (the county historical society, including every `/town/<name>/` page) answers HTTP 403 to `page.py`; chenangocounty.org/historic-museums.php has the museum hours for the whole county in plain text.
- The Chenango Land Trust's home page says the land it owns outright is not open to the public: its canal locks are ask-first.
- HMdb nearby lists with a 5-mile radius round seven Chenango towns gave about 40 Chenango Canal and town markers with positions; the federal names file's "Ward School Number 2" in Norwich is the standing county museum.
- Web search results in this session gave titles and links only, no quoted text.
