# mohawk_astk: Montgomery County: Canajoharie, Fort Plain, Stone Arabia, Fonda, Auriesville
state: New York
region: mohawk
date: 2026-11-20
places: 16
file: data_mohawk_astk.py

## What this batch is
Sixteen places in Montgomery County west of Amsterdam, where the Atlas had nothing between Fonda and St. Johnsville: Fort Plain's museum on the Revolutionary fort hill and the Otsquago Creek aqueduct walls; the 1770 Palatine Church; the 1788 Reformed and 1792 Lutheran churches at Stone Arabia; the Van Alstyne Homestead, the Arkell Museum and the Canajoharie district (with the Shaper quarry and the cleared Beech-Nut site); the Frey house and Fort Frey marker at Palatine Bridge; the 1836 courthouse at Fonda (the county archives); the Coliseum at the Auriesville shrine; the Fultonville, Glen and Nelliston districts; the Ames Academy; the First Baptist Church at Charleston. Mostly standing places; the aqueduct is the one ruin. Sources: Wikipedia as raw text, the Montgomery County Register list (`wiki_raw.py --rows`), HMdb marker pages (nearby lists at five village centres), the county historian's articles and contact page, fortplainmuseum.com, the Town of Minden, the Journal of the American Revolution, the shrine's FAQ and calendar, OSV News, WAMC, mohawkvalleymuseums.us and the county tourism listings, all through `page.py`. Not checked: anything on the ground; interiors (except Trinity Lutheran, from the county historian); the Arkell Museum's hours (its site resets every connection); the Van Alstyne Homestead's hours (only a 2015-era tourism listing); service times for Trinity Lutheran; who owns the Palatine Church and the Reformed church; parking at most rural places. Pins for the Palatine Church, the Frey house, the Ames Academy and the First Baptist Church are Register coordinates that the aerial did not settle onto one building (`prec='site'`, said in the pin notes). Register forms for these listings are placeholders on NPGallery and were not read.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Palatine Bridge Freight House | Palatine Bridge, NY (Register point 42.91, -74.56639, which falls in the Mohawk) | Wikipedia and the county tourism page: a 300-foot limestone freight house of the mid-1850s, listed 1973 | A 600 m aerial (look.py) showed no 300-foot building along the tracks near the point, and OpenStreetMap maps none; whether it still stands and where |
| Webster Wagner House | Palatine Bridge, NY (Register 42.91083, -74.56944; state marker at NY 5 and Tilton Road, HMdb 63091) | Wikipedia: 1876 house by Horatio Nelson White for the sleeping-car maker, "a victim of demolition by neglect"; hudsonvalleyruins.org (undated): front porch collapsed and a demolition permit issued; mohawkvalleycollective.com: its remains sold at auction | Whether anything stands; add as `gone` with the marker if a series wants it |
| Little Red Schoolhouse (Plank Road school) | Fonda-Fultonville school campus, Cemetery Street, Fonda | County historian (2007): the District 7 school of before 1870, moved from NY 30A and Old Trail Road in 1973, restored as a museum dedicated in 1985 | A position and a current source for opening |
| Canajoharie Gorge and pothole, Wintergreen Park | Canajoharie, Wintergreen Park Road | HMdb: a glacial pothole over ten feet deep; Clio entry by the county historian (draft) | Any built remains in the gorge; it is a natural site otherwise |
| Fort Plain Conservation Area and the fort's earthworks | Fort Plain (OSM fort point 42.93912, -74.63221) | Journal of the American Revolution: excavated blockhouse site, spring, trench remnants on the museum grounds | A trail map or positions for each, to pin them separately from the museum |
| Currytown Reformed Church | Root, NY 162 (HMdb 41375: 42.85952, -74.46943) | State marker: congregation organized 1790, first in Jacob Dievendorf's barn | Whether the building stands and its date |

## Tips
- `publish.sh` stopped once because two other batches merged while this session worked (about ten minutes); `resync.sh` then a rebuild fixed it cleanly.
- The county historian's articles (montgomerycountyny.gov/web/sites/departments/historian/articles.asp) are a good, dated source for Montgomery County; the poor house article places the 1828 county farm on the grounds of the present jail on NY 5S, so nothing is left to see there.
- Register coordinates in this county were off by 40 to 300 m for several rural listings (one in the river); look at each.
