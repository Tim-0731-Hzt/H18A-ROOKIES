import datetime
import pickle

userDict = [
        {
            'first_name' : None
            'last_name' : None,
            'email' : None,
            'u_id' : None,
            'handle' : None,
            'password' : None,
            'online' : None            
        } 
]
channelDict = [
        {
            'channel_id': None,
            'name': None,
            'channel_member': None,
            'channel_owner': None,
            'is_public': None
        }
]

messDict = [
        {
            'channel_id': None,
            'message_id': None,
            'u_id': None,
            'message': None,
            'time_created': None,
            'is_unread': None,
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