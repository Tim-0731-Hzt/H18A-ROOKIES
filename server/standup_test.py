from Error import AccessError
from channel import *
from message_pickle import *
from auth_pickle import *
import pickle_unpickle
from standup import *
import pytest

def test_standup_all():
    restart()
    authRegisterDict1 = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register("HaydenSmith@gmail.com","1we33456","Hayden","Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]
    
    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]
    
    UID4 = authRegisterDict4['u_id']
    channel_id = channels_create(token1,'test1',True)
    channel_invite(token1,channel_id,UID2)
    channel_invite(token1,channel_id,UID3)

    with pytest.raises(ValueError, match=r".*"):
        standup_send(token2, channel_id, 'hello')

    standup_start(token1,channel_id)
    
    with pytest.raises(ValueError, match = r".*"):
        standup_start(token2, channel_id)

    with pytest.raises(AccessError, match=r".*"):
        standup_start(token4,channel_id)
        
    with pytest.raises(ValueError,match = r".*"):
        standup_start(token1,-1)

    with pytest.raises(AccessError, match=r".*"):
        standup_send(token4, channel_id , 'hello')

    with pytest.raises(ValueError, match=r".*"):
        standup_send(token1, -1 , 'hello')

    with pytest.raises(ValueError, match=r".*"):
        standup_send(token3, channel_id, "dhbfuyawgefdahdhbfuyawgefdahsgfhiashfuihasfnrweiauehcyaacweynugirnnnnnnnnnnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnfnnnnnnnnnnnnnnnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfaecntyvufyyyyyyyyyyyyyyyfyfyfygyyywyyyyyyyyyyyyyyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywydhbfuyawgefdahsgfhiashfuihasfnrweiauehcyaacweynugirnnnnnnnnnnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnfnnnnnnnnnnnnnnnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfaecntyvufyyyyyyyyyyyyyyyfyfyfygyyywyyyyyyyyyyyyyyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywydhbfuyawgefdahsgfhiashfuihasfnrweiauehcyaacweynugirnnnnnnnnnnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnfnnnnnnnnnnnnnnnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfaecntyvufyyyyyyyyyyyyyyyfyfyfygyyywyyyyyyyyyyyyyyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywyysgfhiashfuihasfnrweiauehcyaacweynugirnnnnnnnnnnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnrnfnnnnnnnnnnnnnnnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfnfaecntyvufyyyyyyyyyyyyyyyfyfyfygyyywyyyyyyyyyyyyyyywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywywyy")

    standup_send(token2,channel_id, 'hello')
    standup_send(token3,channel_id,'daniel')
    standup_send(token2,channel_id, 'quin' )
    channelDict = load()['channelDict']
    for ch in channelDict:
        if channel_id == ch['channel_id']:
            assert 'hello: daniel :quin' == ch['standlist']
    pass