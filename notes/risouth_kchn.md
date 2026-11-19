# risouth_kchn: South County, Rhode Island (fourth pass)
state: Rhode Island
region: risouth
date: 2026-11-19
places: 16
file: data_risouth_kchn.py

## What this batch is
Sixteen places in Washington County (South County), drawn at random by `choose.py` (region `risouth`). The earlier Rhode Island passes took the forts and woodland ruins, so this one is mostly standing places: the Flying Horse Carousel, Watch Hill Lighthouse and the Babcock-Smith House in Westerly; Point Judith Lighthouse, the 1888 life-saving station (Coast Guard House) and the Windswept carriage-house ruin at Black Point in Narragansett; the Old Narragansett Church, Smith's Castle, the Gilbert Stuart Birthplace, Casey Farm, Plum Beach Lighthouse and the Six Principle Baptist meeting house in North Kingstown; Kingston station, the Perry-Carpenter grist mill and the Fayerweather blacksmith shop in South Kingstown; the Upper Rockville stone mill in Hopkinton. Wikipedia was read as raw text (`wiki_raw.py`, the county Register list with `--rows`); museum, fire-district, SAH Archipedia, magazine and lighthouse pages with `page.py`. Not checked: anything on the ground; red brick for eleven places (left `?`: Wikimedia answered 429 to `brick.py look`); Casey Farm hours (historicnewengland.org gives 403 to `page.py`); Old Narragansett Church visiting times; the carousel's and the Watch Hill museum's own hours pages; Coast Guard House restaurant hours. Point Judith: Visit Rhode Island says the grounds are open, New England Lighthouses says they are not; both are given. Perry-Carpenter mill dates disagree (1703 vs c.1716; moved 1825 vs before 1789); both given. The Windswept history rests on a 2020 blog post and an urbex site plus the RI Wild Plant Society trail write-up; DEM's own page was not read. Pins: six were left where the source put them but could not be matched to one building on the aerial (Babcock-Smith, Old Narragansett Church, Six Principle, Kingston station: prec site; Casey Farm: prec area); four were moved onto buildings seen on the aerial (carousel, Coast Guard House, Smith's Castle, Gilbert Stuart). No pin is only a trailhead.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Jireh Bull Blockhouse site | Middlebridge Road, Tower Hill, South Kingstown, RI (no coordinate in Wikipedia) | Wikipedia and the RI Historical Society: stone garrison house of 1657, burned December 15, 1675; mounds excavated by Norman Isham in 1917; RIHS acquired the site in 1925 | A coordinate, whether anything shows, and whether RIHS lets the public walk there |
| Kenyon's Grist Mill | Usquepaug, South Kingstown/Richmond, RI | Wikipedia (Usquepaug): corn-meal mill founded in the late 1600s, in a building of 1886 | kenyonsgristmill.com answers HTTP 999 to `page.py`; hours, a pin and what can be seen inside |
| Peace Dale mills and Hazard office building | Peace Dale, South Kingstown, RI (41.4514, -71.4961) | Wikipedia: stone weaving mill and stone office/store/hall building designed by Rowland Hazard II in 1856; woolen manufacture ended 1948 | Which buildings stand today and their use |
| Shannock mill village | Charlestown and Richmond, RI (41.44806, -71.64111) | Wikipedia: Carmichael plant and Columbia Narrow Fabrics mill complex, worker housing of the later 1800s | Present state of the mills and access |

## Tips
- `wiki_raw.py` saved the redirect page for "Babcock-Smith House" (hyphen) under the en-dash title's file name and printed nothing; ask for the en-dash title directly.
- `brick.py look` hit Wikimedia 429 on the first picture; in a short session leave brick at `?` rather than wait.
- `publish.sh` stopped twice in ten minutes because other batches merged; run resync, the batch time, `all.sh` and `publish.sh` in one shell command to keep the window short.
