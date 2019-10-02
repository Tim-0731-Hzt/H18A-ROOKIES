import message_send
import auth_register
import channels_create
import message_pin
import channel_leave
import pytest
import message_unpin

# Given a message within a channel, remove it's mark as unpinned
# ValueError when:
# message_id is not a valid message
# The authorised user is not an admin
# Message with ID message_id is already unpinned
# AccessError when:
# The authorised user is not a member of the channel that the message is within

def message_unpin(token, message_id):
    pass

def test_message_unpin_invalidmessid():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messDict = message_send(token, channelID, "Hello")
    messID = messDict['message_id']
    message_pin(token, messID)
    # testing
    try:
        message_unpin(token, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_unpin_unauthoriseduser():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messDict = message_send(token, channelID, "Hello")
    messID = messDict['message_id']
    message_pin(token, messID)
    # testing
    try:
        message_unpin(token3, messID)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_unpin_alreadyunpinned():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messDict = message_send(token, channelID, "Hello")
    messID = messDict['message_id']
    message_pin(token, messID)
    message_unpin(token, messID)
    # testing
    try:
        message_unpin(token, messID)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_unpin_notinchannel():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messDict = message_send(token, channelID, "Hello")
    messID = messDict['message_id']
    message_pin(token, messID)
    channel_leave(token, channelID)
    # testing
    try:
        message_unpin(token, messID)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")
