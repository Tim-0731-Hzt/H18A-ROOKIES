# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user
from server.Error import AccessError
from server.auth_pickle import getUserFromToken
from server.pickle_unpickle import *
import re


def user_profile(token, u_id):
    opid = getUserFromToken(token)
    
    DATA = load()
    userdict = DATA['userDict']
    for user in userdict:
        if user['u_id'] == u_id:
            return {
                'email': user['email'], 
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'handle': user['handle']
            }
    raise ValueError('u_id was incorrect')
    
    
# returned: { email, name_first, name_last, handle_str }

def user_profile_setemail(token, email):
    opid = getUserFromToken(token)
    
    DATA = load()
    userDict = DATA['userDict']
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        pass
    else:
        raise ValueError("Invalid Email")
    
    for user in userDict:
        if user['email'] == email:
            raise ValueError("Email address is already used bt another user.")
    '''if token == uid'''
    for user in userDict:
        if opid == user['u_id']:
            user['email'] = email
            DATA['userDict'] = userDict
            save(DATA)
            return
   
     




def user_profile_sethandle(token,handle_str):
    opid = getUserFromToken(token)
    DATA = load()
    userDict = DATA['userDict']
    if len(handle_str) <= 3 :
        raise ValueError('handle too short')
    if len(handle_str) >= 20:
        raise ValueError('handle too long')
    for user in userDict:
        if user['handle'] == handle_str:
            raise ValueError('handle already used')

    for user in userDict:
        if opid == user['u_id']:
            user['handle'] = handle_str
            DATA['userDict'] = userDict
            save(DATA)
            return
    
    





def user_profile_setname(token, name_first, name_last):
    opid = getUserFromToken(token)
    DATA = load()
    userDict = DATA['userDict']
    if len(name_first) > 50 :
        raise ValueError('First name too long')
    if len(name_last) > 50 :
        raise ValueError('Last name too long')
    if len(name_first) < 1:
        raise ValueError('First name too short')
    if len(name_last) < 1:
        raise ValueError('Last name too short')
    
    for user in userDict:
        if opid == user['u_id']:
            user['first_name'] = name_first
            user['last_name'] = name_last
            DATA['userDict'] = userDict
            save(DATA)
            return
    






'''def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    if img_url != 200:
        raise ValueError('url corrupted')
    size = 400
    if x_end > 400 or y_end >400 or x_start > 400 or y_start > 400:
        raise ValueError('Out of bound')
    if x_end < 0 or y_end < 0 or x_start < 0 or y_start < 0:
        raise ValueError('Out of bound')
    pass'''
