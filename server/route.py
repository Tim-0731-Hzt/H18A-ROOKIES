from flask import Flask
from json import dumps
from channel import *
APP = Flask(__name__)

@APP.route('/channel/invite',methods = ['POST'])
def test_channel_invite():
    channel_invite ("d12d2ed32", 1 , "z666")
    dumps(channelDict['member'])

if __name__ == '__main__':
    APP.run()