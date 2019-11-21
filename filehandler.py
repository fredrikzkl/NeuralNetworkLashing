import pickle

def load_data():
    try:
        with open("bin.dat",'rb') as f:
            d = pickle.load(f)
            print("Loaded data from file...")
    except:
        print("Could not load file")
        d = [], []
    return d

def save_data(data):
    with open("bin.dat", "wb") as f:
        pickle.dump(data, f)
        print("Data dumped to file...")


def load_into_matrix():
    data = load_data()
    wins = []
    heroes = []

    for i in range(len(data)):
        wins.append(data[i].radiantWin)
        heroes.append(data[i].heroArray)

    return wins, heroes
