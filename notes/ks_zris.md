# ks_zris: Kansas: the west and south
state: Kansas
region: ks
date: 2026-11-23
places: 19
file: data_ks_zris.py

## What this batch is
Nineteen places spread over the parts of Kansas the Atlas had nothing in (it had 35, nearly all in the north-east and along I-70): the Dodge City Santa Fe Trail ruts, Wagon Bed Spring, the Mueller-Schmidt House, the Ness County Bank, the Pond Creek stage station at the Fort Wallace Museum, the old courthouses at Russell Springs, Tribune and Wichita, Wichita's old city hall museum, Carry Nation's house, the Fromme-Birney round barn, the Big Well, the Elk Falls truss bridge, the old Allen County jail, the Niotaze Methodist church, the Condon Bank in Coffeyville, Route 66's Rainbow Bridge, the Home on the Range cabin and the Shirley Opera House. Sources: Wikipedia read with wiki_raw.py, the Kansas Historical Society's register search (county pages), National Register forms (Old Sedgwick County Courthouse 71000327, Condon Bank 73000771), the managing bodies' pages (Fort Wallace Museum, Horace Greeley Museum, City of Iola, Wichita-Sedgwick County Historical Museum, Ness County Chamber, Ford County Historical Society, Coffeyville Historical Society), HMdb markers and the Kansas Sampler Foundation. Not checked: anything on the ground; hours for the Mueller-Schmidt House, the Butterfield Trail Museum, the Carry Nation Home and the Big Well (no readable page of their own); whether the Condon Bank still opens to callers (the NPS lesson that says so is undated); current use of the Old Sedgwick County Courthouse and the Shirley Opera House; who owns the ground at Wagon Bed Spring; whether the Niotaze church still holds services. The Home on the Range cabin pin is the Wikipedia coordinate; the cabin could not be picked out among the trees. Five pins were moved onto what the 2024 Kansas aerial shows (Greeley courthouse, round barn, Elk Falls bridge, Old Sedgwick courthouse, Rainbow Bridge). OpenStreetMap maps no parking lots near any of the rural places, so none has a th= point.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Herbert and Eliza Steele House | Lake Scott State Park, Scott County, KS | National Register 16000406, listed address restricted | A park page giving where it stands and when it opens |
| Old Gray County Courthouse and Cimarron Hotel | Cimarron, KS (37.806194, -100.348889) | Register list; courthouse is where the 1889 Battle of Cimarron was fought | Any source beyond the list row; owner and use |
| Grainfield Opera House | Grainfield, KS (39.1133, -100.4656) | Register 80001467 | Source text, current use |
| Santa Fe Trail, Ford County Segment 2 (Fowler's Ruts) | SW corner Ridge Rd and 129th Rd, near Ford, KS (37.659178, -99.69657) | Kansas Historical Society summary: swales and a spring on the Wet Route, Cooke's dragoons 1843 | Whether the public may walk it or see it from the road |
| Fort Dodge, Kansas Soldiers' Home | Fort Dodge, KS | State Register lists the cemetery; Junior Officers' Quarters on the National Register | Which fort buildings survive and visitor rules |

## Tips
- The Kansas Historical Society's register search sorts listings alphabetically across pages of ten; the county code is two letters (Ford FO, Sedgwick SG, Seward SW), and the summaries are long, so page.py --all piped through grep for the name works better than -g.
- Small Kansas counties have no Register list page of their own: "National Register of Historic Places listings in Kansas" (wiki_raw.py --rows) holds them all, 184 rows, with coordinates.
- photo_find.py look on three places took more than two minutes; run it in the background from the start.
