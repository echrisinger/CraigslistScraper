
from craigslistscraper import Searches

tacoma_cities = ['flagstaff',
 'mohave',
 'phoenix',
 'prescott',
 'showlow',
 'sierravista',
 'tucson',
 'yuma',
 'bakersfield',
 'chico',
 'fresno',
 'goldcountry',
 'hanford',
 'humboldt',
 'imperial',
 'inlandempire',
 'losangeles',
 'mendocino',
 'merced',
 'modesto',
 'monterey',
 'orangecounty',
 'palmsprings',
 'redding',
 'sacramento',
 'sandiego',
 'sfbay',
 'slo',
 'santabarbara',
 'santamaria',
 'siskiyou',
 'stockton',
 'susanville',
 'ventura',
 'visalia',
 'yubasutter',
 'boulder',
 'cosprings',
 'denver',
 'eastco',
 'fortcollins',
 'rockies',
 'pueblo',
 'westslope',
 'boise',
 'eastidaho',
 'lewiston',
 'twinfalls',
 'billings',
 'bozeman',
 'butte',
 'greatfalls',
 'helena',
 'kalispell',
 'missoula',
 'montana',
 'bend',
 'corvallis',
 'eastoregon',
 'eugene',
 'klamath',
 'medford',
 'oregoncoast',
 'portland',
 'roseburg',
 'salem',
 'bellingham',
 'kpr',
 'moseslake',
 'olympic',
 'pullman',
 'seattle',
 'skagit',
 'spokane',
 'wenatchee',
 'yakima',
 'cariboo',
 'comoxvalley',
 'abbotsford',
 'kamloops',
 'kelowna',
 'kootenays',
 'nanaimo',
 'princegeorge',
 'skeena',
 'sunshine',
 'vancouver',
 'victoria',
 'whistler']

cities = [
    'roseburg',
    'meridian',
    'jonesboro',
    'bakersfield',
    'roswell',
    'odessa',
    'wichitafalls',
    'pensacola',
    'elpaso',
    'enid',
    'medford',
    'lewiston',
    'asheville',
    'treasure',
    'clovis',
    'statesboro',
    'chattanooga',
    'augusta',
    'richmond',
    'lakecharles',
    'victoriatx',
    'lafayette',
    'montgomery',
    'klamath',
    'skagit',
    'raleigh',
    'eastnc',
    'sanangelo',
    'greensboro',
    'austin',
    'wv',
    'lakeland',
    'gulfport',
    'bgky',
    'charleston',
    'brunswick',
    'sanantonio',
    'lexington',
    'hiltonhead',
    'goldcountry',
    'blacksburg',
    'swva',
    'olympic',
    'pullman',
    'imperial',
    'boise',
    'bend',
    'panamacity',
    'jacksontn',
    'salem',
    'mobile',
    'farmington',
    'jacksonville',
    'texoma',
    'fayar',
    'tallahassee',
    'spacecoast',
    'mohave',
    'monterey',
    'eastky',
    'beaumont',
    'sarasota',
    'brownsville',
    'lawton',
    'texarkana',
    'harrisonburg',
    'killeen',
    'columbia',
    'outerbanks',
    'owensboro',
    'clarksville',
    'sandiego',
    'winchester',
    'easttexas',
    'atlanta',
    'santafe',
    'siskiyou',
    'norfolk',
    'dallas',
    'albuquerque',
    'okaloosa',
    'littlerock',
    'fortsmith',
    'ocala',
    'susanville',
    'helena',
    'batonrouge',
    'tricities',
    'lascruces',
    'bigbend',
    'charlotte',
    'nashville',
    'wenatchee',
    'inlandempire',
    'morgantown',
    'gainesville',
    'columbusga',
    'humboldt',
    'winstonsalem',
    'tucson',
    'elko',
    'roanoke',
    'gadsden',
    'fresno',
    'neworleans',
    'showlow',
    'sanmarcos',
    'waco',
    'seattle',
    'knoxville',
    'reno',
    'abilene',
    'tulsa',
    'houston',
    'fredericksburg',
    'fortmyers',
    'eastoregon',
    'slo',
    'myrtlebeach',
    'albanyga',
    'washingtondc',
    'modesto',
    'monroe',
    'jackson',
    'missoula',
    'hattiesburg',
    'chico',
    'yuma',
    'phoenix',
    'boone',
    'billings',
    'bozeman',
    'fayetteville',
    'greenville',
    'santamaria',
    'eastidaho',
    'flagstaff',
    'corpuschristi',
    'charlottesville',
    'macon',
    'bellingham',
    'oregoncoast',
    'sfbay',
    'northmiss',
    'lynchburg',
    'cookeville',
    'martinsburg',
    'miami',
    'tampa',
    'twinfalls',
    'greatfalls',
    'spokane',
    'louisville',
    'parkersburg',
    'collegestation',
    'merced',
    'charlestonwv',
    'valdosta',
    'mcallen',
    'kpr',
    'auburn',
    'butte',
    'swv',
    'eugene',
    'orangecounty',
    'amarillo',
    'tuscaloosa',
    'montana',
    'staugustine',
    'dothan',
    'sacramento',
    'redding',
    'onslow',
    'cenla',
    'ventura',
    'corvallis',
    'nacogdoches',
    'delrio',
    'savannah',
    'huntington',
    'daytona',
    'memphis',
    'danville',
    'natchez',
    'florencesc',
    'keys',
    'athensga',
    'lubbock',
    'wheeling',
    'shreveport',
    'galveston',
    'hickory',
    'yubasutter',
    'lakecity',
    'oklahomacity',
    'sierravista',
    'bham',
    'yakima',
    'westky',
    'houma',
    'palmsprings',
    'orlando',
    'cfl',
    'portland',
    'stockton',
    'nwga',
    'shoals',
    'lasvegas',
    'moseslake',
    'laredo',
    'wilmington',
    'huntsville',
    'mendocino',
    'losangeles',
    'stillwater',
    'visalia',
    'kalispell',
    'santabarbara',
    'prescott'
]

base_filters = [
    '&postedToday=1',
    '&hasPic=1',
    '&min_price=3000',
    '&max_price=18000',
    '&condition=20',
    '&condition=30',
    '&condition=40',
    '&auto_title_status=1',
    '&min_auto_miles=20000',
    '&max_auto_miles=150000'
]
truck_filters = base_filters + ['&auto_drivetrain=3']
gas_filters = base_filters + ['&auto_fuel_type=1']
diesel_filters = base_filters + ['&auto_fuel_type=2']
diesel_truck_filters = truck_filters + ['&auto_fuel_type=2']

cars = {
    # "Toyota+Tacoma": truck_filters,
    # "Toyota+Tundra": truck_filters,
    # "Toyota+Hilux": truck_filters,
    "Ford+Ranger": truck_filters,
    "Mazda+B4000": truck_filters,
    "Nissan+Frontier": truck_filters,
    "GMC+Canyon": truck_filters,
    "Colorado+ZR2": diesel_truck_filters,
    "Chevy Avalanche": truck_filters,
    "Chevrolet Avalanche": truck_filters,
}

vans = {
    "Ram+Promaster": gas_filters,
    "Ford+Transit": base_filters,
    "Mercedes+Sprinter": diesel_filters,
    "Dodge+Sprinter": diesel_filters,
    "Freightliner+Sprinter": diesel_filters
}

if __name__ == '__main__':
    for search, filters in cars.items():
        foo = Searches(search, tacoma_cities, "cto", filters, car_data=True)
        foo.compile_search()
