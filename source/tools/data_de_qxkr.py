# November 28, 2026: Delaware, fourth pass, spread over Kent, Sussex and New Castle counties. Ground taken with
# tools/choose.py --thinnest. Facts from the linked sources only, read in this session: the Park Service's Register
# records and nomination forms, Wikipedia articles read as raw text, and the Delaware Public Archives' marker and
# historic-houses-of-worship pages. Hours and access were not found on the pages of whoever runs most of these places.
from data_b import N
from data_ma import W

NPS='https://npgallery.nps.gov/AssetDetail/NRIS/'
DPA='https://archives.delaware.gov/'

BATCH={'key':'de_qxkr','label':'Delaware: churches, stations and old houses, Kent, Sussex and New Castle','added':'2026-11-28 08:31'}

PLACES=[
N('thomas-chapel-chapeltown','Thomas Chapel (Thomas\' Methodist Episcopal Chapel)','Marydel','de','worship','standing',39.09861,-75.70417,'area','view','drive','cemeteries','1825 (log church 1761)',
  'One of the earliest Methodist churches in America, by the state\'s marker. A log church put up in 1761 as an Episcopal chapel passed, by tradition, to the Methodists in the late 1770s and was renamed for William Thomas, a local Methodist leader. A frame building replaced the log one, and the first brick church went up in 1825. Wikipedia says the site is where the freedman Harry Hosier preached in 1784, called the first sermon by a Black man directly to a white congregation; the state marker page read for this entry does not mention it. The marker page and Wikipedia also differ on early dates, so the 1761 start is the marker\'s account.',
  'A small one-storey, three-bay brick chapel in the Greek Revival style, remodelled in the late 1870s, with an old burying ground beside it and two small outbuildings of about 1900 (a privy and a shed that served as a refreshment stand). Interior not checked.',
  'A Methodist chapel whose first walls were logs, in a country burying ground.',
  'Marker address: 2810 Westville Road, Marydel. Ownership today and whether it opens were not found; look from the road and the burying ground edge, and do not go in unless it is open. Parking not checked.',
  [[ 'National Register record: Thomas\' Methodist Episcopal Chapel',NPS+'93001516'],['Delaware Public Archives: Thomas Chapel marker',DPA+'delaware-historical-markers/thomas-chapel-chapeltown/'],W('Thomas\' Methodist Episcopal Chapel')],
  conf='mixed',brick='?'),

N('barratt-hall-frederica','Barratt Hall (Philip Barratt House)','Frederica','de','landmark','standing',39.02472,-75.44,'site','view','drive','','mid-1700s',
  'A mid-1700s Georgian brick house of two storeys and three bays, laid in Flemish bond with glazed headers. In 1784 Bishops Thomas Coke and Francis Asbury met here with Miriam Barratt and eleven preachers; their council led to the Christmas Conference in Baltimore at which the Methodist Church in America was organized. Philip Barratt gave the land for Barratt\'s Chapel (1780) and helped build it.',
  'The north front in glazed-header Flemish bond with segmental-arched openings, a box cornice and a three-brick belt course of glazed headers; the west gable mixes Flemish and English bond. Interior not checked.',
  'Where the Christmas Conference was planned.',
  'Not known to be open; treat it as a private house and look from the public road. Owner and parking not checked.',
  [['National Register record: Barratt Hall',NPS+'73000492'],W('Barratt Hall')],
  brick='?'),

N('felton-railroad-station','Felton Railroad Station','Felton','de','rail','standing',39.01083,-75.57583,'area','view','drive','stations','1868',
  'The Delaware Railroad built this station in 1868, a one-storey, five-bay brick Italianate building with a low hipped roof, shallow eaves, round-headed doors and windows and a projecting bow window. It has been renovated for use as a museum.',
  'The station\'s round-headed openings and bow window on the trackside front. Interior not checked.',
  'An 1868 Italianate depot on the old Delaware Railroad main line.',
  'The address is given as 215 East Railroad Avenue by Wikipedia and the Park Service and as 210 East Railroad Avenue by the Delaware Public Archives. A 2024 railfan page said the local historical society was working to restore regular public hours; none were found, so check with the Town of Felton before a trip.',
  [['National Register record: Felton Railroad Station',NPS+'81000191'],W('Felton station')],
  conf='mixed',brick='?'),

N('wyoming-railroad-station','Wyoming Railroad Station','Wyoming','de','rail','standing',39.11873,-75.55835,'area','view','drive','stations','1872',
  'The Delaware Railroad built this station in 1872, a one-storey, five-bay brick Italianate building with a low hipped roof, shallow eaves, round-headed doors and windows and a projecting bow window, like the one at Felton. It now serves as town offices and is part of the Wyoming Historic District.',
  'The matching round-headed openings and bow window. Interior not checked.',
  'A sister of the Felton depot, now the town hall.',
  'Used as town offices, so open in town business hours at most; hours were not found. Parking not checked.',
  [['National Register record: Wyoming Railroad Station',NPS+'80000931'],W('Wyoming station (Delaware)')],
  brick='?'),

N('todds-chapel-greenwood','Todd\'s Chapel','Greenwood','de','worship','standing',38.83535,-75.67314,'area','view','drive','cemeteries','1858',
  'A Methodist chapel built in 1858: a one-storey rectangular frame building in a plain Greek Revival style, 32 ft 9 in by 44 ft 9 in, with a gable roof and stained-glass windows. A one-storey school wing was added in 1966. Cemeteries lie east and north, the earliest marker dated 1861.',
  'The 1858 frame meeting-house form with its gable front, and the graveyards beside it. Interior not checked.',
  'A little Greek Revival chapel with graves from 1861.',
  'A United Methodist congregation\'s property; service times were not found. Look from the road and the graveyard edge. Parking not checked.',
  [['National Register record: Todd\'s Chapel',NPS+'98001094'],W('Todd\'s Chapel')],
  brick='no'),

N('griffiths-chapel-williamsville','Griffith\'s Chapel (Williamsville Methodist Church)','Williamsville','de','worship','standing',38.89588,-75.50806,'site','view','drive','cemeteries','1850',
  'A neat, plain, one-storey frame chapel of 1850, 24 by 30 feet, clapboarded, with a small rectangular apse at the east end and a gallery inside lit by two windows in the front gable. When the Register form was written in 1983 it called the exterior and especially the interior very well preserved; the original white paint with green trim had weathered away and a restoration was under way. A graveyard with stones from the mid-1800s lies north and east.',
  'The plain gabled front with its pair of narrow gallery windows, the apse behind, and the old stones. Interior as described in 1983: excellent integrity; not checked since.',
  'An 1850 country chapel kept almost as built.',
  'The form lists the Peninsula General Conference of the United Methodist Church as owner in 1983; present ownership and any opening were not found. Look from the road. Parking not checked.',
  [['National Register record: Griffith\'s Chapel',NPS+'83001370'],W('Griffith\'s Chapel')],
  brick='no'),

N('loockerman-hall-dover','Loockerman Hall','Dover','de','inst','standing',39.185,-75.54556,'area','view','drive','','before 1730',
  'A large two-storey Georgian brick plantation house, 40 by 50 feet, dating to before 1730. It was the first building on the campus of Delaware State College, set up by the General Assembly on 15 May 1891 as the State College for Colored Students, now Delaware State University.',
  'The brick plantation house among the campus buildings. Interior not checked.',
  'The first building of a college founded for Black students in 1891.',
  'On the campus of Delaware State University, Dover; visitor access to the building and parking rules were not found. Look from the campus paths.',
  [['National Register record: Loockerman Hall',NPS+'71000218'],W('Loockerman Hall')],
  brick='?'),

N('great-geneva-camden','Great Geneva','Camden','de','landmark','standing',39.1175,-75.50889,'site','ask','drive','','about 1765',
  'A two-and-a-half-storey brick house of about 1765 on a hall-and-parlor plan, with a small frame kitchen wing, adapted from the Resurrection Manor plan. It is linked with the Hunn family and the local Quaker community and was a station on the Underground Railroad. The north front is in Flemish bond with keyed lintels and a transom over the door.',
  'The Flemish-bond north front and the older rear wall in English bond. Few original interior features survive, according to the Wikipedia account of the Register form; later owners added mouldings and a kitchen.',
  'A Quaker-linked brick farmhouse on the Underground Railroad.',
  'A private house as far as the sources say; ask the owner and do not enter the grounds. Owner and parking not checked.',
  [['National Register record: Great Geneva',NPS+'73000489'],W('Great Geneva')],
  brick='?'),

N('warrens-mill-millsboro','Warren\'s Mill','Millsboro','de','industry','standing',38.59591,-75.30376,'site','view','drive','','1910–1918',
  'A grist mill built between 1910 and 1918: a large two-storey rectangular frame building, clapboarded, with a gambrel roof, on a poured concrete foundation with a concrete spillway. A shed beside it counts as part of the listing. Wikipedia places it among unused buildings in Delaware.',
  'The gambrel-roofed frame mill and the concrete spillway at the pond. Interior and present condition not checked.',
  'A gambrel-roofed grist mill with a concrete spillway.',
  'Ownership not found; look from the public road only. Parking not checked.',
  [['National Register record: Warren\'s Mill',NPS+'78000923'],W('Warren\'s Mill')],
  brick='no'),

N('old-drawyers-church-odessa','Old Drawyers Church','Odessa','de','worship','standing',39.46767,-75.65422,'site','open','drive','cemeteries','1773',
  'A Presbyterian congregation met here from 1700 and was organized in 1708; the land came from John Peterson in 1711 and the first log church was known as the Church of Apoquinimy. The present Georgian brick church, two storeys and five bays with an elaborate doorway, was completed in 1773. Regular services ended in 1858 when the congregation built a new church in Odessa. Thomas McKean, a signer of the Declaration of Independence, was an early member; the oldest tombstone named in the source is dated 1762.',
  'Family box pews painted white with mahogany trim, a gallery on three sides, a high pulpit under a domed sounding board topped by a gold eagle, and curved double pulpit stairs round the precentor\'s desk, as described in a 1947 book (the Public Archives page quotes it). A large enclosed graveyard surrounds it.',
  'An 1773 church with its box pews and eagle-topped sounding board.',
  'On US 13 about a mile north of Odessa. The Friends of Old Drawyer\'s hold an annual service on the first Sunday in June (the Public Archives page and a 2011 newspaper piece); no other opening times were found.',
  [['National Register record: Old Drawyers Church',NPS+'73000533'],['Delaware Public Archives: Old Drawyer\'s Presbyterian Church',DPA+'historic-houses-of-worship/old-drawyers-presbyterian-church/'],W('Old Drawyers Church')],
  hours='First Sunday in June (annual service); other times not found',brick='?'),

N('old-fort-church-christiana','Old Fort Church','Christiana','de','worship','standing',39.66786,-75.65929,'site','view','drive','','1850; moved 1897',
  'An African-American Methodist church built in 1850 on Schoolbell Road in Christiana Hundred, taken down in 1897 and rebuilt on Old Baltimore Pike. It is a one-storey, three-bay brick building under a gable roof, with modified lancet windows and decorative wood shingles painted dark green in the gable ends.',
  'The lancet-type windows and the shingled gables on Old Baltimore Pike. Interior not checked.',
  'A church taken down and rebuilt on a new site in 1897.',
  'A church on Old Baltimore Pike; ownership, services and parking were not found. Look from the road.',
  [['National Register record: Old Fort Church',NPS+'83001402'],W('Old Fort Church')],
  brick='?'),

N('st-james-church-stanton','St. James Episcopal Church, Mill Creek','Stanton','de','worship','standing',39.7186,-75.66064,'site','open','drive','cemeteries','1714–1820s',
  'A log church stood near here about 1703. James Robinson bought 110 acres in 1714 and gave 10 for a church, finished two years later, whose first minister was George Ross, father-in-law of the flagmaker Betsy Ross. The wood church burned in 1820 and was rebuilt in stone over the next three years. An active Episcopal parish at 2106 St. James Church Road.',
  'The stone church of the 1820s and its churchyard. Interior not checked.',
  'A parish founded about 1703 with a stone church of the 1820s.',
  'An active parish; its own page was not read, so service times are not given. Parking not checked.',
  [['National Register record: St. James Church, Stanton',NPS+'73000543'],W('St. James Episcopal Church, Mill Creek')],
  hours='?',brick='?',conf='mixed'),
]

