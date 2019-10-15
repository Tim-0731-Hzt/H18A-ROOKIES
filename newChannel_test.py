from channel import channel_invite
import pytest
from Error import AccessError
import message


def test_channel_invite_1():
        with pytest.raises(ValueError, match=r".*"):
                channel_invite("WDEWDWD", 4, "z666")
