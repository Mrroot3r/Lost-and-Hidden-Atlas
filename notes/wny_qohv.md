# wny_qohv: Elmira, NY: City Hall, churches, the college, the reformatory and the Erie station
state: New York
region: wny
date: 2026-11-24
places: 8
file: data_wny_qohv.py

## What this batch is
Eight places in Elmira, New York, taken from the building names in one Old World Exploration video (the record is `source/videos/20250328_htY1Adrqh3E.md`; the video is a list of names only, never a source). Added: Elmira City Hall, Park Church, the Erste Deutsche Evangelische Kirche (a lead in `notes/wny_rsxe.md`, row deleted), St. Patrick's Church with its 1880s school and convent, Ss. Peter and Paul Church (closed 2021), the Elmira College Old Campus, the Elmira Reformatory (Elmira Correctional Facility, view only) and the former Erie Railroad station. Sources: Wikipedia as raw text, the Chemung County Historical Society blog, the Most Holy Name of Jesus parish page (Mass times for St. Patrick's), the Churches of Rochester pages for St. Patrick and Ss. Peter and Paul, railfanguides.us and elmira-ny.com for the Erie station, and the Library of Congress record of its HAER survey. Six names were already on the Atlas from `wny_rsxe`. Gone: the 1888 armory (demolished 2010), the Mozart Theatre (1967), the Lyceum, the Centenary Methodist church, the Lehigh Valley depot and the 1861 Free Academy. Not checked: service times for Park Church and the Erste Deutsche Kirche (firstuc.org answered 403, and it was not certain that site is this church), the City Hall's public hours, present use of the Erie station and of Ss. Peter and Paul, and the Erie station's building date (marked mixed). Red brick was set only where a Commons picture was looked at (City Hall no, St. Patrick's yes); the rest are '?'. All pins were looked at on the aerial; all are on a building.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Grace Episcopal Church | Elmira, NY, 375 West Church Street (ArcGIS 42.08803, -76.81362) | An HMdb marker stands at West Church and Davis Streets; an organ listing gives 1904 or 1906 | A readable source for the building's date and history (HMdb answered 403) |
| U.S. Post Office and Courthouse (1903) | Elmira, NY, Church Street at Clemens Center Parkway | Contributing building of the Elmira Civic Historic District (Wikipedia); a 2004 photo caption calls it the former post office and court house | Whether it stands and what it is now |
| Central Fire Station (1890) | Elmira, NY, East Market Street opposite Exchange Place | Built 1890, headquarters until 1964 (Chemung County Historical Society blog) | Whether the 1890 building stands |
| Webber house ("the Castle") | Elmira, NY, 615 Columbia Street | 1870s mansard house in the Clinton–Columbia Historic District, sold in 2021 (search results only) | A source opened in full; owner and present state |

## Tips
- HMdb.org, firstuc.org, loc.gov item pages and the Federal Judicial Center answered 403 or came back drawn by script to `page.py`; the Library of Congress JSON (`https://www.loc.gov/item/<id>/?fo=json`) does answer, but holds little more than the title.
- The Churches of Rochester site (served here as packetduck.duckdns.org) has a page for each Catholic church in the Rochester diocese, Elmira included, with dates, status and pastors.
- elmiracatholic.org lists Mass times for both remaining Elmira Catholic churches on its home page.
- `photo_find.py new` did not offer St. Patrick's (it links only a Register list page); `look` by id found a good Commons picture.
