import message_send
import auth_register
import channels_create
import message_remove
import pytest

# Given a message_id for a message, this message is removed from the channel
# ValueError when
# Message (based on ID) no longer exists
# AccessError when
# Message with message_id edited by authorised user is not the poster of the message
# Message with message_id was not sent by the authorised user making this request
# Message with message_id was not sent by an owner of this channel
# Message with message_id was not sent by an admin or owner of the slack

def test_message_remove():

    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']