# kcmo_midt_zqrp: Kansas City: Quality Hill, downtown and Midtown
state: Missouri
region: kcmo
date: 2026-11-24
places: 14
file: data_kcmo_midt_zqrp.py

## What this batch is
Fourteen standing places in Quality Hill, downtown, the Crossroads and Midtown of Kansas City, Missouri, none of which the Atlas had: the two Quality Hill cathedrals (Catholic and Episcopal), City Hall, the Jackson County Courthouse, Municipal Auditorium, the Bryant Building, the former Federal Reserve Bank at 925 Grand, the Western Auto and Sweeney School buildings, the Masonic Temple, the Nelson-Atkins Museum's 1933 building, Kemper Arena, the Hyde Park neighbourhood and Penn Valley Park. They come from the Wikipedia lists of Register listings in Jackson County (downtown and the rest of Kansas City) checked against the Atlas by name, then each article read as raw text (`wiki_raw.py`). Hours: the cathedral's Mass times are from its own page; the Episcopal cathedral's and the City Hall deck's are from web search results quoting the cathedral's and the city's pages (those pages would not open); the Nelson-Atkins hours are Wikipedia's, because its page showed only the free admission and closed holidays. No Register forms were read. Nothing was checked on the ground. Red brick is `?` almost everywhere: no source read gave a colour. Two pictures were chosen (Nelson-Atkins courtyard view, the Scout statue for Penn Valley Park); the rest use their Wikipedia article's picture. Hardesty Federal Complex was dropped: it is the National Cloak and Suit building already on the Atlas, and Wikipedia's point fell on houses.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kansas City Southern Railway Building | 114 W 11th St area, Kansas City, MO (39.10333, -94.585) | Wikipedia: 1914, John McKecknie, KCS headquarters to 2002, Register 2004 | Anything beyond that three-line stub; current use |
| Webster School, Columbia Building, Fairfax Building, Western Newspaper Union Building | Crossroads and downtown, Kansas City, MO | Register-listed, no Wikipedia text or only a stub | Any source describing them |
| Hyde Park and Hanover Place houses (Janssen Place, Bellerive, Knickerbocker site, Westminster Congregational Church) | Midtown, Kansas City, MO | Register districts and listings in the Jackson County list | Sources and a street-level look at each |
| Kansas City Museum (R. A. Long House) | Scarritt Point, Kansas City, MO | Already on the Atlas as Museum of Kansas City (Corinthian Hall) | Nothing; listed so nobody searches again |

## Tips
- Matching Register rows to the Atlas by name needs the built `build/sites.json`; many rows looked missing that matched under another name, so check by keyword before researching.
- The Jackson County Register list is two pages: "...Jackson County, Missouri: Downtown Kansas City" and "...: Kansas City other" (the Kansas City title itself has no rows).
- Wikipedia's coordinates for the Hardesty complex fell on a block of houses; check any KC point on the aerial.
- `kcmo.gov`, the cathedral's own Episcopal site and the Masonic Temple's site would not open from `page.py`; a web search result quoting them gave the hours.
- Excelsior Springs, Lexington, Independence, Lee's Summit, Raytown, Weston and Westport were already worked by earlier batches: `start.py` counts only 15 km, so check `notes/kcmo_*.md` before choosing a part.
