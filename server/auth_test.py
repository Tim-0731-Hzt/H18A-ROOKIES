##AUTH TEST
import server.channel
import pytest
from server.auth_pickle import *
from server.Error import AccessError, ValueError
from server.pickle_unpickle import *
#from auth import userDict
from server.user import user_profile

##
restart()
def test_auth_login_1():
    restart()
    registerDict = auth_register('goodemail@gmail.com', '123456789', 'hayden', 'smith')
    token1 = registerDict['token']
    #token1 = token1[2:len(token1)-1]
    auth_logout(token1)
    loginDict = auth_login('goodemail@gmail.com', '123456789') 
    u_id1 = loginDict['u_id']
    login_token1 = loginDict['token']
    #login_token1 = login_token1[2:len(login_token1)-1]
    assert login_token1 == token1
    assert u_id1 == 1
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"

def test_auth_login_2():
    restart()
    registerDict1 = auth_register('shenjingbing@gmail.com', '123456', 'taobuguo','sb')
    token1 = registerDict1['token']
    auth_logout(token1)
    loginDict1 = auth_login('shenjingbing@gmail.com', '123456')
    u_id1 = loginDict1['u_id']
    login_token1 = loginDict1['token']

    #registerDict2 = auth_register('BoABoABoA@gmail.com', '123456789','BoA','Xv')
    #token2 = registerDict2['token']
    #auth_logout(token2)
    #loginDict2 = auth_login('BoABoABoA@gmail.com', '123456789')
    #u_id2 = loginDict2['u_id']
    #login_token2 = loginDict2['token']
 
    assert login_token1 == token1 
    #assert login_token2 == token2
    assert u_id1 == 1
    #assert u_id2 == 2
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"
   # assert token2 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoyfQ.ZVPCVZoNzgFB9Am_imX_52K6WO_CZf-o8kpsbpdCJl0'"
    

def test_auth_login_invalidEmail():
    restart()
    registerDict = auth_register('zhanggaoping@gmail.com', '123456', 'gaoping', 'zhang')
    with pytest.raises(ValueError, match=r".*"):
        auth_login('soundsbad', '123456')

'''def test_auth_login_alreadyLogin():
    restart()
    registerDict = auth_register('good@gmail.com', '123456', 'hayden', 'smith')
    with pytest.raises(ValueError, match=r".*"):
        auth_login('good@gmail.com', '123456')'''

def test_auth_login_passwordIncorrect(): 
    restart()
    registerDict = auth_register('good@gmail.com', '123456', 'hayden', 'smith')
    token = registerDict['token']
    auth_logout(token)
    with pytest.raises(ValueError, match=r".*"):
        auth_login('good@gmail.com', '888888')

def test_auth_login_notBelongToUser():
    restart()
    registerDict = auth_register('Jankie@gmail.com', '123456', 'hayden', 'smith') 
    with pytest.raises(ValueError, match=r".*"):
        auth_login('bad@gmail.com', '123456')  
    
##
def test_auth_logout_ture():
    restart()
    authRegisterDict = auth_register('hayden@gmail.com', '123456', 'hayden', 'smith')
    token = authRegisterDict['token']
   # token1 = token1[2:len(token1)-1]
    assert auth_logout(token) == True

def test_auth_logout_false():
    restart()
    authRegisterDict = auth_register('hayden@gmail.com', '123456', 'hayden', 'smith')
    token = authRegisterDict['token']
    auth_logout(token)
   # token1 = token1[2:len(token1)-1]
    assert auth_logout(token) == False

##
def test_auth_register_1():
    restart()
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','hongzhou','xuan')
    u_id1 = registerDict['u_id']
    token1 = registerDict['token']
    assert u_id1 == 1
    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"

def test_auth_register_2():
    restart()
    registerDict1 = auth_register('shenjingbing@gmail.com', '123456', 'taobuguo','sb')
    token1 = registerDict1['token']
    registerDict2 = auth_register('BoA@gmail.com', '123456','BoA','Xv')
    token2 = registerDict2['token']

    assert token1 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.Bodqy1hnwpsmGtf3MFEhvemrfLLiGQgxuiW4MlbD2WM'"
    assert token2 == "b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoyfQ.ZVPCVZoNzgFB9Am_imX_52K6WO_CZf-o8kpsbpdCJl0'"

