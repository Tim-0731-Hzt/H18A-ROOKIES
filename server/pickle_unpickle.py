import pickle

def save(DATA):
    with open('datastore.p', 'wb') as FILE:
        pickle.dump(DATA, FILE)

def load():
    DATA = pickle.load(open("datastore.p", "rb"))
    return DATA

def restart():
    DATA = {
        'messDict': [],
        'messID': 0,
        'reactDict': [],
        'channelDict': [],
        'userDict': []
    }
    with open('datastore.p', 'wb') as FILE:
        pickle.dump(DATA, FILE)