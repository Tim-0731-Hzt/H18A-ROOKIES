from error import AccessError
from channel import *
from message import *
from auth import *
from data import *
import time
from datetime import datetime, timedelta
import pickle_unpickle
def standup_start(token, channel_id):
   
    data = load()
    channelDict = data['channelDict']

    opid = getUserFromToken(token)
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            if opid not in ch['channelmember'] and opid not in ch['channelowner']:
                raise AccessError('You are not a member of this channel')
            if ch['standup'] == 1:
                raise AccessError('this channel is already in standup')
            ch['standup'] == 1
            save(channelDict)
            t_end = time.time() + 60*15
            while time.time() < t_end:


            '''time out'''
            channelDt = load().['channelDict']
            for channel in channelDt:
                if channel_id == channel['channel_id']:
                    channel['standup'] == 0
                    message_send(token, channel_id, channel['standlist'])
                    channel['standlist'] == ''
                    save(channelDict)            
            return
    raise ValueError('incorrect channel id')
    pass
            

def showtime():
    now = datetime.now()
    now_15 = now + timedelta(minutes=15)
    return now_15

def standup_send(token, channel_id, message):
    data = load()
    channelDict = data['channelDict']
    
    if len(message) > 1000 :
        raise ValueError("Message too long")
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            if opid not in ch['channelmember'] and opid not in ch['channelowner']:
                raise AccessError('You are not a member of this channel')
            if ch['standup'] != 1:
                raise ValueError(
                    'An active standup is not currently running in this channel')
            if ch['standlist'] == "":
                ch['standlist'] = message
                save(channelDict)
                return
            else:
                ch['standlist'] = ch['standlist'] + ": " + message
                save(channelDict)
                return
    raise ValueError('Channel ID is not a valid channel')
    pass
    
