# carnegie_ny_tpsk: Carnegie libraries, western and central New York
state: New York
region: cny, scho, wny
date: 2026-11-24
places: 20
file: data_carnegie_ny_tpsk.py

## What this batch is

Twenty Carnegie libraries in western and central New York, the first batch of a pass the owner asked for: the buildings Andrew Carnegie (and later the Rockefellers) paid for, all of them in time. The list to work from is Wikipedia's "List of Carnegie libraries in New York": 107 public libraries from 42 grants, 66 of them in New York City (a separate list), plus three college libraries. Before this batch the Atlas had six of the 41 outside New York City (Amsterdam, Gloversville, Fleischmanns, Northport, Ticonderoga's Black Watch Library and, in Troy, RPI's Carnegie Building).

Added: Andover, Bolivar, Franklinville (Blount Library), Olean (now a restaurant), Salamanca (former; buff brick by its Commons picture), Hornell, Elmira (old Steele library, now the Commerce Center), Perry, Warsaw, Penn Yan, Dunkirk, Lackawanna, Niagara Falls (city offices), North Tonawanda (Carnegie Art Center), Binghamton (SUNY Broome's Culinary and Event Center), Canastota, Fulton, Solvay, Syracuse (the Carnegie Building on Montgomery Street) and Syracuse University's Carnegie Library.

Sources: Wikipedia read as raw text with `wiki_raw.py`; libraries' own pages, the Buffalo and Erie County Public Library, local history pages and newspapers read with the web fetch tool (`page.py` could not reach ordinary web pages from this session). Hours are from each library's own page; directories were not used. Pins are ArcGIS geocoder or OpenStreetMap points for the list's street addresses, each looked at on the leaf-off aerial.

The fifteen others outside New York City (Hudson Valley, Mohawk Valley, Westchester, Long Island, Schenectady, Alfred) are in the next batch, `carnegie_nye_lgms`, with its own pull request.

Not checked: whether The Old Library restaurant in Olean has reopened after its 2025 sale; who is in the Salamanca building (only Wikipedia's list says a law office); Warsaw's regular hours (its page showed a holiday week only); Canastota's hours (its hours page refused the fetch); whether Syracuse's Carnegie Building renovation is finished. Red brick is "yes" for Penn Yan, Warsaw and Lackawanna, from their Wikimedia Commons pictures; "no" where a source or picture shows buff, cream, white, yellow or grey brick; and "?" everywhere else.

Pictures: found on Wikimedia Commons for Andover, Bolivar, Salamanca, Warsaw, Penn Yan, Lackawanna, Binghamton and both Syracuse buildings; none fitted Franklinville, Elmira, Perry (the one "Perry Carnegie Library" picture may be Perry, Oklahoma's), Dunkirk or Fulton. The finder ran without the Commons login, at the slow pace.

## Leads

| Place | Town, state | What is missing | Source |
|---|---|---|---|
| Hamburg Carnegie library (1915–1966) | Hamburg, New York | The Carnegie building was on Center Street, not at the present library at 102 Buffalo Street; whether it stands, its number and its use today were not found | buffalolib.org/hamburg-public-library/legacy-nineteenth-century-club |
| Wells College Carnegie library (Cleveland Hall) | Aurora, New York | Not researched yet; a library 1911–1968 | Wikipedia, List of Carnegie libraries in New York |
| The 66 Carnegie branch libraries of New York City | New York, New York | A batch or two of their own; about a dozen were torn down | Wikipedia, List of Carnegie libraries in New York City |

## Tips

- The Wikipedia list's addresses gave PointAddress geocoder hits that landed on the building in 18 of 20 cases; Salamanca's was only interpolated along the street and North Tonawanda's fell under trees on Goundry Street.
- The list can be wrong about which building was Carnegie's: Hamburg's 102 Buffalo Street is the 1966 library, not the Carnegie one. Check the library's own history page.
- Lookalike library sites: perrypubliclibrary.org is Perry, Ohio, and warsawlibrary.org is Warsaw, Indiana.
- A place's own Wikipedia link must come first among its links for the photo; a "List of ..." link is skipped by the photo finder, so it is safe as the only Wikipedia link.
