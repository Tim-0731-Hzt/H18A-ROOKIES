import pytest
import channel_leave
import channels_create
import auth_register
import error
def channel_leave_not_exist():
    channel_id = -1
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    with pytest.raises(ValueError,match="*"):
        channel_leave(token,channel_id)
def channel_leave_test1():
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    channel_id = channels_create(token,"COMP1531",True)
    assert(channel_leave(token,channel_id) == {})
