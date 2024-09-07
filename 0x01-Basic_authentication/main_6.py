#!/usr/bin/env python3
""" Main 6
"""
import base64
import uuid
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "bob@hbtn.io"
user_clear_pwd = "H0lbertonSchool98!"
user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()

"""
Create another user
"""
user_2_email = "holberton_2@gmail.com"
user_2_clear_pwd = "non_encrypted_password"
user_2 = User()
user_2.email = user_2_email
user_2.first_name = "SomeName"
user_2.last_name = "lastName"
user_2.password = user_2_clear_pwd
print("New user: {}".format(user_2.display_name()))
user_2.save()

basic_clear = "{}:{}".format(user_2_email, user_2_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

