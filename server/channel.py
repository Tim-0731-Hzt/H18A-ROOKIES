# channel
from Error import AccessError
import jwt
from data import *
# global varaibles:

SECRET = 'sempai'


# Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
def channel_id_check(channel_id):
    global channelDict
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            return True
    return False

def u_id_check(u_id):
    global userDict
    for parts in userDict:
        if (parts['u_id'] == u_id):
            return True
    return False

# check if user a owner or member
def if_User_Owner(token,channel_id):
    global userDict
    global channelDict
    # get the user id from token
    for parts in userDict:
        if (parts['token'] == token):
            id = parts['u_id']
            break
    # find the channel and serach the owner
    for elements in channelDict:
        if (elements['channel_id'] == channel_id):
            for owners in elements['channel_owner']:
                if owners == id:
                    return True
    return False

def auth_id_check(token,channel_id):
    global userDict
    global channelDict
    # find the channel's member and owner
    for elements in channelDict:
        if (elements['channel_id'] == channel_id):
            mem = elements['channel_member']
            owner = elements['channel_owner']
            break
    new = mem + owner
    for parts in userDict:
        if (parts['token'] == token):
            for users in new:
                if (users == parts['u_id']):
                    return True
    return False
def message_startCheck(start,channel_id):
    messDict = []
    for parts in messDict:
        if (parts['channel_id'] == channel_id):
            if start >= len(parts['message']):
                return False
    return True

# Invites a user (with user id u_id) to join a channel with ID channel_id. 
# Once invited the user is added to the channel immediately
def channel_invite (token, channel_id, u_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if u_id_check(u_id) == False:
        raise ValueError("u_id does not refer to a valid user")
    if auth_id_check(token,channel_id) == False:
        raise AccessError("Auth user is not a member of channel")
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            # the user invite by owner is also a owner
            if if_User_Owner(token,channel_id) == True:
                parts['channel_owner'].append(u_id)
            else:
                parts['channel_member'].append(u_id)

# Given a Channel with ID channel_id that the authorised user is part of, 
# provide basic details about the channel
def channel_details (token, channel_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if auth_id_check(token,channel_id) == False:
        raise AccessError("Auth user is not a member of channel")
    detail = {}
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            detail['name'] = parts['name']
            detail['channel_member'] = parts['channel_member']
            detail['channel_owner'] = parts['channel_owner']
    return detail

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
    if auth_id_check(token,channel_id) == False:
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
