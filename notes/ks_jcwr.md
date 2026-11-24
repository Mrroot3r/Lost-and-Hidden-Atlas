# ks_jcwr: Johnson County, Kansas, third pass
state: Kansas
region: ks
date: 2026-11-24
places: 10
file: data_ks_jcwr.py

## What this batch is
Ten places in Johnson County, Kansas (Shawnee, Overland Park, Merriam, Mission Hills, Westwood Hills, Gardner and Spring Hill), taken from the leads two earlier Johnson County batches (ks_dvmh, ks_hqwz) left behind. The Atlas had 12 places within 12 km of Olathe, and has 37 within 12 km of Shawnee counting this batch's seven that fall there (the count before was not taken). Sources: the Kansas Historical Society's Johnson County register pages (read with curl), the National Register forms for Mt. Pleasant (text) and Virginia School (read as page images, because it is a scan), Wikipedia (Campbell Dome House, Horn-Vincent-Russell Estate, Westwood Hills), and a Johnson County news page. Not checked: the inside of anything, hours, which exact building is the barn at the two barn pins (the register gives only an address; each pin sits on the barn seen on the aerial, a guess), whether the Virginia School has been restored as planned, parking at Mt. Pleasant. Most entries are private houses or farms and are `view` only. Westwood Hills and Broadmoor are whole neighbourhoods listed as districts; they are thin on what to see. Pictures: Virginia School, Walker House and Loomis from Wikimedia Commons; Westwood Hills, Broadmoor (only a street sign), the barns and Mt. Pleasant have none.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Shawnee Indian Cemetery | 10825 W. 59th Terrace, Shawnee, KS (39.0210, -94.7121 per county map, from the form) | National Register 2022 form read: half an acre, Shawnee burials from 1825 to 1870, earliest marker 1837, a place the Shawnee Tribe declared sacred in 2020, fenced among houses | Left out on purpose; add only if the tribe or the state manager invites visitors on a page of their own |
| Hodges House and Hyer House (Hycrest) | Olathe, KS (425 S. Harrison; 505 E. Cedar) | State Register houses of 1990 (Tudor Revival) and 1984 (Bungalow/Craftsman) | The forms are scans; no other source found (a web search found nothing on Hycrest) |
| Dutton-Thomas-Soule Farm; Edgerton Grange Hall | DeSoto vicinity and Edgerton, KS | State Register 2006 and 1998 | Forms are scans; no source beyond the register summary |

## Tips
- The Kansas register search page can be read whole with curl and a few lines of Python (strip the tags); page.py cuts it. The same page gives each listing's summary and the address of its nomination PDF (`/resource/national_register/nominationsNRDB/...pdf`).
- Many Johnson County forms are scans with no text. `pdftoppm -r 100 -f N -l N` makes a page image the session can look at, which worked for the Virginia School; there is no OCR here.
- A web search for a registered house often finds nothing but real-estate pages; the register summary is then the only source.
- Johnson County's news page (jocogov.org/newsroom) is where the Virginia School's "no regular hours" statement came from.
