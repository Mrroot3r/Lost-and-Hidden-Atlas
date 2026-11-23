# kcmo_ene_xwrk: Kansas City: 18th and Vine and the Northeast
state: Missouri
region: kcmo
date: 2026-11-23
places: 11
file: data_kcmo_ene_xwrk.py

## What this batch is
Eleven places on the east side of Kansas City, Missouri: the 18th and Vine district (Mutual Musicians' building, Paseo YMCA, Attucks School, Fire Station No. 11, Gillis Orphans' Home), the Northeast (Museum of Kansas City, the two Scarritt houses, Beth Shalom Synagogue) and the East Bottoms and Independence Avenue (Heim bottling plant, National Cloak and Suit building). Chosen from the Jackson County Register list "Kansas City other", skipping everything already in the Atlas. Sources: Wikipedia as raw text; the Register forms for the Mutual Musicians' building, the Heim plant and the Cloak and Suit building (read); the museum's own visit page; KCUR, Clio and a 1902 book page. The Register forms for the other places are not online (NPGallery returns a placeholder), so those entries are thin and say so. Not checked: any interior, any owner, the Mutual Musicians' and church hours (no page of their own was read, so hours are "?"), who owns the Gillis building. The Gillis pin is area only. Lexington was the first choice but an earlier batch (lex_mhzv) already covered it.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Heim Fire Station No. 20 | 2701 Guinotte Ave, Kansas City, MO (39.1192, -94.5491) | Register-listed 2024; vacant; beside the Heim plant | State Parks nomination PDF would not open (404 live, archive not fetchable): no date or description read |
| Independence Boulevard Christian Church | Kansas City, MO (39.1058, -94.5463) | Register-listed 2015 | No source read |
| St. Stephen Baptist Church | 39.0953, -94.5650 | Register-listed 2026 | No source read |
| Spofford Home for Children; Seven Oaks School; Sanford B. Ladd School; Linwood Presbyterian Church | East side of Kansas City, MO | Register listings, 2012 to 2021 | No source read |
| Byram's Ford, Santa Fe Trail swales, Walt Disney House (Bellefontaine) | Kansas City, MO | Register listings | Disney house and swales not on the Atlas; no source read |

## Tips
- NPGallery serves a placeholder for most pre-2000 forms (82003142, 91001151, 91001150, 77000809, 78001661, 80002366); only some, like 79001372, have text. Newer forms come from the npgallery.nps.gov/GetAsset/<uuid> links in a web search result.
- The Register list for Kansas City is split: use "National Register of Historic Places listings in Jackson County, Missouri: Kansas City other" with wiki_raw.py --rows; the plain Kansas City title has no rows.
- mostateparks.com nomination PDFs now return 404; an archived copy exists but page.py cannot fetch it.
- start.py counts only 15 km round a town, so Lexington looked thin; check notes/ for an earlier kcmo_ batch before choosing.
