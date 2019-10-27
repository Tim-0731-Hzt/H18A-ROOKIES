from channel import *
from message import *
from auth import *

import pickle_unpickle
def search(token, query_str): 
    data = load()
    messDict = data['messDict']
    result = []
    it = channels_list(token)
    for meg in messDict:
        for channel in it :
            if channel['channel_id'] == meg['channel_id']:
                if query_str == meg['message']:
                    result.append(meg['message'])
    return result
    
