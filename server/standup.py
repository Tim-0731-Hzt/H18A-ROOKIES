from server.Error import AccessError, ValueError
# from server.channel import *
from server.message_pickle import message_send
import threading
from server.auth_pickle import getUserFromToken
from server.pickle_unpickle import load, save

import time
from datetime import datetime, timedelta
import server.pickle_unpickle
def standup_start(token, channel_id, length):
    channel_id = int(channel_id)
    data = load()
    channelDict = data['channelDict']

    opid = getUserFromToken(token)
    for ch in channelDict:
        if int(channel_id) == ch['channel_id']:
            if opid not in ch['channel_member'] and opid not in ch['channel_owner']:
                raise AccessError('You are not a member of this channel')
            if ch['standUp'] == True:
                raise ValueError('this channel is already in standup')
            ch['standUp'] = True
            ch['standtime'] = showtime(length)
            time = ch['standtime']
            data['channelDict'] = channelDict
            save(data)
            
            timer = threading.Timer(int(length),send,[channel_id,token])
            timer.start()
                    
            return {'time_finish': time}
    raise ValueError('incorrect channel id')
  
def standup_active(token, channel_id):
    channel_id = int(channel_id)
    data = load()
    channelDict = data['channelDict']
    for ch in channelDict:
        if int(channel_id) == ch['channel_id']:
            a = ch['standUp']
            b = ch['standtime']
            return {
                'is_active': bool(a),
                'time_finish': (b)
            }
    raise ValueError('incorrect channel id')
            
def send(channel_id,token):
    channel_id = int(channel_id)
    data = load()
    channelDict = data['channelDict']
    for channel in channelDict:
        if int(channel_id) == channel['channel_id']:
            message_send(token, channel_id, str(channel['standlist']))

    data = load()
    channelDict = data['channelDict']
    for channel in channelDict:
        if int(channel_id) == channel['channel_id']:
            channel['standUp'] = False
            channel['standtime'] = None
            channel['standlist'] == ''
            data['channelDict'] = channelDict
            save(data)
            return

def showtime(time):
    now = datetime.now()
    now_15 = now + timedelta(seconds=int(time))
    return int(now_15.timestamp())

def standup_send(token, channel_id, message):
    channel_id = int(channel_id)
    data = load()
    channelDict = data['channelDict']
    userDict = data['userDict']
    
    opid = getUserFromToken(token)
    for user in userDict:
        if int(user['u_id']) == int(opid):
            name = user['first_name']
            break
    if len(message) > 1000 :
        raise ValueError("Message too long")
    for ch in channelDict:
        if int(channel_id) == int(ch['channel_id']):
            if opid not in ch['channel_member'] and opid not in ch['channel_owner']:
                raise AccessError('You are not a member of this channel')
            if ch['standUp'] != True:
                raise ValueError(
                    'An active standup is not currently running in this channel')
            append = str(name) + ': ' + str(message)
            if not ch['standlist']:
                ch['standlist'] = append
                data['channelDict'] = channelDict
                save(data)
                return {}
            else:
                ch['standlist'] += '\r\n' + append
                data['channelDict'] = channelDict
                save(data)
                return {}
    raise ValueError('Channel ID is not a valid channel')
  
    
