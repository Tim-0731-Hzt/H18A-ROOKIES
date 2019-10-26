
##CHANNEL TEST
from channel import *
from auth import *
from message_pickle import *
import pytest
from Error import AccessError
from pickle_unpickle import *

restart()

# first user
authRegisterDict1 = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
token1 = authRegisterDict1["token"]
# second user
authRegisterDict2 = auth_register("HaydenSmith@gmail.com","1we33456","Hayden","Smith")
token2 = authRegisterDict2["token"]
# third user
authRegisterDict3 = auth_register("Luhaodong@gmail.com","1we33ee456","Jeff","Lu")
token3 = authRegisterDict3["token"]

authRegisterDict4 = auth_register("Chenkai@gmail.com","1we33ee456","bbeff","lv")
token4 = authRegisterDict4["token"]

authRegisterDict5 = auth_register("Chdrrrenkai@gmail.com","1we33ee456","bbeceff","ledv")
token5 = authRegisterDict5["token"]
def test_channels_create_1():
        global token1
        with pytest.raises(ValueError,match = r".*"):
                channel_id = channels_create(token1,"meet updscsdcdscdscsdcdsdscscddsc",True)
def test_channel_create_2():
        global token1
        assert(channels_create(token1, "COMP1531", True) == 1)
def test_channel_create_3():
        global token1
        assert(channels_create(token1, "COMP2521", True) == 2)
def test_channel_invite_1():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_invite(token1,4,2)
def test_channel_invite_2():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_invite(token1,1,400)
def test_channel_invite_3():
        global token3
        with pytest.raises(AccessError, match=r".*"):
                channel_invite(token3,1,1)
def test_channel_invite_4():
        global token1
        channel_invite(token1,1,2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[0]['channel_owner'] == [1,2])
def test_channel_invite_5():
        global token3
        global token1
        channel_invite(token1,1,3)
        channel_invite(token3,1,4)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[0]['channel_owner'] == [1,2,3])
        assert (channelDict[0]['channel_member'] == [4])

def test_channel_details_1():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_details(token1,5)
def test_channel_detail_2():
        global token5
        with pytest.raises(AccessError, match=r".*"):
                channel_details(token5,1)
def test_channel_details_2():
        global token1
        detail = {
                'name': 'COMP1531', 
                'channel_member': [4], 
                'channel_owner': [1,2,3]
        }
        assert(channel_details(token1,1) == detail)

def test_channel_join_public():
        global token5
        channel_join(token5, 2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[1]['channel_member'] == [5])    
def test_channel_join_public_2():
        global token2
        channel_join(token2, 2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[1]['channel_member'] == [5,2])    

def test_channel_join_private():
        global token1
        global token2
        assert(channels_create(token1, "COMP1521", False) == 3)
        with pytest.raises(AccessError,match = r".*"):
                channel_join(token2, 3)   
def test_channel_leave_1():
        global token5
        with pytest.raises(ValueError, match=r".*"):
                channel_leave(token5,1)
'''def test_channel_leave_2():
        global token2
        global token1
        global token3
        global token4
        channel_leave(token2,1)
        channel_leave(token1,1)
        channel_leave(token3,1)
        channel_leave(token4,1)'''
def test_channel_messages_1():
        global token1
        for i in range(0,20):
                mess_id = message_send(token1,1,str(i))
        with pytest.raises(ValueError, match=r".*"):
                channel_messages (token1, 1, 23)
def test_channel_messages_2():
        global token1
        for i in range(0,100):
                mess_id = message_send(token1,2,str(i))
        dic = {
                'messages': ['96', '95', '94', '93', '92', '91', '90', '89', '88', 
                '87', '86', '85', '84', '83', '82', '81', '80', '79', '78', '77', '76', '75', 
                '74', '73', '72', '71', '70', '69', '68', '67', '66', '65', '64', '63', '62', 
                '61', '60', '59', '58', '57', '56', '55', 
                '54', '53', '52', '51', '50', '49', '48', '47'], 
                'start': 3, 
                'end': 53
        }
        assert(dic == channel_messages (token1, 2, 3))
def test_channel_message_3():
       global token1
       dic = {
               'messages': ['17', '16', '15', '14', 
               '13', '12', '11', '10', '9',
                '8', '7', '6', '5', '4', '3', '2', '1'], 
                'start': 2, 
                'end': -1
        }
       assert(dic == channel_messages (token1, 1, 2))
def test_channel_addowner_1():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_addowner(token1,1,1)
def test_channel_addowner_2():
        global token2
        with pytest.raises(AccessError, match=r".*"):
                channel_addowner(token2,1,4)
def test_channel_addowner_3():
        global token1
        with pytest.raises(AccessError, match=r".*"):
                channel_addowner(token1,1,5)
def test_channel_adowner_4():
        global token1
        channel_addowner(token1,1,4)
        DATA = load()
        channelDict = DATA['channelDict']
        assert(channelDict[0]['channel_owner'] == [1,2,3,4])
        assert(channelDict[0]['channel_member'] == [])
def test_channel_removeowner_1():
        global token2
        with pytest.raises(AccessError, match=r".*"):
                channel_removeowner(token2,1,4)
def test_channel_removeowner_2():
        global token1
        with pytest.raises(AccessError, match=r".*"):
                channel_removeowner(token1,1,5)
