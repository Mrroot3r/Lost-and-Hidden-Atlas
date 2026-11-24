# November 24, 2026: Blue Springs, Lee's Summit, Grandview and Garden City, Missouri (south and east of Kansas City). A third pass
# over ground earlier sessions had already worked, so only what they left. Facts from the linked pages read in this session:
# a KSHB news report, Clio entries, the Grandview Residential Historic District's description on Waymarking (quoting the
# National Register nomination), Wikipedia as raw text, and a Lee's Summit parks page. The National Register forms themselves
# could not be read (NPGallery holds a placeholder and the Missouri State Parks copies answer 404). Nothing was checked on the ground.
from data_b import N
from data_ma import W

PLACES = [
N('chicago-alton-house-blue-springs-mo', 'Chicago & Alton House (first hotel), Blue Springs', 'Blue Springs', 'kcmo', 'hotel', 'standing',
  39.01828, -94.28221, 'area', 'view', 'drive', '', '1878',
  'The Chicago & Alton House stands at 1506 West Main Street, west of the railroad tracks. Wikipedia dates it to 1878 and calls it the oldest business in Blue Springs. '
  'A local news report says the historical society\'s president named J. K. and Isabel Parr, the town\'s first residents, as its builders. It was named for the passenger rail line, and travellers stayed here before settling in town. '
  'It has been empty and falling apart for decades, and the report says it has never had electricity or water.',
  look='A small vacant frame hotel by the old railroad line, shut up and waiting for repair. The Blue Springs Historical Society was raising money (about $200,000, in the report) to rebuild it from the floors up for events and tours. Interior not checked.',
  accn='Looked at from West Main Street only. The report says the building is being restored by the Blue Springs Historical Society, which does not say it is open: look from the street and do not go onto the lot or into the building. Street parking not checked.',
  links=[['KSHB: Blue Springs Historical Society fundraising to restore the city\'s first hotel', 'https://kshb.com/news/local-news/this-started-blue-springs-blue-springs-historical-society-fundraising-to-restore-citys-first-hotel'], W('Blue Springs, Missouri')],
  conf='mixed', brick='?', hours=''),

N('dillingham-lewis-museum-blue-springs-mo', 'Dillingham-Lewis Museum (Blue Springs Historical Society), Blue Springs', 'Blue Springs', 'kcmo', 'landmark', 'standing',
  39.01828, -94.28175, 'area', 'open', 'drive', '', '',
  'Morgan Dillingham, a Confederate veteran who ran a general store and became a bank president, and his wife Melvina built their home at 15th and Main in Blue Springs. '
  'It was later owned by Narra Lewis, who sold it in 1977 to the Blue Springs Historical Society, and it is now the society\'s museum. '
  'A paranormal-investigation group\'s write-up, the only history of the house read, says the rooms are set out in the style of the early 1900s with furnishings that did not belong to the house. The year it was built is not given in anything read.',
  look='A period house museum next to the old Chicago & Alton House. Furnishings are not original to the house. What the museum shows beyond that was not checked.',
  accn='Run by the Blue Springs Historical Society. A map listing puts the society at 101 SW 15th Street, and another says guided tours run April to December; neither gave days or times, and the society\'s own page could not be opened. Call or check the society before going. Street parking not checked.',
  links=[['Paranormal group\'s write-up of the house history (Dillingham-Lewis Museum)', 'https://kcghosts.com/dillingham-lewis-museum']],
  conf='mixed', brick='?', hours='?'),

N('todd-george-house-lees-summit-mo', 'Todd M. George Sr. House, Lee\'s Summit', 'Lee\'s Summit', 'kcmo', 'landmark', 'standing',
  38.9141, -94.37126, 'site', 'view', 'drive', '', '1916',
  'Todd and Florie George built this Craftsman house on a double lot in 1916. George (1887 to 1969) was a real estate developer who built subdivisions, downtown brick buildings and roads, '
  'served as mayor three times (one term ended in impeachment and a re-election), and founded the town\'s first waterworks. The house was listed on the National Register on February 12, 2010. '
  'Clio says his later reputation has turned on his opposition to civil rights, and that the city council voted to rename Todd George Parkway.',
  look='A two-story Craftsman house with a wide porch on a double lot, in a neighbourhood of early 1900s houses. It is a private home: look from the street. Interior not checked.',
  accn='Private residence at 408 SE 3rd Street. Look from the public street only; do not go onto the property. The pin is the ArcGIS address point for that street address.',
  links=[['Clio: Todd M. George, Sr., House', 'https://theclio.com/entry/143707'], ['National Register record (NRIS 10000007)', 'https://historypointer.com/nris/resource/10000007']],
  brick='?', hours=''),

N('grandview-residential-district-mo', 'Grandview Residential Historic District, Grandview', 'Grandview', 'kcmo', 'town', 'standing',
  38.88747, -94.53383, 'area', 'view', 'drive', '', '1900–1924',
  'About 10.8 acres south and east of Grandview\'s old commercial centre, along Highgrove Road, a short stretch of Grandview Road and 10th Street. '
  'The National Register nomination, quoted on Waymarking, counts 28 contributing houses and describes them as built mainly in the first quarter of the 1900s, in Craftsman and bungalow, Tudor Revival, Colonial Revival, Queen Anne and Mission Revival styles. '
  'It was listed in 2005.',
  look='Houses of brick, stone, stucco and wood siding on a few residential blocks, most still in good repair according to the same description. Private homes: walk the public streets. Interiors are not open.',
  accn='Private homes on public streets (807 to 1111 Highgrove Road, 13016 to 13020 and 13019 Grandview Road, 13006 to 13018 10th Street). Look from the sidewalk; parking on the street not checked. The pin is the point Waymarking gives for the district and marks the area only.',
  links=[['Waymarking: Grandview Residential Historic District (quotes the nomination)', 'https://www.waymarking.com/waymarks/WMHZ23_Grandview_Residential_Historic_District_Grandview_Missouri']],
  conf='mixed', brick='?', hours=''),

]

PIN_NOTES = {
  'chicago-alton-house-blue-springs-mo': 'ArcGIS address point for 1506 West Main Street, the address the news report gives. On the aerial the pin falls on a small building among houses; which one is the hotel could not be told apart, so it marks the area.',
  'dillingham-lewis-museum-blue-springs-mo': 'ArcGIS address point for 101 SW 15th Street, the society\'s address on a map listing; it sits beside the Chicago & Alton House and the two could not be told apart on the aerial, so it marks the area.',
  'todd-george-house-lees-summit-mo': 'ArcGIS address point for 408 SE 3rd Street; on the aerial it falls on a building among offices and apartments, so the pin marks the site and the house was not picked out.',
  'grandview-residential-district-mo': 'Point given on Waymarking for the district; marks the area only.',
}

BATCH = {'key': 'kcmo_lsb_hvtn', 'label': 'Blue Springs, Lee\'s Summit and Grandview, Missouri', 'added': '2026-11-24 10:49'}
