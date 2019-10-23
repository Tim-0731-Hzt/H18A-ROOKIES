##AUTH TEST
import channel
from auth import auth_register
from auth import auth_login
from auth import auth_logout
import auth
import pytest
from Error import AccessError



##
def test_auth_login_1():
    registerDict = auth_register('goodemail@gmail.com', '123456','hayden','smith')
    token1 = registerDict['token']
    auth_logout(token1)
    loginDict = auth_login('goodemail@gmail.com', '123456') 
    u_id1 = loginDict['u_id']
    login_token1 = loginDict['token']
    assert login_token1 == token1
    assert u_id1 == '1'
    assert token1 =='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxLCJ0aW1lIjoxNTcxODAzMDMxLjc5MDIyMzZ9.gx27PhR1lkjiOD2vorX7m2RERKSGMC4MEfby3ZJfs3U'
 #   assert u_id1 == '2'
 #   assert token2 =='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoyLCJ0aW1lIjoxNTcxODAxODkzLjc1MDU0NDV9.AiWQnbL9k8BV_UWR2m7PrvR8Oj5R914tFcpTpn0-VfA'

def test_auth_login_invalidEmail():
    with pytest.raises(ValueError, match=r".*"):
        auth_login('soundsbad', '123456')

def test_auth_login_passwordIncorrect(): 
    registerDict = auth_register('goodemail@gmail.com', '123456','hayden','smith')
    with pytest.raises(ValueError, match=r".*"):
        auth_login('goodmail@gmail.com', '888888')

def test_auth_login_notBelongToUser():
    registerDict = auth_register('goodemail@gmail.com', '123456','hayden','smith') 
    with pytest.raises(ValueError, match=r".*"):
        auth_login('bad@gmail.com', '123456') 

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
        auth_register('soundsbad', '123456','jankie','lv') #incorrect email

def test_auth_register_4():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('soundsbad', '1234','jankie','lv') #incorrect password

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
