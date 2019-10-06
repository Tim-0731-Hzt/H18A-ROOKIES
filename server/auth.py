##AUTH########
import re
##
def auth_login (email, password):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        pass
    else:
        raise ValueError("Valid Email")
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")


##
def auth_logout(token):
    pass

##
def auth_register(email, password, name_first, name_last):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        pass
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

##
def auth_passwordreset_request(email):
    pass


##
def auth_passwordreset_reset(reset_code, new_password):
    pass
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")
