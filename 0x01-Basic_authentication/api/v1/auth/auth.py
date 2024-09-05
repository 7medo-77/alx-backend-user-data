#!/usr/bin/env python3
"""
Module which defines an auth class
"""
from flask import request
from typing import List


class Auth:
    """ Class Auth for handling authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method which returns false
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ method which returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ method which returns None
        """
        return None
