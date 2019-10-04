from channel import channels_create
from channel import channel_details
from channel import channel_join
from channel import channel_leave
from channel import auth_register
import error
import pytest

# tests for channel_leave
def channel_leave_not_exist():
    channel_id = -1
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    with pytest.raises(ValueError,match = r"*"):
            channel_leave(token,channel_id)

def channel_leave_test1():
    authRegisterDict = auth_register("TimHu123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    u_id = authRegisterDict["u_id"]
    channel_id = channels_create(token,"COMP1531",True)
    d = {}
    channel_leave(token,channel_id)
    d = channel_details(token,channel_id)
    all_mem = {}
    all_mem =  d[all_members]
    for parts in all_mem:
        if (u_id == parts):
            assert(False)
    pass


# tests for channel_join
def channel_join_notExist_test():
        channel_id = -1
        authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        with pytest.raises(ValueError,match="*"):
                channel_join(token, channel_id)
def channel_join_private_test():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",False)
        with pytest.raises(AccessError,match="*"):
                channel_join(token, channel_id)
def channel_join_test():
        authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
        token = authRegisterDict["token"]
        channel_id = channels_create(token,"meet up",True)
        u_id = authRegisterDict["u_id"]
        d = {}
        channel_join(token,channel_id)
        d = channel_details(token,channel_id)
        all_mem = {}
        all_mem =  d[all_members]
        for parts in all_mem:
                if (u_id == parts):
                        pass
        assert(False)

# test for channel_addowner
def channel_addowner_notExist_test():
    channel_id = -1
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    u_id = authRegisterDict["u_id"]
    with pytest.raises(ValueError,match = r"*"):
            channel_addowner(token,channel_id,u_id)
def channel_addowner_alreadyOwner_test():
    authRegisterDict = auth_register("zhttim684123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    channel_id = channels_create(token,"meet up",True)
    