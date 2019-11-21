class MatchData:
    def __init__(self, radiantWin, heroArray):
        if(radiantWin):
            self.radiantWin = 1
        else:
            self.radiantWin = 0

        self.heroArray = heroArray

