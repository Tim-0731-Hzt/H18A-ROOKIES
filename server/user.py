# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user
from Error import AccessError
from auth import *
import pickle_unpickle
userDict = [
    {
        'first_name' : 1
        'last_name' : 1
        'email' : 1 
        'u_id' : 1
        'handle' : 1
        'password' : 1
        'token' : 1
        'online' : True
        
    } ,
    {
        'first_name' : 2
        'last_name' : 2
        'email' : 2
        'u_id' : 2
        'handle' : 2
    },
    {
        'first_name' : 3
        'last_name' : 3
        'email' : 3
        'u_id' : 3
        'handle' : 3
    }
]

def user_profile(token, u_id):
    opid = getUserFromToken(token)
    if opid != u_id:
        raise ValueError('invalid token')
    global userdict
    for user in userDict:
        if user['u_id'] == u_id:
            return {user['email'], user['firstname'], user['lastname'], user['handle']}
    raise ValueError('uid was incorrect')
    return 'incorrect_uid'
# returned: { email, name_first, name_last, handle_str }

def user_profile_setemail(token, email):
    opid = getUserFromToken(token)
    
    global userdict
    

    if email == 'bademail' :
        raise ValueError('Invalid email')
    if email == 'usedemail' :
        raise ValueError('Used email')
    '''if token == uid'''
    for user in userDict:
        if opid == user['u_id']:
            user['email'] = email
            return
    raise ValueError('incorrect token')
    return 'incorrect_token'




def user_profile_sethandle(token,handle_str):
    opid = getUserFromToken(token)
    
    if len(handle_str) <= 20 :
        raise ValueError('handle too short')
    for user in userDict:
        if opid == user['u_id']:
            user['handle'] = handle_str
            return
    raise ValueError('incorrect token')
    return 'incorrect_token'





def user_profile_setname(token, name_first, name_last):
    opid = getUserFromToken(token)
    
    if len(name_first) > 50 :
        raise ValueError('First name too long')
    if len(name_last) > 50 :
        raise ValueError('Last name too long')
    
    for user in userDict:
        if opid == user['u_id']:
            user['firstname'] = name_first
            user['lastname'] = name_last
            return

    raise ValueError('incorrect token')
    return 'incorrect_token'






def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    if img_url != 200:
        raise ValueError('url corrupted')
    size = 400
    if x_end > 400 or y_end >400 or x_start > 400 or y_start > 400:
        raise ValueError('Out of bound')
    if x_end < 0 or y_end < 0 or x_start < 0 or y_start < 0:
        raise ValueError('Out of bound')
    pass
