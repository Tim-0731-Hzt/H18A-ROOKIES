# MESSAGE

# Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
# ValueError when:
# Channel (based on ID) does not exist
# Message is more than 1000 characters
# Time sent is a time in the past
def message_sendlater(token, channel_id, message, time_sent):
    pass

# Send a message from authorised_user to the channel specified by channel_id
# ValueError when: Message is more than 1000 characters
def message_send(token, channel_id, message):
    pass

# Given a message_id for a message, this message is removed from the channel
# ValueError when
# Message (based on ID) no longer exists
# AccessError when
# Message with message_id edited by authorised user is not the poster of the message
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack
def message_remove(token, message_id):
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



