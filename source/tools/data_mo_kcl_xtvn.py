# November 25, 2026: a short batch of downtown Kansas City, Missouri buildings and the Leavenworth federal penitentiary that
# Wikipedia's building lists name and the Atlas lacked. Most of the Register lists round Kansas City were already on the map.
from data_b import N
from data_ma import W
BATCH={'key':'mo_kcl_xtvn','label':'Kansas City area: leftovers','added':'2026-11-25 03:51'}
CLIO='https://theclio.com/tour/2305/30'
PLACES=[
N('liquid-carbonic-building-kansas-city-mo','Liquid Carbonic Company Building, 2000 Baltimore, Kansas City','Kansas City, Missouri','kcmo','civic','standing',39.08917,-94.58444,'area','view','walk','','1913',
  'A six-story reinforced concrete building of 1913 with a red brick face, put up as the Kansas City branch of the Liquid Carbonic Company, a maker of soda fountains. It had a showroom, space for light manufacturing, warehouse room and offices for regional salesmen. The company left in 1935. The building has been on the National Register since 1994.',
  look='The pin marks the corner of 20th Street and Baltimore Avenue; the building is at 2000 Baltimore. Look at the street fronts from the sidewalk in the Crossroads district. Its use today, offices and a top-floor loft per the walking-tour page, is by private tenants; interior not checked and no public hours found.',
  accn='Privately owned and let to businesses; look from the public sidewalk. Street parking and paid lots in the Crossroads. No hours found: the building is not a visitor site.',
  links=[['Clio: Kansas City Crossroads walking tour, item 30',CLIO],W('Liquid Carbonic Company Building')],brick='yes'),
N('kansas-city-club-building-mo','Kansas City Club Building (Hotel Kansas City), Kansas City','Kansas City, Missouri','kcmo','civic','standing',39.09883,-94.58477,'exact','view','walk','','1918–1922',
  'A fourteen-story Gothic Revival clubhouse built from 1918 to 1922 for the Kansas City Club, a private club. The club used it until 2001, when it merged with a smaller one. A developer bought it in 2002 and turned the lower floors into a banquet hall and the upper nine into lofts. In 2020 it became the Hotel Kansas City. It has been on the National Register since 2002.',
  look='A tall masonry tower in downtown, best seen from the street. The hotel is open to guests; whether visitors may see the lobby or public rooms was not checked, and no source read gave original interior fabric.',
  accn='Privately owned hotel; look from the sidewalk. Paid garages and lots nearby. Hours not checked.',
  links=[W('Kansas City Club Building')],brick='?'),
N('leavenworth-federal-penitentiary-ks','Leavenworth federal penitentiary (FCI Leavenworth, the "Big Top")','Leavenworth, Kansas','ks','inst','standing',39.33,-94.93639,'site','view','drive','','1903',
  'One of three first-generation federal prisons begun in 1903, designed by the St. Louis firm Eames and Young, who also designed the Atlanta penitentiary. It was built by prisoners from the older military Disciplinary Barracks and was the largest maximum-security federal prison in the country until 2005, when it was downgraded to medium security. Its domed main building gave it the nickname the "Big Top." The walls are 40 feet high and enclose 22.8 acres.',
  look='A working federal prison. Visitors can only look at the dome and walls from public roads outside the grounds; do not stop on the approach or photograph staff. Wikipedia says a cemetery for deceased prisoners lies outside the walls; its public access was not checked.',
  accn='Federal Bureau of Prisons facility, closed to the public. View from public roads only; no hours.',
  links=[W('Federal Correctional Institution, Leavenworth')],brick='?'),
]
PIN_NOTES={
'liquid-carbonic-building-kansas-city-mo':'Wikipedia coordinate. On the aerial it falls in the street at 20th and Baltimore, so the pin marks the corner and not the building; the address is 2000 Baltimore.',
'kansas-city-club-building-mo':'Wikipedia coordinate, checked on the aerial.',
'leavenworth-federal-penitentiary-ks':'Wikipedia coordinate; on the aerial it sits on the central dome of the main cell house.',
}
