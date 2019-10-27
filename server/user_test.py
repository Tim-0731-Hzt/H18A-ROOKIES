
import pytest
import re
from auth_pickle import *
from message_pickle import *
from channel import *
from user import *


# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user


    

# returned: { email, name_first, name_last, handle_str }
restart()

def test_user_profile_functional():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict2['u_id']

    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict3['token']
    UID3 = authRegisterDict3['u_id']

    # testing
    userDict = user_profile(token, UID)
    mail = userDict['email']
    fname = userDict['first_name']
    lname = userDict['last_name']
    hd = userDict['handle']
    assert mail == "haodong@gmail.com"
    assert fname == "haodong"
    assert lname == "lu"
    assert hd == "haodonglu"

    user2 = user_profile(token2,UID2)
   
    user3 = user_profile(token3,UID3)
    assert user2['email'] == "jeff@gmail.com"
    assert user2['first_name'] == "jeff"
    assert user2['last_name'] == "lu"
    assert user2['handle'] == "jefflu"
    assert user3['email'] == "normaluser@gmail.com"
    assert user3['first_name'] == "normal"
    assert user3['last_name'] == "user"
    assert user3['handle'] == "normaluser"
    with pytest.raises(ValueError,match = r".*"):
        user_profile(token, 12345)

def test_user_profile_invaliduid():
    # set up
    restart()
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    # testing
    with pytest.raises(ValueError, match = r".*"):
        userDict = user_profile(token, -1)

def test1_user_profile_setname():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']
    user_profile_setname(token,'daniel','quin')
    user = user_profile(token, UID)
    assert 'daniel' == user['first_name']
    assert 'quin' == user['last_name']


def test2_user_profile_setname():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']
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
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register(
        "jeff@gmail.com", "123456789", "jeffsb", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict2['u_id']

    user_profile_sethandle(token, "jeffisnumb")
    user1 = user_profile(token, UID)

    assert "jeffisnumb" == user1['handle']

    user_profile_sethandle(token2,"jeffisdumb")
    user2 = user_profile(token2, UID2)

    assert "jeffisdumb" == user2['handle']
   
def test2_user_profile_sethandle_badhandle():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']
    with pytest.raises(ValueError, match = r".*"):
        user_profile_sethandle(token,"sb")
    with pytest.raises(ValueError, match=r".*"):
        user_profile_sethandle(token, "sbsbsbsbsbsbsbsbsbsbsbssbbsbsbsbsbsbbsbsbsbsbsbsbsbb")


def test3_user_profile_sethandle_usedhandle():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register(
        "jeff@gmail.com", "123456789", "jeffsb", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict['u_id']

    authRegisterDict3 = auth_register(
        "normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']
    UID3 = authRegisterDict['u_id']
    with pytest.raises(ValueError, match = r".*"):
        user_profile_sethandle(token, "jeffsblu")
    with pytest.raises(ValueError, match=r".*"):
        user_profile_sethandle(token, "normaluser")

def test1_user_profile_setemail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']
    user_profile_setemail(token,"daniel@gmail.com")
    
def test2_user_profile_setemail_usedEmail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register(
        "jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict['u_id']

    with pytest.raises(ValueError, match = r".*"):
        user_profile_setemail(token,"jeff@gmail.com")
    
def test3_user_profile_setemail():
    restart()
    authRegisterDict = auth_register(
        "haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    with pytest.raises(ValueError, match = r".*"):
        user_profile_setemail(token, "sahduyhasdh**(())")
    restart()

restart()

'''
def test1_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,2,2,2,2)
def test2_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,100,3,3,3,3)
def test3_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,-5,3,877,9237)
def test4_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,600,5,5,5)
def test5_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,3,456,-1,-1)'''
