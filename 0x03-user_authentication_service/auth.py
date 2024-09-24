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

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user in the database
        Returns: User Object
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    # def register_user(self, email: str, password: str) -> TypeVar('User'):
    #     """ Method which returns a user object """
    #     # self._db._session
    #     try:
    #         user_exists = self._db.find_user_by(email=email)
    #         if user_exists:
    #             raise ValueError('User {} already exists'.format(email))
    #     except NoResultFound:
    #         hashed_password = _hash_password(password)
    #         return self._db.add_user(email, hashed_password)
