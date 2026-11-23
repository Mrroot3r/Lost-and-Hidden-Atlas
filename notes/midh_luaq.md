# midh_luaq: Sleepy Hollow, Tarrytown and the river towns to Yonkers
state: New York
region: midh
date: 2026-11-23
places: 22
file: data_midh_luaq.py

## What this batch is
Twenty-two places in the lower Hudson river towns of Westchester County (Sleepy Hollow, Tarrytown, Pocantico Hills, Irvington, Dobbs Ferry, Hastings-on-Hudson, Elmsford and Yonkers), the first pass there (region `midh`, drawn at random by `choose.py --claim --state ny`, which offered Sleepy Hollow, Mohonk Lake and Tarrytown; `start.py` found no Atlas place within 9 km of Tarrytown). Ruins: the terraced foundation of William Rockefeller's Rockwood Hall (Rockefeller State Park Preserve) and, within a restored garden, Untermyer's gatehouse Ruin Garden. Standing: the Old Dutch Church of Sleepy Hollow (1685–1697) and its burying ground, Philipsburg Manor's mill and manor house, Sleepy Hollow Cemetery, Tarrytown Light, Patriots Park, Philipse Manor station house, Christ Episcopal, First Baptist and Foster Memorial AME Zion churches and the Music Hall in Tarrytown, Lyndhurst, Sunnyside, the Washington Irving Memorial, the Union Church of Pocantico Hills (Matisse and Chagall windows), the Lord & Burnham works in Irvington, the Old Croton Aqueduct Keeper's House in Dobbs Ferry, the Draper observatory and Cropsey's Ever Rest in Hastings, the 1793 Elmsford Reformed Church, Philipse Manor Hall in Yonkers and Untermyer Gardens. Sources: Wikipedia through `wiki_raw.py` (and `--rows` for both Westchester Register lists), and through `page.py` Historic Hudson Valley, Lyndhurst, New York State Parks, Westchester County Parks, the Village of Sleepy Hollow, the Reformed Church of the Tarrytowns, First Baptist Tarrytown, the Friends of the Old Croton Aqueduct, the Hastings Historical Society, the Newington-Cropsey Foundation and the Untermyer Gardens Conservancy. Not checked: nothing on the ground. Pages that would not open (403 or reset): Sleepy Hollow Cemetery, Christ Church San Marcos, the Tarrytown Music Hall; their hours are `?`. Service times for Foster Memorial AME Zion and Elmsford Reformed, and the Irvington library's hours, were not found. Rockwood Hall has no parking point: the lot OpenStreetMap gives nearby is a large office campus, and the state parks page gives no Rockwood Hall parking directions. The Foster Memorial pin is `area` (Wikipedia's point lands on a parking lot; Commons' photo of the church was taken about 150 m away). The Keeper's House pin is an address lookup on Walnut Street. Red brick was left `?` wherever no source or picture settled the colour.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kykuit | Pocantico Hills, NY (estate north of Sleepy Hollow) | Historic Hudson Valley: tours on hiatus for 2026, to be run by the Rockefeller Brothers Fund from 2027 | Whether and how the public can visit in 2027 (rbf.org/pocantico/historic-site-tours) |
| Hammond House | Eastview, Town of Mount Pleasant, NY (41.07611, -73.81167) | Wikipedia: 1720s tenant house of Philipsburg Manor, once the county historical society's museum, sold to New York Medical College and now privately owned | Present owner and whether it can be seen or visited |
| Armour–Stiner Octagon House | Irvington, NY (41.030833, -73.871111) | Register list: possibly the only domed octagon house in the world | Wikipedia article came back empty through `wiki_raw.py`; any source read, and whether it is private (view only) |
| Villa Lewaro | Irvington, NY (41.0333, -73.8656) | Register list: home of Madame C. J. Walker | A source read; private, view only? |
| Church of St. Barnabas | Irvington, NY (41.039722, -73.865833) | Register list: 1853 stone Gothic Revival church | Article read; service times |
| Gould Greenhouse (mapped ruin) | Tarrytown, NY (41.05578, -73.86479) | An OpenStreetMap ruin lead on the Lyndhurst grounds; Wikipedia says the 1881 conservatory is under phased restoration | What the mapped ruin is; written into the Lyndhurst entry for now |

## Tips
- Historic Hudson Valley's old address `hudsonvalley.org/historic-sites/sunnyside/` now serves a photograph; the page is `/historic-sites/washington-irvings-sunnyside/`. Its pages read well with `page.py --all` (the hours sit in one long line: search it for "Friday-Sunday").
- The Old Dutch Church's coordinate in the northern Westchester Register list is wrong (it falls in Irvington); use Wikipedia's.
- `tools/geo.py` needs an output file as a second argument and found nothing for "15 Walnut Street, Dobbs Ferry"; the ArcGIS geocoder called directly found it.
- `parking.py` lists any mapped lot, including big private office lots: near Rockwood Hall the nearest "Rockwood Road" lot is a corporate campus. Look at the TRAILHEAD tile before keeping one.
