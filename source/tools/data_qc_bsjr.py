# November 19, 2026: the Mauricie, Quebec (Trois-Rivières, Shawinigan, Les Chenaux, Maskinongé, La Tuque). Region qc
# drawn at random by tools/choose.py --claim --state qc,nb,ns,pe,nl. Sources opened in this session: the Canadian Register
# of Historic Places statement for each place (historicplaces.ca, read with tools/page.py --all; the Quebec statements are
# in French, from the Ministère de la Culture, and were read in French); the Wikipedia "List of historic places in
# Mauricie" (raw text) for Register ids and coordinates, and the Forges du Saint-Maurice and Saint-Narcisse articles;
# the operators' own pages: Parks Canada (Forges hours and fees), Musée POP (old prison), Boréalis (Manoir Boucher de
# Niverville), Récits qui font jaser (Pointe-du-Lac mill, Batiscan presbytery), La Cité de l'énergie, Parc de la rivière
# Batiscan; Tourisme Mauricie listings only to find the operators' addresses. Nothing was seen on the ground.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def HP(t,i): return ['Canadian Register of Historic Places: '+t,'https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=%d'%i]
LIST=W('List of historic places in Mauricie')

BATCH={'key':'qc_bsjr','label':'The Mauricie, Quebec','added':'2026-11-19 21:15'}

