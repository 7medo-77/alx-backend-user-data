#!/usr/bin/env python3
"""
Module which defines authentication methods
"""
import bcrypt
from typing import ByteString


def _hash_password(password: str) -> ByteString:
    """
    Method which returns a salted hash of a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
