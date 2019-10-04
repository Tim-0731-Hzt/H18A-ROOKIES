# MESSAGE TEST
from message import *
from channel import *
from auth import *
import pytest
from Error import AccessError

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

def test_message_remove_1():

    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']

    messDict = message_send(token, channelID, "Hello")
    messID = messDict['message_id']
    # testing
    message_remove(token, messID)
    try:
        message_remove(token, messID)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_remove_2():

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
        message_remove(token3, messID)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")

def test_message_edit_1():

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
        message_edit(token3, messID, "I Love 1531")
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_react_messremoved():
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
    message_remove(token, messID)
    # testing
    try:
        message_react(token2, messID, 1):
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_react_nonexist():
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
        message_react(token2, -5, 1):
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_react_invalidreactid():
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
        message_react(token2, messID, -1):
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_react_reacted():
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
    message_react(token2, messID, 2):
    # testing
    try:
        message_react(token3, messID, 3):
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

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

def test_message_pin_invalidmessid():
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
        message_pin(token, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_pin_unauthoriseduser():
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
        message_pin(token3, messID)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_pin_alreadypinned():
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
        message_pin(token, messID)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")

def test_message_pin_notinchannel():
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
    channel_leave(token, channelID)
    # testing
    try:
        message_pin(token, messID)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")

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
