import pytest

import pytest
from server.Error import AccessError, ValueError
from server.auth_pickle import *
import server.pickle_unpickle
from server.channel import *

from server.admin_userpermission_change import admin_userpermission_change



def test1_admin_userpermission_change():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']
    with pytest.raises(ValueError,match = r".*"):

        admin_userpermission_change(token1,-1,2)

def test2_admin_userpermission_change():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']

    with pytest.raises(ValueError, match=r".*"):

        admin_userpermission_change(token1, 2, -1)
def test3_admin_userpermission_change():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']
    admin_userpermission_change(token1,2,2)
    with pytest.raises(AccessError, match=r".*"):

        admin_userpermission_change(token2, 3, 1)
def test4_admin_userpermission_change():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']
    with pytest.raises(AccessError, match=r".*"):

        admin_userpermission_change(token3, 2, 3)
def test5_admin_userpermission_change():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']
    admin_userpermission_change(token1,2,2)
    with pytest.raises(AccessError, match=r".*"):

        admin_userpermission_change(token2, 1, 2)
def test6():
    restart()
    authRegisterDict1 = auth_register(
        "zhttim684123@gmail.com", "123456", "Tim", "Hu")
    token1 = authRegisterDict1["token"]
    UID1 = authRegisterDict1['u_id']
    authRegisterDict2 = auth_register(
        "HaydenSmith@gmail.com", "1we33456", "Hayden", "Smith")
    token2 = authRegisterDict2["token"]
    UID2 = authRegisterDict2['u_id']
    authRegisterDict3 = auth_register(
        "Luhaodong@gmail.com", "1we33ee456", "Jeff", "Lu")
    token3 = authRegisterDict3["token"]

    UID3 = authRegisterDict3['u_id']

    authRegisterDict4 = auth_register(
        "quin@gmail.com", "jijijij37236", 'daniel', 'quin')
    token4 = authRegisterDict4["token"]

    UID4 = authRegisterDict4['u_id']
    admin_userpermission_change(token1,3,2)
    admin_userpermission_change(token1,2,1)
    admin_userpermission_change(token2,4,1)
    userDict = load()['userDict']
    assert userDict[1]['permission_id'] == 1
    assert userDict[2]['permission_id'] == 2
    assert userDict[3]['permission_id'] == 1
