# dallas_ggtn: Dallas, Texas: hotels, towers, courthouse, station and cathedral downtown
state: Texas
region: tx
date: 2026-11-26
places: 14
file: data_dallas_ggtn.py

## What this batch is
Fourteen standing buildings in Dallas (thirteen downtown, one on the Southern Methodist University campus in University Park), taken from the names in one video about the city's old buildings (the record is `source/videos/20250321_8NTzJ4YFJpo.md`; the video was a tip only, and nothing in the entries comes from it). The Atlas had nothing within 15 km before. Added: the Adolphus Hotel, the Magnolia Building, the Kirby (Busch) Building, the Santa Fe Terminal Buildings, the Old Red courthouse, the Dallas Municipal Building, the Davis Building (1926 Republic National Bank), the Neiman Marcus Building (the store closed September 30, 2026), the Scottish Rite Temple, Dallas Hall at SMU, Union Station, the Wilson Building, the Mercantile National Bank Building and the Cathedral Shrine of Our Lady of Guadalupe. Facts are from the Wikipedia articles (read with `wiki_raw.py`) and the Register list for Dallas County; the cathedral's weekday Mass times are from its own page; the Adolphus's own page names its guided history tours. Every pin is the ArcGIS PointAddress for the street address, and each landed on its building on the aerial. Not checked: hours for the two hotels, Union Station, the courts in Old Red and the Scottish Rite Temple (all `?` or none); the cathedral's Sunday Masses; which lot to park in (downtown parking is described in general terms only); whether SMU welcomes visitors on its grounds (Dallas Hall is `view`); red brick for most (only Old Red, Neiman Marcus, the Santa Fe buildings and the Mercantile tower are recorded, as `no`). Of the 68 names in the video, 14 are gone and 40 were not checked.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| First Methodist Episcopal Church, South | Dallas, TX | On the National Register (100013503); the Register list gives no coordinates and no article was found under that title | An article or the Register form, an address and a pin |
| Gaston Avenue Baptist Church (Gaston Oaks) | Dallas, TX | Named in the video as still standing in another use | Any source |
| Dallas Power & Light Building | Dallas, TX | Art Deco office building named in the video | An article title that answers; sources and a pin |
| Butler Brothers Building | Dallas, TX | Named in the video | Any source |
| First Presbyterian Church of Dallas | Dallas, TX | A domed classical church named in the video | Any source |

## Tips
- In Dallas, `geo.py` with the full address and ZIP gave a PointAddress on the building for all fourteen addresses tried.
- Several quick opensearch requests to the Wikipedia API brought "too many requests" at once; `wiki_raw.py` with exact titles kept working after a pause.
- `dallasscottishrite.org` gives no visiting hours; `oldred.org` did not answer.
