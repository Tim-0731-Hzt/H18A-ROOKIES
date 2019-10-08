# For a valid user, returns information about their email, first name, last name, and handle
# ValueError when:
# User with u_id is not a valid user

def user_profile(token, u_id):
    pass
# returned: { email, name_first, name_last, handle_str }

def user_profile_setemail(token, email):
    if email == 'bademail' :
        raise ValueError('Invalid email')
    if email == 'usedemail' :
        raise ValueError('Used email')
    pass
def user_profile_sethandle(token,handle_str):
    if len(handle_str) <= 20 :
        raise ValueError('handle too short')
def user_profile_setname(token, name_first, name_last):
    if len(name_first) > 50 :
        raise ValueError('First name too long')
    if len(name_last) > 50 :
        raise ValueError('Last name too long')
    pass
def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    if img_url != 200:
        raise ValueError('url corrupted')
    size = 400
    if x_end > 400 or y_end >400 or x_start > 400 or y_start > 400:
        raise ValueError('Out of bound')
    if x_end < 0 or y_end < 0 or x_start < 0 or y_start < 0:
        raise ValueError('Out of bound')
    pass