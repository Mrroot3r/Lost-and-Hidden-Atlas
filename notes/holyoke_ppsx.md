# holyoke_ppsx: Massachusetts: Holyoke, the Paper City
state: Massachusetts
region: pv
date: 2026-11-26
places: 6
file: data_holyoke_ppsx.py

## What this batch is
Six places in and beside Holyoke (Hampden County), from a "videos" session (job 9) working one Old World Exploration video about Holyoke (the record is `source/videos/20220721_4JhhAg_5B3U.md`; 21 names: 6 added, 3 already on the Atlas, 8 gone, 3 not found). The Atlas had only the canals, the Mount Tom sites and Carnegie libraries near here. Added: Holyoke City Hall (1871 to 1876), the Holyoke Dam (1895 to 1900) with its fishway, the Holyoke Public Library (1902), Scott Tower in Anniversary Hill Park (1939 to 1940), the castle front of the 1907 Holyoke Armory, and Mary Lyon Hall at Mount Holyoke College in South Hadley (1897). Sources: Wikipedia read with wiki_raw.py; the library's own history and hours pages; the city's directory page (City Hall hours) and its park and armory pages; Holyoke Gas & Electric's fishway page; Historic Buildings of Massachusetts; WHDH and the Daily Hampshire Gazette; the Mount Holyoke archives' architects guide. Every pin is an OpenStreetMap point and was looked at on the 2023 leaf-off aerial. Not checked: whether the armory front still stands after the city's study posted in January 2023 (a 2018 photograph shows it); Scott Tower's park hours and whether the tower is fenced off during the 2026 to 2027 work; the Scott Tower trail parking at the dead end of Overlook Drive, which could not be picked out on the aerial and is not pinned; parking at the college; whether Mary Lyon Hall is red brick or red stone (left '?'); interiors other than City Hall's windows and the library's.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kenilworth Castle site (Edward C. Taft's summer house) | Holyoke, MA, near Smith's Ferry | Built 1894 to 1895 and pulled down in 1959, per search results quoting Digital Commonwealth and the Valley Advocate | Whether anything is left to see, and where exactly it stood |
| Holyoke YMCA, where volleyball began | Holyoke, MA | Wikipedia (Holyoke): the first building burned in 1943 | Where it stood, and whether a marker is there |

## Tips
- Holyoke has no Register list of its own on Wikipedia; `wiki_raw.py --rows -g Holyoke "National Register of Historic Places listings in Hampden County, Massachusetts"` gives its 16 rows.
- The armory's 2020 study for the city (a 62-page PDF on the city's storage) has a text layer and reads with `page.py -g`.
