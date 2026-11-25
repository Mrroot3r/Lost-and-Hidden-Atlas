# mo_hvxk: Lexington houses and a Liberty historic district, Missouri
state: Missouri
region: kcmo
date: 2026-11-25
places: 7
file: data_mo_hvxk.py

## What this batch is
Seven places, far fewer than the 15 to 20 aimed for, because the ground I drew (Lee's Summit, Raytown, Grandview and the country round, in Jackson and Cass counties) was already worked: I compared the Register lists for Jackson, Clay, Platte, Lafayette, Ray, Cass and Johnson counties and the Wikipedia building categories for them against every data file, and almost everything is on the Atlas. What was missing: five Lexington-area Register houses (Gosewisch, Catron, Tevis, Cheatham, Spratt-Allen-Aull), the Stramcke House (The Cedars) and the Arthur-Leonard Historic District in Liberty. Facts come from Wikipedia read as raw text, with house addresses taken from web search results that quote the Park Service listing. No Register form could be read. All are private houses or streets, so access is look-from-the-road. Not checked: owners, what survives inside, exact house positions (Wikipedia coordinates; several are approximate; Tevis falls on a road and Arthur-Leonard on a shop intersection on the aerial). Photographs: Commons has none for five, recorded by the tool.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Georgen House, Smallwood V. Noland House | Independence, MO (39.0803, -94.415; 39.0817, -94.4369) | Register list only (Wikipedia list coordinates); no Wikipedia article | A source saying what each is and what is left |
| Jewell-Lightburne Historic District | Liberty, MO | On the Wikipedia Clay County list | An article or page describing it |
| Central Female College (old Masonic College) | Lexington, MO (39.18237, -93.88837) | Wikipedia: Masonic College building given 1870 to a women's college that ran to 1924 | Whether anything of it stands |
| Bailey Family Farm Historic District | Lee's Summit, MO (38.8958, -94.3414) | Register 2006 (from earlier notes) | Anything readable on what stands |

## Tips
- Jackson, Clay, Platte, Lafayette, Cass and Ray counties are now nearly exhausted from Wikipedia lists and categories; the next gain needs Register forms (mostateparks.com PDFs answer 404) or a person with local sources, or the Kansas side.
- grep for O'Bannon fails on the escaped apostrophe in data files (an earlier note says this too): I nearly re-added the O'Bannon Homestead; build_sites.py caught the duplicate id.
- Wikipedia category listing through the API with a plain user agent works but fails now and then: retry after a few seconds.
