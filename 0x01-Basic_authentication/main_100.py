#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("H0lberton:School:98!"))
