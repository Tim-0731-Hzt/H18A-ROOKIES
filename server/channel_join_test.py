import channels_create
import auth_register
import error
import pytest
import channel_join
import channel_details

def channel_join_notExist():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match="*"):
                channel_join(token, channel_id)
def channel_join_private():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",False)
        with pytest.raises(ValueError,match="*"):
                channel_join(token, channel_id)
def channel_join_test():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        d = {}
        d = channel_details(token,channel_id)
        num = d[owner_members]
        d_new = {}
        channel_join(token,channel_id)
        d_new = channel_details(token,channel_id)
        num_new = d_new[owner_members]
        assert(num_new == num + 1)