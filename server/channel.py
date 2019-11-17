# channel
from server.Error import AccessError, ValueError
from server.auth_pickle import getUserFromToken
from server.pickle_unpickle import save, load

def is_user_reacted(u_id, message_id):
    u_id = int(u_id)
    message_id = int(message_id)
    data = load()
    messD = data['messDict']
    for mess in messD:
        if mess['message_id'] == message_id:
            return bool(u_id in mess['reacts'][0]['u_ids'])
    return False

# input: list of u_id
# output: list of members dictionary
def get_members(uids):
    DATA = load()
    userDict = DATA['userDict']
    memDict = []
    for uid in uids:
        for user in userDict:
            if int(user['u_id']) == int(uid):
                dic = {
                    'u_id': uid,
                    'name_first': user['first_name'],
                    'name_last': user['last_name'],
                    'profile_img_url': user['profile_img_url']
                }
                memDict.append(dic)
                break

    return memDict

# given a list od=f channel_ids and return channels as a list
def get_channels(channel_ids):
    data = load()
    channelDict = data['channelDict']
    channel = []
    for cid in channel_ids:
        for cha in channelDict:
            if int(cid) == int(cha['channel_id']):
                dic = {
                    'channel_id': int(cid),
                    'name': cha['name']
                }
                channel.append(dic)
                break
    return channel

# given a list of message_ids and return messages as a list
def get_messages(u_id, message_ids):
    data = load()
    messDict = data['messDict']
    mess = []
    for mID in list(message_ids):
        for message in messDict:
            if message['message_id'] == int(mID):
                mom = {
                    'message_id': message['message_id'],
                    'u_id': message['u_id'],
                    'message': message['message'],
                    'time_created': message['time_created'],
                    'reacts': message['reacts'],
                    'is_pinned': message['is_pinned']
                }
                if is_user_reacted(u_id, message['message_id']):
                    mom['reacts'][0]['is_this_user_reacted'] = True
                mess.append(mom)
                break
    return list(mess)

# given a user's u_id and check if this user is in this channel
def is_in_channel(u_id, channel_id):
    u_id = int(u_id)
    channel_id = int(channel_id)
    data = load()
    channelDict = data['channelDict']
    for cha in channelDict:
        if cha['channel_id'] == channel_id:
            if int(u_id) in cha['channel_member'] or int(u_id) in cha['channel_owner']:
                return True
            else:
                return False
    return False

# Given a user's first and last name, email address, and password,
# create a new account for them and return a new token for authentication in their session
def channel_id_check(channel_id):
    DATA = load()
    channelDict = DATA['channelDict']
    for parts in channelDict:
        if parts['channel_id'] == int(channel_id):
            return True
    return False

# checking u_id if exist
def u_id_check(u_id):
    DATA = load()
    userDict = DATA['userDict']
    for parts in userDict:
        if int(parts['u_id']) == int(u_id):
            return True
    return False

