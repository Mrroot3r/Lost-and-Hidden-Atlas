# jackson_mi_phpi: Michigan: old Jackson
state: Michigan
region: mi
date: 2026-11-28
places: 12
file: data_jackson_mi_phpi.py

## What this batch is
Twelve standing buildings in Jackson, Michigan, from one walk-through video of old Jackson buildings (Old World Exploration, "Old World Jackson Michigan"; the record is source/videos/20250919_-NTAzQ-wecY.md). Added: the First Congregational Church (1859-60), St. Paul's Episcopal Church (1850-52), the former First Baptist Church (1870-72, closed April 2026 and for sale), St. John the Evangelist Catholic Church (cornerstone 1856), the Michigan Theatre (1930), the Hayes Hotel (1926), the Otsego Hotel (1904), the Collins Manufacturing-Jackson Automobile Company complex (1895-1909), the old Michigan State Prison (Armory Arts Village), the Stone Post Office (1839), Jackson High School (1926-27) and the 1932-33 post office now fronting the Consumers Energy headquarters. The Carnegie library is already on the Atlas. Sources: Wikipedia read with wiki_raw.py, SAH Archipedia (Buildings of Michigan, MI-01-JA1 to JA14, read with page.py --all), National Register record pages through form.py, the Michigan Stained Glass Census, a WKAR report (March 2026) and the City of Jackson's news page; service times from the parishes' own pages. Not checked: anything on the ground; First Congregational's service times (its site draws them by script) and the Michigan Theatre's box-office hours (both hours='?'); who now owns the First Baptist building; whether the Hayes Hotel conversion is finished; parking (downtown lots and meters, ownership unknown, so no th= points). Pins: the prison pin is on the Armory Court address point, not on a building known to be the 1842 cell block; the 1933 post office pin is on the headquarters complex, of which the old post office is the west front; the Stone Post Office pin is Wikipedia's point, behind the North Jackson Street frontage.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Masonic Temple (City Center) | downtown Jackson, MI | The City of Jackson's news page (January 2025) says the former Masonic Temple, now City Center, was being renovated into a kitchen incubator and event space | Address, date, architect, a description |
| Union and Peoples National Bank (Jackson County Tower Building) | West Michigan Avenue, Jackson, MI | Web search results say a 1929 Albert Kahn bank tower; not opened | A source opened; whether it is the "Union Bank" of old postcards |
| Peoples National Bank Building | Jackson, MI (42.2473, -84.4057) | National Register 14000977, Wikipedia article exists | Not in the video; not read |
| Michigan Central Railroad Jackson Depot | 501 E. Michigan Ave., Jackson, MI | SAH Archipedia MI-01-JA4 (1872-73, Henry A. Gardner), National Register 02001504 | Not in the video; check whether already on the Atlas, then add |
| St. Mary Star of the Sea Church | 120 E. Wesley St., Jackson, MI | SAH Archipedia MI-01-JA6 (1923-26, Frederick H. Spier) | Not in the video; service times |
| The Ionia row houses | 509-519 W. Michigan Ave., Jackson, MI | SAH Archipedia MI-01-JA9 (c. 1915, Ionia sandstone) | Not in the video |
| Ella Sharp Museum (Hillside Farm) | 3225 4th St., Jackson, MI | SAH Archipedia MI-01-JA12, National Register 72000622 | Not in the video; museum hours |

## Tips
- SAH Archipedia's Jackson entries are MI-01-JA1 to JA14 at https://sah-archipedia.org/buildings/MI-01-JA<n>; page.py --all reads each in full.
- The Michigan State Historic Site marker PDFs on the DNR sites (www and www2 hosts) answered 404 for Jackson markers, and hmdb.org answered 403 to page.py.
- videos.py claim takes a video id that begins with a hyphen (-NTAzQ-wecY) without trouble; do not put "--" before it, or "--" is taken as the id.
- publish.sh stopped once because src/photos.json had changed on main; resync.sh then all.sh fixed it, as it says.
