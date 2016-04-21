import PiousAcademic16807
import json
import time
import os
import config


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
    time.sleep(1)  # stops requesting things too quickly

    
def main():
    api = PiousAcademic16807.Metadata()

    check_or_create_path(os.path.join(config.METADATA_DATA_PATH))

    campaign_missions = api.get_campaign_missions()
    dump_json_to_path(campaign_missions, os.path.join(config.METADATA_DATA_PATH, 'campaignmissions.json'))
    print '=> Stored Campaign Missions at path: %s' % (os.path.join(config.METADATA_DATA_PATH, 'campaignmissions.json'))

    commendations = api.get_commendations()
    dump_json_to_path(commendations, os.path.join(config.METADATA_DATA_PATH, 'commendations.json'))
    print '=> Stored Commendations: %s' % (os.path.join(config.METADATA_DATA_PATH, 'commendations.json'))

    csr_designations = api.get_csr_designations()
    dump_json_to_path(csr_designations, os.path.join(config.METADATA_DATA_PATH, 'CSRdesignations.json'))
    print '=> Stored CSR Designations: %s' % (os.path.join(config.METADATA_DATA_PATH, 'CSRdesignations.json'))

    enemies = api.get_enemies()
    dump_json_to_path(enemies, os.path.join(config.METADATA_DATA_PATH, 'enemies.json'))
    print '=> Stored Enemies: %s' % (os.path.join(config.METADATA_DATA_PATH, 'enemies.json'))

    flexible_stats = api.get_flexible_stats()
    dump_json_to_path(flexible_stats, os.path.join(config.METADATA_DATA_PATH, 'flexiblestats.json'))
    print '=> Stored Flexible Stats: %s' % (os.path.join(config.METADATA_DATA_PATH, 'flexiblestats.json'))

    game_base_variants = api.get_game_base_variants()
    dump_json_to_path(game_base_variants, os.path.join(config.METADATA_DATA_PATH, 'gamebasevariants.json'))
    print '=> Stored Game Base Variants: %s' % (os.path.join(config.METADATA_DATA_PATH, 'gamebasevariants.json'))

    impulses = api.get_impulses()
    dump_json_to_path(impulses, os.path.join(config.METADATA_DATA_PATH, 'impulses.json'))
    print '=> Stored Impluses: %s' % (os.path.join(config.METADATA_DATA_PATH, 'impulses.json'))

    maps = api.get_maps()
    dump_json_to_path(maps, os.path.join(config.METADATA_DATA_PATH, 'maps.json'))
    print '=> Stored Maps: %s' % (os.path.join(config.METADATA_DATA_PATH, 'maps.json'))

    medals = api.get_medals()
    dump_json_to_path(medals, os.path.join(config.METADATA_DATA_PATH, 'medals.json'))
    print '=> Stored Medals: %s' % (os.path.join(config.METADATA_DATA_PATH, 'medals.json'))

    playlists = api.get_playlists()
    dump_json_to_path(playlists, os.path.join(config.METADATA_DATA_PATH, 'playlists.json'))
    print '=> Stored Playlists: %s' % (os.path.join(config.METADATA_DATA_PATH, 'playlists.json'))

    skulls = api.get_skulls()
    dump_json_to_path(skulls, os.path.join(config.METADATA_DATA_PATH, 'skulls.json'))
    print '=> Stored Skulls: %s' % (os.path.join(config.METADATA_DATA_PATH, 'skulls.json'))

    spartan_ranks = api.get_spartan_ranks()
    dump_json_to_path(spartan_ranks, os.path.join(config.METADATA_DATA_PATH, 'spartanranks.json'))
    print '=> Stored Spartan Ranks: %s' % (os.path.join(config.METADATA_DATA_PATH, 'spartanranks.json'))

    team_colors = api.get_team_colors()
    dump_json_to_path(team_colors, os.path.join(config.METADATA_DATA_PATH, 'teamcolors.json'))
    print '=> Stored Team Colors: %s' % (os.path.join(config.METADATA_DATA_PATH, 'teamcolors.json'))

    vehicles = api.get_vehicles()
    dump_json_to_path(vehicles, os.path.join(config.METADATA_DATA_PATH, 'vehicles.json'))
    print '=> Stored Vehicles: %s' % (os.path.join(config.METADATA_DATA_PATH, 'vehicles.json'))

    weapons = api.get_weapons()
    dump_json_to_path(weapons, os.path.join(config.METADATA_DATA_PATH, 'weapons.json'))
    print '=> Stored Weapons: %s' % (os.path.join(config.METADATA_DATA_PATH, 'weapons.json'))

    # now use the above static data to execute the variant meta requests
    with open(os.path.join(config.METADATA_DATA_PATH, 'maps.json')) as data_file:
        mapfile = json.load(data_file)
    mapvariants = {}

    for item in mapfile:
        while True:
            try:
                mapid = item['id']
                variantinfo = api.get_maps_variants_by_id(mapid)
                mapvariants[mapid] = variantinfo
                time.sleep(1)
            except Exception as e:
                time.sleep(9)
                print "Error: %s" % e
                continue
            break

    dump_json_to_path(mapvariants, os.path.join(config.METADATA_DATA_PATH, 'mapvariants.json'))
    print "=> Stored Map Variants: %s" % (os.path.join(config.METADATA_DATA_PATH, 'mapvariants.json'))

    with open(os.path.join(config.METADATA_DATA_PATH, 'gamebasevariants.json')) as data_file:
        gamefile = json.load(data_file)
    gamevariants = {}
    for item in gamefile:
        while True:
            try:
                gameid = item['id']
                variantinfo = api.get_game_variants_by_id(gameid)
                gamevariants[gameid] = variantinfo
                time.sleep(1)
            except Exception as e:
                time.sleep(9)
                print "Error: %s" % e
                continue
            break

    dump_json_to_path(gamevariants, os.path.join(config.METADATA_DATA_PATH, 'gamevariants.json'))
    print "'=> Stored Game Variants: %s" % (os.path.join(config.METADATA_DATA_PATH, 'gamevariants.json'))

    # Still can't do these meta request because there is no actual endpoint that returns all the ids :*[
    # reqpacks = api.get_requisition_packs_by_id('3a1614d9-20a4-4817-a189-88cb781e9152')
    # req = api.get_requisition_by_id('e4f549b2-90af-4dab-b2bc-11a46ea44103')
    
if __name__ == "__main__":
    main()