PLACES=[
N('forges-du-saint-maurice',"Forges du Saint-Maurice","Trois-Rivières",'qc','industry','ruins',46.3982,-72.6622,'area','open','walk','','1730–1883',
  "Canada's first ironworks, founded in 1730 by François Poulin de Francheville, seigneur of Saint-Maurice, on a stream running into the Saint-Maurice River. It was the chief industry of New France, ran for about 150 years (1732 to 1883) under private companies, the French Crown and then the British, and grew into the country's first industrial village. It shut in 1883. Parks Canada has dug and interpreted it since 1973; the Register counts 252 remains on the site.",
  "A wooded cultural landscape on the river bank: the remains of the blast furnace (haut fourneau) and the chimney of the lower forge on the Saint-Maurice bank, the forge stream and the traces of its dams and canals, the footings of the workshops, sawmill and village buildings on the upper terrace, old roadways, and the spring called the Devil's Fountain (fontaine du Diable), all named in the Register statement. Parks Canada's hours page says the trail between the blast furnace and the lower-forge chimney is closed for works from November 9 to 30, 2026.",
  "The oldest ironworks in Canada: a furnace, a forge chimney and a whole vanished company village in the woods.",
  "Parks Canada national historic site, 10000 boulevard des Forges, about 15 km north of downtown Trois-Rivières. Open to the public in summer, with the trails open all year (Parks Canada hours page, read November 2026; closed for the season, back in spring 2027). Daily admission: adult $5.00, senior $4.50, 17 and under free (Parks Canada fees page). Mapped lot at the start of the site trail (OpenStreetMap).",
  [HP("Forges du Saint-Maurice National Historic Site of Canada",11709),W('Forges du Saint-Maurice'),
   L('Parks Canada: hours','https://parcs.canada.ca/lhn-nhs/qc/saintmaurice/visit/heures-hours'),
   L('Parks Canada: fees','https://parcs.canada.ca/lhn-nhs/qc/saintmaurice/visit/tarifs-fees'),LIST],
  th=[46.3984,-72.66103],thn="Site lot (OpenStreetMap)",brick='?',
  hours='June 20 to September 7, 2026: daily 10 a.m. to 5 p.m.; trails open all year'),

N('moulin-seigneurial-pointe-du-lac',"Moulin seigneurial de Tonnancour (Pointe-du-Lac mill)","Trois-Rivières (Pointe-du-Lac)",'qc','industry','standing',46.28786,-72.68967,'exact','open','drive','','1765–1788',
  "A stone water-powered flour mill built between 1765 and 1788 by Louis-Joseph Godefroy de Tonnancour, seigneur of Pointe-du-Lac, on the site of his father's mill of 1721 to 1723, where the Saint-Charles River meets Lac Saint-Pierre. The Montour family worked it from 1795 to 1873; the Frères de l'instruction chrétienne bought it in 1927, and it stopped grinding in 1962 or 1963. It was classified in 1975.",
  "A massive two-and-a-half-storey stone mill of French type on a slope, with a steep gable roof, three dormers a side, two chimneys set in a stagger, the miller's lodging behind the symmetrical gable end, and a sawmill built on at right angles. Inside, by the Register, a brick wall divides the miller's lodging from the works, and some of the machinery survives out of use: turbine, pit wheel and lantern pinion, millstones and bolter. Open to visitors in season (operator's page).",
  "A French-regime seigneurial mill with its turbine and millstones still inside.",
  "11930 rue Notre-Dame Ouest, Pointe-du-Lac. Run as a museum with the Récits qui font jaser group, whose page gives the season and hours. Mapped lot on rue Notre-Dame Ouest about 140 m east (OpenStreetMap).",
  [HP("Moulin seigneurial de Tonnancour",8104),HP("Site historique du Moulin-Seigneurial-de-Tonnancour",8105),
   L('Moulin seigneurial de Pointe-du-Lac: hours and fees','https://moulinpointedulac.recitsquifontjaser.com/en/business-hours-fees-and-access/'),LIST],
  th=[46.28766,-72.68783],thn="Lot on rue Notre-Dame Ouest (OpenStreetMap)",brick='no',
  hours='Last Sunday of May to last Sunday of October: daily 10 a.m. to 5 p.m.'),

N('moulin-a-vent-trois-rivieres',"Moulin à vent de Trois-Rivières","Trois-Rivières",'qc','industry','standing',46.3496,-72.5749,'site','view','walk','','1781',
  "A stone tower windmill built in 1781 near the St. Lawrence. Unlike most Quebec mills it belonged to a private owner, not a seigneury, and was rented to a miller; townspeople ground their grain there until 1854. The city bought it in 1906, and it was repaired and given new sails and a new roof for the city's tercentenary celebrations (Register); it was moved in 1975 to the campus of the Université du Québec à Trois-Rivières. Classified in 1961.",
  "A four-storey cylindrical stone tower with a low conical roof: the tallest of the 19 windmills kept in Quebec, by the Register. Its original machinery is gone. Whether the inside is ever open: not checked.",
  "",
  "3351 boulevard des Forges, on the UQTR campus (Register). Seen from the campus grounds; the university's visiting rules not checked. Mapped lot on boulevard des Forges about 240 m west (OpenStreetMap).",
  [HP("Moulin à vent de Trois-Rivières",1755),LIST],
  th=[46.34957,-72.57806],thn="Lot on boulevard des Forges (OpenStreetMap)",brick='no'),

N('manoir-boucher-de-niverville',"Manoir Boucher-De Niverville","Trois-Rivières",'qc','landmark','standing',46.34366,-72.54048,'exact','open','walk','','about 1668; 1729',
  "A seigneurial manor whose first house, probably half-timbered, was built about 1668 for Jacques Leneuf de La Poterie, a fur trader and several times acting governor of Trois-Rivières. In 1729 the naval officer François Châtelain rebuilt it in stone and lengthened it. Joseph Boucher de Niverville, French army officer and later superintendent of Indian affairs for the district, owned it, and his family kept it some forty years after his death in 1804. It escaped the 1908 fire that burned much of the city, was restored by the province in 1972, and was classified in 1960.",
  "A low one-and-a-half-storey stone house of French rural type with a steep hipped roof in cedar shingles, casement windows with double shutters and dormers. Inside, by the Register: whitewashed walls with soot-blackened baseboards, cut-stone fireplaces, period hardware, and part of the roof frame of the first house, among the oldest in Quebec; Boréalis says visitors can climb to the upper room to stand under it (steep stair, not accessible). Archaeological finds from the grounds guided the restoration.",
  "Under a roof frame from 1729, one of the oldest in Canada.",
  "168 rue Bonaventure, downtown. Run by Boréalis (Culture Trois-Rivières) and open to the public in summer only; closed for the season when read, back in 2027 (Boréalis pages, November 2026). Adult $9. Parking not checked: downtown street parking.",
  [HP("Manoir Boucher-De Niverville",5505),
   L('Boréalis: Le Manoir Boucher de Niverville','https://www.borealis3r.ca/le-manoir-boucher-de-niverville/'),
   L('Boréalis: hours and fees','https://www.borealis3r.ca/planifiez-votre-visite/horaire-et-tarifs/'),LIST],
  brick='?',hours='Summer only (days not posted when read); closed for the season, back in 2027'),

N('vieille-prison-trois-rivieres',"Vieille prison de Trois-Rivières","Trois-Rivières",'qc','inst','standing',46.34511,-72.53936,'exact','open','walk','','1816–1822',
  "A three-storey stone prison built from 1816 to 1822 to plans of 1815 by François Baillairgé, in the English Palladian manner, laid out after the reforms urged by John Howard (prisoners kept apart by age, sex and offence, better hygiene). It is the second-oldest prison in Quebec, and prisoners were held there from 1819 to 1986, the longest use of any jail in Canada, by the Register. Classified in 1978, it is now part of the Musée POP.",
  "A symmetrical stone front with a pedimented centre bay and bull's-eye window, a hipped roof, nine big brick chimneys and barred windows. Inside, by the Register: the plan in three equal parts with the common rooms in the middle and cell blocks to the sides, cells along a corridor, firewalls, a vaulted basement and the rear turrets that held the latrines. Guided tours of the cells (ages 8 and up); in summer the page lists English tours at 12:15 and 3:15.",
  "Prisoners were locked up here from 1819 until 1986.",
  "200 rue Laviolette (Register: 842 rue Saint-Pierre), beside the courthouse. Run by the Musée POP; prison tour adult $24, or $34 with the museum (Musée POP page, read November 2026). Parking not checked.",
  [HP("Ancienne prison de Trois-Rivières",4076),L('Musée POP: hours and admission','https://museepop.ca/en/old-prison/hours-and-admission'),LIST],
  brick='?',hours='June 23 to September 6: daily 10 a.m. to 5 p.m.; rest of the year Saturday and Sunday 10 a.m. to 5 p.m. (closed some holidays)'),

N('maison-hertel-de-la-fresniere',"Maison Hertel-De La Fresnière","Trois-Rivières",'qc','landmark','standing',46.34393,-72.53696,'exact','view','walk','','1824–1829',
  "A one-and-a-half-storey stone town house built between 1824 and 1829 on land held for over a century by the Hertel de La Fresnière family; Joseph-François Hertel de La Fresnière (1642–1722), called 'the Hero', led the French raids on New England border villages. It joins the Quebec City type of house that the French intendants' fire rules required (stone walls, firewall gables on corbels, chimneys at the ends) with neoclassical detail. Classified in 1961.",
  "A symmetrical stone front with a cut-stone cornice, moulded frames and pedimented dormers, firewall gables, a covered gallery round the back corner and a two-storey brick annex behind. Inside, by the Register, a carved turning staircase, a wooden mantel carved with scrolls and garlands, and a coffered ceiling. Whether the public may go in: not checked.",
  "",
  "802 rue des Ursulines, in the old town, between Maison Georges-De Gannes and the Ursuline monastery. Owner and use not checked; look from the street. Downtown street parking.",
  [HP("Maison Hertel-De La Fresnière",4318),LIST],brick='?'),

N('saint-james-trois-rivieres',"Église Saint-James (Récollets)","Trois-Rivières",'qc','worship','standing',46.34353,-72.53685,'exact','view','walk','','1742; 1754',
  "The Récollet friars, curés of Trois-Rivières from 1692, replaced their wooden friary and chapel with a stone friary in 1742 and a stone church in 1754. Barred from recruiting after the Conquest, they left in 1776. The British used the friary as a hospital and then as a court, prison and offices, and the church for Anglican worship and, from 1779 to 1795, a medical store. In 1823 both went to the Church of England, which consecrated the church as St. James and made the friary its rectory. Recognised as a heritage site in 2003.",
  "An L-shaped group on rue des Ursulines: the roughcast stone church of 1754 with a single nave, a flat east end, a low gable roof, an arched door, side niches, a bull's-eye in the gable and a belfry on the ridge; a covered passage; and the two-and-a-half-storey rectory of 1742 with a steep roof. One of the oldest groups of buildings in the city, by the Register. Interior and service times not checked.",
  "A French friars' church of 1754 that has been Anglican since 1823.",
  "811 rue des Ursulines (OpenStreetMap), in the old town. An Anglican church; service times not found on a page of its own. Downtown street parking.",
  [HP("Site historique des Récollets-de-Trois-Rivières",11211),LIST],brick='no'),

N('manoir-de-tonnancour',"Manoir de Tonnancour","Trois-Rivières",'qc','landmark','standing',46.34316,-72.53827,'exact','view','walk','','1795–1797',
  "A large stone town house of 1795 to 1797, raised on the walls of René Godefroy de Tonnancour's grand house of 1723 to 1725, which a fire had partly destroyed. It has served in turn as a home, for the military, for a religious community and as a school, by the Register. Its mansard roof, banned in New France as a fire risk and probably a Loyalist touch, is one of very few of its time. Classified in 1966.",
  "Three storeys of roughcast stone on the place d'Armes with firewalls, three tall stone chimney stacks (one double) and a cedar-shingle mansard with dormers. Inside, by the Register: fireplaces (one with cut-stone jambs), the main stair with turned balusters, a coffered ceiling and mouldings. The Register links the art gallery that occupies it; its hours were not checked.",
  "",
  "864 rue des Ursulines, facing the place d'Armes. Look from the square; gallery opening times not checked. Downtown street parking.",
  [HP("Manoir de Tonnancour",6983),LIST],brick='no'),

N('vieux-presbytere-batiscan',"Vieux presbytère de Batiscan","Batiscan",'qc','landmark','standing',46.4821,-72.2582,'site','open','drive','','1816',
  "Batiscan's first presbytery-chapel was built on this spot by the old Chemin du Roy in 1696, and a stone church beside it in 1708. The present stone presbytery of 1816 replaced the first one and held both the curé's lodging and a hall for the parishioners. The parish moved to the mouth of the Batiscan River in 1866, and the old church burned in 1874. Classified in 1984.",
  "A one-and-a-half-storey stone house of French rural type with a steep roof with slightly flared eaves, three stone chimneys and a neoclassical porch added in 1855. The foundations and a cross wall of the 1696 presbytery can be seen in its cellar, and the ruins of the burned church are on the grounds, which open on the river and fields (Register). Run as a museum with guided and self-guided visits.",
  "The cellar still holds the walls of the 1696 presbytery.",
  "340 rue Principale (route 138). Run with the Récits qui font jaser group, whose page gives the season and hours; dogs on leash allowed (Tourisme Mauricie listing). Parking not mapped: not checked.",
  [HP("Site historique du Vieux-Presbytère-de-Batiscan",6604),
   L('Vieux presbytère de Batiscan: hours, fees and access','https://presbyterebatiscan.recitsquifontjaser.com/en/business-hours-fees-and-access/'),LIST],
  brick='no',hours='Last Sunday of May to last Sunday of October: daily 10 a.m. to 5 p.m.'),

N('centrale-saint-narcisse',"Ancienne centrale hydroélectrique de Saint-Narcisse","Saint-Narcisse",'qc','industry','standing',46.55536,-72.41383,'site','public','walk','','1895–1904',
  "One of the first modern hydroelectric plants in Quebec, built at the Grande Chute of the Batiscan River with horizontal turbines; it fed what the Register calls the first high-tension line in Canada, put in service with the plant. The Register dates the stone dam to 1897 and the surviving building to 1904; the English Wikipedia article says the station was built from 1895 to 1897. The building is a section of a once larger one. Classified in 1963.",
  "A one-storey stone building with a shallow gable roof in metal, small-paned sash windows and a big double door under a glazed transom and relieving arch, and the stone dam across an arm of the river with its two water conduits (Register). Built like a 19th-century water mill, the Register says. Interior not checked.",
  "Where Canada's first high-tension line started, at a falls on the Batiscan.",
  "Beside the trails of the Parc de la rivière Batiscan; OpenStreetMap names the building the annex of the old power station and puts a lot on the park's Sentier de l'Annexe 135 m southeast. Owner of the building not checked. The park is run by a non-profit and charges a day fee (adult $10 with tax on its rates page, November 2026).",
  [HP("Site historique de l'Ancienne-Centrale-Hydroélectrique-de-Saint-Narcisse",6881),W('Saint-Narcisse'),
   L('Parc de la rivière Batiscan: rates','https://parcbatiscan.ca/tarifs/'),LIST],
  th=[46.55478,-72.41228],thn="Lot on the Sentier de l'Annexe (OpenStreetMap)",brick='no',conf='mixed'),

N('pont-couvert-saint-mathieu',"Pont couvert de Saint-Mathieu","Saint-Mathieu-du-Parc",'qc','landmark','standing',46.60303,-72.88393,'exact','public','drive','','1936',
  "A single-span covered bridge over the Shawinigan River, built in 1936 to the 'Town québécois' truss that the Quebec colonisation department used almost everywhere in the 20th century: Ithiel Town's 1820 lattice made lighter, nailed instead of pegged, with added posts. Of about 1,500 covered bridges built in Quebec between the early 1800s and the 1950s, it is one of the last in the Mauricie. Cited a heritage monument by the town.",
  "24.54 m long and 5.77 m wide: lattice trusses with single chords and vertical posts, horizontal board siding with openings at mid-height and under the top chord, slanted portal lintels, a plank deck, wooden abutments and a metal-covered gable roof (Register).",
  "",
  "On chemin de la Terrasse-des-Chutes (Register). Whether it still carries traffic was not checked. OpenStreetMap maps a lot about 55 m north, but on the aerial it looks like lawn by a house, so it is not given; park where the road allows.",
  [HP("Pont couvert de Saint-Mathieu",9779),LIST],
  brick='no'),

N('aluminerie-shawinigan',"Former Shawinigan aluminum smelter","Shawinigan",'qc','industry','standing',46.5396,-72.764,'site','view','walk','','1899–1927',
  "The first aluminum smelter in Canada and the oldest standing in North America, by the Register: built from 1899 by Charles Martin Hall's Pittsburgh Reduction Company with its own power plant at Shawinigan Falls, at the invitation of the Shawinigan Water and Power Company, and run by its Northern Aluminum Company. Canada's first aluminum ingot was cast in Building 7 in 1901, and its first aluminum cable made in Building 3 in 1902. The smelter ran until 1945. A national historic site.",
  "Twelve brick buildings of 1899 to 1927 on a height over the Saint-Maurice, many joined by passages, with a power plant on the bank below and the foundations of a second one (Register). OpenStreetMap names the buildings AL-2 to AL-22 at 1880 and 1882 promenade René-Lévesque. The Register says some have been made into galleries and event halls open to the public, and gives La Cité de l'énergie among the site's names; which buildings open, and when, was not checked.",
  "The oldest aluminum smelter left in North America.",
  "Promenade René-Lévesque, Shawinigan (OpenStreetMap; the Register gives 1 rue des Érables). Owner and opening times not checked; look from the street. Mapped lot at 1792 promenade René-Lévesque about 140 m southeast (OpenStreetMap).",
  [HP("Former Shawinigan Aluminum Smelting Complex National Historic Site of Canada",12043),LIST],
  th=[46.53873,-72.76273],thn="Lot on promenade René-Lévesque (OpenStreetMap)",brick='?'),

N('notre-dame-de-la-presentation-shawinigan',"Église Notre-Dame-de-la-Présentation (Ozias Leduc)","Shawinigan (Shawinigan-Sud)",'qc','worship','standing',46.52774,-72.75016,'exact','open','walk','','1924; painted 1942–1955',
  "A large Romanesque Revival stone church of 1924 overlooking the Saint-Maurice. From 1942 until his death in 1955 the painter Ozias Leduc, with his assistant Gabrielle Messier, covered its walls and ceiling with fifteen large paintings and painted ornament: nine biblical scenes, and six of local history, among them the vision and death of Father Buteux and the trades that built the Mauricie (farming, forestry, pulp and paper). It was Leduc's last work and, by the Register, the end of the great era of religious mural painting in Quebec. A national historic site.",
  "The whole painted interior: the fifteen paintings in a soft, Symbolist style tied together by ornamental bands, inscriptions and motifs painted straight on the walls and vaults (Register). Visited as 'Ozias Leduc en Mauricie', with self-guided and guided visits; the operator's site gives no hours that could be read.",
  "A painter's last work: a whole church interior about God, loggers and paper mills.",
  "823 avenue Ozias-Leduc (OpenStreetMap). Visits run by Ozias Leduc en Mauricie; its hours page answered 404 and its home page gives no times. Mapped lot on avenue du Capitaine-Veilleux about 120 m north (OpenStreetMap).",
  [HP("Church of Notre-Dame-de-la-Présentation National Historic Site of Canada",12766),
   L('Ozias Leduc en Mauricie','https://www.oziasleducenmauricie.com'),LIST],
  th=[46.52878,-72.75047],thn="Lot on avenue du Capitaine-Veilleux (OpenStreetMap)",brick='no',hours='?'),

N('eglise-champlain',"Église de Notre-Dame-de-la-Visitation","Champlain",'qc','worship','standing',46.44172,-72.34297,'site','view','walk','','1878–1879',
  "A stone parish church built in 1878 and 1879 by the architect-builder Gédéon Leblanc, almost a twin of his church at Saint-Stanislas (1870–1873), which copied the front of Saint-Barthélemy attributed to Victor Bourgeau; at Champlain Leblanc followed Bourgeau's front more closely. Facing the St. Lawrence back from the old Chemin du Roy, it heads a group with the cemetery, the old charnel house, the presbytery, the sexton's house, the church square and the old convent. Classified.",
  "A neoclassical front of five bays with an arcaded porch between two towers with two-lantern belfries. Inside, by the Register: a false barrel vault and half-dome, coffered aisle ceilings, Composite columns, trompe-l'oeil painting, works of the 17th, 18th and early 19th centuries including an old Roman-style altar tomb now used as the altar, stained glass, the original pews, two rear galleries and the organ. Tourisme Mauricie wrote in 2021 of summer guided visits with augmented-reality tablets; whether they still run was not checked.",
  "",
  "On rue Notre-Dame in the village. Service and visiting times not found on a page of whoever runs it. Mapped lot on rue Sainte-Anne beside the church (OpenStreetMap).",
  [HP("Église de Notre-Dame-de-la-Visitation",9339),
   L('Tourisme Mauricie: Église Champlain et réalité augmentée (2021)','https://tourismemauricie.com/blogue/eglise-champlain-realite-augmentee'),LIST],
  th=[46.44169,-72.34241],thn="Lot on rue Sainte-Anne (OpenStreetMap)",brick='no'),

N('magasin-general-le-brun',"Magasin général Le Brun","Maskinongé",'qc','civic','standing',46.2292,-73.0703,'site','open','drive','','1803–1916',
  "Three buildings that served as general stores from 1827 to 1974 at a once busy crossroads of the Chemin du Roy: a small store of 1803, moved from a nearby lot and joined to the house-store in 1862; the house-store of 1827, built for Eugène Trudeau; and the neoclassical big store of 1916, built by the Le Brun family, who owned it from 1901 to 1974. It also held the post office from 1873 to 1936. Recognised as a historic site.",
  "The house and the big store front the road side by side under one face of red brick; the big store has its front in the gable with a pediment on paired modillions, and the small log store with its back shop stands behind (Register). Tourisme Mauricie's listing describes a museum, boutique, the L'Grenier theatre, terrace and garden.",
  "A village general store that sold over the counter from 1827 to 1974.",
  "192 rang (route) du Pied-de-la-Côte. Its own website no longer answers (HTTP 404), so hours were not checked; the Tourisme Mauricie listing gives a telephone number. OpenStreetMap maps a lot about 80 m east that shows on the aerial as a bare patch by the road; parking not confirmed.",
  [HP("Magasin général Le Brun",5298),
   L('Tourisme Mauricie: Le Magasin général Le Brun','https://tourismemauricie.com/en/directory/le-magasin-general-le-brun-2'),LIST],
  brick='yes',hours='?'),

N('enfilade-maisons-brique-yamachiche',"Enfilade de maisons en brique rouge de Yamachiche","Yamachiche",'qc','town','standing',46.2822,-72.8308,'area','view','walk','','second half of the 19th century',
  "A row of twelve houses, most built in the second half of the 19th century, along the north side of the old Chemin du Roy (rue Sainte-Anne) facing the church and presbytery. Stone was scarce here and clay soils fed brickworks, so the well-off built in red brick; many houses were built or trimmed by the brothers Joseph and Georges-Félix Héroux (both 1830s–1901), sculptors and joiners trained by Alexis Millette and in Italy, who worked on many Quebec churches. Classified as a historic site in 2008; it includes the separately classified Maison Louis-Léon-Lesieur-Desaulniers.",
  "Red-brick houses of one and a half to two and a half storeys with white wood and cast-iron trim: varied roofs, dormers, balconies, pediments, bracketed cornices, friezes and balustrades in the Victorian eclectic manner (Register).",
  "A whole street front in red brick and white gingerbread.",
  "Private houses on rue Sainte-Anne; look from the street. Mapped lot on rue Sainte-Anne about 50 m southwest (OpenStreetMap).",
  [HP("L'Enfilade-de-Maisons-en-Brique-Rouge-de-Yamachiche",10188),HP("Maison Louis-Léon-Lesieur-Desaulniers",4320),LIST],
  th=[46.28175,-72.83108],thn="Lot on rue Sainte-Anne (OpenStreetMap)",brick='yes'),

N('pont-ducharme',"Pont Ducharme","La Bostonnais",'qc','landmark','standing',47.51989,-72.68109,'exact','public','drive','','1945–1946',
  "A single-span wooden covered bridge of 1945 and 1946 over the Bostonnais River, a late example of the 'Town élaboré' truss worked out by the Quebec colonisation department's engineers. It is named for Charles-Romulus Ducharme (1886–1976), a La Tuque lawyer and member of the Legislative Assembly for Laviolette, who opened it in 1948. Classified.",
  "41.76 m long and 6.55 m wide, with lattice trusses, red-painted clapboard siding and a gable roof (Register); a small park lies near it.",
  "",
  "On rue de l'Église, La Bostonnais (Register). Whether it still carries traffic was not checked. No mapped lot; park on the village streets.",
  [HP("Pont Ducharme",12000),LIST],brick='no'),

N('poste-incendie-police-shawinigan',"Poste d'incendie et de police no 2","Shawinigan",'qc','civic','standing',46.5541,-72.7435,'site','view','walk','','1922',
  "A Beaux-Arts fire and police station of 1922, one of the last big public buildings left from Shawinigan's golden age, when the industrial boom gave the town a city hall, a public market and fire and police stations that were later replaced. Recognised as a heritage monument in 2003.",
  "A brick main block flanked by two lower wings and a square tower, with a three-part front and classical trim (Register). Present use and interior not checked.",
  "",
  "2023 avenue Champlain. Look from the street. Parking not checked.",
  [HP("Poste d'incendie et de police Numéro-Deux-de-Shawinigan",1744),LIST],brick='?'),
]

