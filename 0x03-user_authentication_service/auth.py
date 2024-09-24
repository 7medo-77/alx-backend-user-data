#!/usr/bin/env python3
"""
Module which defines authentication methods
"""
import bcrypt


def _hash_password(password):
    """
    Method which returns a salted hash of a password
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())
