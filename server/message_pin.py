# Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already pinned
# AccessError when: 
# The authorised user is not a member of the channel that the message is within

def message_pin(token, message_id):
    pass