PIN_NOTES={
 'forges-du-saint-maurice':"Register list point, beside the site's parking lot in woods and marsh; Wikipedia gives 46.3972, -72.6597. The ruins themselves could not be picked out on the leaf-off aerial, so the pin marks the general site (prec area); the remains are along the trails toward the Saint-Maurice.",
 'moulin-seigneurial-pointe-du-lac':"OpenStreetMap museum point at 11930 rue Notre-Dame Ouest; checked on the aerial.",
 'moulin-a-vent-trois-rivieres':"Coordinate from the Register list, on the UQTR campus; checked on the aerial.",
 'manoir-boucher-de-niverville':"OpenStreetMap museum point at 168 rue Bonaventure; checked on the aerial.",
 'vieille-prison-trois-rivieres':"OpenStreetMap museum point; checked on the aerial.",
 'maison-hertel-de-la-fresniere':"OpenStreetMap building, 802 rue des Ursulines; checked on the aerial.",
 'saint-james-trois-rivieres':"OpenStreetMap place-of-worship point, 811 rue des Ursulines; checked on the aerial.",
 'manoir-de-tonnancour':"OpenStreetMap building, 864 rue des Ursulines; checked on the aerial.",
 'vieux-presbytere-batiscan':"Coordinate from the Register list; checked on the aerial.",
 'centrale-saint-narcisse':"OpenStreetMap building named the annex of the old power station; checked on the aerial.",
 'pont-couvert-saint-mathieu':"OpenStreetMap bridge; checked on the aerial.",
 'aluminerie-shawinigan':"The Register list point (46.5312, -72.756) fell in the river 900 m away; moved to the middle of the OpenStreetMap buildings named AL-2 to AL-22 on promenade René-Lévesque.",
 'notre-dame-de-la-presentation-shawinigan':"OpenStreetMap place-of-worship point; checked on the aerial.",
 'eglise-champlain':"Register list point fell 46 m southeast of the church; moved with pix.py onto the church roof seen on the aerial.",
 'magasin-general-le-brun':"Coordinate from the Register list; checked on the aerial.",
 'enfilade-maisons-brique-yamachiche':"Register list point for the row; the pin marks the row on rue Sainte-Anne, not one house.",
 'pont-ducharme':"OpenStreetMap road named Pont Ducharme; checked on the aerial.",
 'poste-incendie-police-shawinigan':"Coordinate from the Register list; checked on the aerial.",
}
