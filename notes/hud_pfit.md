# hud_pfit: Hudson, Greenport and the Columbia County hamlets: Olana, Warren Street, Van Hoesen House
state: New York
region: hud
date: 2026-11-22
places: 18
file: data_hud_pfit.py

## What this batch is
Eighteen places in Columbia County, New York (region `hud`, drawn at random by `choose.py --state ny`, which offered Ancramdale, Livingston and Philmont). The city of Hudson had only the lighthouse and Diamond Street, so most of the batch is there: Hudson Hall (the 1855 city hall and opera house), the Hudson Historic District along Warren Street to Promenade Hill, the 1911 post office with its Treasury Relief Art Project sculpture, the Hudson Almshouse, South Bay Mill, the 1874 station, and the Dr. Oliver Bronson House on prison land. Greenport: a full entry for Olana that replaces the thin `lm-olana` pin (`was=`). Claverack: the Jan Van Hoesen House (1715–1724), the Van Rensselaer Lower Manor House and the Cornelius S. Muller House. Philmont: High Falls and its 19th-century mill dam (Columbia Land Conservancy). Germantown: the 1740s Palatine parsonage. Clermont: Clarkson Chapel. Livingston: St. John's Evangelical Lutheran Church. Ancram: St. John's Lutheran Church with its horse sheds. Copake hamlet: the 1944 Memorial Clock and the Grange Hall. Sources were Wikipedia as raw text (`wiki_raw.py`, including `--rows` for the county Register list) and, through `page.py`, the Office of Parks and Olana Partnership pages, the Town of Germantown's calendar, Hill Country Observer (June 2025, Van Hoesen house), Untapped New York (February 2024, Bronson House), Uncovering New York, Scenic Hudson and The River Newsroom (High Falls). Not checked: hours for Hudson Hall (its own site answered 403), the post office lobby, the Hudson station waiting room and the Germantown parsonage (Wikipedia says Saturdays; the town's page only shows a monthly public meeting there); the Columbia Land Conservancy's High Falls page (403), so the falls' hours and rules are not checked; who owns the Almshouse since the library left in 2016; what South Bay Mill looks like now; whether the Bronson House can be seen from any public road; service times at the two Lutheran churches; the Copake Grange's present use. The High Falls pin is the parking lot, not the falls (the Commons photos named High Falls were taken about 600 m from the lot). St. John's Ancram and the Copake Grange are `prec='site'`: the building could not be told apart on the aerial. `check.py` warns that "Olana (Frederic Church's house ...)" and "German Reformed Sanctity Church Parsonage" read as churches: both are right as `inst` and `landmark`.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Richmond Hill | Livingston, NY (Register point 42.12667, -73.81972 falls in an open field) | Wikipedia: Walter Livingston's 1813–1814 brick Federal house with ten farm outbuildings, a Dutch barn among them | The house's true position (not seen at the Register point) and whether it shows from a road |
| Turtle House (Joab Center House) | Greenport, NY (Register point 42.26056, -73.76778 lands on a house in a modern subdivision) | Wikipedia: Federal house of about 1820 with a lozenge-shaped block and two semicircular porticoes; HABS drawings | Its street address, to be sure the pin is on the right house |
| Railway Steel Spring Company foundry and sand house | Hudson, NY (42.2519, -73.7985) | Register list: 1905, the last rail-related building near the station | Any source beyond the list line; owner |
| Hudson Community Theatre | Hudson, NY (OpenStreetMap ruin lead 42.24834, -73.7828) | Mapped as a ruin in OpenStreetMap | Any source at all |
| Copake Railroad Depot | Copake, NY (42.0952, -73.5443) | Register list (100009779, 2023) | A source on its date and use, and a picture |
| Jacob Rutsen Van Rensselaer House and Mill Complex | Claverack, NY (42.22111, -73.71083) | Wikipedia: brick house of about 1805 by Pierre Pharoux, an 18th-century mill, early waterworks; a private home | Whether the mill can be seen from NY 23 (not looked at on the aerial this session) |

## Tips
- `start.py` did not list `lm-olana` for "Philmont, New York" at 14 km (Olana is about 14.5 km away), and no Hudson-area start lists it unless the radius reaches Greenport; grep `build/sites.json` for `lm-` before writing up a big Hudson Valley site.
- clctrust.org (Columbia Land Conservancy) and hudsonhall.org answer 403 to `page.py`, and their archived copies could not be fetched; historichudson.org's old Bronson House page is 404.
- Web search results in this session gave titles and links only, no quoted text, so no hours could be taken from them.
- `photo_find.py look` gave positions with each candidate; the ones named "High Falls" were about 600 m from the lot, which roughly places the falls for a later pin fix.
