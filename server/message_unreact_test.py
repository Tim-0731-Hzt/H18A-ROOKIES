import message_send
import auth_register
import channels_create
import message_react
import message_unreact
import pytest

# Given a message within a channel the authorised user is part of, remove a "react" to that particular message
# ValueError when:
# message_id is not a valid message within a channel that the authorised user has joined
# react_id is not a valid React ID
# Message with ID message_id does not contain an active React with ID react_id
def message_unreact(token, message_id, react_id):

def test_message_unreact_invalidmessid():
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
    message_react(token2, messID, 1):
    # testing
    try:
        message_unreact(token2, -1, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_unreact_invalidreactid():
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
    message_react(token2, messID, 1):
    # testing
    try:
        message_unreact(token2, messID, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_unreact_notreacted():
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
    # testing
    try:
        message_unreact(token2, messID, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")
