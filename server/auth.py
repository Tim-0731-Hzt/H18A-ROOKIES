# AUTH
import re
import hashlib
import jwt
from json import dumps
from flask import Flask, request
from Error import AccessError

APP = Flask(_name_)

SECRET = 'sempai'
# Global variable
authDict = [{
    'handle':[],
}
]
channelDict = []
messDict = [] 

data = {
    'users': [],
}

def sendSuccess(data):
    return dumps(data)

def sendError(message):
    return dumps({
        '_error':message,
    })

def generateToken(username):
    global SECRET
    encoded = jwt.encode({'username':username},SECRET, algorithm='HS256')
    return str(encoded)

def getUserFromToken(token):
    global SECRET
    decoded = jwt.decode(token,SECRET, algorithms=['HS256'])
    return decoded['u_id']

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

@APP.route('/secrets', methods=['GET'])
def get():
    if getUserFromToken(request.args.get('token')) is None:
        return sendError('Invalid token')
    return sendSuccess({
        'secrets':['I','love','durians',]
    })
# Given aregisterd user' email and password and generates a valid token for the user to remain authenticated.
# ValueError when:
# Email entered is not a valid email
# Email entered does not belong to a user
# password is not correct
def auth_login (email, password):
    pass
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if ( re.search(regex, email)):
        pass
    else:
        raise ValueError("Valid Email")
    #incorrect password
    if (len(password) < 5):
        raise ValueError("Password is not correct")
    for user in data['users']:
        if user['email'] is email:
            pass
        else:
             raise ValueError("Email entered doesn't belong to a user")
    for user in data['users']:     
        if user['email'] == email and user['password'] == hashPassword(password):
            return sendSuccess({
                'token':generateToken(username),
            })
    return sendError('Username or password incorrect')


# Given an active token, invalidates the taken to log the user out. If a valid token is given, and the user is successfully logged out, it returns true, otherwise false.
def auth_logout(token):
    pass
    

# Given a user's first and last name, email address, and password, create a new account for them and return a new token for authentication in their session. A handle is generated that is the concatentation of a lowercase-only first name and last name. If the handle is already taken, a number is added to the end of the handle to make it unique.
# ValueError when:
# Email is not valid
# Email address is already used
# password entered less than 6 words
# name_first and name_last is between 1 and 50 characters
def auth_register(email, password, name_first, name_last):
    #check email
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        pass
    else:
        raise ValueError("Valid Email")
    # Email already be used 
    for user in data['users']:
        if email is user['email']:
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
    firstName = name_first.lower()
    lastName = name_last.lower()
    handle = firstName + lastName
    if handle is not in authDict['handle']:
        auth_identity(handle)
    else:
        for i in range(0,9999):
            if handle + str(i) is not in authDict['handle']
                authDict['handle'].append(handle + str(i))
                handle = handle + str(i)
    data['users'].append({
        'username':handle,
        'password':hashPassword(password),
        'email':email,
    })
    return sendSuccess({
        'token':generateToken(handle),
    })

# Given an email address, if the user is a registered user, send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, shows that the user trying to reset the password is the one who got sent this email.
def auth_passwordreset_request(email):
    pass


# Given a reset code for a user, set that user's new password to the password provided
# ValueError when:
# reset_code is not valid reset code
# password entered is not valid
def auth_passwordreset_reset(reset_code, new_password):
    pass
    #incorrect password
    if (len(new_password) < 5):
        raise ValueError("New password is not valid")
