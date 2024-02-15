#!/usr/bin/env python3
"""Auth class"""
import base64
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """_summary_

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if not (authorization_header and isinstance(authorization_header, str)):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """_summary_

        Args:
            base64_authorization_header (str): _description_F

        Returns:
            str: _description_
        """
        if not (
            base64_authorization_header and isinstance(base64_authorization_header, str)
        ):
            return None
        try:
            encoded_header = base64_authorization_header.encode("utf-8")
            b64dc = base64.b64decode(encoded_header)
            return b64dc.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """_summary_

        Args:
            self (_type_): _description_
            str (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not (
            decoded_base64_authorization_header
            and isinstance(decoded_base64_authorization_header, str)
        ):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """_summary_

        Args:
            self (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not (user_email and isinstance(user_email, str)):
            return None
        if not (user_pwd and isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar("User"):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            auth_header = self.authorization_header(request)
            base64_auth_header = self.extract_base64_authorization_header(auth_header)
            decoded_auth_header = self.decode_base64_authorization_header(
                base64_auth_header
            )
            user, pwd = self.extract_user_credentials(decoded_auth_header)
            return self.user_object_from_credentials(user, pwd)
        except Exception:
            return None
