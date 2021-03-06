# MESSAGE TEST
from server.message_pickle import *
from server.channel import channels_create, channel_join
from server.auth_pickle import auth_register
import pytest
from datetime import datetime, timedelta
from server.Error import AccessError, ValueError
from server.pickle_unpickle import restart
from server.admin_userpermission_change import *

def test_message_sendlater_valerr():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    channelID = channels_create(token, "Channel 1", True)
    # testing ValueError
    with pytest.raises(ValueError, match = r".*"):
        message_sendlater(token, channelID, "Hello world" * 300, 5)

def test_message_sendlater_valerr2():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    channelID = channels_create(token, "Channel 1", True)
    # testing ValueError
    with pytest.raises(ValueError, match = r".*"):
        message_sendlater(token, channelID, "Hello world", -3)

def test_message_sendlater_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']
    authRegisterDict3 = auth_register("comp1531@gmail.com", "hi1234566789", "cse", "lu")
    token3 = authRegisterDict3['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token3, channelID)

    t = datetime.now() + timedelta(seconds = 5)
    t_sent = t.timestamp()
    # testing ValueError
    with pytest.raises(AccessError, match = r".*"):
        message_sendlater(token2, channelID, "Hello world", t_sent)


def test_message_send_valerr():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    channelID = channels_create(token, "Channel 1", True)
    # testing ValueError
    with pytest.raises(ValueError, match = r".*"):
        message_send(token, channelID, "Hello world" * 300)

def test_message_send_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    # testing ValueError
    with pytest.raises(AccessError, match = r".*"):
        message_send(token2, channelID, "Hello world")

def test_message_send_normal():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    channelID = channels_create(token, "Channel1", True)

    # testing (check if this function works properly)
    message_send(token, channelID, "Hello world")


def test_message_remove_valerr1():

    # set up
    restart()
    authRegisterDict = auth_register("haodong321@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
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
    authRegisterDict = auth_register("hao123dong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff123@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel31", True)

    messID = message_send(token, channelID, "Hello")
    # testing (try to remove a message with message_id -1)
    with pytest.raises(ValueError, match = r".*"):
        message_remove(token, -1)

def test_message_remove_accerr1():

    # set up
    restart()
    authRegisterDict = auth_register("hao431dong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("123jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
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
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser1@gmail.com", "hi1234566789", "normal1", "user")
    token3 = authRegisterDict3['token']

    authRegisterDict4 = auth_register("normaluser2@gmail.com", "hi1234566789", "normal2", "user")
    token4 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)
    channel_join(token4, channelID)

    messID = message_send(token2, channelID, "Hello")
    # testing (a normal user try to remove a message with message_id was sent by another member in channel)
    with pytest.raises(AccessError, match = r".*"):
        message_remove(token3, messID)

def test_message_remove_accerr3():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token3, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token2, channelID, "Hello")
    # testing (The channel owner try to remove a message which was posted by the a member in channel)
    message_remove(token3, messID)

def test_message_edit_Valerr():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(AccessError, match = r".*"):
        message_edit(token3, messID, "I Love 1531")

def test_message_edit_accerr1():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing (a normal user (unauthorised) try to edit a message which was posted by the owner of the channel)
    with pytest.raises(AccessError, match = r".*"):
        message_edit(token3, messID, "haha")

def test_message_edit_accerr2():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser1@gmail.com", "hi1234566789", "normal1", "user")
    token3 = authRegisterDict3['token']

    authRegisterDict4 = auth_register("normaluser2@gmail.com", "hi1234566789", "normal2", "user")
    token4 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)
    channel_join(token4, channelID)

    messID = message_send(token3, channelID, "Hello")
    # testing (a normal user try to edit a message with message_id was sent by another member in channel)
    with pytest.raises(AccessError, match = r".*"):
        message_edit(token2, messID, "hahahahah")

def test_message_edit():

    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token3, channelID, "Hello")
    # testing (The channel owner try to edit a message which was posted by the a member in channel)
    message_edit(token, messID, "blahblahblah")

def test_message_react_bymember():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    message_react(token2, messID, 1)

def test_message_react_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)

    messID = message_send(token, channelID, "Hello")
    messID2 = message_send(token, channelID, "Hello")
    message_react(token, messID2, 1)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_react(token2, messID, 1)

def test_message_react_multireacts():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token2, messID, 1)
    message_react(token, messID, 1)


def test_message_react_messremoved():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_remove(token, messID)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_react(token, messID, 1)


def test_message_react_Nonexist():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_react(token2, -5, 1)

def test_message_react_invalidreactid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_react(token2, messID, -1)

def test_message_react_reacted():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token2, messID, 1)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_react(token2, messID, 1)

def test_message_unreact_invalidmessid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token2, messID, 1)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unreact(token2, -1, 1)

def test_message_unreact_invalidreactid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token2, messID, 1)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unreact(token2, messID, -1)

def test_message_unreact_invalidreactid2():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token2, messID, 1)

    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unreact(token, messID, 2)


def test_message_unreact_notreacted():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unreact(token2, messID, 1)

def test_message_unreact_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token, messID, 1)
    message_react(token2, messID, 1)

    message_unreact(token, messID, 1)

    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unreact(token3, messID, 1)

def test_message_unreact_nomore_reacts():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")
    message_react(token, messID, 1)
    message_react(token2, messID, 1)

    message_unreact(token, messID, 1)
    message_unreact(token2, messID, 1)

def test_message_pin_invalidmessid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_pin(token, -1)

def test_message_pin_unauthoriseduser():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_pin(token3, messID)

def test_message_pin_alreadypinned():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_pin(token, messID)

def test_message_pin_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")

    admin_userpermission_change(token, u_id3, 2)

    # testing
    with pytest.raises(AccessError, match = r".*"):
        message_pin(token3, messID)

def test_message_pin():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")

    admin_userpermission_change(token, u_id3, 2)
    message_pin(token3, messID)


def test_message_unpin_invalidmessid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unpin(token, -1)

def test_message_unpin_unauthoriseduser():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unpin(token3, messID)

def test_message_unpin_alreadyunpinned():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict2['token']

    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    message_unpin(token, messID)
    # testing
    with pytest.raises(ValueError, match = r".*"):
        message_unpin(token, messID)

def test_message_unpin_notinchannel():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']
    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    admin_userpermission_change(token, u_id3, 2)

    # testing
    with pytest.raises(AccessError, match = r".*"):
        message_unpin(token3, messID)

def test_message_unpin():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']
    u_id3 = authRegisterDict3['u_id']
    channelID = channels_create(token, "Channel 1", True)
    channel_join(token2, channelID)
    channel_join(token3, channelID)

    messID = message_send(token, channelID, "Hello")
    message_pin(token, messID)
    admin_userpermission_change(token, u_id3, 2)
    message_unpin(token3, messID)


restart()