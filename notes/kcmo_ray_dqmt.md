# kcmo_ray_dqmt: Richmond and Plattsburg, Missouri
state: Missouri
region: kcmo
date: 2026-11-24
places: 10
file: data_kcmo_ray_dqmt.py

## What this batch is
Ten places in Richmond (Ray County) and Plattsburg (Clinton County), north-east of Kansas City, where the Atlas had nothing: the 1914 courthouse, the poor farm that is now the Ray County Museum, Dougherty Auditorium (Farris Theatre), the Watkins House, the Pioneer (Mormon) Cemetery, Bob Ford's grave, the old Hughes-Wasson bank, New Hope Primitive Baptist Church, the Mansur farmstead (Rock Hall) and the Stoutimore House in Plattsburg. Facts come from Wikipedia (wiki_raw.py), the Ray County Historical Society's own visitor page (hours, tour), the 2013 National Register form for the Stoutimore House, Clio, and web-search result text for the Bob Ford and Pioneer Cemetery details. The Register forms for the Ray County listings could not be read (NPGallery holds a placeholder; the old mostateparks.com PDF addresses answer 404), so what is left standing inside each was not checked. Pins were looked at on the aerial; the Mansur pin falls in a field about 150 m from the nearest farm buildings and the two cemetery pins mark the area only. Ownership of both Richmond cemeteries was not found, so both are look-from-the-road. Pictures: one found (Stoutimore House); the bank's only candidate showed the courthouse and was refused.

## Leads
| Place | Where | What is known | What is missing |
|---|---|---|---|
| Claybrook House | Kearney, MO (39.38806, -94.33583) | 1858 Federal frame house; Wikipedia says it burned in a controlled burn in 2002 and was demolished | Whether anything is left to see |
| Aker Cemetery | near Smithville, MO (39.41111, -94.54556) | Register-listed 1835 settlers' cemetery, 25 graves, stones down in woods (Wikipedia, search result on the 1974 form) | Whether the public may reach it, and exact location |
| Battle of Albany monument and Partisan Ranger memorial | near Orrick, MO | A hillside monument dedicated in 1988, per a Waymarking entry; the museum page says guerrillas lie in an old cemetery north-east of Orrick | A source for the cemetery and the monument's location |
| Ray County Poor Farm interior, Doniphan statue | Richmond, MO | On the museum's tour page | Which rooms are original |
| Bluffton, first Ray County seat; Camden | Camden, MO | Museum page: fort of 1821, county seat to 1828, river port later | Where anything stood; likely nothing left |

## Tips
- NPGallery serves a placeholder for most Ray County Register forms; the 2013 Stoutimore form read fine with page.py -g.
- The Ray County Museum's visit page (raycountymuseum.org/home/visit/) carries hours and a county driving tour; read it with page.py --all.
- Argument order for wiki_raw.py: -g and its pattern must come before the titles, or they are read as titles.
