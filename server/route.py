from flask import Flask,request
from json import dumps
from channel import *
from auth import *
APP = Flask(__name__)


@APP.route('/user/create',methods = ['POST'])
def test_channel_create():
    email = request.form.get("email")
    password = request.form.get("password")
    name_first = request.form.get("name_first")
    name_last = request.form.get("name_last")
    dic = {}
    dic = auth_register(email, password, name_first, name_last)
    token = dic['token']
    token = token[2:len(token) - 1]
    return dumps(token)

@APP.route('/channel/create',methods = ['POST'])
def test_channel_create_1():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

@APP.route('/channel/listall',methods = ['GET'])
def test_channel_listall():
    token = request.args.get("token")
    return dumps(channels_listall(token))

@APP.route('/channel/list',methods = ['GET'])
def test_channel_list():
    token = request.args.get("token")
    return dumps(channels_list(token))

@APP.route('/channel/invite',methods = ['POST'])
def test_channel_invite():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    #return dumps(channel_id)
    u_id = request.form.get('u_id')
    channel_invite (token, channel_id, u_id)
    return dumps(channels_listall(token))
if __name__ == '__main__':
    APP.run()
