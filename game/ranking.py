import game.constants as c

class Ranking:
    def __init__(self):
        self.ranking=[]
    def generateChanges(self):
        c.TOTAL=self.total
        c.RANKING=self.ranking
        c.RESULT_RANKING=self.result
