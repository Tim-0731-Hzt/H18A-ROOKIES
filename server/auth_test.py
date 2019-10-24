##AUTH TEST
import channel
from auth import auth_register
from auth import auth_login
from auth import auth_logout
import auth
import pytest
from Error import AccessError
from pickle_unpickle import restart
from auth import refresh, userDict
from user import user_profile
##
def test_auth_login_1():
    registerDict = auth_register('goodemail@gmail.com', '123456', 'hayden','smith')
    token1 = registerDict['token']
    #token1 = token1[2:len(token1)-1]
    auth_logout(token1)
    loginDict = auth_login('goodemail@gmail.com', '123456') 
    u_id1 = loginDict['u_id']
    login_token1 = loginDict['token']
    #login_token1 = login_token1[2:len(login_token1)-1]
    assert login_token1 == token1
    assert u_id1 == 1
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"
    refresh() 

def test_auth_login_2():
    registerDict1 = auth_register('shenjingbing@gmail.com', '123456', 'taobuguo','sb')
    token1 = registerDict1['token']
    registerDict2 = auth_register('BoA@gmail.com', '123456','BoA','Xv')
    token2 = registerDict2['token']
    auth_logout(token1)
    auth_logout(token2)
    loginDict1 = auth_login('shenjingbing@gmail.com', '123456')
    loginDict2 = auth_login('BoA@gmail.com', '123456')
    u_id1 = loginDict1['u_id']
    u_id2 = loginDict2['u_id']
    login_token1 = loginDict1['token']
    login_token2 = loginDict2['token']

    assert login_token1 == token1 
    assert login_token2 == token2
    assert u_id1 == 2
    assert u_id2 == 3
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"
    assert token2 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoyfQ.ZVPCVZoNzgFB9Am_imX_52K6WO_CZf-o8kpsbpdCJl0'"
    refresh()

def test_auth_login_invalidEmail():
    registerDict = auth_register('zhanggaoping@gmail.com', '123456','gaoping','zhang')
    with pytest.raises(ValueError, match=r".*"):
        auth_login('soundsbad', '123456')
    refresh()

def test_auth_login_passwordIncorrect(): 
    refresh()
    registerDict = auth_register('good@gmail.com', '123456','hayden','smith')
    with pytest.raises(ValueError, match=r".*"):
        auth_login('good@gmail.com', '888888')

def test_auth_login_notBelongToUser():
    registerDict = auth_register('Jankie@gmail.com', '123456','hayden','smith') 
    with pytest.raises(ValueError, match=r".*"):
        auth_login('bad@gmail.com', '123456')  
    refresh()
##
def test_auth_logout_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    token1 = authRegisterDict['token']
   # token1 = token1[2:len(token1)-1]
    assert auth_logout(token1) == True
    refresh()



##
def test_auth_register_1():
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','hongzhou','xuan')
    u_id1 = registerDict['u_id']
    token1 = registerDict['token']
    assert u_id1 == 1
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"
    refresh()

def test_auth_register_emailBeUsed():
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    with pytest.raises(ValueError, match=r".*"):
        auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    refresh()

def test_auth_register_invalidEmail():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('asdadsad', '123456','gaoping','zhang')
    refresh() 

def test_auth_register_invalidPassword():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','gaoping','zhang')
    refresh() 

def test_auth_register_invalidFirstName():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','','zhang')
    refresh()

def test_auth_register_invalidLastName():
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','Lebron','')
    refresh()

def test_auth_register_50_handleTest():
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','zzxxccvvbbnnmmaassddffggh','qqwweerrttyyuuiiooppaassd')
    token = registerDict['token']
    u_id = registerDict['u_id']
    userDict = user_profile(token, u_id)
    assert userDict['handle'] == 'zzxxccvvbbnnmmaassdd'

""" def test_auth_register_2():
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
  """