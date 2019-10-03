def auth_logout(token):
    pass
    
def test_auth_logout_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    token1 = authRegisterDict['token']

    auth_logout(token1)

def test_auth_logout_2():
    token2 = 'nonvalid'
    auth_logout(token2)
