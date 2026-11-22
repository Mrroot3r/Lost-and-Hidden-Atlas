# troy_wwot: Troy: the River Street collar factories and other works
state: New York
region: troy
date: 2026-11-22
places: 11
file: data_troy_wwot.py

## What this batch is
Eleven standing industrial and Register buildings in Troy that earlier Troy batches left as leads (region `troy`, drawn at random by `choose.py --state ny`). The River Street factory corridor north of downtown, south to north: the Cluett, Peabody & Co. factory (Hedley Park Place, 1917, the only concrete one), the Fitzgerald Brothers brewery bottling works (1892, 1911, 1955), the Miller, Hall & Hartwell collar factory and its 1915 box factory (Flanigan Square), the Wilbur, Campbell, Stephens factory (Tapestry on the Hudson), the Van Zandt, Jacobs factory (Arthaus Hudson), the William Connors paint works (the corridor's last water-power remains) and the Searle, Gardner factory (Collar Factory Lofts, rebuilt after the 2019 fire). South of downtown: the International Shirt and Collar Company building (the 1876 Conkey malt house) and the Neemes Foundry (1886, whose name is on most of Troy's old manhole covers). In Lansingburgh: the old Catholic Central High School, built in 1947 as Cluett, Peabody's textile research laboratory, and the Jacob H. Patten House with its blacksmith's carriage house. Sources: National Register forms read as text from NPGallery with `page.py` (the 2014–2017 forms are there; forms from 2018 on are not), the Hudson Mohawk Industrial Gateway's textile-factory article (updated June 2020) and its manhole-cover page, the Governor's office releases on the December 2023, March 2024 and June 2024 nominations and on Flanigan Square, historypointer.com for the Register addresses (its pages are drawn by script, but `page.py --all` prints the address line), Wikipedia raw text, and news items on 701 River Street (2021), Catholic Central (2023) and the Fitzgerald plant (undated). All pins are ArcGIS PointAddress or OpenStreetMap building points and all sit on the building on the leaf-off aerial. Not checked: present uses after 2020 for most of them (Connors, Fitzgerald, Neemes, Catholic Central, the 558 River Street box factory), interiors, parking rules (no public lot found; street parking said "where signs allow"), and the founding year of the Neemes firm and the build year of two collar factories, where sources disagree (both given, `conf='mixed'`). Red brick is from the forms' own words for two factories and the Commons photograph for one; the rest are `'?'`. Pictures: two found (International Shirt and Collar, Neemes Foundry), nine none.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Whalen Bottling Plant | Troy, NY (Register list 42.7212, -73.6905; NRHP 100013038) | Register list only; historypointer has no page for it | Any description; NPGallery has no form for listings this new |
| St. Peter's Church | Troy, NY (Commons photographs 138 m from 500 River Street) | Commons caption: parish incorporated 1826 or 1827; red brick Gothic church in the photo | A parish or diocese page, the address and service times; not on the Atlas |
| Cluett, Peabody power boiler house | Troy, NY (431-433 River Street, listed with the factory in 2025, NRHP 100012135) | historypointer record only | Which building it is; the state's form PDF answered 404 |
| Thomas S. and Mary Kate Fagan House; Corliss Park and Griswold Heights districts | Troy, NY (NRHP 100009782, 100009935, 100009936) | Governor's office, December 2023: Corliss Park (1952) and Griswold Heights (1950) were the Troy Housing Authority's first two projects | The Fagan house's story; whether the housing districts are worth a pin |

## Tips
- NPGallery's `_text` address still serves Register forms up to about 2017 (reference numbers like 14000009, 100000648); for 2018 and later (100003629 worked, 1000096xx and later did not) it returns an 893-character page. For those, the Governor's office release that announced the nomination has a paragraph on each property: search "governor.ny.gov nominations State and National Registers" with the property name.
- historypointer.com pages are "drawn by script" by `page.py`'s test, but `page.py --all -n 600` still prints the address and listing date.
- The Hudson Mohawk Industrial Gateway (`hudsonmohawkgateway.org`) has short, sourced articles on Troy's textile factories and foundries, with present uses as of 2020.
