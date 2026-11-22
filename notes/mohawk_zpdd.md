# mohawk_zpdd: Amsterdam, Tribes Hill, Fonda and Randall
state: New York
region: mohawk
date: 2026-11-22
places: 15
file: data_mohawk_zpdd.py

## What this batch is
Fifteen places in Montgomery County (region `mohawk`, drawn at random by `choose.py --state ny`, which offered Hallsville; Hallsville itself had nothing sourceable beyond a private Register farm, so the session took the county's thin ground east of Fort Plain). The city of Amsterdam had only its vanished Main Street, the Sweet canal store, the creek dams and the Mohasco power house; this adds its standing Register buildings: the city hall (Sanford mansion), the Carnegie library, the armory now "Amsterdam Castle", the Greene mansion, the Guy Park Avenue and Vrooman Avenue schools (apartments), the former Temple of Israel (now a church), St. Stanislaus church, the post office with its 1939 Schnakenberg murals, Green Hill Cemetery and Pawling Hall in Hagaman. West of the city: Danascara Place at Tribes Hill (1795 brick house inside an 1870 villa; private), the old Caughnawaga burying ground and church boulder in Fonda, Barge Canal Lock E13 at the Thruway's Mohawk Valley Welcome Center (westbound only), and the Windfall Dutch Barn at Salt Springville. Sources: Wikipedia as raw text (`wiki_raw.py`), HMdb marker pages, the Thruway Authority's welcome-centre page, the Diocese of Albany's page for St. Stanislaus (Mass times), the Town of Minden's pages, the county tourism listings, and the 2019 Register form for Danascara Place (NPGallery PDF, text layer read), all with `page.py`. Pins: most are geocoder PointAddress hits on the building; the post office is OpenStreetMap's building; Lock E13 was moved onto the chamber seen on the aerial; St. Stanislaus is the geocoder's named point and the church could not be picked out for sure on the aerial (`prec='site'`). Not checked: anything on the ground; hours for the city hall, library (its site is drawn by script; county tourism lists weekday hours), post office, Temple (its site did not connect), Windfall barn and Pawling Hall; red brick for all but the city hall (yes, from its Commons photograph), the Vrooman Avenue school (yellow brick, per Wikipedia), the lock and the cemetery.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Walter Butler Homestead (Butlersbury) | Near Fonda (Wikipedia 42.96194, -74.35472) | Wikipedia: 18th-century 1½-storey farmhouse, 40 by 30 feet, on limestone foundation, built by Lt. Walter Butler, father of John Butler; Register 1976 | Owner, whether it is seen from a public road, a pin checked on the aerial |
| Currytown Reformed Church | Root, 665 NY 162 (HMdb 41375: 42.85952, -74.46944) | State marker: organized 1790; the marker photographs show a church standing | Date of the building and who uses it; no page found |
| Fonda Tavern and Veeder Home | NY 5 west and east of Fonda (HMdb 66777 at 3266 NY 5; HMdb 131375 at 3666 NY 5) | Markers: Fonda Tavern built about 1781 by John Fonda; Veeder home built about 1781 by Maj. Abraham Veeder, inn and ferry | Whether either house stands |
| Spraker Inn | NY 5 near Sprakers (HMdb 131435: 42.89613, -74.51651) | Marker: built 1795 by the Spraker family, river and turnpike tavern | Whether it stands |
| Barge Canal Locks E12, E14, E15, E16 | Tribes Hill, Canajoharie, Fort Plain, Mindenville | Town of Minden lists Lock 15 (Otsquago Club Road) and Lock 16 (Mindenville Drive); OpenStreetMap has "Lock E14 Canajoharie Dam" at 42.90828, -74.57701 | A source for each lock's date and public viewing point (Canal Corporation pages not read) |
| Hurricana Stock Farm | Amsterdam (Wikipedia 42.95833, -74.18556; HMdb 95887) | Wikipedia: Sanford stud farm, barns 1880–1920, Register 2013 | Present owner and whether the barns can be seen from a road |
| Caspar Getman and Van Wie farmsteads | Near Stone Arabia and McKinley | Wikipedia: Getman Dutch barn c.1790 and limestone smokehouse; Van Wie hop barn c.1884 | Owner and a view from the road; private farms |

## Tips
- Wikipedia's coordinates for Amsterdam City Hall (about 6 km west) and St. Stanislaus (about 1 km north) are wrong; the geocoder's PointAddress for the street address lands on the building.
- `photo_find.py look` on six places took about eight minutes; start it in the background as the prompt says, not in the foreground.
- `nom.py` answered HTTP 629 to most queries in this session; `osmnear.py ... buildings -g` and `geo.py` found what was needed.
