import pytest
from channel import *
from message import *
from Error import AccessError

# invalid channel_id
def test_channel_invite_1():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 4, "z666")
# invalid user_id
def test_channel_invite_2():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 1,"z777")
# not authered user
def test_channel_invite_3():
        with pytest.raises(AccessError, match=r".*"):
                channel_invite("WDEWDWD", 1,"z666")

def test_channel_invite_4():
        global channelDict
        channel_invite("qwert", 1, "z666")
        assert (channelDict[0]['channel_member'] == ["z888","z666"])
      
        channel_invite("WDEWDWrtyyy", 1, "z123")
        assert (channelDict[0]['channel_owner'] == ["zdedx11","z123"])

def test_channel_details():
        global channelDict
        dic_1 = { 'name': "channel_2",
        'channel_member': ["z666"],
        'channel_owner': [1]}
        assert(channel_details("asdf",2) == dic_1)
        '''
        dic_2 = {'name': "channel_1",
        'channel_member': ["z518","z666","z123"],
        'channel_owner': [3]}
        assert(channel_details("23dc3ef*dcdc",1) == dic_2)'''
