import pytest
import channel_leave
import channels_create
import auth_register
import channel_details
import error
def channel_leave_not_exist():
    channel_id = -1
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    with pytest.raises(ValueError,match = r"*")
            channel_leave(token,channel_id)

def channel_leave_test1():
    authRegisterDict = auth_register("TimHu123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    channel_id = channels_create(token,"COMP1531",True)
    d = {}
    channel_leave(token,channel_id)
    d = channel_details(token,channel_id)
    all_mem =  d_new[owner_members]
    assert (num -1 == num_new)