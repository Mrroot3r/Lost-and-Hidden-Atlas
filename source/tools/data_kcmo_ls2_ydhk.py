# November 26, 2026: south-east Jackson County and Cass County, Missouri (Raytown, Vale).
# Part of filling in the Kansas City area on purpose for a local researcher. Facts come from the linked sources only:
# Wikipedia read as raw text, Clio entries for Four Gates Farm and Richards Field, the Missouri State Parks trail page,
# bikerockisland.com for the trailhead address. The National Register forms for these places could not be read
# (the state's copies no longer open and the National Park Service copy is a placeholder). Nothing was checked on the ground.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_ls2_ydhk', 'label': 'Kansas City: Raytown and Vale', 'added': '2026-11-26 01:04'}

PLACES = [
N('four-gates-farm-kc-mo', 'Four Gates Farm (Oak Hill Farm)', 'Kansas City', 'kcmo', 'landmark', 'standing',
  38.99778, -94.42944, 'site', 'view', 'drive', '', '1925–1927',
  'Four Gates Farm is a country estate on Little Blue Road, east of the city, designed by the Kansas City architect Mary Rockwell Hook for her friend Marvin Gates and his family. '
  'Wikipedia says it was designed in 1925; Clio says Gates commissioned it from Hook and her partner Douglas Remington in 1925 and that it was finished in 1927. '
  'The listing covers the main house, a small stone farmhouse, a round stone tower with a conical roof and three stone outbuildings. Clio says its rural look is still intact.',
  look='A three-story house of brick and rubble stone with decks, balconies, porches and a round conical-roofed doorway, with a stone tower and stone outbuildings. Clio notes the living room has a raised stage area built for the owner\'s wife, who was an amateur actress. Interior not checked.',
  accn='Private property at 13001 Little Blue Road (the address Wikipedia gives); who owns it now was not found. Look from the public road only. No visiting hours or tours were found.',
  links=[W('Four Gates Farm'), ['Clio: Four Gates Farm', 'https://theclio.com/entry/145381']],
  conf='mixed', brick='some', hours=''),

N('vale-tunnel-rock-island-kc-mo', 'Vale Tunnel (Rock Island Railroad)', 'Kansas City', 'kcmo', 'rail', 'standing',
  38.9477, -94.43537, 'site', 'public', 'walk', 'stations', '1903–1905',
  'The Chicago, Rock Island and Pacific built this 441-foot tunnel under what is now Bannister Road. Wikipedia gives 1903 to 1904 for the building and its category lists the tunnel as completed in 1905. It was the last of four tunnels the railroad built, all in Missouri. '
  'After the Rock Island was liquidated in 1980 the line passed through several owners. Wikipedia says Jackson County bought it in 2016 and it became the Rock Island Rail Trail, with the tunnel lit as a centrepiece of the trail.',
  look='The lit tunnel on the Rock Island trail, which runs under Bannister Road. Most of the old line and the tunnel survive except where roads have cut through. Material of the portals not checked.',
  accn='A walking and cycling trail. Missouri State Parks lists it as Rock Island Trail State Park and its trail page, as a search result quoted it, says sunrise to sunset; Wikipedia says Jackson County bought the line in 2016, so which body manages this stretch was not settled. The nearest mapped trail lot is at the 98th Street (Vale) trailhead, 12600 E 98th Street, about 430 m south of the pin. Check the state parks trail advisory map for closures.',
  links=[W('Vale Tunnel'), ['Missouri State Parks: Rock Island Trail State Park hours', 'https://mostateparks.com/hours/431/park/rock-island-trail-state-park'], ['Rock Island 98th Street (Vale) Trailhead', 'https://bikerockisland.com/rock-island-98th-street-vale-trailhead-kansas-city.aspx']],
  conf='mixed', th=[38.944, -94.43689], thn='Rock Island Trail, 98th Street (Vale) trailhead', brick='?', hours='Sunrise to sunset'),

N('richards-field-raytown-mo', 'Richards Field (first Kansas City airport) and its marker', 'Raytown', 'kcmo', 'landmark', 'marker',
  38.99472, -94.47611, 'area', 'view', 'drive', '', '1922–1949',
  'Richards Field was opened in 1922 on the Kansas City and Raytown line, at the corner of Blue Ridge and Gregory boulevards, as the first commercial airport in the area. It was named for the Kansas City aviator John F. Richards II, killed in 1918. '
  'Kansas City opened its downtown airport in 1927 and the field was later called Ong Field. Wikipedia says it was abandoned in 1949 and became a subdivision, Gregory Heights; Clio says the lots were platted in 1952. A marker on East Gregory Boulevard, put up in 1979 by the Raytown Historical Society, tells the story (the marker itself says it became Ong Airport in 1943, where Wikipedia and Clio say around 1949).',
  look='Only the marker remains: the airfield is now streets and houses. The pin marks the corner the sources give for the field, not the marker, whose exact spot was not found.',
  accn='Public streets in a residential area. Park on East Gregory Boulevard or Blue Parkway and read the marker from the sidewalk; do not walk onto private yards. No hours.',
  links=[W('Richards Field'), ['Clio: Richard\'s Flying Field marker', 'https://theclio.com/entry/148953'], ['Historical Marker Database: Richards Flying Field', 'https://www.hmdb.org/m.asp?m=140273']],
  conf='mixed', brick='no', hours=''),

]

PIN_NOTES = {
 'four-gates-farm-kc-mo': 'The coordinate is the one Wikipedia gives for the farm; it has not been looked at on the aerial beyond the pin check.',
 'vale-tunnel-rock-island-kc-mo': 'The coordinate is the one Wikipedia gives for the tunnel under Bannister Road; the trailhead point is a lot OpenStreetMap maps about 430 m south.',
 'richards-field-raytown-mo': 'The pin is the corner of Blue Ridge and Gregory boulevards, where Wikipedia says the field stood; the marker\'s own spot was not found, so the pin marks the area. The aerial shows a commercial corner there, not the marker.',
}
