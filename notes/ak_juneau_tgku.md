# ak_juneau_tgku: Alaska: Juneau, Douglas and Lynn Canal
state: Alaska
region: ak
date: 2026-11-19
places: 19
file: data_ak_juneau_tgku.py

## What this batch is
Nineteen places in the City and Borough of Juneau, the first Alaska batch after the one worked example (Kennecott): downtown Juneau (St. Nicholas Orthodox Church, the House of Wickersham, the city museum in the 1951 library, the Alaskan Hotel, the Valentine Building, the Alaska Steam Laundry, the Bergmann Hotel, the Fries miners' cabins, the Governor's Mansion, Evergreen Cemetery), the gold mines (Last Chance Basin / Jualpa camp, the Alaska-Juneau mill ruins, the Treadwell ruins in Douglas), the Mayflower School in Douglas, and out of town the Shrine of St. Thérèse, the Gruening cabin, Taku Glacier Lodge and the Sentinel Island and Point Retreat light stations. Sources: the Register list and articles through `wiki_raw.py`, NPGallery nomination texts through `page.py -g`, and the managing bodies' own pages (Alaska State Parks, City and Borough of Juneau, the parish, the shrine, the hotel, Wings Airways), with the Juneau Empire, Juneau Independent, KTOO and HMdb for current state. Hours come from the parish, shrine and city museum pages; Wickersham's state page gives only "May through September". Not checked: anything on the ground; interiors; the Last Chance museum's hours (no page of its own found; the Travel Juneau directory's hours are quoted in the access note only); whether the Bergmann renovation of 2024 went ahead; who owns the Alaska-Juneau mill ground; whether Point Retreat can be visited. The Alaska-Juneau mill pin is area only (on the site of the steam plant demolished in 2024-25, below the mill); the Shrine and Gruening cabin pins are under trees. The pin check's aerial for Juneau is Esri with leaves on, and its LiDAR showed nothing extra.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Durham (Fort Taku) site | Taku Harbor, Juneau, AK | Hudson's Bay Company post of 1840, a National Historic Landmark (Wikipedia: Fort Durham) | Address restricted in the Register; no source says the public may visit or where |
| Alaska Gastineau mill ruins, Thane | Thane, Juneau, AK (58.26617, -134.33393, OpenStreetMap landuse "Alaska Gastineau Mill") | Mapped in OpenStreetMap; tours advertised by Travel Juneau ("AJ Mine Gastineau Mill Tour") | A source on what is left, the owner and public access |
| Alaska Treasure mine and Gastineau City | Near Juneau, AK | Juneau Empire article on the Alaska Treasure Company (mill 1906, closed 1917, equipment left) | Location, what is left, ownership, access |
| Perseverance Trail mine ruins (Silver Bow Basin, Ebner) | Basin Road, Juneau, AK | Alaska State Parks says the trail "features old mining ruins"; city notices of rockslides and closures | Which ruins, where, and current trail status from the city |
| Holy Trinity Episcopal Church | 415 4th Street, Juneau, AK | 1896 church burned March 12, 2006; rebuilt 2009 (Wikipedia) | Left out: the old building is gone |

## Tips
- Juneau's managing pages read well with `page.py --all`: dnr.alaska.gov state park pages, juneau.org (museum hours, cemetery, newsroom notices), stnicholasjuneau.org, shrineofsainttherese.org (the FAQ page `?p=2890` has visiting hours).
- `wingsairways.com/?p=…` addresses from search results answered 404; the blog page `wingsairways.com/blog/taku-glacier-lodge-tour/` read.
- Web search results here gave titles and links only, no quoted text.
- The Register list coordinate for the Alaska Governor's Mansion is the same as the Rudy-Kodzoff House's (58.37483, -134.58179), miles from the mansion; the ArcGIS PointAddress for 716 Calhoun Avenue is on it.
- `osmnear.py ... buildings -g ruin` returned a "building=ruins" by the Juneau cruise docks that the aerial shows as the AJ steam plant (demolished 2024-25), not the mill ruins.
