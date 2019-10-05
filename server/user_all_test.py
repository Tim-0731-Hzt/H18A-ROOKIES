from user_profile_setname import user_profile_setname

from user_profile_sethandle import user_profile_sethandle 

from user_profile_setemail import user_profile_setemail
from user_profiles_uploadphoto import user_profiles_uploadphoto
import pytest
def test1_user_profile_setname():
    user_profile_setname(123,'Daniel', 'Quin')
def test2_user_profile_setname():
    user_profile_setname(123,'Daniel','bgyerfhuqwdcfcfcfcfcfcfcfafffffffffffffffafafaiffffffffffffffffifififififififififififififi')
def test3_user_profile_setname():
    user_profile_setname(123,'fyhuiawseoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyoyooooooooooso','Quin')

def test1_user_profile_sethandle():
    user_profile_sethandle(123,'sgfdyasgdasygdyuasgdyuasgdugasudguasd')
def test2_user_profile_sethandle():
    user_profile_sethandle(123,'ahsduasd')

def test1_user_profile_setemail():
    user_profile_setemail(123,'goodemail')
def test2_user_profile_setemail():
    user_profile_setemail(123,'bademail')
def test3_user_profile_setemail():
    user_profile_setemail(123,'usedemail')



def test1_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,2,2,2,2)
def test2_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,100,3,3,3,3)
def test3_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,-5,3,877,9237)
def test4_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,600,5,5,5)
def test5_user_profiles_uploadphoto():
    user_profiles_uploadphoto(123,200,3,456,-1,-1)