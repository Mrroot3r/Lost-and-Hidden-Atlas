# wash_nthw: Glens Falls, with Queensbury and Hudson Falls
state: New York
region: wash
date: 2026-11-21
places: 18
file: data_wash_nthw.py

## What this batch is
Eighteen places, all standing or marked, in the city of Glens Falls (where the Atlas had nothing but the Feeder Canal ruins east of the city), Queensbury and Hudson Falls (Kingsbury). Region `wash`, drawn at random by `choose.py --state ny`. Glens Falls: the Hyde Collection and the Pruyn sisters' houses, the Chapman Museum (DeLong House), Crandall Public Library, Three Squares downtown with City Hall and the Empire Theatre (one area pin on City Park), the Queensbury Hotel, the Dr. James Ferguson Office, the 18th Separate Company Armory, the Shirt Factory, the Peyser and Morrison shirt building, the Bemis Eye Sanitarium with the Sherman House, First Presbyterian (Cram), the Church of the Messiah, the Society of Friends Hall and Glens Falls Cemetery. Queensbury: the Quaker Burying Ground and the Sanford and Asa Stower houses on Ridge Road. Hudson Falls: the village park with the 1873 Washington County courthouse, and the 1884 Moss Street School. Sources: Wikipedia as raw text, HMdb marker pages, GlensFalls.com's "History of Iconic Glens Falls Buildings" pages, historypointer.com for Register addresses, the NYS Military Museum armory page, the Preservation League and the Glens Falls Chronicle (Ferguson office), the Glens Falls Business Journal (courthouse, 2017). Hours from the Hyde Collection's, Crandall Library's and First Presbyterian's own pages. Pins are ArcGIS PointAddress results, each looked at on the leaf-off aerial; all are on the buildings except the Peyser and Morrison pin (on a large joined industrial block, `prec='site'`) and the Three Squares area pin. Not checked: the Chapman Museum's and the Shirt Factory's hours (their sites refused `page.py`, or showed none), the Church of the Messiah's service times, who owns or uses the armory (closed), the Society of Friends Hall and the Peyser building today, the courthouse's present use, the cemetery's owner and gate hours, and parking anywhere downtown. Nothing was seen on the ground. Red brick from Commons photographs for ten places; seven left '?'.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cooper's Cave overlook | Glens Falls / South Glens Falls, NY (HMdb 273709 and others, about 43.3058, -73.6407) | Seven HMdb panels at the viewing platform on the Route 9 bridge: the cave in The Last of the Mohicans, the South Glens Falls hydro project | A natural feature, not a building; add only if a literary or bridge series wants it, with who runs the platform and its season |
| Finch, Pruyn & Co. office and Hoopes House | Glens Falls, NY (Warren Street) | GlensFalls.com: Bigelow designed the Finch, Pruyn office as well as the three Pruyn sisters' houses (Glens Falls Multiple Resource Area) | A source for the office building itself and whether it can be seen from the street |
| St. Mary's Academy (St. Mary's – St. Alphonsus school) | Glens Falls, NY (Warren and Church streets, Register 84003400) | GlensFalls.com: Neogothic, the academy moved in in 1932; Wikipedia: a two-storey stained-glass window in the Great Hall | A working school; only worth adding with something on the building's history |
| Glens Falls Home for Aged Women; Glens Falls High School (old, 421-433 Glen Street) | Glens Falls, NY (Register 84003340, 84003335) | Wikipedia: 1903 Colonial Revival home, now a private residence of refuge; Potter's 1902-era high school is apartments | Whether either is worth a pin beyond being old |

## Tips
- GlensFalls.com's buildings pages (`glensfalls.com/history/buildings/<slug>/`) read in full with `page.py --all` and give address, architect, dates and present use for 16 downtown buildings; the slugs are in the links on the index page.
- `chapmanmuseum.org` and `queensburyny.gov` answer 403 to `page.py`; the archived copies it offers need the web fetch tool, which no one can approve in a scheduled run.
- A search for the Church of the Messiah's services turned up `messiahepiscopalchurch.cloversites.com`, which gives no town and mentions a Karen-language congregation: probably a namesake elsewhere, so it was not used.
- Crandall Library's opening hours are only in a JSON blob inside the page (`"days":{"Monday":[{"From":...`); `hours.py page` prints it as one long line.
- `check.py` refuses the tag `cemetery`; the series tag is `cemeteries`.
- The Queensbury Quaker Burying Ground's Wikipedia coordinate reads 44.33 for 43.33; the HMdb marker position is right.
