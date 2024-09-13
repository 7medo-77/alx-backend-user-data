#!/usr/bin/env python3
"""
Module which defines a session auth class
which inherits from auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
from typing import List, TypeVar, Tuple
import base64
import binascii


class SessionAuth(Auth):
    """ Class SessionAuth
    """
    pass
