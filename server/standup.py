from server.Error import AccessError, ValueError
from server.channel import *
from server.message_pickle import *
import threading
from server.auth_pickle import *

import time
from datetime import datetime, timedelta
import server.pickle_unpickle
def standup_start(token, channel_id, second):
    
    data = load()
    channelDict = data['channelDict']

    opid = getUserFromToken(token)
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            if opid not in ch['channel_member'] and opid not in ch['channel_owner']:
                raise AccessError('You are not a member of this channel')
            if ch['standUp'] == 1:
                raise ValueError('this channel is already in standup')
            ch['standUp'] = 1
            
            data['channelDict'] = channelDict
            save(data)
            
            timer = threading.Timer(second,send,[channel_id,token])
            timer.start()
                    
            return
    raise ValueError('incorrect channel id')
  
            
def send(channel_id,token):
    
    data = load()
    channelDict = data['channelDict']
    for channel in channelDict:
        if channel_id == channel['channel_id']:
            channel['standUp'] == 0
            message_send(token, channel_id, channel['standlist'])
            channel['standlist'] == ''
            data['channelDict'] = channelDict
            save(data)
            
            return

def showtime(time):
    now = datetime.now()
    now_15 = now + timedelta(seconds=int(time))
    return now_15

def standup_send(token, channel_id, message):
    data = load()
    channelDict = data['channelDict']
    userDict = data['userDict']
    
    opid = getUserFromToken(token)
    for user in userDict:
        if user['u_id'] == opid:
            name = user['first_name']
    if len(message) > 1000 :
        raise ValueError("Message too long")
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            if opid not in ch['channel_member'] and opid not in ch['channel_owner']:
                raise AccessError('You are not a member of this channel')
            if ch['standUp'] != 1:
                raise ValueError(
                    'An active standup is not currently running in this channel')
            append = name + ': ' + message
            if ch['standlist'] == "":
                ch['standlist'] = append
                data['channelDict'] = channelDict
                save(data)
                return
            else:
                ch['standlist'] = ch['standlist'] + ' ' + append
                data['channelDict'] = channelDict
                save(data)
                return
    raise ValueError('Channel ID is not a valid channel')
  
    
