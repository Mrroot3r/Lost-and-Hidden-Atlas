# ks_kcks_hvmq: Kansas City, Kansas (third pass)
state: Kansas
region: ks
date: 2026-11-24
places: 9
file: data_ks_kcks_hvmq.py

## What this batch is
Nine places in Kansas City, Kansas (Strawberry Hill, the Northeast, Rosedale, Hanover Heights) and Bonner Springs: St. Augustine Hall (the old Mather Hall of Kansas City University), the Theodore Shafer House, the old Bonner Springs High School of 1918, the Old City Hall and Fire Headquarters, St. Mary's Church on Strawberry Hill, the George Rushton Baking Company building, the Judge Louis Gates House, the Cordell Meeks House and the Wyandotte High School building. Fewer than the 15 to 20 asked for. I looked first at Lee's Summit, Raytown and Grandview (the Atlas had 9 places within 12 km, but three earlier batches had taken the Register list there and what is left is small residential districts) and then at Olathe, Gardner, Paola and Leavenworth, whose Register lists are already on the map. The Wyandotte County list (Kansas Historical Society register search, pages 1 to 6) still had a few standing buildings no batch had written up.
Facts come from the National Register forms that opened with a text layer (St. Augustine Hall 71000336, Shafer House 00000108, Bonner Springs High School 02000761), Legends of Kansas, Clio (City Hall, St. Mary's, Rushton) and Wikipedia read as raw text. Pins: address lookups, checked on the 2024 state aerial; three fell in the street and were moved onto the building. Not checked: interiors, present owners and uses, hours (every place is view-only), the year Wyandotte High's building went up, and the architectural style of St. Mary's. Pictures: three from Commons by `photo_find.py`, plus a fourth for the Meeks House; none for St. Mary's or Rushton.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| White Church Memorial Church | 2200 N 85th St, Kansas City, KS | State Register 1982; Legends of Kansas says the congregation began as a Methodist mission among the Delaware in 1832 and a storm destroyed the first church in 1886 | Which building stands now and when it was built; whether the claim of the oldest church still in use in Kansas is sourced |
| Immanuel Baptist Church; First African Methodist Episcopal Church | Kansas City, KS (First AME: 1111 N 8th St per a search result) | National Register 2023 and 2024; no coordinates on Wikipedia's list | The forms (NPGallery serves only a placeholder image for these two) |
| Maunder House (616 N 9th St), Fairfax Hills district, Hanover Heights district, Huron Place | Kansas City, KS | State or National Register listings; the Huron Building itself was imploded in 1999 per a search result, so it is gone | Anything beyond the Society's one-line summaries |
| Shawnee Street Overpass | Kansas City, KS (39.0718, -94.6208) | 1932 overpass, rebuilt in 2005 (Wikipedia) | Left out: rebuilt |

## Tips
- Wikipedia's Wyandotte County Register list names articles ("article: Huron Building (Kansas City, Kansas)") that `wiki_raw.py` then reports as NO SUCH ARTICLE. Try the shorter title, or take the Clio entry (`theclio.com/entry/<number>`), which `page.py` reads in full.
- `page.py` on the Kansas Historical Society search pages returns one very long line; split it in Python on "Register Nomination Inventory Record" to get one block per property. Pages 6 to 8 are the same last page.
- A Register form on NPGallery whose `_text` address returns a PNG (893 characters) is a placeholder, so the form counts as not read (Immanuel Baptist, First AME).
- Wyandotte County's whole Register list is now on the map or in a Leads table; a further Kansas City, Kansas session should look to Clio's Kansas City, Kansas tours and the city's landmark list (wycokck.org returns 403 to `page.py`) instead.
