from flask import Flask,request
from json import dumps
from channel import *
from auth import *
APP = Flask(__name__)

@APP.route('/channel/create',methods = ['POST'])
def test_channel_create_1():
    email = request.form.get("email")
    password = request.form.get("password")
    name_first = request.form.get("name_first")
    name_last = request.form.get("name_last")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    token = auth_register(email, password, name_first, name_last)
    token = token[2:len(token) - 1]
    return dumps(channels_create(token, name, is_public))

if __name__ == '__main__':
    APP.run()
