#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar
import re
from os import getenv

class Auth:
    """Class that implements user authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method that validates and authenticates a url

        Args:
            path (str): url path check
            excluded_paths (List[str]): list of excluded url path

        Returns:
            bool: _description_
        """

        pattern = r"/api/v1/status(/?)"
        if not(path and excluded_paths):
            return True
        if path in excluded_paths:
            return False
        if re.match(pattern, path):
            for paths in excluded_paths:
                if re.match(pattern, paths):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Method that implements a request header

        Args:
            request (_type_, optional): flask request object. Defaults to None.

        Returns:
            str: _description_
        """
        if request is None:
            return None
        if "Authorization" not in request.headers.keys():
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """Method that gets the current user

        Returns:
            _type_: _description_
        """
        return None
    def session_cookie(self, request=None):
        if not request:
            return None
        SESSION_NAME = getenv("SESSION_NAME")
        return request.cookies.get(SESSION_NAME)
