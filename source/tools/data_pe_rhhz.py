# November 19, 2026: Charlottetown and Queens County, Prince Edward Island: what the batch pe_bhrt (merged while this
# session worked on the same ground) does not have. Region pe drawn at random by tools/choose.py --claim; pe_bhrt came
# from a run limited to the eastern provinces. Sources opened in this session: the Canadian Register of Historic Places
# statement for each designated place (historicplaces.ca, read with tools/page.py --all; ids from the {{HPC row}}
# templates of the Wikipedia lists of historic places in Charlottetown and in Queens County); Wikipedia as raw text;
# the Diocese of Charlottetown's Mass-times table; OpenStreetMap and the ArcGIS geocoder for positions.
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
def HP(t,i): return ['Canadian Register of Historic Places: '+t,'https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=%d'%i]
BATCH={'key':'pe_rhhz','label':'More of Charlottetown and Queens County, Prince Edward Island','added':'2026-11-19 19:06'}
MASS=L('Diocese of Charlottetown: Mass times table, February 2026 (PDF)','https://dioceseofcharlottetown.com/wp-content/uploads/2026/02/Masstimesfec2426.pdf')
PLACES=[
N('charlottetown-city-hall','Charlottetown City Hall','Charlottetown','pe','civic','standing',46.23535,-63.12951,'exact','view','drive','','1888',
  'A three-storey red brick city hall in the Romanesque Revival style, designed by Phillips and Chappell and built in 1888 by W. H. Fraser, when Charlottetown was growing and prosperous. Like many town halls of its time it held everything at once: a police station, fire hall and stable on the ground floor, and the council chamber, a court room and offices above. It was made a national historic site in 1984.',
  'A high square corner tower, deep-set windows under round arches, large gables, brick corbel tables under the eaves, bands of contrasting brick and a stone string course; inside, the council chamber ceiling survives (Register). Whether visitors may go in was not checked.',
  'Police, fire horses and the council under one red roof.',
  'City offices at 199 Queen Street, corner of Kent Street (ArcGIS address point). Look from the street; whether the public may go inside was not checked.',
  [HP('Charlottetown City Hall National Historic Site of Canada',4140)],brick='yes'),
N('apothecaries-hall-charlottetown','Apothecaries Hall','Charlottetown','pe','civic','standing',46.2347,-63.1281,'site','view','drive','','1900',
  'A three-storey brick shop on a downtown corner, built in 1900 as an apothecary to replace an earlier building that did the same job. A pharmacy worked on this site from 1810 to 1986, which made it one of the longest-running in Canada and the reason it was made a national historic site in 1969. Shops now use the ground floor and offices the upper two.',
  'Banded brick facing with a decorative brick cornice, large shop windows and a corner door; inside, original woodwork and a tin ceiling (Register). The photograph on Wikipedia\'s list of national historic sites in the province is captioned red and buff brick.',
  '176 years of medicine sold from one corner.',
  'Private, shops and offices. Look from the street.',
  [HP('Apothecaries Hall National Historic Site of Canada',1157),W('List of National Historic Sites of Canada in Prince Edward Island')],brick='yes'),
N('great-george-street-charlottetown','Great George Street Historic District','Charlottetown','pe','town','standing',46.2337,-63.1245,'area','public','walk','','1864',
  'Six blocks of Great George Street climbing gently from Peake\'s Quay on the waterfront to Province House. The delegates to the Charlottetown Conference came ashore at the quay on August 31 and September 1, 1864 and walked up this street to the meetings; roughly half of the buildings along it date from that time. It was made a national historic site in 1990.',
  'A wide street of houses and inns of like height and setback in British classical, Neoclassical, Italianate, Queen Anne Revival and Gothic Revival styles (Register), with St. Dunstan\'s Basilica halfway up and Province House at the top. Walk it from the waterfront uphill, as the delegates did.',
  'Walk the street the Fathers of Confederation walked.',
  'City street, open any time. Pin is the middle of the district.',
  [HP('Great George Street Historic District National Historic Site of Canada',15381)],brick='?'),
N('st-augustines-church-rustico',"St. Augustine's Church",'Rustico','pe','worship','standing',46.4235,-63.2845,'site','open','drive','','1838',
  'The oldest parish church in the Diocese of Charlottetown, begun in the fall of 1838 under Bishop Bernard MacDonald by local Acadian craftsmen with local materials, replacing churches of 1795 and 1806. It served as pro-cathedral until a church was built in Charlottetown. Its three bells were cast in London and bought under Father Belcourt (1859–1869), who founded the Farmers\' Bank next door; Robert Harris drew Acadian nuns at prayer inside it.',
  'A white wooden church with black Gothic trim, paired multi-paned Gothic windows, quatrefoil woodwork, and a front tower with corner finials that seems to have been moved from the side after 1880 (Register). Interior not checked.',
  'The diocese\'s oldest church, built by Acadian hands.',
  'Active parish, Church Road. The diocese\'s Mass-times table of February 2026 lists Masses at 7 p.m., 9 a.m. and 10:30 a.m., but the days could not be read from the table; the parish\'s own page gave no times. Parking shared with the Farmers\' Bank lot.',
  [HP("St. Augustine's Roman Catholic Church",1831),MASS],th=[46.42303,-63.28376],thn='Lot on Church Road (OpenStreetMap)',brick='no',hours='?'),

N('north-rustico-lighthouse','North Rustico Lighthouse','North Rustico','pe','light','standing',46.4553,-63.2918,'site','view','drive','','1876',
  'A lighthouse with its keeper\'s house attached, designed by the federal Department of Marine and Fisheries in 1876 to guard the young fishing industry of North Rustico. It was moved in 1884, 1899 and 1914, and nearly destroyed by a winter storm in 1899 before local people saved it. When a new light was built in 1973 residents fought for this one too, and it was lit again by 1976, its centenary. George Pineau was the last resident keeper, from 1925 until automation in 1960.',
  'A two-storey tapered tower with a red iron lantern on brackets and a railed deck, joined to a gabled keeper\'s house with a brick chimney; original four-over-four windows with red-painted caps (Register). The Register names it one of four island lighthouses that keep an attached keeper\'s house, with New London, Wood Islands and Blockhouse Point. Interior not checked.',
  'A lighthouse its village saved twice.',
  'At the harbour of North Rustico; the Register says the Friends of North Shore Communities work to preserve it. Owner and whether it ever opens not checked: look from outside. Parking not checked.',
  [HP('North Rustico Lighthouse',19724)],conf='mixed',brick='?'),
N('uigg-baptist-church','Uigg Baptist Church','Uigg','pe','worship','standing',46.17787,-62.82418,'exact','view','drive','','1874',
  'A plain clapboard meeting house built in 1874 for Scottish settlers who came in 1829 from Uig on the Isle of Skye, kin of the Selkirk settlers of 1803. The Register calls it a rare example on the island of a "Scotch Baptist" meeting house; it replaced a building of 1852, and before that services were held in members\' homes. Neil MacLeod, premier of the province from 1889 to 1891, came from this congregation.',
  'Sets of three Gothic Revival windows with glazing bars and original glass on each side, a triangular Gothic window above the front door, pegged (not nailed) rafters inside, and the original pews and organ (Register). The Uigg cemetery is beside it.',
  'A Skye Baptist meeting house with its pews still in place.',
  'Closed as a church "for some time" (Register); owner and any opening not checked. Look from the road.',
  [HP('Uigg Baptist Church',1633)],brick='no'),
N('glenaladale-house','Glenaladale House','Tracadie Cross','pe','landmark','standing',46.3606,-62.9688,'area','view','drive','','1883–1884',
  'A large two-storey brick Georgian house on an estate by Tracadie Bay, built in 1883–1884 by Sir William Macdonald, the Montreal tobacco magnate and benefactor of McGill, for his brother John Archibald MacDonald, very likely to designs by the Montreal architect A. C. Hutchinson. It stands on the farm their grandfather Captain John MacDonald of Glenaladale began in 1771, after bringing Highland Catholic settlers here in 1772. The great barn built with it, 277 by 52 feet, burned in 1907; since then the MacKinnon family has owned it, once running a silver fox ranch.',
  'Island brick walls under a hipped roof with dormers, four brick chimneys, window lintels, a wooden verandah and a kitchen wing (Register). Whether the house can be seen well from a public road was not checked. Interior not checked.',
  'A tobacco fortune\'s brick house on a 1771 Highland farm.',
  'Private, owned by the MacKinnon family (Register). Look from the public road only.',
  [HP('Glenaladale House',19511)],brick='?'),
N('dundas-terrace-charlottetown','Dundas Terrace','Charlottetown','pe','landmark','standing',46.2301,-63.1277,'site','view','walk','','1889',
  'A three-and-a-half-storey wooden apartment building of 1889 on Water Street, designed by W. C. Harris in the Queen Anne Revival style to look like a single large house. The Register calls it an early purpose-built apartment building and a rare one built of wood; it was made a national historic site in 1990.',
  'Advancing and receding bays, a steep half-hipped roof with a big cross-gable and many dormers, verandahs and porches, and a mix of clapboard, shingle and board-and-batten with a flare at the second floor (Register). Interior not checked.',
  'An apartment block dressed as a Queen Anne house.',
  'Private apartments on Water Street. Look from the street.',
  [HP('Dundas Terrace National Historic Site of Canada',7412)],brick='no'),
N('fairholm-charlottetown','Fairholm','Charlottetown','pe','hotel','standing',46.23842,-63.12721,'exact','open','drive','','1839',
  'A brick villa of 1839 built for the politician and administrator T. H. Haviland Sr., made a national historic site in 1992 as a fine and rare Picturesque villa in Atlantic Canada and a rare early brick building on the island. A late-19th-century carriage house stands with it. OpenStreetMap maps it as an inn, the Fairholm National Historic Inn, at 230 Prince Street.',
  'Mottled red brick walls with cut stone lintels, basement and string course; bowed windows running the full height of the front; a central door with sidelights and an elliptical fanlight; inside, ceiling rosettes, wide cornices, mantelpieces and round-arched openings in the upper hall (Register).',
  'A curved-front brick villa of 1839, now an inn.',
  'Run as an inn according to OpenStreetMap; its own page was not read, so hours and whether non-guests may look in were not checked. 230 Prince Street.',
  [HP('Fairholm National Historic Site of Canada',1138)],brick='yes',hours='?'),
N('victoria-playhouse-hall','Victoria Community Hall (Victoria Playhouse)','Victoria','pe','civic','standing',46.21499,-63.49128,'exact','open','walk','','1915',
  'A shingled community hall with a gambrel roof, built in 1915 by Win Bradley, a carpenter from Kelly\'s Cross, at the corner of Howard and Main streets in the village of Victoria. It held Women\'s Institute meetings from 1921, lobster suppers, concerts and quilting bees, and was used for recruiting in both wars; Don Messer and Anne Murray played here. Since 1982 it has been the Victoria Playhouse theatre. The gable-roofed entrance was replaced by a larger gambrel addition in 2004.',
  'The gambrel roof, shingles, a rose window in the gable, tall paired windows with original glass and casements, millwork over doors and windows, and the original sandstone bed under the building; tablets for the area\'s war service on the east side (Register).',
  'A 1915 village hall that became a summer theatre.',
  'A working theatre, 20 Howard Street (OpenStreetMap). The Playhouse\'s page speaks of a summer season but no times were read: hours not checked. Victoria\'s public lot on Causeway Road is a short walk (OpenStreetMap).',
  [HP('Victoria Community Hall',7431),L('Victoria Playhouse','https://victoriaplayhouse.com/')],th=[46.21364,-63.48919],thn='Public parking, Causeway Road (OpenStreetMap)',brick='no',hours='?'),
]
PIN_NOTES={
 'charlottetown-city-hall':'ArcGIS PointAddress for 199 Queen Street, matching the OpenStreetMap town hall point.',
 'apothecaries-hall-charlottetown':'Register list coordinate.',
 'great-george-street-charlottetown':'Register list coordinate, the middle of the district.',
 'st-augustines-church-rustico':'Register list coordinate for the church.',

 'north-rustico-lighthouse':'Register list coordinate; not found in OpenStreetMap. On the aerial it is beside a small building on the shore road at the harbour mouth, taken to be the lighthouse but not confirmed.',
 'uigg-baptist-church':'The Register list point was on the road; moved about 20 m west with pix.py onto the small white building among the graves of the cemetery.',
 'glenaladale-house':'Register list coordinate; on the aerial it falls on a road junction at Tracadie Cross and the house was not picked out, so prec is area.',
 'dundas-terrace-charlottetown':'Register list coordinate on Water Street; on the aerial it is at the street edge beside a large house, not confirmed as the building.',
 'fairholm-charlottetown':'OpenStreetMap point for the Fairholm inn, 30 m from the Register list point.',
 'victoria-playhouse-hall':'OpenStreetMap theatre point, 20 Howard Street.',
}
