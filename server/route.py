from flask import Flask
from json import dumps
from message import message_send, message_remove

APP = Flask(__name__)

@APP.route('/message/send', methods=['POST'])
def send():
    return dumps(message_send(1,1,"hello"))

@APP.route('/message/remove', methods=['DELETE'])
def remove():
    return dumps(message_remove(1,5))
    # return redirect("/message")


if __name__ == '__main__':
    APP.run()
