#!/usr/bin/env python3
"""
Module which defines authentication methods
"""
import bcrypt
from typing import ByteString, TypeVar
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """
    Method which returns a salted hash of a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Method which validates credentials for login"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
        self._db._session

    # def register_user(self, email: str, password: str) -> User:
    #     """ Registers a user in the database
    #     Returns: User Object
    #     """
    #     try:
    #         user = self._db.find_user_by(email=email)
    #     except NoResultFound:
    #         hashed_password = _hash_password(password)
    #         user = self._db.add_user(email, hashed_password)
    #         return user
    #     else:
    #         raise ValueError(f'User {email} already exists')

    def register_user(self, email: str, password: str) -> User:
        """ Method which returns a user object """
        try:
            user_exists = self._db.find_user_by(email=email)
            if user_exists:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """ Method which validates credentials for login"""
        try:
            user_result = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(),
                                  user_result.hashed_password)
        except NoResultFound:
            return False
