from collections import deque
import time
import requests
import config


# This class raises exceptions caused by a non-200 response code from a request made
class i343Exception(Exception):
	def __init__(self, error, response):
		self.error = error
		self.headers = response.headers

	def __str__(self):
		return self.error


error_302 = 'Golden Path. The Location header should point at the corresponding emblem image.'
error_400 = 'An unsupported value was provided for a query string parameter.'
error_401 = 'Access denied.'
error_404 = 'Specified Title was not "h5"/Specified player gamertag was not found.'
error_500 = 'Internal Server Error'


def raise_status(response):
	if response.status_code == 302:
		raise i343Exception(error_302, response)
	elif response.status_code == 400:
		raise i343Exception(error_400, response)
	elif response.status_code == 401:
		raise i343Exception(error_401, response)
	elif response.status_code == 404:
		raise i343Exception(error_404, response)
	elif response.status_code == 500:
		raise i343Exception(error_500, response)
	else:
		response.raise_for_status()


# This class makes sure you are operating within your rate limit constraints. Technically it is not
# necessary, but without it you could hit the cap on 343's end accidentally and run the risk of your
# api key being suspended.
class RateLimit:
	def __init__(self, allowed_requests, seconds):
		self.allowed_requests = allowed_requests
		self.seconds = seconds
		self.made_requests = deque()

	def __reload(self):
		t = time.time()
		while len(self.made_requests) > 0 and self.made_requests[0] < t:
			self.made_requests.popleft()

	def add_request(self):
		self.made_requests.append(time.time() + self.seconds)

	def request_available(self):
		self.__reload()
		return len(self.made_requests) < self.allowed_requests

	# The 3 different types of request and all their respective function calls are defined


# under this class. Any function arguments initialized as 'None' are disable unless an
# argument is given, meaning they are optional arguments to pass or not. Refer to the
# official documentation for further details.
class PiousAcademic(object):
	def __init__(self, title="h5", limits=(RateLimit(10, 10), RateLimit(600, 600))):
		self.title = title
		self.limits = limits

	def can_make_request(self):
		for lim in self.limits:
			if not lim.request_available():
				return False
			return True


class Metadata(object):
	def __init__(self, title='h5', limits=(RateLimit(10, 10), RateLimit(600, 600))):
		self.title = title
		self.limits = limits

	def meta_request(self, url, params=None, headers=None):
		if params is None:
			params = {}

		if headers is None:
			headers = {'Ocp-Apim-Subscription-Key': config.MY_KEY}

		entries = {}
		for key, value in params.items():
			if key not in entries:
				entries[key] = value

		r = requests.get(
			'https://www.haloapi.com/metadata/{title}/metadata/{url}'.format(
				title=self.title,
				url=url),
			params=entries,
			headers=headers)
		for lim in self.limits:
			lim.add_request()
		raise_status(r)
		return r.json()

	def get_campaign_missions(self):
		url = 'campaign-missions'
		return self.meta_request(url)

	def get_commendations(self):
		url = 'commendations'
		return self.meta_request(url)

	def get_csr_designations(self):
		url = 'csr-designations'
		return self.meta_request(url)

	def get_enemies(self):
		url = 'enemies'
		return self.meta_request(url)

	def get_flexible_stats(self):
		url = 'flexible-stats'
		return self.meta_request(url)

	def get_game_base_variants(self):
		url = 'game-base-variants'
		return self.meta_request(url)

	def get_game_variants_by_id(self, variant_id):
		url = 'game-variants/{variant_id}'.format(variant_id=variant_id)
		return self.meta_request(url)

	def get_impulses(self):
		url = 'impulses'
		return self.meta_request(url)

	def get_maps_variants_by_id(self, map_id):
		url = 'map-variants/{map_id}'.format(map_id=map_id)
		return self.meta_request(url)

	def get_maps(self):
		url = 'maps'
		return self.meta_request(url)

	def get_medals(self):
		url = 'medals'
		return self.meta_request(url)

	def get_playlists(self):
		url = 'playlists'
		return self.meta_request(url)

	def get_requisition_packs_by_id(self, reqpack_id):
		url = 'requisition-packs/{reqpack_id}'.format(reqpack_id=reqpack_id)
		return self.meta_request(url)

	def get_requisition_by_id(self, req_id):
		url = 'requisitions/{req_id}'.format(req_id=req_id)
		return self.meta_request(url)

	def get_skulls(self):
		url = 'skulls'
		return self.meta_request(url)

	def get_spartan_ranks(self):
		url = 'spartan-ranks'
		return self.meta_request(url)

	def get_team_colors(self):
		url = 'team-colors'
		return self.meta_request(url)

	def get_vehicles(self):
		url = 'vehicles'
		return self.meta_request(url)

	def get_weapons(self):
		url = 'weapons'
		return self.meta_request(url)


