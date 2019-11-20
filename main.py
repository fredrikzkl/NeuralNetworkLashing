from src import utils

import pandas as pd

def getHeroesInMatch(id):
    return 0

path = "../dota_dataset/"

matches = pd.read_csv(path + "match.csv")
players = pd.read_csv(path + "players.csv")
heroes = pd.read_csv(path + "hero_names.csv")['hero_id'].values

print(len(heroes))


heroList = heroes['hero_id']

print(heroList)

#utils.defineInputs(matches.loc[0], heroList)





print("hello world")

