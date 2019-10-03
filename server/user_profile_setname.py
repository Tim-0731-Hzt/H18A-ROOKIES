import pytest
def user_profile_setname(token, name_first, name_last):
    if len(name_first) > 50 :
        raise ValueError('First name too long')
    if len(name_last) > 50 :
        raise ValueError('Last name too long')
    pass