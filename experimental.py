#Completely the work of /u/xelf on Reddit. All credit to him for this beauty!

from random import randint

origins = [ "ABINGTON", "ACTON", "ACUSHNET", "ADAMS", "AGAWAM", "ALFORD", "AMESBURY", "AMHERST", "ANDOVER", "AQUINNAH", "ARLINGTON", "ASHBURNHAM", "ASHBY", "ASHFIELD", "ASHLAND", "ATHOL", "ATTLEBORO", "AUBURN", "AVON", "AYER", "BARNSTABLE", "BARRE", "BECKET", "BEDFORD", "BELCHERTOWN", "BELLINGHAM", "BELMONT", "BERKLEY", "BERLIN", "BERNARDSTON", "BEVERLY", "BILLERICA", "BLACKSTONE", "BLANDFORD", "BOLTON", "BOSTON", "BOURNE", "BOXBOROUGH", "BOXFORD", "BOYLSTON", "BRAINTREE", "BREWSTER", "BRIDGEWATER", "BRIMFIELD", "BROCKTON", "BROOKFIELD", "BROOKLINE", "BUCKLAND", "BURLINGTON", "CAMBRIDGE", "CANTON", "CARLISLE", "CARVER", "CHARLEMONT", "CHARLTON", "CHATHAM", "CHELMSFORD", "CHELSEA", "CHESHIRE", "CHESTER", "CHESTERFIELD", "CHICOPEE", "CHILMARK", "CLARKSBURG", "CLINTON", "COHASSET", "COLRAIN", "CONCORD", "CONWAY", "CUMMINGTON", "DALTON", "DANVERS", "DARTMOUTH", "DEDHAM", "DEERFIELD", "DENNIS", "DIGHTON", "DOUGLAS", "DOVER", "DRACUT", "DUDLEY", "DUNSTABLE", "DUXBURY", "EAST BRIDGEWATER", "EAST BROOKFIELD", "EAST LONGMEADOW", "EASTHAM", "EASTHAMPTON", "EASTON", "EDGARTOWN", "EGREMONT", "ERVING", "ESSEX", "EVERETT", "FAIRHAVEN", "FALL RIVER", "FALMOUTH", "FITCHBURG", "FLORIDA", "FOXBOROUGH", "FRAMINGHAM", "FRANKLIN", "FREETOWN", "GARDNER", "GEORGETOWN", "GILL", "GLOUCESTER", "GOSHEN", "GRAFTON", "GRANBY", "GRANVILLE", "GREAT BARRINGTON", "GREENFIELD", "GROTON", "GROVELAND", "HADLEY", "HALIFAX", "HAMILTON", "HAMPDEN", "HANCOCK", "HANOVER", "HANSON", "HARDWICK", "HARVARD", "HARWICH", "HATFIELD", "HAVERHILL", "HAWLEY", "HEATH", "HINGHAM", "HINSDALE", "HOLBROOK", "HOLDEN", "HOLLAND", "HOLLISTON", "HOLYOKE", "HOPEDALE", "HOPKINTON", "HUBBARDSTON", "HUDSON", "HULL", "HUNTINGTON", "IPSWICH", "KINGSTON", "LAKEVILLE", "LANCASTER", "LANESBOROUGH", "LAWRENCE", "LEE", "LEICESTER", "LENOX", "LEOMINSTER", "LEVERETT", "LEXINGTON", "LEYDEN", "LINCOLN", "LITTLETON", "LONGMEADOW", "LOWELL", "LUDLOW", "LUNENBURG", "LYNN", "LYNNFIELD", "MALDEN", "MANCHESTER-BY-THE-SEA", "MANSFIELD", "MARBLEHEAD", "MARION", "MARLBOROUGH", "MARSHFIELD", "MASHPEE", "MATTAPOISETT", "MAYNARD", "MEDFIELD", "MEDFORD", "MEDWAY", "MELROSE", "MENDON", "MERRIMAC", "METHUEN", "MIDDLEBOROUGH", "MIDDLEFIELD", "MIDDLETON", "MILFORD", "MILLBURY", "MILLIS", "MILLVILLE", "MILTON", "MONROE", "MONSON", "MONTAGUE", "MONTEREY", "MONTGOMERY", "MOUNT WASHINGTON", "NAHANT", "NANTUCKET", "NATICK", "NEEDHAM", "NEW ASHFORD", "NEW BEDFORD", "NEW BRAINTREE", "NEW MARLBOROUGH", "NEW SALEM", "NEWBURY", "NEWBURYPORT", "NEWTON", "NORFOLK", "NORTH ADAMS", "NORTH ANDOVER", "NORTH ATTLEBOROUGH", "NORTH BROOKFIELD", "NORTH READING", "NORTHAMPTON", "NORTHBOROUGH", "NORTHBRIDGE", "NORTHFIELD", "NORTON", "NORWELL", "NORWOOD", "OAK BLUFFS", "OAKHAM", "ORANGE", "ORLEANS", "OTIS", "OXFORD", "PALMER", "PAXTON", "PEABODY", "PELHAM", "PEMBROKE", "PEPPERELL", "PERU", "PETERSHAM", "PHILLIPSTON", "PITTSFIELD", "PLAINFIELD", "PLAINVILLE", "PLYMOUTH", "PLYMPTON", "PRINCETON", "PROVINCETOWN", "QUINCY", "RANDOLPH", "RAYNHAM", "READING", "REHOBOTH", "REVERE", "RICHMOND", "ROCHESTER", "ROCKLAND", "ROCKPORT", "ROWE", "ROWLEY", "ROYALSTON", "RUSSELL", "RUTLAND", "SALEM", "SALISBURY", "SANDISFIELD", "SANDWICH", "SAUGUS", "SAVOY", "SCITUATE", "SEEKONK", "SHARON", "SHEFFIELD", "SHELBURNE", "SHERBORN", "SHIRLEY", "SHREWSBURY", "SHUTESBURY", "SOMERSET", "SOMERVILLE", "SOUTH HADLEY", "SOUTHAMPTON", "SOUTHBOROUGH", "SOUTHBRIDGE", "SOUTHWICK", "SPENCER", "SPRINGFIELD", "STERLING", "STOCKBRIDGE", "STONEHAM", "STOUGHTON", "STOW", "STURBRIDGE", "SUDBURY", "SUNDERLAND", "SUTTON", "SWAMPSCOTT", "SWANSEA", "TAUNTON", "TEMPLETON", "TEWKSBURY", "TISBURY", "TOLLAND", "TOPSFIELD", "TOWNSEND", "TRURO", "TYNGSBOROUGH", "TYRINGHAM", "UPTON", "UXBRIDGE", "WAKEFIELD", "WALES", "WALPOLE", "WALTHAM", "WARE", "WAREHAM", "WARREN", "WARWICK", "WASHINGTON", "WATERTOWN", "WAYLAND", "WEBSTER", "WELLESLEY", "WELLFLEET", "WENDELL", "WENHAM", "WEST BOYLSTON", "WEST BRIDGEWATER", "WEST BROOKFIELD", "WEST NEWBURY", "WEST SPRINGFIELD", "WEST STOCKBRIDGE", "WEST TISBURY", "WESTBOROUGH", "WESTFIELD", "WESTFORD", "WESTHAMPTON", "WESTMINSTER", "WESTON", "WESTPORT", "WESTWOOD", "WEYMOUTH", "WHATELY", "WHITMAN", "WILBRAHAM", "WILLIAMSBURG", "WILLIAMSTOWN", "WILMINGTON", "WINCHENDON", "WINCHESTER", "WINDSOR", "WINTHROP", "WOBURN", "WORCESTER", "WORTHINGTON", "WRENTHAM", "YARMOUTH" ]


