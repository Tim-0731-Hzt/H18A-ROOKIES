def channel_messages(token, channel_id, start):
    pass
    
def test_channel_messages():
    authRegisterDict = auth_register('hayden@gmail.com', '123456','hayden','smith')
    u_id = authRegisterDict['u_id']
    token = authRegisterDict['token']

    authRegisterDict = auth_register('jankie@gmail.com', '123456','jankie','lyu')
    u_id2 = authRegisterDict['u_id']
    token2 = authRegisterDict['token']

    channelDict = channels_create(token, 'hayden', True)
    channel_id = channelDict['channel_id']
    
    #test1
        #channel doesn't exist
    with pytest.raises(ValueError, match=r"*"):
        channel_messages(token, 'randonNum', 0)
    
    #test2
        #not a member of channel
    try:
        channel_details(token2, channel_id)
    except AccessError:
        pass
    else:
        raise AssertionError("AccessError was not raised")

    #test3
    channelMessagesDict = channel_messages(token, channel_id, 0)
    startNum = channelMessagesDict['start']
    endNum = channelMessagesDict['end']
    assert startNum == 0
    assert endNum == 49

    #test4

    channelMessagesDict = channel_messages(token, channel_id, 100)
    startNum = channelMessagesDict['start']
    endNum = channelMessagesDict['end']
    assert startNum == 100
    assert endNum == -1
