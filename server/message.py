# MESSAGE
import time
from Error import AccessError

# global variable:
messDict = []
messID = 0

# just for testing
channelDict = [
    {
        'channel_id': 1,
        'name': "channel_1",
        'channel_member': [1],
        'channel_owner': [3]
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
        'channel_id': channel_id,
        'message_id': messID,
        'u_id': token,   # fix that later
        'message': message,
        'time_created': time.ctime(),
        'is_unread': False,
        'reacts': None,
        'is_pinned': False
    }
    messDict.append(m)
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
    global messDict
    found = False
    
    for mess in messDict:
        if mess['message_id'] == message_id:
            channelID = mess['channel_id']
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
    pass

# Given a message within a channel the authorised user is part of, add a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id already contains an active React with ID react_id
def message_react(token, message_id, react_id):
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



