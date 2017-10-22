import requests
import json


class ServiceLogin:
    URL = "https://starwarsconsola.herokuapp.com/StarWarsConsole/login_juego/"

    def __init__(self):
            pass

    def login(self,user, password):

        payload= {'id':user,'password':password}
        r = requests.post(self.URL,json=payload)
        res = r.json()
        respuesta=res[0]
        respuesta=respuesta['result']
        if (respuesta=="true"):
            estado=True
        else:
            estado=False
        return estado


