# hours_pqjp: hours for the last 11 waiting churches, then 11 museums and historic sites
state: several (New York, Kentucky, Illinois, Louisiana, Ontario, California, Wisconsin, District of Columbia, Montana, Delaware, New Brunswick, Saskatchewan)
region: several
date: 2026-11-22
places: 0
file: hours_pqjp.py
tidied: 2026-11-26

## What this batch is
An "hours" session (PROMPTS.md type 7): no new places and no pins. `tools/hours.py list --kind worship` showed 11 churches still waiting (9 in New York, 2 in Kentucky); all were looked up, so no church waits anywhere now. Then 11 museums and historic sites from `tools/hours.py list` without `--kind`. 22 places recorded: 13 with times from the page of whoever runs the place, 9 recorded `?`. Pages were read with `tools/hours.py page` / `tools/page.py`, and where those could not read a page (TLS failure, script-drawn page, 403) with the web fetch tool; the address or town on each page was checked against the place.

Hours recorded:
- Hunter Synagogue: its own site (7879 Main Street, Hunter). Shabbat services first Friday night of each month, High Holiday services; no clock times given. Open.
- Richmondville UMC: Upper New York Conference church page (268 Main Street). Main service 11:30 a.m., Sunday school 11 a.m.; the page gives no day. Open.
- Cathedral of the Assumption and St. Joseph, Butchertown, Louisville: the Archdiocese of Louisville's parish pages (433 S. Fifth St.; 1406 E. Washington St.). Open.
- Grant Home, Galena; Pierre Menard Home: Illinois DNR site pages. Open.
- Texas and Pacific depot, Natchitoches: NPS Cane River Creole hours page (the depot is the park visitor centre). Open.
- Josiah Henson Museum: Ontario Heritage Trust page; closed for the season, reopens May 15, 2027. Open.
- Benicia Capitol: California State Parks page. Open.
- Pendarvis: its own Wisconsin Historical Society site; closed for 2026, reopens May 2027. Open.
- The Octagon: Architects Foundation visiting page (1799 New York Ave NW). Open.
- World Museum of Mining: its own home page, November 2026 hours only. Open.
- Kings Landing: its plan-your-visit page; closed for the season, reopening in November for Christmas events, no dates given. Open.

Not checked: nothing was seen on the ground and no telephone call was made. No church was found to be closed or sold.

## Pages that would not open, or gave no times (recorded `?`)
| Place | Page tried | What happened |
|---|---|---|
| Trinity Episcopal, Ashland NY | searches; Wikipedia | No parish or diocese page found |
| Mitchell Hollow Union Chapel, Windham NY | Vedder Research Library church-records page | Says nothing of services |
| All Souls Church, Onteora NY | searches; Wikipedia | Only an architecture blog; Onteora Park is a private colony |
| St. John the Evangelist, Tannersville NY | Vedder Research Library church-records page | Says nothing of services; no diocese page found |
| Prattsville Reformed Dutch Church NY | searches; Wikipedia | No church page found |
| Livingstonville Community Church NY | searches; Wikipedia | No church page found |
| West Fulton UMC NY | umc.org find-a-church page (849 West Fulton Road) | Active (attendance 11) but no service times |
| Motherwell Homestead SK | Parks Canada hours page | Only 2024 hours (June 28 to Sept 2, daily 10 to 4); now "closed for the season"; not recorded as current |
| Old Sussex County Court House, Georgetown DE | Delaware Historical and Cultural Affairs historic-sites page | "Please call ahead to discover visiting hours"; `hours.py set` refused that as not days and times |

## Leads
| Place | State | What is known | What is missing |
|---|---|---|---|

## Tips
Folded into `GUIDE.md` and the tools on 2026-11-26 by the tidy job (2 tips).
