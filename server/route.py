from flask import Flask, request
from json import dumps
from auth import *

APP = Flask(__name__)

APP.debug = True


@APP.route('/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    after_hash_password = hashPassword(password)
    return dumps(auth_login(email, after_hash_password))

@APP.route('/auth/logout', methods=['POST'])
def logout():
    token = request.form.get('token')
    return dumps(auth_logout(token))

@APP.route('/auth/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    return dumps(auth_register(email, password, name_first, name_last))
    

@APP.route('/auth/passwordreset/request', methods=['POST'])
def password_request():
    email = request.form.get('email')
    return dumps(auth_passwordreset_request(email))

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def password_reset():
    reset_code = request.form.get('reset_code')
    new_password = request.form.get(hashPassword(new_password))
    return dumps(auth_passwordreset_reset(reset_code, new_password))


if __name__ == '__main__':
    APP.run()
