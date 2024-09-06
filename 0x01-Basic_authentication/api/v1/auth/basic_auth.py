#!/usr/bin/env python3
"""
Module which defines a basic auth class
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
from typing import List, TypeVar, Tuple
import base64
import binascii
import re


class BasicAuth(Auth):
    """ Class BasicAuth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """
        Method to extract base64 authorization header from a request
        """
        if not authorization_header or\
                not isinstance(authorization_header, str) or\
                authorization_header[:6] != 'Basic ':
            return None
        else:
            auth_header_binary = authorization_header[6:]
            return auth_header_binary

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """
        Method to decode base64 authorization header from a request
        """
        if not base64_authorization_header or\
                not isinstance(base64_authorization_header, str):
            return None
        else:
            try:
                binary_auth_header = base64_authorization_header.\
                                        encode('utf-8')
                return base64.b64decode(binary_auth_header).decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str]:
        """
        Method to retrieve username and password
        from encoded auth header
        """
        if decoded_base64_authorization_header and\
                isinstance(decoded_base64_authorization_header, str):
            semi_colon = re.findall(r'\:', decoded_base64_authorization_header)
        else:
            semi_colon = []

        if len(semi_colon) == 0 or\
                not isinstance(decoded_base64_authorization_header, str) or\
                not decoded_base64_authorization_header:
            return (None, None)
        else:
            auth_tuple = tuple(decoded_base64_authorization_header.split(':'))
            return auth_tuple

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """
        Method to retreive User instance from
        username and password paarameters
        """
        if (not user_email or isinstance(user_email, str)) or\
                (not user_pwd or isinstance(user_pwd, str)):
            return None
        else:
            # user_list = User.search({'email': user_email})
            user_list = User.search({'email': user_email})
            User.is_valid_password
            is_valid = user_list.is_valid_password(user_pwd)
            if len(user_list) == 0 or\
                    not is_valid:
                return None
            else:
                return user_list[0]
