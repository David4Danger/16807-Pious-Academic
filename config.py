import os

# Put your API key you got from the developer page in the space of 'YOUR KEY HERE'
MY_KEY = 'YOUR_API_KEY_HERE'

# Can be used for emblem, profile, matches, service records, etc
MY_GAMERTAG = 'e'
ALL_GAMERTAGS = 'GAMERTAG1,GAMERTAG2,GAMETAG3,GAMERTAG4'

# This is used in the get scripts, if you're
DATA_PATH = os.path.expanduser('~/16807-Pious-Academic/')
METADATA_DATA_PATH = os.path.join(DATA_PATH, 'Metadata')
PROFILE_DATA_PATH = os.path.join(DATA_PATH, 'Profile')
STATS_DATA_PATH = os.path.join(DATA_PATH, 'Stats')
