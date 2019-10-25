# MESSAGE
import time
from auth import getUserFromToken

from Error import AccessError
from pickle_unpickle import *

messID = 0

# just for testing
'''channelDict = [
    {
        'channel_id': 1,
        'name': "channel_1",
        'channel_member': [1, 2, 3, 4, 5],
        'channel_owner': [3]
    },
    {
        'channel_id': 2,
        'name': "channel_2",
        'channel_member': [2],
        'channel_owner': [1]
    }
]'''

# helper function for testing
def clear_backup():
    messDict = []
    messID = 0
    reactDict = []
    channelDict = [
        {
            'channel_id': 1,
            'name': "channel_1",
            'channel_member': [1, 2, 3, 4, 5],
            'channel_owner': [3]
        },
        {
            'channel_id': 2,
            'name': "channel_2",
            'channel_member': [2],
            'channel_owner': [1]
        }
    ]

    DATA = {
        'messDict': messDict,
        'messID': messID,
        'reactDict': eractDict,
        'channelDict': channelDict,
        'userDict': userDict
    }


# Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
# ValueError when:
# Channel (based on ID) does not exist
# Message is more than 1000 characters
# Time sent is a time in the past
def message_sendlater(token, channel_id, message, time_sent):
    DATA = load()
    messDict = DATA['messDict']
    uID = getUserFromToken(token)
    if len(message) > 1000:
        raise ValueError("Message is more than 1000 characters")
    
    for cha in channelDict:
        if cha['channel_id'] == channel_id:
            if uID not in cha['channel_member']:
                raise AccessError("The authorised user has not joined the channel they are trying to post to")
    
    DATA['messID'] += 1
    m = {
        'channel_id': int(channel_id),
        'message_id': DATA['messID'],
        'u_id': int(uID),   # fix that later
        'message': message,
        'time_created': time.ctime(),
        'reacts': None,
        'is_pinned': False
    }
    if time_sent < 0:
        raise ValueError("Time sent is a time in the past")
    time.sleep(time_sent)       # time_sent is in unit seconds
    messDict.append(m)
    DATA['messDict'] = messDict
    save(DATA)
    return m['message_id']


# Send a message from authorised_user to the channel specified by channel_id
# ValueError when: Message is more than 1000 characters
# AccessError when: the authorised user has not joined the channel they are trying to post to
def message_send(token, channel_id, message):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    channelDict = DATA['channelDict']
    if len(message) > 1000:
        raise ValueError("Message is more than 1000 characters")
    
    for cha in channelDict:
        if cha['channel_id'] == channel_id:
            if uID in cha['channel_owner']:
                pass
            elif uID in cha['channel_member']:
                pass
            else:
                raise AccessError("The authorised user has not joined the channel they are trying to post to")
    DATA['messID'] += 1
    m = {
        'channel_id': int(channel_id),
        'message_id': DATA['messID'],
        'u_id': int(uID),   # fix that later
        'message': message,
        'time_created': time.ctime(),
        'reacts': None,
        'is_pinned': False
    }
    messDict.append(m)
    DATA['messDict'] = messDict
    save(DATA)
    return m['message_id']

# Given a message_id for a message, this message is removed from the channel
# ValueError when
# Message (based on ID) no longer exists
# AccessError when
# Message with message_id edited by authorised user is not the poster of the message
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_remove(token, message_id):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    channelDict = DATA['channelDict']
    found = False
    
    for mess in messDict:
        if mess['message_id'] == int(message_id):
            channelID = int(mess['channel_id'])
            # messDict.remove(mess)
            found = True
            break
    if not found:
        raise ValueError("Message (based on ID) no longer exists")
    for channel in channelDict:
        if channel['channel_id'] == channelID:
            if uID not in channel['channel_owner']:
                raise AccessError('Unauthorised remove')
    messDict.remove(mess)
    DATA['messDict'] = messDict
    save(DATA)

    pass

# Given a message, update it's text with new text
# ValueError when all of the following are not true:
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_edit(token, message_id, message):
    uID = getUserFromToken(token)

    DATA = load()
    messDict = DATA['messDict']
    for mess in messDict:
        if mess['message_id'] == message_id:
            channelID = mess['channel_id']
            break
    for channel in channelDict:
        if channel['channel_id'] == channelID:
            if uID not in channel['channel_owner']:
                raise AccessError('Unauthorised edit')
    mess['message'] = message
    DATA['messDict'] = messDict
    save(DATA)

    pass

