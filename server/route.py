
from message_pickle import message_send, message_remove, message_edit, message_react, message_unreact, message_pin, message_unpin
from Error import AccessError
from flask import Flask, request
from flask_mail import Mail, Message
from json import dumps
from channel import *
from auth_pickle import *
from user import *
from search import search
from admin_userpermission_change import admin_userpermission_change
from pickle_unpickle import restart


APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'ROOKIESTHEBEST@gmail.com',
    MAIL_PASSWORD = "lvchenkai"
)

@APP.route('/restart', methods = ['POST'])
def begin():
    restart()
    return "restarted"

@APP.route('/send-mail/')
def send_mail():
    mail = Mail(APP)
    try:
        msg = Message("Send Mail Test!",
            sender="ROOKIESTHEBEST@gmail.com",
            recipients=["person.sending.to@gmail.com"])
        msg.body = generateResetCode()
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return (str(e))


@APP.route('/message/sendlater', methods=['POST'])
def sendlater():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    time_sent = request.form.get('time_sent')
    return dumps(message_send(token,channel_id,message))

@APP.route('/message/send', methods=['POST'])
def send():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    return dumps(message_send(token,channel_id,message))

'''@APP.route('/message/send/test', methods=['POST'])
def send_test_error():
    try:
        message_send(1,2,"world")
    except AccessError:
        return "The authorised user has not joined the channel they are trying to post to"
'''

@APP.route('/message/remove', methods=['DELETE'])
def remove():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_remove(token,int(message_id)))

'''@APP.route('/message/remove/test/value', methods=['DELETE'])
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
        return "Unauthorised remove"'''

@APP.route('/message/edit', methods=['PUT'])
def edit():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')
    return dumps(message_edit(token, int(message_id), message))

'''@APP.route('/message/edit/test', methods=['PUT'])
def edit_test():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")

    try:
        message_edit(1, 4, "jeff is awesome")
    except AccessError:
        return "Unauthorised edit"'''

@APP.route('/message/react', methods=['POST'])
def react():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_react(int(token), int(message_id), int(react_id)))

'''@APP.route('/message/react/test1', methods=['POST'])
def react_test1():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_react(1, 3, -1)
    except ValueError:
        return "invalid react_id"

@APP.route('/message/react/test2', methods=['POST'])
def react_test2():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_react(9, 3, 1)
    except ValueError:
        return "message_id is not a valid message within a channel that the authorised user has joined"

@APP.route('/message/react/test3', methods=['POST'])
def react_test3():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    message_react(2, 3, 1)
    try:
        message_react(2, 3, 2)
    except ValueError:
        return "Message with ID message_id already contains an active React with ID react_id"'''

@APP.route('/message/unreact', methods=['POST'])
def unreact():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')
    return dumps(message_unreact(int(token), int(message_id), int(react_id)))

'''@APP.route('/message/unreact/test1', methods=['POST'])
def unreact_test1():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_unreact(1, 3, -1)
    except ValueError:
        return "invalid react_id"

@APP.route('/message/unreact/test2', methods=['POST'])
def unreact_test2():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_unreact(9, 3, 1)
    except ValueError:
        return "message_id is not a valid message within a channel that the authorised user has joined"

@APP.route('/message/unreact/test3', methods=['POST'])
def unreact_test3():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    try:
        message_unreact(2, 3, 2)
    except ValueError:
        return "Message with ID message_id does not contain an active unreact with ID unreact_id"

@APP.route('/message/unreact/test4', methods=['POST'])
def unreact_test4():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    message_react(1, 3, 1)
    try:
        message_unreact(1, 3, 5)
    except ValueError:
        return "invalid react_id"'''

@APP.route('/message/unpin', methods=['POST'])
def unpin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    return dumps(message_unpin(int(token), int(message_id)))

