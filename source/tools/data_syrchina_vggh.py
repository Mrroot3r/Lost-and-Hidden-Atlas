# November 24, 2026: Syracuse China (the Onondaga Pottery Company, "O.P. Co.") in and round Syracuse, New York, asked for
# by the owner, who wants to film a visit to what is left. Sources opened in this session: Wikipedia as raw text
# (Syracuse China, Geddes, Onondaga Historical Association), the Onondaga Historical Association's own pages (company
# history, World War II article, Syracuse China programme page, the downtown museum's visit page, its own history), a
# 2012 YNN article kept by the association, the Abandoned America page on the plant, a 1996 state environmental fact
# sheet on the plant's landfill, the Restaurant Ware Collectors Network's date-code page, and OpenStreetMap.
# The original works on West Fayette Street could not be placed: no source opened gave an address (see the note's Leads).
from data_b import N
from data_ma import W
def L(t,u): return [t,u]
BATCH={'key':'syrchina_vggh','label':'Syracuse China (Onondaga Pottery Company), Syracuse, NY','added':'2026-11-24 03:53'}
OHA=L('Onondaga Historical Association: Syracuse China company history','https://www.cnyhistory.org/2020/04/syracuse-china-history/')
PLACES=[
N('syracuse-china-plant-lyncourt','Syracuse China plant site (Onondaga Pottery Company, Court Street works)','Lyncourt','cny','industry','gone',43.08693,-76.12904,'area','view','drive','','1921–2012',
  'The Onondaga Pottery Company, founded in 1871 in Geddes and renamed Syracuse China in 1966, built a second plant here on Court Street to make its hotel ware; the Onondaga Historical Association calls it the first linear, one-storey plant in the American china industry. The association gives its opening as 1921; Wikipedia, as quoted by Abandoned America, gives June 7, 1922; ware stamped with Court Street date codes begins in January 1923. Libbey, which owned the company, shut the plant on April 9, 2009, putting its last 275 workers out of a job, and the empty factory was torn down in April 2012.',
  'Most of the factory is gone: the ground is now a commercial plaza, with a truck centre and a paper plant on part of the old footprint, according to Abandoned America. The entry drive from Court Street is mapped as Pottery Road. Whether any of the buildings standing on the site today is a piece of the old plant was not checked. North of the railroad, south of Factory Avenue, is the company\'s old landfill, capped under a 1996 state cleanup plan. The company\'s records, tools and tens of thousands of pieces of ware went to the Onondaga Historical Association, whose downtown museum has a permanent Syracuse China exhibit.',
  'Where America\'s railroad dining-car china was made, now a truck lot on Pottery Road.',
  'Private commercial land in the Town of Salina, with working businesses: look from Court Street (Route 298) and do not go onto the lots. Abandoned America and Wikipedia give the address as 2801 Court Street; the pin is the OpenStreetMap address point for it. No public parking at the site; the nearest mapped public lot is at Sehr Park on Marsden Road, about 350 m north-west (the park\'s rules not checked).',
  [OHA,W('Syracuse China'),
   L('Onondaga Historical Association: Syracuse China in World War II','https://www.cnyhistory.org/2017/01/syracuse-china/'),
   L('YNN, April 6, 2012: the Syracuse China building torn down (Onondaga Historical Association copy)','https://www.cnyhistory.org/wp-content/themes/oha/press/2012-04-06-YNN-SC.pdf'),
   L('Abandoned America: Syracuse China','https://www.abandonedamerica.us/syracuse-china'),
   L('NYS DEC fact sheet, May 1996: Syracuse China landfill (site 7-34-053)','https://extapps.dec.ny.gov/data/DecDocs/734053/Fact%20Sheet.HW.734053.1996-05-01.ROD%20Fact%20Sheet.pdf'),
   L('Restaurant Ware Collectors Network: Syracuse China date codes','https://rwcn-idwiki-2.restaurantwarecollectors.com/date-codes-syracuse-opco/')],
  conf='mixed',th=[43.08826,-76.13264],thn='Sehr Park lot, Marsden Road (public park)',brick='?'),
N('onondaga-historical-museum-syracuse','Onondaga Historical Museum (Syracuse China exhibit)','Syracuse','cny','civic','standing',43.04788,-76.14915,'exact','open','walk','','',
  'The Onondaga Historical Association, founded in 1862, has had its museum since about 1980 in a former telephone company building at 321 Montgomery Street, bought with Onondaga County; its older home next door, number 311, built in 1895 or 1896 for the Central New York Telephone & Telegraph Company, was sold in 2005. When Syracuse China closed in 2009 the association took in the company\'s business records, designs, tools and tens of thousands of pieces of ware.',
  'A permanent Syracuse China exhibit of the most significant pieces, beside the museum\'s Onondaga County history galleries; spare unaccessioned ware is sold in the gift gallery. The museum is the six-storey pale-faced Bell Telephone Building (Wikimedia Commons photographs, 2018 and 2024); its building date and interior fabric were not checked. The 1890s former telephone building at 311 Montgomery Street, the association\'s home from 1905 to 2005, stands next door.',
  'The company archive and the china itself, in the museum downtown.',
  'Run by the Onondaga Historical Association, a non-profit. Its visit page gives the museum hours below; admission to the temporary exhibition in November 2026 was free (other admission not checked). The research centre was closed for renovation in November 2026. The association suggests street parking on Fayette Street and Montgomery Street on weekdays. Main entrance on the left of the front; the accessible entrance is on the right, with a bell.',
  [L('Onondaga Historical Association: visit the downtown museum','https://www.cnyhistory.org/visit/downtown/'),
   L('Onondaga Historical Association: Syracuse China','https://www.cnyhistory.org/programs/syracusechina/'),
   OHA,L('Onondaga Historical Association: our history','https://www.cnyhistory.org/our-history/'),
   W('Onondaga Historical Association')],
  brick='no',hours='Wednesday to Saturday 10 a.m. to 4 p.m., Sunday 11 a.m. to 4 p.m.'),
]
PIN_NOTES={
 'syracuse-china-plant-lyncourt':'OpenStreetMap address point for 2801 Court Street. On the state aerial it falls on a long standing building in the middle of the plaza, beside a large cleared slab to the west; which of these was the old plant was not settled, so the pin marks the general ground. The parking point is the lot beside the tennis courts in Sehr Park, a public park, not at the site.',
 'onondaga-historical-museum-syracuse':'OpenStreetMap point for the museum at 321 Montgomery Street.',
}
