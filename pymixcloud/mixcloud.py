import requests

BASE_URL = 'http://api.mixcloud.com/'

class Mixcloud:
    def __init__(self, requests_module=requests):
        self.requests = requests
        
    def _get(self, params=[]):
        params.append['']
        '/'.join([BASE_URL].extend(params))
        
        r = self.requests.get(url)
        r.raise_for_status()
        
        return r.json
            
    def cloudcast(self, user, cloudcast):
        return self._get([user, cloudcast])
        
    def user(self, user):
        return self._get([user])
        
    def tag(self, tag):
        return self._get(['tag', tag])
        
    def artist(self, artist):
        return self._get(['artist', artist])
        
    def track(self, artist, track):
        return self._get(['track', artist, track])
        
    def category(self, category):
        return self._get(['category', category])