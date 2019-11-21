import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import filehandler

class MatchData:
    def __init__(self, radiantWin, heroArray):
        if(radiantWin):
            self.radiantWin = 1
        else:
            self.radiantWin = 0

        self.heroArray = heroArray


class MatchDataset(Dataset):
    def __init__(self, wins, heroes):
        self.len = len(wins)
        self.wins = torch.tensor(wins, dtype=torch.float)
        self.heroes = torch.tensor(heroes, dtype=torch.float)

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        return self.wins[item], self.heroes[item]