class Profile(object):
	def __init__(self, title='h5', limits=(RateLimit(10, 10), RateLimit(600, 600))):
		self.title = title
		self.limits = limits

	def profile_request(self, url, params=None, headers=None):
		"""
        Please note this returns the raw response NOT json (image data).
        """
		if params is None:
			params = {}

		if headers is None:
			headers = {'Ocp-Apim-Subscription-Key': config.MY_KEY}

		entries = {}
		for key, value in params.items():
			if key not in entries:
				entries[key] = value

		r = requests.get(
			'https://www.haloapi.com/profile/{title}/profiles/{url}'.format(
				title=self.title,
				url=url),
			params=entries,
			headers=headers,
			stream=True
		)
		for lim in self.limits:
			lim.add_request()
		raise_status(r)
		return r.raw

	def get_emblem_image_for_player(self, player, size=None):
		"""
        Returns emblem image for Gamertag
        :param player: (string) Gamertag of player
        :param size: (int) 95, 128, 190, 256, 512. If omitted 256 is assumed by API.
        :return: image data
        """
		url = '{player}/emblem'.format(player=player)
		return self.profile_request(url, {'size': size})

	def get_profile_image_for_player(self, player, size=None, crop=None):
		"""
		Returns profile image (stance) for player
		:param player: (string) Gamertag of player
		:param size: (int) 95, 128, 190, 256, 512. If omitted 256 is assumed by API
		:param crop: (string) "full" or "portrait". "Full" is assumed.
		:return: image data
		"""
		url = '{player}/spartan'.format(player=player)
		return self.profile_request(url, {'size': size, 'crop': crop})


class Stats(object):
	def __init__(self, title='h5', limits=(RateLimit(10, 10), RateLimit(600, 600))):
		self.title = title
		self.limits = limits

	def stats_request(self, url, params=None, headers=None):
		if params is None:
			params = {}

		if headers is None:
			headers = {'Ocp-Apim-Subscription-Key': config.MY_KEY}

		entries = {}
		for key, value in params.items():
			if key not in entries:
				entries[key] = value

		r = requests.get(
			'https://www.haloapi.com/stats/{title}/{url}'.format(
				title=self.title,
				url=url),
			params=entries,
			headers=headers
		)
		for lim in self.limits:
			lim.add_request()
		raise_status(r)
		return r.json()

	def events_for_match_by_id(self, match_id):
		"""
        Returns events for matchID
        :param match_id: (string) unique id for match. Can be got from get_matches_for_player()
        :return: json response
        """
		url = '/matches/{match_id}/events'.format(match_id=match_id)
		return self.stats_request(url)

	def get_matches_for_player(self, player, modes=None, start=None, count=None):
		"""
        Returns matches for player
        :param player:  (string) Gamertag of player
        :param modes:   (string) arena, campaign, custom, or warzone. Can be comma-seperated (no space)
        :param start:   (int) index (0-based)
        :param count:   (int) Max amount of results returned, if ommited 25 is assumed by the API
        :return: json response
        """
		url = 'players/{player}/matches'.format(player=player)
		return self.stats_request(url, {'modes': modes, 'start': start, 'count': count})

	def get_leaderboard(self, season_id, playlist_id, count=None):
		"""
        Returns leaderboards for season_id + playlist_id
        :param season_id:
        :param playlist_id:
        :param count:
        :return: json response
        """
		url = 'player-leaderboards/csr/{season_id}/{playlist_id}'.format(season_id=season_id, playlist_id=playlist_id)
		return self.stats_request(url, {'count': count})

	def get_arena_match_by_id(self, match_id):
		"""
        Returns arena match for matchID
        :param match_id: (string) unique id for match
        :return: json response
        """
		url = 'arena/matches/{match_id}'.format(match_id=match_id)
		return self.stats_request(url)

	def get_campaign_match_by_id(self, match_id):
		"""
        Returns campaign match for matchID
        :param match_id: (string) unique id for match
        :return: json response
        """
		url = 'campaign/matches/{match_id}'.format(match_id=match_id)
		return self.stats_request(url)

	def get_custom_match_by_id(self, match_id):
		"""
        Returns custom match for matchID
        :param match_id: (string) unique id for match
        :return: json response
        """
		url = 'custom/matches/{match_id}'.format(match_id=match_id)
		return self.stats_request(url)

	def get_warzone_match_by_id(self, match_id):
		"""
        Returns warzone match for matchID
        :param match_id: (string) unique id for match
        :return: json response
        """
		url = 'warzone/matches/{match_id}'.format(match_id=match_id)
		return self.stats_request(url)

	def get_arena_service_record_for_players(self, player_ids, season_id=None):
		"""
        Returns a json list of up to 32 service records
        :param player_ids: (string) comma-seperated string of gamertages (limit of 32)
        :param season_id: (string) guid of season, can be found through metadata api, defaults to current season
        :return: json response
        """
		url = 'servicerecords/arena'
		return self.stats_request(url, {'players': player_ids, 'seasonID': season_id})

	def get_campaign_service_record_for_players(self, player_ids):
		"""
        Returns list of up to 32 campaign service records
        :param player_ids: (string) comma-seperated gamertags (limit of 32)
        :return: json response
        """
		url = 'servicerecords/campaign'
		return self.stats_request(url, {'players': player_ids})

	def get_custom_service_record_for_players(self, player_ids):
		"""
        Returns list of up to 32 custom game service records
        :param player_ids: (string) comma-seperated gamertags (limit of 32)
        :return: json response
        """
		url = 'servicerecords/custom'
		return self.stats_request(url, {'players': player_ids})

	def get_warzone_servicerecord_for_players(self, player_ids):
		"""
        Returns a list of up to 32 warzone service records
        :param player_ids: (string) comma-seperated gamertags (limit of 32)
        :return: json response
        """
		url = 'servicerecords/warzone'
		return self.stats_request(url, {'players': player_ids})