# Given a message within a channel the authorised user is part of, add a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id already contains an active React with ID react_id
def message_react(token, message_id, react_id):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    reactDict = DATA['reactDict']
    channelDict = DATA['channelDict']

    if react_id < 0:
        raise ValueError('React_id is not a valid React ID')
    for mess in messDict:
        if mess['message_id'] == message_id:
            if mess['reacts'] != react_id and mess['reacts'] != None:
                # raise ValueError('Message with ID message_id already contains an active React with ID {mess['reacts']}')
                raise ValueError('Message with ID message_id already contains an active React with ID')
            channelID = mess['channel_id']
            uID = mess['u_id']
            message = mess
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if int(uID) not in chan['channel_member']:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')
    m = {'reacts': int(react_id)}
    message.update(m)

    found = False
    for rea in reactDict:
        if rea['react_id'] == react_id:
            if int(uID) not in rea['u_ids']:
                rea['u_ids'].append(int(uID))
            found = True
            if uID == int(uID):
                u = {'is_this_user_reacted': True}
                rea.update(u)
    if not found:
        
        if uID == int(uID):
            r = {
                'react_id': react_id, 
                'u_ids': [int(uID)], 
                'is_this_user_reacted': True
            }
        else:
            r = {
                'react_id': react_id, 
                'u_ids': [int(uID)], 
                'is_this_user_reacted': False
            }
        reactDict.append(r)
    DATA['messDict'] = messDict
    DATA['reactDict'] = reactDict
    DATA['channelDict'] = channelDict
    save(DATA)

    pass

# Given a message within a channel the authorised user is part of, remove a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id does not contain an active React with ID react_id
def message_unreact(token, message_id, react_id):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    reactDict = DATA['reactDict']
    channelDict = DATA['channelDict']
    if react_id < 0:
        raise ValueError('React_id is not a valid React ID')
    for mess in messDict:
        if mess['message_id'] == message_id:
            if mess['reacts'] == None:
                # raise ValueError('Message with ID message_id does not contain an active React with ID {mess['reacts']}')
                raise ValueError('Message with ID message_id does not contain an active React with ID')
            if mess['reacts'] != react_id:
                raise ValueError('React_id is not a valid React ID')
            channelID = mess['channel_id']
            uID = mess['u_id']
            message = mess
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if int(uID) not in chan['channel_member']:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')

    for rea in reactDict:
        if rea['react_id'] == react_id:
            rea['u_ids'].remove(int(uID))
            if rea['u_ids'] == []:
                m = {'reacts': None}
                message.update(m)
                reactDict.remove(rea)
            break
    DATA['messDict'] = messDict
    DATA['reactDict'] = reactDict
    DATA['channelDict'] = channelDict
    save(DATA)

    pass

# Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already pinned
# AccessError when: 
# The authorised user is not a member of the channel that the message is within
def message_pin(token, message_id):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    channelDict = DATA['channelDict']

    found = False
    for mess in messDict:
        if mess['message_id'] == message_id:
            if mess['is_pinned']:
                raise ValueError('already pinned')
            channelID = mess['channel_id']
            message = mess
            found = True
            break
    if not found:
        raise ValueError("Invalid message_id")
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if int(uID) not in chan['channel_member']:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise AccessError('message_id is not a valid message within a channel that the authorised user has joined')
            if int(uID) not in chan['channel_owner']:
                raise ValueError('The authorised user is not an admin')
    message['is_pinned'] = True
    DATA['messDict'] = messDict
    DATA['channelDict'] = channelDict
    save(DATA)

    pass

# Given a message within a channel, remove it's mark as unpinned
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already unpinned
# AccessError when:
# The authorised user is not a member of the channel that the message is within
def message_unpin(token, message_id):
    uID = getUserFromToken(token)
    DATA = load()
    messDict = DATA['messDict']
    channelDict = DATA['channelDict']

    found = False
    for mess in messDict:
        if mess['message_id'] == message_id:
            if not mess['is_pinned']:
                raise ValueError('already unpinned')
            channelID = mess['channel_id']
            message = mess
            found = True
            break
    if not found:
        raise ValueError("Invalid message_id")
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if int(uID) not in chan['channel_member']:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise AccessError('message_id is not a valid message within a channel that the authorised user has joined')
            if int(uID) not in chan['channel_owner']:
                raise ValueError('The authorised user is not an admin')
    message['is_pinned'] = False
    DATA['messDict'] = messDict
    DATA['channelDict'] = channelDict
    save(DATA)

    pass



