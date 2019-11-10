# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user
from server.Error import AccessError, ValueError
from server.auth_pickle import getUserFromToken
from server.pickle_unpickle import *
from PIL import Image
import requests
import urllib.request
import sys
import re

def users_all(token):
    uid = getUserFromToken(token)
    data = load()
    userDict = data['userDict']
    lis = []
    for user in userDict:
        d = {
            'u_id': user['u_id'],
            'profile_img_url': user['profile_img_url'],
            # 'profile_img_url': None,
            'email': (user['email']), 
            'name_first': (user['first_name']),
            'name_last': (user['last_name']),
            'handle_str': (user['handle'])
        }
        lis.append(d)

    return {
        'users': list(lis)
    }

def user_profile(token, u_id):
    try:
        ID = getUserFromToken(token)
    except:
        raise ValueError('token was incorrect')
    if int(u_id) != int(ID):
        raise ValueError('incorrect u_id')
    DATA = load()
    userdict = DATA['userDict']
    for user in userdict:
        if int(user['u_id']) == int(u_id):
            d = {
                'u_id': int(u_id),
                'profile_img_url': (user['profile_img_url']),
                'email': (user['email']), 
                'name_first': (user['first_name']),
                'name_last': (user['last_name']),
                'handle_str': (user['handle'])
            }
            return d
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
    





def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    response = requests.get(img_url)
    if response.status_code != 200:
        raise ValueError('url corrupted')
    img = Image. open(urllib. request. urlopen(img_url))
    width, height = img.size
    if img == -1:
        raise ValueError("image does not exist")
    if x_end == x_start or y_end == y_start:
        raise ValueError("incorrect range")
    if int(x_end) > width or int(y_end) > height or int(x_start) > width or int(y_start) > height:
        raise ValueError('Out of bound')
    if int(x_end) < 0 or int(y_end) < 0 or int(x_start) < 0 or int(y_start) < 0:
        raise ValueError('Out of bound')
    if img.format !=  "JPEG" and img.format != "JPG":
        raise ValueError("Image uploaded is not a JPG")
    cropped =  img.crop((int(x_start), int(y_start), int(x_end), int(y_end)))
    id = getUserFromToken(token)
    cropped = cropped.save('server/photo/' + str(id) + '.jpg')
    DATA = load()
    userDict = DATA['userDict']
    for user in userDict:
        if id == user['u_id']:
            user['profile_img_url'] =  'http://localhost:8001/server/photo/'+ str(id) + '.jpg'
    DATA['userDict'] = userDict
    save(DATA)