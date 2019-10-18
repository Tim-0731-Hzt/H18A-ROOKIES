import datetime
memberDict = [
       {
            'u_id': "z666",
            'username':"TimHu",
            'e-mail': "z5210@ad.unsw.edu.au",
            'password': "password"
        },
        {
            'u_id': "z888",
            'username':"JeffLu",
            'e-mail': "z23340@ad.unsw.edu.au",
            'password': "password"
        },
        {
            'u_id': "z123",
            'username':"jackZhang",
            'e-mail': "z4560@ad.unsw.edu.au",
            'password': "password"
        }
]

userDict = [
        {
            'first_name' : "Tim",
            'last_name' : "Hu",
            'email' : "z5210@ad.unsw.edu.au",
            'u_id' : "z666",
            'handle' : "TimHu",
            'password' : "password",
            'token' : "asdf",    
            'online' : True
            
        } ,
        {
            'first_name' : "Jeff",
            'last_name' : "Lu",
            'email' : "z23340@ad.unsw.edu.au",
            'u_id' : "z888",
            'handle' : "JeffLu",
            'password' : "password",
            'token' : "qwert",    
            'online' : True
        },
        {
            'first_name' : "Jack",
            'last_name' : "Zhang",
            'email' : "z4560@ad.unsw.edu.au",
            'u_id' : "z123",
            'handle' : "jackZhang",
            'password': "password",
            'token' : "WDEWDWD",
            'online' : True
        },
        
        {
            'first_name' : "wang",
            'last_name' : "wang",
            'email' : "z4560@ad.unsw.edu.au",
            'u_id' : "zdedx11",
            'handle' : "wangwang",
            'password': "password",
            'token' : "WDEWDWrtyyy",
            'online' : True
            'permission_id': 
        }
]
channelDict = [
        {
            'channel_id': 1,
            'name': "channel_1",
            'channel_member': ["z888"],
            'property':1
        },
        {
            'channel_id': 2,
            'name': "channel_2",
            'channel_member': ["z666"],
            'channel_owner': [1]
            'property':1
        }
]

messDict = [
        {
            'channel_id': 1,
            'message_id': "messID",
            'u_id': u_id,
            'message': ["DCCD","DCDCD   "]
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
            'channel_id': channelID,
            'message_id': messID,
            'u_id': u_id,
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
            'channel_id': channelID,
            'message_id': messID,
            'u_id': u_id,
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        }
]
'''
reactDict = [
        {
            'react_id': react_id, 
            'u_ids': [u_id, u_id, u_id], 
            'is_this_user_reacted': False
        },
        {
            'react_id': react_id, 
            'u_ids': [u_id, u_id, u_id], 
            'is_this_user_reacted': False
        },
        {
            'react_id': react_id, 
            'u_ids': [u_id, u_id, u_id], 
            'is_this_user_reacted': False
        }
]
'''