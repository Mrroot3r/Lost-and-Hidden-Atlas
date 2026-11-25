# kcmo_xesq: Excelsior Springs and Liberty, Missouri
state: Missouri
region: kcmo
date: 2026-11-24
places: 13
file: data_kcmo_xesq.py

## What this batch is
Thirteen standing buildings: nine in downtown Excelsior Springs (the Atlas had only the Hall of Waters, the Elms and a few others there) and four in Liberty's courthouse square and Jewell-Lightburne districts. Facts come from the National Register forms for the Excelsior Springs Hall of Waters Commercial East and West districts and the South Liberty Courthouse Square district (Missouri State Parks copies of the forms, read with page.py), Wikipedia read as raw text, and the Excelsior Springs Museum's own "Plan your visit" page (hours). Pins are address lookups checked on the Esri aerial; only the Clay County Courthouse needed moving (about 40 m north). Not checked: the present use and interior of every building except the museum; whether the 1914 post office is still a post office; whether the Frank Hughes library is now the county archives (only a sign in a Commons photograph says so); hours for the courthouse. Four buildings carry `conf='mixed'` because the form dates them only roughly. Brick: the post office and the library were set from the Commons photographs; Montgomery Ward, Arlington, Washington, Elks and Silvers are `?` because the form says only "brick".

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| The Oaks (rebuilt Snapp Hotel, 1913) | Excelsior Springs, MO | ACHP page: built 1913 after a fire, burned again in 1991, rebuilt 2005-2007 as 38 senior apartments. | A street address or a pin; the sources found give none. |
| Snapp's Hotel (117-119 South Street) and Ideal Hotel | Excelsior Springs, MO | Named in the West district form as notable hotels of the 1900s. | A source for their present state and pin check. |
| Arthur-Leonard and Dougherty-Prospect Heights districts | Liberty, MO | National Register districts, no coordinates or articles. | Forms and a reason to pick a building in each. |

## Tips
- The National Register forms for Missouri districts are not on NPGallery (placeholder page) but are on mostateparks.com: `https://mostateparks.com/sites/g/files/zuston361/files/media/pdf/2025/02/<name>-hd.pdf`, found by a web search limited to that site. `page.py --all -n 400000` reads a whole one; the text is a single line, so use grep -o with context.
- HMdb (hmdb.org) answered 403 to page.py for the nearby list from this session.
- `photo_find.py look` for five places takes several minutes and goes to the background by itself; its sheet files appear one by one, so they can be read before the command ends.
- `tools/app_smoke.js` printed an Error here (the Android www folder was not built); the pull request holds only place data, so it was not pursued.
