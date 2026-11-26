# ia_cedarrapids_ebuj: Cedar Rapids, Iowa
state: Iowa
region: ia
date: 2026-11-26
places: 12
file: data_ia_cedarrapids_ebuj.py

## What this batch is
Twelve standing buildings in Cedar Rapids, Iowa, which had two places in town (the Carnegie library and Brucemore), taken from the buildings named in one video of old postcards of the town (the record is source/videos/20250418_cMykFkwZzBY.md); the video was a tip only and nothing in the entries comes from it. Added: the Veterans Memorial Building and the Linn County Courthouse on May's Island, the 1908 Post Office and Public Building (Witwer Building), the Cedar Rapids Savings Bank Building (Guaranty Bank), the Muskwaki Block, the Hotel Roosevelt, the Paramount Theatre, the Scottish Rite Temple, and four churches: Immaculate Conception, St. Patrick's, Grace Episcopal and Westminster Presbyterian. Sources: Wikipedia read as raw text, the Linn County Register list rows, SAH Archipedia's Cedar Rapids entries (nodes 11243 to 11305), the City of Cedar Rapids Historic Markers pages, the Veterans Memorial Commission's pages, and the congregations' own pages for service times. Not checked: any interior, parking for any place, the Paramount's box office hours (its site did not answer), the courthouse's office hours, St. Patrick's Sunday Masses (its site refused; only the Saturday time, from Immaculate Conception's page, is given). The Savings Bank's material is given both ways: SAH Archipedia says rusticated stone, a Commons photograph shows red brick above stone. Red brick for six places is "?" (no picture or source read settles it).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Warde Hall, Mount Mercy University | Cedar Rapids, IA | Built by William Lightner's firm; the university's grotto pages give both 1923 and 1929 | A source for the building itself and its date |
| Coe College's older buildings | Cedar Rapids, IA | City marker: the first buildings are gone, the quad dates from the first half of the 20th century | Names and dates of the oldest halls; the 1950 chapel is in SAH Archipedia |
| Iowa Masonic Library's 1884 building | Cedar Rapids, IA | Wikipedia: the first Masonic library with its own building, 1884 | Whether any of it stands |
| Order of Railway Conductors building (Masonic Temple of 1897) | First Avenue and First Street NE, Cedar Rapids, IA | Search-result text quoting a Gazette column: the city bought it for urban renewal in 1967 | What stands on the corner now |
| Iowa Theater (Theatre Cedar Rapids) | Cedar Rapids, IA | City marker: 1928 Orpheum house by George L. Fisher, community theatre since 1983 | Address check and pin; not named in the video |
| Union Station | Cedar Rapids, IA | Named in the video, 1897 | Its fate (it is thought gone, not checked) |

## Tips
- The City of Cedar Rapids Historic Markers pages (`cedar-rapids.org/crn/<name>.php`, the list at `/crn/index.php`) read in full with `page.py --all`; each holds a researched paragraph (architect, dates, demolition) for one building, and the plaque PDFs under `cms8.revize.com/revize/cedarrapids/CRN/plaque-pdf/` read too.
- The Gazette's history columns (`thegazette.com/?p=<n>`) open only the home page now, in `page.py` and the web fetch tool alike; their facts reach a session only through search-result text.
- SAH Archipedia's Cedar Rapids entries are nodes 11243 to 11305; reading the range with `page.py --all` lists every one with its type and style.
