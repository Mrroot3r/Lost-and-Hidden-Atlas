# kcmo_evnk: Kansas City: 18th and Vine and the east side
state: Missouri
region: kcmo
date: 2026-11-24
places: 12
file: data_kcmo_evnk.py

## What this batch is
Twelve places on the east side of Kansas City, Missouri: 18th and Vine (the Gem Theater, the Eblon Theater facade, the Black Archives in the old Parade Park maintenance building, the district itself), the Historic Northeast (Independence Boulevard Christian Church, the Edward A. Stevens House at Scarritt Point, Tiffany Castle, Pendleton Heights, Cliff Drive), the East Bottoms (Heim Fire Station No. 20) and Swope Park (Shelter No. 5, the Swope Memorial). The Atlas had about 60 places within 3 km of 18th and Vine, almost all downtown and Midtown, and none of these. Sources: the National Register forms for the church and the Stevens House (NPGallery text), the African American Heritage Trail of Kansas City site, Clio, the city parks pages, KCUR, the Pitch, Wikipedia as raw text, and the Black Archives and American Jazz Museum pages for hours.
Not checked: nothing was seen on the ground. The church gave no service times on its page. The Gem Theater's own visiting hours were not found (the museum next door has them). Whether the Eblon front wall is still standing after the 2016 redevelopment plan was not confirmed. The Heim fire station's use today rests on a 2015 article. The Swope shelter could not be picked out on the aerial (pin is `site`). Red brick is `?` where no source gave the colour. Most Missouri State Parks nomination PDFs (mostateparks.com) now answer 404 and the archived copies cannot be fetched here, so most Register forms for east-side listings were not read.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kansas City Call building | 1715 East 18th Street, Kansas City (about 39.0905, -94.5625) | The Heritage Trail page names the address and the newspaper's history | A source for when the building was put up and what is left of it |
| Allen School | 706 West 42nd Street, Kansas City, Westport | First public school in Westport and Kansas City; on the Kansas City Register (2009), per the Heritage Trail | A source for the building's date and present use |
| Nettleton Home | 5125 Swope Parkway, Kansas City (39.0324, -94.5419) | On the National Register (1999), Colonial Revival, by Wight and Wight, health and medicine | The nomination form could not be read: what the home was and what it is now |
| Scarritt Point North and South historic districts, Bellefontaine Avenue Historic District | Gladstone Boulevard bluff, Kansas City (about 39.115, -94.545) | On the Register (1997, 2011); HMdb markers exist | Forms could not be read; HMdb answered 403 |
| Linwood Presbyterian Church and Home for Convalescent Employed Women; St. Stephen Baptist Church; Phillis Wheatley School-Willis Chapel AME; Christian Church Hospital; Joe Vaccaro Soda Water building; Marks and Garvey district | East of Troost, Kansas City (Register list points, 2004 to 2026) | Register listings only | Forms or a page naming what is left |

## Tips
- Missouri State Parks Register PDFs (mostateparks.com/sites/mostateparks/files/...) turn up in searches but 404 now, and the web fetch tool refuses web.archive.org. Only forms that NPGallery has digitised (about 2012 on, for a few earlier ones) can be read as `.../NRHP/GetAsset/NRHP/<number>_text`; the rest return a one-page placeholder.
- The African American Heritage Trail of Kansas City (aahtkc.org, sitemap at /sitemap.xml) has a short page for each site along 18th and Vine and the east side, with address and what survives or was demolished; page.py reads it well.
- HMdb nearby lists answered 403 from page.py in this run.
- The Wikipedia Register lists for Kansas City are split: "National Register of Historic Places listings in Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other" (wiki_raw.py --rows works on those, not on the "Kansas City, Missouri" page).
