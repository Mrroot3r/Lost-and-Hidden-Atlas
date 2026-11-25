# mo_lafy: Lafayette and Johnson counties, Missouri: a roadside mausoleum and two Lexington-area houses
state: Missouri
region: mo
date: 2026-11-25
places: 3
file: data_mo_lafy.py

## What this batch is
Three places east of Kansas City: the Joseph M. Miller Mausoleum near Holden (a Missouri Preservation page, Wikipedia and a Waymarking page; the sources disagree on its building dates and the entry says so), and two Register-listed Lexington-area houses, the William P. Robinson House (about 1850) and the house at 1413 Lafayette Street (about 1840), both from Wikipedia stubs only. I meant this to be the Lee's Summit, Raytown and Grandview part, but a comparison of the National Park Service's Missouri listings against the Atlas showed it was already finished, so I moved to Lafayette County and found most of its listings (Higginsville depot, Douglass School, Odessa Ice Cream building, the Houx and Dinwiddie houses) were already on the map too. Not checked: the Register forms (every mostateparks.com PDF answers 404 and the web fetch tool refuses web.archive.org), who owns the two houses and whether either can be seen from a public road, the mausoleum's tour arrangements, and the depot's present use (sources disagree). Pins were checked on the aerial; the mausoleum pin was moved 23 m off the road. Brick for the two houses is "?".

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Gosewisch, Catron, Cheatham, Tevis, Stramcke and Spratt-Allen-Aull houses | Lexington, MO | Register-listed houses with address-restricted coordinates (Gosewisch about 39.1578, -93.8917) | A readable source for each and a public view |
| Central Female College (former Masonic College) | Lexington, MO (39.18237, -93.88837) | Wikipedia: women's college 1869 to 1924 in the former Masonic College building | What, if anything, of it stands |
| Magnolia Mills, Jones Brothers Mule Barn, Howard School, Warrensburg station, Chilhowee Historic District | Johnson County, MO | Register listings read on Wikipedia; Warrensburg is about 55 miles from Kansas City, so outside this area | Sources for what stands; Magnolia Mills has only a concrete elevator left |

## Tips
- Compare the National Park Service's Missouri listings (`tools/nrhp_state.py "MISSOURI" mo`, then distance to every Atlas place in build/sites.json) before choosing: it shows in a minute that the Kansas City ring is nearly all done. What is left is single listings in towns 40 to 60 miles out.
- `start.py` counts only 15 km around a town, so it missed that Higginsville, Odessa and Douglass School were already on the map; search build/sites.json by town as well.
- Wikipedia's "Category:Buildings and structures in <County>, Missouri" through the API works and lists articles the Register list lacks.
- HMdb answered 403 from this session.
