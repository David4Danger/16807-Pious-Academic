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
            
    def meta_request(self, url, **kwargs):
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
                
        r = requests.get(
            'https://www.haloapi.com/metadata/{title}/metadata/{url}'.format(
                title=title,
                url=url
            ),
            params=args
        )
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()
    
    def profile_request(self, url, **kwargs):
        args = {'api_key': self.key}
        for k in kwargs:
            if kwargs[k] is not None:
                args[k] = kwargs[k]
                
        r = requests.get(
            'https://www.haloapi.com/profile/{title}/profiles/{url}'.format(
                title=title,
                url=url
            ),
            params=args
        )
        for lim in self.limits:
            lim.add_request()
        raise_status(r)
        return r.json()    
    
    def stats_request(self, url, **kwargs):
            args = {'api_key': self.key}
            for k in kwargs:
                if kwargs[k] is not None:
                    args[k] = kwargs[k]
                    
            r = requests.get(
                'https://www.haloapi.com/stats/{title}/{url}'.format(
                    title=title,
                    url=url
                ),
                params=args
            )
            for lim in self.limits:
                lim.add_request()
            raise_status(r)
            return r.json()       