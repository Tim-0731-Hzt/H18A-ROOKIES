# channel
from Error import AccessError
import jwt
from data import *
from auth import *
import re
# global varaibles:

def channel_handle_check(handle):
    global userDict
    for parts in userDict:
        if (parts['handle'] == handle):
            return True
    return False
# Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
def channel_id_check(channel_id):
    global channelDict
    for parts in channelDict:
        if parts['channel_id'] == int(channel_id):
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
    id = getUserFromToken(token)
    
    # slacker owner or admin
    for parts in userDict:
        if (parts['u_id'] == id and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
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
    id = getUserFromToken(token)
    # if the user is slacker owner or admin
    for parts in userDict:
        if (parts['u_id'] == id and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
    for elements in channelDict:
        if (elements['channel_id'] == channel_id):
            mem = elements['channel_member']
            owner = elements['channel_owner']
            break
    new = []
    new.append(mem)
    new.append(owner)
    for parts in new:
        if (parts == None):
            continue
        else:
            if (id in parts):
                return True
    return False

def channel_property_check(channel_id):
    global channelDict
    for parts in channelDict:
        if (parts['is_public'] == True and parts['channel_id'] == channel_id):
            # public
            return True
    # private
    return False

def channel_admin_check(token):
    global userDict
    id = getUserFromToken(token)
    # if the user is slacker owner or admin
    for parts in userDict:
        if (parts[u_id] == id and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
    return False       
# Invites a user (with user id u_id) to join a channel with ID channel_id. 
# Once invited the user is added to the channel immediately
def channel_invite (token, channel_id, u_id):
    global channelDict
    if channel_id_check(int(channel_id)) == False:
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
    global messDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if auth_id_check(token,channel_id) == False:
        raise AccessError("Auth user is not a member of channnel")
    dic = {'messages':None,
            'start':start,
            'end':None
    }
    L = []
    for parts in messDict:
        if (parts[channel_id] == channel_id):
            L.append(parts['message'])
    L = L[::-1]
    if len(L) <= start:
        raise ValueError("start is greater than or equal to the total number of messages in the channel")

    if (start + 50 >= len(L)):
        for parts in L[start:len(L) - 1]:
            dic['messages'].append(parts)
        dic['end'] = -1
    else:
        for parts in L[start:start + 50]:
            dic['messages'].append(parts)
        dic['end'] = start + 50
    return dic

# Given a channel ID, the user removed as a member of this channel
def channel_leave(token, channel_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    id = getUserFromToken(token)
   
    for parts in channelDict:
        if id in parts['channel_member']:
            parts['channel_member'].remove(parts)
        # check user is a member of channel
        else:
            raise ValueError("user is not a member of channel")

# Given a channel_id of a channel that the authorised user can join, adds them to that channel
def channel_join(token, channel_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    id = getUserFromToken(token)
    # private channel
    if channel_property_check(channel_id) == False:
        if channel_admin_check(token) == False:
            raise AccessError("authorised user is not an admin when channel is private")
        else:
            for parts in channelDict:
                if (parts['channel_id'] == channel_id):
                    parts['channel_owner'].append(id)
    # public channel
    else:
        for parts in channelDict:
            if (parts['channel_id'] == channel_id):
                parts['channel_member'].append(id)
    pass
# Make user with user id u_id an owner of this channel
def channel_addowner(token, channel_id, u_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    # already an owner
    id = getUserFromToken(token)
    for parts in channelDict:
        if parts['channel_id'] == channel_id and id in parts['channel_owner']:
            raise ValueError("user is already an owner in the channel")    
    if if_User_Owner(token,channel_id) == False:
        raise AccessError("the authorised user is not an owner of the slackr, or an owner of this channel")
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            parts['channel_owner'].append(u_id)
# Remove user with user id u_id an owner of this channel
def channel_removeowner(token, channel_id, u_id):
    global channelDict
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if channel_admin_check(token) == False:
        raise AccessError("the authorised user is not an owner of the slackr, or an owner of this channel")
    if if_User_Owner(token,channel_id) == False:
        raise AccessError("user with user id u_id is not an owner of the channel")
    for parts in channelDict:
        if (parts['channel_id'] == channel_id):
            parts['channel_owner'].remove(u_id)
# Provide a list of all channels (and their associated details) that 
# the authorised user is part of
def channels_list(token):
    global channelDict
    L = []
    id = getUserFromToken(token)
    for parts in channelDict:
        if (parts['channel_member'] == None):
            if id in parts['channel_owner']:
                L.append(parts)
        else:
            if (id in parts['channel_member'] or id in parts['channel_owner']):
                L.append(parts)
    return L
# Provide a list of all channels (and their associated details) 
def channels_listall(token):
    global channelDict
    return channelDict
# Creates a new channel with that name that is either a public or private channel
def channels_create(token, name, is_public):
    global channelDict
    if (len(name) > 20):
        raise ValueError("Name is more than 20 characters long")
    id = getUserFromToken(token)
    if channelDict == []:
        d = {
            'channel_id': 1,
            'name': name,
            'channel_member': None,
            'channel_owner':[id],
            'is_public': is_public,
            'standUp':0
        }
        channelDict.append(d)
        return d['channel_id']
    else:
        # if same name
        for parts in channelDict:
            if (parts['name'] == name):
                raise ValueError("this name was already used")
        count = len(channelDict) + 1
        d = {
            'channel_id': count,
            'name': name,
            'channel_member': None,
            'channel_owner':[id],
            'is_public': is_public,
            'standUp':0
        }
        channelDict.append(d)
        return d['channel_id']
