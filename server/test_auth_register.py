def auth_register(email, password, name_first, name_last):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        
    else:
        raise ValueError("Valid Email")
    #incorrect password
    if (len(name_first) > 50):
        raise ValueError("name_first error")
    if (len(name_last) > 50):
        raise ValueError("name_last error")
def test_auth_register():