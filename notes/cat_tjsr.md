# cat_tjsr: Northern Delaware County: Bovina, Kortright, Stamford and Hobart
state: New York
region: cat, scho
date: 2026-11-22
places: 20
file: data_cat_tjsr.py

## What this batch is
Twenty places in northern and eastern Delaware County, New York (region `cat`, drawn at random by `choose.py --state ny`, which offered Bovina Center, New Kingston and Onteora Park; the Atlas had five places within 15 km of Bovina Center), with the Parker 13-sided barn just over the line in Jefferson, Schoharie County (`scho`). Bovina: the Bovina Center hamlet (pin on the 1849 United Presbyterian church; library in the 1893 schoolhouse, the old museum closed since 2016 per the Daily Star), the 1849 Maynard School (town-owned, view only), and St. James' Church, Lake Delaware (Cram, 1922–1924, brown shale). Bramley Mountain (NYC DEP Public Access Area): the abandoned bluestone quarry (area pin) and the 1950 fire tower returned in 2024. Kortright: the Bloomville Methodist "1800 Church", the Sheffield Farms creamery (first pasteurizer, 1892 per Wikipedia, 1893 per HMdb's filing), the West Kortright Centre in the 1850 church. Stamford and Hobart: St. Peter's (1801), the 1889 Masonic hall museum (Saturdays 1–4 in July and August), the Stamford depot on the Catskill Scenic Trail, Churchill Park, the Mount Utsayantha fire tower. Also the Davenport and North Harpersfield churches, New Kingston, the West Delhi church, the Frisbee House (DCHA) and St. John's, Delhi. Sources were read with `wiki_raw.py` and `page.py`: HMdb, the Pomeroy Foundation, the Bovina historian's blog, the Albany diocese's parish pages, the Hobart Historical Society, the Catskill Scenic Trail, the Friends of Bramley Mountain Fire Tower, the Catskill Mountain Club, NYC DEP's maps and list, the Middletown historical society, the Governor's March 2024 Register list, and the Davenport Register form. Not checked: service times for every church (none of the pages read gave one, except St. James' "weekly Sunday mass" with no time); the DCHA's hours (dcha-ny.org refuses `page.py`); the Bramley quarry's exact spot (pin is on the Quarry Trail); which North Harpersfield building is which; owners of the creamery and the North Harpersfield churches; interiors everywhere except where a source describes them.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| McArthur-Martin Hexadecagon Barn (update) | Bloomville, NY (Register point 42.37167, -74.78083) | 1883 sixteen-sided barn, 100 ft across (Wikipedia; Central Plan Dairy Barns form 64000542) | The Register point falls in an open field, and no round barn shows within 500 m on the leaf-off aerial (`look.py` at 500 m); its real spot, owner and road view |
| Harpersfield toll gate | NY 23, Harpersfield (HMdb 132518, 42.43715, -74.67886) | 1960 marker: Susquehanna Turnpike toll gate, keeper Alexander Dales 1845–1855 | Whether any toll house survives |
| Meridale Farms | NY 28 near Meredith (HMdb 247034) | F. W. Ayer's Jersey breeding farm with the Meredith Inn and creameries; the marker says two hill barns and the sale pavilion stood there | Whether anything is left to see |
| Bovina Museum | Bovina Center | 1850s tinsmith's shop, library from about 1917, museum from 1978; closed since 2016 for foundation repairs (Daily Star on yahoo.com) | Whether it has reopened, and its hours |

## Tips
- NPGallery's text route gave placeholders for every Delaware County form tried from 1973 to 2011; the 2017 Davenport form and the 2019 McNaught Farm form had text. The NARA copies (`s3.amazonaws.com/NARAprodstorage/...`) answered 403.
- NYC DEP's "open recreation areas" PDF (`nyc.gov/assets/dep/downloads/pdf/recreation/open-rec-areas-maps.pdf`) lists every watershed unit with a leading Y/N for Public Access Area (no permit), and reads with `page.py`.
- The Episcopal Diocese of Albany's parish pages (`albanyepiscopaldiocese.org/st-<name>-church-<town>-ny/`) give each parish's address and history but no service times.
- `photo_find.py` names its pics file after the workspace's letters (`pics_vnvf.py`), not the batch key.
