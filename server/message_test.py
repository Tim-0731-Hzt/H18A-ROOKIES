# MESSAGE TEST
from message_pickle import *
from channel import channels_create, channel_join
from auth import auth_register
import pytest
from Error import AccessError
from pickle_unpickle import *

#from data import userDict, messDict

def test_message_send_valerr():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    channelID = channels_create(token, "Channel 1", True)
    # testing ValueError
    with pytest.raises(ValueError, match = r".*"):
        message_send(token, channelID, "Hello world" * 300)

def test_message_send_normal():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    channelID = channels_create(token, "Channel1", True)

    # testing (check if this function works properly)
    message_send(token, channelID, "Hello world")


def test_message_remove_valerr1():

    # set up
    restart()
    authRegisterDict = auth_register("haodong321@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel21", True)

    messID = message_send(token, channelID, "Hello")
    # testing (try to remove a message that has alredy been removed)
    message_remove(token, messID)
    with pytest.raises(ValueError, match = r".*"):
        message_remove(token, messID)

def test_message_remove_valerr2():

    # set up
    restart()
    authRegisterDict = auth_register("hao123dong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff123@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel31", True)

    messID = message_send(token, channelID, "Hello")
    # testing (try to remove a message with message_id -1)
    with pytest.raises(ValueError, match = r".*"):
        message_remove(token, -1)



def test_message_remove_accerr1():

    # set up
    restart()
    authRegisterDict = auth_register("hao431dong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("123jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing (a normal user (unauthorised) try to remove a message which was posted by the owner of the channel)
    with pytest.raises(AccessError, match = r".*"):
        message_remove(token3, messID)


def test_message_remove_accerr2():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser1@gmail.com", "123456789", "normal1", "user")
    token3 = authRegisterDict2['token']

    authRegisterDict4 = auth_register("normaluser2@gmail.com", "123456789", "normal2", "user")
    token4 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)
    channel_join(token4, channelID)

    messDict = message_send(token3, channelID, "Hello")
    messID = messDict['message_id']
    # testing (a normal user try to remove a message with message_id was sent by another member in channel)
    with pytest.raises(AccessError, match = r".*"):
        message_remove(token2, messID)
'''
def test_message_remove_accerr3():

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

    messDict = message_send(token3, channelID, "Hello")
    messID = messDict['message_id']
    # testing (The channel owner try to remove a message which was posted by the a member in channel)
    message_remove(token2, messID)

def test_message_edit_Valerr():

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
    with pytest.raises(ValueError, match = r"*"):
        message_edit(token3, messID, "I Love 1531")

def test_message_edit_accerr1():

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
    # testing (a normal user (unauthorised) try to edit a message which was posted by the owner of the channel)
    with pytest.raises(AccessError, match = r"*"):
        message_edit(token3, messID)

def test_message_edit_accerr2():

    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser1@gmail.com", "123456789", "normal1", "user")
    token3 = authRegisterDict2['token']

    authRegisterDict4 = auth_register("normaluser2@gmail.com", "123456789", "normal2", "user")
    token4 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token, "Channel 1", True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)
    channel_join(token3, channelID)
    channel_join(token4, channelID)

    messDict = message_send(token3, channelID, "Hello")
    messID = messDict['message_id']
    # testing (a normal user try to edit a message with message_id was sent by another member in channel)
    with pytest.raises(AccessError, match = r"*"):
        message_edit(token2, messID)

def test_message_edit_accerr3():

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

    messDict = message_send(token3, channelID, "Hello")
    messID = messDict['message_id']
    # testing (The channel owner try to edit a message which was posted by the a member in channel)
    message_edit(token2, messID)


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
    with pytest.raises(ValueError, match = r"*"):
        message_remove(token, messID)


def test_message_react_Nonexist():
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
    with pytest.raises(ValueError, match = r"*"):
        message_react(token2, -5, 1)

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
    with pytest.raises(ValueError, match = r"*"):
        message_react(token2, messID, -1)

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
    message_react(token2, messID, 2)
    # testing
    with pytest.raises(ValueError, match = r"*"):
        message_react(token3, messID, 3)

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
    message_react(token2, messID, 1)
    # testing
    with pytest.raises(ValueError, match = r"*"):
        message_unreact(token2, -1, 1)

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
    message_react(token2, messID, 1)
    # testing
    with pytest.raises(ValueError, match = r"*"):
        message_unreact(token2, messID, -1)

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
    with pytest.raises(ValueError, match = r"*"):
        message_unreact(token2, messID, 1)

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
    with pytest.raises(ValueError, match = r"*"):
        message_pin(token, -1)

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
    with pytest.raises(ValueError, match = r"*"):
        message_pin(token3, messID)

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
    with pytest.raises(ValueError, match = r"*"):
        message_pin(token, messID)

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
    with pytest.raises(AccessError, match = r"*"):
        message_pin(token, messID)

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
    with pytest.raises(ValueError, match = r"*"):
        message_unpin(token, -1)

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
    with pytest.raises(ValueError, match = r"*"):
        message_unpin(token3, messID)

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
    with pytest.raises(ValueError, match = r"*"):
        message_unpin(token, messID)

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
    with pytest.raises(AccessError, match = r"*"):
        message_unpin(token, messID)'''
