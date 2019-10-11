    memberDict = [
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
        },
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
        },
        {
            'u_id': u_id,
            'name_first': first_name,
            'name_last': last_name
        }

    ]
    channelDict = [
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
        },
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
        },
        {
            'channel_id': channel_id,
            'name': name,
            'channel_member': [u_id, u_id, u_id]
        }
    ] 
    messDict = [
        {
            'message_id': messID,
            'u_id': u_id
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
            'message_id': messID,
            'u_id': u_id
            'message': message,
            'time_created': time.ctime(),
            'is_unread': False,
            'reacts': None,
            'is_pinned': False
        },
        {
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