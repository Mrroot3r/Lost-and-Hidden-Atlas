# tx_qdfw: Big Bend, Texas
state: Texas
region: tx
date: 2026-11-17
places: 15
file: data_tx_qdfw.py

## What this batch is
A first pass over the Big Bend (region drawn at random by `choose.py`: tx). Fifteen places: eleven in Big Bend National Park (Castolon, Rancho Estelle / Dorgan-Sublett, Luna's Jacal, Sam Nail Ranch, Homer Wilson Ranch, Johnson's Ranch, Mariscal Mine, Glenn Springs, Hot Springs, Daniels Farm House, the Boquillas ore tramway), the Contrabando movie set in Big Bend Ranch State Park, Fort Leaton near Presidio, the Gage Hotel in Marathon and Kokernot Field in Alpine. Sources were read in this session with `page.py` (NPS history pages, NPS `nps.gov/places/...` pages, NPS campsite, fees and hours pages; TPWD pages for Big Bend Ranch and Fort Leaton) and `wiki_raw.py`. Park fees, opening and the Castolon visitor-center hours come from the NPS fees and hours pages; Big Bend Ranch and Fort Leaton fees and hours from the TPWD pages. Sources disagree, and both versions are given, on: the year La Harmonia moved into the Castolon barracks (1921 or 1925), when Luna came to his jacal (1916 or about 1890 to 1900), when Homer Wilson bought the land (1928 or 1929), Mariscal's last closing (1943 or 1944), and who led the Glenn Springs raid. Not checked: anything on the ground; what stands at Johnson's Ranch; where the Gage Hotel and Kokernot Field may be visited inside (both `view`); the parking at Luna's Jacal and Contrabando; the dates of the Boquillas tramways (no park page read gives them). Pins that mark the general area and not the thing: Johnson's Ranch (the campsite, ruins a five-minute walk away), Glenn Springs (the spring; no building remains seen) and the ore tramway (a point on the Ore Terminal Trail; the exhibit, trailhead and terminal were not located). Every pin was looked at with `pincheck.py --lidar`; none was moved.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| La Coyota village ruins | Big Bend National Park, TX, on the Ross Maxwell Scenic Drive near Alamo Creek | NPS place page `nps.gov/places/la-coyota.htm`: the oldest documented community in the park, settled 1884 by Severiano Chavarria; a few crumbling foundations, the road cuts through them "between mile marker 1 and 2" | A coordinate: which end the mile markers count from was not found, and OpenStreetMap has nothing named there |
| Camp Peña Colorado (Post Park) | About 5 miles south of Marathon, TX (Wikipedia 30.15861, -103.29222) | Wikipedia "Post Park": Army camp at the springs from 1879, 10th Cavalry from 1884, abandoned 1893, land given to Brewster County in 1935 | Brewster County's own page for the park (hours, rules), and whether any trace of the post stands (one secondary site says no buildings remain) |
| Shafter mining town | Presidio County, TX (Wikipedia 29.82028, -104.30333) | Wikipedia "Shafter, Texas": silver mining from about 1880, Register historic mining district, mine reopened by companies after 2012 | Who owns what in town now and where the public may look from; an active mine was mentioned |
| Contrabando waterhole ranch ruins | Big Bend Ranch State Park, TX, on the Contrabando Trail | A TPWD El Solitario newsletter (2009, seen only as a search snippet) mentions ruins of an 1890s ranch by Contrabando Waterhole | Open the newsletter or the park's trail map; a coordinate |
| Boquillas ore terminal | Big Bend National Park, TX, end of the Ore Terminal Trail above Ernst Valley | NPS: terminal of the aerial tramway from the Puerto Rico mine; trail about 8 miles round trip | A coordinate for the terminal and for the tramway exhibit (3.5 miles down Boquillas Canyon Road), to replace the area pin of `boquillas-ore-tramway` |

## Tips
- NPS park pages have a second set of addresses, `https://www.nps.gov/places/<name>.htm`, with quick facts (trail length, parking, location by road mileage) that the park's own history pages lack; guess the slug from the place name and `page.py` says 404 when it is wrong.
- `page.py --all` on nps.gov returns everything on one line, beginning with about 600 characters of site menu; cutting before "Contact Us." and after "Last updated:" leaves only the article.
- `nom.py` found most Big Bend historic sites by name (OpenStreetMap there is well mapped: "Dorgan house ruin", "Luna Jacal", "Homer Wilson Ranch", "Old Sam Nail Ranch" water pump); `osmnear.py ... buildings -g '.'` found the Hot Springs store, motel and house as `building=ruins`.
- LiDAR shading (`--lidar`) worked in far West Texas and showed the Mariscal Mine works and lines at Johnson's Ranch better than the aerial.
- In the desert a 1,600 m `look.py` view is too coarse to find a dirt trailhead lot; 700 m was still not enough on the Boquillas Canyon Road.
