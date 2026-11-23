# utica_peqx: New York: old downtown Utica
state: New York
region: mohw
date: 2026-11-23
places: 10
file: data_utica_peqx.py

## What this batch is
Ten standing places in Utica, New York, all from the names in one Old World Exploration video about the city (the record of every name is `source/videos/20230629_mMW3jm2B02w.md`; the video is a tip and nothing rests on it): the Savings Bank of Utica with its gold dome, the 1911 Central Fire Station, St. John's Catholic Church, the Oneida County Courthouse, Hotel Utica, the Olbiston apartments, the 1930 Utica Armory on Parkway East, the Masonic Home (Masonic Care Community) campus with its 1893 Tompkins chapel and Wiley Hall, the Soldiers' and Sailors' Monument in Oneida Square, and the Bagg's Square East Historic District (a lead row in notes/mohw_akpe.md, deleted). The video named 43 buildings: 7 were already on the Atlas, 4 are gone (Bagg's Tavern, the 1853 Upjohn City Hall, the Hotel Martin, the 1871 Opera House), 10 could not be found in any source read and 8 were not checked. Most facts come from the 2018 National Register nomination for the Downtown Genesee Street Historic District (a 242-page PDF at NPGallery with a text layer, read in the cached copy) and the 2017 nomination for Bagg's Square East; the rest from Wikipedia, the New York State Military Museum's armory pages, the Governor's 2024 release on the Olbiston, the Masonic Care Community's own pages and Mohawk Valley Museums' newspaper extracts on the monument. Pins are ArcGIS address points (Register point for the district, OpenStreetMap's Oneida Square for the monument), all looked at on the aerial and all on the building; the Masonic Home pin is on the main care buildings because the chapel could not be picked out. Not checked: St. John's service times (historicoldstjohnschurch.com refused both page.py and the web fetch tool), every interior, the courthouse's and the law library's public hours, whether casual visitors may walk the Masonic campus, and whether the Olbiston's Register listing date is 2022 (the entry says only that it is listed). The courthouse is the narrator's "old courthouse, no longer a courthouse" only as a likely match: the 1903–08 building is still a courthouse.

## Leads
Places you read about and could not finish. One row each. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Utica Free Academy (last building) | Kemble Street, Utica, NY | Wikipedia: the high school ran 1840–1990; its last building is now a nursing home; a WIBX report says its gym was offered for sale by the city | Which building and when it was built, from a source; a pin |
| Downtown Genesee Street Historic District | Utica, NY (Register 43.1007, -75.2327; 100002668) | The 2018 nomination describes every building, among them the 1897–98 Masonic Temple at 251 Genesee Street, the Fort Schuyler and New Century clubs and the 1950s YMCA | A district entry, and single entries for the best buildings not yet on the Atlas |
| Utica Trust and Deposit Company | Genesee Street, Utica, NY | Named in a banknote history; no building found | Which building it was and whether it stands |
| Kanatenah apartments | Utica, NY (spelling not confirmed) | Named in the video only | Any source |

## Tips
- The Downtown Genesee Street nomination (NPGallery asset 835149cd-a9aa-483a-952c-aeee4858abd1) is longer than page.py keeps even with -n 200000; search the cached copy in research/pages/ with a short Python search for "Property name:", which starts each building's entry with its address, date and architect.
- Many Utica buildings have no Wikipedia article (the Savings Bank, the Olbiston, St. John's, the Masonic Home); the district nomination is the best single source for the downtown ones.
- historicoldstjohnschurch.com answers 403 to page.py and to the web fetch tool; service times are only in Mass-time directories, which are not a source.
- hmdb.org answered 403 to page.py again on November 23, 2026 (Utica's Soldiers' and Sailors' Monument, marker 141426).
