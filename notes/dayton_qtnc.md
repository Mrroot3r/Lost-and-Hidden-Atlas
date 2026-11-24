# dayton_qtnc: Ohio: old Dayton
state: Ohio
region: oh
date: 2026-11-24
places: 11
file: data_dayton_qtnc.py

## What this batch is
Eleven standing places in Dayton, Ohio, where the Atlas had nothing within 15 km. Nine come from the names in one Old World Exploration video about the city (the record of every name is `source/videos/20221029_H5qt3Q5vqeg.md`; the video is a tip and nothing rests on it): the Old Montgomery County Courthouse, the Dayton Arcade, the Victoria Theatre (the old Turner Opera House), the Dayton Masonic Center, the Southern Ohio Lunatic Asylum (Dayton State Hospital), the Dayton Biltmore Hotel, St. Mary Catholic Church, the Home Chapel of the Central Branch soldiers' home (Dayton VA Medical Center) and the old YMCA (Landing Apartments). Two more were added from the Dayton Register list: the Woodland Cemetery gateway, chapel and office, and the Wright Cycle Company shop. Facts are from Wikipedia (read as raw text), the National Register list for Dayton, National Park Service pages (the Central Branch, the Dayton Aviation Heritage park's hours), the VA history page on the Dayton chapel and a WYSO report on the Old Courthouse. Hours were read on the parish page (St. Mary), the cemetery's page and the park's page. Not checked: the Arcade's rotunda hours (on its home page header, drawn by script), the Victoria Theatre's box office hours, whether the VA Home Chapel or the Masonic Center take visitors, parking downtown, and red brick for most places (left '?'). Pins are ArcGIS address points or OpenStreetMap buildings, all looked at on the aerial; the asylum and the YMCA were moved onto their buildings.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Summit Street YWCA | Dayton, OH (236 South Paul Laurence Dunbar Street) | National Register 2020; the National Park Service page says it was the country's first African American YWCA and is privately managed, not open to the public | Year built and a pin looked at on the aerial |
| Putnam Library, Dayton VA | Dayton, OH (Building 120, VA campus) | National Park Service page names it among 28 surviving pre-1930 buildings; a Dayton Daily News listing puts the Miami Valley Military History Museum in Building 120 | Hours from the museum's own page; a separate entry or a note on the chapel |
| Miami and Erie Canal remains in Dayton | Dayton, OH | Named in the video only | Any source saying canal stonework survives in the city |

## Tips
- `geo.py "<street address>"` gave PointAddress results on the building for nearly every Dayton address; 2335 Wayne Avenue (the asylum) fell on Wilmington Avenue and 117 West Monument Avenue beside the YMCA.
- HMdb.org answered 403 to `page.py` again (November 24, 2026).
- The Wikipedia coordinate for the Dayton Biltmore Hotel is about 1 km north of the building; the Register list point and the address agree.
- The Dayton Arcade's own home page shows its rotunda hours in a header drawn by script; `page.py` cannot read them.
