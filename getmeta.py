from PiousAcademic16807 import PiousAcademic
import json
import time
    
def main():
    api = PiousAcademic()
    
    campaign_missions = api.get_campaign_missions()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\campaignmissions.json', 'w') as fp:
        json.dump(campaign_missions, fp)    
            
    commendations = api.get_commendations()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\commendations.json', 'w') as fp:
        json.dump( commendations, fp)
                            
    csr_designations = api.get_csr_designations()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\CSRdesignations.json', 'w') as fp:
        json.dump(csr_designations, fp)    
                            
    enemies = api.get_enemies()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\enemies.json', 'w') as fp:
        json.dump(enemies, fp)    
                            
    flexible_stats = api.get_flexible_stats()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\flexiblestats.json', 'w') as fp:
        json.dump(flexible_stats, fp)        
        
    game_base_variants = api.get_game_base_variants()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\gamebasevariants.json', 'w') as fp:
        json.dump(game_base_variants, fp)        
                            
    impulses = api.get_impulses()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\impulses.json', 'w') as fp:
        json.dump(impulses, fp)  
                            
    maps = api.get_maps()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\maps.json', 'w') as fp:
        json.dump(maps, fp)  
                            
    medals = api.get_medals()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\medals.json', 'w') as fp:
        json.dump(medals, fp)       
                            
    playlists = api.get_playlists()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\playlists.json', 'w') as fp:
        json.dump(playlists, fp)  
                            
    skulls = api.get_skulls()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\skulls.json', 'w') as fp:
        json.dump(skulls, fp)       
                            
    spartan_ranks = api.get_spartan_ranks()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\spartanranks.json', 'w') as fp:
        json.dump(spartan_ranks, fp)      
                            
    team_colors = api.get_team_colors()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\teamcolors.json', 'w') as fp:
        json.dump(team_colors, fp)     
                            
    vehicles = api.get_vehicles()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\vehicles.json', 'w') as fp:
        json.dump(vehicles, fp)    
                            
    weapons = api.get_weapons()
    time.sleep(1)
    with open(r'E:\Python Programs\BTB.net Work\Metadata\weapons.json', 'w') as fp:
        json.dump(weapons, fp)    
    
    #now use the above static data to execute the variant meta requests
    with open(r'E:\Python Programs\BTB.net Work\Metadata\maps.json') as data_file:
        mapfile = json.load(data_file)
    mapvariants = {}
    for item in mapfile:
        while True:
            try:
                mapid = item['id']
                variantinfo = api.get_maps_variants_by_id(mapid)
                mapvariants[mapid] = variantinfo
                print(len(mapvariants))
            except:
                time.sleep(9)
                continue
            break
    with open(r'E:\Python Programs\BTB.net Work\Metadata\mapvariants.json', 'w') as fp:
        json.dump(mapvariants, fp)
        
    with open(r'E:\Python Programs\BTB.net Work\Metadata\gamebasevariants.json') as data_file:
        gamefile = json.load(data_file)
    gamevariants = {}
    for item in gamefile:
        while True:
            try:
                gameid = item['id']
                variantinfo = api.get_game_variants_by_id(gameid)
                gamevariants[gameid] = variantinfo
                print(len(gamevariants))
            except:
                time.sleep(9)
                continue
            break
    with open(r'E:\Python Programs\BTB.net Work\Metadata\gamevariants.json', 'w') as fp:
        json.dump(gamevariants, fp)    
    
    #Still can't do these meta request because there is no actual endpoint that returns all the ids :*[                    
    #reqpacks = api.get_requisition_packs_by_id('3a1614d9-20a4-4817-a189-88cb781e9152')
    #req = api.get_requisition_by_id('e4f549b2-90af-4dab-b2bc-11a46ea44103')    
    
if __name__ == "__main__":
    main()