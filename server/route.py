from message import clear_backup, message_send, message_remove, message_edit
from Error import AccessError
from flask import Flask
from json import dumps

APP = Flask(__name__)
APP.debug = True

@APP.route('/message/send', methods=['POST'])
def send():
    return dumps(message_send(1,1,"hello"))

@APP.route('/message/send/test', methods=['POST'])
def send_test_error():
    try:
        message_send(1,2,"world")
    except AccessError:
        return "The authorised user has not joined the channel they are trying to post to"

@APP.route('/message/remove', methods=['DELETE'])
def remove():
    return dumps(message_remove(3,5))

@APP.route('/message/remove/test/value', methods=['DELETE'])
def remove_test1():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")

    try:
        message_remove(3,100)
    except ValueError:
        return "message not found"
    # return dumps(message_remove(1,100))

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
    return dumps(message_edit(3, 4, "jeff is awesome"))

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