def test_channel_removeowner_3():
        global token1
        channel_removeowner(token1,1,4)
        DATA = load()
        channelDict = DATA['channelDict']
        assert(channelDict[0]['channel_owner'] == [1,2,3])
        assert(channelDict[0]['channel_member'] == [4])
def test_channel_listall():
        global token1
        print(channels_listall(token1))

'''
def test_channel_invite_1():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 4, "z666")

 
 
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


# tests for channel_leave_
def test_channel_leave_not_exist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match = r"*"):
                channel_leave(token,channel_id)

def test_channel_leave():
        authRegisterDict = auth_register("TimHu123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        u_id = authRegisterDict["u_id"]
        channel_id = channels_create(token,"COMP1531",True)
        channel_leave(token,channel_id)
        d = channel_details(token,channel_id)
        all_mem =  d[all_members]
        for parts in all_mem.keys():
                if u_id == parts:
                        assert(False)
        


# tests for channel_join
def test_channel_join_notExist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match="*"):
                channel_join(token, channel_id)
def test_channel_join_private():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",False)
        with pytest.raises(AccessError,match="*"):
                channel_join(token, channel_id)
def test_channel_join():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_join(token,channel_id)
        d = channel_details(token,channel_id)
        all_mem =  d[all_members]
        for parts in all_mem.keys():
                if (u_id == parts):
                        pass
        assert(False)

# test for channel_addowner
def test_channel_addowner_notExist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match = r"*"):
                channel_addowner(token,channel_id,u_id)
def test_channel_addowner_alreadyOwner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():

                if (u_id == parts):
                        assert(False)

def test_channel_addowner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_addowner(token, channel_id, u_id)
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():
                if (u_id == parts):
                        pass
        assert(False)

# test for channel_removeowner
def test_channel_removeowner_ChannelNotExist():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match="*"):
                channel_removeowner(token, channel_id, u_id)
def test_channel_removeowner_UserNotExist():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","Tim","hu")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match="*"):
                channel_removeowner(token, channel_id, u_id)
def test_channel_removeowner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_removeowner(token, channel_id, u_id)
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():
                if (u_id == parts):
                        assert(False)
        pass
def test_channels_list():
        authRegisterDict1 = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token_1 = authRegisterDict1["token"] 
        channel_id_1 = channels_create(token,"meet up",True)
        u_id_1 = authRegisterDict1["u_id"]
        d1 = channels_list(token_1)
        for parts in d1.keys():
                if (parts == u_id_1 or parts == channel_id_1):
                        pass
        assert(False)
        authRegisterDict2 = auth_register("JashankJeremy@gmail.com","dfvfvsfdsf","jashank","jeremey")
        token_2 = authRegisterDict1["token"] 
        channel_id_2 = channels_create(token,"COMP2521",True)
        u_id_2 = authRegisterDict1["u_id"]
        d2 = channels_list(token_1)
        for parts in d2.keys():
                if (parts == u_id_2 or parts == channel_id_2):
                        pass
        assert(False)
        authRegisterDict3 = auth_register("HaydenSmith@gmail.com","Hayden123","Hayden","Smith")
        token_3 = authRegisterDict1["token"] 
        channel_id_3 = channels_create(token,"COMP2521",True)
        u_id_3 = authRegisterDict1["u_id"]
        d3 = channels_list(token_1)
        for parts in d3.keys():
                if (parts == u_id_3 or parts == channel_id_3):
                        pass
        assert(False)
def test_channels_listall():
        authRegisterDict1 = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token_1 = authRegisterDict1["token"] 
        channel_id_1 = channels_create(token,"meet up",True)
        u_id_1 = authRegisterDict1["u_id"]
        d1 = channels_list(token_1)
        for parts in d1.keys():
                if (parts == u_id_1 or parts == channel_id_1):
                        pass
        assert(False)
        authRegisterDict2 = auth_register("JashankJeremy@gmail.com","dfvfvsfdsf","jashank","jeremey")
        token_2 = authRegisterDict1["token"] 
        channel_id_2 = channels_create(token,"COMP2521",True)
        u_id_2 = authRegisterDict1["u_id"]
        d2 = channels_list(token_1)
        for parts in d2.keys():
                if (parts == u_id_2 or parts == channel_id_2):
                        pass
        assert(False)
        authRegisterDict3 = auth_register("HaydenSmith@gmail.com","Hayden123","Hayden","Smith")
        token_3 = authRegisterDict1["token"] 
        channel_id_3 = channels_create(token,"COMP2521",True)
        u_id_3 = authRegisterDict1["u_id"]
        d3 = channels_list(token_1)
        for parts in d3.keys():
                if (parts == u_id_3 or parts == channel_id_3):
                        pass
        assert(False)
def test_channels_create():
        authRegisterDict = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match = r"*"):
                channel_id = channels_create(token,"meet updscsdcdscdscsdcdsdscscddsc",True)
def test_message_sendlater_channelNotExist():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.today()
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1)
def test_message_sendlater_messageTooLong():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.today()
        message = "jomvewiirirjfrijfeijeijeijeijciejiefddcdcdcdcdcdrwrbvasddbcfdsdcmdkcmdkcmdkcmdkcmdcdmcdkcdcmddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssskcmdkcmdkcmkdcmdkcmkdcmkdcmkdmcddcdcdcdcdcd"
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1)
def test_message_snedlater_timeInThePast():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.yesterday()
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1) 
'''