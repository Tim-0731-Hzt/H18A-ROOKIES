from server.channel import *
from server.message_pickle import *
from server.auth_pickle import *

import server.pickle_unpickle
def search(token, query_str): 
    data = load()
    messDict = data['messDict']
    result = []
    channel_list = channels_list(token)['channels']
    cha_ids = []
    for cha in channel_list:
        cha_ids.append(cha['channel_id'])
    l = []
    for meg in messDict:
        if meg['channel_id'] in cha_ids:
            if meg['message'] == query_str:
                m = {
                    'message_id': meg['message_id'],
                    'u_id': meg['u_id'],
                    'message': meg['message'],
                    'time_created': meg['time_created'],
                    'reacts': meg['reacts'],
                    'is_pinned': meg['is_pinned']
                }
                l.append(m)
    return {'messages': l}

    '''for channel in channel_list :
        if channel['channel_id'] == meg['channel_id']:
            if query_str == meg['message']:
                result.append(meg['message'])
    return result'''
    
