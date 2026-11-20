# adk_pbhk: Lake George, Bolton, Warrensburg and northern Warren County
state: New York
region: adk
date: 2026-11-20
places: 18
file: data_adk_pbhk.py

## What this batch is
Eighteen places in Warren County, New York (region `adk`, drawn at random by `choose.py --state ny`, which offered Warrensburg); `start.py` found four Atlas places within 15 km of Warrensburg (all in Lake George village, none of them the forts, the courthouse or its churches) and none round Chestertown or Bolton Landing. Lake George village: the Fort George ruins (the 1759 bastion, DEC Battlefield Park), Fort William Henry (the 1950s reconstruction, a museum), the old Warren County Courthouse (Lake George Historical Association museum), the 1909-11 D&H station, Caldwell Presbyterian and St. James' Episcopal churches, Wiawaka Holiday House and the Mountainside Free Library. Bolton: The Sembrich and The Sagamore. Warrensburg: the Mills district on the Schroon River, the Main Street (Hamlet of Warrensburgh) district and the Mixter Blacksmith Shop. Chestertown's small Register district, the Heintzelman Library at Brant Lake, Riverside station at Riparius, the Stony Creek Methodist church and the Silver Bay Association. One ruin, the rest standing. Sources were read with `wiki_raw.py` and `page.py`: Wikipedia, three Register forms that NPGallery has as text (16000164, 13000310, 100001249), HMdb markers (from nearby lists round Warrensburg, Bolton Landing, Chestertown and Riparius), the DEC Battlefield page, the Lake George Historical Association's hours page, The Sembrich's visit page, St. James' own site, the Pomeroy Foundation's Riverside Station page, Warren County's Horicon marker sheet and Lake George Chamber pages. Every pin was looked at on the leaf-off aerial (and LiDAR sheet); five were moved (D&H station, Caldwell church, Mountainside library, Wiawaka, the Warrensburg Main Street pin). Not checked: anything on the ground; the summer hours of Fort William Henry (its own site refused `page.py`; the winter weekends come from the operator's season post on iloveny.com); the season hours of The Sembrich (closed until May 2027 when read); service times at Caldwell Presbyterian and Stony Creek; hours of the Mountainside library and the Horicon historian's office; whether non-guests may walk the Sagamore, Silver Bay or Wiawaka grounds; present use of the D&H station; parking at Fort George (the mapped lot is a boat yard) and at Riverside station. The Sagamore's rebuild date differs between Wikipedia (early 1920s) and the Bolton marker (opened 1930); both are given. Red brick was settled by picture only for the courthouse (yes); several places are left `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Horicon grist mill site | Brant Lake, NY (HMdb 77378, 43.67602, -73.75221) | Jud Barton's grist mill, 1865 to 1937, on the Mill Pond outlet (Horicon Historical Society marker; Warren County's Horicon marker sheet says "this site was once a grist mill") | Whether anything of the mill or its race is left; mentioned in the Heintzelman Library entry only |
| Hudson Valley Railway power house | Warrensburg, NY (Pomeroy marker 133043, 176 River Street, 43.48944, -73.77832) | Electricity first made here in 1902 for the trolley to Lake George | What stands at the site now |
| Waddell House | Wevertown, Johnsburg, NY (Pomeroy marker 302375, 2363 Route 28, 43.63367, -73.94142) | c. 1869 house of Robert and Electa Waddell; the historical society acquired it in 2021 | Whether it opens as a museum, and when |
| Gates Homestead | Bolton, NY (43.5378, -73.6678) | c. 1830 house with ice house, carpenter shop and barns moved here in 1919 (Wikipedia; Register 10000229) | Who owns it and whether it can be seen; the form is the NPGallery placeholder |
| Merrill Magee House | Warrensburg, NY (43.4964, -73.7767) | Register 85000728 | No article and the form is the placeholder |
| Hague Baptist Church; Church of Saint Sacrement; Mohican Point | Hague and Bolton Landing, NY | Register listings 100005709, 100013036, 100012102 (2020s) | NPGallery returned only 893 characters for each; no other source read |
| Villa Marie Antoinette | Bolton Landing, NY (HMdb 18427, 43.53639, -73.6675) | Millionaires' Row mansion of Dr. William Beckers, sold to Harry K. Thaw in 1943 (Bolton Historical Society marker) | Whether it stands and is visible from 9N |

## Tips
- NPGallery forms for Warren County listings before 2010 are all the one-page placeholder; the 2020s listings (Hague Baptist, St. Sacrement, Mohican Point) return 893 characters, which `page.py` does not yet name as a placeholder.
- The ArcGIS PointAddress for 57 Beach Road, Lake George falls on the steamboat dock; `osmnear.py ... buildings` found the station as "former D&H Lake George (Caldwell) station".
- The Register district point for the Hamlet of Warrensburgh falls in woods south of the hamlet; the Floyd Bennett marker on Main Street is a better pin.
- fwhmuseum.com and fortwilliamhenry.com answer 403 to `page.py` and `hours.py page`; horiconny.gov answers 403 too.
- HMdb nearby lists with a 3-mile radius round four hamlets gave most of the Warren County names and every marker position in a few requests.
