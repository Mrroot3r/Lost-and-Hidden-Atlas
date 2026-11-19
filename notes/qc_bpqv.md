# qc_bpqv: Île d'Orléans and the Côte-de-Beaupré, Quebec
state: Quebec
region: qc
date: 2026-11-19
places: 17
file: data_qc_bpqv.py

## What this batch is
17 standing places of the French Regime and after, on Île d'Orléans (Saint-Pierre, Sainte-Famille, Saint-François, Saint-Jean, Saint-Laurent) and along the Côte-de-Beaupré (Boischatel, L'Ange-Gardien, Château-Richer, Saint-Joachim): the old church of Saint-Pierre (1717–1719), the churches of Sainte-Famille, Saint-Jean, Saint-François (shell of about 1734, rebuilt after the 1988 fire) and Saint-Joachim, procession chapels at Sainte-Famille and L'Ange-Gardien, the Saint-François parish school, Manoir Mauvide-Genest, Maison Drouin, the Godbout rowboat shop at the maritime museum, the Manoir de Charleville (1660s) and Maison Laberge (1674), the Château-Richer church square and old convent, La Grande Ferme, and the towers of the Montmorency Falls bridge that failed in 1856. Facts come from the Canadian Register of Historic Places statements (historicplaces.ca, read with `page.py --all`; the Quebec statements are in French), English Wikipedia raw text, the operators' own pages (manoirmauvidegenest.com, museemaritimeio.ca, fondationfrancoislamy.com FAQ, lagrandeferme.org) and Bridgemeister. Not checked: any church's service or visiting times (no parish page found; all churches are `view`), owners of the churches, chapels, school and the two private houses, Manoir Mauvide-Genest's season (its page gives daily 10 to 5 but no months), Montmorency park hours (sepaq.com refused), the old convent museum's hours (its website is hijacked), and red brick for the rowboat shop, the convent and the Montmorency towers (`?`). Pins are on OpenStreetMap points or Register-list coordinates checked on the aerial; the procession chapels and the parish school are `site`, the Montmorency towers `area`. Nothing was seen on the ground.

## Leads
Places you read about and could not finish. One row each; delete the example row. Leave the table header.

| Place | Where | What is known | What is missing |
|---|---|---|---|
| Moulin du Petit-Pré | Château-Richer, QC (Wikipedia: 46.9346, -71.0626) | Flour mill of 1691–1695 for the Seminary of Quebec, burned 1759 and 1877, restored to its 1763 look and a museum from 2003 (Wikipedia) | Its web address now carries a casino page; current use unknown. The Wikipedia coordinate falls on a building at a road corner not confirmed as the mill on the aerial |
| Maison Racine | 9050 avenue Royale, Sainte-Anne-de-Beaupré (47.0122, -70.9624, Register list) | Long low whitewashed stone house of about 1780, enlarged about 1820, with dairy and outbuildings; Register id 1739 | Owner and whether more than a house; pin not checked |
| Maison de nos Aïeux | 2485 chemin Royal, Sainte-Famille | Fondation François-Lamy museum, open daily mid-June through September 10 to 5 (its FAQ) | The building's own date and history were not read |
| Montmorency: Manoir Montmorency, St. Mary's chapel, mill and power-plant remains | Parc de la Chute-Montmorency, Boischatel/Québec | Listed in the Register statement (id 4112) as parts of the heritage site | Sépaq pages refused `page.py`; no dates or positions for each piece |
| Château Bellevue (Petit-Cap) | Saint-Joachim | Built for the Seminary from 1777, doorway by Michel-Augustin Jourdain 1781 (Register statement for the Saint-Joachim presbytery, id 11424) | No statement of its own read; access unknown |

## Tips
- historicplaces.ca resets the connection now and then; a second try after 10 to 20 seconds read every page. Quebec statements come in French even under /en/; the "Description of Historic Place" paragraph gives address, dates and materials, "Character-Defining Elements" the interior fittings.
- The Wikipedia "List of historic places in Capitale-Nationale" raw text gives each row's Register id and coordinates (split on `{{HPC row`); the id field may be idp, idf or idm.
- Two Quebec museum domains are hijacked by gambling pages: auxtroiscouvents.org (Château-Richer convent museum) and moulin-petitpre.com. Do not link them.
- Destination Québec cité listings (quebec-cite.com) carry the operator's real website link in the cached page; use it to find the operator, not as an hours source.
- sepaq.com (Parc de la Chute-Montmorency) answers 403 to `page.py` with no usable archive copy.
- Web searches for Quebec church service times returned only directories (gcatholic, tourism sites); no parish pages.
