# Given a message, update it's text with new text
# ValueError when all of the following are not true:
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack

def message_edit(token, message_id, message):
    pass
