import PiousAcademic16807
import config
import os
import time
import json


def check_or_create_path(path):
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except OSError:
			if not os.path.isdir(path):
				raise


def dump_json_to_path(json_data, path):
	with open(path, 'w+') as fp:
		json.dump(json_data, fp)
	time.sleep(1)


def main():
	check_or_create_path(config.STATS_DATA_PATH)

	stats = PiousAcademic16807.Stats()

	# Get list of recent matches
	matches = stats.get_matches_for_player(config.MY_GAMERTAG, modes='arena', count=1)
	dump_json_to_path(matches, os.path.join(config.STATS_DATA_PATH, 'matches.json'))
	print '=> Stored matches at path: %s' % os.path.join(config.STATS_DATA_PATH, 'matches.json')

	# this is a motherfucker of a json mess
	events = stats.events_for_match_by_id(matches['Results'][0]['Id']['MatchId'])
	dump_json_to_path(events, os.path.join(config.STATS_DATA_PATH, 'events.json'))
	print '=> Stored events for match id: %s at path: %s' % (matches['Results'][0]['Id']['MatchId'], os.path.join(config.STATS_DATA_PATH, 'events.json'))

	# faking itttttt
	leaderboards = stats.get_leaderboard('2041d318-dd22-47c2-a487-2818ecf14e41', '7b7e892c-d9b7-4b03-bef8-c6a071df28ef')
	dump_json_to_path(leaderboards, os.path.join(config.STATS_DATA_PATH, 'leaderboards.json'))
	print '=> Stored leaderboards at path: %s' % os.path.join(config.STATS_DATA_PATH, 'leaderboards.json')


# Finish this sometime.
if __name__ == '__main__':
	main()
