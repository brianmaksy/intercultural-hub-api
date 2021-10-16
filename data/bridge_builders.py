import random
from .hubs import hubs

_NUMBER_BRIDGE_BUILDS = 200

_FIRST_NAMES = [
    "Arturo",
    "Esteban",
    "River",
    "Yahir",
    "Santos",
    "Casey",
    "Boston",
    "Jermaine",
    "Spencer",
    "Zayden",
    "Cayden",
    "Tyler",
    "Layne",
    "Hassan",
    "Wyatt",
    "Augustus",
    "Lincoln",
    "Cameron",
    "Drew",
    "Alden",
    "Yuliana",
    "Kamari",
    "Janiah",
    "Nadia",
    "Makena",
    "Priscilla",
    "Katelyn",
    "Kennedy",
    "Ashlynn",
    "Kayley",
    "Kenzie",
    "Chasity",
]

_LAST_NAMES = [
    "Gutierrez",
    "Douglas",
    "Chung",
    "Burke",
    "Bonilla",
    "Best",
    "Todd",
    "Clayton",
    "Conway",
    "Stevens",
    "Hinton",
    "Rose",
    "Goodwin",
    "Aguirre",
    "Contreras",
    "Paul",
    "Mcintosh",
    "Cervantes",
    "Woodard",
    "Oneal",
    "Salazar",
    "Silva",
    "Hebert",
    "Perry",
    "Cordova",
    "Jacobs",
    "English",
    "Livingston",
    "Oconnor",
    "Whitney",
]

_CULTURES = [
    "Eritrean",
    "Dominican",
    "Colombian",
    "Australian",
    "Kazakh",
    "Moroccan",
    "Burundian",
    "Nigerien",
    "Malawian",
    "Afghan",
    "Mauritian",
    "Liechtensteiner",
    "Surinamese",
    "Jamaican",
    "Nepalese",
    "Moldovan",
    "Nicaraguan",
    "Kenyan",
    "Venezuelan",
    "Austrian",
    "Tadzhik",
    "Monacan",
    "Bhutanese",
    "Filipino",
    "Swazi",
    "Zimbabwean",
    "Latvian",
    "Egyptian",
    "Algerian",
    "Brazilian",
    "Armenian",
    "Spaniard",
    "Bulgarian",
    "Gambian",
    "Burmese",
    "Gabonese",
    "Yugoslav",
    "Finn",
    "Montenegrin",
    "Australian",
    "Icelander",
    "Panamanian",
    "Georgian",
    "Norwegian",
    "Israeli",
    "Guyanese",
    "Macedonian",
    "Ecuadorean",
    "Slovak",
    "Slovenian",
]

_MINISTRY_AREAS = [
    "Evangelism",
    "Children",
    "Music",
    "Exegesis",
    "Women",
    "Students",
    "Preaching",
    "Elderly",
    "Youth",
    "Social action",
    "Food banks",
    "Funerals",
]

_TRAINING = [
    "Workshops",
    "Video calls",
    "Talks",
    "Language tuition",
    "Music",
    "Church planting",
]

_CHURCH_PREFIX = [
    "Christ Church",
    "Christ the Redeemer",
    "St James'",
    "St Peter's",
    "St Mark's",
    "St Thomas'",
    "Holy Trininty",
    "Calvary Church",
    "Community Church",
    "City Church",
    "Central Church",
]

_CHURCH_SUFFIX = [
    "London",
    "Brandford",
    "Paris",
    "Edinburgh",
    "Glasgow",
    "Dublin",
    "Manchester",
    "Geneva",
    "Lyon",
    "Frankfurt",
    "Kigali",
    "Cairo",
    "Istanbul",
]

_MIN_LATITUDE = 51.41845
_MAX_LATITUDE = 51.654543
_MIN_LONGITUDE = -0.418912
_MAX_LONGITUDE = 0.070899


def random_latitude():
    return (random.random() * (_MAX_LATITUDE - _MIN_LATITUDE)) + _MIN_LATITUDE


def random_longitude():
    return (random.random() * (_MAX_LONGITUDE - _MIN_LONGITUDE)) + _MIN_LONGITUDE


bridge_builders = [
    {
        "id": str(i),
        "name": f"{random.choice(_FIRST_NAMES)} {random.choice(_LAST_NAMES)}",
        "cultures": random.sample(_CULTURES, random.randrange(3) + 1),
        "ministry_areas": random.sample(_MINISTRY_AREAS, random.randrange(2) + 1),
        "hub": random.choice(hubs)["name"] if random.random() < 0.7 else None,
        "phone_number": f"+{random.randrange(99) + 1} {str(random.randrange(10000000000)).zfill(10)}",
        "training": random.sample(_TRAINING, random.randrange(4) + 1),
        "church": f"{random.choice(_CHURCH_PREFIX)}, {random.choice(_CHURCH_SUFFIX)}",
        "latitude": random_latitude(),
        "longitude": random_longitude(),
    }
    for i in range(0, _NUMBER_BRIDGE_BUILDS)
]
