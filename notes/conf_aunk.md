# conf_aunk: Cohoes, Watervliet and Waterford: what was left
state: New York
region: albco, conf
date: 2026-11-21
places: 8
file: data_conf_aunk.py

## What this batch is
Eight places in region `conf` (drawn at random by `choose.py --state ny`), which six earlier batches had already worked closely, so this batch is what was left, with two places just south of Watervliet in Colonie (Menands) filed under `albco`. Colonie: the Schuyler house site and the Old Schuyler Burying Ground at Schuyler Flatts Cultural Park (a separate entry from the existing African burial-ground pin), and the Troy Steel and Iron Company blast-furnace marker on the Empire State Trail (marker only; the island was filled for I-787). Watervliet: the North Reformed Dutch Church of 1839, now the Watervliet Historical Society, with the North Reformed and St. Patrick's Meneely bells at its steps. Cohoes: the 1915 School Street hydroelectric station and Lower Gatehouse (still working, view only), Enlarged Erie Lock 17 (the LiDAR shows the chamber under trees behind the houses; access left `view` because the owner of the ground was not found), the 1844 Egberts and Bailey finishing building at 300 Ontario Street, and a group pin for the Mohawk Street houses (Van Auken, Clarke, the 1849 Claxton building, 2-4 White Street). Waterford: the Button Fire Engine Works marker in Button Park. Sources: HMdb markers (read with `page.py`), Wikipedia (`wiki_raw.py`), the Town of Colonie parks page, the Erie Canalway heritage-award page, the Edison Tech Center, the Spindle City Historic Society's three 2023 brochures, and, through the web fetch tool, troyirish.org and the City of Watervliet historian page. Not checked: anything on the ground; the Watervliet museum hours come from a city page last changed in 2021; how many Schuyler gravestones remain and whether the house foundations show; current use of 300 Ontario Street; red brick for six of the eight. No parking point was given for four places, because the lots `parking.py` listed were on houses or not plain on the aerial; the Schuyler park lot is described from HMdb.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| James Roy Mills | Watervliet, NY (HMdb 226353, Broadway at Fifth Street, 42.71118, -73.70584) | HMdb: woolen mill begun 1835 on the hydraulic canal, eight buildings | Whether any mill building stands; ldsgenealogy.com's 1910 Watervliet history answered 403 |
| Canalside Store (Edwin Emery's) | Watervliet, NY (HMdb 276418, 600 Third Avenue, 42.71315, -73.70722) | HMdb: canal boats unloaded straight into the warehouse behind this building | A second source and a date |
| St. Brigid's Church | Watervliet, NY, 695 Fifth Avenue | troyirish.org: built 1850-51; The Evangelist: closed after the 2005 parish merger, school and hall sold | Whether the church still stands and who owns it |
| Original St. Patrick's church building | Watervliet, NY (23rd Street and Fourth Avenue) | troyirish.org: the first worship site "still stands", later church hall, school and Our Lady of Mount Carmel | Address and present use |
| Corporation Hall | Green Island, NY | Still only HMdb 256010; the village history page does not mention it | Which building it is |
| Cohoes Waterworks Pump House | Cohoes, NY (Harmony Mills district) | Spindle City brochure stop 12: begun 1857, still working, on an original Erie lock | Its position: `osmnear.py ... buildings -g pump` found nothing |

## Tips
- troyirish.org (Troy-area Irish parishes, building by building) answers 403 to `page.py`; the web fetch tool read it.
- menandsny.gov answers 403 to `page.py` with no archived copy; the Town of Colonie's parks page (`colonie.org/parks/parks/`) has Schuyler Flatts' hours, found by reading the cached page round "Schuyler Flatts Cultural Park has".
- Region `conf` is close to worked out: what is left is mostly single houses, markers and buildings with no source saying they stand.
