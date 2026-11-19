# cat_fpix: Western Delaware County, NY: Walton, Franklin, Sidney, Deposit and the Cannonsville hamlets
state: New York
region: cat
date: 2026-11-19
places: 14
file: data_cat_fpix.py

## What this batch is
Fourteen places in western Delaware County, New York, with one over the line in Sullivan County (region `cat`, drawn at random by `choose.py --state ny`, which offered Narrowsburg, Walton and Tannersville; the Atlas had four places within 25 km of Walton, and `cat_qazp` had worked the eastern half of the county). Walton: the two armories side by side (the 1886 Grange hall and Isaac Perry's 1896 castle armory, now the Castle on the Delaware event venue), the First Congregational Church (1840, 1881 glass), Christ Episcopal Church (1832) and the 1914 Walton Theatre with the Gardiner Place district. One-room schools: Common School 32 at Trout Creek (senior centre), the Hamden District No. 1 Schoolhouse Museum (1859, town-owned, open May to October) and Rock Valley School. Franklin: the empty 1856–57 Stone Hall of the Delaware Literary Institute. Sidney: Pioneer Cemetery (from about 1787) and the 1808 church beside it. Deposit: Lawrence Valk's 1880 First Presbyterian Church with its intact auditorium interior. Hancock: the Hotel Delaware at East Branch and Lordville Presbyterian Church. The drowned Cannonsville hamlets (panels at a pull-off on the shore) and the 1892 Hankins stone arch. Sources: Wikipedia as raw text (`wiki_raw.py`, the county Register list), five Register forms through NPGallery (armory, Walton Congregational, Trout Creek, Hamden, Deposit), HMdb nearby lists round Walton, Deposit, Hancock, Sidney and Franklin, and through `page.py` the state military museum, castleonthedelaware.com, Cinema Treasures, Clio, Upstater, the Town of Franklin's Stone Hall page, Franklin Stage Company, I LOVE NY and the Catskill Watershed Corporation. Not checked: anything on the ground; service times for the churches; who owns the theatre, the Hotel Delaware, Lordville church, Rock Valley School, the Hankins bridge and Stone Hall; whether the Sidney cemetery may be walked into (so it is view); the Hamden museum's exact hours (I LOVE NY says weekends and one weekday, May to October). Dates that disagree are given both ways (armory 1895/1896/1897; Stone Hall 1855–56 or 1857; Christ Church 1832 or 1834). Pins: Lordville is an area pin on the road in the hamlet (the Register point was in woods); Trout Creek is the HMdb marker (site); Rock Valley and the Hotel Delaware are Register points not confirmed on the building. Red brick: only the Castle armory is settled from a photograph (yes); Walton Theatre, the Deposit church, Walton Congregational, the Hamden school and the Sidney church are `?`.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Amos Bristol Tavern | West Meredith, NY (Register point 42.34861, -75.01417 falls in woods south of the road) | c. 1800 plank-walled tavern, five bays, NRHP 2000 (Wikipedia) | Which house it is along the road (no address found), owner |
| Schoolhouse No. 5 (Upper Dunk Hill School) | Hamden, NY, 5942 Dunk Hill Road (42.26795, -75.08551) | 1857–58 one-room school, used to 1954, NRHP 2011 (Wikipedia; NPGallery has only the placeholder) | Owner, whether it can be seen or visited |
| West Delhi Presbyterian Church, Manse and Cemetery | West Delhi, NY (42.30011, -75.00702) | 1892 church, c. 1840 manse, settlement-era cemetery, NRHP 2008 (Wikipedia) | Use, access, a look at the pin |
| Oldest building in Deposit (former Rookery Tavern) | Deposit, NY, River Street (HMdb 92766, 42.06064, -75.41910, Broome County side) | Marker: built 1799, a tavern 1800–1870 | Any source beyond the one-line marker; owner |
| Hankins and Long Eddy bluestone and acid-factory sites | Upper Delaware, Sullivan and Delaware counties | HMdb Long Eddy markers (Bluestone Quarries 122006, Long Eddy Industry 121978); dcnyhistory.org has acid-factory pages | A quarry or factory ruin on public land with a source |
| Sidney Historic District archaeological site | Sidney, NY | Register district includes a site of 850 BC–1400 AD (Wikipedia) | Probably address-restricted; leave unpinned unless a source says it may be visited |

## Tips
- NPGallery text forms worked for every Delaware County listing from 2011 on and returned the placeholder for every one from 1999–2008 tried (Christ Church Walton, Hotel Delaware, Lordville, Rock Valley, Bristol Tavern, Pioneer Cemetery).
- A short script over the cached form in `research/pages/` (find "Summary Paragraph", then grep brick/stained/owner) read five forms quickly without re-fetching.
- The Town of Franklin's site (`franklindelco-ny.gov/download_file/view/...`) has one-page PDFs on village landmarks; the Stone Hall one gave dates, size and present use.
- `publish.sh` stopped once because another batch (vtn_kfjq) merged; `resync.sh` then the batch time again worked first time.
