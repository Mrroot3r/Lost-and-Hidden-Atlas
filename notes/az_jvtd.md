# az_jvtd: Arizona: Navajo County, Seligman, Camp Verde and two bridges
state: Arizona
region: az
date: 2026-11-28
places: 10
file: data_az_jvtd.py

## What this batch is
Ten Arizona places, drawn as the state with the fewest on the map (65 before): the Navajo County Courthouse, Wigwam Village #6, the Winslow Hubbell trading post warehouse, the Brigham City fort site, the Shumway School and the Snowflake Stake Academy (Navajo County), the Cottage Hotel at Seligman, Clear Creek Church at Camp Verde, and the Perkinsville and Verde River Sheep bridges (Yavapai County and the Tonto National Forest). Facts come from the National Register records and nomination forms (tools/form.py), Wikipedia articles read as raw text, one National Park Service page and web search results. Not checked: hours (none found on an operator page; all left '?'), present ownership and condition of Shumway School, Brigham City, Clear Creek Church and the Snowflake academy, and every interior. Pins were looked at on the aerial; Brigham City marks the fort area on city land. Pictures from Wikimedia Commons for seven places.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mayer Business Block (1902, Joseph Mayer's brick) | Mayer, AZ (34.39844, -112.23316) | Register form: panel-brick commercial block by the town founder | Present use and condition |
| UVX Smelter and Clemenceau town | Cottonwood, AZ (34.7326, -112.0267) | Register listings for the smelter, machine shop and company houses | Which survive and who owns them |
| Mingus Lookout Complex | Mingus Mountain, AZ (34.694, -112.128) | Listed fire tower complex, Prescott National Forest | Form not read |
| Kirkland Store | Kirkland, AZ (34.417, -112.710) | Register listing 98001215 | Form text did not extract |
| Snowflake and Taylor pioneer houses | Navajo County, AZ | Seven Register houses in Snowflake and four in Taylor | Not read |

## Tips
- Register forms with OCR text are slow to skim: grep the form for built|constructed|now first.
- Navajo County's winslowaz.gov pages returned almost no text through tools/page.py.
- The Wikipedia article for the Navajo County Courthouse does not exist under that title.
