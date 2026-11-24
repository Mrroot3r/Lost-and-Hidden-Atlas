# bc_ymqk: British Columbia: a third scatter
state: British Columbia
region: bc
date: 2026-11-24
places: 11
file: data_bc_ymqk.py

## What this batch is
Eleven places in British Columbia, claimed with `choose.py --thinnest` (BC had 52): Kinsol Trestle and Craigflower Schoolhouse on Vancouver Island; Emily Carr House, Helmcken House and the E&N Roundhouse in Victoria; Hatley Castle in Colwood; the Hastings Mill store in Vancouver; Irving House in New Westminster; the Walhachin hall; the sternwheeler Sicamous at Penticton; and the ghost town of Anyox. Facts come from Wikipedia (`wiki_raw.py`), the Cowichan Valley Regional District's Kinsol page and the Hastings Mill museum's home page. The Canadian Register, Parks Canada, carrhouse.org, hatleypark.ca, pandosymission.ca, newwestmuseums.ca and the Sicamous site would not open, so every opening time in the batch is `hours='?'` with a note of what a web search quoted from the operator's page; none was read in full. Not checked: any interior, who owns the Roundhouse and whether it can be entered, what is left of the Walhachin flumes (the pin is the OpenStreetMap community hall), what is left at Anyox (the aerial shows only forest at the pin; boat only), the Kinsol parking point (the lot is on the district page but has no coordinate here). No picture was found for the Hastings Mill store, Irving House, Walhachin or Anyox (the first two candidates were a playground and a park view). The Emily Carr House, E&N Roundhouse and Craigflower Schoolhouse rows were removed from the earlier BC notes.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Kwinitsa Railway Station | Prince Rupert, BC (OpenStreetMap 54.31369, -130.3311) | Mapped as Kwinitsa Station Museum on the waterfront | No page read: history, dates, hours |
| Kitwanga Fort (Gitwangak Battle Hill) | Kitwanga, BC (Wikipedia 55.0997, -128.0681 for the village) | National Historic Site near the village | No source read; check the Gitxsan and Parks Canada invitation to visitors |
| Hedley Mascot Mine | Hedley, BC (Wikipedia 49.37094, -120.04756) | Gold mine 1936 to 1949 with tours run from the Snaza'ist Discovery Centre | Which buildings stand and whether tours run now |
| Ashcroft Manor | Highway 1, 11 km south of Cache Creek (OpenStreetMap 50.71881, -121.32842) | Cornwall brothers' ranch of the 1860s with a sod building of 1863 | What can be visited now |
| Father Pandosy Mission | Kelowna, BC | Founded 1859, restored as a museum owned by the Catholic Church and run with the Okanagan Historical Society | A coordinate and hours; no page opened |

## Tips
- `nom.py` found nothing for the Hastings Mill and Father Pandosy museums by name; `osmnear.py <lat> <lon> 150 buildings` found the Hastings Mill building from the park's Wikipedia coordinate.
- The Wikipedia titles "Kwinitsa Station", "Gitwangak Battle Hill" and "Mascot Mine (Hedley)" do not exist; the last is "Hedley Mascot Mine".
- Web search quoting an operator's page gives seasonal hours, but several listings disagreed for every museum here; try the operator's page first.
