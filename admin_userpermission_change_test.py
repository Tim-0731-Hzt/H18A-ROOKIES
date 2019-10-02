import pytest
from admin_userpermission_change import admin_userpermission_change
def test1_admin_userpermission_change():
    admin_userpermission_change(123456, 1, 1)
def test2_admin_userpermission_change():
    admin_userpermission_change(123456, 2, 1)
def test3_admin_userpermission_change():
    admin_userpermission_change(123456, 3, 1)
def test4_admin_userpermission_change():
    admin_userpermission_change(123456, 1, 2)