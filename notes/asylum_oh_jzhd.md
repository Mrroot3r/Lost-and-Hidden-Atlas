# asylum_oh_jzhd: State hospitals and asylums, Ohio
state: Ohio
region: oh
date: 2026-11-28
places: 10
file: data_asylum_oh_jzhd.py

## What this batch is

Ten Ohio state hospitals and asylums for the themed pass, beside the Dayton asylum and the Toledo Old Cemetery already on the map: the Athens Lunatic Asylum (The Ridges, standing, the Kennedy Museum of Art in its administration block) and its 1914 cow barn (the Dairy Barn Arts Center, a separate entry with its own Register listing); the sites of the Columbus State Hospital and the Ohio Institution for Feeble-Minded Youth on the Columbus Hilltop (both gone); the Cleveland State Hospital in Newburgh (gone, now housing); Massillon State Hospital (an active state hospital; two original buildings said to survive, not identified); the Lima State Hospital for the Criminally Insane (standing, reinforced concrete faced with red brick, inside state prison land); the Orient State Institute (several early buildings inside the Pickaway prison); the Ohio Hospital for Epileptics' sandstone water towers at Gallipolis; and the Toledo State Hospital New Cemetery. Sources: Wikipedia, the Park Service's Register records, the Register cover document "Federal and State Correctional Institutions in Ohio" (2006, amended 2021; the best source for Lima and Orient), SAH Archipedia, KirkbrideBuildings.com, Ohio State University Libraries, WOSU, the Encyclopedia of Cleveland History, Cleveland Historical, us-data.org, Asylum Projects, the Frank Packard pages at ghmchs.org, HMdb marker texts, and the museums' own pages for hours. Not checked: which two Massillon buildings and which Orient buildings are original; whether Lima's main building is still empty or can be seen from a public road; where exactly the Gallipolis towers and the gone Cleveland and Columbus Feeble-Minded main buildings stood (pins are area); the Columbus State Hospital cemeteries' positions and access; red brick on every place except Athens and Lima.

## Leads

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Longview State Hospital (Commercial Hospital and Lunatic Asylum) | Carthage, Cincinnati, west of Paddock Road by the old Miami and Erie Canal | Kirkbride asylum opened 1859 or 1860; state took over 1927; cemetery of about 1,160 plots on the grounds; renamed Pauline Warfield Lewis Center 1984 and Summit Behavioral 2000 (Asylum Projects, Cincinnati library blog) | Where the main building stood and when it was razed; the successor hospital's address lies east of Paddock Road, so it cannot stand in for the site |
| Apple Creek State Hospital (Apple Creek State School) | Apple Creek, Wayne County | Opened February 14, 1931 in a former tuberculosis hospital; architect Joseph A. Gattozzi; closed 2006; most buildings demolished; about 130 buried beside the Apple Creek Presbyterian Cemetery (Asylum Projects) | A second source; which buildings stand; the Wayne County library wiki page sits behind a robot check |
| Hawthornden State Hospital | Northfield (Summit County) | Farm colony of Cleveland State Hospital from 1922, separate in 1941, cottage plan; many 1920s-30s buildings razed in the 1970s; now Northcoast Behavioral Healthcare (Asylum Projects) | What, if anything, of the old buildings survives; a second source |
| Columbus State Hospital cemeteries | Hilltop, Columbus | Two (WOSU) or four (KirkbrideBuildings.com) small hospital cemeteries with plaques and numbered stones | Their positions and whether the public may walk in |
| Athens asylum cemeteries | The Ridges, Athens | Three cemeteries, about 1,930 burials, restored by NAMI Athens since 2000 (Wikipedia) | Positions; could be a separate burial entry |
| Woodside Receiving Hospital | Youngstown | Opened 1945 as a state receiving hospital, closed 1996, razed 2013 (Asylum Projects) | Too late and gone; left out on purpose |
| Cambridge State Hospital | Cambridge, Guernsey County | Took over the WWII Fletcher General Hospital after the war, until 2008 (Ohio marker 7-30 at Fletcher Memorial Park) | A wartime army hospital, not an asylum building; left out on purpose |

## Tips

- The Register cover document "Federal and State Correctional Institutions in Ohio" (npgallery 64500954_text, 287 pages with a text layer) describes every asylum that became a prison (Lima, Orient, the Southeast Ohio TB hospital) with architects and condition; read it from research/pages/ with a short Python slice rather than page.py -g.
- page.py could not reach www.ohio.edu or sah-archipedia.org from this machine (connection refused), but the web fetch tool opened both.
- Asylum Projects pages are at asylumprojects.org/index.php/<Name>, but several Ohio ones live under other names (Toledo_Insane_Asylum, Orient_Institute, Columbus_Feeble_Minded_Institute); search for them rather than guessing.
- An address point for a state campus (Lima, 2350 North West Street) can fall a kilometre from the building: look wide with look.py before trusting it.
