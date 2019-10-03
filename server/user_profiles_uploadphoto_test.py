import pytest
from user_profiles_uploadphoto import user_profiles_uploadphoto
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