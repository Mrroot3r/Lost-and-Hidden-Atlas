# kcmo_jax_qwnb: Jackson County, Missouri: eleven more Register listings
state: Missouri
region: kcmo
date: 2026-11-26
places: 11
file: data_kcmo_jax_qwnb.py

## What this batch is
Eleven National Register listings in Jackson County, Missouri (nine in Kansas City, one in Independence), 1845 to 1927: a Santa Fe Trail merchant's brick house, a women's home, two factories, a soda works, a shop block, two schools, a warehouse, a convent school hall, an apartment block and an apartment hotel. Each was read from the Park Service record and the registration form (state copy, via tools/form.py). Photographs are Commons pictures named for each place, chosen from the candidate sheets. Pins are ArcGIS address points; the Register list points were 150 to 300 m off for most of them (the Vaccaro, ABC Storage, Bancroft and Barclay points fell on empty ground, a ramp and a road). Not checked: present use, owners, parking and whether any interior opens, for every place; ABC Storage and the Nettleton Home are `prec='area'` because the building could not be told apart on the aerial; the Atlas's pictures show Nettleton restored in 2015. Set aside: Bixby House, BMA Tower and Milo Apartments (modernist); R. A. Long House and Paseo YMCA (already on the Atlas).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Smith and Sons Manufacturing Company Building | 1400-26 Guinotte Ave, Kansas City (Register 07001290) | c. 1900 railway-equipment factory in the East Bottoms; form says vacant, rehabilitation planned; one aggregator says it left the Register in June 2025 | Whether it still stands (the aerial was not looked at) |
| Bailey Family Farm Historic District | Bailey and Ranson roads, Lee's Summit (06000537) | 15-acre farmstead, 1914-15 Prairie School house, barns; form read | The Register point and address point show houses and fields, no farmstead; location of the farm not found |
| Hiland Telephone Exchange Building | 1020 E 63rd St, Kansas City (05000373) | Park Service record only (1910, early commercial) | No form copy found at the state's address |

## Tips
- Missouri Register points in Jackson County are often 150 to 300 m off; `ArcGIS findAddressCandidates` on the form's street address lands on the building. Run it before the pin check.
- `tools/form.py` found the state's copy for all but a few of the 30 listings tried; the 2024 and later listings (numbers starting 1000) are not in the state's index yet.
