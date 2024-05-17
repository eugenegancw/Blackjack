from .participant import Participant

class Player(Participant):
    def __init__(self, name):
        super().__init__(name)
        self.score = 100 #starts off with 100 points first

    def get_score(self):
        return self.score
