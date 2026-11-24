# November 24, 2026: Lenexa Old Town and two monuments at Olathe and Overland Park, Johnson County, Kansas (fourth pass).
# Johnson County's Register listings were used by earlier batches, so these come from the Lenexa Historical Society's own
# pages on its historic buildings and from the Clio driving tour of Olathe, Overland Park and Shawnee.
from data_b import N
LHS='https://lenexahistoricalsociety.org/'
CLIO='https://theclio.com/tour/1012/%d'
BATCH={'key':'ks_lnxa_qprd','label':'Lenexa Old Town and two Johnson County monuments','added':'2026-11-24 08:54'}
PLACES=[
N('krumm-building-lenexa-ks','Krumm Building','Lenexa, Kansas','ks','civic','standing',38.96082,-94.74182,'site','view','drive','','1910',
  'Louis O. Krumm built this two-storey limestone store in 1909 and 1910 next to his father Matthias Krumm\'s blacksmith shop of 1875. The stone came from Max Zahner\'s quarry less than a mile north of town; the masons finished in February 1910 and the building was open by the end of April. Krumm\'s Store was on the ground floor and Krumm Hall, used for fundraisers, music and political meetings, was upstairs. The family sold groceries here until about 1967.',
  'Walls of local limestone, 30 by 70 feet. After later use by the VFW, a furniture store and law firms, the owner renovated it in 2019 and 2020, refinishing the original floors, exposing some original structural supports and showing the stone walls inside. Offices and a window showroom use it now; the Historical Society page does not say whether visitors may walk in.',
  'A 1910 general store and dance hall in rough local limestone, the best-kept building of Old Town.',
  'Private business premises on Santa Fe Trail Drive in Old Town Lenexa; look from the sidewalk. Street parking in Old Town (not checked). Business hours and whether the public may enter were not read.',
  [['Lenexa Historical Society: The Krumm Building',LHS+'the-krumm-building-in-lenexa'],['Lenexa Historical Society: historic locations',LHS+'historic-locations']],
  brick='no'),
N('farmers-state-bank-ryckerts-lenexa-ks','Farmers State Bank building (Ryckert\'s Market)','Lenexa, Kansas','ks','civic','standing',38.96026,-94.74195,'area','view','drive','','1923',
  'The Farmers State Bank, founded by E. H. Haskin in 1904, opened this two-storey brick building on May 14, 1923, at a cost of $40,000. It held the bank and a grocery on the ground floor and an opera house and movie theatre upstairs, with Haskin\'s wife Maud playing the piano for silent films. The bank moved out in 1963. Ryckert\'s Market, a family grocery that began in 1929, took over the corner and ran until June 1993. The building was threatened when a nearby building burned in 1972.',
  'A brick building on the corner of Santa Fe Trail Drive and Pflumm Road. The Historical Society says it has been a landmark for more than 100 years. Tenants now include a dance studio and Sincerely Susan\'s, a shop. What of the upstairs theatre survives was not read.',
  'The corner brick block of Old Town, a bank, a grocery and a silent-film theatre in one.',
  'On the corner of Santa Fe Trail Drive and Pflumm Road in Old Town Lenexa, privately owned, with shops inside that keep their own hours (not read). Look from the sidewalk.',
  [['Lenexa Historical Society: Ryckert\'s Market Building',LHS+'historic-locations/brick-building-lenexa-ryckerts']],
  brick='yes',conf='mixed'),
N('haskin-home-lenexa-ks','E. H. Haskin Home','Lenexa, Kansas','ks','landmark','standing',38.95735,-94.74233,'site','view','drive','','1904',
  'Frank Legler built this Dutch Colonial house in 1904 for $7,000 for E. H. Haskin, who co-founded the Farmers State Bank that year, was mayor in the 1920s and is said to have been the first person in Lenexa with a car. The house stood on six acres. The Haskin family kept it until 1964, and businesses used it from the 1990s.',
  'A Dutch Colonial house in Old Town. A Historical Society page described renovation for an autism-services group, keeping the wood floors, most pocket doors and the stairs, with a new addition on the west side. The page is undated, so the finished state was not checked.',
  'A banker\'s 1904 house, kept for its stairs and pocket doors.',
  'Private property on Pflumm Road in Old Town Lenexa; look from the public sidewalk. Whether it opens to visitors was not checked.',
  [['Lenexa Historical Society: E.H. Haskin Home',LHS+'historic-locations/e-h-haskin-home']],
  brick='?',conf='mixed'),
N('santa-fe-trail-marker-olathe-courthouse-plaza-ks','Santa Fe Trail marker, Olathe Courthouse Plaza','Olathe, Kansas','ks','curio','standing',38.88215,-94.82056,'area','public','drive','','1907',
  'The Johnson County Old Settlers Society paid for this monument to the Santa Fe Trail and had it set in the old courthouse yard in Olathe on September 7, 1907, during a meeting held for Olathe\'s fiftieth anniversary. It carries one of six bronze plaques the Kansas Daughters of the American Revolution ordered, but it is not counted among the 96 trail markers the Kansas DAR put up that year.',
  'The 1907 marker with its bronze plaque in a small plaza near where the first courthouse stood. The plaza also holds courthouse monuments, time-capsule markers and a modern fountain sculpture by Kwan Wu.',
  'A 1907 trail stone in the yard of the county seat.',
  'A plaza by the Johnson County Courthouse at 100 N. Kansas Avenue; Clio says the stone was set in the courthouse yard, so the ground belongs to the county. Open ground by the street (the address lookup gave the courthouse; the exact spot of the stone was not found). Park on the streets of downtown Olathe.',
  [['Clio: Santa Fe Trail Marker, Olathe Courthouse Historical Plaza',CLIO%4]],
  brick='?',conf='mixed'),
N('memorial-six-million-jcc-overland-park-ks','Memorial to the Six Million','Overland Park, Kansas','ks','curio','standing',38.9205,-94.6519,'area','view','drive','','1963',
  'Dedicated June 9, 1963, with President Harry Truman speaking, this was one of the first memorials in the United States to recognise the Holocaust. Survivors in Kansas City began raising money for it in the late 1950s. It first stood on Holmes Road, and in 1988 it was moved to the grounds of the Jewish Community Center.',
  'A monument on the Jewish Community Center campus in Overland Park. The exact position on the grounds was not found; the pin is the campus.',
  'One of the first Holocaust memorials in the country, moved in 1988.',
  'On the grounds of the Jewish Community Center of Greater Kansas City, 5801 W. 115th Street. A private campus: whether the grounds are open to visitors, and when, was not read. Ask at the centre.',
  [['Clio: The Memorial to the Six Million',CLIO%14]],
  brick='?',conf='mixed'),
]
PIN_NOTES={
'krumm-building-lenexa-ks':'Started from an OpenStreetMap address lookup for 13420 Santa Fe Trail Drive, which fell on the parking lot; moved about 50 metres west onto the stone building seen on the aerial.',
'farmers-state-bank-ryckerts-lenexa-ks':'Corner of Santa Fe Trail Drive and Pflumm Road; the pin was placed from the Historical Society\'s description and the aerial, and the building itself could not be picked out with certainty.',
'haskin-home-lenexa-ks':'Coordinate from an address lookup for 9426 Pflumm Road.',
'santa-fe-trail-marker-olathe-courthouse-plaza-ks':'The pin is the courthouse address; the marker stands in the plaza nearby.',
'memorial-six-million-jcc-overland-park-ks':'The pin is on the Jewish Community Center campus; the memorial\'s exact spot was not found.',
}
