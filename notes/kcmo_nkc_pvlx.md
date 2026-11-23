# kcmo_nkc_pvlx: North Kansas City, Parkville, Gladstone and Liberty, Missouri
state: Missouri
region: kcmo
date: 2026-11-23
places: 15
file: data_kcmo_nkc_pvlx.py

## What this batch is
Fifteen places north of the Missouri River from Kansas City: three North Kansas City buildings (the Armour Theatre, the Sears warehouse, the Wheeling Corrugating building), five in Parkville (Mackay Hall, the relocated Waddell "A" truss bridge, the Banneker School, Washington Chapel), Gladstone's Atkins-Johnson Farm and Big Shoal Cemetery, the 1859 Antioch church chapel, the Compton log house, and four in Liberty (Garrison School, Mt. Memorial Cemetery, the Major Hotel, the Miller Building). The Atlas had nothing in North Kansas City or Parkville. Sources: the National Register lists for Clay and Platte counties and Wikipedia articles as raw text; the operators' own pages for the Atkins-Johnson Farm, Screenland Armour, Antioch Community Church, the Banneker School Foundation, Clay County African American Legacy and the City of Liberty; Clio; a Flatland KC article on Washington Chapel; and web search results that quote the City of Parkville's park page (English Landing Park hours and parking). Not checked: the Register forms (none could be opened), present use of the Wheeling building and the Compton house, service times at the two churches, hours at Garrison School, any interior, and pins for the Major Hotel and Miller Building, which come from the Register list and were not matched to a street address. Red brick is "?" for most because no source or picture opened said what colour the brick is; the Banneker School is "yes" (Wikipedia says red brick) and the stone and wood places are "no". The pictures tool found nothing on Commons for Big Shoal Cemetery and only unrelated Oak Ridge, Tennessee photographs for the Compton house.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Frank Hughes Memorial Library | 210 E. Franklin St, Liberty, MO | Wikipedia: 1940 Wight and Wight library, Register 1992; the library joined Mid-Continent Public Library in 1981 | What the building is used for now, and whether the public may go in |
| IOOF Liberty Lodge No. 49 and the South and West Liberty courthouse-square districts | Liberty, MO | Register 1992; Wikipedia: 1923 Moderne lodge in glazed light brick, still shops | A source for what each building is now; addresses for pins |
| Aker Cemetery | NE of Smithville, MO (39.411, -94.546) | Register 1974: first settlers' burial plot, about 25 graves, above Smithville Lake's full pool | Whether visitors may reach it and from where (Clay County Parks or Smithville) |
| TWA Administrative Offices Building | Kansas City, Platte County, MO (39.302, -94.682) | Wikipedia: 1968-71 steel and glass building by Skidmore, Owings and Merrill, Register 2007 | Present owner and use; whether it can be seen from a public road |
| McCoy Meetin' House (1932) | Park University, Parkville, MO | A campus tour (via search result) names the McCoy Meetin' House as the only other bell tower on campus | A page of the university describing it, and whether visitors may go in |

## Tips
- Missouri Register forms: the mostateparks.com PDF addresses that search results list were not opened; plan on Wikipedia, Clio and the operators' pages.
- A museum's street address can land on its car park, not the building: the Atkins-Johnson Farm's address match fell 60 m from the farmhouse, and Park University's on a small building 40 m from Mackay Hall. Look at the aerial before keeping an address match.
- `photo_find.py` for a place named "Oak Ridge" returns Oak Ridge, Tennessee photographs by the dozen; record none for those.
- The Banneker School Foundation's own history page (bannekerschoolparkvillemo.org/history) read well with `page.py --all`; ccaal-garrisonschool.org/history gave HTTP 403 but the home page opened.
