# kcmo_hyde_bzkp: Kansas City: Midtown, Hyde Park and Sunset Hill
state: Missouri
region: kcmo
date: 2026-11-24
places: 15
file: data_kcmo_hyde_bzkp.py

## What this batch is
Fifteen National Register listings in Midtown, Hyde Park, Sunset Hill and the blocks east of Troost, Kansas City, Missouri, none of which the Atlas had: the Peters and Braley mansions (both by Henry Hoit), the Michelson and Shankman buildings on Troost, the Luzier laboratories, the ACME cleansing plant, the First Swedish Baptist Church, the Gotham and Aurora apartments, the Swinney, Norman, Ladd and St. Francis Xavier schools, the Spofford children's home and the Interstate Bakeries headquarters. Chosen after Platte County, Johnson County (Kansas) and the other parts named for this run turned out to be nearly covered already; Register listings in Kansas City itself were the real gap (a keyword match of the Jackson County lists against build/sites.json showed about 100 unmatched rows).
Facts come from NPGallery nomination forms that have a text layer (listings from 2013 on mostly do; those from before about 2012 give a one-page placeholder). Present use and ownership were not checked, so every place is acc='view' and says so. Pins: the ArcGIS address lookup (PointAddress) put most on the building; the Wikipedia list points were often on the street. Michelson, Shankman and the Swedish church were moved by eye on the aerial. No parking was looked up; no hours exist because none is open to visitors on a page read. Pictures are Commons photographs; Braley and the Interstate building have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Walt Disney House | 3028 Bellefontaine, Kansas City, MO (39.07, -94.5472) | Register 78001654; a Commons picture exists; Wikipedia has no article | Any source beyond the list (NPGallery has a placeholder) |
| Mary Rockwell Hook's Sunset Hill houses (Hook, Rockwell, Ostertag, Four Gates Farm) | Kansas City, MO | Nine listed together in 1983; the Wikipedia article on Hook gives no per-house facts | Per-house sources; the forms are placeholders |
| Bellerive Hotel, Janssen Place, William Volker House, Norman Tromanhauser House, Hiland Telephone Exchange | Midtown and Volker, Kansas City, MO | Register listings, forms are placeholders | A readable source for each |
| Hazelle Building, Firestone service station, Mayfair Apartment Hotel, St. Francis Xavier church, Phillis Wheatley School-Willis Chapel | Kansas City, MO | Register listings of 2021 to 2026; NPGallery returns a 893-character stub | The nomination text from the Missouri SHPO |

## Tips
- NPGallery text is readable for Missouri listings numbered 13xxxxxx and later and 100xxxxx up to about 100008xxx; 100008xxx and later returned a stub. Test with page.py before planning.
- A cached form is in research/pages; extract the Section 7 summary with a regex on "Section number 7 Page 1" and the significance with "Section number 8".
- A Wikipedia list link in `links` makes photo_find.py treat the place as having an article (it then lists nothing to look at); cite the form only.
- The ArcGIS PointAddress result was better than the Register list point for 12 of 15 Kansas City buildings; two buildings on one block can geocode to the same point.
