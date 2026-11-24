# ks_dgco_fmqb: Douglas County, Kansas (Lawrence area)
state: Kansas
region: ks
date: 2026-11-24
places: 14
file: data_ks_dgco_fmqb.py

## What this batch is
Fourteen places in and around Lawrence, Lecompton, Baldwin City and Vinland, taken from the Kansas Historical Society's National and State Register list for Douglas County and not yet on the Atlas. The Atlas had about 40 places within 15 km of Lawrence before and has 51 after (11 of the 14 fall within that radius). Facts come from the society's register pages, the nomination forms it publishes (Winter School, Kibbee Farmstead, Lone Star Lake Dam read whole; the older scanned forms have no text layer and could not be read), a Lawrence Journal-World local-history column (English Lutheran Church), a City of Lawrence planning report (Lucy Hobbs Taylor House), Trinity Lutheran's own page for service times, and Wikipedia and Commons captions. Nothing was checked on the ground. Pins are on each address as the ArcGIS geocoder gives it, looked at on the Kansas aerial. Wikipedia's list coordinate for the English Lutheran Church was 3 km off, so do not trust list coordinates without checking the address. Owners and present use are not known for most of the private houses. Pictures: 12 of 14 have one (two use their Wikipedia picture); English Lutheran Church has none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Upper Wakarusa River Crossing | south of Lawrence, E 1400 Road (38.9098, -95.2369) | 2014 nomination: two cutdowns of the Oregon and California trails on the north bank, 20 to 30 feet wide and 60 feet long; private land | A public place to see them from |
| Elmwood Stock Farm Barn | Baldwin City, 571 E 1000 Road (38.822, -95.3171) | 2022 nomination: dairy barn built before 1901 with milking parlour, on a private farm with 2-3 miles of ruined stone fences | Whether it can be seen from the road |
| Sowers/Crawford Farms and O'Sullivan Farmstead | Overbrook, Douglas County | 2023 and 2018 listings: family farms with stone cellar and dry-stacked stone fences | Any public view |
| Akers House | Lawrence (38.9538, -95.2420) | Commons captions call it a two-story brick Italianate house, listed 2022 | A source for its history and owner |
| Dr. Morse House, Benedict House, Pilla House, Clinton School District 25 | Lawrence and Eudora | Register listings (Second Empire 1041 Tennessee; Stick/Eastlake 923 Tennessee; Queen Anne in Eudora; former school now Clinton city hall) | The nomination forms are scans with no text; no other source read |
| Kansas Homestead of Thomas McQuillan, Appanoose Church of the Brethren | Baldwin City and Overbrook areas | Register listings only | A source describing each |

## Tips
- kansashistory.gov answers `curl` and `page.py`: `natreg_listings/search/page:N/county:DG/records:all` lists every Register property for a county with a summary, and nomination PDFs follow the pattern `resource/national_register/nominationsNRDB/<name>.pdf`. Newer forms (about 2006 on) have a text layer (pdftotext); older ones are scans. Good for any Kansas county.
- The Wikipedia list rows say "article:" even when the article does not exist; `wiki_raw.py` then says NO SUCH ARTICLE. Wikipedia is almost no help for Lawrence's Register houses.
- Commons has the Register photographs for newer Douglas County listings, uploaded by one contributor, named for the property, taken at the pin.
- fumclawrence.org answers 403 to `page.py`, so its hours stayed unread.
