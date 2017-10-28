import requests
import json
import game.gameconf as gc

class ServiceLogin:
    URL = "https://starwarsconsola.herokuapp.com/StarWarsConsole/login_juego/"

    def __init__(self):
            pass

    def login(self,user, password):
        payload= {'id':user,'password':password}
        '''r = requests.post(self.URL,json=payload)
        res = r.json()
        respuesta=res[0]
        result=respuesta['result']
        '''
        result=True
        gamecf= gc.GameConfig()
        gamecf.mision="Luna de Endor"
        gamecf.bando="Rebelde"
        gamecf.dificultad="Facil"
        gamecf.generateChanges()
        '''
        if (result=="true"):
            mision = respuesta['mision']
            bando = respuesta['bando']
            dificultad = respuesta['dificultad']
            config=gc.GameConfig(result)
            config.mision=mision
            config.bando=bando
            config.dificultad=dificultad
        else:
            config = gc.GameConfig(result)
        '''
        return result


