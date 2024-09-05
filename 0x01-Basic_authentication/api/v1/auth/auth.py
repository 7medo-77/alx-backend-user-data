#!/usr/bin/env python3
"""
Module which defines an auth class
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Class Auth for handling authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ method which returns false
        """
        excluded_paths_string_array = [
            re.findall(r'(\w+)+/?', path) for path in excluded_paths
        ]
        if not path or not excluded_paths or len(excluded_paths) == 0:
            return True
        else:
            path_strings = re.findall(r'(\w+)+/?', path)

            if path_strings in excluded_paths_string_array:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """ method which returns None
        """
        if not request or\
                request.headers.get('Authorization') is None:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ method which returns None
        """
        return None
