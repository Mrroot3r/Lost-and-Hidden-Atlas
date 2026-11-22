# Pictures batch yfbh (2026-11-22, scheduled run)

## What this batch is

Pictures only, for 27 places already on the map that had none. No new places, no pins, no text. The tool wrote tools/pics_yfbh.py. Four rounds of `next 5` covered 20 places that had candidates from Commons; the other 7 Commons had nothing for and the tool recorded them as none by itself. The run stopped at the 40-minute limit set in the prompt, so about 30 was not reached.

Results: 13 places got a picture, 7 were set to none by me after looking, and 7 were recorded as none by the tool (Commons had nothing near the pin, under the name or in a category).

## How it was checked

Every sheet (research/photofind_<id>.jpg) was opened and looked at. Pictures were chosen only where the candidate's own name and description fit the place and the picture showed the building or site from outside. The credit and licence in the file were taken from Commons by the tool.

## Places where I hesitated

- salem-custom-house: several 2010 and 2024 frontal views; chose a 2024 wide view with the street, which shows the building as it stands.
- mohawk-street-houses-cohoes: the candidate is "Buildings on Mohawk Street", a brick house on the street, not named as the Van Auken house. It fits the street and the brick Second Empire type, but the exact house is not confirmed.
- auburn-prison-copper-john: the picture is of the Streamline Moderne Auburn Correctional Facility (1930s facade), not the 1816 original. It is the prison as it stands today, so it was chosen, but a reader may expect an older building.
- summerside-back-range-light: the photo's description says 1904, the place says built 1895 and closed in 1904. The shape and shingle cladding fit; the date difference is the photographer's, not checked.
- taku-glacier-lodge-twin-glacier-camp: chosen as "Taku Lodge June 2012 a"; it shows the lodge with a bear carving and sign, and small people in the far background.
- kessler-park-reservoir: 272 m from the pin, named "Cliff Drive yellow limestone ... by Reservoir". It shows a crumbling stone wall, which may be the old reservoir works, but this is not confirmed.
- marshall-methodist-church: the chosen photo is a night shot, dark, of a white church with a steeple, named "Methodist Church of Marshall". The shape fits the place's description; the photograph is poor.
- wellsville-erie-depot: the chosen photo is a modern view of the station with tracks and cars in front, not the 1911 construction photos on the sheet. The 1911 photos show the building being built and were not used.
- lidar-alder-brook-road-pit and minor-park-swales: none. Candidates were a valve panel, a plague-pit engraving, trail signs and a DAR stone marker; none shows the pit or the swales.
- powers-opera-house-site-lansingburgh: none. The one candidate is the Joy of Troy church, a different brick building.
- parker-woodland-ruins: none. The candidate is a house in Coventry, Rhode Island, not the ruins.
- oklahoma-state-bank-mulhall, suburban-park-unionville, silvery-slocan-museum: none. Candidates were a church, a Hopeton bank, the Unionville village and streetcar terminus, and rock specimens.

## Tips for the next session

Wikimedia answered 429 at the first check; it cleared on its own. A `look` command on five ids ran past the 2-minute default shell limit, so the sheets are the better way to see candidates again. The `set` text in the tool is written into the pics file as typed, so write a plain note. The rounds took about 4 to 8 minutes each.
