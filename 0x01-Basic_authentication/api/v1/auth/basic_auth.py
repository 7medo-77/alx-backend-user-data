#!/usr/bin/env python3
"""
Module which defines a basic auth class
"""
from flask import request
from typing import List, TypeVar
import base64
import binascii
from api.v1.auth.auth import Auth


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
                binary_auth_header = base64_authorization_header.encode('utf-8')
                return base64.b64decode(binary_auth_header).decode('utf-8')
            except binascii.Error:
                return None
