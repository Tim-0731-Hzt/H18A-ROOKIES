from server.message_pickle import message_send, message_remove, message_edit, message_react, message_unreact, message_pin, message_unpin
from server.Error import AccessError, ValueError
from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
from json import dumps
from server.channel import *
from server.auth_pickle import *
from server.user import *
from server.search import search
from server.admin_userpermission_change import admin_userpermission_change
from server.pickle_unpickle import restart
from werkzeug.exceptions import HTTPException
from flask_cors import CORS

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

'''
class AccessError(HTTPException):
    code = 500
    message = 'AccessError'
'''




APP = Flask(__name__)
APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'ROOKIESTHEBEST@gmail.com',
    MAIL_PASSWORD = "lvchenkai"
)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)


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
def send_error():
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
def user_register():
    email = request.form.get("email")
    password = request.form.get("password")
    name_first = request.form.get("name_first")
    name_last = request.form.get("name_last")
    dic = {}
    dic = auth_register(email, password, name_first, name_last)
    token = dic['token']
    return dumps(token)

@APP.route('/channels/create',methods = ['POST'])
def channel_create():
    token = request.form.get("token")
    name = request.form.get("name")
    is_public = request.form.get("is_public")
    return dumps(channels_create(token, name, is_public))

@APP.route('/channels/listall', methods = ['GET'])
def channel_listall():
    token = request.args.get("token")
    return dumps(channels_listall(token))

@APP.route('/channels/list', methods = ['GET'])
def channel_list():
    token = request.args.get("token")
    return dumps(channels_list(token))

@APP.route('/channels/invite', methods = ['POST'])
def channels_invite():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    #return dumps(channel_id)
    u_id = request.form.get('u_id')
    return dumps(channel_invite(token, channel_id, u_id))

@APP.route('/channel/details', methods = ['GET'])
def channels_details():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    return dumps(channel_details(token, channel_id))
    '''print(channel_details(token, channel_id))
    return dumps({
        'name': "haha",
        'all_members': [],
        'owner_members': []
    })'''

@APP.route('/channel/messages', methods = ['GET'])
def channel_messages():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    return dumps(channels_messages(token, channel_id,start))

@APP.route('/channels/leave', methods = ['POST'])
def channels_leave():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_leave(token, channel_id))

@APP.route('/channel/join', methods = ['POST'])
def channels_join():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    return dumps(channel_join(token, channel_id))

@APP.route('/channels/addowner',methods = ['POST '])
def channels_addowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_addowner(token, channel_id,u_id))

@APP.route('/channels/removeowner',methods = ['POST '])
def channels_removeowner():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    return dumps(channel_removeowner(token, channel_id,u_id))

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
    profile = user_profile(token, u_id)
    #profile['u_id'] = 3
    #profile['profile_img_url'] = 'https://webcms3.cse.unsw.edu.au/static/uploads/coursepic/COMP1531/19T3/f69768934fc5db2bb478f938db95efe98b02af69adc0d4a9e79545d0aae44908/Screenshot_from_2019-09-10_22-16-33.png'
    print(profile)
    return dumps(profile)

@APP.route('/users/profile/setname', methods = ['PUT'])
def user2():
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    user_profile_setname(token,name_first, name_last)
    return dumps({})

@APP.route('/users/profile/setemail', methods = ['PUT'])
def user3():
    token = request.form.get('token')
    email = request.form.get('email')
    user_profile_setmail(token,email)
    return dumps({})

@APP.route('/users/profile/sethandle', methods = ['PUT'])
def user4():
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    user_profile_sethandle(token,handle_str)
    return dumps({})


@APP.route('/users/all', methods = ['GET'])
def user_all():
    token = request.args.get('token')
    return dumps(users_all(token))



@APP.route('/standup/start', methods = ['POST'])
def standup1():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    second = request.form.get('length')
    standup_start(token,channel_id)
    time = showtime(second)
    return dumps(time)

@APP.route('/standup/send', methods = ['POST'])
def standup2():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    standup_send(token,channel_id, message)
    return dumps({})

@APP.route('/standup/active', methods = ['GET'])
def active():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    
    return dumps({
        'is_active': False,
        'time_finish': None
    })


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

@APP.route('/user/profiles/uploadphoto',methods = ['POST'])
def uploadphoto():
    token = request.form.get('token')
    img_url = request.form.get('img_url')
    x_start = request.form.get('x_start')
    y_start = request.form.get('y_start')
    x_end = request.form.get('x_end')
    y_end = request.form.get('y_end')
    user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end)
    id = getUserFromToken(token)
    #return send_from_directory("photo/",str(id)+'.jpg')
    return dumps({})
    
if __name__ == '__main__':
    APP.run()

