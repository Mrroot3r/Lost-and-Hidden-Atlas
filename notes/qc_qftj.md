# qc_qftj: Across Quebec: first places in eleven regions
state: Quebec
region: qc
date: 2026-11-23
places: 21
file: data_qc_qftj.py

## What this batch is
21 places spread over eleven Quebec regions that had nothing on the map: Val-Jalbert ghost town (Chambord) and La Pulperie de Chicoutimi (Saguenay–Lac-Saint-Jean); the Bourlamaque mining village (Val-d'Or) and Obadjiwan–Fort Témiscamingue (Abitibi-Témiscamingue); Manoir Papineau (Montebello); the Carillon Canal and Moulin Légaré (Laurentides); Château Ramezay and Moulin Fleming (Montreal); Fort Chambly, Coteau-du-Lac, Fort Lennox and the Île Perrot windmill and miller's house (Montérégie); the Mansonville round barn (Estrie); the Moulin banal des Aulnaies and Grosse-Île (Chaudière-Appalaches); Fort Ingall and the Pointe-au-Père lighthouse (Bas-Saint-Laurent); the Cap-des-Rosiers lighthouse and the Paspébiac fishery station (Gaspésie); and the Pointe-des-Monts lighthouse (Côte-Nord). Facts come from the Canadian Register statements (historicplaces.ca with `page.py --all`, in French for the Quebec-listed ones), the Wikipedia regional "List of historic places" pages for ids and coordinates, a few English Wikipedia articles, and the operators' own pages for hours (Parks Canada, Château Ramezay, Pointe-du-Moulin, Fort Ingall, Cité de l'Or, the City of Montreal; La Pulperie only from its archived copy of March 9, 2026). Not checked: anything on the ground; hours for Val-Jalbert (its site answers with a bot check), Moulin Légaré (site down), Cap-des-Rosiers, Paspébiac, Pointe-des-Monts and the Aulnaies mill (`hours='?'`); whether the Mansonville barn opens to visitors (`view`); what is left on the ground at Fort Témiscamingue (`conf='mixed'`, from Wikipedia only); Pulperie summer hours; parking at Pointe-des-Monts and the Aulnaies mill. Fort Lennox is closed for the whole 2026 season (Parks Canada). Eight Register list points were off their buildings on the aerial (Pulperie, Fort Chambly, Fort Lennox in the river, Château Ramezay, Moulin Fleming on houses across the road, Manoir Papineau, Pointe-au-Père, Mansonville barn) and were moved to OpenStreetMap buildings or to what the aerial showed. Village minier de Bourlamaque, Fort Témiscamingue and Grosse-Île are `area` pins for whole sites. check.py warns that the Fort Témiscamingue and Grosse-Île pins are just outside the coarse Quebec outline; on the aerial Fort Témiscamingue is on the east (Quebec) shore of Lake Timiskaming and Grosse-Île is an island in the St. Lawrence, both in Quebec. No LiDAR sheet: the pin tool has no bare-ground coverage in Quebec.

## Leads
Places you read about and could not finish. One row each.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Carillon Barracks | 50 rue Principale, Saint-André-d'Argenteuil (45.5686, -74.3765, Register list) | National historic site, Register id 11123; Parks Canada's page names it as the Caserne-de-Carillon, at the entrance of Carillon village | Statement not read; operator (Argenteuil regional museum) and hours not checked |
| Moulin du Petit-Sault | Route 132, L'Isle-Verte (48.0578, -69.2894, Register list) | Register id 1729 | Statement not read |
| Moulin à vent de Vincelotte | 641 chemin des Pionniers Est, Cap-Saint-Ignace (47.0635, -70.4522) | Register id 4457 | Statement not read |
| Site historique de l'Île-des-Moulins | 900 rue du Moulin, Terrebonne (45.6927, -73.6384) | Register id 5282 | Statement not read |
| Pont couvert de Warwick | 28 route Saint-Albert, Warwick (45.9562, -72.0066) | Register id 11353 | Statement not read; whether it still stands |
| Moulin à laine d'Ulverton | 210 chemin Porter, Ulverton (45.6905, -72.2695) | Register id 7030 | Statement not read |
| Moulin du Domaine-de-Lotbinière, Moulin du Portage | Lotbinière (46.6449, -71.8923; 46.5549, -71.9693) | Register ids 6865, 5283; both have Wikipedia articles | Not read |
| Poste de traite du Lac-aux-Allumettes | chemin Perrault, Sheenboro (45.9519, -77.2708) | Register id 9807 | Statement not read; access |
| Moulin des Plourde | boulevard Renard Ouest, Gaspé (48.9959, -64.3961) | Register id 10281 | Statement not read |
| Pointe-au-Père Fog Alarm Building and the Empress of Ireland wreck site | Pointe-au-Père, Rimouski | Register ids 11346, 15164 | Could be folded into the Pointe-au-Père entry or added on their own |

## Tips
- The Wikipedia "List of historic places in <region>" pages for Quebec use `{{HPC row` templates; `wiki_raw.py --rows` reads none of them (it looks for NRHP rows). Split the raw text in research/wikiraw on `{{HPC row` yourself; the `idf`/`idp`/`idm` value is the historicplaces.ca id.
- Parks Canada slugs are not guessable: Manoir Papineau is `qc/manoirpapineau`, the canal is `qc/canalcarillon` (`qc/carillon` is the Barracks), Fort Témiscamingue is `qc/obadjiwan-temiscamingue`. The French `parcs.canada.ca/lhn-nhs/qc/<slug>/visit/heures-hours` pages read at once with `page.py`; Pointe-au-Père's hours page is drawn by script and shows only the late-season dates.
- valjalbert.com/horaire-et-tarifs answers with a bot check page; moulinlegare.com did not answer; pulperie.com answers HTTP 415 (page.py fell back to the archive).
- Register list coordinates in Quebec were off the building in 8 of 21 places; `nom.py` and `osmnear.py ... buildings` found the right buildings every time.
- `pip install Pillow` did nothing because a broken system copy of PIL shadowed it; `python3 -m pip install --break-system-packages --ignore-installed Pillow` fixed pincheck.
