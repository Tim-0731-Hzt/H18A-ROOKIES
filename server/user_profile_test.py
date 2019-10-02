import message_send
import auth_register
import user_profile
import pytest


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
    try:
        userDict = user_profile(token, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("ValueError was not raised")
