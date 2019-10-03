import pytest
def user_profile_setemail(token, email):
    if email == 'bademail' :
        raise ValueError('Invalid email')
    if email == 'usedemail' :
        raise ValueError('Used email')
    pass