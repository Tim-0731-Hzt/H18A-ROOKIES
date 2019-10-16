memberDict = [
       {
            'u_id': "z666",
            'username':"TimHu",
            'e-mail': z5210@ad.unsw.edu.au,
            'password': "password"
        },
        {
            'u_id': "z888",
            'username':"JeffLu",
            'e-mail': z23340@ad.unsw.edu.au,
            'password': "password"
        },
        {
            'u_id': "z123",
            'username':"jackZhang",
            'e-mail': z4560@ad.unsw.edu.au,
            'password': "password"
        },
    ]
channelDict = [
        {
            'channel_id': 1,
            'name': "channel_1",
            'channel_member': ["z518"],
            'channel_owner': [3]
        },
        {
            'channel_id': 2,
            'name': "channel_2",
            'channel_member': ["z521"],
            'channel_owner': [1]
        }
    ]
    messDict = [
        {
            'channel_id': channelID,
            'message_id': messID,
            'u_id': u_id
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
            'channel_id': channelID,
            'message_id': messID,
            'u_id': u_id
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
            'channel_id': channelID,
            'message_id': messID,
            'u_id': u_id
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        }
    ]
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
