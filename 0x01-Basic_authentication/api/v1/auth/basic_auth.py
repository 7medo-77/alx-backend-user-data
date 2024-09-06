#!/usr/bin/env python3
"""
Module which defines a basic auth class
"""
from api.v1.auth.auth import Auth
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
