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


