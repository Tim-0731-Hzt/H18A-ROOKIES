from message import message_send, message_remove
from Error import AccessError
from flask import Flask
from json import dumps


APP = Flask(__name__)

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
    # return redirect("/message")
@APP.route('/message/remove/test/value', methods=['DELETE'])
def remove_test1():
    try:
        message_remove(3,100)
    except ValueError:
        return "message not found"
    # return dumps(message_remove(1,100))

@APP.route('/message/remove/test/access', methods=['DELETE'])
def remove_test2():
    try:
        message_remove(1,4)
    except AccessError:
        return "Unauthorised remove"



if __name__ == '__main__':
    APP.run()
