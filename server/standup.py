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
            t_end = time.time() + 60*15
            while time.time() < t_end:


            '''time out'''
            ch['standup'] == 0
            standlist = load().['standList']
            message_send(token, channel_id, standlist)
            return
    raise ValueError('incorrect channel id')
            

def showtime():
    now = datetime.now()
    now_15 = now + timedelta(minutes=15)
    return now_15

def standup_send(token, channel_id, message):
    data = load()
    channelDict = data['channelDict']
    standlist = data['standlist']
    if len(message) > 1000 :
        raise ValueError("Message too long")
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            if opid not in ch['channelmember'] and opid not in ch['channelowner']:
                raise AccessError('You are not a member of this channel')
            if ch['standup'] != 1:
                raise ValueError(
                    'An active standup is not currently running in this channel')
            if standlist == "":
                standlist = message
                save(standlist)
                return
            else: standlist = standlist + ": " + message
                save(standlist)
                return
    raise ValueError('Channel ID is not a valid channel')

    
