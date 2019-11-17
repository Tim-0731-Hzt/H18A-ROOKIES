from server.channel import channels_list
from server.pickle_unpickle import load

def search(token, query_str):
    data = load()
    messDict = data['messDict']
    channel_list = channels_list(token)['channels']
    cha_ids = []
    for cha in channel_list:
        cha_ids.append(cha['channel_id'])
    lis = []
    for meg in messDict:
        if meg['channel_id'] in cha_ids:
            if meg['message'] == query_str:
                mess = {
                    'message_id': meg['message_id'],
                    'u_id': meg['u_id'],
                    'message': meg['message'],
                    'time_created': meg['time_created'],
                    'reacts': meg['reacts'],
                    'is_pinned': meg['is_pinned']
                }
                lis.append(mess)
    return {'messages': lis}
