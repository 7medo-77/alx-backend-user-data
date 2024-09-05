#!/usr/bin/env python3
"""
Module which defines an auth class
"""
from flask import request
from typing import List, TypeVar
import re
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Class BasicAuth
    """
