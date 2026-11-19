# qc_bsjr: The Mauricie, Quebec
state: Quebec
region: qc
date: 2026-11-19
places: 18
file: data_qc_bsjr.py

## What this batch is
18 places in the Mauricie, the first in that region: in Trois-Rivières the Forges du Saint-Maurice ironworks ruins (1730–1883, Parks Canada), the Pointe-du-Lac seigneurial mill (1765–1788, machinery inside), the 1781 stone windmill on the UQTR campus, Manoir Boucher-De Niverville (about 1668 and 1729), the old prison (1816–1822, Musée POP), Maison Hertel-De La Fresnière, the Récollet church and friary now St. James Anglican (1742, 1754) and Manoir de Tonnancour; the old presbytery of Batiscan (1816, with the 1696 walls in its cellar), the Saint-Narcisse hydro plant and dam on the Batiscan, the Champlain church (1878–1879), the Le Brun general store at Maskinongé, the red-brick row at Yamachiche, the covered bridges at Saint-Mathieu-du-Parc (1936) and La Bostonnais (Pont Ducharme, 1945–1946), and in Shawinigan the former aluminum smelter (1899–1927), Ozias Leduc's painted church Notre-Dame-de-la-Présentation and the 1922 fire and police station. Facts come from the Canadian Register statements (historicplaces.ca with `page.py --all`; the Quebec ones in French), the Wikipedia "List of historic places in Mauricie" (raw text) for ids and coordinates, and the operators' own pages for hours: Parks Canada (Forges, read from the parcs.canada.ca address), Musée POP, Boréalis (Niverville), Récits qui font jaser (Pointe-du-Lac mill and Batiscan presbytery), Parc de la rivière Batiscan. Not checked: anything on the ground; owners and present use of Maison Hertel-De La Fresnière, Manoir de Tonnancour (an art gallery, by the Register), the smelter buildings and the Shawinigan fire station; service times of St. James and the Champlain church; hours of the Le Brun store (its site is gone) and of the Ozias Leduc church (its hours page answers 404); whether the two covered bridges still carry traffic; red brick for the Forges, the Niverville chimneys, the prison chimneys, the Hertel annex, the smelter and the fire station (`?`). No LiDAR sheet: no bare-ground coverage in Quebec in the pin tool. The Forges pin is the general site beside its lot (`area`); the Yamachiche pin marks the row, not one house. The smelter's Register coordinate was in the river; its pin is on the OpenStreetMap buildings AL-2 to AL-22.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Gare de Sainte-Anne-de-la-Pérade | Sainte-Anne-de-la-Pérade, QC (Register list 46.5764, -72.2032) | 1877 QMO&O station, later CP, heritage railway station 1993 (Register id 6898) | The Register point is on back yards beside the track; the station was not found on the aerial or in OpenStreetMap, so whether it still stands is unknown |
| Site archéologique des Forges-Grondin | Saint-Boniface, QC (46.5036, -72.8689) | Register id 15241 | Register page returned almost nothing; access unknown |
| Auberge Grand-Mère | 10 6e Avenue, Grand-Mère (Shawinigan) (46.6204, -72.6809) | Boarding house of 1897 for the Laurentide Pulp Company's senior staff, later a hotel; cited monument 2008 (Register id 13260) | Present use and whether it takes guests not checked |
| Gare du CP de Shawinigan | 1245 avenue de la Station, Shawinigan (OpenStreetMap 46.54518, -72.75088) | Register heritage railway station (id 4607); a CN station is id 4598 | Statements not read |
| Manoir des Jésuites, Calvaire Lacoursière, Maison Rivard-Dit-Lanouette, Église de Saint-Léon-le-Grand | Trois-Rivières, Batiscan, Sainte-Anne-de-la-Pérade, Saint-Léon-le-Grand (Register list) | Register ids 8277, 8935, 4319, 8421 | Statements not read |
| Clova railway station | Clova, QC (48.11, -75.359) | Register id 4580 | Not read; remote |

## Tips
- Tourisme Mauricie directory pages (`tourismemauricie.com/en/directory/<name>-2`) carry the operator's own website and its hours page as links in the cached page: `grep -oE 'href="https?://[^"]+"' research/pages/<file>` finds them. Use them to find the operator, not as an hours source.
- parks.canada.ca and pc.gc.ca reset the connection from `page.py`; the French address `parcs.canada.ca/lhn-nhs/qc/<site>/...` read at once.
- The Register list coordinate for the Shawinigan aluminum smelter (id 12043) is in the Saint-Maurice River, about 900 m from the buildings; OpenStreetMap names them AL-2 to AL-22 on promenade René-Lévesque.
- pincheck's `land:` line and CHECK ACCESS come from PAD-US, which has nothing in Canada; every Canadian pin gets them.
- Web search results for Quebec places came back as titles and links only, with no quoted text.
