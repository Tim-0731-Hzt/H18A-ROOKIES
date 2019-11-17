from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
from json import dumps
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

import os

from server.message_pickle import message_send, message_sendlater, message_remove, message_edit
from server.message_pickle import message_react, message_unreact, message_pin, message_unpin
from server.Error import AccessError, ValueError
from server.channel import channel_invite, channel_details, channels_messages, channel_leave
from server.channel import channel_addowner, channel_removeowner, channels_list
from server.channel import channel_join, channels_listall, channels_create
from server.auth_pickle import auth_login, auth_logout, auth_register, auth_passwordreset_request
from server.auth_pickle import auth_passwordreset_reset
from server.user import users_all, user_profile, user_profile_setmail, user_profile_sethandle
from server.user import user_profile_setname, user_profiles_uploadphoto, getUserFromToken
from server.search import search
from server.admin_userpermission_change import admin_userpermission_change
from server.pickle_unpickle import restart
from server.standup import standup_active, standup_send, standup_start

# Flask route for defalut handler for errors
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

# route for backend date wiping
@APP.route('/restart', methods=['POST'])
def begin():
    restart()
    return "restarted"

# Flask route for sendlater
@APP.route('/message/sendlater', methods=['POST'])
def sendlater():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    return dumps(message_sendlater(token, channel_id, message, time_sent))

# Flask route for message_send
@APP.route('/message/send', methods=['POST'])
def send():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    return dumps(message_send(token, channel_id, message))

# Flask route for messsage_remove
@APP.route('/message/remove', methods=['DELETE'])
def remove():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_remove(token, int(message_id)))

# Flask route for message_edit
@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    return dumps(message_edit(token, int(message_id), message))

# Flask route for message_react
@APP.route('/message/react', methods=['POST'])
def react():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_react((token), int(message_id), int(react_id)))

# Flask route for message_unreact
@APP.route('/message/unreact', methods=['POST'])
def unreact():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_unreact((token), int(message_id), int(react_id)))

# Flask route for message_pin
@APP.route('/message/pin', methods=['POST'])
def pin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_pin((token), int(message_id)))

# Flask route for message_unpin
@APP.route('/message/unpin', methods=['POST'])
def unpin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_unpin((token), int(message_id)))

# Flask route for channel_create
@APP.route('/channels/create', methods=['POST'])
def channel_create():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

# Flask route for channels_listall
@APP.route('/channels/listall', methods=['GET'])
def channel_listall():
    token = request.args.get("token")
    lis = channels_listall(token)
    return dumps(lis)

# Flask route for channels_list
@APP.route('/channels/list', methods=['GET'])
def channel_list():
    token = request.args.get("token")
    lis = channels_list(token)
    return dumps(lis)

# Flask route for channel_invite
@APP.route('/channel/invite', methods=['POST'])
def channels_invite():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_invite(token, channel_id, u_id))

# Flask route for channel_details
@APP.route('/channel/details', methods=['GET'])
def channels_details():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    return dumps(channel_details(token, channel_id))

# Flask route for channel_messages
@APP.route('/channel/messages', methods=['GET'])
def channel_messages():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    messages = channels_messages(token, channel_id, start)
    return dumps(messages)

# Flask route for channel_leave
@APP.route('/channel/leave', methods=['POST'])
def channels_leave():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_leave(token, channel_id))

# Flask route for channel_join
@APP.route('/channel/join', methods=['POST'])
def channels_join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_join(token, channel_id))

# Flask route for channel_addowner
@APP.route('/channel/addowner', methods=['POST'])
def channels_addowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_addowner(token, channel_id, u_id))

# Flask route for channel_removeowner
@APP.route('/channel/removeowner', methods=['POST'])
def channels_removeowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_removeowner(token, channel_id, u_id))

# Flask route for auth_login
@APP.route('/auth/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    #after_hash_password = hashPassword(password)
    return dumps(auth_login(email, password))

# Flask route for auth_logout
@APP.route('/auth/logout', methods=['POST'])
def logout():
    token = request.form.get('token')
    return dumps(auth_logout(token))

# Flask route for auth_register
@APP.route('/auth/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    user = auth_register(email, password, name_first, name_last)
    return dumps(user)

# Flask route for auth_password_request
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
        return str(e)
    return dumps({})
    # return dumps(auth_passwordreset_request(email))

# Flask route for auth_password_reset
@APP.route('/auth/passwordreset/reset', methods=['POST'])
def password_reset():
    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    return dumps(auth_passwordreset_reset(reset_code, new_password))

# Flask route for user_profile
@APP.route('/user/profile', methods=['GET'])
def user1():
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    profile = user_profile(token, u_id)
    # profile['u_id'] = 3
    # profile['profile_img_url'] = '7'
    return dumps(profile)

# Flask route for user_profile_setname
@APP.route('/user/profile/setname', methods=['PUT'])
def user2():
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    user_profile_setname(token, name_first, name_last)
    return dumps({})

# Flask route for user_profile_setmail
@APP.route('/user/profile/setemail', methods=['PUT'])
def user3():
    token = request.form.get('token')
    email = request.form.get('email')
    user_profile_setmail(token, email)
    return dumps({})

# Flask route for user_profile_sethandle
@APP.route('/user/profile/sethandle', methods=['PUT'])
def user4():
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    user_profile_sethandle(token, handle_str)
    return dumps({})

# Flask route for user_all
@APP.route('/users/all', methods=['GET'])
def user_all():
    token = request.args.get('token')
    return dumps(users_all(token))

# Flask route for standup_start
@APP.route('/standup/start', methods=['POST'])
def standup1():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    length = request.form.get('length')
    time = standup_start(token, channel_id, length)
    return dumps(time)

# Flask route for standup_send
@APP.route('/standup/send', methods=['POST'])
def standup2():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    standup_send(token, channel_id, message)
    return dumps({})

# Flask route for standup_active
@APP.route('/standup/active', methods=['GET'])
def active():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    result = standup_active(token, channel_id)
    return dumps(result)

# Flask route for search
@APP.route('/search', methods=['GET'])
def searching():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    result = search(token, query_str)
    return dumps(result)

# Flask route for change permission
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

# Flask route for user_profile_uploadphoto
@APP.route('/user/profiles/uploadphoto', methods=['POST'])
def uploadphoto():
    token = request.form.get('token')
    img_url = request.form.get('img_url')
    x_start = request.form.get('x_start')
    y_start = request.form.get('y_start')
    x_end = request.form.get('x_end')
    y_end = request.form.get('y_end')
    return dumps(user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end))

# Flask route for displaying image
@APP.route('/<filename>', methods=['GET'])
def send_js(filename):
    print('\n\n\n\nshit\n\n')
    return send_from_directory('', filename)

if __name__ == '__main__':
    APP.run()
