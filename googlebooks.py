import json
import requests

volumes = '/volumes/'
origin = 'https://www.googleapis.com/books/v1'

class Book(object):
    def __init__(self):
       pass

    def _get(self, path, params = None):
        if params is None:
            params = {}
        answer = requests.get(origin + path, params=params)
        if answer.status_code == 200:
            return json.loads(answer.content)
        return answer
    
    def info(self, q, **args):
        path = volumes
        params = dict(q=q)
        for parameter in 'download filter langRestrict libraryRestrict maxResults orderBy partner printType projection showPreorders source startIndex'.split():
            if parameter in args:
                params[parameter] = args[parameter]
        return self._get(volumes, params)
    
    def get(self, volumeId, **args):
        path = volumes + volumeId
        params = dict()
        for p in 'partner projection source'.split():
            if p in args:
                params[p] = args[p]
        return self._get(path)

