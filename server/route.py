from message import clear_backup, message_send, message_remove, message_edit
from Error import AccessError
from flask import Flask, request
from json import dumps

APP = Flask(__name__)
APP.debug = True

@APP.route('/message/send', methods=['POST'])
def send():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    return dumps(message_send(token,channel_id,message))

@APP.route('/message/send/test', methods=['POST'])
def send_test_error():
    try:
        message_send(1,2,"world")
    except AccessError:
        return "The authorised user has not joined the channel they are trying to post to"

@APP.route('/message/remove', methods=['DELETE'])
def remove():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_remove(token,int(message_id)))

@APP.route('/message/remove/test/value', methods=['DELETE'])
def remove_test1():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_remove(3,100)
    except ValueError:
        return "message not found"

@APP.route('/message/remove/test/access', methods=['DELETE'])
def remove_test2():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_remove(1,4)
    except AccessError:
        return "Unauthorised remove"

@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    return dumps(message_edit(token, int(message_id), message))

@APP.route('/message/edit/test', methods=['PUT'])
def edit_test():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")

    try:
        message_edit(1, 4, "jeff is awesome")
    except AccessError:
        return "Unauthorised edit"

if __name__ == '__main__':
    APP.run()
