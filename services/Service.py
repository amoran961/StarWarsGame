import requests
import json


class ServiceLogin:
    URL = ""

    def __init__(self):
            pass

    def login(self,user, password):
        par= {'usuarios':user,'password':user}
        r = requests.get(url=self.URL, params=par)
        data = r.json()
        estado=data['estado']
        return estado


