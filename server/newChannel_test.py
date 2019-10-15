import pytest
from channel import channel_invite
from Error import AccessError
import message

# invalid channel_id
def test_channel_invite_1():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 4, "z666")
# invalid user_id
def test_channel_invite_2():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 1,"z777")