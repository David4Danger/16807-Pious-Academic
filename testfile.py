from PiousAcademic16807 import PiousAcademic
import json

def main():
    api = PiousAcademic()
    
    #Meta requests
    #I'd recommend storing all of this data locally and updating it every once in a while to be sure your
    #metadata is up-to-date.
    #Note that the information used for game_variants_by_id is obtained from game_base_variants. The same
    #follows for maps_variants_by_id and maps.
    campaign_missions = api.get_campaign_missions()
    commendations = api.get_commendations()
    csr_designations = api.get_csr_designations()
    enemies = api.get_enemies()
    flexible_stats = api.get_flexible_stats()
    game_base_variants = api.get_game_base_variants()
    game_variants_by_id = api.get_game_variants_by_id('1571fdac-e0b4-4ebc-a73a-6e13001b71d3')
    impulses = api.get_impulses()
    maps_variants_by_id = api.get_maps_variants_by_id('cb251c51-f206-11e4-8541-24be05e24f7e')
    maps = api.get_maps()
    medals = api.get_medals()
    playlists = api.get_playlists()
    skulls = api.get_skulls()
    spartan_ranks = api.get_spartan_ranks()
    team_colors = api.get_team_colors()
    vehicles = api.get_vehicles()
    weapons = api.get_weapons()
    
    #These two calls are, as of now, just demos. There is currently no endpoint that allows you to obtain a list of the
    #ids of all req packs and req items. This test data is just to confirm the integrity of the request itself, and was obtained
    #from the developer forums.
    #Moral of the story: Use the developer forums! There are helpful people there waiting to answer any and all questions.
    reqpacks = api.get_requisition_packs_by_id('3a1614d9-20a4-4817-a189-88cb781e9152')
    req = api.get_requisition_by_id('e4f549b2-90af-4dab-b2bc-11a46ea44103')    
    
    #Stat requests
    #Note that I'm too lazy to write out demos for requests of similar nature. So in the case of all service record requests,
    #the format is that exact same as the history constant I defined below. The same follows for all post-game carnage
    #report requests, they follow the format that arena_match_by_id uses.
    history = api.get_arena_servicerecord_for_players('ROFL A WET SOCK,ScorchedAbyss')
    playermatches1 = api.get_matches_for_player('ROFL A WET SOCK')
    playermatches2 = api.get_matches_for_player('ROFL A WET SOCK','warzone')
    arena_match_by_id = api.get_warzone_match_by_id('2568c24a-7604-4a55-9fac-201f03f3b813')
    
if __name__ == "__main__":
    main()          