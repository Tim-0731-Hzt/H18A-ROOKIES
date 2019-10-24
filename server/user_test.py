from auth import auth_register
import pytest
from user import user_profile
from user import user_profile_setname
from user import user_profile_sethandle 
from user import user_profile_setemail
from user import user_profiles_uploadphoto



# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user

def user_profile(token, u_id):
    pass
# returned: { email, name_first, name_last, handle_str }

def test_user_profile_functional():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    authRegisterDict2 = auth_register("jeff@gmail.com", "123456789", "jeff", "lu")
    token2 = authRegisterDict2['token']
    UID2 = authRegisterDict['u_id']


    authRegisterDict3 = auth_register("normaluser@gmail.com", "123456789", "normal", "user")
    token3 = authRegisterDict2['token']
    UID3 = authRegisterDict['u_id']

    # testing
    userDict = user_profile(token, UID)
    mail = userDict['email']
    fname = userDict['name_first']
    lname = userDict['name_last']

    assert mail == "haodong@gmail.com"
    assert fname == "haodong"
    assert lname == "lu"

def test_user_profile_invaliduid():
    # set up
    authRegisterDict = auth_register("haodong@gmail.com", "12345", "haodong", "lu")
    token = authRegisterDict['token']
    UID = authRegisterDict['u_id']

    # testing
    with pytest.raises(ValueError, match = r".*"):
        userDict = user_profile(token, -1)

def test1_user_profile_setname():
    user_profile_setname(123,'Daniel', 'Quin')
def test2_user_profile_setname():
    user_profile_setname(123,'Daniel','bgyerfhuqwdcfcfcfcfcfcfcfafffffffffffffffafafaiffffffffffffffffifififififififififififififi')
def test3_user_profile_setname():
    user_profile_setname(123,'fyhuiawseoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyooooooooooso','Quin')

def test1_user_profile_sethandle():
    user_profile_sethandle(123,'sgfdyasgdasygdyuasgdyuasgdugasudguasd')
def test2_user_profile_sethandle():
    user_profile_sethandle(123,'ahsduasd')

def test1_user_profile_setemail():
    user_profile_setemail(123,'goodemail')
def test2_user_profile_setemail():
    user_profile_setemail(123,'bademail')
def test3_user_profile_setemail():
    user_profile_setemail(123,'usedemail')



def test1_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,2,2,2,2)
def test2_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,100,3,3,3,3)
def test3_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,-5,3,877,9237)
def test4_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,600,5,5,5)
def test5_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,3,456,-1,-1)