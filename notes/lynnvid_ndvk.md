# lynnvid_ndvk: Massachusetts: Lynn, buildings named in a video
state: Massachusetts
region: nshore
date: 2026-11-28
places: 10
file: data_lynnvid_ndvk.py

## What this batch is
Ten standing buildings in downtown Lynn and round Lynn Common, taken from the names in one video about the city (the video is a tip only; its record is source/videos/20250905_otor9uUxP0Q.md). Each was read in its National Register record and nomination form (tools/form.py: all ten forms had a text layer), its Wikipedia article (tools/wiki_raw.py) and, for the buildings on the Common and Market Street, SAH Archipedia. Added: the Lynn Armory, High Rock Tower and park, the Lynn Public Library, the Old Post Office Building, St. Stephen's Memorial Episcopal Church, the Vamp Building, the Mowers' Block, the former English High School, the Old Lynn High School and the Lynn Masonic Hall (built as the YMCA). Pins were checked on the 2023 MassGIS aerial; High Rock Tower was moved onto the tower, and three downtown pins that fall in the street or between buildings are marked site. Not checked: nothing on the ground; interiors; the library's hours (the city's page gives none; only a directory listed them) and St. Stephen's service times; whether the armory's planned conversion to veterans' housing has happened; the present use of the Masonic Hall. The forms and Wikipedia disagree on the armory's material (red brick with sandstone trim, against red sandstone) and the tower's year (1904, against 1905); both are given.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| St. Joseph's Church | Lynn, MA (115 Union Street) | A search summary gave a cornerstone of 1875 and dedication in 1885; the parish's own page gives no dates | A source that can be opened for its dates and fabric |
| Washington Street Baptist Church | Lynn, MA (Essex and Washington Streets) | The church's own page gives Sunday worship at 11 a.m.; a newspaper article (paywalled) is quoted in search results as giving 1874 for the building | A readable history of the building |
| Congregational church, 152 South Common Street | Lynn, MA | SAH Archipedia: brick church of 1871-1872 by John Stevens of Boston, vacant, its spire lost | Whether it still stands and who owns it |
| G.A.R. Hall and Museum | Lynn, MA (58 Andrew Street) | Register-listed (79000331); SAH Archipedia says the city keeps it as a museum with its original stencilling | Hours from the city's or the museum's page |

## Tips
- In Lynn the Register forms all had a text layer and read cleanly with form.py; SAH Archipedia's Lynn pages (sah-archipedia.org/node/13862 and 13867) read in full with page.py and name several more buildings.
- The Lynn Daily Item (itemlive.com) is paywalled: page.py gets only the first sentence.
- The Massachusetts Historical Commission's town reconnaissance report for Lynn (sec.state.ma.us .../town-reports/lyn.pdf) answers 404.
