# on_vtqe: Ontario: National Historic Sites scatter
state: Ontario
region: on
date: 2026-11-28
places: 12
file: data_on_vtqe.py

## What this batch is
Twelve National Historic Sites spread across Ontario, from the Detroit River to Thunder Bay: Castle Kilbride (Baden), the Capitol Theatre (Port Hope), the Wellington County poorhouse (Fergus), the Canal Lake concrete arch bridge, Barnum House (Grafton), the Bois Blanc lighthouse, the Thunder Bay Tourist Pagoda, St. Raphael's Ruins, and the sites of the Normandale and Lansdowne iron works, the Backhouse grist mill and the Rosamond woollen mill. Sources: Wikipedia, the Parks Canada Directory of Federal Heritage Designations, HistoricPlaces.ca, Doors Open Ontario, and the managers' own pages (Castle Kilbride, the Long Point Region Conservation Authority, St. Raphael's Ruins). Not checked: hours for the Wellington museum (taken from a web search result quoting its site), the Capitol Theatre, the Pagoda and the textile museum (no page gave any); whether Barnum House is open; how visitors reach Bois Blanc Island; ownership of the Normandale and Lansdowne remains; brick for most standing places ('?'). The Normandale and Lansdowne pins are area points, not located foundations.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Algoma Central Engine House | Sault Ste. Marie, ON (46.5282, -84.3505) | National Historic Site, 1912 | A source on what stands and who runs it |
| Bridge Island / Chimney Island blockhouse ruins | St. Lawrence River near Johnstown, ON | National Historic Site, blockhouse of 1814 | A source and a way to see it |
| Penman Textile Mill | Paris, ON | National Historic Site, 1874 | Sources opened and a pin check |
| Belleville Grand Trunk station; Prescott Grand Trunk station | Belleville and Prescott, ON | National Historic Sites, 1855-56 | Sources opened and a pin check |
| Oil Springs, First Commercial Oil Field | Lambton County, ON | National Historic Site, discovery of 1858 | Sources opened; what is on the ground |

## Tips
- historicplaces.ca and the Parks Canada directory (pc.gc.ca/apps/dfhd/page_nhs_eng.aspx?id=N) opened fine with page.py; heritagetrust.on.ca, wellington.ca and mississippimills.ca guessed URLs gave 404, so find the page with a web search first.
- wiki_raw.py does not find many Ontario site articles by their Parks Canada names; Wikipedia's Ontario list page does not give link titles through page.py, but its cached html in research/pages can be parsed.
- A Commons photograph caption showed the Rosamond mill is partly condominiums: look at the picture sheet before writing "what to look for".
