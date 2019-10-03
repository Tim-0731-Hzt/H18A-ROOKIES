def channel_invite(token, channel_id, u_id):
    pass
    
def test_channel_invite_1():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']


    with pytest.raises(ValueError, match=r"*"):
        channel_invite(token, 'randonNum', u_id2)

    
def test_channel_invite_2():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict2['u_id']
    token2 = authRegisterDict2['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']


    with pytest.raises(ValueError, match=r"*"):
        channel_invite(token, channel_id, '00002')
