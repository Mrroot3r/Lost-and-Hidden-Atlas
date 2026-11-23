# kcmo_lex_mhzv: Lexington, Higginsville and Odessa, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 12
file: data_kcmo_lex_mhzv.py

## What this batch is
Twelve places in Lafayette County, about 40 miles east of Kansas City, from the county's National Register list. The Atlas had two places near Lexington before. Facts come from Wikipedia read as raw text, Missouri State Parks and VisitMO pages as web search results quote them, a KSHB report on the Douglass School, and the Wikimedia Commons descriptions of the Douglass School photographs (which quote its Register form). The Register forms themselves could not be read (the Missouri State Parks PDFs answer 404). Nothing was checked on the ground. Hours were found only for the Confederate Memorial site (grounds sunrise to sunset; tours by appointment); the courthouse, museum and depot are `hours='?'`. Red brick is `?` for several houses whose source says "brick" but not its colour. Pins were checked on the aerial; the Hicklin farm, the Hicklin School and the Odessa ice cream building are site or area pins. Wikipedia's courthouse coordinate was about 250 m off; the address lookup was used. Pictures: 6 places have a Wikipedia photo; the depot and the Douglass School got Commons photos; Linwood Lawn, both Hicklin places and Wentworth have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Madonna of the Trail statue | Lexington, MO (OpenStreetMap point 39.18662, -93.8863) | 1928 statue; sources give three different corners (Highland and Broadway, Highland and Cliff Drive, Commerce Street) | A source or look at the aerial that settles where it stands now |
| Other Lexington Register houses | Lexington, MO | Minatree Catron, John E. Cheatham, Gosewisch (39.15778, -93.89167), Tevis, Stramcke, Spratt-Allen-Aull houses and others on the Register list | Coordinates (most are address-restricted) and a source on what is left and who owns each |
| Machpelah Cemetery and Forest Grove Cemetery | Lexington, MO | Both Register-listed in recent years | No Wikipedia article; Register forms not read |
| Houx-Hoefer-Rehkop House | Higginsville, MO (39.07583, -93.71861) | Register listing | A source describing it |
| James M. Dinwiddie House | Dover, MO (39.19222, -93.70167) | Register listing | A source describing it |
| Lexington Battlefield earthworks and Masonic College site | Lexington, MO | Within the Anderson House entry's grounds | Whether they deserve their own entries |

## Tips
- `mostateparks.com/sites/mostateparks/files/<Name>.pdf` Register forms answered 404 for Douglass School, Wentworth and Cumberland Presbyterian Church, and `page.py` could not fetch the archived copies.
- Wikipedia's coordinate for the Lafayette County Courthouse is on the wrong block; the address lookup (`geo.py`) was right. Check courthouse coordinates against the aerial.
- Commons photograph descriptions often quote the Register form (the Douglass School ones did), which gives size and style when the form itself cannot be read.
