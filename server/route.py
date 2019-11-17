from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
from json import dumps
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

import os

from server.message_pickle import message_send, message_sendlater, message_remove, message_edit
from server.message_pickle import message_react, message_unreact, message_pin, message_unpin
from server.Error import AccessError, ValueError
from server.channel import channel_invite, channel_details, channels_messages, channel_leave, channel_join
from server.channel import channel_addowner, channel_removeowner, channels_list, channels_listall, channels_create 
from server.auth_pickle import auth_login, auth_logout, auth_register, auth_passwordreset_request, auth_passwordreset_reset
from server.user import users_all, user_profile, user_profile_setmail, user_profile_sethandle
from server.user import user_profile_setname, user_profiles_uploadphoto, getUserFromToken
from server.search import search
from server.admin_userpermission_change import admin_userpermission_change
from server.pickle_unpickle import restart
from server.standup import standup_active, standup_send, standup_start

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__, static_url_path='/frontend/prebundle/profile_image')
# APP._static_folder = os.path.abspath("/frontend/prebundle/static/")
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='ROOKIESTHEBEST@gmail.com',
    MAIL_PASSWORD="lvchenkai"
)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

@APP.route('/restart', methods=['POST'])
def begin():
    restart()
    return "restarted"

@APP.route('/message/sendlater', methods=['POST'])
def sendlater():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    return dumps(message_sendlater(token, channel_id, message, time_sent))

@APP.route('/message/send', methods=['POST'])
def send():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    return dumps(message_send(token, channel_id, message))

@APP.route('/message/remove', methods=['DELETE'])
def remove():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_remove(token, int(message_id)))

@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    return dumps(message_edit(token, int(message_id), message))

@APP.route('/message/react', methods=['POST'])
def react():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_react((token), int(message_id), int(react_id)))

@APP.route('/message/unreact', methods=['POST'])
def unreact():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_unreact((token), int(message_id), int(react_id)))

@APP.route('/message/pin', methods=['POST'])
def pin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_pin((token), int(message_id)))

@APP.route('/message/unpin', methods=['POST'])
def unpin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_unpin((token), int(message_id)))

@APP.route('/channels/create', methods=['POST'])
def channel_create():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

@APP.route('/channels/listall', methods=['GET'])
def channel_listall():
    token = request.args.get("token")
    lis = channels_listall(token)
    return dumps(lis)

@APP.route('/channels/list', methods=['GET'])
def channel_list():
    token = request.args.get("token")
    lis = channels_list(token)
    return dumps(lis)

@APP.route('/channel/invite', methods=['POST'])
def channels_invite():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_invite(token, channel_id, u_id))

@APP.route('/channel/details', methods=['GET'])
def channels_details():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    return dumps(channel_details(token, channel_id))

@APP.route('/channel/messages', methods=['GET'])
def channel_messages():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    messages = channels_messages(token, channel_id, start)
    return dumps(messages)

@APP.route('/channel/leave', methods=['POST'])
def channels_leave():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_leave(token, channel_id))

@APP.route('/channel/join', methods=['POST'])
def channels_join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_join(token, channel_id))

@APP.route('/channel/addowner', methods=['POST'])
def channels_addowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_addowner(token, channel_id, u_id))

@APP.route('/channel/removeowner', methods=['POST'])
def channels_removeowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_removeowner(token, channel_id, u_id))

#Jankie
@APP.route('/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    #after_hash_password = hashPassword(password)
    return dumps(auth_login(email, password))

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
    user = auth_register(email, password, name_first, name_last)
    return dumps(user)

@APP.route('/auth/passwordreset/request', methods=['POST'])
def password_request():
    email = request.form.get('email')
    mail = Mail(APP)
    try:
        msg = Message("Slackr Password Reset Number",
            sender="ROOKIESTHEBEST@gmail.com",
            recipients=[email])
        msg.body = str(auth_passwordreset_request(email))
        mail.send(msg)
        return {}
    except Exception as e:
        return (str(e))
    return dumps({})
    # return dumps(auth_passwordreset_request(email))

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def password_reset():
    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    return dumps(auth_passwordreset_reset(reset_code, new_password))

'''Dan'''
@APP.route('/user/profile', methods=['GET'])
def user1():
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    profile = user_profile(token, u_id)
    # profile['u_id'] = 3
    # profile['profile_img_url'] = 'https://webcms3.cse.unsw.edu.au/static/uploads/coursepic/COMP1531/19T3/f69768934fc5db2bb478f938db95efe98b02af69adc0d4a9e79545d0aae44908/Screenshot_from_2019-09-10_22-16-33.png'
    # profile['profile_img_url'] = '7'
    return dumps(profile)

@APP.route('/user/profile/setname', methods=['PUT'])
def user2():
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    user_profile_setname(token, name_first, name_last)
    return dumps({})

@APP.route('/user/profile/setemail', methods=['PUT'])
def user3():
    token = request.form.get('token')
    email = request.form.get('email')
    user_profile_setmail(token, email)
    return dumps({})

@APP.route('/user/profile/sethandle', methods=['PUT'])
def user4():
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    user_profile_sethandle(token, handle_str)
    return dumps({})


@APP.route('/users/all', methods=['GET'])
def user_all():
    token = request.args.get('token')
    return dumps(users_all(token))

@APP.route('/standup/start', methods=['POST'])
def standup1():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    length = request.form.get('length')
    time = standup_start(token, channel_id, length)
    return dumps(time)

@APP.route('/standup/send', methods=['POST'])
def standup2():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    standup_send(token, channel_id, message)
    return dumps({})

@APP.route('/standup/active', methods=['GET'])
def active():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    result = standup_active(token, channel_id)
    return dumps(result)


@APP.route('/search', methods=['GET'])
def searching():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    result = search(token, query_str)
    return dumps(result)

@APP.route('/admin/userpermission/change', methods=['POST'])
def admin():
    token = request.form.get('token')
    u_id = request.form.get('premission_id')
    permission_id = request.form.get('premission_id')
    admin_userpermission_change(token, u_id, permission_id)
    return dumps({})

'''@APP.route('/frontend/prebundle/static/<path:filename>')
def show_img(filename):
    print('\n\n\n')
    print('Displaying image:')
    print(filename)
    print('\n\n\n')
    try:
        send_from_directory("/frontend/prebundle/static", str(filename))
    except:
        return dumps({})
    # send_from_directory("frontend/prebundle/static/",filename)
    root_dir = os.path.dirname(os.getcwd())
    print(root_dir)
    print(os.path.join(root_dir, 'project', 'frontend', 'prebundle', 'static/'))
    return send_from_directory(os.path.join(root_dir, 'frontend', 'prebundle', 'static/'), str(filename))
    #     return send_from_directory("/frontend/prebundle/static", str(filename))
'''

@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def uploadphoto():
    token = request.form.get('token')
    img_url = request.form.get('img_url')
    x_start = request.form.get('x_start')
    y_start = request.form.get('y_start')
    x_end = request.form.get('x_end')
    y_end = request.form.get('y_end')
    return dumps(user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end))

@APP.route('/<filename>', methods=['GET'])
def send_js(filename):
    print('\n\n\n\nshit\n\n')
    return send_from_directory('', filename)

if __name__ == '__main__':
    APP.run()
