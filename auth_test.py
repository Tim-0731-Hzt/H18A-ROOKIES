import message
import channel
import auth
import pytest

from Error import AccessError


##
def test_auth_login_1():
    authLoginDict = auth_login('goodemail@gmail.com', '123456') 
    u_id1 = authLoginDict['u_id']
    token1 = authLoginDict['token1']

    assert u_id1 == '00001'
    assert token1 =='token1'
def test_auth_login_2():
    with pytest.raises(ValueError, match=r".*"):
        auth_login('soundsbad', '123456')

##
def test_auth_logout_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    token1 = authRegisterDict['token']

    auth_logout(token1)

def test_auth_logout_2():
    token2 = 'nonvalid'
    auth_logout(token2)

##
def test_auth_register_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id1 = authRegisterDict['u_id']
    token1 = authRegisterDict['u_id']
    assert u_id1 == "00001"
    assert token1 == "1"

def test_auth_register_2():
    authRegisterDict = auth_register('Jankie@gmail.com', '123456','Jankie','Lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['u_id']
    assert u_id2 == "00002"
    assert token2 == "2"

def test_auth_register_3():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('soundsbad', '123456') #incorrect email

def test_auth_register_4():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('soundsbad', '1234') #incorrect password

##
def test_auth_passwordreset_request_1():
    authLoginDict = auth_login('hayden@gmail.com','123456')
    u_id1 = authLoginDict['u_id']
    assert u_id1 == '00001'
    auth_passwordreset_request('hayden@gmail.com')

def test_auth_passwordreset_request_2():
    authLoginDict = auth_login('jankie@gmail.com','123456')
    u_id2 = authLoginDict2['u_id']
    assert u_id2 == '00002'
    auth_passwordreset_request('jankie@gmail.com')

##
def test_auth_passwordreset_reset_1():
    auth_passwordreset_reset('wawawa','123456')
    
def test_auth_passwordreset_reset_2():   
    with pytest.raises(ValueError, match=r".*"):
        auth_passwordreset_reset('asasas', '123456')
