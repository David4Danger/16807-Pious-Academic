import PiousAcademic16807
import json

def main():
	# Meta requests
	# I'd recommend storing all of this data locally and updating it every once in a while to be sure your
	# metadata is up-to-date.
	# Note that the information used for game_variants_by_id is obtained from game_base_variants. The same
	# follows for maps_variants_by_id and maps.
	meta = PiousAcademic16807.Metadata()

	campaign_missions = meta.get_campaign_missions()
	commendations = meta.get_commendations()
	csr_designations = meta.get_csr_designations()
	enemies = meta.get_enemies()
	flexible_stats = meta.get_flexible_stats()
	game_base_variants = meta.get_game_base_variants()
	game_variants_by_id = meta.get_game_variants_by_id('1571fdac-e0b4-4ebc-a73a-6e13001b71d3')
	impulses = meta.get_impulses()
	maps_variants_by_id = meta.get_maps_variants_by_id('cb251c51-f206-11e4-8541-24be05e24f7e')
	maps = meta.get_maps()
	medals = meta.get_medals()
	playlists = meta.get_playlists()
	skulls = meta.get_skulls()
	spartan_ranks = meta.get_spartan_ranks()
	team_colors = meta.get_team_colors()
	vehicles = meta.get_vehicles()
	weapons = meta.get_weapons()

	# These two calls are, as of now, just demos. There is currently no endpoint that allows you to obtain a list of the
	# ids of all req packs and req items. This test data is just to confirm the integrity of the request itself, and was obtained
	# from the developer forums.
	# Moral of the story: Use the developer forums! There are helpful people there waiting to answer any and all questions.
	reqpacks = meta.get_requisition_packs_by_id('3a1614d9-20a4-4817-a189-88cb781e9152')
	req = meta.get_requisition_by_id('e4f549b2-90af-4dab-b2bc-11a46ea44103')

	# Stat requests
	# Note that I'm too lazy to write out demos for requests of similar nature. So in the case of all service record requests,
	# the format is that exact same as the history constant I defined below. The same follows for all post-game carnage
	# report requests, they follow the format that arena_match_by_id uses.
	stats = PiousAcademic16807.Stats()
	history = stats.get_arena_service_record_for_players('ROFL A WET SOCK,ScorchedAbyss')
	playermatches1 = stats.get_matches_for_player('ROFL A WET SOCK')
	playermatches2 = stats.get_matches_for_player('ROFL A WET SOCK', 'warzone')
	arena_match_by_id = stats.get_warzone_match_by_id('2568c24a-7604-4a55-9fac-201f03f3b813')

	# Profile requests
	# Note that these return image data and NOT json (not even JSON with a link to an image).
	profile = PiousAcademic16807.Profile()
	emblem_image = profile.get_emblem_image_for_player('ROFL A WET SOCK')
	profile_image = profile.get_profile_image_for_player('ROFL A WET SOCK')


if __name__ == "__main__":
	main()