import re

def auth_login (email, password):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        
    else:
        raise ValueError("Valid Email")
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")
    
def test_auth_login_1():
    authLoginDict = auth_login('goodemail@gmail.com', '123456') 
    u_id1 = authLoginDict['u_id']
    token1 = authLoginDict['token1']

    assert u_id1 == '00001'
    assert token1 =='token1'
def test_auth_login_2():
    with pytest.raises(ValueError, match=r".*"):
        auth_login('soundsbad', '123456')