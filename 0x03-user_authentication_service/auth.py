#!/usr/bin/env python3
"""
Module which defines authentication methods
"""
import bcrypt
from typing import ByteString


# def _hash_password(password: str) -> str:
#     """ Returns a salted hash of the input password """
#     hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
#     return hashed


def _hash_password(password: str) -> str:
    """
    Method which returns a salted hash of a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
