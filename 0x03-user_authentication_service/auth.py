#!/usr/bin/env python3
"""
Module which defines authentication methods
"""
import bcrypt
from typing import ByteString, TypeVar
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> str:
    """
    Method which returns a salted hash of a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
        self._db._session

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """ Method which returns a user object """
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = str(_hash_password(password))
            return self._db.add_user(email, hashed_password)
