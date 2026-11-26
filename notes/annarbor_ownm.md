# annarbor_ownm: Michigan: old Ann Arbor
state: Michigan
region: mi
date: 2026-11-26
places: 19
file: data_annarbor_ownm.py

## What this batch is
Nineteen standing buildings in downtown Ann Arbor and on the University of Michigan's Central Campus, from one walk-through video of old Ann Arbor buildings (Old World Exploration, "Old World Ann Arbor, Michigan"; the record is source/videos/20230726_PVgwIMM2rr8.md, 64 names). Added: the 1882 Central Fire Station (Hands-On Museum), the 1854 Detroit Observatory, the First National Bank Building, the 1886 Michigan Central depot (Gandy Dancer), Nickels Arcade, the 1881 First Unitarian Church on State Street, Hill Auditorium, Burton Memorial Tower, the Law School Quadrangle, the Clements Library, the Michigan Union, Angell Hall, Yost Field House, Newberry Hall (Kelsey Museum), St. Thomas the Apostle, St. Andrew's Episcopal, First Congregational, Bethlehem United Church of Christ and the 1909 Main Street post office. Facts come from Wikipedia read with wiki_raw.py, SAH Archipedia's Washtenaw pages (Buildings of Michigan), and the Ann Arbor District Library's "Historic Buildings, Ann Arbor, Michigan" pages, read with page.py. Hours come from the operators' own pages for the Hands-On Museum, the Kelsey Museum and the three parishes (St. Thomas, St. Andrew's, Bethlehem); the Clements Library's exhibit hours are as a web search result quotes its exhibits page, which answered 403. Not checked: the hours of the Detroit Observatory, the Gandy Dancer, the Michigan Union, Hill Auditorium and Nickels Arcade (pages refused or down, hours='?'); whether the Law Quadrangle's courtyard and reading room are open to visitors; First Congregational's service times (its site answered 403); red brick for the Detroit Observatory, the Michigan Union, Yost and the post office. Angell Hall and Newberry Hall's brick was read from Commons pictures. Burton Tower's bell count differs between Wikipedia (53 bells, 43 tons) and Buildings of Michigan (67 bells, 100 tons); Newberry Hall's date is 1888 in Wikipedia's infobox while Commons captions say 1890-1891, not settled. Nothing was visited on the ground.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Michigan League | Ann Arbor, MI (North University Avenue) | Pond and Pond's Collegiate Gothic women's union of 1929 (SAH Archipedia, University of Michigan Central Campus) | A page for the building itself, its hours and a pin |
| West Engineering Building | Ann Arbor, MI (550 East University Avenue) | Mason and Kahn, 1904 and 1909-1910, with an archway over the Diagonal (SAH Archipedia, Central Campus) | Its own page; whether the arch is open to walk through |
| Masonic Temple | Ann Arbor, MI | Named in a video; no source read says whether it stands | A source for its fate |
| Kempf House Museum and Judge Robert S. Wilson House | Ann Arbor, MI | Both have SAH Archipedia pages (MI-01-WA3, WA2) and are on the National Register | Not in the video; worth a later session |

## Tips
- SAH Archipedia's Washtenaw County pages are MI-01-WA1 to WA24, with campus buildings as WA7.1 to WA7.8 (Hill Auditorium WA7.1, Burton Tower WA7.2, Clements Library WA7.6, Law Quadrangle WA7.7); all read in full with page.py --all.
- The Ann Arbor District Library's "Historic Buildings, Ann Arbor, Michigan" pages (aadl.org/buildings_hhaaNNN and aadl.org/node/NNN) read well with page.py and give architect, dates and materials for downtown churches and buildings.
- detroitobservatory.umich.edu, clements.umich.edu, uunions.umich.edu, fccannarbor.org and hmdb.org answered 403 to page.py and the web fetch tool; the fetch tool cannot open web.archive.org; muer.com answered 522.
- aahom.org now redirects to discoverscienceandnature.org/aahom; its hours are drawn by script, so page.py sees none but the web fetch tool reads them.
