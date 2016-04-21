import config
import os
import shutil
import time

import PiousAcademic16807


def check_or_create_path(path):
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except OSError:
			if not os.path.isdir(path):
				raise


def save_image_to_path_from_response(response, path):
	with open(path, 'wb') as f:
		shutil.copyfileobj(response, f)
	time.sleep(1)  # stops requesting things too quickly
	print '=> Saved image to path: %s' % path


def main():
	check_or_create_path(os.path.join(config.PROFILE_DATA_PATH))

	api = PiousAcademic16807.Profile()

	emblem_image = api.get_emblem_image_for_player(config.MY_GAMERTAG)
	save_image_to_path_from_response(emblem_image, os.path.join(config.PROFILE_DATA_PATH, 'emblem.png'))
	time.sleep(1)

	profile_image = api.get_profile_image_for_player(config.MY_GAMERTAG)
	save_image_to_path_from_response(profile_image, os.path.join(config.PROFILE_DATA_PATH, 'profile.png'))
	time.sleep(1)

if __name__ == '__main__':
	main()