def test_auth_register_incorrectFirstName():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('jankie@gmail.com', '123456','qweiousdasdsidjoijoijsaoaisjdoiajdoasijdoaisjdoaisjdia','zhang')

def test_auth_register_incorrectLastName():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('jankie@gmail.com', '123345','what','asdasdasdasdasdfghjkloiuytrewqasdfsdsdaasdasdghjklmnbvx')

def test_auth_register_emailBeUsed():
    restart()
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    with pytest.raises(ValueError, match=r".*"):
        auth_register('jankie@gmail.com', '123456','gaoping','zhang')


def test_auth_register_invalidEmail():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('asdadsad', '123456','gaoping','zhang')


def test_auth_register_invalidPassword():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','gaoping','zhang')
  

def test_auth_register_invalidFirstName():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','','zhang')


def test_auth_register_invalidLastName():
    restart()
    with pytest.raises(ValueError, match=r".*"):
        auth_register('zhanggaoping@gmail.com', '6','Lebron','')


def test_auth_register_50_handleTest():
    restart()
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','zzxxccvvbbnnmmaassddffggh','qqwweerrttyyuuiiooppaassd')
    DATA =load()
    userDict = DATA['userDict']
    assert userDict[0]['handle'] == 'zzxxccvvbbnnmmaassdd'

def test_auth_register_handleCombine():
    restart()
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','hongzhou','xuan')
    DATA =load()
    userDict = DATA['userDict']
    assert userDict[0]['handle'] == 'hongzhouxuan'

def test_auth_handle10plus():
    restart()
    auth_register('xuanhongzhou@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanhongzho@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanhongzh@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanhongz@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanhong@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanhon@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanho@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuanh@gmail.com', '123456','hongzhou','xuan')
    auth_register('xuan@gmail.com', '123456','hongzhou','xuan')
    auth_register('xua@gmail.com', '123456','hongzhou','xuan')
    auth_register('xu@gmail.com', '123456','hongzhou','xuan')
    DATA = load()
    userDict = DATA['userDict']
    assert userDict[10]['handle'] == '010gzhouxuan'

def test_auth_register_handleCombineConflict():
    restart()
    registerDict = auth_register('xuanhongzhou@gmail.com', '123456','hongzhou','xuan')
    registerDict = auth_register('xuanhongzhou123@gmail.com', '123456','hongzhou','xuan')
    DATA =load()
    userDict = DATA['userDict']
    assert userDict[0]['handle'] == 'hongzhouxuan'
    assert userDict[1]['handle'] == '001gzhouxuan'
##
def test_auth_passwordreset_request_1():
    restart()
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    auth_passwordreset_request('jankie@gmail.com')
    DATA = load()
    userDict = DATA['userDict']
    reset_code = userDict[0]['reset_code']
    assert len(str(reset_code)) == 6


##
def test_auth_passwordreset_reset_1():
    restart()
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    auth_passwordreset_request('jankie@gmail.com')
    DATA = load()
    userDict = DATA['userDict']
    reset_code = userDict[0]['reset_code']

    auth_passwordreset_reset(reset_code,'000000')
    DATA = load()
    userDict = DATA['userDict']
    assert userDict[0]['password'] == hashPassword('000000')
    assert userDict[0]['reset_code'] == 0

def test_auth_passwordreset_reset_invalidResetCode():
    restart()
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    auth_passwordreset_request('jankie@gmail.com')

    with pytest.raises(ValueError, match=r".*"):
        auth_passwordreset_reset('123', '123456')

def test_auth_passwordreset_reset_invalidNewPassword():
    restart()
    auth_register('jankie@gmail.com', '123456','gaoping','zhang')
    auth_passwordreset_request('jankie@gmai.com')
    DATA = load()
    userDict = DATA['userDict']
    reset_code = userDict[0]['reset_code']

    with pytest.raises(ValueError, match=r".*"):
        auth_passwordreset_reset(reset_code, '1')

def test_reset_code():
    restart()
    reset_code = generateResetCode()
    assert len(reset_code) == 6

restart()