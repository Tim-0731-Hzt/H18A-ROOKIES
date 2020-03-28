import pytest
import re
from server.auth_pickle import auth_register
from server.user import user_profile, user_profile_setname, user_profile_sethandle, user_profile_setmail, users_all, user_profiles_uploadphoto
from server.pickle_unpickle import restart
from server.Error import ValueError, AccessError

restart()

def test_user_profile_functional():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict2['u_id']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    token3 = authRegisterDict3['token']
    UID3 = authRegisterDict3['u_id']

    # testing
    userDict = user_profile(token, UID)
    mail = userDict['email']
    fname = userDict['name_first']
    lname = userDict['name_last']
    hd = userDict['handle_str']
    assert mail == "haodong@gmail.com"
    assert fname == "haodong"
    assert lname == "lu"
    assert hd == "haodonglu"

    user2 = user_profile(token2, UID2)
   
    user3 = user_profile(token3,UID3)
    assert user2['email'] == "jeff@gmail.com"
    assert user2['name_first'] == "jeff"
    assert user2['name_last'] == "lu"
    assert user2['handle_str'] == "jefflu"
    assert user3['email'] == "normaluser@gmail.com"
    assert user3['name_first'] == "normal"
    assert user3['name_last'] == "user"
    assert user3['handle_str'] == "normaluser"
    with pytest.raises(ValueError,match = r".*"):
        user_profile(token, 12345)

def test_user_profile_invaliduid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    # testing
    with pytest.raises(ValueError, match = r".*"):
        user_profile(token, -1)

def test1_user_profile_setname():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']
    user_profile_setname(token,'daniel','quin')
    user = user_profile(token, UID)
    assert 'daniel' == user['name_first']
    assert 'quin' == user['name_last']


def test2_user_profile_setname():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    with pytest.raises(ValueError, match=r".*"):
        user_profile_setname(token, '', 'quin')
    with pytest.raises(ValueError, match=r".*"):
        user_profile_setname(token, 'daniel', '')
    with pytest.raises(ValueError, match=r".*"):
        user_profile_setname(token, 'dhasgbdhbashjdbjhasbdhjasgbdhjasgbhjcxbashjbdhjasvgbdyhuasgdyuagsyxgvuasgvduasgbduasg', 'quin')
    with pytest.raises(ValueError, match=r".*"):
        user_profile_setname(token, 'daniel', 'sgbhdyhugausydghuasjdgbyhujasgdyuagyudgasyugdyuqawgyuegawyhughuagshjdgvbhjasvdjhasv')
    

def test1_user_profile_sethandle_normalCases():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register(
        "jeff@gmail.com", "hi1234566789", "jeffsb", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict2['u_id']

    user_profile_sethandle(token, "jeffisnumb")
    user1 = user_profile(token, UID)

    assert "jeffisnumb" == user1['handle_str']

    user_profile_sethandle(token2,"jeffisdumb")
    user2 = user_profile(token2, UID2)

    assert "jeffisdumb" == user2['handle_str']
   
def test2_user_profile_sethandle_badhandle():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    with pytest.raises(ValueError, match = r".*"):
        user_profile_sethandle(token,"sb")
    with pytest.raises(ValueError, match=r".*"):
        user_profile_sethandle(token, "sbsbsbsbsbsbsbsbsbsbsbssbbsbsbsbsbsbbsbsbsbsbsbsbsbb")


def test3_user_profile_sethandle_usedhandle():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    auth_register("jeff@gmail.com", "hi1234566789", "jeffsb", "lu")

    auth_register("normaluser@gmail.com", "hi1234566789", "normal", "user")
    with pytest.raises(ValueError, match = r".*"):
        user_profile_sethandle(token, "jeffsblu")
    with pytest.raises(ValueError, match=r".*"):
        user_profile_sethandle(token, "normaluser")

def test1_user_profile_setmail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    user_profile_setmail(token,"daniel@gmail.com")
    
def test2_user_profile_setmail_usedEmail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']

    auth_register("jeff@gmail.com", "hi1234566789", "jeff", "lu")

    with pytest.raises(ValueError, match = r".*"):
        user_profile_setmail(token,"jeff@gmail.com")
    
def test3_user_profile_setmail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    authRegisterDict['u_id']

    with pytest.raises(ValueError, match = r".*"):
        user_profile_setmail(token, "sahduyhasdh**(())")

def test_user_all():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "hi123456", "haodong", "lu")
    token = authRegisterDict['token']
    user = users_all(token)
    assert user['users'][0]['u_id'] == 1
    assert user['users'][0]['email'] == "haodong@gmail.com"
    assert user['users'][0]['name_first'] == "haodong"
    assert user['users'][0]['name_last'] == "lu"


restart()
'''
def test1_user_profiles_uploadphoto():
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "hihi1234566", "haodong", "lu")
    token = authRegisterDict['token']
    user_profiles_uploadphoto(token, "https://romanroadlondon.com/wp-content/uploads/2019/03/phil-verney-night-sky-bow-1.jpg", 40, 40, 1000 , 600)

'''