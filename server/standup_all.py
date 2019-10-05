from error import AccessError
def standup_start(token, channel_id):
    channel = [1,2,3]
    if channel_id not in channel:
        raise ValueError('Channel does not exit')
    pass
def standup_send(token, channel_id, message):
    channel = [1,2,3,4,5,6,7,8,9]
    if channel_id not in channel :
        raise ValueError("Channel does not exit")
    if len(message) > 1000 :
        raise ValueError("Message too long")
    pass
