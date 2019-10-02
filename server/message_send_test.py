import message_send
import auth_register
import channels_create
import pytest

# Send a message from authorised_user to the channel specified by channel_id
# ValueError when: Message is more than 1000 characters

def test_message_send():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    '''authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']'''

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']

    # testing v1.0
    with pytest.raises(ValueError, match = r"*"):
        message_send(token, channelID, "Hello world" * 300)

    # testing v1.1
    try:
        message_send(token, channelID, "Hello" * 300)
    except ValueError:
        # The exception was raised as expected
        pass
    else:
        # If we get here, then the ValueError was not raised
        # raise an exception so that the test fails
        raise AssertionError("ValueError was not raised")



