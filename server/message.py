# MESSAGE
import time
from Error import AccessError

# global variable:
messDict = []
messID = 0
reactDict = []
# just for testing
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

# helper function for testing
def clear_backup():
    global messDict
    global messID
    global channelDict
    global reactDict
    messDict = []
    messID = 0
    reactDict = []
    channelDict = [
        {
            'channel_id': 1,
            'name': "channel_1",
            'channel_member': [1, 2, 3, 4, 5],
            'channel_owner': [1]
        },
        {
            'channel_id': 2,
            'name': "channel_2",
            'channel_member': [2],
            'channel_owner': [1]
        }
    ]


# Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
# ValueError when:
# Channel (based on ID) does not exist
# Message is more than 1000 characters
# Time sent is a time in the past
def message_sendlater(token, channel_id, message, time_sent):
    pass

# Send a message from authorised_user to the channel specified by channel_id
# ValueError when: Message is more than 1000 characters
# AccessError when: the authorised user has not joined the channel they are trying to post to
def message_send(token, channel_id, message):
    
    if len(message) > 1000:
        raise ValueError("Message is more than 1000 characters")
    
    for cha in channelDict:
        if cha['channel_id'] == channel_id:
            if token not in cha['channel_member']:
                raise AccessError("The authorised user has not joined the channel they are trying to post to")
    global messID
    global messDict
    messID += 1
    m = {
        'channel_id': int(channel_id),
        'message_id': int(messID),
        'u_id': int(token),   # fix that later
        'message': message,
        'time_created': time.ctime(),
        'is_unread': True,
        'reacts': None,
        'is_pinned': False
    }
    messDict.append(m)
    return messDict

# Given a message_id for a message, this message is removed from the channel
# ValueError when
# Message (based on ID) no longer exists
# AccessError when
# Message with message_id edited by authorised user is not the poster of the message
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_remove(token, message_id):
    global messDict
    found = False
    
    for mess in messDict:
        if mess['message_id'] == int(message_id):
            channelID = int(mess['channel_id'])
            mess['is_unread'] = False
            # messDict.remove(mess)
            found = True
            break
    if not found:
        raise ValueError("Message (based on ID) no longer exists")
    for channel in channelDict:
        if channel['channel_id'] == channelID:
            if token not in channel['channel_owner']:
                raise AccessError('Unauthorised remove')
    messDict.remove(mess)
    pass

# Given a message, update it's text with new text
# ValueError when all of the following are not true:
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_edit(token, message_id, message):
    global messDict
    for mess in messDict:
        if mess['message_id'] == message_id:
            channelID = mess['channel_id']
            mess['is_unread'] = False
            break
    for channel in channelDict:
        if channel['channel_id'] == channelID:
            if token not in channel['channel_owner']:
                raise AccessError('Unauthorised edit')
    mess['message'] = message
    mess['is_unread'] = True

    return mess


# Given a message within a channel the authorised user is part of, add a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id already contains an active React with ID react_id
def message_react(token, message_id, react_id):

    global reactDict
    global messDict
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
            if int(token) not in chan['channel_member']:
                # raise ValueError('message_id:{message_id} is not a valid message within a channel that the authorised user has joined')
                raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')
    m = {'reacts': int(react_id)}
    message.update(m)

    found = False
    for rea in reactDict:
        if rea['react_id'] == react_id:
            if int(token) not in rea['u_ids']:
                rea['u_ids'].append(int(token))
            found = True
            if uID == int(token):
                u = {'is_this_user_reacted': True}
                rea.update(u)
    if not found:
        
        if uID == int(token):
            r = {
                'react_id': react_id, 
                'u_ids': [int(token)], 
                'is_this_user_reacted': True
            }
        else:
            r = {
                'react_id': react_id, 
                'u_ids': [int(token)], 
                'is_this_user_reacted': False
            }
        reactDict.append(r)
    pass

# Given a message within a channel the authorised user is part of, remove a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id does not contain an active React with ID react_id
def message_unreact(token, message_id, react_id):
    pass

# Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already pinned
# AccessError when: 
# The authorised user is not a member of the channel that the message is within
def message_pin(token, message_id):
    pass

# Given a message within a channel, remove it's mark as unpinned
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already unpinned
# AccessError when:
# The authorised user is not a member of the channel that the message is within
def message_unpin(token, message_id):
    pass