#def load_distances(origins):
#    distances = { o : { c : randint(10,500) if c!= o else 0 for c in origins  } for o in origins }

def load_distances(origins):
    distances = {}
    for o in origins:
        d = list(map(float,open(f'maDistsLists/{o}.txt').readlines()))
        distances[o] = { origins[i] : d[i] for i in range(350) if origins[i] != o }
    return distances

distances = load_distances(origins)
orders    = { o : sorted(distances[o], key=lambda x: distances[o][x]) for o in origins }

#start     = max(distances, key = lambda x: max(distances[x].values()))
start    = "BRAINTREE"
current   = start
seen      = {'', start}
results   = []
total     = 0

N = 12

while len(orders) - len(results) > N:
    furthest = orders[current]
    found = ''
    while found in seen:
        if len(furthest)==0:
            found = start
            break
        found = furthest.pop()
    seen.add(found)
    total += distances[current][found]
    results.append((current,found,distances[current][found]))
    current = found

usedup = { o[0] for o in results } | { found }
remaining = [ o for o in origins if o not in usedup ]

from itertools import permutations

combs = {}
for perm in permutations(remaining, r=N-1):
    perms = [found] + list(perm) + [start]
    dists = [distances[perms[i]][perms[i+1]] for i in range(N)]
    combs[sum(dists)] = (perms, dists)
large = max(combs)

print(total + large)
print(' '.join(c[0] for c in results), ' '.join(c for c in combs[large][0]))
