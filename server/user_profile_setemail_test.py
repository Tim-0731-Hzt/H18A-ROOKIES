import pytest
from user_profile_setemail import user_profile_setemail
def test1_user_profile_setemail():
    user_profile_setemail(123,'goodemail')
def test2_user_profile_setemail():
    user_profile_setemail(123,'bademail')
def test3_user_profile_setemail():
    user_profile_setemail(123,'usedemail')