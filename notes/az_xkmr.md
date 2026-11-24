# az_xkmr: Arizona: Kingman, Tucson, Phoenix, Globe and the north
state: Arizona
region: az
date: 2026-11-24
places: 9
file: data_az_xkmr.py

## What this batch is
Nine places in Arizona's emptiest ground: Kingman (Bonelli House, the 1908 power plant now the Route 66 Museum, Santa Fe 3759 in Locomotive Park), Tucson (San Xavier del Bac mission, the 1928 Pima County Courthouse), Phoenix (Rosson House), Globe (Besh-Ba-Gowah), Navajo National Monument (Betatakin) and Walnut Canyon. Facts come from Wikipedia articles read with wiki_raw.py and NPS pages read with page.py. Not checked: hours for most places (operators' pages 404, 403 or would not open; the Powerhouse row comes from a search result quoting the Mohave Museum page and is marked mixed), fees, parking, interiors, brick. Pins: Bonelli House sits under trees at Fifth and Spring (Wikipedia point; the geocoder's address point was 100 m west on the road); the Betatakin and Walnut Canyon pins mark visitor centres, not the dwellings.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Mohave County Courthouse and Jail | Kingman, AZ (35.1919, -114.0519) | On the Register (83002990); no Wikipedia article | A readable source for its history and visiting |
| Old Trails Bridge | Topock, AZ / Needles, CA (34.7158, -114.4847) | 1915-16 brace-ribbed arch, Route 66, now a pipeline bridge | Straddles the state line, so the pin check may refuse it; public access not checked |
| Peach Springs Trading Post | Peach Springs, AZ (35.5289, -113.4269) | 1928, Pueblo Revival, Hualapai Nation owned (Register 2003) | Whether visitors may go in; tribal permission |
| Kinishba Ruins | near Whiteriver, AZ (33.8147, -110.0544) | 600-room Mogollon pueblo, National Historic Landmark, White Mountain Apache | A page from the tribe saying visitors are welcome |
| Hayden Flour Mill | Tempe, AZ | Known only from memory | No source opened |

## Tips
- Arizona operator sites (mohavemuseum.org, sanxaviermission.org, heritagesquarephx.org) answered 404 or 403 to page.py; NPS pages (/planyourvisit/hours.htm, /basicinfo.htm, /guidedtours.htm) read fine, but the Walnut Canyon hours page came back with no hours in it.
- geo.py's address point for 430 East Spring Street, Kingman, was 100 m from the house the Register and Wikipedia place at Fifth and Spring; check street-address points against the aerial.
- Several Wikipedia titles are not the Register name (no article for "Mohave County Courthouse", "Hayden Flour Mill"); try the Register list rows first.
