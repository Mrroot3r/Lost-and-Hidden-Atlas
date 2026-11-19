# tx_goliad_vbqe: Texas: Goliad, Karnes and DeWitt counties
state: Texas
region: tx
date: 2026-11-19
places: 13
file: data_tx_goliad_vbqe.py

## What this batch is
A first pass over the Goliad country of South Texas (region `tx` drawn at random by `choose.py`; the Atlas had nothing within 40 km). Thirteen places: in Goliad County, Presidio La Bahía, Mission Espíritu Santo, the Mission Rosario ruins, the Fannin Memorial Monument (grave of the Goliad dead), the Goliad County Courthouse with its Hanging Tree, the Market House Museum, the Bull Durham painted wall ad on the square, and Fannin Battleground State Historic Site; in Karnes County, the 1873 Old Helena Courthouse, the Immaculate Conception Church at Panna Maria and the Karnes County Courthouse; in DeWitt County, the Eckhardt Stores in Yorktown and the DeWitt County Courthouse in Cuero. Sources were read in this session with `page.py` (Texas Historical Commission site and courthouse pages, Texas Parks and Wildlife's Goliad pages, Handbook of Texas entries, SAH Archipedia, National Register forms as PDFs from the THC Atlas, the Panna Maria visitors center, the Yorktown museum page, Austin Chronicle day-trip columns), HMdb nearby lists and marker pages, and `wiki_raw.py`. Not checked: hours of the Market House Museum, the Helena museum and the courthouses' insides; who owns the Fannin monument ground and the Market House (both marked look-only for that reason); whether the Yorktown museum is still in the Eckhardt building; whether the Karnes courthouse lost its stucco in the 2018 restoration. Mission Rosario: the Handbook says guided tours only, the Austin Chronicle says it is viewed from behind a fence; both are in the entry (`conf='mixed'`). Presidio La Bahía: Wikipedia says the Diocese of Victoria owns it, the THC runs it. Pins: three were moved from the aerial with `pix.py` (Espíritu Santo, the Fannin obelisk, the DeWitt courthouse); the Helena pin is on a building among trees that could not be told for certain to be the courthouse. Red brick: Presidio and Panna Maria settled from Wikipedia photographs (no); five left `?`. Nothing was checked on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Concrete College ruins | Concrete, DeWitt County, TX (HMdb marker 29.23823, -97.29307) | HMdb marker 125622: a school of 1865–1881; the stone walls were later crushed for road metal and "only rubble marks site today" | Where the rubble is, who owns it, any public way in |
| Old Riedel Dam (Riddleville) | Near Gillett, Karnes County, TX (marker 29.12662, -97.78887) | HMdb marker 235012: remains of an 1869 dam for Riedel's sawmill, gristmill and gin lie 250 yards west of the marker | Owner, whether the remains can be seen from a road, a pin on the dam |
| English-German School | 201 E. Newman (Register form) / Terrell St marker, Cuero, TX | Register form 88001978: 1877 one-story frame school, a house since 1911, owned by descendants | Left out as an ordinary private house; add only if a source shows more |
| Mission Refugio site | Refugio, TX (28.29403, -97.27755) | HMdb marker 240807 and a Register-listed monument by Our Lady of Refuge church | Whether anything of the mission is visible; probably only a monument |
| El Fuerte del Cibolo | About 2.5 mi N of the marker on Cibolo Creek, Karnes County (marker 29.011, -97.93414) | HMdb marker 121606: Spanish fort of 1734–37 and 1771–82 | Anything on the ground, owner, access |
| Zaragoza Birthplace | Next to Presidio La Bahía, Goliad | THC site, open daily 10–5, adult $5; TPWD calls the house a reconstruction | A source for when it was rebuilt; could be added with the presidio's access note |

## Tips
- In Texas the Texas Historical Commission's `thc.texas.gov/historic-sites/<name>` pages read in full with `page.py --all` and give hours and fees at the top; TPWD park overview pages (`tpwd.texas.gov/state-parks/<park>`) give hours and fees near the end of `page.py --all`, while the park's "fees-facilities" subpage returns almost nothing.
- Presidio La Bahía is now run by the THC (Wikipedia says the Catholic Diocese of Victoria owns it and does not name the THC); `presidiolabahia.org` did not answer.
- The THC Atlas holds Register forms as PDFs with a text layer at `https://atlas.thc.state.tx.us/NR/pdfs/<ref>/<ref>.pdf`, where NPGallery's text route gave only the placeholder (Eckhardt Stores, 76002020).
- HMdb nearby lists round four Texas county seats (5 miles) found most of this batch and the leads in one request each.
