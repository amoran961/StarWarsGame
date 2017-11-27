import requests
import json
import game.gameconf as gc
import game.ranking as gr
import game.constants as c
class ServiceLogin:
    def __init__(self):
            pass

    def login(self,user, password):
        url = "https://starwarsconsola.herokuapp.com/StarWarsConsole/login_juego/"
        payload= {'id':user,'password':password}
        r = requests.post(url,json=payload)
        res = r.json()
        respuesta=res[0]
        result=respuesta['result']
        if (result=="true"):
            mision = respuesta['mision']
            bando = respuesta['bando']
            dificultad = respuesta['dificultad']
            config=gc.GameConfig()
            config.mision=mision
            config.bando=bando
            config.dificultad=dificultad
            config.generateChanges()
            result=True
        else:
            result=False
        return result

    def register(self,user, password):
        result=False
        url = "https://starwarsconsola.herokuapp.com/StarWarsConsole/register_juego/"
        payload= {'id':user,'password':password}
        try:
            r = requests.post(url,json=payload)
            res = r.json()
            respuesta=res[0]
            result=respuesta['result']
            if (result=="true"):
                result=True
            else:
                result = False
        except requests.exceptions.HTTPError as err:
            print(err)
        except ValueError:
            print("Usuario ya existe")
        return result

    def register_record(self,user,record):
        result=False
        url = "https://starwarsconsola.herokuapp.com/StarWarsConsole/register_record/"
        payload = {'id':user,'record':record}
        try:
            r = requests.post(url,json=payload)
            res=r.json()
            respuesta=res[0]
            result=respuesta['result']
            if(result=="true"):
                result=True
        except requests.exceptions.HTTPError as err:
            print(err)
        return result

    def ranking(self):
        result=False
        url = "https://starwarsconsola.herokuapp.com/StarWarsConsole/ranking/"
        r = requests.post(url)
        res=r.json()
        respuesta=res[0]
        result=respuesta['result']
        rank = gr.Ranking()
        rank.result=result
        if (result=='true'):
            c.RANKING = respuesta['ranking']
            c.RESULT_RANKING=True
        else:
            c.RESULT_RANKING=False