# MESSAGE
from datetime import datetime
from server.auth_pickle import getUserFromToken
import threading
import time
from server.Error import AccessError, ValueError
from server.pickle_unpickle import *

def is_owner(token, channel_id):
    channel_id = int(channel_id)
    DATA = load()
    channelDict = DATA['channelDict']
    userDict = DATA['userDict']
    # get the user id from token
    id = getUserFromToken(token)
    id = int(id)
    
    # slacker owner or admin
    for parts in userDict:
        if (parts['u_id'] == id and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
    # find the channel and serach the owner
    for elements in channelDict:
        if (elements['channel_id'] == channel_id):
            # if (elements['channel_creater'] == id):
            if id in elements['channel_owner']:
                return True
    return False

def is_sender(token, message_id):
    u_id = getUserFromToken(token)
    u_id = int(u_id)
    message_id = int(message_id)
    data = load()
    messDict = data['messDict']
    for m in messDict:
        if m['message_id'] == message_id:
            if m['u_id'] == u_id:
                return True
    return False

# Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
# ValueError when:
# Channel (based on ID) does not exist
# Message is more than 1000 characters
# Time sent is a time in the past
def message_sendlater(token, channel_id, message, time_sent):

    if len(message) > 1000:
        raise ValueError("Message is more than 1000 characters")
    stime = datetime.fromtimestamp(int(time_sent))
    if datetime.now() > stime:
        raise ValueError("Time sent is a time in the past")
    diff = int((stime-datetime.now()).total_seconds())
    time.sleep(diff)
    return message_send(token, channel_id, message)


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
            if uID not in cha['channel_owner'] and uID not in cha['channel_member']:
                raise AccessError("The authorised user has not joined the channel they are trying to post to")
    DATA['messID'] += 1
    m = {
        'channel_id': int(channel_id),
        'message_id': int(DATA['messID']),
        'u_id': int(uID),
        'message': message,
        'time_created': int(datetime.now().timestamp()),
        'reacts': [{
            'react_id': 1,
            'u_ids': [],
            'is_this_user_reacted': False
        }],
        'is_pinned': False
    }

    mID = int(m['message_id'])
    messDict.append(m)
    DATA['messDict'] = messDict
    save(DATA)
    return int(mID)

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
            m = mess
            found = True
            break
    if not found:
        raise ValueError("Message (based on ID) no longer exists")
    if not is_owner(token, channelID) and not is_sender(token, message_id):
        raise AccessError('Unauthorised remove !')
    messDict.remove(m)
    DATA['messDict'] = messDict
    save(DATA)

    return {}

# Given a message, update it's text with new text
# ValueError when all of the following are not true:
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_edit(token, message_id, message):
    uID = getUserFromToken(token)
    uID = int(uID)
    message_id = int(message_id)

    DATA = load()
    messDict = DATA['messDict']
    channelDict = DATA['channelDict']
    for mess in messDict:
        if mess['message_id'] == message_id:
            channelID = mess['channel_id']
            m = mess
            break
    if not is_owner(token, channelID) and not is_sender(token, message_id):
        raise AccessError('Unauthorised edit !')
    if len(message) == 0:
        DATA['messDict'].remove(m)
    else:
        m['message'] = message
    DATA['messDict'] = messDict
    save(DATA)

    return {}

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
    is_mess = False
    for mess in messDict:
        if mess['message_id'] == message_id:
            if mess['reacts'] != react_id and mess['reacts'] != None:
                raise ValueError('Message with ID message_id already contains an active React with ID')
            channelID = mess['channel_id']
            sender_id = mess['u_id']
            message = mess
            is_mess = True
            break
    if not is_mess:
        raise ValueError('invalid message_id')
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if uID in chan['channel_owner']:
                pass
            elif uID in chan['channel_member']:
                pass
            else:
                raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')
    m = {'reacts': int(react_id)}
    message.update(m)

    found = False
    for rea in reactDict:
        if rea['react_id'] == react_id:
            if int(uID) not in rea['u_ids']:
                rea['u_ids'].append(int(uID))
            found = True
            if uID == sender_id:
                u = {'is_this_user_reacted': True}
                rea.update(u)
    if not found:
        
        if uID == sender_id:
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
    is_mess = False
    for mess in messDict:
        if mess['message_id'] == message_id:
            if mess['reacts'] == None:
                raise ValueError('Message with ID message_id does not contain an active React with ID')
            if mess['reacts'] != react_id:
                raise ValueError('React_id is not a valid React ID')
            channelID = mess['channel_id']
            #sender_id = mess['u_id']
            message = mess
            is_mess = True
            break
    if not is_mess:
        raise ValueError('invalid message_id')
    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if uID in chan['channel_owner']:
                pass
            elif uID in chan['channel_member']:
                pass
            else:
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
    userDict = DATA['userDict']

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
    is_admin = False
    for user in userDict:
        if user['u_id'] == uID:
            if user['permission_id'] == 1 or user['permission_id'] == 2:
                is_admin = True
    if not is_admin:
        raise ValueError('The authorised user is not an admin')

    for chan in channelDict:
        if chan['channel_id'] == channelID:
            
            if uID in chan['channel_owner'] or uID in chan['channel_member']:
                pass
            else:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise AccessError('message_id is not a valid message within a channel that the authorised user has joined')
    message['is_pinned'] = True
    DATA['messDict'] = messDict
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
    userDict = DATA['userDict']

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
    is_admin = False
    for user in userDict:
        if user['u_id'] == uID:
            if user['permission_id'] == 1 or user['permission_id'] == 2:
                is_admin = True
    if not is_admin:
        raise ValueError('The authorised user is not an admin')

    for chan in channelDict:
        if chan['channel_id'] == channelID:
            if int(uID) in chan['channel_member']:
                pass
            elif uID in chan['channel_owner']:
                pass
            else:
                raise AccessError('message_id is not a valid message within a channel that the authorised user has joined')
    message['is_pinned'] = False
    DATA['messDict'] = messDict
    DATA['channelDict'] = channelDict
    save(DATA)

    pass



