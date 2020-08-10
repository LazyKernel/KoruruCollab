import urllib
import json 
    
class WebEndpoint:

    def __init__(self, host, port):
        self.url = str(host) + ':' + str(port)
    
    def get(self, endpoint):
        with urllib.request.urlopen(self.url + endpoint) as res:
            return json.load(res)
            