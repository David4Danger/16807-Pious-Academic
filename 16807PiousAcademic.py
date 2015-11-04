from collections import deque
import time
import requests

class i343Exception(Exception):
    def __init__(self, error, response):
        self.error = error
        self.headers = response.headers

    def __str__(self):
        return self.error

error_302 = 'Golden Path. The Location header should point at the corresponding emblem image.'
error_400 = 'An unsupported value was provided for a query string parameter.'
error_404 = 'Specified Title was not "h5"/Specified player gamertag was not found.'
error_500 = 'Internal Server Error'

def raise_status(response):
    if response.status_code == 302:
        raise i343Exception(error_302, response)
    elif response.status_code == 400:
        raise i343Exception(error_400, response)
    elif response.status_code == 404:
        raise i343Exception(error_404, response)
    elif response.status_code == 500:
        raise i343Exception(error_500, response)
    else:
        response.raise_for_status()
        
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
    
class PiousAcademic:
    def __init__(self, key, title="h5", limits=(RateLimit(100,10))):
        self.key = key
        self.title = title
        self.limits = limits
        
    def can_make_request(self):
        for lim in self.limits:
                    if not lim.request_available():
                        return False
                return True        
            
    def meta_request(self, url, params={}):
        entries = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in entries:
                entries[key] = value
                
        r = requests.get(
            'https://www.haloapi.com/metadata/{title}/metadata/{url}'.format(
                title=title,
                url=url),
            params = entries)
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()
    
    def  get_campaign_missions(self):
        url = 'campaign-missions'
        return self.meta_request(url)
    
    def  get_commendations(self):
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
        
    def get_game_variants_by_id(self,  varID):
        url = 'game-variants/{id1}'.format(
            id1 = varID)
        return self.meta_request(url)    
    
    def get_impulses(self):
        url = 'impulses'
        return self.meta_request(url)
    
    def get_game_variants_by_id(self,  mapID):
        url = 'map-variants/{id1}'.format(
            id1 = mapID)
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

    def get_requisition_packs_by_id(self, reqpackID):
        url = 'requisition-packs/{id1}'.format(
            id1 = reqpackID)
        return self.meta_request(url)      
    
    def get_requisition_by_id(self, reqID):
            url = 'requisitions/{id1}'.format(
                id1 = reqID)
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
    
    def profile_request(self, url, params={}):
        entries = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in entries:
                entries[key] = value
                
        r = requests.get(
            'https://www.haloapi.com/profile/{title}/profiles/{url}'.format(
                title=title,
                url=url
            ),
            params = entries
        )
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()    
    
    def stats_request(self, url, params={}):
        entries = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in entries:
                entries[key] = value
                    
            r = requests.get(
                'https://www.haloapi.com/stats/{title}/{url}'.format(
                    title=title,
                    url=url
                ),
                params = entries
            )
            for lim in self.limits:
                lim.add_request()
            raise_status(r)
            return r.json()       
        
    def get_matches_for_player(self, playerID, modes=None, start=None, count=None):
        url = 'players/{player}/matches'.format(player = playerID)
        return self.stats_request(url,
                                 modes=modes if modes is not None else None,
                                 start=start if start is not None else None,
                                 count=count if count is not None else None)
    
    def get_arena_match_by_id(self, matchID):
        url = 'arena/matches/{matchId}'.format(
            matchId = matchID)
        return self.stats_request(url)              
        
    def get_campaign_match_by_id(self, matchID):
        url = 'campaign/matches/{matchId}'.format(
            matchId = matchID)
        return self.stats_request(url)
    
    def get_custom_match_by_id(self, matchID):
        url = 'custom/matches/{matchId}'.format(
            matchId = matchID)
        return self.stats_request(url)    
        
    def get_warzone_match_by_id(self, matchID):
        url = 'warzone/matches/{matchId}'.format(
            matchId = matchID)
        return self.stats_request(url)       
    
    def get_arena_servicerecord_for_players(self, playerIDs):
        url = 'servicerecords/arena'
        return self.stats_request(url,
                                  playerIDs)
    
    def get_campaign_servicerecord_for_players(self, playerIDs):
        url = 'servicerecords/campaign'
        return self.stats_request(url,
                                  playerIDs)    
        
    def get_custom_servicerecord_for_players(self, playerIDs):
        url = 'servicerecords/custom'
        return self.stats_request(url,
                                  playerIDs)    

    def get_warzone_servicerecord_for_players(self, playerIDs):
        url = 'servicerecords/warzone'
        return self.stats_request(url,
                                  playerIDs)        