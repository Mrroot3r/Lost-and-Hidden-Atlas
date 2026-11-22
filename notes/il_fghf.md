# il_fghf: Illinois: Galena to Cairo
state: Illinois
region: il
date: 2026-11-22
places: 19
file: data_il_fghf.py

## What this batch is
A first statewide scatter for Illinois, claimed with `choose.py --thinnest` when Illinois had 23 places (now 42). Nineteen places from Galena to Cairo: in the north, the Grant Home and Galena's Main Street, Lockport and the Gaylord Building on the I&M Canal, and in Chicago Pullman, Glessner House and the Water Tower; in the middle, the Bishop Hill colony, Nauvoo, Jubilee College and the Metamora and Mount Pulaski courthouses; in the French colonial south-west, the Holy Family log church and the Cahokia Courthouse, Fort de Chartres and the Pierre Menard House; and in the far south, the Illinois Iron Furnace, the Shawneetown bank, Magnolia Manor and the Cairo district. Facts come from Wikipedia read as raw text (`wiki_raw.py`), the National Park Service's Pullman basic-information page, the Forest Service's Illinois Iron Furnace page, Glessner House's own tour and closed-days pages, the Diocese of Belleville's parish directory and the Institute of Christ the King's Cahokia page (log church Mass), and one Southeast Missourian article on Magnolia Manor. Not checked: the hours of every Illinois state historic site (Cahokia Courthouse, Fort de Chartres, Pierre Menard, Mount Pulaski, Metamora, Jubilee College, Grant Home, Bishop Hill, Shawneetown Bank), because the state's site pages could not be read (see Tips); they carry `hours='?'`. Also not checked: Magnolia Manor's and the Water Tower gallery's hours, which Nauvoo buildings open, which Cairo district buildings still stand, and every interior. Pins were looked at on the aerial; the Jubilee College pin is on the one large building in the clearing, taken to be the college building without a source saying so, and the Mount Pulaski pin is on the HMdb markers at the courthouse, which is under trees on the aerial. Parking is given only for Fort de Chartres. Brick: some is from the article text (Magnolia Manor, Mount Pulaski, Galena's Main Street, Pullman, the Shawneetown bank), the rest '?' or 'no' from the stated material.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Fort Massac | Metropolis, IL | Wikipedia: French fort of 1757, rebuilt 1794; a reconstruction of 2002 and a museum stand on the site, in Fort Massac State Park | Only a reconstruction stands; an access page and what original traces show were not read |
| Postville Courthouse | Lincoln, IL | Wikipedia: a 1953 replica of the 1840 courthouse, the original moved to Greenfield Village, Michigan | A replica; left out for that reason |
| Old Market House | Galena, IL (42.41583, -90.4275) | Wikipedia: brick Greek Revival market and city hall of 1845, a state historic site, now the welcome centre | Mentioned inside the Galena entry; could be a place of its own with hours |
| Channahon locks (I&M Canal) | Channahon, IL (41.42417, -88.2275) | Channahon State Park lies at the canal; the Wikipedia article read says nothing of the locks | A source for the locks and locktender's house |
| Kaskaskia and the Kaskaskia Bell | Kaskaskia, IL | Named in the Fort de Chartres article as part of the French Colonial district | Not read |

## Tips
- The Illinois DNR historic-sites pages (`dnrhistoric.illinois.gov/experience/sites/...`) answer every address with the Albany Mounds page (its content fragment is the default), so `page.py` cannot read any site's hours; web searches gave titles only, no quoted text. A future session might try the hours through a phone call note or a newer archived copy.
- `photo_find.py look` on three places took about eight minutes because of Commons' limit; start it in the background before doing anything else.
- `publish.sh` stopped once because `photo_find.py` changed on main during the session; `resync.sh` fixed it in one go, but leaves a local branch of the first name behind, so publish to a new branch name.
- HMdb's nearby list gave the Mount Pulaski courthouse position when the Register coordinate fell on a house.
