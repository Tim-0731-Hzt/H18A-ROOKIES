
from flask import Flask
from flask_mail import Mail, Message
from auth import *

APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'ROOKIESTHEBEST@gmail.com',
    MAIL_PASSWORD = "lvchenkai"
)

@APP.route('/send-mail/')
def send_mail():
    mail = Mail(APP)
    try:
        msg = Message("Send Mail Test!",
            sender="ROOKIESTHEBEST@gmail.com",
            recipients=["hzt731tim@gmail.com"])
        msg.body = generateResetCode()
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return (str(e))

if __name__ == '__main__':
    APP.run()

# 
