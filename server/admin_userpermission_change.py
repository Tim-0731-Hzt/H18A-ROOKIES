
from server.Error import AccessError
from server.auth_pickle import *
import server.pickle_unpickle
from server.channel import *

def admin_userpermission_change(token, u_id, permission_id):
    fl = 1
    data = load()
    userDict = data['userDict']
    for user in userDict:
        if u_id == user['u_id']:
            fl = 0
    if fl == 1:
        raise ValueError('Wrong user id')
    if permission_id not in range(1,4):
        raise ValueError('Unmatch permission id')
    
    opid = getUserFromToken(token)
    for user in userDict:
        if user['u_id'] == opid:
            if user['permission_id'] == 2 and permission_id == 1:
                raise AccessError('Permission Denied: Trying to give owner by admin')
            if user['permission_id'] == 3:
                raise AccessError('Permission Denied : member can not do this')
    for sb in userDict:
        if sb['u_id'] == u_id:
            if sb['permission_id'] == 1:
                raise AccessError('Permission Denied: Trying to change owner permission')
            sb['permission_id'] = permission_id
    data['userDict'] = userDict
    save(data)
    pass
  
