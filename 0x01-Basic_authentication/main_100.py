#!/usr/bin/env python3
""" Main 4
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User


# ba = BasicAuth()
# res1, res2 = ba.extract_user_credentials("Holberton:HBTN:is:so:cool")
# if res1 is None:
#     print("extract_user_credentials must return the first part of 'decoded_base64_authorization_header' (separated by ':')")
#     exit(1)
# if res2 is None:
#     print("extract_user_credentials must return the last part of 'decoded_base64_authorization_header' (separated by ':')")
#     exit(1)
#
# if res1 != "Holberton":
#     print("Wrong first part of 'decoded_base64_authorization_header': {}".format(res1))
#     exit(1)
# if res2 != "HBTN:is:so:cool":
#     print("Wrong second part of 'decoded_base64_authorization_header': {}".format(res1))
#     exit(1)
# print("OK", end="")

# ba = BasicAuth()
# res1, res2 = ba.extract_user_credentials("Holberton:HBTN:iscool")
# if res1 is None:
#     print("extract_user_credentials must return the first part of 'decoded_base64_authorization_header' (separated by ':')")
#     exit(1)
# if res2 is None:
#     print("extract_user_credentials must return the last part of 'decoded_base64_authorization_header' (separated by ':')")
#     exit(1)
#
# if res1 != "Holberton":
#     print("Wrong first part of 'decoded_base64_authorization_header': {}".format(res1))
#     exit(1)
# if res2 != "HBTN:iscool":
#     print("Wrong second part of 'decoded_base64_authorization_header': {}".format(res1))
#     exit(1)
#
# print("OK", end="")

# a = BasicAuth()
# print(a.extract_user_credentials("Holberton:School"))
# print(a.extract_user_credentials("H0lberton:School:98!"))
# print(a.extract_user_credentials("Holberton:HBTN:is:so:cool"))

""" Create a user test """
user_email = "bob100@hbtn.io"
user_clear_pwd = "H0lberton:School:98!"

user = User()
user.email = user_email
user.password = user_clear_pwd
print("New user: {}".format(user.id))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