# given a token and return if this user is a slackr admin(i.e. with permission_id 1 or 2)
def if_slackr_owner(token):
    DATA = load()
    userDict = DATA['userDict']
    # get the user id from token
    id = getUserFromToken(token)
    id = int(id)
    # slacker owner or admin
    for parts in userDict:
        if (parts['u_id'] == id and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
    return False

# check if user a owner or member
def if_User_Owner(token, channel_id):
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
        if elements['channel_id'] == channel_id:
            if id in elements['channel_owner']:
                return True
    return False

# checking if given user is in channel or is slackr owner
def auth_id_check(token, channel_id):
    DATA = load()
    channelDict = DATA['channelDict']
    userDict = DATA['userDict']
    # find the channel's member and owner
    uid = getUserFromToken(token)
    # if the user is slacker owner or admin
    for parts in userDict:
        if (int(parts['u_id']) == int(uid) and (int(parts['permission_id']) == 1 or int(parts['permission_id']) == 2)):
            return True
    for elements in channelDict:
        if int(elements['channel_id']) == int(channel_id):
            return bool(int(uid) in elements['channel_member'] or int(uid) in elements['channel_owner'])
    return False

# checking if the given channel is public
def channel_property_check(channel_id):
    DATA = load()
    channelDict = DATA['channelDict']
    for parts in channelDict:
        if (bool(parts['is_public']) and int(parts['channel_id']) == int(channel_id)):
            # public
            return True
    # private
    return False

# checking if given user is slackr owner(i.e. with permission_id 1 or 2)
def channel_admin_check(token):
    DATA = load()
    userDict = DATA['userDict']
    id = getUserFromToken(token)
    # if the user is slacker owner or admin
    for parts in userDict:
        if (parts['u_id'] == int(id) and (parts['permission_id'] == 1 or parts['permission_id'] == 2)):
            return True
    return False
# Invites a user (with user id u_id) to join a channel with ID channel_id.
# Once invited the user is added to the channel immediately
def channel_invite(token, channel_id, u_id):
    if channel_id_check(int(channel_id)) == False:
        raise ValueError("channel_id is invalid")
    if u_id_check(u_id) == False:
        raise ValueError("u_id does not refer to a valid user")
    if auth_id_check(token, channel_id) == False:
        raise AccessError("Auth user is not a member of channel")
    if is_in_channel(u_id, channel_id):
        raise AccessError('The user you are inviting is already in this channel.')
    DATA = load()
    channelDict = DATA['channelDict']
    for parts in channelDict:
        if int(parts['channel_id']) == int(channel_id):
            # the user invite by owner is also a owner
            if if_slackr_owner(token) == True:
                parts['channel_owner'].append(int(u_id))
            else:
                parts['channel_member'].append(int(u_id))
    DATA['channelDict'] = channelDict
    save(DATA)
    return {}

# Given a Channel with ID channel_id that the authorised user is part of,
# provide basic details about the channel
def channel_details(token, channel_id):
    DATA = load()
    channelDict = DATA['channelDict']
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if not auth_id_check(token, channel_id):
        raise AccessError("Auth user is not a member of channel")
    detail = {}
    for parts in channelDict:
        if int(parts['channel_id']) == int(channel_id):
            all_members = list(parts['channel_member']) + list(parts['channel_owner'])
            detail['name'] = parts['name']
            detail['all_members'] = list(get_members(all_members))
            detail['owner_members'] = list(get_members(list(parts['channel_owner'])))
    return dict(detail)

# Given a Channel with ID channel_id that the authorised user is part of,
# return up to 50 messages between index "start" and "start + 50".
# Message with index 0 is the most recent message in the channel.
# This function returns a new index "end" which is the value of "start + 50",
# or, if this function has returned the least recent messages in the channel,
# returns -1 in "end" to indicate there are no more messages to load after this return.
def channels_messages(token, channel_id, start):
    u_id = getUserFromToken(token)
    u_id = int(u_id)
    DATA = load()
    messDict = DATA['messDict']
    start = int(start)
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if auth_id_check(token, channel_id) == False:
        raise AccessError("Auth user is not a member of channnel")
    dic = {
        'messages': [],
        'start': start,
        'end': None
    }
    L = []
    for parts in messDict:
        if int(parts['channel_id']) == int(channel_id):
            L.append(int(parts['message_id']))
    if len(L) != 1:
        L = L[::-1]
    L = get_messages(u_id, L)
    if len(L) < int(start):
        raise ValueError("start is greater than the total number of messages in the channel")

    if int(start) + 50 >= len(L):
        for parts in L[int(start):len(L)]:
        # for parts in L[int(start):len(L) - 1]:
            dic['messages'].append(parts)
        dic['end'] = -1
    else:
        for parts in L[int(start):int(start) + 50]:
            dic['messages'].append(parts)
        dic['end'] = start + 50
    return dic

# Given a channel ID, the user removed as a member of this channel
def channel_leave(token, channel_id):
    id = getUserFromToken(token)
    id = int(id)
    channel_id = int(channel_id)
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if not is_in_channel(id, channel_id):
        raise ValueError("user is not a member of channel")
    DATA = load()
    channelDict = DATA['channelDict']
    for cha in channelDict:
        if cha['channel_id'] == channel_id:
            if id in cha['channel_owner']:
                cha['channel_owner'].remove(id)
            else:
                cha['channel_member'].remove(id)
    DATA['channelDict'] = channelDict
    save(DATA)

# Given a channel_id of a channel that the authorised user can join, adds them to that channel
def channel_join(token, channel_id):
    DATA = load()
    channelDict = DATA['channelDict']
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    id = getUserFromToken(token)
    id = int(id)
    # private channel
    if channel_property_check(channel_id) == False:
        if channel_admin_check(token) == False:
            raise AccessError("authorised user is not an admin when channel is private")
        else:
            for parts in channelDict:
                if parts['channel_id'] == int(channel_id):
                    parts['channel_owner'].append(id)
    # public channel
    else:
        for parts in channelDict:
            if parts['channel_id'] == int(channel_id):
                if channel_admin_check(token) == False:
                    if parts['channel_member'] == []:
                        parts['channel_member'] = [id]
                    else:
                        parts['channel_member'].append(id)
                else:
                    parts['channel_owner'].append(id)  
    DATA['channelDict'] = channelDict
    save(DATA)

# Make user with user id u_id an owner of this channel
def channel_addowner(token, channel_id, u_id):
    DATA = load()
    channelDict = DATA['channelDict']
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    # already an owner
    id = getUserFromToken(token)
    id = int(id)
    u_id = int(u_id)
    channel_id = int(channel_id)
    for parts in channelDict:
        if parts['channel_id'] == channel_id and u_id in parts['channel_owner']:
            raise ValueError("user is already an owner in the channel")    
    if not if_User_Owner(token, channel_id):
        raise AccessError("the authorised user is not an owner of the slackr, or an owner of this channel")
    if u_id not in channelDict[channel_id - 1]['channel_member']:
        raise AccessError("the user is not a member of this channel")
    for parts in channelDict:
        if parts['channel_id'] == channel_id:
            parts['channel_owner'].append(u_id)
            parts['channel_member'].remove(u_id)
    DATA['channelDict'] = channelDict
    save(DATA)
    return {}

# Remove user with user id u_id an owner of this channel
def channel_removeowner(token, channel_id, u_id):
    id = getUserFromToken(token)
    id = int(id)
    u_id = int(u_id)
    channel_id = int(channel_id)
    DATA = load()
    channelDict = DATA['channelDict']
    if channel_id_check(channel_id) == False:
        raise ValueError("channel_id is invalid")
    if if_User_Owner(token, channel_id) == False: 
        raise AccessError("the authorised user is not an owner of the slackr, or an owner of this channel")
    if u_id not in channelDict[channel_id - 1]['channel_owner']:
        raise AccessError("user with user id u_id is not an owner of the channel")
    for parts in channelDict:
        if parts['channel_id'] == channel_id:
            parts['channel_owner'].remove(u_id)
            parts['channel_member'].append(u_id)
    DATA['channelDict'] = channelDict
    save(DATA)
    return {}

# Provide a list of all channels (and their associated details) that 
# the authorised user is part of
def channels_list(token):
    DATA = load()
    channelDict = DATA['channelDict']
    lis = []
    uid = getUserFromToken(token)
    for parts in channelDict:
        if (uid in parts['channel_member'] or uid in parts['channel_owner']):
            lis.append(parts['channel_id'])
    lis = get_channels(lis)
    return {'channels': lis}

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    DATA = load()
    channelDict = DATA['channelDict']
    getUserFromToken(token)
    channel = []
    for cha in channelDict:
        dic = {
            'channel_id': int(cha['channel_id']),
            'name': cha['name']
        }
        channel.append(dic)
    return {'channels': channel}

# Creates a new channel with that name that is either a public or private channel
def channels_create(token, name, is_public):
    DATA = load()
    channelDict = DATA['channelDict']
    if len(name) > 20:
        raise ValueError("Name is more than 20 characters long")
    id = getUserFromToken(token)
    if channelDict == []:
        dic = {
            'channel_id': 1,
            'name': name,
            'channel_creater': int(id),
            'channel_member': [],
            'channel_owner':[int(id)],
            'is_public': is_public,
            'standUp': False,
            'standlist' : '',
            'standtime': None
        }
        channelDict.append(dic)
        DATA['channelDict'] = channelDict
        save(DATA)
        return dic['channel_id']
    else:
        # if same name
        for parts in channelDict:
            if parts['name'] == name:
                raise ValueError("this name was already used")
        count = len(channelDict) + 1
        dic = {
            'channel_id': int(count),
            'name': name,
            'channel_creater': int(id),
            'channel_member': [],
            'channel_owner':[int(id)],
            'is_public': is_public,
            'standUp': False,
            'standlist' : '',
            'standtime' : None
        }
        channelDict.append(dic)
        DATA['channelDict'] = channelDict
        save(DATA)
        return int(dic['channel_id'])
