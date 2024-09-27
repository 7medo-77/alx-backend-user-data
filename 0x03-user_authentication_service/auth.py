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

    def create_session(self, email: str) -> str:
        """Method which creates a session_ID
        and adds it to a cookie"""
        try:
            user_result = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        new_session = _generate_uuid()
        self._db.update_user(user_result.id, session_id=new_session)
        return new_session

    def get_user_from_session_id(self, session_id: str) -> User:
        """Method which retrieves a User from session_id"""
        try:
            result_user = self._db.find_user_by(session_id=session_id)
            return result_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """Method which retrieves a User from session_id"""
        try:
            result_user = self._db.find_user_by(user_id=user_id)
            setattr(result_user, 'session_id', None)
            return None
        except NoResultFound:
            return None
