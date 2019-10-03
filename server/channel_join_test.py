import channels_create
import auth_register
import error
import pytest
import channel_join

def channel_join_notExist():
    channel_id = -1
    authRegisterDict = auth_register("qwerty123@gmail.com","asdffdf","jack","ma")
    token = authRegisterDict["token"]
    with pytest.raises(ValueError,match="*"):
        channel_join()