
##CHANNEL#########

##
def channel_invite(token, channel_id, u_id):
    pass

##
def channel_details(token, channel_id):
    pass

##
def channel_messages(token, channel_id, start):
    pass

# Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
def auth_register(email, password, name_first, name_last):
    pass
# Invites a user (with user id u_id) to join a channel with ID channel_id. 
# Once invited the user is added to the channel immediately
def channel_invite (token, channel_id, u_id):
    pass
# Given a Channel with ID channel_id that the authorised user is part of, 
# provide basic details about the channel
def channel_details (token, channel_id):
    pass
# Given a Channel with ID channel_id that the authorised user is part of, 
# return up to 50 messages between index "start" and "start + 50". 
# Message with index 0 is the most recent message in the channel. 
# This function returns a new index "end" which is the value of "start + 50", 
# or, if this function has returned the least recent messages in the channel, 
# returns -1 in "end" to indicate there are no more messages to load after this return.
def channel_messages (token, channel_id, start):
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