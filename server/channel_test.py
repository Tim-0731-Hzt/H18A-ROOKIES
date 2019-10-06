import channel
from datetime import datetime
import Error
import pytest

# tests for channel_leave_
def test_channel_leave_not_exist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match = r"*"):
                channel_leave(token,channel_id)

def test_channel_leave():
        authRegisterDict = auth_register("TimHu123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        u_id = authRegisterDict["u_id"]
        channel_id = channels_create(token,"COMP1531",True)
        channel_leave(token,channel_id)
        d = channel_details(token,channel_id)
        all_mem =  d[all_members]
        for parts in all_mem.keys():
                if u_id == parts:
                        assert(False)
        


# tests for channel_join
def test_channel_join_notExist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match="*"):
                channel_join(token, channel_id)
def test_channel_join_private():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",False)
        with pytest.raises(AccessError,match="*"):
                channel_join(token, channel_id)
def test_channel_join():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_join(token,channel_id)
        d = channel_details(token,channel_id)
        all_mem =  d[all_members]
        for parts in all_mem.keys():
                if (u_id == parts):
                        pass
        assert(False)

# test for channel_addowner
def test_channel_addowner_notExist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match = r"*"):
                channel_addowner(token,channel_id,u_id)
def test_channel_addowner_alreadyOwner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():

                if (u_id == parts):
                        assert(False)

def test_channel_addowner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_addowner(token, channel_id, u_id)
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():
                if (u_id == parts):
                        pass
        assert(False)

# test for channel_removeowner
def test_channel_removeowner_ChannelNotExist():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match="*"):
                channel_removeowner(token, channel_id, u_id)
def test_channel_removeowner_UserNotExist():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","Tim","hu")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        with pytest.raises(ValueError,match="*"):
                channel_removeowner(token, channel_id, u_id)
def test_channel_removeowner():
        authRegisterDict = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        channel_removeowner(token, channel_id, u_id)
        d = channel_details(token,channel_id)
        owner = d[owner_members]
        for parts in owner.keys():
                if (u_id == parts):
                        assert(False)
        pass
def test_channels_list():
        authRegisterDict1 = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token_1 = authRegisterDict1["token"] 
        channel_id_1 = channels_create(token,"meet up",True)
        u_id_1 = authRegisterDict1["u_id"]
        d1 = channels_list(token_1)
        for parts in d1.keys():
                if (parts == u_id_1 or parts == channel_id_1):
                        pass
        assert(False)
        authRegisterDict2 = auth_register("JashankJeremy@gmail.com","dfvfvsfdsf","jashank","jeremey")
        token_2 = authRegisterDict1["token"] 
        channel_id_2 = channels_create(token,"COMP2521",True)
        u_id_2 = authRegisterDict1["u_id"]
        d2 = channels_list(token_1)
        for parts in d2.keys():
                if (parts == u_id_2 or parts == channel_id_2):
                        pass
        assert(False)
        authRegisterDict3 = auth_register("HaydenSmith@gmail.com","Hayden123","Hayden","Smith")
        token_3 = authRegisterDict1["token"] 
        channel_id_3 = channels_create(token,"COMP2521",True)
        u_id_3 = authRegisterDict1["u_id"]
        d3 = channels_list(token_1)
        for parts in d3.keys():
                if (parts == u_id_3 or parts == channel_id_3):
                        pass
        assert(False)
def test_channels_listall():
        authRegisterDict1 = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token_1 = authRegisterDict1["token"] 
        channel_id_1 = channels_create(token,"meet up",True)
        u_id_1 = authRegisterDict1["u_id"]
        d1 = channels_list(token_1)
        for parts in d1.keys():
                if (parts == u_id_1 or parts == channel_id_1):
                        pass
        assert(False)
        authRegisterDict2 = auth_register("JashankJeremy@gmail.com","dfvfvsfdsf","jashank","jeremey")
        token_2 = authRegisterDict1["token"] 
        channel_id_2 = channels_create(token,"COMP2521",True)
        u_id_2 = authRegisterDict1["u_id"]
        d2 = channels_list(token_1)
        for parts in d2.keys():
                if (parts == u_id_2 or parts == channel_id_2):
                        pass
        assert(False)
        authRegisterDict3 = auth_register("HaydenSmith@gmail.com","Hayden123","Hayden","Smith")
        token_3 = authRegisterDict1["token"] 
        channel_id_3 = channels_create(token,"COMP2521",True)
        u_id_3 = authRegisterDict1["u_id"]
        d3 = channels_list(token_1)
        for parts in d3.keys():
                if (parts == u_id_3 or parts == channel_id_3):
                        pass
        assert(False)
def test_channels_create():
        authRegisterDict = auth_register("zhttim684123@gmail.com","123456","Tim","Hu")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match = r"*"):
                channel_id = channels_create(token,"meet updscsdcdscdscsdcdsdscscddsc",True)
def test_message_sendlater_channelNotExist():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.today()
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1)
def test_message_sendlater_messageTooLong():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.today()
        message = "jomvewiirirjfrijfeijeijeijeijciejiefddcdcdcdcdcdrwrbvasddbcfdsdcmdkcmdkcmdkcmdkcmdcdmcdkcdcmddcddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssskcmdkcmdkcmkdcmdkcmkdcmkdcmkdmcddcdcdcdcdcd"
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1)
def test_message_snedlater_timeInThePast():
        authRegisterDict = auth_register("LebrownJames@gmail.com","James0643","Lebrown","James")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"dad",True)
        u_id = authRegisterDict["u_id"]
        t1 = datetime.date.yesterday()
        with pytest.raises(ValueError,match="*"):
                message_sendlater(token, channel_id, "Hello NBA", t1)

