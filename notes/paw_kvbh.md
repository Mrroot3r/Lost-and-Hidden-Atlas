# paw_kvbh: Erie, Pennsylvania
state: Pennsylvania
region: paw
date: 2026-11-23
places: 14
file: data_paw_kvbh.py

## What this batch is
The first places in the city of Erie, worked from one video walk-through of the city's old buildings (record: `source/videos/20240726_5bJVorRmgSs.md`; the video was a tip only). 14 places, all standing: the Erie Club (Reed mansion), the county courthouse, the Scott-Strong house at Gannon, the Old Custom House (Erie Art Museum), the 1899 public library now in the federal courthouse, St. Peter Cathedral, St. Patrick and St. Stanislaus churches, the Erie Trust Company Building (Renaissance Centre), Strong Vincent High School, Villa Maria Academy, Mercyhurst Old Main, Erie Cemetery and First Presbyterian Church of the Covenant. Facts come from SAH Archipedia (Buildings of Pennsylvania) pages read with `tools/page.py --all`, Wikipedia read with `wiki_raw.py`, the Diocese of Erie's parish pages and the churches', museum's and cemetery association's own pages. Pins are ArcGIS PointAddress matches, all on the building on the leaf-off aerial except Mercyhurst Old Main, which is an `area` pin on the campus. Not checked: parking everywhere (no public lots near most), interiors of the courthouse, library and Renaissance Centre, whether the cemetery's porters' lodge survives, and red brick for eight places (the sources give colours such as "soft orange" and "golden-orange Pompeian", left as `?`).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Erie Masonic Temple | Erie, PA, Eighth and Peach streets (Register list 42.1271, -80.0851; ref 100005518) | Listed on the National Register; a blog post and a property listing at 24-34 West 8th Street turned up in search | A Register form or register page read for dates and what it looks like |
| Pennsylvania Soldiers' and Sailors' Home | Erie, PA, 560 East Third Street | Opened 1886 on the site of the state's unused Marine Hospital (Erie County Historical Society blog); the Wayne Blockhouse of 1880 is on the grounds (state page) | Whether the old hospital building still stands; visiting rules for the blockhouse |
| St. Mary's Church and school | Erie, PA, 310 East Tenth Street | The 1866 school building is now the Studio at St. Mary's (Erie Reader, 2024) | The church itself: dates, whether it is still a church, a source |
| Downtown YMCA | Erie, PA | Search found Waymarking pages and an old-Erie blog only | A register or owner's page with its date |
| Pierre S. V. Hamot House, Dickson Tavern, Watson-Curtze Mansion, West 21st Street district | Erie, PA (Register list coordinates) | On the county Register list; not named in the video | Sources read and pins checked |

## Tips
- SAH Archipedia's Erie entries are numbered `https://sah-archipedia.org/buildings/PA-01-ER1` to about ER40 and read in full with `page.py --all`; the text sits between "Print Source" and "Writing Credits".
- The Diocese of Erie's parish pages (`eriercd.org/Parish<n>-<Name>.html`) give Mass times and the street address; St. Peter Cathedral is `Parish10317`, not the number a guess gives.
- erieartmuseum.org without `www` resets the connection; `https://www.erieartmuseum.org/visit` reads.
- A place linked to another building's Wikipedia article (a school district, a neighbouring cathedral) can take that article's photo: link it with a plain `L()` link, not `W()`.
