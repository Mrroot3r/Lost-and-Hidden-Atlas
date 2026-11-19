# November 16, 2026: a first pass at Central New York, where the Atlas had nothing within 35 miles of Syracuse.
# Seven works of the old Erie Canal and its Black River branch between Utica and Rochester, and the Split Rock quarry.
# Facts come from the linked Wikipedia articles, read through tools/wiki_raw.py. Where an article is silent the text
# says so and conf is set; nothing is filled in from memory.
# Ownership lines that say "public-land database" come from PAD-US (tools/pad.py) at the pin.
# Pins come from the article's coordinates or a named OpenStreetMap feature (tools/nom.py), as each pin note says.
from data_b import N
from data_ma import W
BATCH={'key':'cny','label':'Central New York','added':'2026-11-16 13:00'}
PLACES=[
N('five-lock-combine-boonville','Five Lock Combine, Black River Canal','Boonville','mohw','canal','ruins',43.40306,-75.36361,'site','public','walk','canal','about 1850–1924',
  'Seven locks of the abandoned Black River Canal in the Boonville gorge, five of them joined in one staircase, locks 39 through 43. The locks were first built about 1850 and rebuilt between 1887 and 1900; they took boats of 70 tons. The canal closed in 1924. The group was listed on the National Register in 1973.',
  'The five-lock staircase and locks 37 and 38. The article does not describe their condition.',
  'Five locks in a row on a canal shut since 1924.',
  'In Boonville Gorge Park. The public-land database shows state canal land and Buck Hill State Forest here, both open to the public. The article gives no parking or trail details.',
  [W('Five Lock Combine and Locks 37 and 38, Black River Canal')]),
N('chittenango-landing-dry-docks','Chittenango Landing dry docks','Chittenango','cny','canal','standing',43.06005,-75.87221,'site','public','walk','canal','1856–1917',
  'Three dry-dock bays built in 1856 on the enlarged Erie Canal for repairing canal boats. The yard was abandoned after the Barge Canal bypassed this stretch in 1917, and the land went to farming, the barn housing horses and cows. The docks were dug out again from 1986, and several buildings have been restored; one houses the Chittenango Landing Canal Boat Museum. The site was listed on the National Register in 1992.',
  'The three excavated dry docks beside the old canal, and the restored yard buildings.',
  'A canal-boat repair yard dug back out of a farm.',
  'On the Erie Canalway Trail, in Old Erie Canal State Historic Park by the public-land database. The article does not give the museum\'s hours.',
  [W('Chittenango Landing Dry Dock Complex')]),
N('syracuse-weighlock','Syracuse Weighlock Building','Syracuse','cny','canal','standing',43.05067,-76.14883,'exact','open','drive','canal','1850–1883',
  'Built in 1850 as a giant scale: canal boats floated in, were weighed, and paid their toll by the result. It worked as a weighlock until 1883, when the canal stopped charging tolls, and then had many other uses; by 1940 the state\'s Department of Public Works was in it. The Erie Canal Museum, founded in 1962, has occupied it since. It was listed on the National Register in 1971.',
  'The weighlock building, now the Erie Canal Museum.',
  'A building that weighed boats.',
  'A museum run by a private non-profit. The article does not give hours or admission.',
  [W('Erie Canal Museum')]),
N('split-rock-quarry','Split Rock quarry and munitions works','Onondaga','cny','industry','ruins',43.02745,-76.24818,'area','public','hike','','about 1834–1918',
  'Gilbert Coons opened a limestone quarry here around 1834. From 1880 the Solvay Process Company worked it on a large scale, sending the stone to its plant at Solvay by an elevated conveyor, until the quarry was abandoned about 1912. In 1915 the Semet-Solvay Company put a munitions factory on the site, with about 2,500 workers. On July 2, 1918 a fire that is said to have started at an overheated mixing motor in the main TNT building spread through the wooden factory, and it blew up. At least 50 men died; some reports say 52.',
  'Ruins in regrown woods, with man-made tunnels and natural limestone caves. The article does not list them one by one.',
  'A quarry that became a TNT plant and exploded in 1918.',
  'The quarry and factory remains are kept as a New York State Unique Area; other land round it belongs to the state and to Onondaga County. The pin is the middle of the Unique Area as OpenStreetMap maps it. The article gives no parking or trail details, and says nothing on whether the tunnels are safe or open: stay out of them.',
  [W('Split Rock, New York')],conf='mixed'),
N('nine-mile-creek-aqueduct','Nine Mile Creek Aqueduct','Camillus','cny','canal','standing',43.05899,-76.28567,'exact','public','walk','canal','1841–1917',
  'A stone and wood aqueduct that carried the Erie Canal over Nine Mile Creek, built in 1841 with a marine cement that was new at the time and has lasted. The towpath side stands on four arches. Work began in 2008 to rebuild the wooden trough so that it could hold water again, and in August 2009 boats crossed it for the first time since 1917. It was listed on the National Register in 1976.',
  'The restored aqueduct, with the canal watered on both sides of it.',
  'An 1841 aqueduct that carries boats again.',
  'In Camillus Erie Canal Park, on town land. A few hundred yards\' walk from a small parking area on Thompson Road, about a mile east of Sims\' Store.',
  [W('Nine Mile Creek Aqueduct')]),
N('centreport-aqueduct','Centreport Aqueduct','Weedsport','cny','canal','ruins',43.04278,-76.5775,'site','public','drive','canal','1857–1917',
  'A wood and stone aqueduct built in 1854–1857 to carry the Erie Canal over Cold Spring Brook, about 125 feet long and wide and 16 feet high. It was improved in 1895 and went out of use when the Barge Canal opened in 1917. The stonework is intact. The state\'s Department of Transportation and the Weedsport Lions Club made a roadside park round it in 1972, and it was listed on the National Register in 2000.',
  'The stone piers and walls of the aqueduct in a roadside park.',
  '',
  'Centerport Aqueduct Park, open to the public by the public-land database.',
  [W('Centreport Aqueduct')]),
N('erie-lock-52-port-byron','Erie Canal Lock 52 and the Erie House','Port Byron','cny','canal','standing',43.03694,-76.635,'site','public','drive','canal','1853–1917',
  'Lock 52 was built in 1849–1853 for the enlarged Erie Canal and worked until the canal was rerouted in 1917. Beside it stand the Erie House, a two-story frame saloon and hotel of 1894, and a blacksmith shop and mule barn. The complex, with a culvert and a length of the old canal bed, was listed on the National Register in 1998.',
  'The lock, the Erie House, the blacksmith shop and mule barn, and the dry canal bed.',
  'A canal lock with its saloon still next to it, at a Thruway rest area.',
  'A local historic park. It is reached from local streets or from a rest area on the eastbound side of the New York State Thruway.',
  [W('Erie Canal Lock 52 Complex')]),
N('richmond-aqueduct','Richmond Aqueduct and the Seneca River crossing','Montezuma','cny','canal','ruins',43.01005,-76.71903,'site','public','walk','canal','1857–1917',
  'Where the Erie Canal crossed the Seneca River. The district holds more than a mile of the enlarged canal\'s bed, built here between 1849 and 1857, with its towpath, a dry dock and a culvert, and the remains of the Richmond, or Montezuma, Aqueduct over the river. There are also remnants of the first canal of 1817–1825: its Lock 62 and the piers of its mule bridge. It was listed on the National Register in 2005.',
  'The surviving arches of the aqueduct, which the aerial shows running out into the river, the dry canal bed and towpath, and the older lock and bridge piers.',
  'Two generations of Erie Canal at one river crossing.',
  'State canal land, open to the public by the public-land database. OpenStreetMap maps the aqueduct on a path it names the Aqueduct Trail. The article gives no parking details.',
  [W('Seneca River Crossing Canals Historic District')]),
]
PIN_NOTES={
 'five-lock-combine-boonville':'The Wikipedia coordinate. The aerial shows a wooded river gorge with a road above it; the locks were not picked out under the trees.',
 'chittenango-landing-dry-docks':'The Chittenango Landing Canal Boat Museum as OpenStreetMap maps it (Erie Canalway Trail), 140 m from the Wikipedia coordinate. The ring sits on the yard buildings; rectangular bays show at the canal bank beside them.',
 'syracuse-weighlock':'The Wikipedia coordinate for the Erie Canal Museum; the ring sits on a building on a downtown block.',
 'split-rock-quarry':'The middle of the Split Rock Unique Area as OpenStreetMap maps it, not any one ruin. The Wikipedia coordinate is the hamlet, 1.4 km to the east. The aerial shows bare rock and paths in regrown woods.',
 'nine-mile-creek-aqueduct':'The aqueduct as OpenStreetMap maps it (waterway=canal), 25 m from the Wikipedia coordinate. The ring sits on the aqueduct where the canal crosses the creek.',
 'centreport-aqueduct':'The Wikipedia coordinate; the ring sits on stone piers across a brook, in a small park beside the road.',
 'erie-lock-52-port-byron':'The Wikipedia coordinate. On the aerial it falls beside the Thruway rest-area ramp, with a long narrow channel about 40 m to the northwest and buildings to the east; the lock was not told apart for certain.',
 'richmond-aqueduct':'The Richmond Aqueduct as OpenStreetMap maps it (man_made=bridge, Aqueduct Trail), about 560 m from the Wikipedia coordinate for the whole district. The ring sits on a row of arches running out into the river.',
}
