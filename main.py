import numpy as np
import pandas as pd
import matchData
import filehandler

from nettverk import Nettverk

import torch.optim as optim

from trainer import trainer


def getHeroesInMatch(id):
    return players.loc[players['match_id'] == id]

def isRadiant(slot):
    return (slot >= radiantSlots[0]) & (slot <= radiantSlots[1])


def generateInputArray(players):
    array = np.empty(len(heroes))
    array.fill(0)

    for index, row in players.iterrows():
        hero = row['hero_id']
        slot = row['player_slot']
        if isRadiant(slot):
            array[hero - 1] = 1
        else:
            array[hero - 1] = -1
    return array


#Init variables
direSlots = [128,132]
radiantSlots = [0,4]
path = "../dota_dataset/"
#Fetch relevant data
matches = pd.read_csv(path + "match.csv").head(100)
players = pd.read_csv(path + "players.csv")
heroes = pd.read_csv(path + "hero_names.csv")['hero_id'].values

model = Nettverk()
data = []

for index, row in matches.iterrows():
    heroesInMatch = getHeroesInMatch(row['match_id'])
    temp_heroArray = generateInputArray(heroesInMatch)
    temp = matchData.MatchData(radiantWin=row['radiant_win'], heroArray=temp_heroArray)
    data.append(temp)

print("Completed processing til data set!")

filehandler.save_data(data=data)