import pickle
import os
f = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datastore.p')
def save(DATA):
    with open(str(f), 'wb') as FILE:
        pickle.dump(DATA, FILE)

def load():
    DATA = pickle.load(open(str(f), "rb"))
    return DATA

def restart():
    DATA = {
        'messDict': [],
        'messID': 0,
        'channelDict': [],
        'userDict': []
    }
    with open(str(f), 'wb') as FILE:
        pickle.dump(DATA, FILE)