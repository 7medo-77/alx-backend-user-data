#!/usr/bin/env python3
"""
Module which defines a session auth class
which inherits from auth
"""
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from flask import request
from os import getenv
from typing import List, TypeVar, Tuple, Dict
import base64
import binascii
from datetime import datetime, timedelta
import uuid


class SessionExpAuth(SessionAuth):
    """ Class SessionAuth
    """
    def __init__(self):
        self.SESSION_DURATION: int = int(getenv('SESSION_DURATION'))\
            if getenv('SESSION_DURATION')\
            and isinstance(int(getenv('SESSION_DURATION')), int)\
            else 0

    def create_session(self, user_id: str=None) -> str:
        """
        Overload of the create_session() of SessionAuth
        Sets the value of self.user_id_by_session_id
        Returns session_id
        """
        session_id: str = super().create_session(user_id)
        if not session_id:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now(),
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """
        Overload of the user_id_for_session_id() of SessionAuth
        Sets the 
        Returns 
        """
        session_dict: Dict = self.user_id_by_session_id.get(session_id)
        if not session_id\
                or not self.user_id_by_session_id.get(session_id)\
                or not session_dict.get('created_at'):
            return None
        if self.SESSION_DURATION <= 0:
            return session_dict.get('user_id')
        time_remaining = datetime.now() - (session_dict.get('created_at') + timedelta(seconds=self.SESSION_DURATION) )
        if time_remaining.seconds > 0:
            return session_dict.get('user_id')
