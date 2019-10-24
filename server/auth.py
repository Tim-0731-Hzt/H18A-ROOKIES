# AUTH
import re
import hashlib
import jwt
import random
from json import dumps
from flask import Flask, request
from Error import AccessError


SECRET = 'ROOKIES'
# Global variable
#memberDict = []
#channelDict = []
#messDict = [] 
userDict = []

def sendSuccess(userDict):
    return dumps(userDict)

def sendError(message):
    return dumps({
        '_error':message,
    })


def generateResetCode():
    num = []
    for i in range(6):
         num.append(random.randint(1,10))
    reset_code = ''.join(map(str,num))
    
    return reset_code
    

def generateToken(username):
    global SECRET
    encoded = jwt.encode({'u_id':username},SECRET, algorithm='HS256')
    return str(encoded)

def getUserFromToken(token):
    global SECRET
    decoded = jwt.decode(token, verify = False)
    return decoded['u_id']

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Given aregisterd user' email and password and generates a valid token for the user to remain authenticated.
# ValueError when:
# Email entered is not a valid email
    # Email entered does not belong to a user
# password is not correct
def auth_login (email, password):
    global userDict
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if ( re.search(regex, email)):
        pass
    else:
        raise ValueError("Invalid Email")
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")
    for user in userDict:
        if user['email'] == email:
            break
        else:
             raise ValueError("Email entered doesn't belong to a user")
    for user in userDict:     
        if user['email'] == email and user['password'] == hashPassword(password):
            return {
                'u_id': user['u_id'],
                'token': generateToken(user['u_id'])
            }
    return sendError('Username or password incorrect')


# Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false.
def auth_logout(token):
    global userDict
    u_id = getUserFromToken(token)
    print(u_id)
    for user in userDict:
        if user['u_id'] == u_id:
            user['online'] = False
            return True
    return False

# Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the handle is already taken, a number is added to the end of the handle to make it unique.
# ValueError when:
# Email is not valid
# Email address is already used
# password entered less than 6 words
# name_first and name_last is between 1 and 50 characters
def auth_register(email, password, name_first, name_last):
    global userDict
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        pass
    else:
        raise ValueError("Invalid Email")
    # Email already be used 
    for user in userDict:
        if user['email'] == email:
            raise ValueError("Email address is already used bt another user.")
    # incorrect name
    if (len(name_first) > 50):
        raise ValueError("Firstname is needed between 1 and 50 characters.")
    if (len(name_last) > 50):
        raise ValueError("Lastname is needed between 1 and 50 characters.")
    # incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not valid")
 #   username = request.form.get('username')
 #   password = request.form.get('password') 
    newUser = { 
        'first_name' : None,
        'last_name' : None,
        'email' : None,
        'u_id' : None,
        'handle' : None,
        'password' : None,
        'online' : True,
        'reset_code': None,
    }
    firstName = name_first.lower()
    lastName = name_last.lower()
    handle = firstName + lastName 

    newUser['handle'] = handle 
    for user in userDict:
        if user['handle'] is handle:
            for i in range(0,9999):
                if user['handle'] is not handle + str(i):
                    newUser['handle'] = handle + str(i)
                    break
        else:
            pass
        
    newUser['first_name'] = name_first
    newUser['last_name'] = name_last
    newUser['email'] = email
    newUser['u_id'] = len(userDict) + 1
    newUser['password'] = hashPassword(password)
    userDict.append(newUser)
    
    returned = {
        'u_id': newUser['u_id'],
        'token': generateToken(newUser['u_id'])
    }

    return returned

# Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.
def auth_passwordreset_request(email):
    global userDict
    for user in userDict:
        if user['email'] == email:
            user['reset_code'] = generateResetCode()
            return user['reset_code']
            

# Given a reset code for a user, set that user's new password to the password provided
# ValueError when:
# reset_code is not valid reset code
# password entered is not valid
def auth_passwordreset_reset(reset_code, new_password):
    global userDict
    #incorrect password
    if (len(new_password) < 5):
        raise ValueError("New password is not valid")
    if (len(reset_code) != 6):
        raise ValueError("reset_code is not valid")

    for user in userDict:
        if user['reset_code'] == reset_code:
            user['password'] = hashPassword(new_password)
            user['reset_code'] = None
    raise ValueError("reset_code is not valid")