'''@APP.route('/message/unpin/test1', methods=['POST'])
def unpin_test1():
    clear_backup()
    for i in range(5):
        message_send(1, 1, "hello")
    try:
        message_unpin(3, 10)
    except ValueError:
        return "invalid message_id"

@APP.route('/message/unpin/test2', methods=['POST'])
def unpin_test2():
    clear_backup()
    for i in range(5):
        message_send(1, 1, "hello")
    message_pin(3, 3)
    try:
        message_unpin(1, 3)
    except ValueError:
        return "authorised user is not admin"

@APP.route('/message/unpin/test3', methods=['POST'])
def unpin_test3():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    message_pin(3,3)
    message_unpin(3,3)
    try:
        message_unpin(3,3)
    except ValueError:
        return "already unpinned"

@APP.route('/message/unpin/test4', methods=['POST'])
def unpin_test4():
    clear_backup()
    for i in range(5):
        message_send(1,1,"hello")
    message_pin(3,3)    
    try:
        message_unpin(9,3)
    except AccessError:
        return "The authorised user is not a member of the channel that the message is within"'''


@APP.route('/user/create',methods = ['POST'])
def test_user_register():
    email = request.form.get("email")
    password = request.form.get("password")
    name_first = request.form.get("name_first")
    name_last = request.form.get("name_last")
    dic = {}
    dic = auth_register(email, password, name_first, name_last)
    token = dic['token']
    return dumps(token)

@APP.route('/channels/create',methods = ['POST'])
def test_channel_create_1():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

@APP.route('/channels/listall',methods = ['GET'])
def test_channel_listall():
    token = request.args.get("token")
    return dumps(channels_listall(token))

@APP.route('/channels/list',methods = ['GET'])
def test_channel_list():
    token = request.args.get("token")
    return dumps(channels_list(token))
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
        msg = Message("Send Mail Test!",
            sender="ROOKIESTHEBEST@gmail.com",
            recipients=[email])
        msg.body = generateResetCode()
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return (str(e))
    
   # return dumps(auth_passwordreset_request(email))

@APP.route('/auth/passwordreset/reset', methods=['POST'])
def password_reset():
    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    return dumps(auth_passwordreset_reset(reset_code, new_password))

'''Dan'''
@APP.route('/user/profile', methods = ['GET'])
def user1():
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    profile = user_profile(token,u_id)
    return dumps(profile)

@APP.route('/user/profile/setname', methods = ['PUT'])
def user2():
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    user_profile_setname(token,name_first, name_last)
    return dumps({})

@APP.route('/user/profile/setemail', methods = ['PUT'])
def user3():
    token = request.form.get('token')
    email = request.form.get('email')
    user_profile_setmail(token,email)
    return dumps({})

@APP.route('/user/profile/sethandle', methods = ['PUT'])
def user4():
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    user_profile_sethandle(token,handle_str)
    return dumps({})

@APP.route('/user/profiles/uploadphoto', methods = ['POST'])
def upload_photo():
    pass


@APP.route('/standup/start', methods = ['POST'])
def standup1():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    standup_start(token,channel_id)
    time = showtime()
    return dumps(time)

@APP.route('/standup/send', methods = ['POST'])
def standup2():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    standup_send(token,channel_id, message)
    return dumps({})

@APP.route('/search', methods = ['GET'])
def se():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    result = search(token, query_str)
    return dumps(result)

@APP.route('/admin/userpermission/change', methods = ['POST'])
def admin():
    token = request.form.get('token')
    u_id = request.form.get('premission_id')
    permission_id = request.form.get('premission_id')
    admin_userpermission_change(token,u_id,premission_id)
    return dumps({})



'''
@APP.route('/user/create',methods = ['POST'])
def test_channel_create():
    email = request.form.get("email")
    password = request.form.get("password")
    name_first = request.form.get("name_first")
    name_last = request.form.get("name_last")
    dic = {}
    dic = auth_register(email, password, name_first, name_last)
    token = dic['token']
    token = token[2:len(token) - 1]
    return dumps(token)

@APP.route('/channel/create',methods = ['POST'])
def test_channel_create_1():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

@APP.route('/channel/listall',methods = ['GET'])
def test_channel_listall():
    token = request.args.get("token")
    return dumps(channels_listall(token))

@APP.route('/channel/list',methods = ['GET'])
def test_channel_list():
    token = request.args.get("token")
    return dumps(channels_list(token))

@APP.route('/channel/invite',methods = ['POST'])
def test_channel_invite():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    #return dumps(channel_id)
    u_id = request.form.get('u_id')
    channel_invite (token, channel_id, u_id)
    return dumps(channels_listall(token))
'''
if __name__ == '__main__':
    APP.run()
