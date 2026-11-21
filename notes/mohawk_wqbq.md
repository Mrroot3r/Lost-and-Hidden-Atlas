# mohawk_wqbq: Eastern Schoharie County: Schoharie, Gallupville, Middleburgh
state: New York
region: mohawk, scho
date: 2026-11-21
places: 22
file: data_mohawk_wqbq.py

## What this batch is
Twenty-two places in eastern Schoharie County, the first close pass there (region `mohawk`, drawn at random by `choose.py --state ny`, which offered Gallupville; Lansing Manor is filed under `scho` like the Blenheim bridge). Nearly all standing. Schoharie village: a full entry for the Old Stone Fort (replaces `lm-old-stone-fort`), the 1743 Palatine House, St. Paul's Lutheran church and cemetery, the Schoharie Valley Railroad Museum, the courthouse, Lasell Hall, Main Street (area pin), the Vroman and Sternbergh houses. Gallupville: the Becker Stone House, the Gallupville House and the Lutheran and Methodist churches. Central Bridge: the Westinghouse birthplace. Middleburgh: the Middle Fort site (markers only), the Dr. Best House museum, the post office with its 1941 mural, St. Mark's Lutheran, the Bellinger–Dutton house, the M&S depot and the Upper Middleburgh Cemetery. North Blenheim: Lansing Manor (closed for renovation in 2026 per NYPA). Sources: Wikipedia as raw text (`wiki_raw.py`, mostly short Register stubs), HMdb marker pages, and through `page.py` theoldstonefort.org, mohawkvalleymuseums.us, schohariepresbyterian.org, drbesthouse.com, villageofmiddleburgh.com and nypa.gov. Not checked: anything on the ground; interiors; red brick for most places (Wikimedia answered 429 to `brick.py`, so 17 places are `'?'`); service times for St. Paul's (its page gives none), Gallupville and St. Mark's (no pages found); the Best House's hours (its page gives none); post office hours; whether the Gallupville Methodist church still holds services; the use of the Middleburgh depot building; which of the two Westinghouse houses is the birth house. Every pin was looked at on the leaf-off aerial; five were moved (Old Stone Fort, Palatine House, Sternbergh, Westinghouse, Lansing Manor), each said in its pin note.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Old Stone House / Swarts Tavern | Schoharie, NY, North Main Street 0.1 mi south of Fort Road (HMdb 145449 at 42.67427, -74.30482; HMdb 32197 at 455 Main Street, 20 m away) | Two 1930s state markers: a stone house of about 1772 used as a tavern, set on fire Oct. 17, 1780 and put out by patriot soldiers; and "Swarts Tavern", erected about 1772, duel of 1820 behind it | Whether the two markers name one building or two, and whether it stands |
| Breakabeen Historic District | Breakabeen, Fulton, NY (42.52417, -74.38528) | Wikipedia: 33 buildings, Greek Revival, temple-front houses, a post-Civil War Italian villa hotel; listed 1974 | What survived the 2011 Irene flood |
| North Blenheim Historic District | North Blenheim, NY (42.47028, -74.45083) | Wikipedia: 25 buildings, an 1841 Greek Revival church; listed 1974 | What survived the 2011 Irene flood |
| Bramanville Mill (Chickering Grist Mill) | Cobleskill, NY (42.68806, -74.40611) | Wikipedia: 30 by 50 ft frame grist mill; listed 1976 | Whether it stands today, owner |
| Masick and Schoharie No. 3 quarries and mills | Schoharie, NY (42.63081, -74.30763; 42.68331, -74.27539) | USGS mine records in `start.py` | Any source on what is left; not looked at on the aerial |

## Tips
- NPGallery `_text` forms for Schoharie County (72000913 tried) are the placeholder, as elsewhere in New York.
- mohawkvalleymuseums.us gives days and times for the Old Stone Fort and the Schoharie Colonial Heritage Association; theoldstonefort.org itself gives only the season and fees.
- HMdb's nearby list round Schoharie village (3 miles) named about 90 markers; reading the marker numbers out of the cached page (as section 6 says) was the quickest way to find the Vroman, Sternbergh, Becker and Middle Fort positions.
- `brick.py look` hit Wikimedia 429 on the first picture and then hung past two minutes; run it after `photo_find.py`, not straight after.
