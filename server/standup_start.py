'''For a given channel, start the standup period whereby for the next 15 minutes if someone calls "standup_send" with a message, it is 
buffered during the 15 minute window then at the end of the 15 minute window a message will be added to the message queue in the channel
 from the user who started the standup.'''
from error import AccessError
def standup_start(token, channel_id):
    channel = [1,2,3]
    if channel_id not in channel:
        raise ValueError('Channel does not exit')
    pass