# November 25, 2026: a fourth pass over Lee's Summit, Raytown and Grandview, Missouri, and one school in south Kansas City.
# Earlier sessions had already worked this ground, so only two places were new and sourced: a 1909 firehouse and city hall in
# Lee's Summit (a Clio entry quoting the National Register form) and the Blenheim School (the National Register form itself,
# read in full from NPGallery). Nothing was checked on the ground.
from data_b import N
from data_ma import W

BATCH = {'key': 'kcmo_lsc_vxqe', 'label': "Lee's Summit and south Kansas City, Missouri (fourth pass)", 'added': '2026-11-25 00:51'}

PLACES = [
N('lees-summit-old-firehouse-city-hall-mo', "Lee's Summit Old Firehouse and City Hall (1909)", "Lee's Summit", 'kcmo', 'civic', 'standing',
  38.91142, -94.37844, 'exact', 'view', 'drive', '', '1909',
  "This brick building at 11 to 13 SW 3rd Street was put up in 1909 for the fire department and the city government together. The fire engines used the ground floor and the mayor's staff the second floor. "
  "City Hall moved out to the old post office (now the Lee's Summit History Museum) in the 1960s. Several fires had burned downtown buildings in the late 1800s, and the brick front reflects the change from wood to brick that followed.",
  look="The shaped parapet with its stone coping, the dentilled cornice and limestone quoins on the second storey, and \"1909\" near the top of the front. The wide doorway where the fire engines came out is now a shop door and window at number 13. "
       "The National Register form, as quoted in the Clio entry, says the upstairs window units are not original and the central door with its sidelights is gone. Interior not checked.",
  accn="Private shops on the ground floor, seen from the sidewalk on SW 3rd Street in the downtown historic district. Street parking nearby; no lot was checked. Shops keep their own hours.",
  links=[["Clio: Lee's Summit Old Firehouse and City Hall", 'https://theclio.com/entry/143748']],
  conf='', brick='?', hours=''),

N('blenheim-school-kc-mo', 'Blenheim School, 2411 E 70th Terrace, Kansas City', 'Kansas City', 'kcmo', 'civic', 'standing',
  38.99857, -94.55838, 'exact', 'view', 'drive', '', '1924–1930',
  "The Blenheim School was built in three stages, in 1924, 1927 and 1930, to the plans of the architect Charles A. Smith, with Miller-Stauch Construction as builder. "
  "It is a three-storey school on a hilltop block of 3.9 acres, in the Tudor Revival style, with brick walls over a stone foundation and cut-stone trim. "
  "It was listed on the National Register of Historic Places in 2017. The form describes it as vacant.",
  look="A large Tudor Revival school filling its own city block, with brick walls and stone ornament. The form's photographs show an auditorium on the second floor and a basement gymnasium; the building was empty when the form was written, so the inside is not open. "
       "Its present use and owner were not checked. A photograph on Wikimedia Commons shows dark red-brown brick with light stone trim.",
  accn="Look from the public sidewalks on E 70th Terrace and Olive Street; the building was vacant when listed and is not open to visitors. Street parking nearby; the OpenStreetMap parking point beside E 70th Terrace was not checked. Owner not checked.",
  links=[['National Register of Historic Places registration form, Blenheim School (2017)', 'https://npgallery.nps.gov/NRHP/GetAsset/NRHP/100001348_text']],
  conf='', brick='yes', hours=''),
]

PIN_NOTES = {
  'lees-summit-old-firehouse-city-hall-mo': "The ArcGIS address lookup for 13 SW 3rd Street; the pin check was run on the aerial.",
  'blenheim-school-kc-mo': "The National Register list gives the coordinate; the pin check was run on the aerial.",
}
