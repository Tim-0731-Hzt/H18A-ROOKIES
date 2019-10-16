    memberDict = [
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
            'e-mail': e-mail
            'password': password
        },
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
            'e-mail': e-mail
            'password': password
        },
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
            'e-mail': e-mail
            'password': password
        }

    ]
    channelDict = [
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
            'channel_owner': [u_id, u_id, u_id]
        },
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
            'channel_owner': [u_id, u_id, u_id]
        },
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
            'channel_owner': [u_id, u_id, u_id]
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