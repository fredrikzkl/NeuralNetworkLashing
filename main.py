import numpy as np
import pandas as pd

def getHeroesInMatch(id):
    return players.loc[players['match_id'] == id]

def getHeroesInTeam(heroes, slots):
    return heroes.loc[(heroes['player_slot'] >= slots[0]) & (heroes['player_slot'] <= slots[1])]

def generateInputArray(playersInTeam):
    array = np.empty(len(heroes))
    array.fill(0)

    for i in range(len(playersInTeam)):
        hero = players.loc[i]['hero_id']
        array[hero - 1] = 1

    return array


#Init variables
direSlots = [128,132]
radiantSlots = [0,4]
path = "../dota_dataset/"
#Fetch relevant data
matches = pd.read_csv(path + "match.csv")
players = pd.read_csv(path + "players.csv")
heroes = pd.read_csv(path + "hero_names.csv")['hero_id'].values



playersInMatch = getHeroesInMatch(0)


radiantArray = generateInputArray(getHeroesInTeam(playersInMatch, radiantSlots))
direArray = generateInputArray(getHeroesInTeam(playersInMatch, direSlots))

print(radiantArray)
print(direArray)



