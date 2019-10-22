from flask import Flask
from json import dumps
from channel import *
from auth import *
APP = Flask(__name__)

@APP.route('/channel/create',methods = ['POST'])
def test_channel_create():
    token = auth_register("hzt731tim@gmail.com","Qewewfrfc","Tim","Hu")
    channels_create(token,"COMP1531", True):

if __name__ == '__main__':
    APP.run()