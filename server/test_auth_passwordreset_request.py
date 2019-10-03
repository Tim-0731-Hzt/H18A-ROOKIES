def auth_passwordreset_request(email):
    pass
    
def test_auth_passwordreset_request_1():
    authLoginDict = auth_login('hayden@gmail.com','123456')
    u_id1 = authLoginDict['u_id']
    assert u_id1 == '00001'
    auth_passwordreset_request('hayden@gmail.com')

def test_auth_passwordreset_request_2():
    authLoginDict = auth_login('jankie@gmail.com','123456')
    u_id2 = authLoginDict2['u_id']
    assert u_id2 == '00002'
    auth_passwordreset_request('jankie@gmail.com')