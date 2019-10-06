import message
import channel
import auth
import pytest

from Error import AccessError

##
def test_channel_invite_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']


    with pytest.raises(ValueError, match=r".*"):
        channel_invite(token, 'randonNum', u_id2)

    
def test_channel_invite_2():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']


    with pytest.raises(ValueError, match=r".*"):
        channel_invite(token, channel_id, '00002')

##
def test_channel_details():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict2 = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['token']

    authRegisterDict3 = auth_register('Boa@gmail.com', '123456','Boa','Xv')
    u_id3 = authRegisterDict3['u_id']
    token3 = authRegisterDict3['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']
    #make sure u_id2 is a member of channel
    channel_invite(token, channel_id, u_id2)
    #test1
        #channel doesn't exist
    with pytest.raises(ValueError, match=r".*"):
       channel_details(token2, 222211111)

    #test2
        #Authorised user is not a member
    try:
        channel_details(token3, channel_id)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")

    #test3

    channelDetailsDict = channel_details(token, channel_id)
    ownerMembers = channelDetailsDict['owner_members']
    allMembers = channelDetailsDict['all_members']

    assert re.search('hayden', ownerMembers)
    assert re.search('jankie', allMembers)
    assert re.search('hayden', allMembers)

##
def test_channel_messages():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict['u_id']
    token2 = authRegisterDict['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']
    
    #test1
        #channel doesn't exist
    with pytest.raises(ValueError, match=r".*"):
        channel_messages(token, 'randonNum', 0)
    
    #test2
        #not a member of channel
    try:
        channel_details(token2, channel_id)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")

    #test3
    channelMessagesDict = channel_messages(token, channel_id, 0)
    startNum = channelMessagesDict['start']
    endNum = channelMessagesDict['end']
    assert startNum == 0
    assert endNum == 49

    #test4

    channelMessagesDict = channel_messages(token, channel_id, 100)
    startNum = channelMessagesDict['start']
    endNum = channelMessagesDict['end']
    assert startNum == 100
    assert endNum == -1
