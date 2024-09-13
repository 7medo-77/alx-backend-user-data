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
import uuid


class SessionAuth(Auth):
    """ Class SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method to append a new session id and user id
        to class attribute user_id_by_session_id
        """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method to get the user id of
        a particular session by session_id
        """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, session_id: str = None) -> TypeVar('User'):
        """
        Method to get the current user
        instance from the request cookie
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id) if User.get(user_id) else None
