def auth_passwordreset_reset(reset_code, new_password):
    pass
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")
def test_auth_passwordreset_reset_1():
    auth_passwordreset_reset('wawawa','123456')
    
 def test_auth_passwordreset_reset_2():   
    with pytest.raises(ValueError, match=r"*"):
        auth_passwordreset_reset('asasas', '123456')