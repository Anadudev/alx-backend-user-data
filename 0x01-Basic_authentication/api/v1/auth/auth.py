#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        pattern = r"/api/v1/status(/?)"
        if path is None:
            return True
        if re.match(pattern, path):
            for paths in excluded_paths:
                if re.match(pattern, paths):
                    return False
        if path not in excluded_paths:
            return True
        if not excluded_paths:
            return True
        # for string in excluded_paths:
        return False

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if request is None:
            return None
        if "Authorization" not in request.headers.keys():
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None
