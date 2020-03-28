from server.channel import channels_create, channel_invite
from server.message_pickle import message_send
from server.auth_pickle import auth_register
from server.pickle_unpickle import restart

from server.search import search
import pytest



def test1():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
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
    channel_id = channels_create(token1, 'test1', True)
    channel_invite(token1, channel_id, UID2)
    channel_invite(token1, channel_id, UID3)
    message_send(token1, channel_id, 'hello')
    message_send(token2, channel_id, 'hi')
    message_send(token3, channel_id, 'numb')
    result = search(token1,'hello')
    assert result['messages'][0]['message'] == 'hello'
    assert result['messages'][0]['message_id'] == 1

def test2():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
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
    channel_id = channels_create(token1, 'test1', True)
    channel_invite(token1, channel_id, UID2)
    channel_invite(token1, channel_id, UID3)
    message_send(token1, channel_id, 'hello')
    message_send(token2, channel_id, 'hi')
    message_send(token3, channel_id, 'numb')
    result = search(token2, 'hi')
    assert result['messages'][0]['message'] == 'hi'



def test3():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
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
    channel_id = channels_create(token1, 'test1', True)
    channel_invite(token1, channel_id, UID2)
    channel_invite(token1, channel_id, UID3)
    message_send(token1, channel_id, 'hello')
    message_send(token2, channel_id, 'hi')
    message_send(token3, channel_id, 'numb')
    result = search(token3, 'numb')
    assert result['messages'][0]['message'] == 'numb'


restart()