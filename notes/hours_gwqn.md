# hours_gwqn: hours for 28 places of worship in New York and Quebec
state: New York
region: ny
date: 2026-11-20
places: 0
file: hours_gwqn.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. All 17 New York places of worship still waiting were looked up, then all 11 in Quebec, from `tools/hours.py list "<state>" --kind worship`. Twelve got times from the page of whoever runs them, each read in the session with `hours.py page` or `page.py --all`; 16 are recorded `?`.

Hours recorded (the page is in the file; the address or town on each page was checked against the place):
- St. Andrew's Episcopal, Yaphank: the Episcopal Asset Map entry for it (244 E Main Street, Yaphank). Sunday 10.
- St. Luke's Episcopal, Beacon: the Episcopal Asset Map entry "St. Andrew and St. Luke Church, East Campus", 850 Wolcott Ave. Sunday 10. (A squarespace "saint-lukes" site that came up first is St. Luke's, Auburn, California: not used.) The entry also gives "Saturdays 10 to 11" as hours of operation, left out because it does not say what for.
- Trinity Church, Fishkill: the Episcopal Asset Map entry (Box 484, Fishkill). Sunday 10 all year.
- Warren Chapel, Oakwood Cemetery, Troy: the cemetery's own events pages show the inside opened only at occasional paid tours (May 2022, April 2024). Recorded as such, not marked open.
- Saint-Jean, Sainte-Famille and Saint-François, Île d'Orléans: the Fabrique Sainte-Famille-de-l'Île-d'Orléans mass page (November 2026). Each church has Mass every second week; the dates given are November's, so these go stale: the parish posts a new month each month.
- Saint-Joachim and La Visitation, Château-Richer: Paroisse Notre-Dame-de-la-Nouvelle-France's schedule for October to December 2026 (linked from the Archdiocese of Quebec's church pages, which give 165 rue de l'Église and 277 rue du Couvent). Alternate Sundays.
- Notre-Dame-de-la-Présentation, Shawinigan: Ozias Leduc en Mauricie's activities page: visits Monday to Friday 9 to 4, adults $10 (2026). Its contact page gives 825 avenue Ozias-Leduc (the place says 823).

Not checked: nothing was seen on the ground and no telephone call was made.

## Pages that would not open, or gave no times
| Place | Page tried | What happened |
|---|---|---|
| First Reformed Church, Fishkill | fishkillreformed.org (nearly empty), fishkill-reformed.org (connection failed, 409); rca.org church page (address only) | The Town of Fishkill history page says Sunday 10 and tours by appointment, but it is not the church's page: not used |
| Caldwell Presbyterian, Lake George | adk.bar-z.com/node/1111 (connection reset) | Only the chamber of commerce and directories found |
| First Methodist, St. Johnsville; Methodist, West Martinsburg; Methodist, Stony Creek | unyumc.org church pages (404 or reset), umc.org find-a-church (404; archive copy of 2016 for Martinsburg not fetched) | No page with times |
| St. Mark's, Port Leyden | Episcopal Asset Map, Central New York | No entry for Port Leyden found; rcdony.org's Port Leyden page is St. Martin's (Catholic), a different church |
| Forest Presbyterian, Lyons Falls | lyonsfallsny.gov/churches (address only) | The "Forest Presbyterian" site found is in Forest, Virginia |
| St. Barnabas (New Hope Missionary Baptist), Troy; Oakwood Avenue Presbyterian, Troy | directories only; troyirish.org (403) | No page of their own |
| Pine Grove Community Church; Crum Creek church; Jamesport Meeting House | their own society pages/blog | Events only, no set times |
| Reformed Church of Beacon | directories only | Owner not found |
| Saint-James, Trois-Rivières | the city's heritage sheet (v3r.net PDF) | History only, no times |
| Procession chapels at L'Ange-Gardien and Sainte-Famille; old church of Saint-Pierre, Île d'Orléans | parish and heritage pages | No visiting times found. The Saint-Pierre Mass on the parish page is taken to be in the present church, not the old one |
| Église de Champlain | web search only | Tourism listings only |

Closed or sold: none found in this batch.

## Leads
None.

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (4 tips).
