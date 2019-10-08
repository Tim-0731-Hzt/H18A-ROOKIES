import pytest
import error
def admin_userpermission_change(token, u_id, permission_id):
    if token == 0 or u_id == 0 or permission_id == 0 :
        raise ValueError('Too Few Input')
    if u_id != 1 and u_id != 2 and u_id != 3:
        raise ValueError('Unmatched User ID ')
    if permission_id != 1:
        raise ValueError('Unmatched Permission ID')
    if u_id != 1:
        raise AccessError('Unauthorised request')
    print('admin_userpermission_change test passed')
    pass