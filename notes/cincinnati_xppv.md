# cincinnati_xppv: Ohio: old Cincinnati, from Music Hall to Eden Park
state: Ohio
region: oh
date: 2026-11-22
places: 13
file: data_cincinnati_xppv.py

## What this batch is
Thirteen standing places in Cincinnati, from the names in one Old World Exploration video about the city (the record is source/videos/20220827_nfyI7eW_vUE.md; the video is a tip and nothing rests on it): Music Hall, Plum Street Temple, the Cathedral Basilica of St. Peter in Chains, City Hall, the Hamilton County Courthouse, the Hotel Metropole (21c Museum Hotel), the Doctors' Building, the Clyffside Brewery, the Over-the-Rhine Historic District, and in Eden Park the Stand Pipe, Pumping Station No. 7, the Elsinore Arch and the Spring House Gazebo with Mirror Lake. Facts are from Wikipedia (read with wiki_raw.py), the Cincinnati Parks Eden Park page and its park-hours rule (6 a.m. to 10 p.m.), Friends of Music Hall's tours page, the Wise Temple's Plum Street page (tours Thursday mornings by appointment), the cathedral's own calendar for Mass times, the 21c hotel page (no gallery hours given), the HMdb text of the Ohio Historical Society's Cincinnati Breweries marker, Soapbox Media (2008) and Queen City Discovery (2010) for the Clyffside. Pins are ArcGIS address points or the Wikipedia point, all looked at on the aerial; none moved. Not checked: any interior not described by a source; whether the 2008 Clyffside condominium plan and the 2024 Doctors' Building apartment conversion were finished; the hours of City Hall, the courthouse and the 21c galleries; the downtown garages' hours and fees. Red brick is from Commons pictures opened for Music Hall, the Stand Pipe, the Elsinore Arch, the Metropole, the courthouse, the temple and the Clyffside, and from the articles for City Hall (stone), the cathedral (limestone) and the Doctors' Building (terracotta); Station No. 7 (brick walls, colour not stated), the gazebo and Over-the-Rhine are left '?'. check.py warns that the Metropole and Doctors' Building pins are just outside Ohio's coarse outline along the river; both are on their buildings in downtown Cincinnati on the aerial.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Cincinnati Subway tunnels | Under Central Parkway, Cincinnati, OH (39.11337, -84.51814, Wikipedia) | Wikipedia: about 2 miles of tunnel and four underground stations (Race, Liberty, Linn, Brighton) survive, closed | A source for anything a visitor can legally see (a portal, or a current public tour) |
| Melan Arch Bridge, Eden Park | Cincinnati, OH (39.11714, -84.4892, OpenStreetMap) | Named in the Wikipedia Eden Park article as historic, on the road from the Twin Lakes to the overlook | A source for its date and builder |
| Klotter and Sons / Bellevue Brewery | Over-the-Rhine or the West End, Cincinnati, OH | Listed as a surviving brewery building on the Ohio Historical Society's Cincinnati Breweries marker (HMdb 24835) | Address, owner and a source describing it |
| Central Parkway YMCA | Central Parkway, Cincinnati, OH | Search results say it was restored and reopened (WCPO) and also holds senior apartments | Its date and an article or Register form that could be read |
| Altenheim | Cincinnati, OH | A German old people's home pictured in the video | Which building, and whether it stands |

## Tips
- In Cincinnati the Wikipedia Register lists are split into "downtown", "eastern" and "western Cincinnati"; the plain "listings in Cincinnati" page has no rows.
- start.py "Cincinnati, Ohio" printed no "State:" and region line (it did for Asheville); the region code is oh, from tools/states.py.
- videos.py check accepts an outcome only as the bare word or the word followed by a space: "gone: razed 1942" is a PROBLEM, "gone (razed 1942)" passes.
- nom.py answered one query and then HTTP 629 for the next, as an Arkansas note found; geo.py address points did the downtown pins.
- cincinnatiarts.org answered HTTP 406 to page.py; friendsofmusichall.org has the Music Hall tour details.
