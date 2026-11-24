# ks_dgmn: Douglas County, Kansas (second pass)
state: Kansas
region: ks
date: 2026-11-24
places: 17
file: data_ks_dgmn.py

## What this batch is
Seventeen National Register buildings in Douglas County, Kansas, that the first pass (data_ks_kwud, ks_pmvt, ks_nrqf) did not reach: four Lawrence houses (Ludington, the Roberts "Castle", Blood, Priestly), Parmenter Hall and Case Library at Baker University, a Baldwin City school and the Quayle house, and country places round Vinland, Worden and Lecompton (a grange hall, a church, a Lutheran church and cemetery, a stone barn, two farmsteads, a country school, the empty Vermilya-Boener villa, the William Henry stone house and the Lewis-Crowder cemetery). Facts come from National Register forms read as text from NPGallery with tools/page.py, the Kansas Historical Society's register summaries, and Lawrence Journal-World articles (2009, 2010, 2019, 2026). Each form is dated in the entry because it describes the building as it was when written (1971 to 2006). Nothing was seen on the ground and no owner's page was read. Not checked: whether the Castle (1307 Massachusetts) takes visitors now, whether Vinland Grange Hall is open, the present condition of the Vermilya-Boener house and the Stoebener barn, and any parking for the country places (all are private; each is marked view-only). Three entries (Clearfield School, Baldwin City School, Knud Anderson Farmstead) rest on a register summary alone, and say so. Lewis-Crowder Cemetery rests on two newspaper articles; its nomination was not read. Pins were looked at on the Kansas state aerial: Parmenter Hall, Case Library, Clearfield School, Baldwin City School and Stony Point church were moved onto the building (Parmenter Hall was first moved onto the wrong building, then put back after a Commons photograph and the roof shape settled it); the Stoebener barn, Vinland Grange and the Lewis-Crowder graves could not be picked out and are `area` pins. Brick: Ludington and Blood are red brick by their forms, Priestly part brick, the stone and wood buildings no, three left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Elmwood Stock Farm Barn | Baldwin City vicinity, KS (38.8220, -95.3171) | Listed 2022 (reference 100007704) | No nomination text found on NPGallery; need a description |
| Sowers-Crawford Farms Historic District | Overbrook vicinity, KS (38.7536, -95.3861) | Listed 2022 (100009424) | No description read |
| John and Anna O'Sullivan Farmstead | Overbrook, KS (38.8418, -95.4820) | Listed (100002623) | No description read |
| Kansas Homestead of Thomas McQuillan | Baldwin City vicinity, KS (38.7605, -95.2566) | Listed (100006683); has a Wikipedia article | Article title not found; nomination not read |
| Winter School No. 70 | Lecompton vicinity, KS (39.0006, -95.3645) | Country school, listed (100005947) | Description and access not read |
| Marion Springs School | Baldwin City, KS (38.7840, -95.3349) | 1950s Modern consolidated school, listed 2018 | Not read beyond the summary; not an obvious draw |
| English Lutheran Church, First Presbyterian, First Methodist Episcopal | Lawrence, KS | Listed 2019 to 2022 | Nominations of the 100xxxxx numbers have no text on NPGallery; need KHS PDFs |
| Pilla House (1874) and John Brender House | Eudora, KS | Queen Anne (Pilla) and Second Empire (Brender) houses | Descriptions not read |

## Tips
- NPGallery's text for a 1970s to 2006 form opens with `https://npgallery.nps.gov/NRHP/GetAsset/NRHP/<number>_text`; forms with numbers starting 100 (listed after 2016) have no text there. The Kansas Historical Society keeps those as PDFs under `/resource/national_register/nominationsNRDB/`, and a web search for the name finds the link.
- `page.py` with no pattern shows only a few lines of a form; use `--all -n 400000` and cut out Section 7 and Section 8 yourself.
- The Commons photo finder's distances are a check on the pin: a 130 m gap on a campus building meant either the register point or Commons was off, and a look at the photograph against the aerial settled which.
- app_smoke.js could not reach its own local server in this session; no app change was made, so it was not needed.
