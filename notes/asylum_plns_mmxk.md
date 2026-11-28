# asylum_plns_mmxk: State hospitals and asylums, Iowa, Missouri, Kansas and Nebraska
state: Iowa, Kansas, Missouri, Nebraska
region: ia, ks, mo, ne
date: 2026-11-28
places: 17
file: data_asylum_plns_mmxk.py

## What this batch is
Seventeen state hospitals, asylums and related places in Iowa, Missouri, Kansas and Nebraska for the themed pass on historic state hospitals: the four Iowa Kirkbride hospitals (Mount Pleasant, Independence, Clarinda, Cherokee) and the Glenwood institution for "feeble-minded" children; Missouri's four numbered state asylums (Fulton, St. Joseph with the Glore Psychiatric Museum as a second entry, Nevada, Farmington), the 1869 St. Louis County Insane Asylum on Arsenal Street and St. Vincent's in Normandy; Topeka (site and cemetery), Larned and Parsons in Kansas; and the Norfolk hospital site and the Beatrice institution's 1935 farm in Nebraska. Sources: Wikipedia, the Kirkbride Buildings site, National Register records and the Beatrice farm form, the Missouri State Archives' exhibit on Fulton, Missouri Department of Mental Health history pages, St. Joseph Museums' hours page, the City of St. Louis preservation plan and Built St. Louis, the Buchanan County (Iowa) history site, the Kansas Preservation Alliance, the Topeka library, the 1912 Kansas cyclopedia, and news reports; Asylum Projects only for dates nothing else gave. Not checked: which early buildings survive at Fulton, Parsons, Larned and Farmington (all active state hospitals or prisons); whether the Mount Pleasant prison museum (opened 2018) and the Cherokee and Clarinda museums still open; the exact footprint of the Nevada and Topeka Kirkbride buildings; red brick at most places (only Clarinda and St. Louis have a source saying red brick; Independence is stone).

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Lincoln State Hospital (Nebraska Hospital for the Insane, Lincoln Regional Center) | Lincoln, NE | First brick asylum by D. Winchell burned April 17, 1871 (History Nebraska); a stone building followed in 1872 (Asylum Projects); now the Lincoln Regional Center | Whether any 1800s or early 1900s building stands; the 1976 state history of Nebraska institutions (dhhs.ne.gov PDF) would not open |
| Hastings State Hospital (Ingleside) | Hastings, NE | 1889 three-storey brick building with central tower by Charles C. Rittenhouse, wings 1891, later buildings to 1957; Ingleside cemetery about 1,000 burials; south campus a prison from 1987 (Adams County Historical Society page on NEGenWeb) | What stands now; comments on a 2016 blog speak of demolition plans, not confirmed |
| Beatrice State Developmental Center main campus | Beatrice, NE | Created 1885, opened 1887; five early buildings incl. a main building | Whether any early building stands |
| Winfield State Hospital and Training Center (Kansas State Asylum for Idiotic and Imbecile Youth) | Winfield, KS | Moved to Winfield 1887; closed 1996 or 1998; prison absorbed many buildings (Kansas Department of Corrections); first building of Cowley stone and brick per 1880s newspapers | Which old buildings stand and where; a pin |
| Woodward State Hospital-School | Woodward, IA | Not researched | Everything |
| Marshall State School (Missouri State School for the Feeble-Minded and Epileptic) | Marshall, MO | Not researched | Everything |
| Topeka State Hospital Center Building footprint | Topeka, KS | Demolished June 2010; school district land | Where on today's grounds it stood |

## Tips
- dhhs.ne.gov refuses both page.py and the web fetch tool; the Nebraska institutions history PDF needs another route.
- The Register form's UTM reference fixed the Beatrice farm pin when a by-eye guess had landed on the wrong farmstead a kilometre away: read the form's section 10 before guessing a rural pin.
- `nrhp_state.py` for IA, MO, KS and NE ran in the background and left no cache/nrhp files; `form.py mo "<name>"` then says there is no Register list.
- The workspace tools folder was recopied while this batch was being written and the new data file disappeared; keep a copy outside tools/ until publishing.
