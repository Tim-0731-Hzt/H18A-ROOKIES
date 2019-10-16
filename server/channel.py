# channel
from Error import AccessError
import jwt
# global varaibles:

memberDict = [
       {
            'u_id': "z666",
            'name_first':"Tim",
            'name_last': "Hu"
        },
        {
            'u_id': "z888",
            'name_first': "Jack",
            'name_last': "Lu"
        },
        {
            'u_id': "z123",
            'name_first': "Zhang",
            'name_last': "Lu"
        },
]
channelDict = [
    {
        'channel_id': 1,
        'name': "channel_1",
        'channel_member': ["z518"],
        'channel_owner': [3]
    },
    {
        'channel_id': 2,
        'name': "channel_2",
        'channel_member': ["z521"],
        'channel_owner': [1]
    }
]


messDict = []
# Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
def channel_id_check(channel_id):
    global channelDict
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            return True
    return False

def u_id_check(u_id):
    global memberDict
    for parts in memberDict:
        if (parts['u_id'] == u_id):
            return True
    return False

def auth_id_check(token):
    return True
def message_startCheck(start,channel_id):
    messDict = []
    for parts in messDict:
        if (parts['channel_id'  ] == channel_id):
            if start >= len(parts['message']):
                return False
    return True

def auth_register(email, password, name_first, name_last):

    pass

# Invites a user (with user id u_id) to join a channel with ID channel_id. 
# Once invited the user is added to the channel immediately
def channel_invite (token, channel_id, u_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if u_id_check(u_id) == False:
        raise ValueError("u_id does not refer to a valid user")
    if auth_id_check(token) == False:
        raise AccessError("Auth user is not a member of channel")
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            parts['channel_member'].append(u_id)
'''
# Given a Channel with ID channel_id that the authorised user is part of, 
# provide basic details about the channel
def channel_details (token, channel_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if auth_id_check(token) == False:
        raise AccessError("Auth user is not a member of channel")
    detail = {}
    for parts in channelDict:
        if (parts[channel_id] == channel_id):
            detail['name'] = parts['name']
            detail['channel_member'] = parts['channel_member']
            detail['channel_owner'] = parts['channel_owner']
    return detail
    pass
# Given a Channel with ID channel_id that the authorised user is part of, 
# return up to 50 messages between index "start" and "start + 50". 
# Message with index 0 is the most recent message in the channel. 
# This function returns a new index "end" which is the value of "start + 50", 
# or, if this function has returned the least recent messages in the channel, 
# returns -1 in "end" to indicate there are no more messages to load after this return.
def channel_messages (token, channel_id, start):
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if message_startCheck(start,channel_id) == False:
        raise ValueError("start is greater than or equal to the total number of messages in the channel")
    if auth_id_check(token) == False:
        raise AccessError("Auth user is not a member of channel")
        
    pass
# Given a channel ID, the user removed as a member of this channel
def channel_leave(token, channel_id):
    pass
# Given a channel_id of a channel that the authorised user can join, adds them to that channel
def channel_join(token, channel_id):
    pass
# Make user with user id u_id an owner of this channel
def channel_addowner(token, channel_id, u_id):
    pass
# Remove user with user id u_id an owner of this channel
def channel_removeowner(token, channel_id, u_id):
    pass
# Provide a list of all channels (and their associated details) that 
# the authorised user is part of
def channels_list(token):
    pass
# Provide a list of all channels (and their associated details) 
def channels_listall(token):
    pass
# Creates a new channel with that name that is either a public or private channel
def channels_create(token, name, is_public):
    pass
# Send a message from authorised_user to the channel specified
# by channel_id automatically at a specified time in the future
def message_sendlater(token, channel_id, message, time_sent):

    pass
    '''