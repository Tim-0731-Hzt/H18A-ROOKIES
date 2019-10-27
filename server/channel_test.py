
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

authRegisterDict6 = auth_register("denilqian@gmail.com","1we33ee456","bbeceff","ledv")
token6 = authRegisterDict6["token"]

authRegisterDict7 = auth_register("denilqia32222n@gmail.com","1we33ee456","bbec22eff","ledv")
token7 = authRegisterDict7["token"]
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
def test_channels_create_4():
        global token1
        with pytest.raises(ValueError,match = r".*"):
                channels_create(token1, "COMP2521", True)
        
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
def test_channel_join_1():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_join(token5, 13)
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

def test_channel_join_private1():
        global token1
        global token2
        global token7
        assert(channels_create(token1, "COMP1521", False) == 3)
        assert(channels_create(token7, "COMP2121", False) == 4)
        with pytest.raises(AccessError,match = r".*"):
                channel_join(token2, 3)   
def test_channel_join_private2():
        global token1
        channel_join(token1, 4)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[3]['channel_owner'] == [7,1])    
def test_channel_leave_1():
        global token5
        with pytest.raises(ValueError, match=r".*"):
                channel_leave(token5,1)
def test_channel_leave_2():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_leave(token5,10)
def test_channel_message_invalidchannel():
        global token1
        with pytest.raises(ValueError, match=r".*"):
                channel_messages (token1, 50, 23)
def test_channel_message():       
        global token7
        with pytest.raises(AccessError, match=r".*"):
                channel_messages (token7, 1, 23)
def test_channel_message_noMessage():
        global token1
        with pytest.raises(AccessError, match=r".*"):
                channel_messages (token1, 1, 23)
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
def test_channel_addowner_5():
        global token2
        with pytest.raises(ValueError, match=r".*"):
                channel_addowner(token2,26,2)
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
def test_channel_removeowner_4():
        global token2
        with pytest.raises(ValueError, match=r".*"):
                channel_removeowner(token2,6,2)
def test_channels_list_1():
        global token2
        l = [
                {
                'channel_id': 1, 'name': 'COMP1531', 
                'channel_creater': 1, 
                'channel_member': [4], 
                'channel_owner': [1, 2, 3], 
                'is_public': True, 'standUp': 0,'standlist': ''
                }, 
                {'channel_id': 2, 'name': 'COMP2521', 
                'channel_creater': 1, 
                'channel_member': [5, 2], 'channel_owner': [1], 
                'is_public': True, 'standUp': 0, 'standlist': ''
                }
        ]
        assert(channels_list(token2) == l)
def test_channels_list_2():
        global token1
        l = [
                {
                'channel_id': 1, 'name': 'COMP1531', 'channel_creater': 1, 
                'channel_member': [4], 'channel_owner': [1, 2, 3], 
                'is_public': True, 'standUp': 0,'standlist': ''
                }, 
                {
                'channel_id': 2, 'name': 'COMP2521', 'channel_creater': 1, 
                'channel_member': [5, 2], 'channel_owner': [1], 'is_public': True, 
                'standUp': 0,'standlist': ''
                }, 
                {'channel_id': 3, 'name': 'COMP1521', 
                'channel_creater': 1, 'channel_member': [], 
                'channel_owner': [1], 'is_public': False, 'standUp': 0,'standlist': ''
                },
                {
                'channel_id': 4, 'name': 'COMP2121', 
                'channel_creater': 7, 'channel_member': [], 
                'channel_owner': [7,1], 'is_public': False, 'standUp': 0,'standlist': ''
                }
        ]
        assert(channels_list(token1) == l)
def test_channels_list_3():
        global token6
        with pytest.raises(AccessError, match=r".*"):
                channels_list(token6)
def test_channel_listall():
        global token1
        l = [
                {
                'channel_id': 1, 'name': 'COMP1531', 'channel_creater': 1, 
                'channel_member': [4], 'channel_owner': [1, 2, 3], 
                'is_public': True, 'standUp': 0,'standlist': ''
                }, 
                {
                'channel_id': 2, 'name': 'COMP2521', 'channel_creater': 1, 
                'channel_member': [5, 2], 'channel_owner': [1], 'is_public': True, 
                'standUp': 0,'standlist' : ''
                }, 
                {'channel_id': 3, 'name': 'COMP1521', 
                'channel_creater': 1, 'channel_member': [], 
                'channel_owner': [1], 'is_public': False, 'standUp': 0,'standlist' : ''
                },
                {
                'channel_id': 4, 'name': 'COMP2121', 
                'channel_creater': 7, 'channel_member': [], 
                'channel_owner': [7,1], 'is_public': False, 'standUp': 0,'standlist' : ''
                }
        ]
        assert(channels_listall(token1) == l)

def test_channel_leave_3():
        global token1
        channel_leave(token1,1)
        DATA = load()
        channelDict = DATA['channelDict']
        assert(channelDict[0]['channel_owner'] == [2,3])
def test_channel_leave_4():
        global token4
        channel_leave(token4,1)
        DATA = load()
        channelDict = DATA['channelDict']
        assert(channelDict[0]['channel_member'] == [])
def test_channel_leave_5():
        global token1
        channel_leave(token1,3)
        global token2
        with pytest.raises(ValueError, match=r".*"):
                channel_leave(token2,3)
def test_channel_leave_6():
        global token1
        global token5
        channel_leave(token1,2)
        channel_leave(token5,2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert(channelDict[1]['channel_member'] == [2])
        assert(channelDict[1]['channel_owner'] == [])
def test_channel_join_public_3():
        global token1
        channel_join(token1, 2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[1]['channel_owner'] == [1])    

def test_invite():
        global token7
        channel_invite(token7,4,2)
        DATA = load()
        channelDict = DATA['channelDict']
        assert (channelDict[3]['channel_owner'] == [7,1,2])