PIN_NOTES={
 'thomas-chapel-chapeltown':'Taken from a published point near the building; on the aerial the building itself could not be picked out with certainty, so the pin marks the neighbourhood.',
 'barratt-hall-frederica':'From the Wikipedia article; to be checked on the aerial.',
 'felton-railroad-station':'Taken from a published point near the building; on the aerial the building itself could not be picked out with certainty, so the pin marks the neighbourhood.',
 'wyoming-railroad-station':'Taken from a published point near the building; on the aerial the building itself could not be picked out with certainty, so the pin marks the neighbourhood.',
 'todds-chapel-greenwood':'Taken from a published point near the building; on the aerial the building itself could not be picked out with certainty, so the pin marks the neighbourhood.',
 'griffiths-chapel-williamsville':'From the Park Service record area; to be checked on the aerial.',
 'loockerman-hall-dover':'Taken from a published point near the building; on the aerial the building itself could not be picked out with certainty, so the pin marks the neighbourhood.',
 'great-geneva-camden':'From the Wikipedia article; to be checked on the aerial.',
 'warrens-mill-millsboro':'From the Wikipedia article; to be checked on the aerial.',
 'old-drawyers-church-odessa':'From the Wikipedia article; to be checked on the aerial.',
 'old-fort-church-christiana':'From the Wikipedia article; to be checked on the aerial.',
 'st-james-church-stanton':'From the Wikipedia article; to be checked on the aerial.',
}
