def auth_register(email, password, name_first, name_last):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        
    else:
        raise ValueError("Valid Email")
    #incorrect name
    if (len(name_first) > 50):
        raise ValueError("name_first error")
    if (len(name_last) > 50):
        raise ValueError("name_last error")
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")


def test_auth_register_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id1 = authRegisterDict['u_id']
    token1 = authRegisterDict['u_id']
    assert u_id1 == "00001"
    assert token1 == "1"

def test_auth_register_2():
    authRegisterDict = auth_register('Jankie@gmail.com', '123456','Jankie','Lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['u_id']
    assert u_id2 == "00002"
    assert token2 == "2"

def test_auth_register_3():
    with pytest.raises(ValueError, match=r"*"):
        auth_register('soundsbad', '123456') #incorrect email

def test_auth_register_4():
    with pytest.raises(ValueError, match=r"*"):
        auth_register('soundsbad', '1234') #incorrect password

